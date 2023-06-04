# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
        stack = []

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                    stack.append((r, c))

                while stack:
                    cr, cc = stack.pop()
                    # convert the current cell to 0 to mark it as visited
                    grid[cr][cc] = "0"

                    # get the neighbouring cells
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + x, cc + y
                        if (
                            nr < row
                            and nr >= 0
                            and nc < col
                            and nc >= 0
                            and grid[nr][nc] == "1"
                        ):
                            stack.append((nr, nc))

        return count


# when traversing graphs, make sure to get the row first with graph length
# then get the column length with the lenght of the very first row

grid = [["1", "0", "1", "1", "0", "1", "1"]]
sample = Solution()
print(sample.numIslands(grid))
