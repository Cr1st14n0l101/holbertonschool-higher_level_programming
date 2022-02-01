#!/usr/bin/node
const request = require('request');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) throw error;
  const json = JSON.parse(body);
  const size = Object.keys(json).length;
  const tasksObject = {};
  for (let i = 0; i < size; i++) {
    if (json[i].completed) {
      if (tasksObject[json[i].userId]) {
        tasksObject[json[i].userId] += 1;
      } else {
        tasksObject[json[i].userId] = 1;
      }
    }
  }
  console.log(tasksObject);
});
