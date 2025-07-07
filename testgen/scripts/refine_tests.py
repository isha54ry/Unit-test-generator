import os
from generate_tests import read_file, write_file, call_llm

PROMPT_DIR = "../prompts"
TEST_DIR = "../tests"

system_prompt = read_file(os.path.join(PROMPT_DIR, "refine_tests.yaml"))

for file in os.listdir(TEST_DIR):
    if file.endswith(".cpp"):
        content = read_file(os.path.join(TEST_DIR, file))
        improved = call_llm(system_prompt, content)
        write_file(os.path.join(TEST_DIR, file), improved)
        print(f"Refined: {file}")