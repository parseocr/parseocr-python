# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileDataParam"]


class FileDataParam(TypedDict, total=False):
    file_data: Required[str]
    """Raw file data encoded as a base64 string"""
