# https://binarysearch.com/room/Array-of-Sunshine-LkGA3FOABd?questionsetIndex=2

def two_sum(arr, target):
    nums_map = {}

    for num in arr:
        if target - num in nums_map:
            return True
        
        nums_map[num] = True
    
    return False
    

class Solution:
    def solve(self, nums, k):
        
        for index in range(len(nums)):
            current_number = nums[index]

            search_arr = nums[:index] + nums[index + 1:]

            if two_sum(search_arr, k - current_number):
                return True
        
        return False


class Solution:
    def solve(self, nums, k):
        nums.sort()

        _len = len(nums)
        i, j = 0, _len - 1

        for i in range(_len):
            fixed = nums[i]

            l, r = i+1,  _len -1

            while l < r:
                sm = fixed + nums[l] + nums[r]
                if sm == k:
                    return True
                elif sm > k:
                    r-=1
                else:
                    l+=1
        
        return False