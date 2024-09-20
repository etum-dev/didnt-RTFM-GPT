import requests

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas 

# There's no validation (yet) - Be careful what you're scraping. Otherwise you'll probably have a shell on your system soon... :)

def siteToPdf(url,outfile):
    # TODO: append http(s) if not present
    r = requests.get(url)
    #its ugly, gpt-chan wont judge.
    html = r.text
    print(r.text)
    pdf = canvas.Canvas(outfile, pagesize=A4)
    width=150
    height=200
    pdf.drawString(width,height,html)
    pdf.showPage()
    pdf.save()


