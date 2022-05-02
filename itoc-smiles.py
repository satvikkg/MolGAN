import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools as pt

def itoc_smiles(self):
	sdf = pt.LoadSDF(self)
	sdf['can-smiles'] = [Chem.MolToSmiles(mol, isomericSmiles=False)for mol in sdf['ROMol']]
	print(sdf.shape)
	df = sdf.drop(['ROMol'],axis=1)
	df.to_csv(f'{os.path.split(self)[0]}/converted.csv',index=False)
	print("Conversion complete")
	
itoc_smiles("/home2/satvik/ml_dl/molGAN/enamie-diversity-dd2-50240/Enamine_Discovery_Diversity_Set_50240_DDS-50_20211022.sdf")
