def walk_fixed_window(nums: list[int], k: int):
    """Return every contiguous window of width k, left to right, as lists."""
    res = []
    for i in range(len(nums) - k + 1):
        res.append(nums[i : i + k])
    return res
