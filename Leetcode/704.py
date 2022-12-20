# https://leetcode.com/problems/binary-search/description/?envType=study-plan&id=algorithm-i
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums)

        while start < end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                return mid

        return -1
