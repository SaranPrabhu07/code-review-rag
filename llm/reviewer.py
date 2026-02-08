from openai import OpenAI
from core.config import OPENAI_API_KEY
from .prompts import REVIEW_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def review_code(code, analysis, rules):

    prompt = REVIEW_PROMPT.format(
        code=code,
        analysis=analysis,
        rules=rules
    )

    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
