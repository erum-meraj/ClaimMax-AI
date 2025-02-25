# ClaimMax AI - Tax Deduction Assistant

## Overview

ClaimMax AI is an AI-powered tax deduction assistant designed to help users identify potential tax deductions they are eligible for. The application also provides recommendations on investment strategies to maximize tax benefits in future filings. Built on Flask, the application leverages the Gemini API to generate intelligent responses and insights.

## Problem Statement

Many taxpayers are unaware of their potential tax refunds, leading to missed savings and inefficient financial planning. Our solution aims to simplify this process by providing an AI-driven predictive model that estimates tax refunds based on income, deductions, and previous filings.

## Features

- **Automated Tax Deduction Analysis**: Identifies deductions based on user-provided financial details.
- **Tax Refund Prediction**: Uses AI to estimate potential tax refunds.
- **Investment Recommendations**: Suggests tax-saving investment opportunities for future filings.
- **Conversational AI Support**: Utilizes the Gemini API to provide real-time insights and responses.

## Prerequisites

Ensure you have the following installed:

- Python (>=3.8)
- pip (Python package manager)
- Virtual environment module (venv)

## Setup Instructions

### 1. Clone the Repository

```bash
 git clone <repository_url>
 cd <repository_folder>
```

### 2. Create and Activate a Virtual Environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

Obtain a Gemini API key and set it in your environment variables:

```bash
export GEMINI_API_KEY='your_api_key_here'
```

On Windows:

```bash
set GEMINI_API_KEY='your_api_key_here'
```

### 5. Run the Application

```bash
cd src
python app.py
```

By default, the app runs on `http://127.0.0.1:5000/`. You can modify the port by editing `app.py`.

### 6. Deactivate Virtual Environment (When Done)

```bash
deactivate
```

## Project Structure

```
project_folder/
│── venv/                 # Virtual environment (ignored in .gitignore)
│── src/
│   ├── app.py            # Main Flask application
│   ├── templates/        # HTML templates
│   ├── static/           # Static files (CSS, JS, images)
│── requirements.txt      # Project dependencies
│── README.md             # Documentation
```

## Requirements

The `requirements.txt` file includes the necessary dependencies for running this project:

```
flask
Flask
flask-cors
PyPDF2
langchain
langchain-google-genai
google-generativeai
faiss-cpu
python-dotenv
pandas
json
joblib
```

## Contributing

Feel free to contribute! Fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License.
