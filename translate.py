from deep_translator import GoogleTranslator

def translate_text(text, target_language="pt"):
    if not text:
        return ""
    return GoogleTranslator(source='en', target=target_language).translate(text)
