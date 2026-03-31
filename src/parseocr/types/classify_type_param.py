# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ClassifyTypeParam"]


class ClassifyTypeParam(TypedDict, total=False):
    description: Required[str]
    """Description of the classified type"""

    name: Required[str]
    """Name of the classified type"""
