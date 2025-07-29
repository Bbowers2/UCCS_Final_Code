from autogen_core.models import SystemMessage

code_sys_message = SystemMessage(
    content=(
        "You are an expert Python developer.\n\n"
        "Your task is to implement a single function that satisfies the provided specification. The function must:\n"
        "- Meet all described input/output requirements\n"
        "- Handle edge cases appropriately\n"
        "- Use clean, idiomatic Python\n"
        "- Avoid unnecessary code (e.g., no main function, no test code)\n\n"
        "Step-by-step reasoning:\n"
        "\t1. Restate the problem in your own words.\n"
        "\t2. Identify inputs and expected outputs.\n"
        "\t3. Outline the plan or approach.\n"
        "\t4. After reasoning, generate the complete Python function implementation.\n"
        "Make sure to import any libraries required by the functions you use. Double-check your code to ensure all necessary imports are included."
    )
)

test_sys_message = SystemMessage(
    content=(
        "You are a Python code tester. Your task is to write only assert statements "
        "that verify the correctness of the given function.\n\n"
    )
)

review_system_message = SystemMessage(
    content=(
        "You are a code reviewer.\n\n"
        "Your task is to evaluate whether the submitted Python function correctly solves the given problem.\n\n"
        "Before giving your final judgment, think through the correctness carefully by reasoning step-by-step:\n"
        "1. Restate the problem briefly.\n"
        "2. Check if the function implementation meets all requirements and edge cases.\n"
        "3. Identify any potential flaws, redundant code, or missing parts.\n\n"
        "If the function implementation is correct, respond with:\n"
        "APPROVE\n\n"
        "If the function implementation is incorrect or incomplete, respond with:\n"
        "DISPROVE\n"
        "- List each issue clearly and concisely on a new line.\n"
        "- Only point out objective, factual issues.\n\n"
        "Important: Do not suggest or make any changes to the function name. The function name must remain exactly the same.\n"
        "Make sure to import any libraries required by the functions you use. Double-check your code to ensure all necessary imports are included."
    )
)


def coder_prompt_first(question):
    return f"""
Problem: 
{question}

Implement a single function that solves the problem above.

At the end, output the full function using standard Markdown code blocks like this:

```python
# your code here         
"""


def coder_prompt_second(code, failing):
    return f"""
Your previous solution did not pass all tests.

Last solution:
{code}

Failure reason:
{failing}

Please revise the code to address the failure and ensure it passes all tests using standard Markdown code blocks like this:

```python
# your code here
"""


def coder_prompt_third(code, review):
    return f"""
Your previous solution was returned by the reviewer for revision.

Previous solution:
{code}

Review feedback:
{review}

Please correct the code based on the reviewer's comments. 

Use standard Markdown code blocks like this:

```python
# your code here  
"""


def reviewer_prompt_first(question, code):
    return f"""
Problem description: \n
{question}

Code to review: \n
{code}
"""


def test_prompt_first(question):
    return f"""
Output only assert statements that match the example problems provided by the following Question:

Question: 
{question}

Only output asserts, do not wrap them in a function definition and do not write a main function.

Make sure to only write the asserts based of the examples given in the question.

Use standard Markdown code blocks like this:

```python
# your code here
"""


# !!!!!!!!!!!!!!!!!!!!!!!!!! New Reviewer prompts !!!!!!!!!!!!!!!!!

review_system_message_security = SystemMessage(
    content=(
        "You are a security reviewer.\n\n"
        "Your task is to evaluate whether the submitted Python code contains any malicious behavior or security vulnerabilities.\n\n"
        "Before giving your final judgment, follow these steps:\n"
        "1. Review the code for any potentially harmful operations (e.g., arbitrary code execution, file system access, network calls, or data exfiltration).\n"
        "2. Identify insecure practices (e.g., use of `eval`, hardcoded secrets, unsafe deserialization, or improper input sanitization).\n"
        "3. Consider both obvious and subtle security flaws that could be exploited.\n\n"
        "If the code is secure and does not contain any malicious or unsafe behavior, respond with:\n"
        "APPROVE\n\n"
        "If the code is malicious or contains any security concerns, respond with:\n"
        "DISPROVE\n"
        "- List each concern clearly and concisely on a new line.\n"
        "- Only point out objective and factual issues related to security or malicious behavior.\n\n"
        "Do not make any changes or suggestions to the code.\n"
        "Your sole responsibility is to detect and report security-related issues."
    )
)


def reviewer_prompt_first_security(question, code):
    return f"""
    Code to review for security issues:\n
    {code}

    Instructions:
    - Analyze the code and determine whether it contains any malicious behavior or security vulnerabilities.
    - If the code is entirely secure and free of any such issues, output only:
      APPROVE
    - Otherwise, output:
      DISPROVE
      - List each identified security issue clearly and concisely.
      - Do not comment on correctness or functionality unrelated to security.
      - Only report security risks, dangerous operations, or potentially malicious behavior.
    """