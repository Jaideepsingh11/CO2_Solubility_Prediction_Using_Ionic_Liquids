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

    return (
    float(prediction[0]),
    features
)