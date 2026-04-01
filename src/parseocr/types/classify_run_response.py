# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ClassifyRunResponse", "Result"]


class Result(BaseModel):
    """Classification result for the provided document"""

    confidence: float
    """Confidence score between 0 and 1"""

    type: str
    """Type of the classified result"""


class ClassifyRunResponse(BaseModel):
    credit_used: float
    """Cost in EUR (€) for this classification (per page for PDFs, flat for images)"""

    result: Result
    """Classification result for the provided document"""
