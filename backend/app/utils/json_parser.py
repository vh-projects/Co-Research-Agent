import json
import re
from typing import Any


class JSONParseError(Exception):
    """Raised when a valid JSON object cannot be extracted."""


def extract_json(response: str) -> dict[str, Any] | list[Any]:
    """
    Extract and parse JSON from an LLM response.

    Handles:
    - Raw JSON
    - ```json fenced blocks
    - Extra text surrounding JSON
    """

    response = response.strip()

    # Case 1: Markdown fenced JSON
    fenced = re.search(
        r"```(?:json)?\s*(.*?)\s*```",
        response,
        flags=re.DOTALL | re.IGNORECASE,
    )

    if fenced:
        response = fenced.group(1).strip()

    # Case 2: Try parsing directly
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    # Case 3: Extract first JSON object
    start = response.find("{")
    end = response.rfind("}")

    if start != -1 and end != -1 and end > start:
        candidate = response[start : end + 1]

        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass

    # Case 4: Extract first JSON array
    start = response.find("[")
    end = response.rfind("]")

    if start != -1 and end != -1 and end > start:
        candidate = response[start : end + 1]

        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass

    raise JSONParseError(
        "Could not extract valid JSON from the LLM response."
    )

