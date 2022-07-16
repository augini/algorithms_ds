class Solution:
    def solve(self, nums):
        diff = int((nums[-1] - nums[0]) / len(nums))
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != diff:
                return nums[i-1] + diff
            elif nums[i] == nums[i-1]:
                return nums[i]

        return 0

sample = Solution()
# print(sample.solve([1, 3, 5, 9]))
# print(sample.solve([-8, 0]))
print(sample.solve([8, 8]))

