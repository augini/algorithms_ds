// reverse
// Write a recursive function called reverse
// which accepts a string and returns a new string in reverse.

function reverse(str) {
  if (str.length > 1) {
    let firstChar = str[0];
    return reverse(str.slice(1)) + firstChar;
  }
  return str[0];
}

console.log(reverse("awesome")); // 'emosewa'
console.log(reverse("rithmschool")); // 'loohcsmhtir'
