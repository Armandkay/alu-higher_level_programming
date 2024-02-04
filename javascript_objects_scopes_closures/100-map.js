#!/usr/bin/node
// Import the list from the file
const { list } = require('./100-data.js');

// Compute a new array using map
const newList = list.map((value, index) => value * index);

// Print both the initial array and the new array
console.log('Initial list:', list);
console.log('New list:', newList);
