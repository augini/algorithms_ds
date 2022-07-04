# Data Types

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
```
