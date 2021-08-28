// Given a string, write a function to check if it is a permutation of a palindrome

// lleev -> [level] -> true
// hnnaha -> [hannah] -> true

const isPalindromePermutation = (input) => {
  if (!input) {
    return null;
  }

  let instanceCount = {};

  for (let i = 0; i < input.length; i++) {
    let item = instanceCount[input[i].toLowerCase()];
    instanceCount[input[i].toLowerCase()] = item ? item + 1 : 1;
  }

  let oddInstanceCount = 0;

  for (let i in instanceCount) {
    if (instanceCount[i] % 2) {
      oddInstanceCount = oddInstanceCount + 1;
    }
  }

  return input.length % 2 ? oddInstanceCount === 1 : oddInstanceCount === 0;
};

console.log(isPalindromePermutation("Level"));
