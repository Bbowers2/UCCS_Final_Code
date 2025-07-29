import json
import numpy as np
from scipy.stats import t

models = ["C", "CT", "CRT"]
attacks = ["None", "first", "last"]

results = {}


def calculate_me(array):
    n = len(array)
    mean = np.mean(array)
    std_err = np.std(array, ddof=1) / np.sqrt(n)
    t_score = t.ppf(0.975, df=n - 1)  # t-dist for 95% confidence
    margin_of_error = t_score * std_err
    return float(mean), float(margin_of_error)


for m in models:
    for a in attacks:

        final_results = {}
        acc = []
        llm_calls = []
        effectiveness = []
        reviews = []
        tests = []

        for i in range(3):
            with open(f"{m}-{a}-result{i}.txt", "r") as f:
                data = json.load(f)
                acc.append(data["Accuracy"])
                (
                    effectiveness.append(data["Cont_Success_rate"])
                    if a == "last"
                    else effectiveness.append(data["Attack_Success_rate"])
                )
                llm_calls.append(data["LLM_calls"])
                reviews.append(data["Mean_Review_rounds"])
                tests.append(data["Mean_Test_rounds"])

        final_results["Accuracy_mean"], final_results["Accuracy_me"] = calculate_me(acc)
        final_results["Effectiveness_mean"], final_results["Effectiveness_me"] = (
            calculate_me(effectiveness)
        )
        final_results["LLM_calls_mean"], final_results["LLM_calls_me"] = calculate_me(
            llm_calls
        )
        final_results["Review_mean"], final_results["Review_me"] = calculate_me(reviews)
        final_results["Test_mean"], final_results["Test_me"] = calculate_me(tests)

        results[f"{m}_{a}"] = final_results

with open(f"open_results.txt", "w") as f:
    json.dump(results, f)
print(results)
