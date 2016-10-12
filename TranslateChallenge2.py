import httplib2
import urllib
import json

TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2?key="
GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
TRANSLATE_SOURCE = "&source=en"
TRANSLATE_TARGET = "&target="
TRANSLATE_TEXT = "&q="

# Extend your wrapper function with target language:
# print translate(text, language='XX') -> text in XX language

def translate(text, language):
    text_encoded = urllib.quote_plus(text)
    url = TRANSLATE_URL + GOOGLE_API_KEY + TRANSLATE_SOURCE + TRANSLATE_TARGET + language + TRANSLATE_TEXT + text_encoded
    http = httplib2.Http()
    response, body = http.request(url, "GET")

    try:
        parsed_body = json.loads(body)
        return parsed_body['data']["translations"][0]['translatedText']
    except Exception as e:
        return "translation failed with no JSON response"

print translate('words and more words', 'es')
