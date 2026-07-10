Write a SQL query to report the **second highest distinct salary** from the `Employee` table. When there is no second highest salary — fewer than two distinct values — the query must return `NULL`.

## Schema

```text
Employee
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
id is the primary key. salary is a non-negative integer.
```

## Examples

```text
Input:  Employee = [[1, 100], [2, 200], [3, 300]]
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

```text
Input:  Employee = [[1, 100]]
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| NULL                |
+---------------------+
```

## Constraints

- Salaries are compared as **distinct** values: `[300, 300, 200]` has second highest `200`.
- Return a single row containing `NULL` (not an empty result) when no second highest exists.
