#!/usr/bin/node
exports.esrever = function (list) {
  let j = 0;
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList[j++] = list[i];
  }
  return newList;
};
