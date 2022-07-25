class Solution:
    def solve(self, nums):
        
        _length = len(nums)
        
        for i in range(_length):
            bound = 2*i + 1
            bound_2 = 2*i + 2

            if  bound_2 < _length:
                if not (nums[i] >= nums[bound]) or not (nums[i] >= nums[bound_2]):
                    return False
            else:
                if i!=0 and nums[(i-1)//2] < nums[i]:
                    return False

        return True