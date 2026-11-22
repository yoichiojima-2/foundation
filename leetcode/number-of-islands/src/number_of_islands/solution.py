class Solution:
    def solution(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        return count
