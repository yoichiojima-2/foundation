from binary_search.binary_search import Solution


def test_solution_0():
    assert Solution().search([1, 3, 5, 7, 9], 3) == 1


def test_solution_1():
    assert Solution().search([1, 3, 5, 7, 9], 5) == 2


def test_solution_2():
    assert Solution().search([1, 3, 5, 7, 9], 7) == 3


def test_solution_3():
    assert Solution().search([1, 3, 5, 7, 9], 9) == 4
