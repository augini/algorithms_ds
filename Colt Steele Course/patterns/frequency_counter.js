// Problem 1
// Find if the square of the numbers exist in the second array
const same = (a, b) => {
  if (a.length !== b.length) {
    return false;
  }
  let temp = {};

  for (let i = 0; i < a.length; i++) {
    if (temp.hasOwnProperty(a[i])) {
      temp[a[i]] = temp[a[i]] + 1;
    } else {
      temp[a[i]] = 1;
    }
  }

  for (let i = 0; i < b.length; i++) {
    let squareRoot = Math.sqrt(b[i]);

    if (temp.hasOwnProperty(squareRoot)) {
      temp[squareRoot] = temp[squareRoot] - 1;
    }
  }

  let counts = Object.values(temp);

  return counts.every((i) => i === 0);
};

// Colt Steele version
// function same(arr1, arr2) {
//   if (arr1.length !== arr2.length) {
//     return false;
//   }
//   let frequencyCounter1 = {};
//   let frequencyCounter2 = {};
//   for (let val of arr1) {
//     frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1;
//   }
//   for (let val of arr2) {
//     frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1;
//   }
//   console.log(frequencyCounter1);
//   console.log(frequencyCounter2);
//   for (let key in frequencyCounter1) {
//     if (!(key ** 2 in frequencyCounter2)) {
//       return false;
//     }
//     if (frequencyCounter2[key ** 2] !== frequencyCounter1[key]) {
//       return false;
//     }
//   }
//   return true;
// }

// Problem 2
// Anagrams
// Given two strings, write a function to determine if the second string is
// the anogram of the first string
// An anagram a word, phrase or name formed by rearranging the letters of another such as cinema formed by rearranging iceman

// I am going to solve this problem using Frequency Counter approach

const validAnagram = (a, b) => {
  if (a.length !== b.length) {
    return false;
  }

  let counter1 = {};
  let counter2 = {};

  for (let val of a) {
    counter1[val] = (counter1[val] || 0) + 1;
  }

  for (let val of b) {
    counter2[val] = (counter2[val] || 0) + 1;
  }
  console.log(counter1);
  console.log(counter2);
  for (let key1 in counter1) {
    if (!counter2[key1]) {
      return false;
    }
  }

  return true;
};

console.log(validAnagram("azeaf", "fzeaa"));
