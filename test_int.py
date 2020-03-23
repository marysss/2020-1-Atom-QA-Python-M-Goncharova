import pytest

class TestDefaultInt:
    """Тесты с ожидаемыми ошибками"""

    def test_int_zero(self):
        """Error: division by zero"""
        with pytest.raises(ZeroDivisionError):
            assert 1 / 0

    def test_int_divide(self):
        """Assertion Error"""
        with pytest.raises(AssertionError):
            assert 10 // 3 == 10 / 3

    def test_int_value(self):
        """Error: strings result in an integer type"""
        with pytest.raises(ValueError):
            assert int('10.0')

    def test_int_bool(self):
        """Assertion Error"""
        with pytest.raises(AssertionError):
            assert type(10 / 2) == type(5)

@pytest.mark.parametrize('i', list(range(10)))
def test_int_whole(i):
    """Test of int"""
    a = i + 0.1256
    assert int(a) == a//1
    
