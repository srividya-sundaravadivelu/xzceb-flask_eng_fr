import os
from deep_translator import MyMemoryTranslator
from dotenv import load_dotenv

load_dotenv()

def english_to_french(english_text):
    if english_text in (None,''):
        return "error: text is empty"
    translator = MyMemoryTranslator(source='en', target='fr')
    result = translator.translate(english_text)
    return result
    

def french_to_english(french_text):
    if french_text in (None,''):
        return "error: text is empty"

    translator = MyMemoryTranslator(source='fr', target='en')
    result = translator.translate(french_text)
    return result