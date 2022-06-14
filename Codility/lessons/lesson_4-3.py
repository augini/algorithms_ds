# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    # write your code in Python 3.6

    length = len(A)
    
    # init the counters with 0
    _counters = [0 for i in range(N)]

    max_values = []
    for c in range(0, length):
        if A[c] <= N:
            indx = A[c]-1
            if len(max_values) > 0 and _counters[indx] < max_values[-1]:
                _counters[indx] = max_values[-1] +1
            else:
                _counters[indx] = _counters[indx] + 1
        elif A[c] == N+1:
            max_values.append(max(_counters))
     
    try:        
        min_value = max_values[-1]
    except:
        min_value=0
    
    for count in range(0, len(_counters)):
        if _counters[count] < min_value:
            _counters[count] = min_value
            
    return _counters


# print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
print(solution(1, [1]))
# print(solution(20, [21, 7, 14, 21, 14, 21, 18, 5, 5, 21, 14, 7, 6, 21, 6, 14, 18, 15, 4, 10, 19, 5, 10, 10, 12, 10, 17, 4, 16, 21]))


