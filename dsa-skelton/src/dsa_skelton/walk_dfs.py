from dsa import GraphNode


def walk_dfs(node: GraphNode) -> list[int]:
    """Recursive pre-order DFS from node: visit node, then recurse into its
    neighbors (children) in list order; return the visited vals.
    """
    visited = []

    def dfs(node):
        if not node:
            return
        visited.append(node.val)
        for nb in node.neighbors:
            dfs(nb)
        return visited

    return dfs(node)
