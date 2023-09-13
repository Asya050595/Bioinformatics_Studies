from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem, Lipinski
import rdkit.Chem.Lipinski as Lipinksi
import pubchempy as pcp
import nglview as nv

ibu = Chem.MolFromSmiles('CC(C)CC1=CC=C(C=C1)C(C)C(=O)O')
Draw.MolToFile(ibu, 'ipuprophen.png')

print(Lipinksi.NumHDonors(ibu))
print(Lipinksi.NumHAcceptors(ibu))
print(Lipinksi.rdMolDescriptors.CalcExactMolWt(ibu))
print(Lipinksi.rdMolDescriptors.CalcCrippenDescriptors(ibu)[0])

def check_Lipinski(mol):
    is_Lipinsky = bool((Lipinski.NumHDonors(mol) <= 5) \
    and (Lipinski.NumHAcceptors(mol) <= 10) \
    and (Lipinski.rdMolDescriptors.CalcExactMolWt(mol) < 500) \
    and(Lipinski.rdMolDescriptors.CalcCrippenDescriptors(mol)[0]) <= 5)
    return is_Lipinsky

ne_ibu_smiles = []
smiles = []
compounds = []
per_page = 10**5
for smi in smiles:
    if "N=[N+]=[N-]" in smi:
        newsmi = smi.replace("N=[N+]=[N-]", ne_ibu_smiles)
    else:
        continue
    for i in range(200):
        try:
            a = pcp.get_properties(
              properties="CanonicalSMILES",
              identifier=smiles, namespace="Smiles",
              searchtype="substructure",
              RingsNotEmbedded=True,
              listkey_count=per_page, listkey_start=i*per_page
            )
            if check_Lipinski(newsmi):
                compounds.append((newsmi))
        except Exception:
            pass
print(len(compounds))

m3d=Chem.AddHs(ibu)
Chem.AllChem.EmbedMolecule(m3d)
AllChem.MMFFOptimizeMolecule(m3d,maxIters=500,nonBondedThresh=200 )
nv.show_rdkit(m3d)
