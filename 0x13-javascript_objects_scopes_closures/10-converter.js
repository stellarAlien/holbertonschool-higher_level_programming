#!/usr/bin/node
exports.converter = function (base) {
  function conv (x) {
    return (parseInt(x).toString(base));
  }
  return conv;
};
