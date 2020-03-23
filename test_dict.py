import pytest

def dict_creation():
    """Create dictionary"""
    dct = {"c": "c",
           "a": "a",
           "b": "b"}
    return dct

def test_dict_empty():
    """Clear of dictionary"""
    empty_dict = dict()
    dct = dict_creation()
    dct.clear()
    assert empty_dict == dct

def test_dict_sort():
    """Sort of dictionary"""
    dct = dict_creation()
    sorted(dct)
    with pytest.raises(AssertionError):
        assert bool(dct == {"a": "a",
                   "b": "b",
                   "c": "c"}) == 0

def test_dict_update():
    """Update key in dictionary"""
    dct = dict_creation()
    assert dct.update({"a": "d"}) == None

class TestDefaultDict:
    """Тесты с ожидаемыми ошибками"""

    def test_dict_popitem(self):
        """Key Error"""
        empty_dict = dict()
        with pytest.raises(KeyError):
            assert empty_dict.popitem()

@pytest.mark.parametrize('i', ('a', 'b', 'c'))
def test_dict_get(i):
    """Key search"""
    dct = dict_creation()
    assert dct.get(i) == i

