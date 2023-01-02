from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        for m in range(row):
            for n in range(column):

                if grid[m][n] == 1 and (m, n) not in visited:
                    stack = [(m, n)]
                    visited.add((m, n))
                    counter = 0

                    while stack:
                        y, x = stack.pop()
                        counter += 1

                        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            temp_y = y + i
                            temp_x = x + j

                            if temp_y > row - 1 or temp_x > column - 1:
                                continue
                            if temp_y < 0 or temp_x < 0:
                                continue

                            if (
                                grid[temp_y][temp_x] == 1
                                and (temp_y, temp_x) not in visited
                            ):
                                stack.append((temp_y, temp_x))
                                visited.add((temp_y, temp_x))

                    if counter > max_area:
                        max_area = counter

        return max_area
