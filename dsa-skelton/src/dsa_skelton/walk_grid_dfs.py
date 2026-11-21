def walk_grid_dfs(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Scan row-major; from each unvisited 1, recursive DFS in direction order down, up, right, left; return cells in visit order."""
    pass


GRID1 = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
]
GRID2 = []
GRID3 = [
    [0, 0],
    [0, 0],
]
GRID4 = [[1]]
GRID5 = [
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1],
]
