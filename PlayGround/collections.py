from collections import namedtuple

collection = (10, 12,32,34,34)
print(collection[1])

fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
print(guava.count)