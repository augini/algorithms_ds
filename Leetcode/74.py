# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search for the matrix rows
        start, end = 0, len(matrix)
        while start < end:
            mid = (start + end) // 2
            if matrix[mid][-1] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                # do binary search inside the row
                r = matrix[mid]
                start, end = 0, len(r)
                while start < end:
                    mid = (start + end) // 2
                    if r[mid] < target:
                        start = mid + 1
                    elif r[mid] > target:
                        end = mid - 1
                    else:
                        return True
        return False
