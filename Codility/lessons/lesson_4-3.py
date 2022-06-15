# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    # write your code in Python 3.6

    length = len(A)

    # init the counters with 0
    _counters = [0 for i in range(N)]

    max_value, last_update = 0, 0

    for c in range(0, length):
        if A[c] <= N:
            indx = A[c] - 1
            
            if _counters[indx] < last_update:
                _counters[indx] = last_update + 1
            else:
                _counters[indx] = _counters[indx] + 1
            
            if _counters[indx] > max_value:
                max_value = _counters[indx]
                
        elif A[c] == N + 1:
            last_update = max_value

    for c in range(0, len(_counters)):
        if _counters[c] < last_update:
            _counters[c] = last_update

    return _counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
# print(solution(1, [1]))
# print(solution(20, [21, 7, 14, 21, 14, 21, 18, 5, 5, 21, 14, 7, 6, 21, 6, 14, 18, 15, 4, 10, 19, 5, 10, 10, 12, 10, 17, 4, 16, 21]))
