#!/usr/bin/node
const fs = require('fs');
const { exit } = require('process');
const args = process.argv;
fs.readFile(args[2], 'utf8', function (err, data) {
  if (data !== undefined) {
    console.log(data);
    exit();
  }
  console.log(err);
});
