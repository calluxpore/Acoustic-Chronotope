import streamlit as st
import os
import tempfile
import base64
from engine import process_memory_spark, clean_keywords, generate_soundscape
from styles import (
    custom_css, HEADER_HTML, DEFAULT_BANNER_SVG, get_image_banner_html
)

# Set page configuration to clean centered layout
st.set_page_config(
    page_title="Acoustic Chronotope",
    page_icon="⏳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state keys
if 'audio_generated' not in st.session_state:
    st.session_state.audio_generated = False
if 'keywords' not in st.session_state:
    st.session_state.keywords = ""
if 'last_text' not in st.session_state:
    st.session_state.last_text = ""
if 'last_file' not in st.session_state:
    st.session_state.last_file = None
if 'generated_mode' not in st.session_state:
    st.session_state.generated_mode = None
if 'generated_image_uri' not in st.session_state:
    st.session_state.generated_image_uri = None
if 'text_draft' not in st.session_state:
    st.session_state.text_draft = ""
if 'clicked_trigger' not in st.session_state:
    st.session_state.clicked_trigger = False

# Render Custom CSS styles
st.markdown(custom_css, unsafe_allow_html=True)

# Render Header Section
st.markdown(HEADER_HTML, unsafe_allow_html=True)

# Helper function to get icons for keyword tags dynamically
def get_keyword_icon(keyword):
    k = keyword.lower()
    if any(word in k for word in ["bird", "chirp", "sing", "avian"]):
        return "🐦"
    elif any(word in k for word in ["leaf", "rustl", "tree", "forest", "wood", "foliage", "branch", "woodland"]):
        return "🍂"
    elif any(word in k for word in ["wind", "breeze", "air", "gale", "draft"]):
        return "💨"
    elif any(word in k for word in ["rain", "drizzl", "shower", "wet", "water"]):
        return "🌧️"
    elif any(word in k for word in ["thunder", "storm", "lightn"]):
        return "⛈️"
    elif any(word in k for word in ["ocean", "wave", "sea", "beach", "tide"]):
        return "🌊"
    elif any(word in k for word in ["fire", "crackl", "burn", "camp"]):
        return "🔥"
    elif any(word in k for word in ["clock", "tick", "ticking", "time"]):
        return "⏳"
    elif any(word in k for word in ["cricket", "insect", "buzz"]):
        return "🦗"
    elif any(word in k for word in ["cloud", "fog", "mist"]):
        return "☁️"
    return "✨"

# Helper function to safely compare Streamlit UploadedFile objects
def files_are_equal(f1, f2):
    if f1 is None and f2 is None:
        return True
    if f1 is None or f2 is None:
        return False
    return getattr(f1, 'name', '') == getattr(f2, 'name', '') and getattr(f1, 'size', 0) == getattr(f2, 'size', 0)

# INPUT CARD SECTION
st.markdown('<div class="app-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Memory Trace Input</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Describe a moment, place, or memory to generate ambient audio.</div>', unsafe_allow_html=True)

# Select between Text and Image
mode = st.radio("Memory Source", ["✏️ Text", "📷 Image"], horizontal=True, label_visibility="collapsed")

text_mem = ""
uploaded_img = None

if "Text" in mode:
    text_mem = st.text_area(
        label="Write a memory fragment...",
        placeholder="Describe a moment in time, sensory details, weather, or location...",
        value=st.session_state.text_draft,
        max_chars=500,
        height=140,
        label_visibility="collapsed",
        key="text_mem_input"
    )
    st.session_state.text_draft = text_mem
else:
    uploaded_img = st.file_uploader(
        label="Upload a photograph...",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
        key="uploaded_img_input"
    )
    if uploaded_img is not None:
        # Simple native preview
        st.image(uploaded_img, caption=uploaded_img.name, width=220)

# Tip Box
st.markdown("""
<div class="tip-box">
    💡 <strong>Tip:</strong> Be descriptive. Include environmental sounds, weather conditions, location details, and textures for the best audio generation results.
</div>
""", unsafe_allow_html=True)

# Trigger Button
trigger = st.button("Trigger Memory Spark", key="trigger_spark", use_container_width=True)
if trigger:
    # Validation
    if "Text" in mode and not text_mem.strip():
        st.error("Please describe a memory fragment to trigger the soundscape.")
    elif "Image" in mode and uploaded_img is None:
        st.error("Please upload a photograph to trigger the soundscape.")
    else:
        st.session_state.clicked_trigger = True
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)


# Reset audio state if user modifies input text or upload file of the generated mode
should_reset = False
if st.session_state.audio_generated:
    if "Text" in st.session_state.generated_mode:
        if "Text" in mode and text_mem != st.session_state.last_text:
            should_reset = True
    elif "Image" in st.session_state.generated_mode:
        if "Image" in mode and uploaded_img is not None and not files_are_equal(uploaded_img, st.session_state.last_file):
            should_reset = True

if should_reset:
    st.session_state.audio_generated = False
    st.session_state.keywords = ""
    st.session_state.generated_mode = None
    st.session_state.generated_image_uri = None


