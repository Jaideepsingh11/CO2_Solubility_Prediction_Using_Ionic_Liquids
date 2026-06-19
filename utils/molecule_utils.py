from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors


def get_molecule_info(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid SMILES")

    svg = Draw.MolsToGridImage(
        [mol],
        molsPerRow=1,
        subImgSize=(400, 300),
        useSVG=True
    )

    molecular_weight = Descriptors.MolWt(mol)

    return {
        "image": svg,
        "molwt": round(molecular_weight, 2)
    }