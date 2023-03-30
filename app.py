import gradio as gr
import numpy as np
import joblib
from extractor import main
import sys




# Define a function to make predictions
def predict_phishing_website(url):
    features = main(url)
    features = np.array(features).reshape((1, -1))
    model = joblib.load('model\gbc.pkl')
    
    return int(model.prefict(features)[0])

# Create a Gradio interface
gr.Interface(fn=predict_phishing_website, 
             inputs="text", 
             outputs="text", 
             title="Phishing Website Detector",
             description="Enter a website URL to determine whether it's safe or phishing").launch()