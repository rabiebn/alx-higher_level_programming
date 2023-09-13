#!/usr/bin/node

let x = parseInt(process.argv[2]);
let j = 0;
let i = 0;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  while (i < x) {
    while (j < x) {
      process.stdout.write('X');
      j++;
    }
    console.log();
    i++;
    j = 0;
  }
}
