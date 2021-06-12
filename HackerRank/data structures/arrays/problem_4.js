// Sparse Arrays
// LINK: https://www.hackerrank.com/challenges/sparse-arrays/problem

// SOLUTION:
/*
 * Complete the 'matchingStrings' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY strings
 *  2. STRING_ARRAY queries
 */

function matchingStrings(strings, queries) {
  // Write your code here
  let answers = [];

  queries.forEach((query) => {
    let a = 0;
    strings.forEach((string) => {
      if (string === query) a++;
    });

    answers.push(a);
  });

  return answers;
}

console.log(matchingStrings(["ab'", "ab'", "abc'"], ["ab'", "abc'", "bc'"]));

// TAKEAWAY || APPROACH
//d
