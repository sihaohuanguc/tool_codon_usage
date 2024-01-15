#!/usr/bin/env python
# -*- coding: utf-8

import pickle

def collect_CDS_sequences(in_annotate,in_ref,out_annotate):

    with open(in_annotate,"rb") as in_an:
        dict1=pickle.load(in_an)

    dict_rev={"A":"T","a":"T","C":"G","c":"G","G":"C","g":"C","T":"A","t":"A","N":"N","n":"N"}

    def rev_comp(ref):
        rev_comp=[]
        # print(ref)
        for item in ref:
            if item in "ACTGNactgn":
                rev_comp.append(dict_rev[item])
            else:
                print(item+": Wrong input!")
        rev_comp.reverse()
        return "".join(rev_comp)

    with open(in_ref,"r") as f:
        all_ref={}
        chrom_name="delete_this"
        all_sequence=[]
        for line in f:
            if line[0]==">":
                all_sequence="".join(all_sequence)
                all_ref[chrom_name]=all_sequence
                chrom_name=line.strip(">").split(" ")[0]
                all_sequence=[]
            else:
                all_sequence.append(line.strip("\n"))
        all_sequence="".join(all_sequence)
        all_ref[chrom_name]=all_sequence
        del all_ref["delete_this"]

    with open(out_annotate,"w+") as out_f:
        for key in dict1.keys():
            coding_strand=""
            if "CDS" in dict1[key].keys():
                gene_name=dict1[key]["gene_name"]
                chrom=dict1[key]["chrom"]
                strand=dict1[key]["strand"]
                for pairs in dict1[key]["CDS"]:  # the indexes are all based on the forward strand
                    if strand=="+":
                        fragment=all_ref[chrom][(pairs[0]-1):(pairs[1])]
                    if strand=="-": # the indexes are from small index to large index within the fragment, but the order of the fragments are from larger to smalles
                        fragment=rev_comp(all_ref[chrom][(pairs[0]-1):(pairs[1])])
                    coding_strand+=fragment
                # print(coding_strand,dict1[key],key)      
                out_f.write(f">{key}_{gene_name}_{chrom}_{strand}_CDS_{len(coding_strand)}\n")
                out_f.write(coding_strand+"\n")


