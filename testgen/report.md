## Summary
This tool uses an LLM (LLaMA or GPT) to generate and refine unit tests for C++ applications.

### Features
- Generates initial tests for all `.cc` files
- Refines tests to remove duplicates and follow best practices
- Uses GoogleTest
- Calculates code coverage with lcov

### Coverage Report
See `testgen/coverage/index.html` for full visual report.

### Structure
- `prompts/`: YAML prompt instructions
- `tests/`: Generated and refined test files
- `coverage/`: Coverage HTML
- `scripts/`: Python scripts for automation

---

Make sure you have environment variables and `g++`, `cmake`, `lcov`, and `genhtml` installed.
