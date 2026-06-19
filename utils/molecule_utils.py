from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors


def get_molecule_info(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid SMILES")

    image = Draw.MolToImage(
        mol,
        size=(350, 250)
    )

    molecular_weight = Descriptors.MolWt(mol)

    tpsa = Descriptors.TPSA(mol)

    logp = Descriptors.MolLogP(mol)

    return {
        "image": image,
        "molwt": round(molecular_weight, 2),
        
    }