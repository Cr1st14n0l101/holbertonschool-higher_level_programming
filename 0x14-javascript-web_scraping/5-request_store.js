#!/usr/bin/node
const args = process.argv;
const request = require('request');
const fs = require('fs');
request(args[2], function (error, response, body) {
  if (error) throw error;
  fs.writeFile(args[3], body, 'utf-8', function (err) {
    if (err) throw err;
  });
});
