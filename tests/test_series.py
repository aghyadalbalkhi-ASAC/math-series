from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import other_values
from math_series.series import sum_series



def test_version():
    assert __version__ == '0.1.0'



"""
Test case:
 fibonacci   5 => 5
 lucas   5 => 11
 other_values   5 => 30
 without optional parameters 5 => 5
"""


def test_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_other_values():
    actual = other_values(5,5,3)
    expected = 30
    assert actual == expected

def test_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected
