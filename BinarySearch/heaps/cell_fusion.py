import heapq
import math

class Solution:
    def solve(self, cells):
       
        for i in range(len(cells)):
           cells[i] = -cells[i]
           
        heapq.heapify(cells)
        
        while len(cells) > 1:
           max_1, max_2 = heapq.heappop(cells),heapq.heappop(cells)
           
           if max_1 != max_2:
              cells.append(math.ceil((max_1+max_2)/3))

        if len(cells) == 1:
           return -cells[0]
        
        return -1
     
sample = Solution()
# print(sample.solve([10,30,30,20]))
# print(sample.solve([1]))
print(sample.solve([1,1,3]))

