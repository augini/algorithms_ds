const Firstpivot = (arr) => {
  let pivotPoint = 0;
  let temp;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[pivotPoint]) {
      if (pivotPoint + 1 === i) {
        temp = arr[i];
        arr[i] = arr[pivotPoint];
        arr[pivotPoint] = temp;
      } else {
        temp = arr[pivotPoint];
        arr[pivotPoint] = arr[pivotPoint + 1];
        arr[pivotPoint + 1] = temp;

        temp = arr[pivotPoint];
        arr[pivotPoint] = arr[i];
        arr[i] = temp;
      }

      pivotPoint = pivotPoint + 1;
    }
  }

  return pivotPoint;
};

// this is the optimized version of the first pivotHelper function
const findPivot = (arr, start = 0, end = arr.length - 1) => {
  let indexToSwap = start,
    temp;
  let pivot = start + 1;

  for (let i = start + 1; i <= end; i++) {
    if (arr[i] < arr[indexToSwap]) {
      temp = arr[pivot];
      arr[pivot] = arr[i];
      arr[i] = temp;

      pivot = pivot + 1;
    }
  }

  temp = arr[pivot - 1];
  arr[pivot - 1] = arr[indexToSwap];
  arr[indexToSwap] = temp;

  return pivot - 1;
};

const quickSort = (arr, start = 0, end = arr.length - 1) => {
  if (start >= end) {
    return arr;
  }
  let pivot = findPivot(arr, start, end);

  quickSort(arr, start, pivot - 1);
  quickSort(arr, pivot + 1, end);

  return arr;
};

console.log(quickSort([3, 4, 1, 2, 5, 32, 21, 23, 43, 12, 43, 56, 45, 1, 3]));
