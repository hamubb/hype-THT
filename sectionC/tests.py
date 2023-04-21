import unittest

import pytest

from check_isbn import validate_isbn_number


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("9781603095020", "Valid"),
        ("978-1-60309-503-7", "Valid"),
        ("9784603095020", "Invalid"),
    ],
)
def test_validate_isbn_13_number(test_input, expected):
    assert validate_isbn_number(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [("0316066524", "9780316066525"), ("0-19-852663-6", "9780198526636")],
)
def test_validate_isbn10_number_without_x(test_input, expected):
    assert validate_isbn_number(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [("0316066524", "9780316066525")],
)
def test_validate_isbn10_number_with_x(test_input, expected):
    assert validate_isbn_number(test_input) == expected
