#!/usr/bin/env ts-node

// ensure proper usage
if (process.argv.length != 3) { console.log("Usage: map.ts <input>"); process.exit(1) }

var range: number = Number(process.argv[2]);

// generate first `range` chars from the alphabet
var buff: Array<string> | string = []; for (let i = 0; i < range; i++) buff.push(String.fromCharCode(97 + i));

// these elements will be excluded
var exclude: Array<string> = ['a', 'b', 'c'];

// using in-built functions with single-line parsing
buff = buff.filter(x => !exclude.includes(x)).sort().join(' ');
console.log(buff);
