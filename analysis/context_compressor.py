def compress_context(docs):

    # simple version
    compressed = []

    for doc_list in docs:
        for doc in doc_list:
            compressed.append(doc[:200])

    return "\n".join(compressed)
