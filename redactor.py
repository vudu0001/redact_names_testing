# -*- coding: utf-8 -*-
# Example main.py
import argparse
from project3 import main
import sys

def mains(args):
    i=0
    stats={}
    # Getting the input data
    if args.input:
        #print(args.input)
        input_data=main.Read_file(args.input)

    if args.names:
    # Reading names
        input_data, count=main.Redact_names(input_data)
        stats['Redactd Names']=count

    if args.output:
    # Writing data into a File
        directory = args.output[0:len(args.output)-1]
        main.write_output(input_data,directory)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', action='append', help="Input Files", nargs='*', required=True)
    parser.add_argument('--names', action='store_true', help='Redact_names', required=False)
    parser.add_argument('--output', help='write_output', required=False)
    args=parser.parse_args()

    mains(args)
