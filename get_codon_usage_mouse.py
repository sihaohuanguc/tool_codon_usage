#!/usr/bin/env python
# -*- coding: utf-8

import os,sys
from retain_longest_only import retain_longest_only
from collect_region_range import collect_region_range
from collect_CDS_sequences import collect_CDS_sequences
from generate_codon_table import generate_codon_table,remove_stop

def main():
    
    in_ref=sys.argv[1]
    in_anno=sys.argv[2]
    out_file=sys.argv[3]

    print(in_ref,in_anno,out_file)

    ban_file_names=["temp.gff3","range.pkl","CDS.fa","CDS.csv"]

    if in_ref in ban_file_names:  # prevent covering the files or deleting them accidentally
        print(f"Please change the name for {in_ref}. Exit.")
        exit(10)
    elif in_anno in ban_file_names:
        print(f"Please change the name for {in_anno}. Exit.")
        exit(10)

    retain_longest_only(in_anno,"temp.gff3")
    collect_region_range("temp.gff3","range.pkl")
    collect_CDS_sequences("range.pkl",in_ref,"CDS.fa")
    generate_codon_table("CDS.fa","CDS.csv")
    remove_stop("CDS.csv",out_file)

    # os.system("rm temp.gff3 range.pkl CDS.fa CDS.csv")

if __name__ == "__main__":
    main()