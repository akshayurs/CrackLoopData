The stack in the first approach only ever gets popped by `*` and `/`, and everything else just gets summed at the end — so you don't actually need to keep the whole list around. Track a running `total` for everything that's already settled, and keep just the *last* term separately so a following `*` or `/` can still fold into it before it's added to the total.

When you hit `+` or `-`, the pending term is finished: fold it into `total` and start a fresh pending term with the new sign. When you hit `*` or `/`, the pending term isn't finished yet — recompute it in place.

```javascript
function calculate(s) {
  let total = 0;
  let prev = 0;
  let num = 0;
  let sign = "+";
  const n = s.length;
  for (let i = 0; i < n; i++) {
    const ch = s[i];
    if (ch >= "0" && ch <= "9") {
      num = num * 10 + Number(ch);
    }
    const isLast = i === n - 1;
    if ((ch !== " " && (ch < "0" || ch > "9")) || isLast) {
      if (sign === "+") {
        total += prev;
        prev = num;
      } else if (sign === "-") {
        total += prev;
        prev = -num;
      } else if (sign === "*") {
        prev *= num;
      } else if (sign === "/") {
        prev = Math.trunc(prev / num);
      }
      sign = ch;
      num = 0;
    }
  }
  return total + prev;
}
```

## Why it works

`prev` always holds the value of the term currently being built — the part that a later `*` or `/` might still rewrite. `total` holds everything already locked in. Seeing `+`/`-` proves the current term can never change again, so it's folded into `total` before starting the next term; seeing `*`/`/` rewrites `prev` in place since precedence means it still binds to the number that follows. Adding the final `prev` after the loop accounts for the last term, which never gets flushed by a trailing operator.

## Complexity

- Time: O(n) — each character is visited once.
- Space: O(1) — a fixed number of scalar variables, regardless of input size.
