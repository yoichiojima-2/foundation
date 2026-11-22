def walk_subsets(nums: list[int]) -> list[list[int]]:
    """Return all 2**len(nums) subsets via backtracking (duplicate values give duplicate
    subsets).
    """
    res = []
    path = []

    def backtrack(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res
