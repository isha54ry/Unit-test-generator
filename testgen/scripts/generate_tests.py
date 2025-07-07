import os
import subprocess
import json
import llama_cpp  

SRC_DIR = "../../models"
TEST_DIR = "../tests"
PROMPT_DIR = "../prompts"

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def call_llm(system_prompt, user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "llama-3"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ]
    )
    return response["choices"][0]["message"]["content"]

def generate_test_for_file(source_path):
    file_name = os.path.basename(source_path)
    class_name = file_name.replace(".cc", "")
    header = class_name + ".h"

    system_prompt = read_file(os.path.join(PROMPT_DIR, "generate_tests.yaml"))
    user_input = f"Source file: {file_name}\nContent:\n" + read_file(source_path)

    test_code = call_llm(system_prompt, user_input)

    test_file = os.path.join(TEST_DIR, f"test_{class_name}.cpp")
    write_file(test_file, test_code)
    print(f"Generated: {test_file}")
# Batch generate for all .cc files
for file in os.listdir(SRC_DIR):
    if file.endswith(".cc"):
        generate_test_for_file(os.path.join(SRC_DIR, file))