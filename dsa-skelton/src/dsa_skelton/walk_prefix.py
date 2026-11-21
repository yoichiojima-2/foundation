def walk_prefix(nums: list[int]) -> list[int]:
    """Return prefix sums with a leading 0, so the result has len(nums) + 1 entries."""
    res = [0]
    for i in nums:
        res.append(res[-1] + i)
    return res
