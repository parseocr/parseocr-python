# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ClassifyRunResponse", "Result"]


class Result(BaseModel):
    confidence: float

    type: str


class ClassifyRunResponse(BaseModel):
    credit_used: int

    result: Result
