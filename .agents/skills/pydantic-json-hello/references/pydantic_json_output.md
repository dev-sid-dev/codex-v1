# Pydantic JSON Output Reference

This project uses Pydantic v2 to create structured JSON responses.

## Basic pattern

Use `BaseModel` to define the schema:

```python
from pydantic import BaseModel


class Calculation(BaseModel):
    expression: str
    result: int


class HelloResponse(BaseModel):
    message: str
    calculation: Calculation
    status: str