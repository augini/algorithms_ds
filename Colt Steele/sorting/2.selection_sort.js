// Similar to bubble sort, but instead of first placing large values into sorted position,
// it places small values into sorted position.

const selection_sort = (input) => {
  let min;

  for (let i = 0; i < input.length; i++) {
    min = i;

    for (let m = i; m < input.length; m++) {
      min = input[m] < input[min] ? m : min;
    }

    if (min !== i) {
      let temp = input[i];
      input[i] = input[min];
      input[min] = temp;
    }
  }

  return input;
};

console.log(selection_sort([4, 5, 2, 5, 6, 7, 1]));
