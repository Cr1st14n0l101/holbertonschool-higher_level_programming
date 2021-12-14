#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += c;
    }
    for (let j = 0; j < this.height - 1; j++) {
      console.log(line);
    }
    console.log(line);
  }
};
