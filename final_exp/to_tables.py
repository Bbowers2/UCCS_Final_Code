import json
import numpy as np

attacks = [None, "single", "continued", "continued with comments"]
models = ["CT", "CRT", "CRTs"]

final_results = {}

for model in models:
    for attack in attacks:

        accuracy = []
        attack_success = []
        cont_success = []
        llm_calls = []
        mean_reviews = []
        mean_tests = []

        for i in range(5):
            with open(f"{model}-{attack}-result{i}.txt", "r") as f:
                result = json.load(f)
                accuracy.append(result["Accuracy"])
                attack_success.append(result["Attack_Success_rate"])
                cont_success.append(result["COnt_Success_rate"])
                llm_calls.append(result["LLM_calls"])
                mean_reviews.append(result["Mean_Review_rounds"])
                mean_tests.append(result["Mean_Test_rounds"])

        success = attack_success
        if attack not in [None, "single"]:
            success = cont_success

        final_results[model][str[attack]] = [
            np.mean(accuracy),
            np.mean(attack_success),
            np.mean(cont_success),
            np.mean(llm_calls),
            np.mean(mean_reviews),
            np.mean(mean_tests),
            np.mean(success),
        ]

with open("final_results.txt", "w") as f:
    json.dump(final_results, f)
