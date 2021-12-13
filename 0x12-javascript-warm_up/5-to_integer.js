#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt(args[2]));
}
