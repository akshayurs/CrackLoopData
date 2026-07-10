The stack in the first approach only ever gets popped by `*` and `/`, and everything else just gets summed at the end — so you don't actually need to keep the whole list around. Track a running `total` for everything that's already settled, and keep just the *last* term separately so a following `*` or `/` can still fold into it before it's added to the total.

When you hit `+` or `-`, the pending term is finished: fold it into `total` and start a fresh pending term with the new sign. When you hit `*` or `/`, the pending term isn't finished yet — recompute it in place.

```python
def calculate(s):
    total = 0
    prev = 0
    num = 0
    sign = "+"
    n = len(s)
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        is_last = i == n - 1
        if (not ch.isdigit() and ch != " ") or is_last:
            if sign == "+":
                total += prev
                prev = num
            elif sign == "-":
                total += prev
                prev = -num
            elif sign == "*":
                prev *= num
            elif sign == "/":
                prev = int(prev / num)
            sign = ch
            num = 0
    return total + prev
```

## Why it works

`prev` always holds the value of the term currently being built — the part that a later `*` or `/` might still rewrite. `total` holds everything already locked in. Seeing `+`/`-` proves the current term can never change again, so it's folded into `total` before starting the next term; seeing `*`/`/` rewrites `prev` in place since precedence means it still binds to the number that follows. Adding the final `prev` after the loop accounts for the last term, which never gets flushed by a trailing operator.

## Complexity

- Time: O(n) — each character is visited once.
- Space: O(1) — a fixed number of scalar variables, regardless of input size.
