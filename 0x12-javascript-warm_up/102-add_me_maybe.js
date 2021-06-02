#!/usr/bin/node
// 101-call_me_moby.js
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
