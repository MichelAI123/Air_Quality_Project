from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# 1. Initialiser l'API
app = FastAPI(
    title="API de prédiction de la qualité de l'air",
    description="API pour prédire la qualité de l'air en Inde",
    version="1.0.0"
)

# 2. Charger le modèle au démarrage
# model = joblib.load("best_xgb_model.pkl")
# 2. Charger le modèle au démarrage
model = None
try:
    model = joblib.load("best_xgb_model.pkl")
except FileNotFoundError:
    print("⚠️ Erreur : Le fichier modèle 'best_xgb_model.pkl' est introuvable.")
except Exception as e:
    print(f"⚠️ Erreur lors du chargement du modèle : {e}")


# 3. Définir la structure des données d'entrée (A ADAPTER selon vos features)
class AirQualityInput(BaseModel):
    PM2_5: float  # représente PM2.5 dans les données d'entraînement
    PM10: float
    NO: float
    NO2: float
    NOx: float
    NH3: float
    CO: float
    SO2: float
    O3: float
    Benzene: float
    Toluene: float
    Xylene: float
    City_Frequency_Encoded: float
    annee: int
    mois: int
    jour: int

# 4. Route de santé (Health Check)
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API opérationnelle"}

# 5. Route de prédiction
@app.post("/predict")
def predict(data: AirQualityInput):
    if model is None:
        return {"error": "Modèle non chargé"}

    # Convertir les données reçues en dict
    data_dict = data.dict()

    # Renommer PM2_5 → PM2.5 pour correspondre au modèle
    data_dict["PM2.5"] = data_dict.pop("PM2_5")

    # Ordre attendu des colonnes par le modèle
    columns_order = [
        "PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2",
        "O3", "Benzene", "Toluene", "Xylene",
        "City_Frequency_Encoded", "annee", "mois", "jour"
    ]

    # Construire un DataFrame propre
    input_df = pd.DataFrame([data_dict])[columns_order]

    # Prédiction
    try:
        prediction = model.predict(input_df)
        return {
            "prediction": float(prediction[0]),
            "message": "Prédiction réussie"
        }
    except Exception as e:
        return {"error": f"Erreur lors de la prédiction : {e}"}
