/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  let indices = [];

  if (needle === "") {
    return 0;
  }

  if (needle.length > haystack.length) {
    return -1;
  }

  let frequency1 = {},
    frequency2 = {};

  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) indices.push(i);
    frequency1[haystack[i]] = frequency1[haystack[i]]
      ? frequency1[haystack[i]] + 1
      : 1;
  }

  for (let i = 0; i < needle.length; i++) {
    frequency2[needle[i]] = frequency2[needle[i]]
      ? frequency2[needle[i]] + 1
      : 1;
  }

  for (let i in frequency1) {
    if (frequency1[i] < frequency2[i]) {
      return -1;
    }
  }

  let c = 0;
  while (c < indices.length) {
    if (haystack.slice(indices[c], indices[c] + needle.length) === needle) {
      return indices[c];
    }
    c = c + 1;
  }

  return -1;
};

console.log(strStr("", ""));
