from flask import Flask, request, jsonify
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

VONAGE_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")


@app.route("/answer")
def answer_call():
    for param_key, param_value in request.args.items():
        print("{}: {}".format(param_key, param_value))

    from_ = request.args['from']

    return jsonify([
        {
            "action": "talk",
            "text": "Thank you for calling from " + " ".join(from_)
        }
    ])


if __name__ == '__main__':
    app.run(port=5002)