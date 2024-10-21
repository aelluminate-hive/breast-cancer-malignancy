import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import (
    classification_report,
)


# Constants
DATASET = "datasets/preprocessed.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "svm.pkl")

# Load the dataset
data = pd.read_csv(DATASET)

# Spit the dataset into features and target
features = [
    "Clump",
    "UnifSize",
    "UnifShape",
    "MargAdh",
    "SingEpiSize",
    "BareNuc",
    "BlandChrom",
    "NormNucl",
    "Mit",
]
target = "Class"

X = np.asarray(data[features])
y = np.asarray(data[target])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = SVC(kernel="linear", gamma="auto", C=2)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model to a file
print("Saving the model to", MODEL_PATH)
joblib.dump(model, MODEL_PATH)
print("Model saved successfully.")
