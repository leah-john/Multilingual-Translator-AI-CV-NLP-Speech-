from transformers import pipeline

# ---------------- LANGUAGE DETECTION ----------------
lang_detector = pipeline(
    "text-classification",
    model="papluca/xlm-roberta-base-language-detection"
)

# ---------------- TRANSLATION (NLLB MODEL) ----------------
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

def detect_language(text):
    try:
        result = lang_detector(text[:200])
        return result[0]['label']
    except:
        return "unknown"

def translate_text(text, target_lang):
    try:
        # Map language codes
        lang_map = {
            "en": "eng_Latn",
            "fr": "fra_Latn",
            "es": "spa_Latn",
            "hi": "hin_Deva"
        }

        src_lang = lang_map.get(detect_language(text), "eng_Latn")
        tgt_lang = lang_map.get(target_lang, "eng_Latn")

        result = translator(text, src_lang=src_lang, tgt_lang=tgt_lang)
        return result[0]["translation_text"]

    except Exception as e:
        return f"Error: {str(e)}"