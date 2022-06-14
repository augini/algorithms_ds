
# get the position of elements in the new list and create that list
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    dict = {}
    
    # get the new positions of elements in the new array
    for i in range(len(A)):
      dict[f"{i}_{A[i]}"] = (i+K)%len(A)

    new_list = []
    print(dict)

    for i in range(len(A)):
      current = list(dict.keys())[list(dict.values()).index(i)]
      digit = int(current.split("_")[1])
      new_list.append(digit)
    
    return new_list

    pass

print(solution([0,0,0], 1))