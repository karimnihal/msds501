import pytest
from string_operations import reverse_string

def test_hw():
    assert reverse_string("Hello World") == "dlroW olleH"

def test_empty():
    assert reverse_string("") == ""

def test_pal():
    assert reverse_string("racecar") == "racecar" 