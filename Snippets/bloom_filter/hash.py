from bitarray import bitarray

arr = bitarray(20)
# arr.setall(0)
# arr.append(False)
# arr.append(True)
# arr.append(False)
# arr.append(1)
# print(arr)

def hash_djb2(s):                                                                                                                            
    hash = 5381
    for x in s:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF

print(hex(hash_djb2(u'hex(hash_djb2(uhello world, 世界)) o world, 世界'))) # '0xa6bd702fL'