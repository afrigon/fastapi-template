"""
Application fixtures to easily create app instances

Examples:
    $ python -m pytest
    $ coverage run -m pytest
    $ coverage report
    $ coverage html
"""

import pytest
from starlette.testclient import TestClient
from app import ApplicationFactory


@pytest.fixture
def app():
    """debug application fixture"""

    return ApplicationFactory('API', 'Test application').create(debug=True)


@pytest.fixture
def client(app):
    """application client fixture"""

    return TestClient(app)
