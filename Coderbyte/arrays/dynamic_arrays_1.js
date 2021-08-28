console.log("going to solve a greedy algorithmic problem");

// Given an array (arr) of integers, return an array (products) such that products[i] is equal to the product of all the elements of arr except arr[i].
// Solve without the division operator in O(n) time.

// [1,2,3,4] -> [24, 12, 8, 6]
const returnProductsArray = (input) => {
  if (!input) {
    return null;
  }

  let products = [];

  let temp = 1;
  for (let i = 0; i < input.length; i++) {
    temp = i === 0 ? 1 : temp * input[i - 1];
    products[i] = temp;
  }

  temp = 1;
  for (let i = input.length - 1; i >= 0; i--) {
    temp = i === input.length - 1 ? temp : temp * input[i + 1];
    products[i] = products[i] * temp;
  }

  return products;
};

console.log(returnProductsArray([0, 1, 2, 4]));
