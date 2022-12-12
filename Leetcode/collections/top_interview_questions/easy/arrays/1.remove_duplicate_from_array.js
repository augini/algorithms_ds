const removeDuplicates = function (nums) {
  console.log(typeof nums);

  let counter = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i + 1]) {
      nums = [...nums.slice(0, i), ...nums.slice(i + 1)];
      i = i - 1;
      continue;
    }
    counter++;
  }

  return counter;
};

console.log(removeDuplicates([1, 1, 2]));
