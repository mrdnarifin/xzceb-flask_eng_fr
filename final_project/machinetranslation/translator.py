""" Translator Instance """

import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """ English to French """
    try:
        frenchText = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        return frenchText['translations'][0]['translation']
    except ApiException:
        return englishText

def frenchToEnglish(frenchText):
    """ French to English """
    try:
        englishText = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        return englishText['translations'][0]['translation']
    except ApiException:
        return frenchText
