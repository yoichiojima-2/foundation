from functools import cache


class Solution:
    def solution(self, n):
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def _solution(self, n):
        _solution(n)


@cache
def _solution(n):
    if n <= 2:
        return n
    return _solution(n - 1) + _solution(n - 2)
