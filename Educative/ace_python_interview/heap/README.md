# Heap

Heaps are advanced data structures that are useful in applications such as sorting and implementing priority queues. They are regular binary trees with two special properties

- Heaps must be Complete Binary Trees
- The Heap Order Property

## Where are Heaps Used?

The primary purpose of heaps is to return the smallest or largest element. This is because the time complexity of getting the minimum/maximum value from a min/max heap is O(1), i.e., constant time complexity. This way, algorithms that require retrieving the maximum/minimum value can be optimized. Heaps are also used to design Priority Queues. Some of the famous algorithms which are implemented using Heaps are Prim’s Algorithm, Dijkstra’s algorithm and the famous Heap Sort algorithm which is entirely based on the Heap data structure.

## Heap Representation in Lists

Heaps can be implemented using arrays or lists in Python. The node values are stored such that all the parent nodes occur in the first half of the list (where 0 ≤ i ≤ ⌊(n-1)/2⌋, where n is the last index) and the leaves exist in the rest. So the last parent will be at the ⌊(n-1)/2⌋ index. The left child of the node at the kth index will be at the 2k+1 index, and the right child will be at 2k+2. To put it simply, the index of each node is how much you'd count if you started from 0 at the root and went left to right level-wise in a tree.
