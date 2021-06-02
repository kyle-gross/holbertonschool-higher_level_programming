#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs.length === 0) {
  console.log('%i', 0);
} else if (myArgs.length === 1) {
  console.log(myArgs[0]);
} else {
  console.log(secondMax(myArgs));
}

function secondMax (myArr) {
  let max = -Infinity;
  let result = -Infinity;

  for (const value of myArr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  }
  return (result);
}
