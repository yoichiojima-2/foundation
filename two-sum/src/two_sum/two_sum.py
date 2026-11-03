class Solution:
    def two_sum(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return seen[need], i
            seen[x] = i
