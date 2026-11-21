def walk_topo(graph: dict[int, list[int]]) -> list[int]:
    """Return a topological order of the DAG (edge u -> v means u comes before v)."""
    pass


# Every node appears as a key; graph[u] lists the nodes u points to.
GRAPH1 = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
GRAPH2 = {}
GRAPH3 = {1: []}
GRAPH4 = {1: [2], 2: [3], 3: []}  # a chain has exactly one valid order
GRAPH5 = {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: [7], 7: [], 8: [5]}
