#!/usr/bin/node
let x = 0;
exports.logMe = function (item) {
  console.log('%d: %s', x, item);
  x += 1;
};
