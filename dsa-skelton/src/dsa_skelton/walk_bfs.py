def walk_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """Breadth-first visit order from start, enqueuing neighbours in list order."""
    pass


# Every node appears as a key; neighbours are visited in the order listed.
GRAPH1 = {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: []}
GRAPH2 = {1: []}
GRAPH3 = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}  # undirected, has cycles
GRAPH4 = {1: [2], 2: [], 3: [1]}  # 3 is unreachable from 1
GRAPH5 = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [6, 7],
    4: [8],
    5: [9],
    6: [9, 10],
    7: [10],
    8: [],
    9: [],
    10: [1],  # back edge to the start
}
