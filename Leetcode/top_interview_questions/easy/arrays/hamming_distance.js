// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/

/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function (x, y) {
  // first approach

  // let count = 0;
  // let xor = (x ^ y).toString(2);
  // for (let i = 0; i < xor.length; i++) {
  //     if (xor[i]==="1"){
  //         count++;
  //     }
  // }
  // return count;

  // second approach

  let xor = x ^ y;
  let count = 0;
  while (xor !== 0) {
    count += xor & 1;
    xor = xor >> 1;
  }
  return count;

  // third approach
  // loop through the bits of x and y at the same time.
};

hammingDistance(1, 4);
