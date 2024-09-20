import requests
from reportlab.pdfgen import canvas

# There's no validation (yet) - Be careful what you're scraping. Otherwise you'll probably have a shell on your system soon... :)

#TODO: set uesr option for url
testurl="http://etum.wtf"
# TODO: set user option for outfile
outfile="1.pdf" 

def siteToPdf(url):
    r = requests.get(url)
    #its ugly, gpt-chan wont judge.
    html = r.text
    print(r.text)
    pdf = canvas.Canvas(outfile)
    pdf.drawString(200,200,html)
    pdf.showPage()
    pdf.save()


siteToPdf(testurl)
