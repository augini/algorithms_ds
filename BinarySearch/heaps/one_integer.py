import heapq

class Solution:
    def solve(self, nums):
        heapq.heapify(nums)
        total_sum = 0

        while len(nums) > 1:
           num1, num2 = heapq.heappop(nums), heapq.heappop(nums)
           total_sum+=num1+num2
           heapq.heappush(nums,num1+num2)
         
        return total_sum
     
sample = Solution()
print(sample.solve([1, 2, 3, 4, 5]))