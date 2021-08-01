/*
 * Complete the 'isBalanced' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function isBalanced(s) {
  let stack = [];
  let bracketPairs = {
    "(": ")",
    "[": "]",
    "{": "}",
  };

  for (let i = 0; i < s.length; i++) {
    if (bracketPairs[stack[stack.length - 1]] === s[i]) {
      stack.pop();
      continue;
    }
    stack.push(s[i]);
  }

  return stack.length ? "NO" : "YES";
}

isBalanced("{[(])}");
