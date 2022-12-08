#!/usr/bin/env python
# -*- coding: utf-8

import pickle

def collect_region_range(in_file,out_file):

    dict1={}
    dict2={}
    with open(out_file,"wb+") as out_f:
        with open(in_file,"r") as f:
            for line in f:
                if not line[0]=="#":
                    elements=line.strip("\n").split("\t")

                    infos=elements[8].split(";")
                    temp_dict={}
                    for item in infos:
                        temp_dict[item.split("=")[0]]=item.split("=")[1]

                    transcript_ID=temp_dict["gene_name"] # it's actually gene name now

                    if elements[2]=="transcript":
                        dict1[transcript_ID]={}
                        dict1[transcript_ID]["gene_ID"]=temp_dict["gene_id"].split(".")[0]
                        dict1[transcript_ID]["strand"]=elements[6]
                        dict1[transcript_ID]["chrom"]=elements[0]
                    elif elements[2] in ["CDS"]:
                        if not elements[2] in dict1[transcript_ID].keys():
                            dict1[transcript_ID][elements[2]]=[]
                        dict1[transcript_ID][elements[2]].extend([(int(elements[3]),int(elements[4]))])

        for key in dict1:
            if len(dict1[key])>1:
                dict2[key]=dict1[key]

        out_f.write(pickle.dumps(dict2))
             
        