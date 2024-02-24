import gradio as gr

def predict_health(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target):
    # Your health prediction model goes here
    # Replace this with your actual model prediction logic
    return "Healthy" if age > 50 else "Not Healthy"

iface = gr.Interface(
    fn=predict_health,
    inputs=[
        gr.Slider(minimum=0, maximum=120,  label="age"),
        gr.Radio(["Male", "Female"], label="sex"),
        gr.Slider(minimum=0, maximum=10,  label="cp"),
        gr.Slider(minimum=0, maximum=200, label="trestbps"),
        gr.Slider(minimum=0, maximum=500, label="chol"),
        gr.Slider(minimum=0, maximum=1, label="fbs"),
        gr.Slider(minimum=0, maximum=2, label="restecg"),
        gr.Slider(minimum=0, maximum=200, label="thalach"),
        gr.Slider(minimum=0, maximum=1, label="exang"),
        gr.Slider(minimum=0, maximum=10, label="oldpeak"),
        gr.Slider(minimum=0, maximum=2, label="slope"),
        gr.Slider(minimum=0, maximum=4, label="ca"),
        gr.Slider(minimum=0, maximum=3, label="thal"),
        gr.Slider(minimum=0, maximum=1, label="target"),
    ],
    outputs="text",
    title="Health Prediction",
    description="Enter the parameters and see the health prediction.",
)

iface.launch()

