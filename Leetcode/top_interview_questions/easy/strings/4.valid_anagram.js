/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  let frequency1 = {};
  let frequency2 = {};

  if (s.length !== t.length) {
    return false;
  }

  for (let i = 0; i < s.length; i++) {
    frequency1[s[i]] = frequency1[s[i]] ? frequency1[s[i]] + 1 : 1;
  }

  for (let i = 0; i < t.length; i++) {
    frequency2[t[i]] = frequency2[t[i]] ? frequency2[t[i]] + 1 : 1;
  }

  for (let i in frequency1) {
    if (frequency2[i] !== frequency1[i]) {
      return false;
    }
  }

  return true;
};

console.log(isAnagram("a", "ab"));
