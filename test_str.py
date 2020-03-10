import pytest

def str_creation():
    """Create string"""
    return 'Hello world'

def test_str_reverse():
    """Reverse string"""
    s = str_creation()
    assert s[::-1] == 'dlrow olleH'

def test_str_add():
    """Add word in string"""
    s = str_creation()
    s += ', hello!'
    assert s == 'Hello world, hello!'

def test_str_len():
    """Lenght of string"""
    s = str_creation()
    assert len(s) == 11

class TestStr:

    def test_str_digit(self):
        """Numbers check in string"""
        s = str_creation()
        assert bool(s.isdigit()) == 0

@pytest.mark.parametrize('i', ('H', 'e', 'l', 'o', 'w', 'r', 'd'))
def test_str_top(i):
    s = str_creation()
    assert (i in s) == 1