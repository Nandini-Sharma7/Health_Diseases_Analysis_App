# 🏥 Multi_Diseases_Analysis

This project is a web-based application built with Flask that utilizes pre-trained machine learning models to predict the risk of various diseases based on user-provided health data. The system offers an intuitive interface for users to get quick predictions for Heart Disease, Brain Stroke, Lung Disease, and Kidney Disease.

# ✨ Features

Heart Disease Prediction: A model to assess the risk of heart disease. ❤️

Brain Stroke Prediction: Predicts the likelihood of a brain stroke. 🧠

Lung Disease Prediction: Determines the risk of developing a lung-related condition. 🫁

Kidney Disease Prediction: Analyzes data to detect the presence of chronic kidney disease. 🫘

User-Friendly Interface: A simple and clean web interface for data input and result display.

# 🛠️ Tech Stack

Backend: Python 🐍

Web Framework: Flask 🧪

Machine Learning: joblib for model loading 📦

Frontend: HTML, Tailwind CSS (for styling)

# 🚀 Getting Started

Follow these steps to get a local copy of the project up and running.

Prerequisites
You need to have Python 3.x and pip installed on your system.

Installation
Clone the repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install the required packages:

pip install Flask joblib scikit-learn

Place your model files:
Create a models directory in the root of your project and place your .pkl model files inside it. The file names must match those in the app.py script.

/your-app-directory
├── app.py
└── models/
    ├── heartdisease.pkl
    ├── brain.pkl
    ├── lungs.pkl
    └── kid.pkl

Run the application:

python app.py

The application will start and be accessible at http://127.0.0.1:5000.

💡 Usage
Navigate to http://127.0.0.1:5000 in your web browser. From the main page, click on the button for the disease you wish to predict. Enter the required health data into the form and click "Predict" to see the result.

📂 Project Structure
.
├── app.py               # Main Flask application file
├── models/              # Directory for your pre-trained .pkl models
│   ├── brain.pkl
│   ├── heartdisease.pkl
│   ├── kid.pkl
│   └── lungs.pkl
└── templates/           # HTML templates for the web pages
    ├── body.html
    ├── brain.html
    ├── heart.html
    ├── kidney.html
    └── lungs.html

This project is for educational and demonstrative purposes and should not be used as a substitute for professional medical advice.
