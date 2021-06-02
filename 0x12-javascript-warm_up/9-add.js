#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (typeof myArgs[0] === 'undefined' || isNaN(myArgs[0])) {
  console.log('NaN');
} else if (typeof myArgs[1] === 'undefined' || isNaN(myArgs[1])) {
  console.log('NaN');
} else {
  console.log(add(myArgs[0], myArgs[1]));
}
function add(a, b) {
    return +a + +b;
}
