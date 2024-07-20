from flask import Blueprint, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

# Current directory
current_dir = os.path.dirname(__file__)

# Create blueprint
visiona_bp = Blueprint('visiona', __name__, template_folder='template')

# Function to load model
def load_model():
    model_path = os.path.join(current_dir, 'VISIONA.pkl')
    print(f"Intentando cargar el modelo desde: {model_path}")
    try:
        model = joblib.load(model_path)
        print("Modelo cargado exitosamente")
        return model
    except Exception as e:
        print(f"Error al cargar el modelo: {str(e)}")
        raise

# Function to preprocess input data
def preprocess_input(data):
    processed_data = {}
    for key, value in data.items():
        try:
            processed_data[key] = float(value.replace(',', ''))
        except ValueError:
            processed_data[key] = 0.0
    return processed_data

# Home page
@visiona_bp.route('/')
def home():
    return render_template('index.html')

# Prediction page
@visiona_bp.route('/prediction', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the data from form
            input_data = {
                'id_municipio': request.form['id_municipio'],
                'habitantes': request.form['habitantes'],
                'accidentes': request.form['accidentes'],
                'vic_masculina': request.form['vic_masculina'],
                'vic_femenino': request.form['vic_femenino']
            }

            # Preprocess input data
            processed_data = preprocess_input(input_data)

            # Create DataFrame
            df = pd.DataFrame([processed_data])

            # Add 'estatus' column with a default value
            df['estatus'] = 0  # Add this line

            # Load model and make prediction
            model = load_model()
            prediction = model.predict(df)[0]

            # Determine the output
            result = 'El municipio es peligroso.' if prediction == 1 else 'El municipio no es peligroso.'

            return render_template('prediction.html', prediction=result)
        except Exception as e:
            print(f"Error durante la predicción: {str(e)}")
            return render_template('error.html', message="Ocurrió un error durante la predicción. Por favor, inténtelo de nuevo.")
    
    # If not POST method
    return render_template('error.html', message="Método no permitido")