#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let current = args[2];
  let beforeCurrent = 0;
  for (let i = 2; args[i]; i++) {
    if (args[i] > current) {
      beforeCurrent = current;
      current = args[i];
    } else if (args[i] < current && args[i] >= beforeCurrent) {
      beforeCurrent = args[i];
    }
  }
  console.log(beforeCurrent);
}
