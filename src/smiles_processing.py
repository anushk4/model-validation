import numpy as np
from rdkit import Chem
from standardiser import standardise


def standardise_smiles(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
    except:
        mol = np.nan

    if mol:
        try:
            st_mol = standardise.run(mol)
        except:
            st_mol = np.nan

    if st_mol:
        st_smiles = Chem.MolToSmiles(mol)
    else:
        st_smiles = np.nan
        
    return st_smiles

def smile_to_inchikey(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
    except:
        mol = np.nan

    if mol:
        inchi = Chem.inchi.MolToInchi(mol)
    else:
        inchi = np.nan

    if inchi:
        inchi_key = Chem.inchi.InchiToInchiKey(inchi)
    else:
        inchi_key = np.nan

    return inchi_key