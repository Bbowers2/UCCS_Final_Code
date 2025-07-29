import json
import numpy as np
from scipy.stats import t
import os


def calculate_me(array):
    n = len(array)
    mean = np.mean(array)
    std_err = np.std(array, ddof=1) / np.sqrt(n)
    t_score = t.ppf(0.975, df=n - 1)  # t-dist for 95% confidence
    margin_of_error = t_score * std_err
    return float(mean), float(margin_of_error)


final_results = {}
key = ["CodeLlama", "Mistral", "GPT4.1-mini"][1]
fp = "../final_inj_results.txt"

for i in range(7):
    temp = []
    for y in range(3):
        with open(f"ctr_results-{i}-run{y}.json", "r") as f:
            data = json.load(f)
        temp.append(data["Effectiveness"])

    mean, me = calculate_me(temp)
    final_results[i] = {"Mean": mean, "ME": me}

if not os.path.exists(fp):
    with open(fp, "w") as f:
        json.dump({}, f)

with open(fp, "r") as f:
    try:
        fr = json.load(f)
    except json.JSONDecodeError:
        fr = {}

fr[key] = final_results
with open(fp, "w") as f:
    json.dump(fr, f, indent=4)
