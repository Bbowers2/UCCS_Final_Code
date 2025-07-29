import asyncio
import os
from pydantic import BaseModel
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

BASE_URL = "http://localhost:11434/v1"
API_KEY = "llama"
MODEL_NAME = "llama3.2"

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set EXAMPLE_BASE_URL, EXAMPLE_API_KEY, EXAMPLE_MODEL_NAME via env var or code."
    )


class CodeOutput(BaseModel):
    thinking: str
    code: str


class CodeReview(BaseModel):
    thinking: str
    assert_statements: str


client = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)
set_default_openai_client(client=client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)

# Agents

test_agent = Agent(
    name="2ndAssistant",
    instructions="Given the provided code write several assert statements. Pay special attention to base cases and other possible errors. Write only executable assert statements in the field 'assert_statements'.",
    model=MODEL_NAME,
    output_type=CodeReview,
)
coding_agent = Agent(
    name="coding_agent",
    instructions=(
        "You are an expert coder. Generate only executable Python code. Do not use or call any tools. Output a completed, runnable function in the field 'code'."
    ),
    model=MODEL_NAME,
    output_type=CodeOutput,
)


async def main():
    print("Starting...")
    question = """from typing import List, Tuple
    
    def sum_product(numbers: List[int]) -> Tuple[int, int]:
        \"\"\"
        For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
        Empty sum should be equal to 0 and empty product should be equal to 1.
            >>> sum_product([])\n
                (0, 1)
            >>> sum_product([1, 2, 3, 4])
                (10, 24)
        \"\"\"
    """
    result = await Runner.run(coding_agent, question)

    code = result.final_output.code
    print(code)

    test_result = await Runner.run(test_agent, f"{question} \n {code}")
    print(test_result.final_output.assert_statements)


asyncio.run(main())