Find the largest salary that is strictly below the overall maximum. Everything under the top value is a candidate; the greatest candidate is the second highest. Wrapping the result in an outer `SELECT ... AS` guarantees a single `NULL` row — rather than zero rows — when no candidate exists.

```sql
SELECT (
    SELECT MAX(salary)
    FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee)
) AS SecondHighestSalary;
```

## Why it works

The innermost `MAX(salary)` is the highest salary. The middle query takes the highest salary strictly below it — the second highest *distinct* value, since `MAX` naturally ignores duplicates. If only one distinct salary exists, the middle query has no rows and returns `NULL`; selecting that scalar subquery still yields exactly one row containing `NULL`, which is what the problem requires.

## Output

```text
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

_Authored expected result for the example input `[[1, 100], [2, 200], [3, 300]]`. The app does not execute SQL — this output is shown for reference, not produced by a live run._