# RIGHT PAGE: SYNTHESIS & OUTPUTS (manifests immediately below inputs in a clean container)
if st.session_state.clicked_trigger or st.session_state.audio_generated:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Acoustic Canvas</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Your memory, reimagined as ambient sound.</div>', unsafe_allow_html=True)
    
    if st.session_state.clicked_trigger:
        try:
            keywords_extracted = ""
            
            # Phase 1: Sensing the memory texture (Ollama LLM)
            with st.spinner("Sensing the memory texture..."):
                if uploaded_img is not None:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                        tmp_file.write(uploaded_img.getvalue())
                        tmp_file_path = tmp_file.name
                    
                    try:
                        keywords_extracted = process_memory_spark(image_path=tmp_file_path)
                    finally:
                        if os.path.exists(tmp_file_path):
                            os.remove(tmp_file_path)
                else:
                    keywords_extracted = process_memory_spark(text_input=text_mem)
            
            if not keywords_extracted:
                st.error("No keywords could be extracted from the memory spark. Please try again.")
                st.session_state.clicked_trigger = False
            else:
                keywords_clean = clean_keywords(keywords_extracted)
                
                # Phase 2: Crafting the sound waves (AudioCraft AudioGen)
                with st.spinner("Crafting the sound waves..."):
                    audio_file = generate_soundscape(keywords_clean)
                
                st.session_state.keywords = keywords_clean
                st.session_state.audio_generated = True
                st.session_state.generated_mode = mode
                st.session_state.last_text = text_mem
                st.session_state.last_file = uploaded_img
                if "Image" in mode and uploaded_img is not None:
                    bytes_data = uploaded_img.getvalue()
                    base_64_str = base64.b64encode(bytes_data).decode('utf-8')
                    mime_type = uploaded_img.type
                    st.session_state.generated_image_uri = f"data:{mime_type};base64,{base_64_str}"
                else:
                    st.session_state.generated_image_uri = None
                st.session_state.clicked_trigger = False
                st.rerun()
                
        except Exception as e:
            st.error(f"An error occurred during processing: {str(e)}")
            st.session_state.clicked_trigger = False

    elif st.session_state.audio_generated:
        # If an image was uploaded, render it in the banner frame. Otherwise, show the default vector banner SVG.
        if "Image" in st.session_state.generated_mode and st.session_state.generated_image_uri:
            st.markdown(get_image_banner_html(st.session_state.generated_image_uri), unsafe_allow_html=True)
        else:
            st.markdown(DEFAULT_BANNER_SVG, unsafe_allow_html=True)
        
        st.markdown('<div class="keywords-label">Extracted Sensory Textures</div>', unsafe_allow_html=True)
        
        # Display individual keyword tags with matching emojis
        keywords_list = [k.strip() for k in st.session_state.keywords.split(',') if k.strip()]
        tags_html = "".join([f'<span class="keyword-tag">{get_keyword_icon(k)} {k}</span>' for k in keywords_list])
        st.markdown(f'<div class="output-keywords-container">{tags_html}</div>', unsafe_allow_html=True)
        
        # Audio player
        if os.path.exists('output_memory.wav'):
            st.audio('output_memory.wav', format='audio/wav')
        else:
            st.error("Soundscape generation completed, but output file was not found.")
            
        # Action Buttons Row
        st.markdown('<div style="margin-top: 1.2rem;"></div>', unsafe_allow_html=True)
        col_act_l, col_act_r = st.columns([1, 1])
        with col_act_l:
            reset = st.button("Reset Memory Spark", use_container_width=True)
            if reset:
                st.session_state.audio_generated = False
                st.session_state.keywords = ""
                st.session_state.generated_mode = None
                st.session_state.generated_image_uri = None
                st.session_state.last_text = ""
                st.session_state.last_file = None
                st.rerun()
        with col_act_r:
            if os.path.exists('output_memory.wav'):
                with open('output_memory.wav', 'rb') as f:
                    st.download_button(
                        label="Download Soundscape",
                        data=f,
                        file_name="output_memory.wav",
                        mime="audio/wav",
                        use_container_width=True
                    )

    st.markdown('</div>', unsafe_allow_html=True)


# Footer row with columns and icons
st.markdown('<div style="margin-top: 2.5rem; border-top: 1px solid rgba(214, 123, 98, 0.15); padding-top: 1.5rem;"></div>', unsafe_allow_html=True)
f_col1, f_col2, f_col3, f_col4 = st.columns(4)
with f_col1:
    st.markdown("""
    <div class="footer-feature">
        <div class="footer-icon">〰️</div>
        <div>
            <div class="footer-title">Sensory Translation</div>
            <div class="footer-subtitle">Converts memories into rich ambient textures.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with f_col2:
    st.markdown("""
    <div class="footer-feature">
        <div class="footer-icon">🍃</div>
        <div>
            <div class="footer-title">Nature-Inspired</div>
            <div class="footer-subtitle">Grounded in organic, real-world soundscapes.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with f_col3:
    st.markdown("""
    <div class="footer-feature">
        <div class="footer-icon">❤️</div>
        <div>
            <div class="footer-title">Emotional Resonance</div>
            <div class="footer-subtitle">Captures the feeling behind the memory.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with f_col4:
    st.markdown("""
    <div class="footer-feature">
        <div class="footer-icon">☁️</div>
        <div>
            <div class="footer-title">Personal & Ambient</div>
            <div class="footer-subtitle">Designed for reflection, focus, and calm.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
