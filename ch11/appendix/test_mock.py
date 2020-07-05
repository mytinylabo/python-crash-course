import os
import pytest
from unittest import mock


def test_method():
    m = mock.Mock()
    m.get_answer.return_value = 42
    assert m.get_answer() == 42
    assert m.get_answer("with", "arguments") == 42


def test_side_effect():
    m = mock.Mock()

    def print_hello():
        print("hello, world!")
        return 43
    m.foo.side_effect = print_hello
    assert m.foo() == 43
    assert m.foo.call_count == 1


def test_assertion():
    m = mock.Mock()
    m.some_method('foo', 'bar')  # Just calling an undefined method creates a corresponding mocked method
    m.some_method.assert_called_once_with('foo', 'bar')
    m.some_method.assert_called_once_with('foo', mock.ANY)
    m.some_method.assert_called_with('foo', 'baz')  # Gonna fail


def fake_os_unlink(path):
    raise IOError("Testing!")


def test_mocking_libs():
    with mock.patch('os.unlink', fake_os_unlink):
        with pytest.raises(IOError):
            os.unlink('foobar')
