/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const sign = x < 0;
  let temp = Math.abs(x);
  let reverseN = 0;

  while (temp) {
    reverseN = reverseN * 10 + (temp % 10);
    temp = Math.floor(temp / 10);
  }

  return reverseN > 0x7fffffff ? 0 : sign ? -reverseN : reverseN;
};

console.log(reverse(-123));
