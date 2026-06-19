import pandas as pd

from rdkit import Chem
from rdkit.Chem import Descriptors


TOP_FEATURES = [
    "Pressure (bar)",
    "Temperature (0 C)",
    "Cat_MolLogP",
    "Cat_EState_VSA2",
    "An_TPSA",
    "Cat_VSA_EState3",
    "An_AvgIpc",
    "An_SlogP_VSA1",
    "Cat_TPSA",
    "Cat_EState_VSA9",
    "Cat_BCUT2D_LOGPLOW",
    "Cat_NumHDonors",
    "Cat_SMR_VSA5",
    "Cat_SMR_VSA1",
    "Cat_PEOE_VSA1",
    "Cat_NHOHCount",
    "Cat_EState_VSA8",
    "Cat_Chi4v",
    "An_BalabanJ",
    "An_PEOE_VSA3"
]


def generate_descriptors(
    cation_smiles,
    anion_smiles,
    temperature,
    pressure
):

    cation_mol = Chem.MolFromSmiles(
        cation_smiles
    )

    anion_mol = Chem.MolFromSmiles(
        anion_smiles
    )

    if cation_mol is None:
        raise ValueError(
            "Invalid Cation SMILES"
        )

    if anion_mol is None:
        raise ValueError(
            "Invalid Anion SMILES"
        )

    cat_desc = Descriptors.CalcMolDescriptors(
        cation_mol
    )

    an_desc = Descriptors.CalcMolDescriptors(
        anion_mol
    )

    cat_desc = {
        "Cat_" + key: value
        for key, value in cat_desc.items()
    }

    an_desc = {
        "An_" + key: value
        for key, value in an_desc.items()
    }

    features = {}

    features["Pressure (bar)"] = pressure
    features["Temperature (0 C)"] = temperature

    features.update(cat_desc)
    features.update(an_desc)

    final_features = {
        col: features[col]
        for col in TOP_FEATURES
    }

    return pd.DataFrame(
        [final_features]
    )