# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/process-data', methods=['POST'])
def process_data():
    # Get the JSON data sent from the JavaScript
    data = request.get_json()

    try:
        name = data.get('name')
        message = data.get('message')

        if not name or not message:
            # If data is missing, return an error
            return jsonify({'status': 'error', 'message': 'Missing name or message'}), 400

        # Process the data (here, we'll just print it and create a response)
        print(f"Received data: Name = {name}, Message = {message}")

        # Create a response to send back to the JavaScript
        response_message = f"Hello, {name}! Your message '{message}' was received by the Python server."

        return jsonify({'status': 'success', 'response': response_message})

    except Exception as e:
        # Handle any other errors
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'An internal error occurred'}), 500


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5999, debug=True)