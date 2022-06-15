// flatten
// Write a recursive function called flatten which accepts an array of arrays
// and returns a new array with all values flattened.

const flatten = (arr) => {
  let result = [];

  const helper = (inArr) => {
    for (let i in inArr) {
      if (typeof inArr[i] === "object") {
        helper(inArr[i]);
      }
      if (typeof inArr[i] === "number") {
        result.push(inArr[i]);
      }
    }
  };

  helper(arr);
  return result;
};

console.log(flatten([1, 2, 3, [4, 5]])); // [1, 2, 3, 4, 5]
console.log(flatten([1, [2, [3, 4], [[5]]]])); // [1, 2, 3, 4, 5]
console.log(flatten([[1], [2], [3]])); // [1, 2, 3]
console.log(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])); // [1, 2, 3]
