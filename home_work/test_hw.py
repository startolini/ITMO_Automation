def test_passing_hw():
    assert ('home', 'work') == ('home', 'work')

def test_passing_qa():
    assert ('QA') == ('QA')

def test_passing_num():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)