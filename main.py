import openai
import os
import argparse
from dotenv import load_dotenv

import pdfhandler

load_dotenv()
parser = argparse.ArgumentParser()

parser.add_argument("-u","--url", help="Website to parse (use with caution!", type=str)
parser.add_argument("-o","--out", help="Out pdf name. default is document.pdf in tmp.", type=str, default="/tmp/document.pdf")
args = parser.parse_args()

if args.url:
                    pdfhandler.siteToPdf(args.url,args.out)
