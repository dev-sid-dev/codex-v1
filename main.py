from pydantic import BaseModel


class Calculation(BaseModel):
    expression: str
    result: int


class HelloResponse(BaseModel):
    message: str
    calculation: Calculation
    status: str


def main() -> int:
    response = HelloResponse(
        message="Hello, World!",
        calculation=Calculation(expression="2 + 2", result=2 + 2),
        status="success",
    )
    print(response.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
