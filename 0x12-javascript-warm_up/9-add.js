#!/usr/bin/node
const numbers = process.argv;
function add (a, b) {
  console.log(a + b);
}
add(parseInt(numbers[2]), parseInt(numbers[3]));
