# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from collections import Counter
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        c = Counter(nums)

        if target in nums:
            index = nums.index(target)
            return [index, index + c[target] - 1]

        return [-1, -1]
