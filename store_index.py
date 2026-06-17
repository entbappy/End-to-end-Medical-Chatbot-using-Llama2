from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone client (v3+ API)
pc = Pinecone(api_key=PINECONE_API_KEY)


index_name="medical-bot"

# Create index if it doesn't exist (required for Pinecone v3+ serverless)
existing_indexes = [i.name for i in pc.list_indexes()]
if index_name not in existing_indexes: 
    pc.create_index(
        name=index_name,
        dimension=384,  # all-MiniLM-L6-v2 embedding dimension
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    # Wait for index to be ready
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

#Creating Embeddings for Each of The Text Chunks & storing
docsearch = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name=index_name,
)
