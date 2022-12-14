# https://leetcode.com/problems/minimum-falling-path-sum/description/

# 931. Minimum Falling Path Sum

from collections import defaultdict
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        col, row = len(matrix) - 1, len(matrix[0]) - 1
        dp = defaultdict(int)

        def dfs(curr_col, curr_row):

            if curr_col < col:
                curr = matrix[curr_col][curr_row]
                middle = (curr_col + 1, curr_row)

                if curr_row > 0 and curr_row < row:
                    left, right = (curr_col + 1, curr_row - 1), (
                        curr_col + 1,
                        curr_row + 1,
                    )

                    if dp[left] and dp[middle] and dp[right]:
                        return curr + min(dp[left], dp[middle], dp[right])
                    else:
                        dp[left] = dfs(curr_col + 1, curr_row - 1)
                        dp[right] = dfs(curr_col + 1, curr_row + 1)
                        dp[middle] = dfs(curr_col + 1, curr_row)
                        return curr + min(dp[left], dp[middle], dp[right])

                elif curr_row == 0:
                    right = (curr_col + 1, curr_row + 1)

                    if dp[middle] and dp[right]:
                        return curr + min(dp[middle], dp[right])
                    else:
                        dp[right] = dfs(curr_col + 1, curr_row + 1)
                        dp[middle] = dfs(curr_col + 1, curr_row)
                        return curr + min(dp[middle], dp[right])

                elif curr_row == row:
                    left = (curr_col + 1, curr_row - 1)
                    return curr + min(
                        dfs(curr_col + 1, curr_row), dfs(curr_col + 1, curr_row - 1)
                    )

            coor = (curr_col, curr_row)

            return matrix[curr_col][curr_row]

        mins = []
        for i in range(len(matrix[0])):
            temp = dfs(0, i)
            mins.append(temp)
        return min(mins)
