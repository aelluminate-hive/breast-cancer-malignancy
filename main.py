import numpy as np
import joblib
import inquirer
from src.inputs.input_handler import get_user_input

# Load the model
model = joblib.load("models/svm.pkl")

# Define the initial question to ask if the user wants to predict or exit
initial_question = [
    inquirer.List(
        "action",
        message="What would you like to do?",
        choices=["Predict", "Exit"],
    )
]

# Prompt the user for the initial action
initial_answer = inquirer.prompt(initial_question)

if initial_answer["action"] == "Predict":
    # Get user input
    new_data = get_user_input()

    # Make a prediction
    prediction = model.predict(new_data)[0]

    # Map numerical predictions to categorical labels
    label_map = {2: "Benign", 4: "Malignant"}
    prediction_label = label_map.get(prediction, "Unknown")

    print("Prediction:", prediction_label)
else:
    print("Exiting the program.")
