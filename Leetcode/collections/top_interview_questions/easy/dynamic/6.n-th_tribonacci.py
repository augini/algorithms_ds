class Solution:
    def tribonacci(self, n: int) -> int:
       tribonaccis = [0, 1, 1]
       # edge case if n is less than 3
       
       for x in range (3, n+1):
          next_seq = tribonaccis[x-3] + tribonaccis[x-2] + tribonaccis[x-1]
          tribonaccis.append(next_seq)
         
       return tribonaccis[n]

Sample = Solution()
print(Sample.tribonacci(25))