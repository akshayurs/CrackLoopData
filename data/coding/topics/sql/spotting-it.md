Reach for the join/aggregate/window toolkit the moment a problem sounds like any of these:

- **"Combine information from two tables"** — an employee table and a department table, orders and customers. That is a `JOIN` (inner, left, or self-join depending on whether unmatched rows must still appear).
- **"Find the Nth highest / second highest …"** — `DISTINCT` + `ORDER BY` + `LIMIT/OFFSET`, or a window function (`DENSE_RANK`), especially once ties or gaps matter.
- **"Rank / top-K per group"** — "top 3 salaries per department" is the signature phrase for `RANK()`/`DENSE_RANK()` partitioned `OVER` a group, not a plain `GROUP BY`.
- **"Employees who earn more than their manager" / "compare a row to another row of the same table"** — a **self-join** on a foreign key that points back into the same table.
- **"Customers who never ordered" / "rows with no match"** — `LEFT JOIN ... WHERE right.key IS NULL`, or `NOT IN` / `NOT EXISTS`.
- **"Find duplicates" / "appears more than once"** — `GROUP BY` the column(s) with `HAVING COUNT(*) > 1`.
- **"Consecutive days/rows with a condition"** — compare a row to its neighbor via a self-join on `id ± 1` or `LAG()/LEAD()`.

Signal words: *"for each …"* (→ `GROUP BY`), *"at least / more than N times"* (→ `HAVING`), *"per department/category"* (→ partition, either `GROUP BY` or `PARTITION BY`), *"without a match"* (→ outer join), *"Nth"* / *"rank"* (→ window function). If the question needs one row per group, think `GROUP BY`; if it needs every row kept but annotated, think window function.
