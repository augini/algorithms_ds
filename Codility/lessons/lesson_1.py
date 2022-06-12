# binary gap


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary_rep = format(N, "b")
    print(binary_rep)
    steps, counting, count = [], False, 0

    if len(binary_rep) == 1 or "0" not in binary_rep:
      return 0

    for digit in binary_rep:

      if digit == "1" and counting == False:
        counting = True
      elif digit == "1" and counting == True:
        steps.append(count)
        count = 0
      
      if digit == "0" and counting == True:
        count = count + 1

    if len(steps) >= 1:
      return max(steps)
    
    return 0


print(solution(32))