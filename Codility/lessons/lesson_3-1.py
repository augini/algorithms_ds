import math

def solution(X, Y, D):
    # write your code in Python 3.6
    
    if X == Y:
      return 0

    if (Y % D) == X:
      return math.floor( Y / D )

    else:
      remainder = (Y-X) % D
      steps = (Y-X) / D
      if remainder == 0:
        return int(steps)
      else: 
        return int(math.floor(steps) + 1)
