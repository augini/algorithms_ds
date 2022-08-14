import math
import mmh3
from bitarray import bitarray



class BloomFilter(object):

    def __init__(self, items_count, fault):
        self.fault = fault
        self.size = self.get_size(items_count, fault)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = True

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                return False
        return True


    @classmethod
    def get_size(self, n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)


    @classmethod
    def get_hash_count(self, m, n):
        k = (m / n) * math.log(2)
        return int(k)




###############################################  TESTING !!!  #####################################################




from random import choice
import string
import time

def get_random_string(length):
    result_str = ''.join(choice(string.ascii_lowercase) for i in range(length))
    return result_str

# INPUTS
n = 700000 #n o of items to add
p = 0.1 # set false positive probability
r = 100000 # no of reads

start = time.time()
bloomf = BloomFilter(n,p)

faults = 0
yes = 0
no = 0

words_added = set()

for i in range(n):
    word = get_random_string(6)
    words_added.add(word)
    bloomf.add(word)        # (i%10) +5

for i in range(r):
    word = get_random_string(6)

    if bloomf.check(word):

        if word not in words_added:
            faults += 1
        else:
            yes += 1





# STATS
print("Size of bit array: {}".format(bloomf.size))
print("False positive Probability: {}".format(bloomf.fault))
print("Number of hash functions: {}\n".format(bloomf.hash_count))

print(f"'{faults}' FALSE POSITIVES")
print(f"'{yes}' PRESENT")
print(f"'{r-yes-faults}' NOT PRESENT\n")
end = time.time()
print(f"{math.ceil(end - start)} sec. Script run time")