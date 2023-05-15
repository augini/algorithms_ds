# https://leetcode.com/problems/longest-consecutive-sequence/
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if (num - 1) not in numbers:
                length = 1
                temp = num + 1
                while temp in numbers:
                    length += 1
                    temp += 1

                if length > longest:
                    longest = length
        return longest
