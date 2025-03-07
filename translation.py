import streamlit as st
from googletrans import Translator

# Streamlit App Configuration
st.set_page_config(page_title="TransLingua - Free AI Translator", layout="centered")

# Title and Description
st.title("🌍 TransLingua - Free AI Language Translator")
st.write("Translate text between multiple languages!")

# Initialize Translator
translator = Translator()

# Supported Languages
languages = {
    "English": "en", "French": "fr", "Spanish": "es", "German": "de",
    "Chinese (Simplified)": "zh-cn", "Japanese": "ja", "Korean": "ko",
    "Hindi": "hi", "Portuguese": "pt", "Russian": "ru",
    "Italian": "it", "Dutch": "nl", "Telugu": "te"
}

# Language Selection
source_language = st.selectbox("Select Source Language:", ["Auto-Detect"] + list(languages.keys()))
target_language = st.selectbox("Select Target Language:", list(languages.keys()))

# Text Input
text_to_translate = st.text_area("Enter text to translate:")

# Translate Button
if st.button("Translate"):
    if text_to_translate.strip():
        src_lang = languages.get(source_language, "auto")  # Auto-detect if not specified
        tgt_lang = languages[target_language]

        try:
            translated_text = translator.translate(text_to_translate, src=src_lang, dest=tgt_lang)
            st.subheader("Translated Text:")
            st.success(translated_text.text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")

# Footer
st.markdown("---")

