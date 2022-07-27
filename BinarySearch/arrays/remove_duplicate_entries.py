# https://binarysearch.com/problems/Remove-Last-Duplicate-Entries
from collections import Counter

class Solution:
    def solve(self, nums):
        _c = Counter(nums)
        result = []

        for i in range(len(nums)):
            if _c[nums[i]] > 0:
                result.append(nums[i])
                
                if _c[nums[i]] == 2:
                    _c[nums[i]] = 0
                else:
                    _c[nums[i]] = _c[nums[i]] - 1
        
        return result