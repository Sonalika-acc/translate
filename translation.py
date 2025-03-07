import streamlit as st
from googletrans import Translator
from docx import Document
import pdfplumber

# Streamlit Page Config
st.set_page_config(page_title="🌍 TransLingua - AI Translator", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .stApp {
        background: linear-gradient(to right, #e3f2fd, #fce4ec);
        color: #333;
    }
    .stTitle {
        font-size: 36px !important;
        text-align: center;
        font-weight: bold;
        color: #2c3e50;
    }
    .stSidebar {
        background-color: #2c3e50 !important;
        color: white !important;
    }
    .stButton>button {
        background-color: #3498db !important;
        color: white !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        padding: 10px 20px !important;
    }
    .stTextArea textarea {
        font-size: 16px !important;
        border-radius: 10px !important;
    }
    .stSelectbox select {
        font-size: 16px !important;
        border-radius: 5px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='stTitle'>🌍 TransLingua - AI Language Translator</h1>", unsafe_allow_html=True)
st.write("Translate text and documents easily with an elegant UI! ✨")

# Initialize Translator
translator = Translator()

# Supported Languages
languages = {
    "English": "en", "French": "fr", "Spanish": "es", "German": "de",
    "Chinese (Simplified)": "zh-cn", "Japanese": "ja", "Korean": "ko",
    "Hindi": "hi", "Arabic": "ar", "Portuguese": "pt", "Russian": "ru",
    "Italian": "it", "Dutch": "nl", "Turkish": "tr", "Thai": "th"
}

# Sidebar for Language Selection
st.sidebar.header("🌐 Select Languages")
source_language = st.sidebar.selectbox("Source Language:", ["Auto-Detect"] + list(languages.keys()))
target_language = st.sidebar.selectbox("Target Language:", list(languages.keys()))

# File Upload
uploaded_file = st.file_uploader("📄 Upload a document (TXT, DOCX, PDF)", type=["txt", "docx", "pdf"])

# Function to Extract Text from Files
def extract_text_from_file(file):
    text = ""
    if file.name.endswith(".txt"):
        text = file.getvalue().decode("utf-8")
    elif file.name.endswith(".docx"):
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    elif file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

# Text Input
text_to_translate = ""
if uploaded_file:
    text_to_translate = extract_text_from_file(uploaded_file)
    st.text_area("📜 Extracted Text:", text_to_translate, height=150)
else:
    text_to_translate = st.text_area("📝 Enter text to translate:")

# Translate Button
if st.button("🔄 Translate"):
    if text_to_translate.strip():
        src_lang = languages.get(source_language, "auto")  # Auto-detect if needed
        tgt_lang = languages[target_language]

        try:
            translated_text = translator.translate(text_to_translate, src=src_lang, dest=tgt_lang).text
            st.subheader("✅ Translated Text:")
            st.success(translated_text)

            # Option to Download Translated Text
            translated_file = "translated_text.txt"
            with open(translated_file, "w", encoding="utf-8") as f:
                f.write(translated_text)

            st.download_button(
                label="📥 Download Translated File",
                data=translated_text,
                file_name="translated_text.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Translation failed: {e}")
    else:
        st.warning("⚠️ Please enter text or upload a document.")

# Footer
st.markdown("---")
<<<<<<< HEAD
st.write("💡 *Powered by Google Translate (Unofficial API) & Streamlit.*")
=======
st.write("💡 *Powered by Google Translate (Unofficial API) & Streamlit.*")


>>>>>>> 5be354b98bac21d66b74e59e65651c5404a819c5
