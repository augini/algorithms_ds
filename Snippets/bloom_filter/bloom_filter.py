import math
import random
import string
from bitarray import bitarray

WRITE_SIZE = 700000
READ_SIZE = 100000

class BloomFilter(object):
   
   def __init__(self, size, num_exp_elements=100000):
      self.size = size
      self.num_exp_elements = num_exp_elements
      
      self.bloom_filter = bitarray(self.size)
      self.bloom_filter.setall(0)
      
      self.num_hash_functions = 4

   def _hash_djb2(self, s):
      hash = 5381
      for x in s:
         hash = ((hash << 5) + hash) + ord(x)
      return hash % self.size
   
   def _hash(self, item, K):
        return self._hash_djb2(str(K) + item)

   def add_to_filter(self, item):
        for i in range(self.num_hash_functions):
            self.bloom_filter[self._hash(item, i)] = 1
            
   def check_is_not_in_filter(self, item):
        for i in range(self.num_hash_functions):
            if self.bloom_filter[self._hash(item, i)] == 0:
                return True
        return False
     
   def gen_random_string(self, max_length):
      len = int((random.random() * 100)) % (max_length - 1) + 1
      random_list=[]
      for i in range(len):
         random_list.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + "_"))
      return ''.join(random_list)



# --------------------------------------------
bloom_filter = BloomFilter(10000000, READ_SIZE)
existing = set()
false_positives = 0

# writes
for i in range(WRITE_SIZE):
   username = bloom_filter.gen_random_string(15)
   existing.add(username)
   bloom_filter.add_to_filter(username)
      
# reads
taken = 0
for i in range(1, READ_SIZE):
    username = bloom_filter.gen_random_string(15)
    if not bloom_filter.check_is_not_in_filter(username):
       if username not in existing:
          false_positives+=1
       else:
          taken+=1
          
print(f"False Positives: {false_positives}")
print(f"Names Taken: {taken}")
print(f"Names Not Taken: {READ_SIZE - taken - false_positives}")