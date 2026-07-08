A parenthesized group is just a smaller expression whose value slots into the outer one, so let recursion mirror that structure. Scan left to right keeping a running `result`, a pending `num`, and the `sign` (`+1`/`-1`) that applies to the next number. On `+` or `-` you finalize the pending number into `result` and set the sign for what comes next.

When you hit `(`, recurse to evaluate the inner expression and treat its return value as the next `num`; when you hit `)`, fold the pending number in and return. A shared cursor field `pos` tells every frame where scanning currently sits, so it resumes past the matching `)`.

```java
class Solution {
    private int pos;

    public int calculate(String s) {
        pos = 0;
        return parse(s);
    }

    private int parse(String s) {
        int result = 0, num = 0, sign = 1;
        while (pos < s.length()) {
            char ch = s.charAt(pos);
            if (ch >= '0' && ch <= '9') {
                num = num * 10 + (ch - '0');
                pos++;
            } else if (ch == '(') {
                pos++;
                num = parse(s);
            } else if (ch == ')') {
                pos++;
                return result + sign * num;
            } else {
                if (ch != ' ') {
                    result += sign * num;
                    num = 0;
                    sign = ch == '+' ? 1 : -1;
                }
                pos++;
            }
        }
        return result + sign * num;
    }
}
```

## Why it works

`result` accumulates every completed term, while `num` and `sign` hold the term currently being read. An operator commits the pending term with its sign, then arms the sign for the next one. A `(` recurses; the inner call consumes through its own `)` (advancing the shared `pos`) and returns its value, which behaves exactly like a literal number. Unary minus falls out for free: a leading `-` simply flips `sign` while `num` is still `0`.

## Complexity

- Time: O(n) — each character is examined once across all recursive frames.
- Space: O(n) — recursion depth equals the maximum parenthesis nesting.
