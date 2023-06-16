# Outbound and Inbound Calls with Vonage API - Flask App
Here are three samples of inbound and outbound call control using Vonage's Voice API

1. outbound.py is a simple script that utilizes the Vonage SDK to set up an outbound call.  Get your feet wet
2. outbound_with_flask.py is a set of functions using the flask framework to accept webhooks/API calls to send outbound calls, potentially based on triggers 
3. inbound_with_flask.py is a set of functions using the flask framework to accept webhooks/API calls to deal with inbound calls, and specifically to utilize a webhook server for inbound event notifications



This Flask applications (e.g., 'outbound_ | inbound_with_flask.py') demonstrates making inbound and outbound calls using the Vonage API. It allows you to initiate a voice call from Vonage to a specified destination number.

## Prerequisites

Before running the application, make sure you have the following prerequisites:

- Python 3.x installed
- Flask framework installed
- Required Python packages listed in the `requirements.txt` file installed
- Vonage API credentials (Application ID, private key, and Vonage number)
- Properly configured environment variables in a `.env` file

## Getting Started

1. Clone the repository

2. Install the required packages:
pip install -r requirements.txt


3. Configure the environment variables:
Create a `.env` file in the project's root directory and add the following variables:
VONAGE_APPLICATION_ID=<your_vonage_application_id>
VONAGE_APPLICATION_PRIVATE_KEY_PATH=<path_to_private_key_file>
FROM_NUMBER=<your_vonage_number>
TO_NUMBER=<destination_number_to_call>

4. Run the application:
e.g, python app.py or directly in your IDE

6. Access the application:

Visit `http://localhost:5002` with route extension ('/')in your web browser to confirm the application is running and reachable.

## Usage

- **Webhook**: Accessing the root URL (`/`) of the application will return a webhook indicating the app is functional and reachable.

- **Initiating an Outbound Call**: Send a GET or POST request to `/make_call` to initiate an outbound call. The application will use the Vonage API to make the call to the specified destination number.

- **Making an inbound Call**: You do not need to make a GET or POST request.  Just run the app file and dial the designated inbound number.  

Please refer to the code comments within each `.py` for more detailed explanations of the implementation.

## License

This project is licensed under the [MIT License](LICENSE).



