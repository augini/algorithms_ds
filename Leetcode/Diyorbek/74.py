# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        left = 0
        right = len(matrix) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid
            else:
                right = mid
        if matrix[right][0] > target:
            return binary_search(matrix[left], target)
        return binary_search(matrix[right], target)