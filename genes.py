from Bio import Phylo
from Bio import SeqIO
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Entrez
from Bio import SeqIO
from Bio import GenBank 
import csv 
import re 
import matplotlib
import matplotlib.pyplot as plt
from Bio.Align.Applications import ClustalwCommandline
import os

def descargar():
    """" 
    La funcion fasta_downloader permite:
        1. Convertir un .txt con ids de datos de genbank en lista
        2. Para despues obtener la secuencia de cada id en formato genbank
        3. Guardar los datos obtenidos en un documento .gb del tipo genbank
    """
    with open('gen1.txt', 'r+') as list:
            id_CTX_M_55 = list.readlines()
            Entrez.email = "pmbarba@gmail.com"
            CTX_M_55 = []
            for ids in id_CTX_M_55:
                 handle = Entrez.efetch(db="nucleotide", id=ids, rettype="gb", retmode="text")
                 secuencias = SeqIO.read(handle, "genbank")
                 CTX_M_55.append(secuencias)
                 SeqIO.write(CTX_M_55, "gen1.gb", "genbank")
                
