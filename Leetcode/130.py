from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])

        def flip(starting: tuple):
            all_points = []
            stack = [starting]
            visited = set()

            while stack:
                cr, cc = stack.pop()
                visited.add((cr, cc))
                all_points.append((cr, cc))

                for _r, _c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = cr + _r, cc + _c
                    if (nr, nc) not in visited:
                        if (
                            nr < row
                            and nr >= 0
                            and nc < col
                            and nc >= 0
                            and board[nr][nc] == "O"
                        ):
                            stack.append((nr, nc))

            for x, y in all_points:
                if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                    return

            for x, y in all_points:
                board[x][y] = "X"

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    flip((r, c))
        return board
