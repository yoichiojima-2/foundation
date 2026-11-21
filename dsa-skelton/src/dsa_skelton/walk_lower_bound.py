def walk_lower_bound(nums: list[int], target: int) -> int:
    """Return the first index i with nums[i] >= target in sorted nums
    (len(nums) if none).
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left