import pickle
import pandas as pd
import gradio as gr

def predict_health(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Create a dictionary with the input values
    input_data = {
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    }

    # Create a DataFrame from the input data
    x = pd.DataFrame(input_data)

    # Load the pre-trained model
    model = pickle.load(open('logistic_model.pkl', 'rb'))

    # Make predictions
    y = model.predict(x)

    if y == 1:
        return "You have heart disease."
    else:
        return "You are fine."

iface = gr.Interface(
    fn=predict_health,
    inputs=[
        gr.Slider(minimum=0, maximum=120, label="Age"),
        gr.Radio(["Male", "Female"], label="Sex"),
        gr.Slider(minimum=0, maximum=10, label="Chest Pain (cp)"),
        gr.Slider(minimum=0, maximum=200, label="Resting Blood Pressure (trestbps)"),
        gr.Slider(minimum=0, maximum=500, label="Cholesterol (chol)"),
        gr.Slider(minimum=0, maximum=1, label="Fasting Blood Sugar (fbs)"),
        gr.Slider(minimum=0, maximum=2, label="Resting Electrocardiographic Results (restecg)"),
        gr.Slider(minimum=0, maximum=200, label="Maximum Heart Rate Achieved (thalach)"),
        gr.Slider(minimum=0, maximum=1, label="Exercise-Induced Angina (exang)"),
        gr.Slider(minimum=0, maximum=10, label="ST Depression Induced by Exercise (oldpeak)"),
        gr.Slider(minimum=0, maximum=2, label="Slope of the ST Segment (slope)"),
        gr.Slider(minimum=0, maximum=4, label="Number of Major Vessels (ca)"),
        gr.Slider(minimum=0, maximum=3, label="Thalassemia (thal)")
    ],
    outputs="text",
    title="Heart Disease Prediction System",
    description="Enter the parameters and see the health prediction."
)

iface.launch()


