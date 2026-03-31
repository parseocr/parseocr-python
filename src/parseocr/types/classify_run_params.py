# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .file_data_param import FileDataParam
from .classify_type_param import ClassifyTypeParam

__all__ = ["ClassifyRunParams", "File", "FileFileURL"]


class ClassifyRunParams(TypedDict, total=False):
    file: Required[File]

    types: Required[Iterable[ClassifyTypeParam]]


class FileFileURL(TypedDict, total=False):
    file_url: Required[str]


File: TypeAlias = Union[FileDataParam, FileFileURL]
