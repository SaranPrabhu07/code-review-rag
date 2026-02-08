import os
import re
import uuid

from retrieval.vector_store import add_documents

DATA_DIR = "data/best_practices"


# -------------------------------
# Extract semantic blocks
# -------------------------------

def parse_semantic_blocks(text):

    # Split based on --- markers
    blocks = re.split(r"\n---\n", text)

    parsed = []

    for block in blocks:
        if not block.strip():
            continue

        metadata = {}
        content = block

        # Detect YAML-like metadata
        meta_match = re.match(r"(.*?)\n\n(.*)", block, re.DOTALL)

        if meta_match:
            meta_text = meta_match.group(1)
            content = meta_match.group(2)

            for line in meta_text.split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    metadata[key.strip()] = val.strip()

        parsed.append((content.strip(), metadata))

    return parsed


# -------------------------------
# Auto tag if metadata missing
# -------------------------------

def auto_tag(content, metadata):

    text = content.lower()

    if "security" in text or "input" in text:
        metadata.setdefault("category", "security")

    elif "loop" in text or "complexity" in text:
        metadata.setdefault("category", "performance")

    else:
        metadata.setdefault("category", "general")

    return metadata


# -------------------------------
# Main ingestion
# -------------------------------

def ingest():

    docs = []
    metas = []
    ids = []

    for filename in os.listdir(DATA_DIR):

        path = os.path.join(DATA_DIR, filename)

        with open(path, "r") as f:
            text = f.read()

        blocks = parse_semantic_blocks(text)

        for content, metadata in blocks:

            metadata = auto_tag(content, metadata)

            docs.append(content)
            metas.append(metadata)
            ids.append(str(uuid.uuid4()))

    add_documents(docs, metas, ids)

    print(f"Ingested {len(docs)} semantic blocks.")


if __name__ == "__main__":
    ingest()
