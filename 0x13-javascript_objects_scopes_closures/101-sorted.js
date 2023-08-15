#!/usr/bin/node
const dictionary = require('./101-data').dict;
const newDictionary = {};
for (const key in dictionary) {
  if (newDictionary[dictionary[key]] === undefined) {
    newDictionary[dictionary[key]] = [key];
  } else {
    newDictionary[dictionary[key]].push(key);
  }
}
console.log(newDictionary);
