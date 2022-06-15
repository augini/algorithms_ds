/**
 * @param {number[]} nums
 * @return {number}
 */

// This is the first approach that use extra space O(n)
var singleNumber = function (nums) {
  let temp = [];
  for (let i = 0; i < nums.length; i++) {
    if (!nums.slice(i + 1).includes(nums[i]) && !temp.includes(nums[i])) {
      return nums[i];
    }
    temp[i] = nums[i];
  }
};

// This is the approach based on XOR operation
var singleNumber = function (nums) {
  let temp = 0;
  for (let i = 0; i < nums.length; i++) {
    temp = temp ^ nums[i];
  }

  return temp;
};

console.log(singleNumber([2, 2, 1]));
