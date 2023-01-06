# https://leetcode.com/problems/permutations-ii/description/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        first = nums[0]
        rest = nums[1:]

        permsWithoutFirst = self.permuteUnique(rest)
        allPerms = set()

        for item in permsWithoutFirst:
            for i in range(len(item) + 1):
                permsWithFirst = [*item[:i], first, *item[i:]]
                allPerms.add(tuple(permsWithFirst))

        return allPerms
