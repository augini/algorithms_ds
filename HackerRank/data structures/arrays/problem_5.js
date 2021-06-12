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
  let arr = new Array(n).fill(0);
  let sum = 0;
  let max = 0;

  for (let i = 0; i < queries.length; i++) {
    let a = queries[i][0];
    let b = queries[i][1];
    let k = queries[i][2];

    arr[a] += k;
    arr[b + 1] -= k;
  }

  for (let i = 0; i <= arr.length; i++) {
    sum += arr[i];
    max = sum > max ? sum : max;
  }

  return max;
}

console.log(
  arrayManipulation(10, [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1],
  ])
);

// TAKEAWAY || APPROACH
