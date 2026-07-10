The most direct reading of RPN: an operator always sits right after the two numbers it combines. So repeatedly scan left to right for the first operator, fold the two integers before it into a single result, and rebuild the list around that result. Each fold shrinks the list by two entries, and eventually one number remains — the answer.

Restarting the scan from the front after every fold keeps the logic simple at the cost of rescanning, which makes this quadratic; it is a fine way to build intuition before reaching for a stack.

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int evalRPN(String[] tokens) {
        List<String> list = new ArrayList<>(List.of(tokens));
        int i = 0;
        while (list.size() > 1) {
            String t = list.get(i);
            if (t.equals("+") || t.equals("-") || t.equals("*") || t.equals("/")) {
                int a = Integer.parseInt(list.get(i - 2));
                int b = Integer.parseInt(list.get(i - 1));
                int r = t.equals("+") ? a + b : t.equals("-") ? a - b
                        : t.equals("*") ? a * b : a / b;
                list.subList(i - 2, i + 1).clear();
                list.add(i - 2, String.valueOf(r));
                i = 0;
            } else {
                i++;
            }
        }
        return Integer.parseInt(list.get(0));
    }
}
```

## Why it works

A valid RPN expression guarantees that the first operator encountered is preceded by exactly the two operands it applies to. Folding `[a, b, op]` into its numeric result is therefore always safe, and it preserves the postfix structure of everything around it. Repeating until one token is left evaluates the whole expression. Java integer division already truncates toward zero, matching the required semantics.

## Complexity

- Time: O(n²) — up to n/2 folds, and each fold may rescan and shift O(n) tokens.
- Space: O(n) — the working copy of the token list.
