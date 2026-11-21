from __future__ import annotations

from dataclasses import dataclass, field


# eq=False/repr=False: graphs can have cycles, so the generated __eq__/__repr__
# would recurse forever through neighbors. Nodes compare by identity instead.
@dataclass(eq=False, repr=False)
class GraphNode:
    val: int = 0
    neighbors: list[GraphNode] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"GraphNode({self.val}, neighbors={[n.val for n in self.neighbors]})"


def to_graph(adj: dict[int, list[int]]) -> dict[int, GraphNode]:
    """Build linked GraphNodes from an adjacency dict; return them keyed by val.

    Neighbour order is preserved. A node that only appears as a neighbour
    still gets a GraphNode.
    """
    nodes: dict[int, GraphNode] = {}

    def get(val: int) -> GraphNode:
        if val not in nodes:
            nodes[val] = GraphNode(val)
        return nodes[val]

    for val, neighbors in adj.items():
        node = get(val)  # create before its neighbours so keys keep adj order
        node.neighbors = [get(n) for n in neighbors]
    return nodes
