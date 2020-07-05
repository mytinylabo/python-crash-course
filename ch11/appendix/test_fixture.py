import os

import pytest


@pytest.fixture(scope="module")
def database():
    ...  # Set up a fixture
    yield {}
    ...  # Tear down the fixture


@pytest.fixture(autouse=True)
def change_user_env():
    curuser = os.environ.get("USER")
    os.environ["USER"] = "foobar"
    yield
    os.environ["USER"] = curuser


def test_insert(database):
    database['foo'] = 'bar'
    assert 'foo' in database


def test_user():
    assert os.getenv("USER") == "foobar"
