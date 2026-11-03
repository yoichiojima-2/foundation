from two_sum.two_sum import Solution


def test_two_sum_0():
    assert Solution().two_sum([1, 3, 5, 9], 8) == (1, 2)


def test_two_sum_1():
    assert Solution().two_sum([1, 3, 5, 9], 14) == (2, 3)
