let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]);
const answser = (N + 2) * (N + 1) * N / 2
console.log(answser);