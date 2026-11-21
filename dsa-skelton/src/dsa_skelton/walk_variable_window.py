def walk_variable_window(nums: list[int], k: int):
    """Grow the window rightward, shrink from the left while its sum exceeds k;
    return the window (as a list) after each step.
    """
    left = 0
    results = []
    for right in range(len(nums)):
        if right - left + 1 > k:
            left += 1
        results.append(nums[left:right])
    return results
