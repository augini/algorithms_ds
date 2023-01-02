from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque([])

        row, column = len(grid), len(grid[0])
        rotten_cells = 0
        orange_cells = 0

        for m in range(row):
            for n in range(column):
                if grid[m][n] == 2:
                    rotten.append((m, n, 0))

                if grid[m][n] == 1 or grid[m][n] == 2:
                    orange_cells += 1

        max_minute = 0

        while rotten:
            y, x, minute = rotten.popleft()
            rotten_cells += 1

            if minute > max_minute:
                max_minute = minute

            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                temp_y = y + i
                temp_x = x + j

                if temp_y > row - 1 or temp_x > column - 1:
                    continue
                if temp_y < 0 or temp_x < 0:
                    continue

                if grid[temp_y][temp_x] == 1:
                    grid[temp_y][temp_x] = 2
                    rotten.append((temp_y, temp_x, minute + 1))

        if rotten_cells == orange_cells:
            return max_minute
        else:
            return -1
