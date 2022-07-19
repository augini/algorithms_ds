class Solution:
    def solve(self, nums):
        _min = nums[0]
        nums[0] = 0
        
        for i in range(1, len(nums)): 
            current = nums[i]
            
            nums[i] = _min
            if current < _min:
                _min = current
        
        return nums
     
sample = Solution()
print(sample.solve([10, 5, 7, 9]))