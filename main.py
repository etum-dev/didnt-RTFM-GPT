import argparse
import os

import gpt
import pdfhandler


parser = argparse.ArgumentParser()

parser.add_argument("-u","--url", help="Website to parse (use with caution!)", type=str)
parser.add_argument("-o","--out", help="Out pdf dir. default is pdfs in tmp.", type=str, default="/tmp/pdfs")
parser.add_argument("-f","--file", help="Local document.")
parser.add_argument("-os","--outputStyle", help="Style of output. basic, explain, fuzzable. \n Basic = attempts to make full URLs, POST Requests in a curl-format, and lastly a table of possible creds.\n Explanatory: More verbose. Tries to TLDR the purpose of the API call. \n fuzzable: Appends FUZZ on endpoints. ",default="basic")
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
                os.mkdir(args.out)

if args.outputStyle:
    if "basic" or "fuzzable" or "explain" in args.outputStyle:
        style = args.outputStyle
if args.url:
    # TODO: for the future, maybe the siteToPdf is bloat and I can just send the text directly . func can remain for file pdf tho.
    pdf = pdfhandler.siteToPdf(args.url,args.out)
    gpt.parseDoc(pdf,style)
if args.file:
    gpt.parseDoc(args.file,style)

