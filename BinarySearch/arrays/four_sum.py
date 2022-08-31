# https://binarysearch.com/problems/Sum-of-Four-Numbers

from collections import defaultdict
from re import L

# Solution 1
# Time Complexity: O(n)^3
# Space Complexity: O(n)


class _Solution:
    nums = []

    def solve(self, nums, k):
        self.nums = nums

        def twoSum(nums, k):
            length = len(nums)
            d = defaultdict(int)

            for i in range(length):
                diff = k - nums[i]

                if d[nums[i]]:
                    return True
                else:
                    d[diff] = 1
            return False

        def threeSum(nums, k):
            length = len(nums)

            for i in range(1, length):
                if twoSum(nums[i:], k - nums[i - 1]):
                    return True

            return False

        def fourSum(nums, k):
            length = len(nums)

            for i in range(1, length):
                if threeSum(nums[i:], k - nums[i - 1]):
                    return True

            return False

        return fourSum(nums, k)


# We can make the above solution little better by getting
# rid of threeSum and fourSum functions and using a two pointer approach for twoSum


class Solution:
    def solve(self, nums, k):
        l = len(nums)
        d = {}

        for i in range(l - 1):
            for j in range(i + 1, l):
                d[nums[i] + nums[j]] = [i, j]

        for i in range(l - 1):
            for j in range(i + 1, l):
                sm = nums[i] + nums[j]

                if (k - sm) in d:
                    val = d[k - sm]

                    if val[0] != i and val[0] != j and val[1] != i and val[1] != j:
                        return True
        return False


sample = Solution()
print(sample.solve([0, 0, 0, -1], 0))
