def walk_variable_window(nums: list[int], k: int):
    """Grow the window rightward, shrink from the left while its sum exceeds k; return the window (as a list) after each step."""
    left = 0
    results = []
    for right in range(len(nums)):
        if right - left + 1 > k:
            left += 1
        results.append(nums[left:right])
    return results


# Inputs are non-negative, so shrinking always lowers the sum.
NUMS1, K1 = [1, 2, 3, 4, 5], 6
NUMS2, K2 = [], 5
NUMS3, K3 = [9], 5  # single element larger than k -> window shrinks to empty
NUMS4, K4 = [3, 3, 3, 3], 6
NUMS5, K5 = [2, 1, 5, 1, 3, 2, 4, 1], 7
