// Builds up the sort by gradually creating a larger left half which is always sorted

const insertion_sort = (input) => {
  for (let i = 1; i < input.length; i++) {
    for (let m = i; m >= 0; m--) {
      if (input[m - 1] > input[m]) {
        let temp = input[m - 1];
        input[m - 1] = input[m];
        input[m] = temp;
      }
    }
  }

  return input;
};

console.log(insertion_sort([2, 1, 9, 76, 4]));
// [12, 34, 4, 1, 45, 32, 19, 223]
// [12, 4, 34, 1, 45, 32, 19, 223]
