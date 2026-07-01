# Custom CSS for the Editorial Warm Minimalist style
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');

/* Hide default Streamlit visual headers/footers */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Adjust outer layout block spacing and width to be single-column and readable */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 720px !important;
    margin: 0 auto !important;
}

/* Remove Streamlit default header bar decoration */
div[data-testid="stDecoration"] {
    background-image: none !important;
    background-color: transparent !important;
}
div[data-testid="stAppHeader"] {
    background-color: transparent !important;
}

/* Main App Page Background and Base Font */
.stApp, .stAppHeader, .stMain {
    background-color: #FBF9F6 !important;
    color: #2C2A29 !important;
    font-family: 'Inter', sans-serif !important;
}

/* Heading Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Lora', Georgia, serif !important;
    color: #2C2A29 !important;
}

/* Clean title block */
.journal-header {
    text-align: center;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(214, 123, 98, 0.15);
    margin-bottom: 1.8rem;
}
.journal-title {
    font-size: 2.6rem !important;
    font-weight: 700;
    color: #D67B62 !important;
    margin: 0;
    letter-spacing: -0.8px;
}
.journal-subtitle {
    font-family: 'Lora', Georgia, serif !important;
    font-style: italic;
    font-size: 1.05rem;
    color: #5C5856;
    margin-top: 0.4rem;
}

/* Clean block container borders */
.app-card {
    background-color: #FFFFFF !important;
    border: 1px solid rgba(44, 42, 41, 0.08) !important;
    border-radius: 12px !important;
    padding: 1.8rem !important;
    box-shadow: 0 4px 20px rgba(44, 42, 41, 0.02) !important;
    margin-bottom: 1.5rem !important;
}

/* Section headings */
.section-title {
    font-family: 'Lora', Georgia, serif !important;
    font-size: 1.35rem !important;
    font-weight: 700 !important;
    color: #2C2A29 !important;
    margin-bottom: 0.3rem !important;
}
.section-subtitle {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    color: #8C8682 !important;
    margin-bottom: 1.2rem !important;
}

/* Custom Terracotta Trigger Button */
div.stButton > button {
    background-color: #D67B62 !important;
    color: #FFFFFF !important;
    border: 1px solid #D67B62 !important;
    border-radius: 24px !important;
    padding: 0.6rem 1.8rem !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    box-shadow: 0 4px 12px rgba(214, 123, 98, 0.15) !important;
    transition: all 0.25s ease !important;
}
div.stButton > button:hover {
    background-color: #C56950 !important;
    border-color: #C56950 !important;
    box-shadow: 0 6px 16px rgba(214, 123, 98, 0.25) !important;
}

/* Clean text tags */
.keyword-tag {
    background-color: #F8F4F0 !important;
    color: #5C5856 !important;
    padding: 0.4rem 0.9rem !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    margin: 0.25rem 0.4rem 0.25rem 0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    border: 1px solid rgba(214, 123, 98, 0.08) !important;
}
.keywords-label {
    font-family: 'Lora', Georgia, serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    color: #2C2A29 !important;
    margin-top: 1rem !important;
    margin-bottom: 0.5rem !important;
}

/* Photo/Image Banner styling */
.banner-image-container {
    width: 100% !important;
    height: 220px !important;
    border-radius: 8px !important;
    border: 1px solid rgba(44, 42, 41, 0.08) !important;
    overflow: hidden !important;
    margin-bottom: 1rem !important;
}
.banner-image-element {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
}

/* Clean Tip Box */
.tip-box {
    background-color: #F8F4F0 !important;
    border: 1px solid rgba(214, 123, 98, 0.12) !important;
    border-radius: 8px !important;
    padding: 0.5rem 0.8rem !important;
    font-size: 0.8rem !important;
    color: #5C5856 !important;
    margin-top: 0.5rem !important;
    margin-bottom: 1rem !important;
}

/* Custom styled sub-sections for footer features */
.footer-feature {
    display: flex !important;
    align-items: flex-start !important;
    gap: 12px !important;
    padding: 0.5rem 0 !important;
}
.footer-icon {
    background-color: #F3ECE6 !important;
    border-radius: 50% !important;
    width: 32px !important;
    height: 32px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 0.9rem !important;
    flex-shrink: 0 !important;
    border: 1px solid rgba(44, 42, 41, 0.04) !important;
}
.footer-title {
    font-family: 'Lora', Georgia, serif !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    color: #2C2A29 !important;
}
.footer-subtitle {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.74rem !important;
    color: #6C6865 !important;
    line-height: 1.3 !important;
}

