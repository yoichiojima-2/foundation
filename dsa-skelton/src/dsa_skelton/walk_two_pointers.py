def walk_two_pointers(nums: list[int]):
    """Move left/right pointers inward while left < right; return the (nums[left],
    nums[right]) pairs visited.
    """
    left, right = 0, len(nums) - 1
    res = []
    while left < right:
        res.append((nums[left], nums[right]))
        left += 1
        right -= 1
    return res

