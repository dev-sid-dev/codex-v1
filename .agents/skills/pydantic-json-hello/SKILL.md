---
name: pydantic-json-hello
description: Use this skill when the user asks to modify a Python Hello World program to return a structured JSON response validated with Pydantic, especially when the output must follow a fixed schema.
---

# Pydantic JSON Hello Skill

Use this skill when the task involves:
- Python
- Pydantic
- JSON output
- replacing a simple `print("Hello, World!")` example with structured data
- validating or serializing output using a defined schema

## Goal

Transform simple Python examples into small, production-style scripts that:

1. Define a Pydantic model.
2. Build a response object.
3. Validate the data through the model.
4. Print a JSON string using the model serializer.
5. Keep the program executable through `main() -> int`.

## Required output schema

The final Python program should produce JSON with this structure:

```json
{
  "message": "Hello, World!",
  "calculation": {
    "expression": "2 + 2",
    "result": 4
  },
  "status": "success"
}