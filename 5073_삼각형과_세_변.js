// 5073 삼각형과 세 변 221119 브론즈 3
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
for (let i=0; i<input.length; i++) {
  const [a, b, c] = input[i].split(' ').map((e) => Number(e));
  const arr = [a, b, c]
  const maxNum = Math.max(...arr);
  const sum = arr.reduce((a, b) => a+b);
  if (a === 0 && b === 0 && c === 0){
    break
  }
  if (maxNum >= sum - maxNum){
    console.log('Invalid');
  } else if (a === b && b === c) {
    console.log('Equilateral');
  } else if (a === b || a === c || b === c) {
    console.log('Isosceles');
  } else {
    console.log('Scalene');
  }
}