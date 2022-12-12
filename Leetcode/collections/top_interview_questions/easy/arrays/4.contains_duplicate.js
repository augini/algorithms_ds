/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let temp = [];

  for (let i = 0; i < nums.length; i++) {
    if (temp.includes(nums[i])) {
      return true;
    }
    temp[i] = nums[i];
  }
  return false;
};

console.log(containsDuplicate([1, 2, 3, 4, 1, 5, 6]));
