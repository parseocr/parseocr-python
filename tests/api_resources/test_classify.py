# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parseocr import Parseocr, AsyncParseocr
from tests.utils import assert_matches_type
from parseocr.types import ClassifyRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: Parseocr) -> None:
        classify = client.classify.run(
            file={"file_data": "file_data"},
            types=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(ClassifyRunResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Parseocr) -> None:
        response = client.classify.with_raw_response.run(
            file={"file_data": "file_data"},
            types=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyRunResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Parseocr) -> None:
        with client.classify.with_streaming_response.run(
            file={"file_data": "file_data"},
            types=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyRunResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassify:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncParseocr) -> None:
        classify = await async_client.classify.run(
            file={"file_data": "file_data"},
            types=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(ClassifyRunResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncParseocr) -> None:
        response = await async_client.classify.with_raw_response.run(
            file={"file_data": "file_data"},
            types=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyRunResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncParseocr) -> None:
        async with async_client.classify.with_streaming_response.run(
            file={"file_data": "file_data"},
            types=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyRunResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True
