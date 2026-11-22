def walk_components(n: int, unions: list[tuple[int, int]]) -> int:
    """Return the number of connected components among n nodes after the unions."""
    raise NotImplementedError


class DSU:
    """Disjoint-set union over the nodes 0..n-1."""

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def find(self, x: int) -> int:
        """Return the representative of the set containing x."""
        raise NotImplementedError

    def union(self, a: int, b: int) -> None:
        """Merge the sets containing a and b."""
        raise NotImplementedError


def count_provinces(is_connected: list[list[int]]) -> int:
    """Return the number of provinces in the adjacency matrix is_connected."""
    raise NotImplementedError
