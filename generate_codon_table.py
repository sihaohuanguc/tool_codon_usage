#!/usr/bin/env python
# -*- coding: utf-8

import csv
import pandas as pd
from codon_dict import codon_dict

def generate_codon_table(in_file,out_file):

    base_list=["A","C","G","T"]
    codon_list=[] # used for calculating codon counts, there are T in the sequences
    for i in range(4):
        for j in range(4):
            for k in range(4):
                codon_list.append("".join([base_list[i],base_list[j],base_list[k]]))

    codon_list_for_output=[] # used for the head line
    for item in codon_list:
        codon=item.replace("T","U")
        aa=codon_dict[codon[0]][codon[1]][codon[2]]
        codon_list_for_output.append(aa+"_"+codon)

    with open(out_file,"w+") as out_f:
        writer=csv.writer(out_f)
        first_line=["gene_ID","gene_name","chrom","strand","length_aa"]
        first_line.extend(codon_list_for_output)
        writer.writerow(first_line)
        with open(in_file,"r") as f:
            for line in f:
                if line[0]==">":
                    out_line=line.strip(">").strip("\n").split("_")[:4] # "gene" to "strand"
                # elif line[:3]=="ATG":  # we assume that all protein start with ATG
                else:
                    line=line.strip("\n")
                    codons=[line[i:(i+3)] for i in range(0,len(line),3)]
                    if len(codons[-1])<3:
                        del codons[-1]
                    out_line.append(len(codons))  # length_aa
                    out_codon_counts=[0 for i in range(64)]
                    # print(codons)
                    for item in codons:
                        out_codon_counts[codon_list.index(item)]+=1
                    out_line.extend(out_codon_counts)
                    writer.writerow(out_line)


def remove_stop(in_file,out_file):

    df=pd.read_csv(in_file)
    df.drop(["stop_UAA","stop_UAG","stop_UGA"],axis=1,inplace=True)
    df.to_csv(out_file,index=False)


