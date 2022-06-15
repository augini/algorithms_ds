// collectStrings
// Write a function called collectStrings which accepts an object and
// returns an array of all the values in the object that have a typeof string.

const collectStrings = (input) => {
  let result = [];
  const helper = (data) => {
    for (let i in data) {
      if (typeof data[i] === "object") {
        helper(data[i]);
      }
      if (typeof data[i] === "string") {
        result.push(data[i]);
      }
    }
  };

  helper(input);

  return result;
};

const obj = {
  stuff: "foo",
  data: {
    val: {
      thing: {
        info: "bar",
        moreInfo: {
          evenMoreInfo: {
            weMadeIt: "baz",
          },
        },
      },
    },
  },
};

console.log(collectStrings(obj)); // ['foo', 'bar', 'baz'])
