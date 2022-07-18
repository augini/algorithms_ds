# https://binarysearch.com/room/Graph-Traversers-CbCAR4sq12?questionsetIndex=0

class _Solution:
    def solve(self, nums):

        if len(nums) == 1:
           return nums[0]

        _min = min(nums)
        _max = 1
        
        for i in range(1, _min+1):
            if _min % i == 0:
                count = 0
                for val in nums:
                    if val % i == 0:
                        count+=1
                    else:
                        break

                if count == len(nums) and i > _max:
                    _max = i
                    
        return _max

# Euclidian algorithm states this regarding GCD of two numbers
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a%b)

class _Solution:
    def solve(self, nums):
       res = nums[0]
       
       for i in range(1, len(nums)):
          res = self.gcd(res, nums[i])
       return res 
     
    def gcd(self, a, b):
       if b == 0:
          return a
       
       return self.gcd(b, a % b)
       
# another approach is to use sorting and assume the smallest integer is the smallest, if it is not the smallest, we decrement it by one and keep going
   
class Solution:
    def solve(self, nums):
       max_gcd = sorted(nums)[0]
       
       counter = 0
       
       while max_gcd > 0:
         for value in nums:
            if value % max_gcd == 0:
               counter+=1
            else:
               break
            
         if counter == len(nums):
            return max_gcd
         
         else:
            counter = 0
            max_gcd-=1
            
       return max_gcd
       
    
Sample = Solution()
print(Sample.solve([6, 12, 9]))
# print(Sample.solve([6, 7, 9]))

