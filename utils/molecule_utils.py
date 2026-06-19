from rdkit import Chem
from rdkit.Chem import Descriptors


def get_molecule_info(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid SMILES")

    molecular_weight = Descriptors.MolWt(mol)

    return {
        "image": None,
        "molwt": round(molecular_weight, 2)
    }