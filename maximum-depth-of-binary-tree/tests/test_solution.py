from collections import deque

import pytest
from maximum_depth_of_binary_tree.solution import Solution, TreeNode


def to_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


@pytest.mark.parametrize(
    "values, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([1, 2, None, 3, None, 4], 4),
        ([1, None, 2, None, 3, None, 4], 4),
    ],
)
def test_max_depth(values, expected):
    assert Solution().solution(to_tree(values)) == expected
