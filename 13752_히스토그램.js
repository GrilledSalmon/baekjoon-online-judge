// 221101  13752 히스토그램 브론즈 3
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

for (let i = 1; i < input.length; i++) {
  const k = input[i];
  let str = '';
  for (let j = 0; j < k; j ++) {
    str += '=';
  }
  console.log(str);
}