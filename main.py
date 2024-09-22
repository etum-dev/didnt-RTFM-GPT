import argparse
import os

import gpt
import pdfhandler


parser = argparse.ArgumentParser()

parser.add_argument("-u","--url", help="Website to parse (use with caution!", type=str)
parser.add_argument("-o","--out", help="Out pdf dir. default is pdfs in tmp.", type=str, default="/tmp/pdfs")
args = parser.parse_args()

if args.out: 
    if os.path.exists(args.out):
        pass
    else:
        print("Folder does not exist, should it be created? Y/N")
        prompt = input("Y/N: ")
        if prompt:
            p = prompt.upper()
            if p != "Y":
                print("Cancelled.")
            else:
                pass


if args.url:
    pdf = pdfhandler.siteToPdf(args.url,args.out)
    gpt.parseDoc(pdf)

