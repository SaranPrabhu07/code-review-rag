from .vector_store import collection


def retrieve_by_category(query, category):

    results = collection.query(
        query_texts=[query],
        where={"category": category},
        n_results=3
    )

    return results["documents"][0]


def dynamic_retrieval(query, risks):

    all_docs = []

    if not risks:
        # fallback retrieval
        results = collection.query(
            query_texts=[query],
            n_results=3
        )
        return results["documents"][0]

    for risk in risks:
        docs = retrieve_by_category(query, risk)
        all_docs.extend(docs)

    return all_docs
