# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
      return A[0]

    A = sorted(A)
    
    length = len(A)
    for i in range(0, length, 2):
      
      if i+1 == length:
        return A[i]

      if A[i] != A[i+1]:
        if A[i+1] == A[i+2]:
          return A[i]
        else:
          return A[i+1]
    
    return 0
    pass



print(solution([2, 2, 3, 3, 4]))