from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from analysis.code_parser import analyze_code_structure
from analysis.risk_detector import detect_risks
from retrieval.retriever import dynamic_retrieval
from analysis.context_compressor import compress_context
from llm.reviewer import review_code

router = APIRouter()


# ✅ Request schema
class ReviewRequest(BaseModel):
    code: str


@router.post("/review")
def review(request: ReviewRequest):

    try:
        code = request.code

        if not code.strip():
            raise HTTPException(status_code=400, detail="Code cannot be empty")

        # 1️⃣ Analyze structure
        structure = analyze_code_structure(code)

        # 2️⃣ Detect risk categories
        risks = detect_risks(structure)

        # 3️⃣ Dynamic Retrieval (Smart RAG)
        docs = []

        if risks:
            for r in risks:
                retrieved = dynamic_retrieval(code, category=r)
                docs.extend(retrieved)
        else:
            # fallback retrieval
            docs = dynamic_retrieval(code)

        # remove duplicates
        docs = list(set(docs))

        # 4️⃣ Compress context
        compressed = compress_context(docs)

        # 5️⃣ LLM review
        result = review_code(code, structure, compressed)

        return {"review": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
