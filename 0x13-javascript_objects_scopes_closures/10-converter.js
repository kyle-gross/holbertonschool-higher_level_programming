#!/usr/bin/node

exports.converter = function (base) {
  function baseChanger (number) {
    return number.toString(base);
  }
  return baseChanger;
};
