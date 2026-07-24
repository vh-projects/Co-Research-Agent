# app/utils/llm

from typing import Type, TypeVar
from pydantic import BaseModel
from app.llm.client import llm
from app.utils.json_parser import extract_json

T = TypeVar("T", bound=BaseModel)


def generate_structured_output(
    prompt: str, model: Type[T],
) -> T:
    """
    Generate a structured Pydantic object from an LLM prompt.

    Steps:
    1. Invoke the LLM
    2. Extract JSON
    3. Validate with Pydantic
    """

    response = llm.invoke(prompt)
    data = extract_json(response)

    return model.model_validate(data)
    
    