from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv
import vonage


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

VONAGE_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)
print("TO_NUMBER:", TO_NUMBER) # debug statement
print("VONAGE_NUMBER:", VONAGE_NUMBER) # debug statement

response = client.voice.create_call({
    'to': [{'type': 'phone', 'number': TO_NUMBER}],
    'from': {'type': 'phone', 'number': VONAGE_NUMBER},
    'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Vonage.  Have a great day'}]
})

pprint(response)