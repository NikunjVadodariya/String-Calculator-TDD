import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from string_calculator import add, NegativeNumberError


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number():
    assert add("1") == 1


def test_two_numbers():
    assert add("1,5") == 6


def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15


def test_newline_as_delimiter():
    assert add("1\n2,3") == 6


def test_custom_delimiter():
    assert add("//;\n1;2") == 3


def test_negative_number_raises():
    with pytest.raises(NegativeNumberError) as excinfo:
        add("1,-2,3")
    assert "negative numbers not allowed -2" in str(excinfo.value)


def test_multiple_negatives_in_exception():
    with pytest.raises(NegativeNumberError) as excinfo:
        add("-1,-2,3")
    assert "negative numbers not allowed -1,-2" in str(excinfo.value)
