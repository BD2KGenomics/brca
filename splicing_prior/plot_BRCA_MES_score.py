"""
Note: these things are the same:
3' of an intron == 5' of the next exon == splice acceptor == 23nt sequence
5' of an intron == 3' of the previous exon == splice donor == 9nt sequence 
"""

from matplotlib import pyplot as plt
import numpy as np
from pprint import pprint as pp


BRCA1 = "../resources/genome_sequences/brca1_hg38_no_flanking.txt"
BRCA2 = "../resources/genome_sequences/brca2_hg38_no_flanking.txt"
REFSEQ = "../resources/refseq/hg38.BRCA.refGene.txt"


def main():
    create_MES_inputfile()
    #plot_score("BRCA1")

def get_exon_boundaries(gene):
    """
    return splicing donor (5' end of intron) sites
     and splicing acceptor (3' end of intron) list as two lists
    """
    brca2_refseq, brca1_refseq, dummy = open(REFSEQ, "r").read().split("\n")
    refseq = {"BRCA1": brca1_refseq.split("\t"),
              "BRCA2": brca2_refseq.split("\t")}
    #exon_starts = refseq[gene][9][:-1].split(",") # splicing acceptors
    #exon_ends = refseq[gene][10][:-1].split(",") # splicing donors
    return refseq
    #exon_starts, exon_ends


def plot_score(gene):
    scores = get_MES_score(gene)
    print len(scores['3'])
    print len(scores['5'])
#    plt.plot(scores)
#    plt.title("BRCA1")
#    plt.legend(["3 prime", "5 prime"])
#    plt.show()


def get_MES_score():
    for direction in scores.keys():
        f = open("MES_data/{0}_{1}_{2}.txt".format(gene, sj, strand), "r")
        for line in f:
            scores[direction].append(float(line.strip().split("\t")[1]))
        scores[direction] = np.array(scores[direction])
        scores[direction][scores[direction]<=6] = 6
    return scores


def create_MES_inputfile():
    """
    8 files: BRCA1/BRCA2, postive/negative strand, splice donor/acceptor
    """
    files = {"BRCA1": BRCA1, "BRCA2": BRCA2}
    sj_dict = {"donor": 9, "acceptor": 23}
    sequence = {"+": "", "-": ""}
    for gene in ["BRCA1", "BRCA2"]:
        sequence["+"] = open(files[gene], "r").read().upper().strip()
        sequence["-"] = reverse_complement(sequence["+"])
        for strand in ["+", "-"]:
            for sj, window in sj_dict.iteritems():
                f_out = open("MES_data/{0}_{1}_{2}.txt".format(gene, sj, strand), "w")
                for i in range(len(sequence[strand]) - window + 1):
                    f_out.write(sequence[strand][i: i+window] + "\n")
                f_out.close()


def run_MaxEntScan():
    """"
    run MaxEntScan by calling shell script
    """
    pass



def reverse_complement(sequence):
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join([complement[each] for each in sequence[::-1]])


if __name__ == "__main__":
    main()
