#!/usr/bin/node
const len = process.argv;
if (isNaN(len[2])) {
  console.log('Missing size');
} else {
  const index = parseInt(len[2]);
  let line = 'X';
  for (let j = 0; j < index - 1; j++) {
    line += 'X';
  }
  for (let i = 0; i < index; i++) {
    console.log(line);
  }
}
