# Notes from Educative's Ace Python Interview Module

## Big O Notation

<details>
<summary>Common Complexity Scenarios</summary>

This lesson summarizes our discussion of complexity measures and includes some commonly used examples and handy formulas to help you with your interview.

### **Simple for-loop**

```python
for x in range(n):
    # statement(s) that take constant time
```

`Running Time Complexity = n = O(n)`

Explanation: Python’s range(n) function returns an array that contains integers from 0 till n-1 ([0, 1, 2, …, n-1]). The in means that x is set equal to the numbers in this array at each iteration of the loop sequentially. So n is first 0, then 1, then 2, …, then n-1. This means the loop runs a total of n times, hence the running time complexity is n.

### **For-loop with Increments**

```python
for x in range(1, n, k):
    # statement(s) that take constant time
```

`Running Time Complexity = floor(n/k) = O(n)`

### **Simple Nested For-loop**

```python
for i in range(n):
    for x in range(m):
        # Statement(s) that take(s) constant time
```

`Running Time Complexity = n*m = O(nm)`

Explanation: The inner loop is a simple for loop that takes m time and the outer loop runs it n times. In other words, the outer loop runs n times and the inner loop runs m times at each iteration of the outer loop. So that makes it so that it takes n \times m n×m time in total.

### **Nested For-loop with Dependant Variables**

```python
for i in range(n):
    for x in range(i):
        # Statement(s) that take(s) constant time
```

`Running Time Complexity = (n-1)((n-1)+1)/2 = O(n^2)`

Explanation: The outer loop runs n times and for each time the outer loop runs, the inner loop runs i times. So, the statements in the inner loop do not run at the first iteration of the outer loop since i is 0 then; they run once at the second iteration of the outer loop since i is equal to 1 at that point, then they run twice, then thrice, until i is n-1.

### **Nested For-loop with Index Modification**

```python
for i in range(n):
    i *= 2
    for x in range(i):
        # Statement(s) that take(s) constant time
```

`Running Time Complexity = (n)(n-1) = n^2-n = O(n^2)`

### **Loops with log(n) time complexity**

```python

i = #constant
n = #constant
k = #constant

while i < n:
    i*=k
    # Statement(s) that take(s) constant time
```

`Running Time Complexity = log_k(n) = O(log_k(n))`

Explanation: A loop statement that multiplies/divides the loop variable by a constant such as the above takes log(k) of n time because the loop runs that many times. Let’s consider an example where i = 1, n = 16, and k = 2:

| i   | Count |
| --- | ----- |
| 1   | 1     |
| 2   | 2     |
| 4   | 3     |
| 8   | 4     |
| 16  | -     |

log_k(n) = log_2(16) = 4

</details>
