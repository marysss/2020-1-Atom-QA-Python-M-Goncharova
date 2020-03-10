import pytest

def func():
    """Create a list"""
    source_list = [10, 'abc', 15, '10c']
    return source_list

def test_list_reverse():
    """Reverse list"""
    lst = func()
    lst.reverse()
    assert lst == ['10c', 15, 'abc', 10]

def test_list_unpacking():
    """Add new elements in list"""
    lst = func()
    new_lst = [*lst, 1, 0]
    assert new_lst == [10, 'abc', 15, '10c', 1, 0]

class TestDefaultList:
    """Тесты с ожидаемыми ошибками"""

    def test_list_sort(self):
        """Type Error"""
        lst = func()
        with pytest.raises(TypeError):
            assert lst.sort()

    def test_list_zero(self):
        """Zero Division Error"""
        lst = [1, 0]
        with pytest.raises(ZeroDivisionError):
            assert lst[0] / lst[1]

@pytest.mark.parametrize('i', list(range(10)))
def test_list_append(i):
    """Add of number in list"""
    lst = func()
    lst.append(i)
    assert lst == [10, 'abc', 15, '10c', i]

