# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    if len(A) == 0:
      return 1

    A = sorted(A)

    for i in range (0, len(A)+1):
      
      temp = i+1
      if  i >= len(A) or temp != A[i]:
        return temp
    
    return 0
    pass


print(solution([1]))