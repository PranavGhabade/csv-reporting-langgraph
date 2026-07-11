import re


def clean_python_code(code: str) -> str:
    """
    Removes markdown code fences from LLM generated code.
    """

    code = code.strip()

    code = re.sub(r"^```python\s*", "", code)
    code = re.sub(r"^```\s*", "", code)
    code = re.sub(r"\s*```$", "", code)

    return code.strip()


def execute_code(code: str, df):
    """
    Executes generated Pandas code and returns the variable 'result'.
    """

    code = clean_python_code(code)

    local_scope = {
        "df": df
    }

    try:

        exec(code, {}, local_scope)

        return local_scope.get("result")

    except Exception as e:

        print("\n===== EXECUTION ERROR =====")
        print(e)

        raise