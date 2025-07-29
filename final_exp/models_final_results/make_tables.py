import json

with open("open.txt", "r") as f:
    open_results = json.load(f)

with open("codellama.txt", "r") as f:
    codellama_results = json.load(f)

with open("mistral.txt", "r") as f:
    mistral_results = json.load(f)


# Different LLMs comparison of accuracy, effectiveness, and calls
def get_body():
    models = ["C", "CT", "CRT"]
    llms = [codellama_results, mistral_results, open_results]
    attacks = ["None", "first", "last"]

    tabs = []

    for model in models:
        rows = [["& No Attack"], ["& Single"], ["& Continued"]]
        for i, attack in enumerate(attacks):
            for llm in llms:
                name = f"{model}_{attack}"
                rows[i].append(
                    f"{llm[name]["Accuracy_mean"]:.2f}\\(\\pm{llm[name]["Accuracy_me"]:.2f}\\)"
                )
                rows[i].append(
                    f"{llm[name]["Effectiveness_mean"]:.2f}\\(\\pm{llm[name]["Effectiveness_me"]:.2f}\\)"
                )
                rows[i].append(
                    f"{llm[name]["LLM_calls_mean"]:.2f}\\(\\pm{llm[name]["LLM_calls_me"]:.2f}\\)"
                )
        tabs.append(rows)

    sections = []

    for t in tabs:
        sections.append("\n".join([" & ".join(row) + " \\\\" for row in t]))

    return sections


s = get_body()

table = (
    """
\\begin{table*}[h!]
  \\centering
  \\resizebox{\\textwidth}{!}{

  \\begin{tabular}{ll 
    c c c  % codellama
    c c c  % mistral
    c c c  % gpt4.1-mini
  }
    \\toprule
    \\textbf{Architecture} & \\textbf{Attack} & 
    \\multicolumn{3}{c}{\\textbf{codellama}} & 
    \\multicolumn{3}{c}{\\textbf{mistral}} & 
    \\multicolumn{3}{c}{\\textbf{gpt4.1-mini}} \\\\
    \\cmidrule(lr){3-5} \\cmidrule(lr){6-8} \\cmidrule(lr){9-11}
    & & \\textbf{Acc} & \\textbf{Eff} & \\textbf{Calls} 
      & \\textbf{Acc} & \\textbf{Eff} & \\textbf{Calls} 
      & \\textbf{Acc} & \\textbf{Eff} & \\textbf{Calls} \\\\
    \\midrule
    \\multirow{3}{*}{C}"""
    + str(s[0])
    + """
    \\multirow{3}{*}{CT}"""
    + str(s[1])
    + """
    \\multirow{3}{*}{CRT}"""
    + str(s[2])
    + """
    \\bottomrule
  \\end{tabular}
  }
  \\caption{Performance metrics across models, architectures, and attack types}
  \\label{tab:model_comparison}
\\end{table*}
"""
)


print(table)


# # make the different attack table

# """
# Arch.      | Attack 1 | Attack 2 | Attack 3 |
# --------------------------------------------------
# CodeLlama  |          |          |          |
# Mistral    |          |          |          |
# GPT4.1-mini|          |          |          |
# """


# def get_body2():
#     return "TODO"


# body = get_body2()

# table2 = """
# \\begin{table}[h!]
#   \\centering
#   \\begin{tabular}{lccc}
#     \\toprule
#     \\textbf{Architecture} & \\textbf{Attack 1} & \\textbf{Attack 2} & \\textbf{Attack 3} \\\\
#     \\midrule
# """
# +body
# +"""
#     \\bottomrule
#   \\end{tabular}
#   \\caption{Results by architecture and attack type}
#   \\label{tab:attack_summary}
# \\end{table}"""
