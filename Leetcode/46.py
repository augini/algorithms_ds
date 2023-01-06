# https://leetcode.com/problems/permutations/description/?envType=study-plan&id=algorithm-i

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        first = nums[0]
        rest = nums[1:]

        permsWithoutFirst = self.permute(rest)
        allPerms = []

        for item in permsWithoutFirst:
            for i in range(len(item) + 1):
                permsWithFirst = [*item[:i], first, *item[i:]]
                allPerms.append(permsWithFirst)

        return allPerms
