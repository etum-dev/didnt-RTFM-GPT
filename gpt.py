from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

# TODO: clear errors if failing to parse
client = OpenAI(
    api_key=os.environ.get("API_KEY")
)

def parseDoc(document):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a silent assistant who will look for URL/URIs, API endpoints, SDK code, et-cetera in a supplied PDF-document, as well as potential default secrets in the document."},
            {
                "role": "user",
                "content": "Please parse the supplied document and return a list of all the interesting endpoints as a full URL. If no full URL is specified in the document, try to see if they use a \{placeholder\} and use that. Otherwise, set <your-web-here>. After generating a list of these URLs, make a new line, and generate a list of potential default secrets - such as admin:admin."
            }
        ]
    )

    print(completion.choices[0].message)