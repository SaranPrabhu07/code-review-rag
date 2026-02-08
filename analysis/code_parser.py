import ast

def analyze_code_structure(code: str):
    tree = ast.parse(code)

    loops = 0
    functions = 0

    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While)):
            loops += 1
        if isinstance(node, ast.FunctionDef):
            functions += 1

    return {
        "loops": loops,
        "functions": functions
    }
