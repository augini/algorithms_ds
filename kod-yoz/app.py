import math
from collections import deque


def print_digits(num: int) -> None:
    """
    Kodni bu yerda yozing.
    """
    num = str(num)[::-1]
    for x in range(len(num)):
        print(num[x])


# print_digits(456)


def reverse_digits(num: int) -> int:
    """
    Kodni bu yerda yozing.
    """
    num = str(num)[::-1]
    return int(num)


# print(reverse_digits(710))

"""
Berilgan sonni ikkilik sanoqga o'tkazing.
Misol uchun:
    convert_to_binary(6) => "110"
    convert_to_binary(13) => "1101"
"""


def convert_to_binary(num: int) -> str:
    """
    Kodni bu yerda yozing.
    """
    return "{0:b}".format(int(num))


# print(convert_to_binary(32))


def is_power_of_two(num: int) -> bool:
    """
    Kodni bu yerda yozing.
    """
    binary = "{0:b}".format(num)
    if binary.index("1") == 0 and binary.count("1") == 1:
        return True
    return False


# print(is_power_of_two(4))


def sum_of_odd_numbers(n: int) -> int:
    """
    Kodni bu yerda yozing.
    """

    sum = 0
    for x in range(0, n + 1):
        if x % 2 == 1:
            sum += x
    return sum


# print(sum_of_odd_numbers(5))


def is_palindrome(word: str) -> bool:
    """
    Kodni bu yerda yozing.
    """
    reversed = word[::-1]
    if reversed == word:
        return True
    return False


"""
Ikki arrayda tartiblangan sonlar keltirilgan.
Ularni tartiblangan ko'rinishda birlashtiring.
Misol uchun:
  merge_two_arrays([4,5], [3]) -> [3,4,5]
  merge_two_arrays([1,3], [2,6]) -> [1,2,3,6]
"""
# Linear time


def merge_two_arrays(arr1, arr2):
    """
    Kodni bu yerda yozing.
    """
    sorted_arr = []
    index_1, index_2 = 0, 0

    for counter in range(0, (len(arr1) + len(arr2))):

        if index_1 >= len(arr1):
            sorted_arr.extend(arr2[index_2:])
            break
        elif index_2 >= len(arr2):
            sorted_arr.extend(arr1[index_1:])
            break

        if arr1[index_1] < arr2[index_2]:
            sorted_arr.append(arr1[index_1])
            index_1 = index_1 + 1

        elif arr1[index_1] > arr2[index_2]:
            sorted_arr.append(arr2[index_2])
            index_2 = index_2 + 1

    return sorted_arr


# print(merge_two_arrays([1,3], [2,6]))

"""
Berilgan linked list sonlarini ekranga chiqaring.
Misol: 1->2->3
Kutilgan natija:
1
2
3
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_elements(head: Node) -> None:
    """
    Kodni bu yerda yozing.
    """
    if head == None:
        return False

    while head != None:
        print(head.val)
        head = head.next


"""
Berilgan linked list o'rtasidagi elementni ekranga chiqaring.
Misol: 1->2->3
Kutilgan natija: 2

Yana bir misol: 1->2
Kutilgan natija: 2
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_middle(head: Node) -> None:
    """
    Kodni bu yerda yozing.
    """
    length = 0

    pointer = head
    if pointer == None:
        return False

    while pointer != None:
        length = length + 1
        pointer = pointer.next

    middle = math.floor(length / 2)
    length = 0
    pointer = head
    while pointer != None:
        if length == middle:
            print(pointer.val)

        length = length + 1
        pointer = pointer.next


"""
Berilgan linked listni teskari qiling.
Misol: 1->2->3
Kutilgan natija: 3->2->1

Yana bir misol: 1->2
Kutilgan natija: 2->1
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def reverse(head: Node) -> Node:
    """
    Kodni bu yerda yozing.
    """

    if head == None:
        return 0

    prev = None
    current = head

    while current.next is not None:
        next = current.next
        current.next = prev

        prev = current
        current = next

    current.next = prev

    return current


"""
Berilgan ikki so'z anagram ekanligiga tekshiring.
Misol uchun:
  is_anagram("lama", "alam") => True
  is_anagram("mosh", "shom") => True
  is_anagram("non", "nok") => False
"""


def is_anagram(word1: str, word2: str) -> bool:
    """
    Kodni bu yerda yozing.
    """
    count = {}
    for char in word1:
        count[char] = count.setdefault(char, 0) + 1

    for char in word2:
        if char in count.keys():
            count[char] = count[char] - 1

    for c in list(count.values()):
        if c != 0:
            return False

    return True


# print(is_anagram("lamma", "malla"))

"""
Array va bir son keltirilgan.
Array ichida yig'indisi berilgan songa teng bo'lgan juftlik borligni tekshiring.  
Misol uchun:
  two_sum([1,4,5,2], 3) => True  # chunki 1 va 2 soni arrayda mavjud, 1+2=3 
  two_sum([1,4,5,2], 8) => False
