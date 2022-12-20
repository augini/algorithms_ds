# https://leetcode.com/problems/search-insert-position/description/?envType=study-plan&id=algorithm-i
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums)

        while start < end:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
        return start
