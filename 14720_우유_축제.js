// 14720 우유 축제 221109 브론즈 3
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
const N = Number(input[0]);
const milkShop = input[1].split(" ").map((e) => Number(e));
let ind = 0;
const milkOrder = [0, 1, 2]
let ans = 0;
for (let i = 0; i < milkShop.length; i++) {
  nowMilk = milkOrder[ind];
  if (nowMilk === milkShop[i]) {
    ans += 1
    ind += 1
    if (ind == 3) {
      ind = 0
    }
  }
}
console.log(ans);