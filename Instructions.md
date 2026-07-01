# Objective
Build a completely local desktop application called "Acoustic Chronotope." The app allows users to input either a text memory or an image memory, uses a local Multimodal Vision-LLM via Ollama to extract sensory/environmental keywords, and passes those keywords to a local audio generation model to synthesize an ambient background soundscape (no speech/vocals) to trigger memory recall.

# System Architecture & Tech Stack (All Local)
1. Frontend/UI: Streamlit (enhanced with custom CSS for styling).
2. LLM Orchestrator: Ollama Python API.
   - Text routing: Uses `gemma4:e4b` for pure text inputs.
   - Image routing: Uses `llava-phi3:latest` for image inputs.
3. Sound Generation Engine: Meta's `AudioCraft` library executing the `facebook/audiogen-medium` model locally via PyTorch.
4. Audio Playback: Standard local web audio controls embedded natively in Streamlit.

# Technical Requirements & Dependencies
Ensure your environment setup routine includes:
- `pip install ollama audiocraft torch torchvision torchaudio streamlit`
- Access to a running local Ollama instance with `llava-phi3:latest` and `gemma4:e4b` available.

# Visual & Frontend Specifications: Modern "Human Style" Design
Do NOT build a dark-themed or standard tech dashboard. Apply a custom CSS block to transform the interface into a warm, tactile, human-centric journal experience using the following guidelines:
- **Color Palette:** Warm Minimalist. Background must be Linen Cream / Soft Sand (#FBF9F6). Text must be rich warm-charcoal (#2C2A29). Use a terracotta accent color (#D67B62) for active states and buttons.
- **Typography:** High-contrast editorial style. Use a premium serif font (like Playfair Display, Lora, or Georgia) for headers, and a clean sans-serif (like Inter, Helvetica Neue, or Arial) for functional controls and body text.
- **Form & Tactility:** Use generous whitespace, soft structural shadows, and rounded container corners (12px to 16px radius) to evoke the physical quality of premium stationery.

# Step-by-Step Implementation Instructions for Agent

## Step 1: LLM Processing Module (Ollama Integration)
- Create a function `process_memory_spark(text_input=None, image_path=None)` that communicates with the Ollama Python client.
- **Routing Logic:**
  - If `image_path` is provided: Send the image file along with the system prompt to model `llava-phi3:latest`.
  - If `text_input` is provided (and no image): Send the text string along with the system prompt to model `gemma4:e4b`.
- **System Prompt for Ollama:**
  "You are a sensory extraction engine. Analyze the provided text or image memory. Identify the core environmental background sounds, weather conditions, locations, and textures. Output EXACTLY 3 to 6 highly descriptive soundscape keywords separated by commas. Do not mention vocals, speech, music, or instruments. Example Output: 'heavy rain on glass, distant rolling thunder, quiet indoor room tone, ticking clock'."

## Step 2: Audio Synthesis Module (AudioCraft Integration)
- Create a function `generate_soundscape(prompt_keywords, duration=10)` using AudioCraft's AudioGen model.
- Load the `facebook/audiogen-medium` model onto the local device safely.
- Set generation parameters using: `model.set_generation_params(duration=duration)`.
- Generate the audio tensor from the processed Ollama keywords, clean up the audio data tensor, and save it locally as an exported `.wav` file named `output_memory.wav`.

## Step 3: Frontend Interface (Streamlit Layout)
Using the custom CSS styling defined above, implement a vertical, stacked editorial flow:
- **Header:** A serif title "Acoustic Chronotope" with a subtitle: *"Transforming visual and textual memory traces into local ambient soundscapes."*
- **Input Canvas Container:** Create two distinct, vertically stacked input sections:
  - Top Section: A text-area input field labeled *"Write a memory fragment..."*.
  - Bottom Section: A file uploader restricted to `.jpg`, `.jpeg`, and `.png` formats, labeled *"Or drop a photograph here..."*.
- **The Trigger Button:** A highly visible, padded button labeled "Trigger Memory Spark" centered below the inputs.
- **Processing States:** While processing, display `st.spinner` with custom text:
  - Phase 1: *"Sensing the memory texture..."*
  - Phase 2: *"Crafting the sound waves..."*
- **The Output Card:** Once generation is complete, display:
  - The extracted keywords styled as bold text elements above the audio player.
  - A clean `st.audio` HTML5 playback bar pre-loaded with `output_memory.wav`.

# Safety & Robustness
- Wrap the Ollama client calls and AudioCraft tensor processing in `try/except` blocks. If an error occurs (e.g., OOM or Ollama offline), surface a clean, user-friendly `st.error` message instead of crashing the UI.
- Automatically overwrite the `output_memory.wav` file on subsequent runs to prevent local storage bloat.