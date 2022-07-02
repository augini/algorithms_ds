# Data Types

- Each collection data type has `.count` method to count the number of occurrances for each element
- Each collection data type also supports **unpacking**

         unpack_list = [23, "username", "password", False]

         age, name, passwd, boolean = unpack_list

         print(age, boolean) # 23, False

  We can also use rest operator denoted by `*` to pack multiple variables into a single variable

         unpack_list = [23, "username", "password", False]

         first, *rest = unpack_list

## Lists

- We can create a list with a certain length of same elements
  `list = [0] \* 10`

- To slice the list with steps
  `step_list = cool_list[::4]`

- To copy one list into another
  If we use `old_list = new_list syntax`, they basically refer to the same place in memory

  Meaning, if we change the new list, the old one also be changed

  To avoid this, we can use the below syntax

      old_list = [1,34,5,23,4]

      # 1
      new_list = old_list.copy()

      # 2
      new_list = list(old_list)

      # 3
      new_list = old_list[:]

- **List comprehension**

      original_list = [34,213,43,4,345,45,4]

      new_list = [i*12 for i in original_list]

      print(new_list)

## Tuples

- We can leave parantheses away when creating tuples

      _tuple = (12, "string", "tuple", False)

      _tuple = 12, "string", "tuple", False

      print(type(_tuple)) # <class 'tuple'>

- If we have only one element inside a parantheses, it will not be a tuple data type

      _tuple = (12)

      print(type(_tuple)) # <class 'int'>

  To counter this, add a comma

      _tuple = (12,)

      print(type(_tuple)) # <class 'tuple'>

- Since tuple data type is immutable, Python makes internal optimizations to make working with this data type easier

  To illustrate this point

      import sys

      _list  = [1,3,4,True,'string','username']
      _tuple = [23,12,'he_there',False,'boolean']

      print(sys.getsizeof(_list))
      print(sys.getsizeof(_tuple))

  We get 152 bytes for list and 120 bytes for tuple

  Keep in mind that working with tuples can be much more efficient