/* Custom Segmented Radio Buttons (Text / Image) */
div[data-testid="stRadio"] {
    margin-bottom: 0.8rem !important;
    width: 100% !important;
    display: flex !important;
    justify-content: flex-start !important;
}
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: row !important;
    justify-content: flex-start !important;
    gap: 0.2rem !important;
    background-color: #FAF8F5 !important;
    padding: 4px !important;
    border-radius: 24px !important;
    border: 1px solid rgba(44, 42, 41, 0.06) !important;
    width: 100% !important;
    max-width: 320px !important;
}
div[data-testid="stRadio"] > div[role="radiogroup"] label {
    flex: 1 1 0% !important;
    text-align: center !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    padding: 6px 14px !important;
    margin: 0 !important;
    border-radius: 20px !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
    background-color: transparent !important;
    color: rgba(44, 42, 41, 0.5) !important; /* Visible but dim by default */
}
/* Hide default radio check circle icon */
div[data-testid="stRadio"] > div[role="radiogroup"] label > div:first-child {
    display: none !important;
}
div[data-testid="stRadio"] > div[role="radiogroup"] label p,
div[data-testid="stRadio"] > div[role="radiogroup"] label span {
    color: rgba(44, 42, 41, 0.5) !important; /* Visible but dim by default */
    transition: all 0.25s ease !important;
}
/* Selected state using modern :has selector */
div[data-testid="stRadio"] > div[role="radiogroup"] label:has(input:checked) {
    background-color: #D67B62 !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 10px rgba(214, 123, 98, 0.15) !important;
}
div[data-testid="stRadio"] > div[role="radiogroup"] label:has(input:checked) span,
div[data-testid="stRadio"] > div[role="radiogroup"] label:has(input:checked) div,
div[data-testid="stRadio"] > div[role="radiogroup"] label:has(input:checked) p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}
/* Hover effect for unselected items */
div[data-testid="stRadio"] > div[role="radiogroup"] label:not(:has(input:checked)):hover {
    color: rgba(44, 42, 41, 0.8) !important;
}
div[data-testid="stRadio"] > div[role="radiogroup"] label:not(:has(input:checked)):hover p,
div[data-testid="stRadio"] > div[role="radiogroup"] label:not(:has(input:checked)):hover span {
    color: rgba(44, 42, 41, 0.8) !important;
}
</style>
"""

# Journal Header HTML
HEADER_HTML = """
<div class="journal-header">
    <h1 class="journal-title">Acoustic Chronotope</h1>
    <p class="journal-subtitle">Transforming visual and textual memory traces into local ambient soundscapes.</p>
