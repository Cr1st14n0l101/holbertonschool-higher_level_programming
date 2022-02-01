#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
const id = 18;
let counter = 0;
request(url, function (error, response, body) {
  if (error) throw error;
  const json = JSON.parse(body);
  const size = Object.keys(json.results).length;
  for (let i = 0; i < size; i++) {
    const sizeCarasters = Object.keys(json.results[i].characters).length;
    for (let j = 0; j < sizeCarasters; j++) {
      if (json.results[i].characters[j].includes(String(id))) {
        counter++;
      }
    }
  }
  console.log(counter);
});
