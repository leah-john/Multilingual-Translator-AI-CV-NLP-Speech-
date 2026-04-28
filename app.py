import streamlit as st
import numpy as np
import cv2

from modules.ocr import extract_text
from modules.hf_model import detect_language, translate_text
from modules.speech import text_to_speech

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Translator AI", layout="wide")

st.title("🌐 Multilingual Translator (CV + NLP + Voice)")

# ---------------- LANGUAGE OPTIONS ----------------
languages = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "hi": "Hindi",
    "unknown": "Unknown"
}

target_lang_name = st.selectbox("Select Target Language", list(languages.keys()))
target_lang = languages[target_lang_name]

# ---------------- INPUT ----------------
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
manual_text = st.text_area("Type text in any language")

# ---------------- INIT TEXT ----------------
text = ""

# ---------------- GET TEXT ----------------
if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, caption="Uploaded Image")

    text = extract_text(image)

elif manual_text:
    text = manual_text.strip()

# ---------------- PROCESS ----------------
if text:
    with st.spinner("Processing..."):
        detected_lang = detect_language(text)
        translated = translate_text(text, target_lang)

    # ---------------- OUTPUT ----------------
    st.subheader("📄 Text")
    st.write(text)

    st.subheader("🌍 Detected Language")
    st.success(detected_lang)

    st.subheader(f"🔁 Translated ({target_lang_name})")
    st.success(translated)

    # ---------------- AUDIO ----------------
    st.subheader("🔊 Voice Output")

    speech_text = f"The detected language is {detected_lang}. The translated text is {translated}."

    if st.button("Play Audio"):
        try:
            audio_file = text_to_speech(speech_text, target_lang)
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.error(f"Audio error: {str(e)}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("⚠️ First run downloads models (~1GB). Be patient.")