# Problem Statement

# You have to implement the trace_path() function which will take in a list of source-destination pairs and
# return the correct sequence of the whole journey from the first city to the last.

# dict = {  "NewYork": "Chicago",  "Boston": "Texas",  "Missouri": "NewYork",  "Texas": "Missouri"}
# [["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]


def trace_path(my_dict):  # A Map object
    # dict = {
    #     "NewYork": "Chicago",
    #     "Boston": "Texas",
    #     "Missouri": "NewYork",
    #     "Texas": "Missouri"
    # }

    # find the starting city
    starting = set(my_dict.keys())
    destinations = set(my_dict.values())
    current = None

    for start in starting:
        if start not in destinations:
            current = start

    result = []
    while True:
        if current in starting:
            next_point = my_dict[current]
            result.append([current, next_point])
            current = next_point
        else:
            break
    return result


# Problem #2
# In this problem, you have to implement the find_pair() function which will find two pairs, [a, b] and [c, d], in a list such that : a+b=c+d

# You only have to find the first two pairs in the list which satisfies the above condition.


def find_pair(my_list):
    result = []
    # Create a dictionary my_dict with the key being the sum
    # and the value being a pair, i.e key = 3 , value = {1,2}
    # Traverse all possible pairs in my_list and store sums in my_dict
    # If sum already exists then print out the two pairs.
    my_dict = dict()
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            added = my_list[i] + my_list[j]  # calculate sum
            if added not in my_dict:
                # If added is not present in dict then insert it with pair
                my_dict[added] = [my_list[i], my_list[j]]
            else:
                # added already present in Map
                prev_pair = my_dict.get(added)
                # Since list elements are distinct, we don't
                # need to check if any element is common among pairs
                second_pair = [my_list[i], my_list[j]]
                result.append(prev_pair)
                result.append(second_pair)
                return result
    return result
