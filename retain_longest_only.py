#!/usr/bin/env python
# -*- coding: utf-8

def retain_longest_only(in_file,out_file):
    with open(out_file,"w+") as out_f:
        with open(in_file,"r") as f:
            len_list=[]
            info_list=[]
            for line in f:
                if line[0]=="#" and not line[1]=="#":
                    out_f.write(line)  
                elif not line[0]=="#":
                    elements=line.strip("\n").split("\t")
                    if elements[2]=="gene":
                        if not len(len_list)==0:
                            out_block=info_list[len_list.index(max(len_list))]
                            for item in out_block:
                                out_f.write(item)
                            len_list=[]
                            info_list=[]
                    elif elements[2]=="transcript" and elements[8].split(";")[6].split("=")[1]=="protein_coding": # yes there are transcripts for protein coding genes that are not protein coding transcripts
                        len_list.append(int(elements[4])-int(elements[3]))
                        info_list.append([line])
                    elif elements[2]=="transcript" and elements[8].split(";")[6].split("=")[1]!="protein_coding": # yes there are transcripts for protein coding genes that are not protein coding transcripts
                        len_list.append(-100) # it's easy to make it never the longest, just asign a length with is < 0
                        info_list.append([line])
                    else:
                        info_list[-1].append(line)

                
                
    