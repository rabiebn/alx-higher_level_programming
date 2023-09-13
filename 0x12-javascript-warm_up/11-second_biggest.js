#!/usr/bin/node

const argArray = [];
let i;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    argArray.push(parseInt(process.argv[i]));
  }
  i = 0;
  let maxInt, sndMax;
  maxInt = sndMax = argArray[0];
  while (i < argArray.length) {
    if (maxInt < argArray[i]) {
      sndMax = maxInt;
      maxInt = argArray[i];
    }
    i++;
  }
  console.log(sndMax);
}
