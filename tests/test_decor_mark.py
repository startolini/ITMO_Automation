import pytest

@pytest.mark.smoke
def test_first():
    assert 1 == 1


@pytest.mark.regress
def test_first1():
    assert True


@pytest.mark.regress
def test_first2():
    assert True


@pytest.mark.regress
def test_first3():
    assert True
