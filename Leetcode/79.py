# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    # start the depth first search
                    visited = set()
                    visited.add((r, c))

                    s = [(r, c, 0, visited.copy())]

                    while s:
                        _r, _c, index, visited = s.pop()

                        if index == len(word) - 1:
                            return True

                        for x, y in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                            rr = _r + x
                            cc = _c + y
                            if (
                                (rr, cc) not in visited
                                and 0 <= rr < R
                                and 0 <= cc < C
                                and board[rr][cc] == word[index + 1]
                            ):
                                s.append(
                                    (
                                        rr,
                                        cc,
                                        index + 1,
                                        set([(rr, cc), *visited.copy()]),
                                    )
                                )
        return False


sample = Solution()
print(
    sample.exist(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        "ABCEFSADEESE",
    )
)
