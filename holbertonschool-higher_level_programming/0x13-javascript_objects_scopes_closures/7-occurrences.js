#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // if(typeof(searchElement) == "undefined")
  // return;
  let i = 0;
  let S = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      S += 1;
    }
  }
  return (S);
};
