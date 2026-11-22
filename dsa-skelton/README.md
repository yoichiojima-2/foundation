# dsa-skelton

Algorithm skeletons to implement for practice. Each module in
`src/dsa_skelton/` holds one or more functions with a docstring describing
the expected result, and `tests/` has a matching test file. A skeleton that
is not implemented yet raises `NotImplementedError`, so its tests fail until
it is written.

```sh
uv run pytest                          # everything
uv run pytest tests/test_bfs.py        # one skeleton
uv run pytest tests/test_bfs.py -vvv   # with full assertion diffs
```

| Module | Functions | Topic |
|---|---|---|
| `walk_hash` | `walk_hash` | Hash map counting |
| `walk_prefix` | `walk_prefix` | Prefix sums |
| `walk_two_pointers` | `walk_two_pointers` | Two pointers |
| `walk_fixed_window` | `walk_fixed_window` | Fixed-size sliding window |
| `walk_variable_window` | `walk_variable_window` | Variable-size sliding window |
| `walk_binary_search` | `walk_binary_search` | Binary search |
| `walk_lower_bound` | `walk_lower_bound` | Lower bound |
| `walk_stack` | `walk_stack` | Stack |
| `walk_next_greater` | `walk_next_greater`, `daily_temperatures` | Monotonic stack |
| `walk_heap` | `walk_heap` | Heap |
| `walk_reverse` | `walk_reverse`, `merge_two_lists` | Linked list |
| `walk_middle` | `walk_middle`, `has_cycle` | Slow and fast pointers |
| `walk_bfs` | `walk_bfs` | Breadth-first search |
| `walk_dfs` | `walk_dfs` | Depth-first search |
| `walk_grid_dfs` | `walk_grid_dfs` | Depth-first search on a grid |
| `walk_topo` | `walk_topo` | Topological sort |
| `walk_components` | `walk_components`, `count_provinces` | Union-find |
| `walk_dijkstra` | `walk_dijkstra`, `network_delay` | Dijkstra shortest paths |
| `walk_merge` | `walk_merge` | Merge intervals |
| `walk_subsets` | `walk_subsets` | Backtracking |
| `walk_dp` | `walk_dp` | Dynamic programming |

Linked lists, trees and graphs in the tests are built with the helpers from
[`../dsa`](../dsa).
