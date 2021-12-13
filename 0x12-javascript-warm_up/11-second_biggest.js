#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const numbersArray = process.argv.slice(2).map(Number);
  const penultimate = numbersArray.sort(function (a, b) { return b - a; })[1];
  console.log(penultimate);
}
