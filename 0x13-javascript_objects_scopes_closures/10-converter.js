#!/usr/bin/node
exports.converter = function (base) {
  return function (decimalBase) {
    return decimalBase.toString(base);
  };
};
