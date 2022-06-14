# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Check if the given array is a permutation or not
def solution(A):
    # write your code in Python 3.6
    _sorted = sorted(A)

    for count, x in zip(range(1, len(_sorted) + 1), _sorted):
        print(count, x)
        if count != x:
            return 0

    return 1


print(solution([2]))
