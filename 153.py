# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        while nums[start] > nums[end]:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]
