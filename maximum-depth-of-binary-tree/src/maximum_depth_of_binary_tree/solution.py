from dsa import TreeNode


class Solution:
    def solution(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1 + max(self.solution(root.left), self.solution(root.right))
