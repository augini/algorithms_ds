// A sorting algorithm where the largest values bubble up to the top.

const bubble_sort = (input, type) => {
  let noSwaps;
  // one loop for steppting from the end of the array
  for (let i = input.length; i >= 0; i--) {
    // x loops the array and swaps values
    // if one is larger than another
    noSwaps = true;
    for (let x = 0; x <= i - 1; x++) {
      let condition =
        type === "asc" ? input[x] < input[x + 1] : input[x] > input[x + 1];

      if (condition) {
        let temp = input[x];
        input[x] = input[x + 1];
        input[x + 1] = temp;
        noSwaps = false;
      }
    }

    if (noSwaps) break;
  }

  return input;
};

console.log(bubble_sort([23, 12, 43, 4, 123, 3, 1, 43, 56, 68, 1, 32], "asc"));
// console.log(bubble_sort([5, 4, 3, 1]));