"""


def two_sum(arr, target) -> bool:
    """
    Kodni bu yerda yozing.
    """

    for x in range(len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] + arr[y] == target:
                return True
    return False


# print(two_sum([1,4,5,2], 3))

"""
Berilgan qavslar to'g'ri yopilganligiga tekshiring.
Qavslar - (), {}, [].
Misol uchun:
  valid_brackets("()()") = True
  valid_brackets("{()[]}") = True
  valid_brackets("{(]}") = False
"""


def valid_brackets(s: str) -> bool:
    """
    Kodni bu yerda yozing.
    """
    pairs = {"}": "{", ")": "(", "]": "["}
    stack = []

    for bracket in s:
        if bracket in pairs.keys() and len(stack) != 0 and stack[-1] == pairs[bracket]:
            stack.pop()
        else:
            stack.append(bracket)

    if len(stack) != 0:
        return False
    return True


# print(valid_brackets("{()[]}"))

"""
Berilgan sonlar yig'indisini rekursiya orqali hisoblang.
Misol uchun:
  sum_recursive([1,3]) => 4
  sum_recursive([4,5,2]) => 11
"""


def sum_recursive(nums) -> int:
    """
    Kodni bu yerda yozing.
    """
    if len(nums) == 1:
        return nums[0]

    current = nums.pop()
    return current + sum_recursive(nums)


# print(sum_recursive([4,5,2]))

"""
Rekursiya orqali, berilgan so'zga teskari so'z qaytaring.
Misol uchun:
  reverse_recursive("space") => "ecaps"
  reverse_recursive("where") => "erehw"
"""


def reverse_recursive(word: str) -> str:
    """
    Kodni bu yerda yozing.
    """
    if len(word) == 1:
        return word

    current = word[len(word) - 1]
    return current + reverse_recursive(word[0:-1])


# print(reverse_recursive("space"))

"""
Tartiblangan sonlar ro'yhati va qidirilayotgan son berilgan.
Array ichida berilgan son borligiga tekshiring.
Misol uchun:
  binary_search_recursive([1,4,5,7], 3) => False
  binary_search_recursive([1,4,5,7], 5) => True
"""


def binary_search_recursive(arr, target: int) -> bool:
    """
    Kodni bu yerda yozing.
    """

    if len(arr) == 1:
        return arr[0] == target

    mid = len(arr) // 2
    if arr[mid] == target:
        return True

    if target < arr[mid]:
        return binary_search_recursive(arr[0:mid], target)

    elif target > arr[mid]:
        return binary_search_recursive(arr[mid:], target)


# print(binary_search_recursive([1,4,5,7], 5))

"""
Tartiblangan sonlar ro'yhati va qidirilayotgan son berilgan.
Array ichida berilgan son borligiga tekshiring.
Misol uchun:
  binary_search_iterative([1,4,5,2], 3) => False
  binary_search_iterative([1,4,5,2], 5) => True
"""


def binary_search_iterative(arr, target: int) -> bool:
    """
    Kodni bu yerda yozing.
    """

    while len(arr) != 1:
        mid = len(arr) // 2

        if arr[mid] == target:
            return True

        if target < arr[mid]:
            arr = arr[0:mid]

        elif target > arr[mid]:
            arr = arr[mid:]

    return arr[0] == target


# print(binary_search_iterative([1,4,5,2], 3))


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_leaves(root: TreeNode) -> int:
    # Kodni shu yerda yozing.

    stack = [root]
    counter = 0

    while len(stack) > 0:

        if root.right == None and root.left == None:
            counter = counter + 1

        if root.left != None:
            stack.append(root.left)
        if root.right != None:
            stack.append(root.right)

        root = stack.pop()

    return counter


print(count_leaves())


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root: TreeNode) -> None:
    # Kodni shu yerda yozing.
    q = deque([root])
    output = []
    while q:
        iters = len(q)
        output.append([])
        while iters:
            cur = q.popleft()
            output[-1].append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            iters -= 1

    for arr in output:
        for item in arr:
            print(item)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root: TreeNode) -> None:
    # Kodni shu yerda yozing.
    q = deque([root])
    output = []
    while q:
        iters = len(q)
        output.append([])
        while iters:

            cur = q.pop()

            output[-1].append(cur.val)

            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)

            iters -= 1

    for arr in output:
        for item in arr:
            print(item)
