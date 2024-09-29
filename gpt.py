from openai import OpenAI
from dotenv import load_dotenv
import os

from pdfminer.high_level import extract_text

load_dotenv() 

# TODO: clear errors if failing to parse
client = OpenAI(
    api_key=os.environ.get("API_KEY")
)

def extractText(document):
    text = extract_text(document)
    pageText = []
    return text

def parseDoc(document,outputStyle="basic"):
    text = []
    if outputStyle == "basic":
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            # TODO: split job, we can use Pagination.
            
            messages=[
                    {"role": "system", 
                    "content": "You are a silent assistant who will look for URL/URIs, API endpoints, SDK code, et-cetera in a supplied PDF-document, as well as potential default secrets in the document. Please parse the supplied document and return a list of all the interesting endpoints as a full URL. If no full URL is specified in the document, try to see if they use any kind of placeholder and use that. In the case of a POST request, return these in a curl-format. If any specific data is required in eg a POST request, add this in your output as well. Otherwise, set <your-web-here>. After generating a list of these URLs, make a new line, and generate a list of potential default secrets - such as admin:admin."},
                    {
                        
                    
                    "role": "user",
                    "content": "test. no doc."
                    }
                ]
        )

        print(completion.choices[0].message)