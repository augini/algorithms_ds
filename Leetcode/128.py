# https://leetcode.com/problems/longest-consecutive-sequence/
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        sequence = 0

        for n in numbers:
            if (n - 1) not in numbers:
                length = 1
                temp = n + 1
                while temp in numbers:
                    length += 1
                    temp += 1

                if length > sequence:
                    sequence = length

        return sequence
