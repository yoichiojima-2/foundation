from collections import deque


def walk_topo(graph: dict[int, list[int]]) -> list[int]:
    """Return a topological order of the DAG (edge u -> v means u comes before v)."""
    in_degree = {vertex: 0 for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1
    queue = deque([vertex for vertex in graph if in_degree[vertex] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order
