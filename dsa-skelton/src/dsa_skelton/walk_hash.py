from collections import defaultdict


def walk_hash(nums: list[int]) -> dict[int, int]:
    """Count occurrences of each value in nums."""
    counter = defaultdict(int)
    for i in nums:
        counter[i] += 1
    return dict(counter)
