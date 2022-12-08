# General
This repo is a small tool used for generating the codon usage count table for mouse.

# package version
Python 3.8.8

| Software | Version    |
| :---:   | :---: |
| Python | 3.8.8 |
| Pandas | 1.2.4 |


# Usage
Please run the following script in the terminal. Replace the reference, annotation and output file path. The input annotation file is supposed to be in the gff3 format. Stop codons are removed. The version numbers in the gene ID (the part after the decimal) are removed in the output file. It usually takes ~ 1 min to run the script on your local device.
```bash
python get_codon_usage_mouse.py GRCm39.genome.fa gencode.vM30.annotation.gff3 CDS_mouse.csv
```