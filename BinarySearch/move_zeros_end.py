class Solution:
    def solve(self, nums):
        
        zero_count = 0
        non_zero_index = 0
        list_len = len(nums)

        for i in range(list_len):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index+=1

            elif nums[i] == 0:
                zero_count +=1

        for i in range(list_len - zero_count, list_len):
            nums[i] = 0
        
        return nums
     
sample = Solution()
print(sample.solve([0, 1, 0, 2, 3, 5, 6, 0,129]))