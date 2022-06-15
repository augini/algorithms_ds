/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function (x, y) {
  let XOR = x ^ y;

  let count = 0;
  while (XOR) {
    count += XOR & 1;
    XOR >>= 1;
  }
  return count;
};

console.log(hammingDistance(93, 73));
