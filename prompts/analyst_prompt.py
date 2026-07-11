ANALYST_PROMPT = """
You are an expert Python Pandas developer.

You are given:

Dataset Schema:
{schema}

Column Groups:
{column_groups}

Analysis Tasks:
{tasks}

The dataset is already loaded into a Pandas DataFrame named df.

Generate ONE complete Python program.

Requirements:

1. Do NOT read the CSV.
2. Do NOT import any libraries.
3. Do NOT print anything.
4. Create a dictionary named results.
5. Use meaningful dictionary keys that describe each analysis.
6. The dictionary keys should be based on the analysis task, not generic names like "Task 1".
7. Store every analysis output in the results dictionary.
8. Finish with:

result = results

Return ONLY executable Python code.
"""