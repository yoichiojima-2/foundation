class Solution:
    def solution(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def _solution(self, s):
        # simple, but the purpose is learning
        t = [c.lower() for c in s if c.isalnum()]
        return t == t[::-1]