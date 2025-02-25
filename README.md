# Flask Project

## Overview

This is a Flask-based web application. The main application file (`app.py`) is located in the `src` folder. This guide provides instructions on setting up the environment, installing dependencies, and running the application.

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

### 4. Run the Application

```bash
cd src
python app.py
```

By default, the app runs on `http://127.0.0.1:5000/`. You can modify the port by editing `app.py`.

### 5. Deactivate Virtual Environment (When Done)

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

## Contributing

Feel free to contribute! Fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License.
