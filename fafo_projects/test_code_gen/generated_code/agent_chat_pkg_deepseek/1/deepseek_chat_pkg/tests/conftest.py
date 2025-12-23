"""Pytest configuration and fixtures."""

import pytest
import requests_mock as rm


@pytest.fixture
def requests_mock():
    """Provide requests_mock fixture."""
    with rm.Mocker() as m:
        yield m
