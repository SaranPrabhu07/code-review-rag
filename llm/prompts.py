REVIEW_PROMPT = """
You are a senior software engineer performing code review.

Code:
{code}

Analysis:
{analysis}

Relevant Rules:
{rules}

Return:

- Issue
- Explanation
- Severity
- Suggested Fix
"""
