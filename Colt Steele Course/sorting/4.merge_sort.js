// merge two sorted arrays
const merge = (array_1, array_2) => {
  let pointer_1 = 0;
  let pointer_2 = 0;

  let result = [];

  for (let i = 0; i < array_1.length + array_2.length; i++) {
    if (array_1[pointer_1] <= array_2[pointer_2]) {
      result.push(array_1[pointer_1]);
      pointer_1 = pointer_1 + 1;
    } else {
      result.push(array_2[pointer_2]);
      pointer_2 = pointer_2 + 1;
    }

    if (pointer_1 === array_1.length) {
      result.push(...array_2.slice(pointer_2));
      break;
    } else if (pointer_2 === array_2.length) {
      result.push(...array_1.slice(pointer_1));
      break;
    }
  }

  return result;
};

const mergeSort = (input) => {
  if (input.length <= 1) return input;

  let mid = Math.floor(input.length / 2);
  let left = mergeSort(input.slice(0, mid));
  let right = mergeSort(input.slice(mid));
  return merge(left, right);
};

console.log(mergeSort([23421, 2123, 32, 3, 2, 3, 453, 5, 12, 1, 3, 89, 90]));
