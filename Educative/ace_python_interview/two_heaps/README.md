# Overview

As the name suggests, the two heaps pattern uses either two min-heaps, two max-heaps, or a min-heap and a max-heap simultaneously to solve the problem.

Insertion - O(logn)
Removing - O(logn)
Access - O(1)

In some problems, we’re given a set of data such that it can be divided into two parts. We can either use the first part to find the smallest element using the min-heap and the second part to find the largest element using the max-heap, or we can do the reverse and use the first part to find the largest element using the max-heap and the second part to find the smallest element using the min-heap.

## Does my problem match this pattern?#

Yes, if both of these conditions are fulfilled:

- We need to repeatedly calculate two maxima, two minima, or one maximum and one minimum, based on a changing set of data.
- The input data is not sorted.

No, if any of these conditions are fulfilled:

- We don’t need to track two extreme values (minima or maxima), but only one.
- When we don’t need to repeatedly calculate the extreme values (minima or maxima), but only need to calculate it a fixed number of times.
- The input data is already sorted—in which case, there is no benefit to using heaps.

# Real-world problems#

- Video streaming:

  During a user session, there is often a possibility that packet drops and buffering might occur. We want to record the median number of buffering events that might occur in a particular session, which could then be used to improve the user experience.

- Netflix:

  As part of a demographic study, we’re interested in the median age of our viewers. We want to implement a functionality whereby the median age can be updated efficiently whenever a new user signs up for video streaming.

# Problems

## Find Median from a Data Stream

Implement a data structure that’ll store a dynamically growing list of integers and provide access to their median in O(1).

## Naive approach

- The naive solution is to first sort the data and then find the median. Insertion sort is an algorithm that can be used to sort the data as it appears. This way, every time a new number is added to the stream, the numbers before that new number are already sorted, allowing insertion at the correct index. This, however, also requires us to shift the elements greater than the inserted number one place forward.

- The overall time complexity of the algorithm becomes O(n2), where n is the number of elements in the data stream.
- The time complexity of the function that calculates median would be O(1)
- The space complexity is O(1)

## Step by step approach

- Split incoming numbers into two lists - small and large. Those that are smaller than the current middle element are small and those that are large than it are large

- Maintain these lists as heaps so that the root of the small heap is the largest element in it and the root of large heap is the smallest element in it.

- If the number of elements is even, the median is the mean of the root of the two heaps. Else, it’s the root of the small heap.

- If the size of the large heap is greater than the size of small heap or, if size of small heap is greater than the size of the large heap + 1, rebalance the heaps.
