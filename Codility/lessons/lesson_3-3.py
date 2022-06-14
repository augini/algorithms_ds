# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    total_sum = sum(A)
    diff_array = []

    left_part = 0

    for x in range(1, len(A)):
        left_part = left_part + A[x - 1]
        right_part = total_sum - left_part

        diff_array.append(abs(left_part - right_part))

    # print(diff_array)
    if len(diff_array) != 0:
        return min(diff_array)

    return 0
    pass


print(f"Testing abs method {abs(3-9)}")

print(solution([3, 1, 1]))
