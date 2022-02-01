#!/usr/bin/node
const args = process.argv;
const request = require('request');
request(args[2], function (error, response, body) {
  if (error) throw error;
  console.log('code:', response && response.statusCode);
});
