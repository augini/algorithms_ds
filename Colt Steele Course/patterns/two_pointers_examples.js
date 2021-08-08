// Problem 1
// Write a function called sumZero that accepts a sorted array of integers and returns the pairs that sum equals 0;

const sumZero = (arr) => {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    let sum = arr[left] + arr[right];

    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum > 0) {
      right--;
    } else if (sum < 0) {
      left++;
    }
  }
};

// Problem 2
// Implement a function called count unique values that accepts a sorted array and counts the unique values in the array
// There can be negative values in the array but it will always be sorted

const countUniqueValues = (arr) => {
  let first = arr[0];
  let counter = 1;

  if (arr.length === 0) return 0;
  for (let i = 1; i < arr.length; i++) {
    if (first !== arr[i]) {
      counter++;
      first = arr[i];
    }
  }

  return counter;
};

// Colt Steele solution
function countUniqueValues(arr) {
  if (arr.length === 0) return 0;
  var i = 0;
  for (var j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j];
    }
  }
  return i + 1;
}

console.log(countUniqueValues([-2, -1, -1, 0, 1]));
