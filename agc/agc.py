
Conversation ouverte. 1 message lu.

Aller au contenu
Utiliser Gmail avec un lecteur d'écran
Meet
Hangouts
6 sur 9 627
amine gozlane
Boîte de réception
Grace Djiraibe <grace.djiraibe@gmail.com>
	
Pièces jointes08:54 (il y a 12 heures)
	
À moi

Zone contenant les pièces jointes
	
	
	

#!/bin/env python3
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    A copy of the GNU General Public License is available at
#    http://www.gnu.org/licenses/gpl-3.0.html

"""OTU clustering"""

import argparse
import sys
import os
import gzip
import statistics
from collections import Counter
# https://github.com/briney/nwalign3
# ftp://ftp.ncbi.nih.gov/blast/matrices/
import nwalign3 as nw

__author__ = "Grace Djiraïbe"
__copyright__ = "Universite de Paris"
__credits__ = ["Grace Djiraïbe"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Grace Djiraibe"
__email__ = "grace.djiraibe@gmail.com"
__status__ = "Developpement"


def isfile(path):
    """Check if path is an existing file.
      :Parameters:
          path: Path to the file
    """
    if not os.path.isfile(path):
        if os.path.isdir(path):
            msg = "{0} is a directory".format(path)
        else:
            msg = "{0} does not exist.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


def get_arguments():
    """Retrieves the arguments of the program.
      Returns: An object that contains the arguments
    """
    # Parsing arguments
    parser = argparse.ArgumentParser(description=__doc__, usage=
                                     "{0} -h"
                                     .format(sys.argv[0]))
    parser.add_argument('-i', '-amplicon_file', dest='amplicon_file', type=isfile, required=True, 
                        help="Amplicon is a compressed fasta file (.fasta.gz)")
    parser.add_argument('-s', '-minseqlen', dest='minseqlen', type=int, default = 400,
                        help="Minimum sequence length for dereplication (default 400)")
    parser.add_argument('-m', '-mincount', dest='mincount', type=int, default = 10,
                        help="Minimum count for dereplication  (default 10)")
    parser.add_argument('-c', '-chunk_size', dest='chunk_size', type=int, default = 100,
                        help="Chunk size for dereplication  (default 100)")
    parser.add_argument('-k', '-kmer_size', dest='kmer_size', type=int, default = 8,
                        help="kmer size for dereplication  (default 10)")
    parser.add_argument('-o', '-output_file', dest='output_file', type=str,
                        default="OTU.fasta", help="Output file")
    return parser.parse_args()

def read_fasta(amplicon_file, minseqlen):
    '''
    Function that tsakes as arguments a fasta file and the seqeunce length.

    PARAMETERS
    ----------
        ** amplicon_file : str
            The file name.
        ** mineseqlen : int
            The minimun sequence size.
    RETURNS
    -------
        ** Generator of seqeunces.
    '''
    # En raison des restriction github amplicon fasta.gz devra rester compréssée.
    if amplicon_file.endswith("gz"):
        with gzip.open("amplicon.fasta.gz", "rt") as fasta_file:
            for line in fasta_file:
                if not line.startswith(">"):
                    if len(line) >= minseqlen:
                        yield line
    else:
        with open(amplicon_file, "r") as fasta_file:
            for line in fasta_file:
                if not line.startswith(">"):
                    if len(line) >= minseqlen:
                        yield line 



def dereplication_fulllength(amplicon_file, minseqlen, mincount):
    '''
    This function is using the generator create buy read_fasta.

    PARAMETERS
    ----------
    ** amplicon_file : str
        The file name.
    ** mineseqlen : int
        The minimun sequence size.
    ** minecount : 
        The minimun amount of couting.

    RETURNS
    -------
    ** Sequences in descending order of accuracy yield[seq, my_seq_count]
    '''

    seq_amplicon = {}
    for amplicon in read fasta_file(amplicon_file,minseqlen):
        if amplicon not in seq_amplicon.keys():
            seq_amplicon[amplicon] = 1
        else:
            seq_amplicon[amplicon] += 1
    for seq, my_seq_count in sorted(seq_amplicon.items(), key=lamda item: item[1], reverse = True):
        if count >= mincount:
            yield[seq, my_seq_count]


def get_unique(ids):
    return {}.fromkeys(ids).keys()


def common(lst1, lst2): 
    return list(set(lst1) & set(lst2))


def get_chunks(sequence, chunk_size):
    """"""
    len_seq = len(sequence)
    if len_seq < chunk_size * 4:
        raise ValueError("Sequence length ({}) is too short to be splitted in 4"
                         " chunk of size {}".format(len_seq, chunk_size))
    return [sequence[i:i+chunk_size] 
              for i in range(0, len_seq, chunk_size) 
                if i+chunk_size <= len_seq - 1]


def cut_kmer(sequence, kmer_size):
    """Cut sequence into kmers"""
    for i in range(0, len(sequence) - kmer_size + 1):
        yield sequence[i:i+kmer_size]

def get_identity(alignment_list):
    """Prend en une liste de séquences alignées au format ["SE-QUENCE1", "SE-QUENCE2"]
    Retourne le pourcentage d'identite entre les deux."""
    id_nu = 0
    for i in range(len(alignment_list[0])):
        if alignment_list[0][i] == alignment_list[1][i]:
            id_nu += 1
    return round(100.0 * id_nu / len(alignment_list[0]), 2)

def chimera_removal(amplicon_file, minseqlen, mincount, chunk_size, kmer_size):
    '''
    
    '''

def abundance_greedy_clustering(amplicon_file, minseqlen, mincount, chunk_size, kmer_size):
    pass

def fill(text, width=80):
    """Split text with a line return to respect fasta format"""
    return os.linesep.join(text[i:i+width] for i in range(0, len(text), width))

def write_OTU(OTU_list, output_file):
    pass

#==============================================================
# Main program
#==============================================================
def main():
    """
    Main program function
    """
    # Get arguments
    args = get_arguments()
    # Votre programme ici


if __name__ == '__main__':
    main()



agc.py
Affichage de agc.py en cours...
