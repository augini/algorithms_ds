import math

class Solution:
    def solve(self, nums):

        shortest = math.inf
        count = 0

        for i in range(1, len(nums)):
            if nums[i+1] < nums[i]:
                count+=1
            else:
                if count + 1 < shortest and count != 0:
                    shortest = count + 1
                count = 0

        print(count, shortest)
        return min(shortest, count)