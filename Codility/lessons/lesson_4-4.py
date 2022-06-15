# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # sort the list
    A = list(dict.fromkeys(A))
    A = sorted(A)

    filtered = []

    # get rid of negative values
    for x in A:
      if x > 0:
         filtered.append(x)
         
    A = filtered
    
    # return 1 if all values were negative
    if len(A) == 0:
       return 1
    
    for i in range (1, len(A)+1):
      if i != A[i-1]:
         return i

    return i+1
 

# print(solution([1, 3, 6, 4, 1, 2]))
# print(solution([1,2,3]))
print(solution([-1, -3]))
# print(solution([1, 2, 3, 1, 1, 2, 4, 5, -1000000, 1000000]))
