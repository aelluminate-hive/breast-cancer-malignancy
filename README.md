# Breast Cancer Malignancy

This project explores the application of Support Vector Machines (SVM) in classifying human cell records to predict the malignancy of breast cancer samples. By training an SVM model on a dataset of breast cancer features, the goal is to accurately differentiate between benign and malignant cases.

## Usage

To generate `preprocessed.csv` dataset, run the notebook `report.ipynb` in the `notebooks` directory. You need to have the required libraries installed. To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

### Why Do You Need to Preprocess the Data?

The preprocessed data is essential for building the Support Vector Machine (SVM) model. The SVM model is used to predict the malignancy of breast cancer. The SVM model is built using the `preprocessed.csv` dataset.

### How to Use the SVM Model?

To use the SVM model, run the `main.py` script located in the root directory. This script will load the SVM model and predict the malignancy of breast cancer either as benign or malignant.

```bash
py -m main
```

Once you run the script, the program will prompt you to enter the values of the features. After entering the values, the program will predict the malignancy of breast cancer.

#### Example Usage

```bash
[?] What would you like to do?:
 > Predict
   Exit
```

If you choose `Predict`, the program will prompt you to enter the values of the features.

```bash
[?] Clump Thickness: 8
[?] Uniformity of Cell Size: 7
[?] Uniformity of Cell Shape: 6
[?] Marginal Adhesion: 4
[?] Single Epithelial Cell Size: 6
[?] Bare Nuclei: 1
[?] Bland Chromatin: 6
[?] Normal Nucleoli: 3
[?] Mitoses: 1
```

After entering the values, the program will predict the malignancy of breast cancer.

```bash
Prediction: Malignant
```

## Introduction

Breast cancer is one of the most common cancers affecting women worldwide. Early detection and accurate diagnosis are crucial for effective treatment and improved survival rates. This project aims to develop a machine learning model to predict the malignancy of breast cancer tumors using a Support Vector Machine (SVM) algorithm. By preprocessing the data and training the SVM model, we can classify tumors as either benign or malignant based on various features extracted from cell nuclei present in breast tissue samples.

This repository contains all the necessary code and instructions to preprocess the data, train the SVM model, and make predictions on new data. The goal is to provide a reliable tool for medical professionals and researchers to assist in the early detection and diagnosis of breast cancer.

## Project Goal

The primary goal of this project is to develop a machine learning model that can accurately predict the malignancy of breast cancer tumors based on histopathological features. By leveraging the power of SVM algorithms and preprocessing techniques, we aim to create a robust and reliable tool for diagnosing breast cancer at an early stage.

## The Data

The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) dataset obtained from the UCI Machine Learning Repository. The dataset contains almost 700 samples of breast cancer tumors, each characterized by 10 features related to the size and shape of cell nuclei present in the tumor tissue. The target variable is the diagnosis of the tumor, which can be either benign (2) or malignant (4).

### Dataset Snapshot

The dataset used in this project will contain the following columns:

- **Clump Thickness**: The thickness of the tumor cell clumps.
- **Uniformity of Cell Size**: The uniformity of cell sizes in the tumor.
- **Uniformity of Cell Shape**: The uniformity of cell shapes in the tumor.
- **Marginal Adhesion**: The level of adhesion of tumor cells to surrounding cells.
- **Single Epithelial Cell Size**: The size of single epithelial cells in the tumor.
- **Bare Nuclei**: The number of bare nuclei in the tumor.
- **Bland Chromatin**: The level of chromatin staining in the tumor.
- **Normal Nucleoli**: The number of normal nucleoli in the tumor.
- **Mitoses**: The number of mitoses observed in the tumor.
- **Class**: The diagnosis of the tumor (2 for benign, 4 for malignant).

## Methodology

- **Data Preprocessing**: The dataset will be preprocessed to handle missing values, encode categorical variables, and scale the features.
- **Model Training**: An SVM model will be trained on the preprocessed dataset to predict the malignancy of breast cancer tumors.
- **Model Evaluation**: The model will be evaluated using various performance metrics such as accuracy, precision, recall, and F1 score.
- **Model Deployment**: The trained SVM model will be deployed as a standalone application to predict the malignancy of new breast cancer tumors.

## Tools

The project will be implemented using the following tools and libraries such as **Python**, **Pandas**, **NumPy**, **Scikit-learn**, **Matplotlib**, and **Seaborn**. These tools provide robust support for data preprocessing, machine learning model development, and data visualization.

## Model Evaluation

The SVM model will be evaluated using the following metrics:

- **Accuracy**: The proportion of correctly classified samples.
- **Precision**: The proportion of correctly classified malignant samples among all samples predicted as malignant.
- **Recall**: The proportion of correctly classified malignant samples among all actual malignant samples.

### Our Results

The SVM model was evaluated on a test set, and the following classification report summarizes the performance:

```
              precision    recall  f1-score   support

           2       0.95      0.99      0.97        79
           4       0.98      0.93      0.96        58

    accuracy                           0.96       137
   macro avg       0.97      0.96      0.96       137
weighted avg       0.96      0.96      0.96       137
```

The model achieved an overall accuracy of 96%, with high precision and recall for both benign (2) and malignant (4) classes. The F1-scores indicate a balanced performance across both classes.

## Conclusion

The SVM model developed in this project demonstrates high accuracy and reliability in predicting the malignancy of breast cancer tumors. By leveraging histopathological features extracted from tumor samples, the model can assist medical professionals in diagnosing breast cancer at an early stage. The model's robust performance and ease of deployment make it a valuable tool for improving patient outcomes and survival rates.