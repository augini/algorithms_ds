# https://leetcode.com/problems/minimum-path-sum/
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_length = len(grid[0])
        
        for i in range(len(grid)):
            for j in range(row_length):

                if i > 0 and j > 0: 
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
        
        return grid[-1][-1]
                