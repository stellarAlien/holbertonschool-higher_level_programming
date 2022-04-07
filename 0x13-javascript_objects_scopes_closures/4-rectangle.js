#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(h) || isNaN(w)) { return; }
    this.height = h;
    this.width = w;
  }
  double () {
    for (let i = 0; i < this.height * 2; i++) {
      for (let j = 0; j < this.width * 2; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
    return;
  }
  rotate () {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
    return;
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
