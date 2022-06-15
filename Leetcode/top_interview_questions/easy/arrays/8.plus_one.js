/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  if (digits[digits.length - 1] === 9) {
    let result = plusOne(digits.slice(0, digits.length - 1));
    result.push(0);
    return result;
  } else {
    let lastItem = digits[digits.length - 1];
    if (digits.length) {
      digits[digits.length - 1] = lastItem + 1;
      return digits;
    }
    return [1];
  }
};

console.log(plusOne([9, 9]));
