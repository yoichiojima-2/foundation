from dsa_skelton.walk_dp import walk_dp

N1 = 5
N2 = 0
N3 = 1
N4 = 15


def test_small():
    assert walk_dp(N1) == [0, 1, 1, 2, 3, 5]


def test_zero():
    assert walk_dp(N2) == [0]


def test_one():
    assert walk_dp(N3) == [0, 1]


def test_larger():
    assert walk_dp(N4) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
