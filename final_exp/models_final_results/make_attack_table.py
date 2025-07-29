import json

"""
Arch.      | Attack 1 | Attack 2 | Attack 3 |
--------------------------------------------------
CodeLlama  |          |          |          |
Mistral    |          |          |          |
GPT4.1-mini|          |          |          |
"""

models = ["CodeLlama", "Mistral", "GPT4.1-mini"]


def get_body2():
    with open("final_inj_results.txt", "r") as f:
        b = ""
        data = json.load(f)
        for model in models:
            b += model + " & "
            line = (
                " & ".join(
                    [
                        f"{data[model][str(i)]["Mean"]:.2f}\\(\\pm{data[model][str(i)]["ME"]:.2f}\\)"
                        for i in range(7)
                    ]
                )
                + "  \\\\\n"
            )
            b += line
        return b


table2 = (
    """
\\begin{table}[h!]
  \\centering
  \\begin{tabular}{lcccccc}
    \\toprule
    \\textbf{LLM} & Baseline &  \\textbf{Attack 1} & \\textbf{Attack 2} & \\textbf{Attack 3} & \\textbf{Attack 4} & \\textbf{Attack 5} & \\textbf{Attack 6} \\\\
    \\midrule
"""
    + get_body2()
    + """
    \\bottomrule
  \\end{tabular}
  \\caption{\\textit{coder-tester with review agent} tested on a baseline and with 5 different attacks, found in \\ref{list:attacks}. We evaluate using three different LLM models. The effectiveness of each attack is measured, as a percentage.}
  \\label{tab:attack_summary}
\\end{table}"""
)

print(table2)
