# Collection Data Types

- Each collection data type has `.count` method to count the number of occurrances for each element
- Each collection data type also supports **unpacking**

```python
unpack_list = [23, "username", "password", False]

age, name, passwd, boolean = unpack_list

print(age, boolean) # 23, False
```

We can also use rest operator denoted by `*` to unpack multiple variables into a single variable

```python
unpack_list = [23, "username", "password", False]

first, *rest = unpack_list
```

## Lists

- We can create a list with a certain length of same elements
  `list = [0] \* 10`

- To slice the list with steps
  `step_list = cool_list[::4]`

- If we use `old_list = new_list syntax`
  to copy one list into another, they basically refer to the same place in memory

  Meaning, if we change the new list, the old one also be changed

  To avoid this, we can use one of the below options

```python
old_list = [1,34,5,23,4]

# 1
new_list = old_list.copy()

# 2
new_list = list(old_list)

# 3
new_list = old_list[:]
```

- **List comprehension**

```python
original_list = [34,213,43,4,345,45,4]

new_list = [i*12 for i in original_list]

print(new_list)
```

## Tuples

> Tuple is an immutable data structure that can contain elements of any data type

- We can leave parantheses away when creating tuples

```python
_tuple = (12, "string", "tuple", False)

_tuple = 12, "string", "tuple", False

print(type(_tuple)) # <class 'tuple'>
```

- If we have only one element inside `()`, it will not considered a tuple data type

```python
_tuple = (12)

print(type(_tuple)) # <class 'int'>
```

To counter this, add a comma

```python
_tuple = (12,)

print(type(\_tuple)) # <class 'tuple'>
```

- Since tuple data type is immutable, Python makes internal optimizations to make working with this data type easier

  To illustrate this point

```python
import sys

_list = [1,3,4,True,'string','username']
_tuple = [23,12,'he_there',False,'boolean']

print(sys.getsizeof(_list))
print(sys.getsizeof(_tuple))
```

We get 152 bytes for list and 120 bytes for tuple

Keep in mind that working with tuples can be much more efficient than working with lists

## Dictionaries

> Dictionary is a data structure that is **undered** and **mutable**

- To remove a property from a dictionary, we can use one of the options below

```python
user_ages = {"john":10,"michael":30, "mike":35}

#1
del user_ages["mike"]

#2
user_ages.pop("mike")

#3 -> removes the element that was added last
user_ages.popitem()
```

- To make a deep copy of a dictionary, use one of the options below

```python
old_dict = { "name": "username", "age": 23}

# 1
new_dict = old_dict.copy()

# 2
new_dict = dict(old_dict)
```

- We can also merge two dictionaries as such below:

  In this merge, existing keys will get overwritten and non existing keys will get added

```python
dict_1={ "name": "username", "age": 23}

dict_2 = {"city":"This city", "state":"AL"}

dict_1.update(dict_2)
```

- We can also use tuples as dictionary keys

```python
_tuple = (7, 8)

_dict = {_tuple:15}
```

## Sets

> Set is a data structure that is **unordered**, **mutable** and has **no duplicates**

- We can initialize a set in of the following ways

```python
_set = {1, 3,4,5}

_set = set([2,3,4,5])

_set = set("Hello")
```

- Can't create an empty set with `{}`, it will be regarded as dictionary

  Instead use `set()`

```python
empty_set = set()
```

- We can remove values from the set in the following ways:

```python

myset = set([23, 12, 4, "hey", True, 34])

# removes the given element, raises a key error if non-existant key is passed
myset.remove(23)

# removes the given element, does not raise an error if key does not exist
myset.discard(13)

# clears the set
myset.clear()

# pops an arbitrary value and returns it
while len(myset) > 0:
   item = myset.pop()
   # print(item)

```

- We can also get an intersection, union, difference of sets in the following ways:

```python
odd   = {1, 3, 5, 7, 9}
even  = {2, 4, 6, 8}
prime = {3, 5, 7}

# union returns unique elements from both sets
union = odd.union(even)
print(union) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection returns elements that exist in both sets
intersection = odd.intersection(even)
print(intersection) # set()

# difference returns the elements that exist only in the first set
diff = odd.difference(even)
print(diff) # {1, 3, 5, 7, 9}

# there is also symmetric difference that returns elements that exist only in any of the sets
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

print(setA.symmetric_difference(setB)) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

```

- We can create an immutable version of set called `frozenset`

```python
a = frozenset([1,2,3,4])

a.add(12) # 'frozenset' object has no attribute 'add'
```

## Collections module

- Collections: Counter, namedtuple, OrderedDict, defaultDict, dequeue

```python
from collections import Counter

names = ['john', 'michael', "mike", 'dunder', 'mike']
count = Counter(names)
print(count)

# we can get the most common element from counter as below:
print(count.most_common(1)) # [('mike', 2)]
print(count.most_common(1)[0][0]) # mike

#total() -> Compute the sum of the counts.
print(count.total())
```

- We have named tuples in collections module that enable to access tuple data types with names

```python
from collections import namedtuple

Point = namedtuple("Point","x,y")

pt = Point(x=4,y=5)

print(pt.x, pt.y)

print(pt[0], pt[1])
```

- OrderedDict

> OrderedDict has been less important now since built in dictionaries also rememember the order of insertion since Python 3.7

- defaultdict - It will have the defualt value for the key if it has not been set yet
- We will get a keyError if we try to access a key that does not exist in a normal dictionary, with default dict we get the default value

```python
from collections import defaultdict

d = defaultdict(int)

d['a'] = 1
d['b'] = 2

print(d['c']) # 0

d = defaultdict(float)

d['a'] = 1

print(d['c']) # 0.0
```

- deque - deque is a double ended queue and can be used to add or remove elements from both sides of the list

```python
from collections import deque
d = deque()

d.append(1)
d.append(4)

d.appendleft(12)

d.pop()
d.popleft()

d.rotate(1)
d.rotate(-1)

print(d)
```
