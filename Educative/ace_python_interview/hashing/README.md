# Hashing: hash table and hash map

- **Hashing**: a process of converting a key to a fixed size value
- **Hash**: the code produced by hashing

## Hash table

- A data structure that stores key/value pairs in a table of spots, it uses hashing to calculate the index where an element should be located, we use it when we have keys and values that are associated to them, for example a phone agenda or dictionary

One of the properties needed to create a hash table is a hash function.

- **Hash function**: A deterministic function that is used in hashing. It takes input as a key and calculates its hash. A good function is a hash function that respects some important properties such as:

  - Distributing keys as evenly as possible across the different hash values
  - Being computationally efficient in having a good performance overall when using our hash table

## Collision

Collision is when two different values result in the same hash. This happens because the possible keys for a hash table are indefinite whereas the size of the array needed to store those values in most cases is limited.
There are different ways to handle collisions that include algorithms such as **separate chaining**, **open addressing**.

- Separeate chaining is a collision handling technique that works by storing pairs with the same value in a linked list at the spot, each node contains a key/value pair. The best time complexity for a hash table using this collision handling is constant and the worst time complexity is O(n) where all the keys are stored in a single index.
- Open addressing is another technique that works by searching for an alternative spot if the actual one is occupied. The limitation of this technique is that it can only have the number of keys as the size of the array since a single spot can only contain a single value

There is also a concept called **perfect hashing** which means to have a hash table with no collisions.

No matter how efficient the collision handling techniques are, if we keep inserting keys to the hash table, we will reach a point where its array size is met or if using a separate chaining algorith, it starts to loose the constant retrieval property of hash table. So come a technique called **rehashing** which means to move the existing keys in the array to a new array with a larger size.

When to apply rehashing is determined by **load factor** which is a value calculated by n / m. (n=keys in the array, m=array size).
