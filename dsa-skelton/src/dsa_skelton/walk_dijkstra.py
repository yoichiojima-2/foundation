def walk_dijkstra(
    graph: dict[int, list[tuple[int, int]]], start: int
) -> dict[int, int]:
    """Return the shortest distance from start to every node of the weighted graph."""
    raise NotImplementedError


def network_delay(times: list[list[int]], n: int, k: int) -> int:
    """Return the time for a signal from k to reach all n nodes, or -1 if it cannot."""
    raise NotImplementedError
