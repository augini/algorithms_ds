# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan&id=algorithm-i

from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = defaultdict(int)
        l = len(numbers)

        for i in range(l):
            curr = numbers[i]

            if indices[target - curr]:
                return [indices[target - curr], i + 1]
            else:
                indices[curr] = i + 1
