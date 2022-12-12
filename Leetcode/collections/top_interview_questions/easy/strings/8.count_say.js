/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function (n) {
  if (n === 1) {
    return "1";
  }

  return countAndSay(n - 1) + n.toString();
};

console.log(countAndSay(3));
