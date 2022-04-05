#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(h) || isNaN(w)) { return; }
    this.height = h;
    this.width = w;
  }
}
module.exports = Rectangle;
