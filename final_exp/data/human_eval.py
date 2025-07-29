import json

# dataset has the problem and then has the tests that need to be passed. Need to set up some way to run the generated code against the tests safely.

from datasets import load_dataset

ds = load_dataset("openai_humaneval")

data = []

for question in ds["test"]:
    data.append(
        {
            "question": question["prompt"],
            "entry_point": question["entry_point"],
            "answer": question["test"],
        }
    )


# with open("human_eval.json", "w") as file:
#     json.dump(data, file)
