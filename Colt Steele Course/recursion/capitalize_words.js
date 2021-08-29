// capitalizeWords
// Write a recursive function called capitalizeWords.
// Given an array of words, return a new array containing each word capitalized.

const capitilizeWords = (input) => {
  if (input.length) {
    let lastItem = input[input.length - 1];
    lastItem = lastItem.toUpperCase();
    input = capitilizeWords(input.slice(0, input.length - 1));
    input.push(lastItem);
    return input;
  }
  return input;
};

console.log(
  capitilizeWords(["hello", "welcome", "good", "doinggreat", "comeaboard"])
);
