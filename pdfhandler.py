from bs4 import BeautifulSoup

import requests

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# TODO: delete if unecessary
from reportlab.rl_config import defaultPageSize
#from reportlab.pdfgen import canvas 


def stripHTML(html):
    # Function to fix html for PDF generation. (<a href=> messes up for example)
    soup = BeautifulSoup(html)
    strHtml = soup.get_text()
    return strHtml

def pdfCheck(size):
    # Function to validate PDF size.
    pass

def spider():
    pass

def siteToPdf(url,outfolder):
    n = 0
    pdfFile = f"{n}.pdf"
    if "http" not in url:
        url = "http://"+url
    r = requests.get(url)
    html=r.text
    #TODO: if multi-page, spider it.
    #TODO: as GPT can't take too much text, split into multiple PDFs.
    #TODO: If pages > 5, split

    pdf = SimpleDocTemplate(outfolder+"/"+pdfFile)
    w = 100
    h = 100
    Story = [Spacer(w,h)]
    try: 
        Story.append(Paragraph(stripHTML(html)))
        
    except Exception as err:
        print(err)
        exit()
    pdf.build(Story)
    return pdf



