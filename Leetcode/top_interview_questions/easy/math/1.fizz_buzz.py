class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
       answers = []
       for x in range(1, n+1):
            if x %3 == 0 and x% 5 == 0:
              answers.append("FizzBuzz")
            elif x % 3 == 0 and x%5 !=0:
              answers.append("Fizz")
            elif x % 5 == 0 and x%3 != 0:
              answers.append("Buzz")
            else:
               answers.append(f"{x}")
       return answers
     
Sample = Solution()
print(Sample.fizzBuzz(15))
# print(Sample.fizzBuzz(3))
