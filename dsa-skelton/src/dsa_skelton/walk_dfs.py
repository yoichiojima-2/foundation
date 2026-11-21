def walk_dfs(tree: dict[int, list[int]], node: int, order: list[int]) -> list[int]:
    """Recursive pre-order DFS: append node to order, recurse into children in list order, return order."""
    pass


# Every node appears as a key; leaves map to [].
TREE1 = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
TREE2 = {1: []}
TREE3 = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8, 9],
    5: [10],
    6: [],
    7: [],
    8: [11, 12],
    9: [],
    10: [],
    11: [],
    12: [],
}
