from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import PyPDFLoader, EmailLoader
from langchain_core.documents import Document
import os
import pandas as pd

embeddings=OllamaEmbeddings(model="mxbai-embed-large:latest")
db_location="./chrome_langchain_db "
add_docs= not os.path.exists(db_location)
