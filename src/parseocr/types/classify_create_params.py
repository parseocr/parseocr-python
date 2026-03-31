# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ClassifyCreateParams", "File", "FileFileData", "FileFileURL", "Type"]


class ClassifyCreateParams(TypedDict, total=False):
    file: Required[File]

    types: Required[Iterable[Type]]


class FileFileData(TypedDict, total=False):
    file_data: Required[str]


class FileFileURL(TypedDict, total=False):
    file_url: Required[str]


File: TypeAlias = Union[FileFileData, FileFileURL]


class Type(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
