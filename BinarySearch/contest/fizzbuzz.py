class Solution:
    def _solve(self, n):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    def solve(self, n):
        c3, c5 = 0, 0
        result = []
        for i in range(1, n+1):
            c3+=1
            c5+=1

            if c3 == 3 and c5 == 5:
                result.append("FizzBuzz")
                c3, c5 = 0, 0
            elif c3 == 3:
                result.append("Fizz")
                c3 = 0
            elif c5 == 5:
                result.append("Buzz")
                c5=0
            else:
                result.append(str(i))

        return result