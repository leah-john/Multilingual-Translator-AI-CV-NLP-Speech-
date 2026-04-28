🔥 Multilingual Translator AI (CV + NLP + Speech)

An AI-powered application that extracts text from images, detects language, translates it into a target language, and generates natural speech output.

🧠 Features

📷 OCR-based text extraction from images
🌍 Automatic language detection
🔁 Multilingual translation
🔊 Text-to-speech output
🖥️ Interactive Streamlit UI

⚙️ Tech Stack

Programming: Python
Computer Vision: EasyOCR, OpenCV
NLP: Hugging Face Transformers
Models:
XLM-RoBERTa (Language Detection)
NLLB-200 (Translation)
Speech: Edge-TTS
Framework: Streamlit
Backend: PyTorch
Libraries: NumPy

🧠 System Pipeline

Image/Text Input
        ↓
OCR (EasyOCR)
        ↓
Language Detection (XLM-RoBERTa)
        ↓
Translation (NLLB)
        ↓
Speech Output (Edge TTS)


🚀 Installation

git clone https://github.com/your-username/text_translator_ai.git
cd text_translator_ai
📦 Create Virtual Environment
python -m venv venv

Activate:
venv\Scripts\activate   # Windows

📥 Install Dependencies
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

⚠️ Note
First run will download models (~1GB)
Requires internet connection for speech synthesis

💡 Future Improvements

Real-time camera translation
Translation history
Improved OCR accuracy
UI enhancements


👩‍💻 Author
Leah John
