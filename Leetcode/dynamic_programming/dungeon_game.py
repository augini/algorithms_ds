# https://leetcode.com/problems/dungeon-game/
from typing import List

class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        row_length = len(grid[0]) -1
        grid_length = len(grid) - 1
        
        if grid[-1][-1] < 0:
            grid[-1][-1] = abs(grid[-1][-1]) + 1
        else:
            grid[-1][-1] = 1
            
        for i in range(grid_length, -1, -1):
            for j in range(row_length, -1, -1):

                if i < grid_length and j < row_length :
                    _min = min(grid[i+1][j],grid[i][j+1])
                    
                    if grid[i+1][j] < 0 or grid[j][i+1] < 0:
                        _min = -1 * _min
                        
                    grid[i][j] = _min - grid[i][j]
                    if _min == 0:
                        grid[i][j] +=1
                elif i == grid_length and j < row_length:
                    grid[i][j] = grid[i][j+1] - grid[i][j]
                    
                    if grid[i][j+1] == 0:
                        grid[i][j] +=1
                    
                elif j == row_length and i < grid_length:
                    grid[i][j] = grid[i+1][j] - grid[i][j]
                    
                    if grid[i+1][j] == 0:
                        grid[i][j] +=1
                    
        for item in grid:
            print(item)
            
        if grid[0][0] <= 0:
            return 1
        return grid[0][0]
                    