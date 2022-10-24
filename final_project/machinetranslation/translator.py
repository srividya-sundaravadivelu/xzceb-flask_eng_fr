import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = 'cgh1iRSQF2AtdS0c_5d7E7693XAzE54VJ7AQ236GoZQY'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/605ee971-fbff-47d5-96dd-9b0788d7c015'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text in (None,''):
        return "error: text is empty"

    result = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return result["translations"][0]["translation"]
    

def french_to_english(french_text):
    if french_text in (None,''):
        return "error: text is empty"

    result = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return result["translations"][0]["translation"]