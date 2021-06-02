#!/usr/bin/node

const myArgs = process.argv.slice(2);

console.log(factorial(myArgs[0]));

function factorial (n) {
  return (n != 1) ? n * factorial(n - 1) : 1;
}
