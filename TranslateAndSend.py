import httplib2
import urllib
import json

from twilio.rest import TwilioRestClient
account_sid = "ACd8c5445de39b09128dbad18be4b6ce72" # Your Account SID from www.twilio.com/console
auth_token  = "c03f19867cab01243e3cd63731b0ff19"  # Your Auth Token from www.twilio.com/console

TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2?key="
GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
TRANSLATE_SOURCE = "&source=en"
TRANSLATE_TARGET = "&target="
TRANSLATE_TEXT = "&q="

def sendText(text, number):
    if type(text) is list:
        # TODO Delegation
        textToSend = ""
        for item in text:
            textToSend += item + ", "
    elif type(text) is unicode or str:
        textToSend = text
    else:
        raise Exception("Not expected type")
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(
        body = textToSend,
        to = "+1" + number,    # Replace with your phone number
        from_ = "+16315339961") # Replace with your Twilio number

def translate(text, language):
    if type(text) is list:
        return translateArray(text, language)
    elif type(text) is unicode or str:
        return translateString(text, language)
    else:
        raise Exception("Not expected type")

def translateArray(iterable, language):
    return translateString(', '.join(iterable), language)

def translateString(text, language):
    text_encoded = urllib.quote_plus(text)
    url = TRANSLATE_URL + GOOGLE_API_KEY + TRANSLATE_SOURCE + TRANSLATE_TARGET + language + TRANSLATE_TEXT + text_encoded
    http = httplib2.Http()
    response, body = http.request(url, "GET")
    try:
        parsed_body = json.loads(body)
        return parsed_body['data']["translations"][0]['translatedText']
    except Exception as e:
        return "translation failed with no JSON response"

sendText(translate('it is lit', 'es'), "6318384440")
sendText(translate(["word", "another set of words", "here are more words"], 'es'), "6318384440")
