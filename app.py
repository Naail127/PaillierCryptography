# app.py
from flask import Flask, request, jsonify, render_template # <-- Add render_template
from flask_cors import CORS
import PasswordManager


app = Flask(__name__)

CORS(app)

@app.route('/')
def login_page():
    # This tells Flask to look in the 'templates' folder for 'login.html'
    return render_template('Login_page.html')

# --- NEW ROUTE FOR THE SUCCESS PAGE ---
@app.route('/manager')
def manager_page():
    # This will be the page we redirect to
    return render_template('PasswordManager.html')
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
        Username, Password = PasswordManager.view_details('tim')
        if Username == name and Password == message:
            # Create a response to send back to the JavaScript
            response_message = "Welcome."

            return jsonify({'status': 'success', 'response': response_message})
        else:
            response_message = f"Invalid credentials."
            return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

    except Exception as e:
        # Handle any other errors
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'An internal error occurred'}), 500

@app.route('/addPassword', methods=['POST'])
def addPassword():
    data = request.get_json()
    try:
        site = data.get('siteName')
        username = data.get('username')
        password = data.get('password')
        print(site,username,password)
        PasswordManager.add_details(site, username, password)
        return jsonify({'status': 'success', 'message': 'Password added successfully'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'An internal error occurred'}), 500

@app.route('/viewPassword', methods=['POST'])
def viewPassword():
    data = request.get_json()
    print('received data:')
    try:
        site = data.get('siteName')
        print(site)
        username, password = PasswordManager.view_details(site)

        return jsonify({'status': 'success', 'username': username, 'password': password})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'An internal error occurred'}), 500

@app.route('/removePassword', methods=['POST'])
def removePassword():
    data = request.get_json()
    try:
        site = data.get('siteName')
        print(site)
        PasswordManager.delete_details(site)

        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'An internal error occurred'}), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5999, debug=True)