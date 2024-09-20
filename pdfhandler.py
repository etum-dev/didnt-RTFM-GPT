import requests

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# TODO: delete if unecessary
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas 

# There's no validation (yet) - Be careful what you're scraping. Otherwise you'll probably have a shell on your system soon... :)

def siteToPdf(url,outfile):
    # TODO: append http(s) if not present
    r = requests.get(url)
    #its ugly, gpt-chan wont judge.
    html = r.text
    
    pdf = SimpleDocTemplate(outfile)
    w = 300
    h = 500
    Story = [Spacer(w,h)]
    #style = styles["Normal"]
    #pdf.setFont('Times-Roman',9)
    Story.append(Paragraph(html))
    Story.append(Spacer(100,100))
    pdf.build(Story)
    #pdf.showPage()
    #pdf.save()


