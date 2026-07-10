SQL interview questions are not about syntax trivia — they are about shaping a **relational query** that combines, filters, and aggregates rows from one or more tables to answer a question. The core moves are **joins** (combine related rows across tables), **`GROUP BY`** (collapse many rows into one per key, paired with aggregates like `COUNT`, `SUM`, `MAX`), and **window functions** (compute a value per row while still seeing the whole partition, e.g. a running rank).

Unlike algorithmic code, there is no explicit loop — the engine decides how to execute your query. Your job is to describe *what* result you want, not *how* to compute it row by row. That mental shift — "declare the shape of the answer" instead of "step through the data" — is the heart of the pattern.

A typical query composes like this:

```
SELECT grouping_key, AGGREGATE(value)
FROM table
JOIN other_table ON join_condition
WHERE row_level_filter
GROUP BY grouping_key
HAVING aggregate_level_filter
ORDER BY sort_key
```

**Self-joins** compare a table to itself (employee vs. manager, this month vs. last month). **Subqueries / CTEs** let you compute an intermediate result (e.g. "the second highest salary") and then query that result. **Window functions** (`RANK() OVER (...)`, `LAG()/LEAD()`) solve "top-N per group" and "compare to previous row" problems without collapsing rows the way `GROUP BY` does — that distinction (keep every row vs. collapse rows) is the first fork in the road for most SQL problems.
