# Sets
# Set is an unordered, mutable and no duplicates

# We can remove values from the set in the following ways:
myset = set([23, 12, 4, "hey", True, 34])

# removes the given element, raises a key error if non-existant key is passed
myset.remove(23)

# removes the given element, does not raise an error if key does not exist
myset.discard(13)

# clears the set
# myset.clear()

# pops an arbitrary value and returns it
while len(myset) > 0:
   item = myset.pop()
   # print(item)
   
# we can also get an intersection, union, difference of sets.
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

# there is also an immutable version of set called `frozenset`
a = frozenset([1,2,3,4])
a.add(12) # 'frozenset' object has no attribute 'add'