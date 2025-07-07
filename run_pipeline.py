import subprocess
import os

# Define file paths
SOURCE_FILE = "models/DepartmentController.cc"
TEST_FILE = "testgen/tests/test_DepartmentController.cpp"
PROMPT_FILE = "testgen/prompts/1_generate.yaml"
BUILD_LOG = "testgen/build_logs/build.log"

# Helper to read a file
def read_file(path):
    with open(path, "r") as f:
        return f.read()

# Helper to write a file
def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# Function to call LLaMA via Ollama
def call_llama(prompt, code):
    full_prompt = f"""You are a C++ unit test generator.

Prompt (YAML):
{prompt}

C++ File:
Please generate a GoogleTest-compatible unit test file named test_DepartmentController.cpp.
Only output valid C++ code, no markdown or explanations.
"""
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=full_prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8")

# Function to build tests via CMake
def build_tests():
    os.makedirs("build", exist_ok=True)
    with open(BUILD_LOG, "w") as log:
        subprocess.run(["cmake", ".."], cwd="build", stdout=log, stderr=subprocess.STDOUT)
        proc = subprocess.run(["cmake", "--build", "."], cwd="build", stdout=log, stderr=subprocess.STDOUT)
    return proc.returncode == 0

# Main pipeline logic
if __name__ == "__main__":
    print("🔹 Loading YAML prompt...")
    prompt = read_file(PROMPT_FILE)

    print("🔹 Loading C++ source file...")
    code = read_file(SOURCE_FILE)

    print("🔹 Generating unit test with LLaMA...")
    test_code = call_llama(prompt, code)

    print("🔹 Saving generated test...")
    write_file(TEST_FILE, test_code)

    print("🔹 Building tests...")
    success = build_tests()

    if success:
        print("✅ Build passed! You can now run tests via `ctest`.")
    else:
        print("❌ Build failed. Check logs in:", BUILD_LOG)
