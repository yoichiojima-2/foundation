# dsa

Shared data structures and builders for the other Python projects in this
repo. Depend on it as an editable path dependency (`uv add --editable ../dsa`)
and import everything from the package root: `from dsa import ListNode, to_linked`.

| Name | Module | What it is |
|---|---|---|
| `ListNode` | `linked_list` | Singly linked list node (`val`, `next`) |
| `to_linked(values)` | `linked_list` | Build a linked list from a list; `None` when empty |
| `to_cyclic_linked(values, pos)` | `linked_list` | Build a linked list whose tail links back to index `pos` |
| `to_list(head)` | `linked_list` | Collect a linked list's values into a list |
| `TreeNode` | `tree` | Binary tree node (`val`, `left`, `right`) |
| `to_tree(values)` | `tree` | Build a tree from a LeetCode-style level-order list (`None` = missing) |
| `GraphNode` | `graph` | Graph node (`val`, `neighbors`), compared by identity |
| `to_graph(adj)` | `graph` | Build linked nodes from an adjacency dict, keyed by `val` |
| `DSU(n)` | `dsu` | Disjoint set union over `0..n-1`: `find`, `union`, `connected` |

```sh
uv run pytest
```
