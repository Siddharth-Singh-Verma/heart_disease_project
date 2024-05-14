# Heart Disease Prediction Project

## Table of Contents
- Project Description
- Data
- Evaluation
- Features
- Modeling
- Installation
- Usage
- Contributing


## Project Description
This project aims to predict heart disease using machine learning. I have applied three different classification algorithms: Logistic Regression, K-Nearest Neighbors Classifier, and Random Forest Classifier. These algorithms were evaluated and hyperparameter tuning was used to further boost their accuracy. Various graphs have been used to visualize my work. In the end, I have also tried to create a GUI using Gradio to facilitate user interactions with the final tuned model. 

## Data
The dataset used in this project is a modified version of the UCI Heart Disease dataset available on Kaggle. It consists of 303 instances with 14 features related to heart health.

## Evaluation
The goal is to achieve high accuracy in predictions. We aim for at least 85% accuracy to ensure the reliability of our model.
#### Note 
85% is not high enough for the commercial usecase but since the dataset is a smaller version and only has limited 14 features so it is not possible to get  90-95% accuracy.
## Features of the dataset 
The dataset includes the following features:
- Age
- Sex
- Chest pain type (4 values)
- Resting blood pressure
- Serum cholesterol in mg/dl
- Fasting blood sugar > 120 mg/dl
- Resting electrocardiographic results (values 0,1,2)
- Maximum heart rate achieved
- Exercise-induced angina
- ST depression induced by exercise relative to rest (oldpeak)
- The slope of the peak exercise ST segment
- Number of major vessels (0-3) colored by fluoroscopy
- Thalassemia (thal): 0 = normal; 1 = fixed defect; 2 = reversible defect
- Target variable indicating the presence of heart disease

## Modeling
We have explored the following machine learning models:
- Logistic Regression
- K-Nearest Neighbors Classifier
- Random Forest Classifier

The models were evaluated using cross-validation and metrics such as precision, recall, and F1-score.

## Installation
git clone https://github.com/Siddharth-Singh-Verma/heart_disease_project.git


## Usage
To run the Gradio UI and interact with the model:

python user_interface.py

## Contributing
Contributions are welcome. Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.
