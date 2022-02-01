#!/usr/bin/node
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) throw error;
  const json = JSON.parse(body);
  const size = Object.keys(json).length;
  const tasksObject = {};
  let counter = 0;
  let id = json[0].userId;
  for (let i = 0; i <= size; i++) {
    if (i === size) {
      tasksObject[id] = counter;
      break;
    }
    if (json[i].userId !== id) {
      tasksObject[id] = counter;
      counter = 0;
    }
    if (json[i].completed === true) {
      counter += 1;
    }
    id = json[i].userId;
  }
  console.log(tasksObject);
});
