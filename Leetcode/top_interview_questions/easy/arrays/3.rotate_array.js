/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  let temp = [];

  for (let i = 0; i < nums.length; i++) {
    temp[(i + k) % nums.length] = nums[i];
  }

  for (let i = 0; i < nums.length; i++) {
    nums[i] = temp[i];
  }
};

console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
