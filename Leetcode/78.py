# https://leetcode.com/problems/subsets/description/
from typing import List


class Solution:
    def _subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        first = nums[0]
        rest = nums[1:]

        combsWithoutFirst = self.subsets(rest)
        combsWithFirst = []

        for item in combsWithoutFirst:
            combsWithFirst.append([first, *item])

        return [*combsWithoutFirst, *combsWithFirst]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, length = [], len(nums)
        subset = []

        def dfs(i):
            if i >= length:
                res.append(subset.copy())
                return

            # decision to include i
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include i
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
