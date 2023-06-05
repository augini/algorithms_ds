from typing import Literal, List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        result = []

        def dfs(cell: tuple, ocean: Literal["p", "a"]):
            stack = [cell]
            visited = set()

            while stack:
                cr, cc = stack.pop()
                visited.add((cr, cc))

                if ocean == "p" and (cr == 0 or cc == 0):
                    return True
                elif ocean == "a" and (cr == row - 1 or cc == col - 1):
                    return True

                for r, c in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    nr, nc = cr + r, cc + c
                    if (nr, nc) not in visited:
                        if (
                            nr < row
                            and nr >= 0
                            and nc < col
                            and nc >= 0
                            and heights[nr][nc] <= heights[cr][cc]
                        ):
                            stack.append((nr, nc))
            return False

        for r in range(row):
            for c in range(col):
                if dfs((r, c), "p") and dfs((r, c), "a"):
                    result.append([r, c])
        return result
