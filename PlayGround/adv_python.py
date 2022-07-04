# Collections module
# collections: Counter, namedtuple, OrderedDict, defaultDict, dequeue

from collections import Counter

names = ['john', 'michael', "mike", 'dunder', 'mike']
count = Counter(names)
print(count)

# we can get the most common element from counter as below:
print(count.most_common(1)) # [('mike', 2)]
print(count.most_common(1)[0][0]) # mike

#total() -> Compute the sum of the counts.
print(count.total())
