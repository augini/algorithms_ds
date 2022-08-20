# https://leetcode.com/problems/triangle/submissions/
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tri_length = len(triangle)
        
        for i in range(1, tri_length):
            for j in range(len(triangle[i])):
                cur = triangle[i][j]
                prev_row, prev_col = i-1, j-1
                
                if j > 0 and j <= len(triangle[prev_row])-1:
                    triangle[i][j] = min(triangle[prev_row][prev_col], triangle[prev_row][j]) + cur
                elif j == 0:
                    triangle[i][j] = triangle[prev_row][j] + cur
                elif j == len(triangle[prev_row]):
                    triangle[i][j] = triangle[prev_row][prev_col] + cur
        
        return min(triangle[-1])
        