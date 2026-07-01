import os
import torch
import ollama
from audiocraft.models import AudioGen
from audiocraft.data.audio import audio_write
import streamlit as st

# Device Configuration for AudioCraft
device = 'cuda' if torch.cuda.is_available() else 'cpu'

@st.cache_resource
def load_audiogen_model():
    """
    Load facebook/audiogen-medium onto target hardware device safely.
    """
    return AudioGen.get_pretrained('facebook/audiogen-medium', device=device)

def process_memory_spark(text_input=None, image_path=None):
    """
    Step 1: LLM Processing Module (Ollama Integration)
    Processes textual/visual input and extracts 3 to 6 descriptive soundscape keywords.
    """
    if image_path:
        # Image routing: llava-phi3:latest (optimized to extract sound-producing elements)
        image_prompt = (
            "You are a sensory extraction engine. Analyze the provided image memory. "
            "Identify the active, sound-producing elements present in the environment shown. "
            "Describe only the background and ambient sounds that would naturally occur in this scene. "
            "Do not include visual details, colors, textures, or static objects. "
            "Output EXACTLY 3 to 6 highly descriptive soundscape keywords separated by commas. "
            "Do not write sentences or descriptions. Do not mention vocals, speech, music, or instruments."
        )
        response = ollama.generate(
            model='llava-phi3:latest',
            prompt=image_prompt,
            images=[image_path]
        )
        return response.get('response', '').strip()
    elif text_input:
        # Text routing: gemma4:e4b
        system_prompt = (
            "You are a sensory extraction engine. Analyze the provided text or image memory. "
            "Identify the core environmental background sounds, weather conditions, locations, and textures. "
            "Output EXACTLY 3 to 6 highly descriptive soundscape keywords separated by commas. "
            "Do not mention vocals, speech, music, or instruments. "
            "Example Output: 'heavy rain on glass, distant rolling thunder, quiet indoor room tone, ticking clock'."
        )
        combined_prompt = f"Memory:\n{text_input}\n\nSystem Prompt:\n{system_prompt}"
        response = ollama.generate(
            model='gemma4:e4b',
            prompt=combined_prompt
        )
        return response.get('response', '').strip()
    else:
        raise ValueError("Neither memory fragment text nor image was provided.")

def clean_keywords(raw_output):
    """
    Cleans Ollama outputs to isolate and format keywords as a comma-separated string.
    Supports both comma-separated phrases and numbered/bulleted lists.
    """
    text = raw_output.strip()
    if ":" in text:
        parts = text.split(":")
        after_colon = parts[-1].strip()
        if "," in after_colon or "\n" in after_colon:
            text = after_colon

    lines = text.split("\n")
    cleaned_items = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Strip list indicators like "1. ", "- ", "* "
        parts = line.split(".", 1)
        if len(parts) > 1 and parts[0].strip().isdigit():
            item = parts[1].strip()
        elif line.startswith("-") or line.startswith("*"):
            item = line[1:].strip()
        else:
            item = line

        # Strip remaining quotes and brackets
        item = item.replace('"', '').replace("'", "").replace("[", "").replace("]", "").strip()
        if item:
            if "," in item:
                cleaned_items.extend([i.strip() for i in item.split(",") if i.strip()])
            else:
                cleaned_items.append(item)

    if len(cleaned_items) > 1:
        text = ", ".join(cleaned_items)
    else:
        text = text.replace('"', '').replace("'", "").replace("[", "").replace("]", "").replace("\n", " ").strip()
        
    return text

def generate_soundscape(prompt_keywords, duration=10):
    """
    Step 2: Audio Synthesis Module (AudioCraft Integration)
    Synthesizes environmental soundscape wav file locally.
    """
    model = load_audiogen_model()
    model.set_generation_params(duration=duration)
    
    with torch.inference_mode():
        wav = model.generate([prompt_keywords])
        
    wav_to_save = wav[0].cpu()
    sr = model.sample_rate
    
    target_path = 'output_memory'
    
    # Overwrite by removing old output_memory.wav if it exists
    if os.path.exists(target_path + '.wav'):
        try:
            os.remove(target_path + '.wav')
        except Exception:
            pass
            
    # Save the generated audio tensor
    written_path = audio_write(
        target_path, 
        wav_to_save, 
        sr, 
        format='wav', 
        strategy='loudness', 
        loudness_headroom_db=16, 
        loudness_compressor=True
    )
    return written_path
