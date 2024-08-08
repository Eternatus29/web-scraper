import requests
import bs4
import spacy
from transformers import __version__ as transformers_version
import torch

# I created this file to find out the versions of the libraries I used in the project. This helped me to create a requirements.txt file.
print(f"requests version: {requests.__version__}")
print(f"beautifulsoup4 version: {bs4.__version__}")
print(f"spacy version: {spacy.__version__}")
print(f"transformers version: {transformers_version}")
print(f"torch version: {torch.__version__}")