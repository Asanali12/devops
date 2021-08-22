"""
Setting an environment for testing
"""
import pytest

from app import app as my_app


@pytest.fixture
def app():
    """
    Setting up an app
    """
    yield my_app


@pytest.fixture
def client(app):
    """
    Setting up a client
    """
    return app.test_client()
    