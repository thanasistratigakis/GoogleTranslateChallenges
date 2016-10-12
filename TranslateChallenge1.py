import httplib2
import urllib
import json

GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2?key=AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk&source=en&target=es&q="

# create a python wrapper function for translate:
# print translate(text) -> translated_text

def translate(text):
    text_encoded = urllib.quote_plus(text)
    url = TRANSLATE_URL + text_encoded

    http = httplib2.Http()
    response, body = http.request(url, "GET")
    # print body
    try:
        parsed_body = json.loads(body)
        print parsed_body['data']["translations"][0]['translatedText']
    except Exception as e:
        print "translation failed with no JSON response"

translate('words and more words')
