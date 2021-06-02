#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (typeof myArgs[0] === 'undefined' || isNaN(myArgs[0])) {
  console.log('%i', 1);
} else {
  console.log(factorial(myArgs[0]));
}

function factorial (n) {
  return (n !== 1) ? n * factorial(n - 1) : 1;
}
