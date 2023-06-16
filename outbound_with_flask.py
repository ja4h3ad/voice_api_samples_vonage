# load imports
from flask import Flask, request, jsonify
import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv
import vonage

# define path to your .env file
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
# fetch the Vonage Application ID from .env - this is important to generate the JWT
VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
# fetch the private key path generated from the project settings from .env - this is important to generate the JWT
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
# fetch your "From" number that will be the CLID in the outbound call
VONAGE_NUMBER = os.environ.get("FROM_NUMBER")
# destination number to call
TO_NUMBER = os.environ.get("TO_NUMBER")


@app.route("/") # returns a webhook to ngrok indicating the web app is functional and ngrok is reachable
# test using browser line reflective of your ngrok implementation and app port ("http://localhost:5002/)
def index():
    return "You are now making an outbound call!"

@app.route("/make_call", methods=["GET", "POST"])
# test using browser line reflective of your ngrok implementation and app port ("http://localhost:5002/make_call")
def make_call():
    client = vonage.Client(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
    print("TO_NUMBER:", TO_NUMBER)  # debug statement - you can comment out as appropriate
    print("VONAGE_NUMBER:", VONAGE_NUMBER)  # debug statement - you can comment out as appropriate

    response = client.voice.create_call({
        'to': [{'type': 'phone', 'number': TO_NUMBER}],
        'from': {'type': 'phone', 'number': VONAGE_NUMBER},
        'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Vonage.  Have a great day'}]
    })

    pprint(response)
    return jsonify({"message": "Voice call initiated."})

if __name__ == "__main__":
        app.run(port=5002)