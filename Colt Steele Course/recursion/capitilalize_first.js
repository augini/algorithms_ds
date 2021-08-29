// capitalizeFirst
// Write a recursive function called capitalizeFirst.
// Given an array of strings, capitalize the first letter of each string in the array.

const capitilizeFirst = (input) => {
  if (input.length) {
    let lastItem = input[input.length - 1];
    lastItem = lastItem.charAt(0).toUpperCase() + lastItem.slice(1);

    input = capitilizeFirst(input.slice(0, input.length - 1));

    input.push(lastItem);
    return input;
  }
  return input;
};

console.log(
  capitilizeFirst(["hello", "welcome", "good", "doinggreat", "comeaboard"])
);