</div>
"""

# Hand-crafted vector banner SVG with bird and soundwave
DEFAULT_BANNER_SVG = """
<svg viewBox="0 0 800 240" width="100%" height="auto" style="border-radius: 12px; border: 1px solid rgba(44,42,41,0.08); display: block;" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E2E5D5" />
      <stop offset="40%" stop-color="#EBE8D8" />
      <stop offset="100%" stop-color="#F2ECD9" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="240" fill="url(#bgGrad)" />
  
  <!-- Branch and Leaves -->
  <path d="M0,230 Q120,200 200,160 T350,110 T460,95" fill="none" stroke="#7C8367" stroke-width="4" stroke-linecap="round" opacity="0.85" />
  
  <!-- Secondary branches -->
  <path d="M100,205 Q70,160 50,140" fill="none" stroke="#7C8367" stroke-width="2.5" stroke-linecap="round" opacity="0.8" />
  <path d="M150,183 Q160,130 140,95" fill="none" stroke="#7C8367" stroke-width="2.5" stroke-linecap="round" opacity="0.8" />
  <path d="M250,145 Q280,110 270,80" fill="none" stroke="#7C8367" stroke-width="2" stroke-linecap="round" opacity="0.8" />
  <path d="M300,128 Q330,150 360,160" fill="none" stroke="#7C8367" stroke-width="2" stroke-linecap="round" opacity="0.8" />
  
  <!-- Leaves -->
  <path d="M50,140 Q40,120 55,115 Q65,130 50,140 Z" fill="#909A7C" opacity="0.9" />
  <path d="M60,145 Q70,125 80,135 Q75,150 60,145 Z" fill="#A5B091" opacity="0.9" />
  <path d="M80,175 Q60,170 70,160 Q90,165 80,175 Z" fill="#7C8367" opacity="0.9" />
  <path d="M140,95 Q125,85 135,75 Q150,85 140,95 Z" fill="#909A7C" opacity="0.9" />
  <path d="M145,110 Q165,100 160,90 Q145,100 145,110 Z" fill="#A5B091" opacity="0.9" />
  <path d="M155,145 Q175,140 180,150 Q165,160 155,145 Z" fill="#7C8367" opacity="0.9" />
  <path d="M220,152 Q210,135 225,130 Q235,145 220,152 Z" fill="#909A7C" opacity="0.9" />
  <path d="M270,80 Q255,75 260,65 Q275,70 270,80 Z" fill="#A5B091" opacity="0.9" />
  <path d="M275,95 Q295,85 290,75 Q275,85 275,95 Z" fill="#7C8367" opacity="0.9" />
  <path d="M330,115 Q340,95 350,105 Q345,120 330,115 Z" fill="#909A7C" opacity="0.9" />
  <path d="M390,103 Q410,95 405,85 Q390,95 390,103 Z" fill="#A5B091" opacity="0.9" />
  <path d="M430,98 Q440,82 450,90 Q440,102 430,98 Z" fill="#7C8367" opacity="0.9" />

  <!-- Bird -->
  <line x1="416" y1="96" x2="416" y2="104" stroke="#48443B" stroke-width="2" />
  <line x1="422" y1="95" x2="422" y2="103" stroke="#48443B" stroke-width="2" />
  <path d="M385,115 L405,102 L395,95 Z" fill="#585245" />
  <path d="M400,100 C405,80 435,80 438,98 C438,110 415,115 400,100 Z" fill="#6A6253" />
  <circle cx="434" cy="85" r="9" fill="#6A6253" />
  <path d="M443,84 L451,86 L443,89 Z" fill="#D67B62" />
  <circle cx="432" cy="83" r="1.5" fill="#FFF" />
  
  <!-- Bird Song Wave Overlay -->
  <path d="M447,85 Q485,75 515,105 T575,118" fill="none" stroke="#D67B62" stroke-width="2.5" stroke-dasharray="1 5" stroke-linecap="round" opacity="0.75" />
  
  <!-- Soundwave Bars -->
  <g transform="translate(565, 115)" fill="#D67B62">
    <rect x="0" y="-12" width="3" height="24" rx="1.5" opacity="0.5" />
    <rect x="7" y="-8" width="3" height="16" rx="1.5" opacity="0.45" />
    <rect x="14" y="-18" width="3" height="36" rx="1.5" opacity="0.55" />
    <rect x="21" y="-28" width="3" height="56" rx="1.5" opacity="0.7" />
    <rect x="28" y="-15" width="3" height="30" rx="1.5" opacity="0.6" />
    <rect x="35" y="-6" width="3" height="12" rx="1.5" opacity="0.4" />
    <rect x="42" y="-22" width="3" height="44" rx="1.5" opacity="0.65" />
    <rect x="49" y="-35" width="3" height="70" rx="1.5" opacity="0.8" />
    <rect x="56" y="-25" width="3" height="50" rx="1.5" opacity="0.75" />
    <rect x="63" y="-10" width="3" height="20" rx="1.5" opacity="0.5" />
    <rect x="70" y="-18" width="3" height="36" rx="1.5" opacity="0.55" />
    <rect x="77" y="-30" width="3" height="60" rx="1.5" opacity="0.75" />
    <rect x="84" y="-20" width="3" height="40" rx="1.5" opacity="0.65" />
    <rect x="91" y="-8" width="3" height="16" rx="1.5" opacity="0.45" />
    <rect x="98" y="-15" width="3" height="30" rx="1.5" opacity="0.55" />
    <rect x="105" y="-26" width="3" height="52" rx="1.5" opacity="0.7" />
    <rect x="112" y="-12" width="3" height="24" rx="1.5" opacity="0.5" />
    <rect x="119" y="-5" width="3" height="10" rx="1.5" opacity="0.35" />
    <rect x="126" y="-18" width="3" height="36" rx="1.5" opacity="0.6" />
    <rect x="133" y="-25" width="3" height="50" rx="1.5" opacity="0.7" />
    <rect x="140" y="-14" width="3" height="28" rx="1.5" opacity="0.55" />
    <rect x="147" y="-6" width="3" height="12" rx="1.5" opacity="0.4" />
    <rect x="154" y="-20" width="3" height="40" rx="1.5" opacity="0.65" />
    <rect x="161" y="-28" width="3" height="56" rx="1.5" opacity="0.75" />
    <rect x="168" y="-16" width="3" height="32" rx="1.5" opacity="0.55" />
    <rect x="175" y="-8" width="3" height="16" rx="1.5" opacity="0.45" />
    <rect x="182" y="-4" width="3" height="8" rx="1.5" opacity="0.3" />
    <rect x="189" y="-12" width="3" height="24" rx="1.5" opacity="0.5" />
    <rect x="196" y="-18" width="3" height="36" rx="1.5" opacity="0.55" />
    <rect x="203" y="-8" width="3" height="16" rx="1.5" opacity="0.4" />
    <rect x="210" y="-4" width="3" height="8" rx="1.5" opacity="0.3" />
  </g>
</svg>
"""

def get_image_banner_html(image_uri):
    """
    Returns image styled in the banner frame to match the SVG banner aspect ratio.
    """
    return f"""
    <div class="banner-image-container">
        <img src="{image_uri}" class="banner-image-element" />
    </div>
    """
