from collections import deque

from dsa import GraphNode


def walk_bfs(start: GraphNode) -> list[int]:
    """Breadth-first visit order (node vals) from start, enqueuing neighbours
    in list order.
    """
    q = deque([start])
    res = []
    while q:
        node = q.popleft()
        if node.val in res:
            continue
        res.append(node.val)
        for nb in node.neighbors:
            q.append(nb)
    return res
