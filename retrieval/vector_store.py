import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("code_review_knowledge")

def add_documents(docs, metadatas, ids):
    collection.add(
        documents=docs,
        metadatas=metadatas,
        ids=ids
    )