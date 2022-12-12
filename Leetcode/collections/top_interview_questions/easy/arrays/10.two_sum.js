/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// BigO(n2)
// var twoSum = function (nums, target) {
//   for (let i = 0; i < nums.length; i++) {
//     for (let n = 1; n < nums.length; n++) {
//       if (nums[i] + nums[n] === target && i !== n) {
//         return [i, n];
//       }
//     }
//   }

//   return null;
// };

// BigO(n)
var twoSum = function (nums, target) {
  let container = {};
  let toTarget;

  for (let i = 0; i <= nums.length; i++) {
    toTarget = target - nums[i];
    if (container.hasOwnProperty(toTarget)) {
      return [container[toTarget], i];
    }
    container[nums[i]] = i;
  }
};

console.log(twoSum([2, 7, 11, 5], 9));
