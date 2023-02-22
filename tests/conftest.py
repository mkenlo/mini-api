import pytest

from api import create_app
import config


@pytest.fixture
def app():
    app = create_app(config.TestConfig)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
