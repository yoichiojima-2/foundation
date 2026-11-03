from longest_substring_without_repeating_charactors.solution import Solution

def test_soluion_0():
    assert Solution().solution("abcabcbb") == 3

def test_soluion_1():
    assert Solution().solution("bbbbb") == 1

def test_solution_2():
    assert Solution().solution("pwwkew") == 3