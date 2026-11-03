from __future__ import annotations
from dataclasses import dataclass


class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    rigt: TreeNode | None = None
