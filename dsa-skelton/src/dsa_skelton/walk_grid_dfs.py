def walk_grid_dfs(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Scan row-major; from each unvisited 1, recursive DFS in direction order down, up,
    right, left; return cells in visit order.
    """
    if not grid:
        return []

    rows, cols = len(grid), len(grid[0])
    dirs = (1, 0), (-1, 0), (0, 1), (0, -1)
    visited = []

    def dfs(row, col):
        if (
            row < 0 or col < 0 or row >= rows or col >= cols
            or grid[row][col] == 0
        ):
            return
        grid[row][col] = 0
        visited.append((row, col))
        for row_offset, col_offset in dirs:
            dfs(row + row_offset, col + col_offset)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                dfs(row, col)
    return visited
