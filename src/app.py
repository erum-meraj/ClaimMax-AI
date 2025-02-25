from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import pandas as pd
import json
import joblib  # For loading ML model
from deductions import get_applicable_deductions  # Custom module for deductions
from investments import suggest_investments  # Custom module for investment advice

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Load trained ML model for tax refund prediction
# model = joblib.load("tax_refund_model.pkl")

@app.route('/')
def home():
    # Render the basic form when the user lands on the app
    return render_template('basic_form.html')

# Handle basic form submission
@app.route('/submit_basic_form', methods=['POST'])
def submit_basic_form():
    # Get data from the form
    user_data = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'occupation': request.form.get('occupation'),
        'income': float(request.form.get('income')),
        'investments': request.form.get('investments'),
        'health_insurance': request.form.getlist('health-insurance'),  # For checkboxes
        'disability': request.form.get('disability'),
        'loan': request.form.getlist('loan'),  # For checkboxes
        'donations': request.form.get('donations'),
        'interest': request.form.getlist('interest')  # For checkboxes
    }

    # Store user data in session
    session['user_data'] = user_data

    # Redirect to the chatbot interface
    return redirect(url_for('chatbot'))

# Chatbot interface
@app.route('/chatbot')
def chatbot():
    # Render the chatbot interface
    return render_template('chatbot.html')

# Handle chatbot responses
@app.route('/get', methods=['GET'])
def get_bot_response():
    # Get the user's message from the query parameters
    user_message = request.args.get('msg')

    # Retrieve user data from session
    user_data = session.get('user_data', {})
    print(user_message.lower())
    user_data = str(user_data)
    # Generate bot response based on user input
    if "deduction" in user_message.lower():
        response = get_applicable_deductions(user_data)
    elif "investment" in user_message.lower():
        response = suggest_investments(user_data)
    else:
        response = "I'm here to help with tax-related queries. Ask me about deductions or investments!"

    return jsonify(response)

# 1. Upload Form 16 (CSV or JSON format)
@app.route('/upload_form16', methods=['POST'])
def upload_form16():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.filename.endswith('.json'):
        data = pd.read_json(file)
    else:
        return jsonify({"error": "Invalid file format. Use CSV or JSON."}), 400
    
    return jsonify({"message": "Form 16 uploaded successfully", "data": data.to_dict()})

if __name__ == '__main__':
    app.run(debug=True)