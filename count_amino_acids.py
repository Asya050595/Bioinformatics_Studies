from collections import Counter
from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1
import sys
import os
from os import listdir

d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K', \
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', \
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', \
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

def triple_aa(val):
    for key, value in d.items():
         if val == value:
             return key


def single_aa(x):
    for i in x:
        return i


with open('countfile' , 'w') as out:
    for fname in listdir('/home/asik/Документы'):
        if fname.endswith('.pdb') and os.path.isfile(fname):
            with open(fname, 'r') as f:
                pdbparser = PDBParser()
                structure_id = fname.rsplit('.pdb')
                structure = pdbparser.get_structure(structure_id, fname)
                for chain in structure.get_chains():
                    chains = {chain.id:seq1(''.join(residue.resname for residue in chain)) \
                              for chain in structure.get_chains()}
                for l, m in chains.items():
                    newList = Counter(m)
                for k, v in newList.items():
                    out.write('{k} {v} {f}\n'.format(k = triple_aa(k), v = v, f = fname))
                    out.write('{k} {v} {f}\n'.format(k = single_aa(k), v = v, f = fname))

