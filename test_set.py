import pytest

def set_creation(n):
    """Create set"""
    st = {i for i in range(n)}
    return st

def test_set_remove():
    """Remove set"""
    st = set_creation(10)
    st.clear()
    assert bool({}) == 0

def test_set_intersection():
    """Intersection"""
    st1 = {0}
    st2 = {1}
    assert (st1 & st2) == set()

class TestSet:

    def test_set_difference(self):
        """Difference"""
        st = {1, 2}
        st1 = {1, 3}
        assert st - st1 == {2}

@pytest.mark.parametrize('i', list(range(10)))
def test_set_len(i):
    """Lenght of set"""
    st = set_creation(i)
    assert len(st) == i

@pytest.mark.parametrize('i', list(range(2, 10)))
def test_set_bool(i):
    """Element test in set """
    st = set_creation(i)
    assert (1 in st) == 1

