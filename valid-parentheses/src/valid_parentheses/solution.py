class Solution:
    def solution(self, s):
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in pairs:  # closing
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:  # opening
                stack.append(c)
        return not stack