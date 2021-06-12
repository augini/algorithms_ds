console.log("Hacker rank dynamic array problem");

// Hacker rank dynamic link problem
// Link: https://www.hackerrank.com/challenges/dynamic-array/problem

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

// Solution
function dynamicArray(n, queries) {
  // Write your code here
  let lastAnswer = 0;
  let arr = [];
  let answers = [];
  for (let i = 0; i < n; i++) {
    arr[i] = [];
  }

  for (let i = 0; i < queries.length; i++) {
    let numbersArray = queries[i];
    if (numbersArray[0] === 1) {
      let x = (numbersArray[1] ^ lastAnswer) % n;
      arr[x].push(numbersArray[2]);
    } else if (numbersArray[0] === 2) {
      let x = (numbersArray[1] ^ lastAnswer) % n;
      lastAnswer = arr[x][numbersArray[2] % arr[x].length];
      answers.push(lastAnswer);
    }
  }
}

dynamicArray(2, [
  [1, 0, 5],
  [1, 1, 7],
  [1, 0, 3],
  [2, 1, 0],
  [2, 1, 1],
]);

// The problem shows how to work with dynamic arrays
// The problem covers simple loops. nothing special
// Understanding the problem was little hard but once I understoo the problem, the solution was simple and easy
