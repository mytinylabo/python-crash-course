import pytest


def add(a, b):
    return a + b


# Parametrized test
@pytest.mark.parametrize("a, b", [
    (2, 3), (0, 0), (19, 0), (-13, 3), (-5, -5)
])
def test_add(a, b):
    assert add(a, b) == a + b


def sub(a, b):
    return a - b


# Parametrized fixture
@pytest.fixture(params=[(2, 3), (0, 0), (19, 0), (-13, 3), (-5, -5)])
def pair(request):
    return request.param


def test_sub(pair):
    a, b = pair
    assert sub(a, b) == a - b
