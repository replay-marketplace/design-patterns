"""Pytest configuration and fixtures."""

import pytest
import requests_mock as rm


@pytest.fixture
def requests_mock():
    """Fixture to mock HTTP requests."""
    with rm.Mocker() as m:
        yield m
