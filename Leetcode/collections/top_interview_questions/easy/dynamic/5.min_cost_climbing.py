class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
       costs  = [cost[0], cost[1]]
       
       for step in range (2, len(cost)):
          total_cost = cost[step] + min(costs[step-1], costs[step-2])
          costs.append(total_cost)

       return min(costs[-1], costs[-2])
     
Sample = Solution()
print(Sample.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))