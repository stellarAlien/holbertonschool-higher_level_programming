#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const fs = require('fs');
request(url, function (err, result, body) {
  if (err) {
    console.log(err);
  } else {
    const file = process.argv[3];
    fs.writeFile(file, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
