# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .file_url_param import FileURLParam
from .file_data_param import FileDataParam
from .classify_type_param import ClassifyTypeParam

__all__ = ["ClassifyRunParams", "File"]


class ClassifyRunParams(TypedDict, total=False):
    file: Required[File]
    """File to classify, either as raw data or a URL"""

    types: Required[Iterable[ClassifyTypeParam]]
    """List of classification types to classify the document into"""


File: TypeAlias = Union[FileDataParam, FileURLParam]
