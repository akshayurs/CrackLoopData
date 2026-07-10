When the question generalizes to "Nth highest" or "top-N per group", a window function scales better than nested `MAX`. `DENSE_RANK()` numbers distinct salaries from the top — ties share a rank and no numbers are skipped — so the second highest is simply the rows at rank 2.

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) ranked
WHERE rnk = 2;
```

## Why it works

`DENSE_RANK() OVER (ORDER BY salary DESC)` assigns 1 to the highest distinct salary, 2 to the next distinct value, and so on with no gaps on ties. Filtering `rnk = 2` keeps the second-highest tier. Aggregating it with `MAX` collapses that tier to one value and, crucially, returns `NULL` automatically when no row has rank 2 (fewer than two distinct salaries).

## Output

```text
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

_Authored expected result for the example input `[[1, 100], [2, 200], [3, 300]]`. The app does not execute SQL — this output is shown for reference, not produced by a live run._
