/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  let validItems = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
  let result = "";

  // remove the trailing space
  s = s.trim();

  // isPositive determines if the result will be negative
  // based on first character in the string
  let isPositive = s[0] === "-" ? false : true;

  if (s[0] === "+" || s[0] === "-") {
    s = s.slice(1);
  }

  for (let i = 0; i < s.length; i++) {
    if (validItems.indexOf(s[i]) !== -1) {
      result = result + s[i];
      continue;
    }
    break;
  }

  if (result >= 0x80000000 || result <= -0x80000000) {
    return isPositive ? parseInt(0x7fffffff) : -parseInt(0x80000000);
  }

  if (result.length === 0) {
    result = 0;
  }

  return isPositive ? parseInt(result) : -parseInt(result);
};

console.log(myAtoi("      -11919730356x"));
