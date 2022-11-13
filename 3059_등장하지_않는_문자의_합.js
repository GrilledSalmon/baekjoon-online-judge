// 3059 등장하지 않는 문자의 합 221113 브론즈 3
// js 잘하고 싶다... python만 쓰고싶다...

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

const solve = () => {
  const T = Number(input[0]);
  for (let t = 0; t < T; t++) {
    const S = input[t + 1];
    const alphArray = Array(26);
    for (let i = 0; i < S.length; i++) {
      alphArray[S.charCodeAt(i) - 65] = 1;
    }
    let ans = 0;
    for (let i = 0; i < 26; i++) {
      if (!alphArray[i]) {
        ans += i + 65;
      }
    }
    console.log(ans);
  }
};

rl.on("line", function (line) {
  input.push(line);
}).on("close", solve);