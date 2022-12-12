/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let result = "";

  let counter = 0;
  for (let n = 0; n < strs[0].length; n++) {
    counter = 0;
    for (let i = 1; i < strs.length; i++) {
      if (strs[0][n] === strs[i][n]) {
        counter = counter + 1;
      }
    }

    if (counter === strs.length - 1) {
      result = result + strs[0][n];
    } else {
      break;
    }
  }

  return result.length ? result : "";
};

console.log(longestCommonPrefix(["a"]));
