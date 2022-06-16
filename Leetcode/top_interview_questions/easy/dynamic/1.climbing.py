class _Solution:   
    # time limit exceeded when using this approach    
     def _climbStairs(self, n: int) -> int:
       #initialize the values    
       queue = [[1], [2]]
       sums = [1, 2]
       combinations = []
       
       while len(queue) > 0:
           current = queue.pop(0)
           current_sum = sums.pop(0)
           
           if current_sum == n:
               combinations.append(current)
               continue
           
           if current_sum + 1 <= n:
               queue.append([*current, 1])
               sums.append(current_sum+1)
               
           if current_sum + 2 <= n:
               queue.append([*current, 2])
               sums.append(current_sum+2)
                
       return len(combinations)

class Solution:
    # dynamic programming approach
     def climbStairs(self, n: int) -> int:   
       combinations = [1,1] # one way to climb zero starirs, one stair
       
       for x in range (2, n+1):
           steps = combinations[x-1] + combinations[x-2]
           combinations.append(steps)
        
       return combinations[n]
   
Sample = Solution()

print(Sample.climbStairs(2))