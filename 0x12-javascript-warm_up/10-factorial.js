#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
function factorial (number) {
  if (number < 0) {
    number = number * -1;
  }
  if (isNaN(number)) {
    return 1;
  }
  if (number === 0) {
    return 1;
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(num));
