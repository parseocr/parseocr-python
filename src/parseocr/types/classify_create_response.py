# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ClassifyCreateResponse", "Result"]


class Result(BaseModel):
    confidence: float

    type: str


class ClassifyCreateResponse(BaseModel):
    credit_used: int

    result: Result
