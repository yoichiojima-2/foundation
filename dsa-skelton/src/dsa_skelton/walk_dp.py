def walk_dp(n: int) -> list[int]:
    """Bottom-up Fibonacci table dp[0..n] with dp[0] = 0, dp[1] = 1."""
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1): 
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp
