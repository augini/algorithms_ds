/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  let frequency = {};

  for (let i = 0; i < s.length; i++) {
    frequency[s[i]] = frequency[s[i]] ? frequency[s[i]] + 1 : 1;
  }

  for (let i in frequency) {
    if (frequency[i] === 1) {
      return s.indexOf(i);
    }
  }
  return -1;
};

console.log(firstUniqChar("loveleetcode"));
