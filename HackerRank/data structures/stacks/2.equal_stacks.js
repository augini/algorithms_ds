/*
 * Complete the 'equalStacks' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY h1
 *  2. INTEGER_ARRAY h2
 *  3. INTEGER_ARRAY h3
 */

function equalStacks(h1, h2, h3) {
  let sum1 = [];
  let sum2 = [];
  let sum3 = [];

  let maxHeight = 0;
  h1 = h1.reverse();
  h2 = h2.reverse();
  h3 = h3.reverse();

  for (let i = 0; h1.length; i++) {
    let temp = h1.reduce((pv, cv) => pv + cv, 0);
    sum1.push(temp);
    h1.pop();
  }

  for (let i = 0; h2.length; i++) {
    let temp = h2.reduce((pv, cv) => pv + cv, 0);
    sum2.push(temp);
    h2.pop();
  }

  for (let i = 0; h3.length; i++) {
    let temp = h3.reduce((pv, cv) => pv + cv, 0);
    sum3.push(temp);
    h3.pop();
  }

  sum1 = sum1.reverse();
  sum2 = sum2.reverse();
  sum3 = sum3.reverse();

  while (sum1.length && sum2.length && sum3.length) {
    let stack1Height = sum1[sum1.length - 1];
    let stack2Height = sum2[sum2.length - 1];
    let stack3Height = sum3[sum3.length - 1];

    // If all stacks are of same height, just return the height
    if (stack1Height == stack2Height && stack2Height == stack3Height) {
      maxHeight = sum1[sum1.length - 1];
      break;
    }

    // Else find the stack with maximum height and remove the block
    if (stack1Height >= stack2Height && stack1Height >= stack3Height) {
      sum1.pop();
    } else if (stack2Height >= stack1Height && stack2Height >= stack3Height) {
      sum2.pop();
    } else if (stack3Height >= stack1Height && stack3Height >= stack2Height) {
      sum3.pop();
    }
  }

  return maxHeight;
}

console.log(
  equalStacks(
    [1, 1, 4, 1, 1, 6, 7, 2, 1, 6, 2, 1],
    [3, 2, 6, 7, 1, 2, 1, 1, 2, 5, 1],
    [1, 3, 1, 6, 2, 1, 6, 7, 1, 2, 4, 8, 1]
  )
);
// console.log(equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]));

// Approach
// 1.
// 2.
