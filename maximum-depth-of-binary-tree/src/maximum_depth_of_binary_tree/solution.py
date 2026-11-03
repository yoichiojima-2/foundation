from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def solution(self, root):
        if root is None:
            return 0
        return 1 + max(self.solution(root.left), self.solution(root.right))
