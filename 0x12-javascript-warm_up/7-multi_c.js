#!/usr/bin/node
const index = process.argv;
if (isNaN(index[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < index[2]; i++) {
    console.log('C is fun');
  }
}
