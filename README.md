# UCCS_Final_Code

## Steps for running on the GPUs

### Setup
1. ssh into the gpu - you will need two windows and ollama needs to be installed on the gpu
2. In one window ```ollama list```
    You should see the LLM model that you are trying to use on the GPU
3. If you don't see the model, then ```ollama pull {model name}```

### Running experiments
1. In one terminal window run ```ollama serve``` then leave it running
2. In the other window cd to the final_exp folder
3. To run the C, CT, and CRT then change the LLM model to correct model found in file autogen_model.py, then change the rounds, architecture, etc in evaluate_autogen.py. Then simply run python[3] evaluate_autogen.py
4. To run the security analysis experiment, change to the correct model found in the file ctr.py then change the specific attack list in evaluate_ctr.py. Then simply run python[3] evaluate_ctr.py

### Running with open ai model
1. You need to use an api key, along with the commented out import openaicompletionclient import and model lines found in the file. Remove the config and the OllamCompletionClient lines. The key should be saved in a file called .env

### Making the tables and storing data
The results from the different attacks should be in inject_results/{llm_model}/. Once each of the llm_models has the results run consolidate.py in each of the folders. Then .. to inject_results, where you should see a file named final_inj_results.txt. Copy this file into models_final_results then navigate to that folder. From there, run make_attack_table.py.

For the CT, CTR, C architectures tables, copy the results after running evaluate_autogen.py to {model}_ag_results/. Then run the file get_final_results.py and move the file name {llm model}.txt to model_final_results. Once all the model.txt's are there, run make_tables.py.


### Requirements

pip install tqdm
pip install autogen-ext
pip install numpy
 
install ollama from their website