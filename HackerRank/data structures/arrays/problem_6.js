// Array Manipulation
// LINK: https://www.hackerrank.com/challenges/crush/problem?h_r=next-challenge&h_v=zen

// SOLUTION:
/*
 * Complete the 'arrayManipulation' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

function arrayManipulation(n, queries) {
  // Write your code here
  let arr = new Arr(n).fill(0);

  for (let i = 0; i < queries.length; i++) {
    for (let x = queries[i][0] - 1; x < queries[i][1]; x++) {
      arr[x] = arr[x] + queries[i][2];
    }
  }

  return Math.max(...arr);
}

console.log(
  arrayManipulation(10, [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1],
  ])
);

// TAKEAWAY || APPROACH
