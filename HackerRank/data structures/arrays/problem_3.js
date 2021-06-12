// Array Left Rotation
// LINK: https://www.hackerrank.com/challenges/array-left-rotation/problem?h_r=next-challenge&h_v=zen

// SOLUTION:
/*
 * Complete the 'rotateLeft' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */

function rotateLeft(d, arr) {
  return [...arr.slice(d, arr.length), ...arr.slice(0, d)];
}

console.log(rotateLeft(2, [1, 2, 3, 4, 5]));

// TAKEAWAY || APPROACH
// To rotate array to the left, slice it from the number of rotations and move first half to the last
