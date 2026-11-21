def walk_variable_window(nums: list[int], k: int):
    """Grow the window rightward, shrink from the left while its sum exceeds k;
    return the window (as a list) after each step.
    """
    left = 0
    results = []
    sum_ = 0
    for right in range(len(nums)):
        sum_ += nums[right]
        while sum_ > k:
            sum_ -= nums[left]
            left += 1
        results.append(nums[left:right + 1])
    return results
