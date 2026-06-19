import pickle
import os

from utils.descriptor_generator import (
    generate_descriptors
)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "xgboost_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


def predict_solubility(
    cation_smiles,
    anion_smiles,
    temperature,
    pressure
):

    features = generate_descriptors(
        cation_smiles,
        anion_smiles,
        temperature,
        pressure
    )

    prediction = model.predict(
    features
)

    final_prediction = float(
    prediction[0]
)

    if final_prediction < 0:
        final_prediction = 0.0

    return (
    final_prediction,
    features
)