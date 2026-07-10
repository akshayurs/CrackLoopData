You're advising a startup that is about to go public and wants to pump up its capital before the IPO by greenlighting a handful of internal projects first. There are `n` candidate projects; project `i` requires `capital[i]` money to start and, once finished, returns a **pure profit** of `profit[i]` (already completed — no risk, no failure). The company currently has `w` money and may greenlight **at most `k`** projects, one at a time, in any order.

Before starting a project the company's current money must be `>= capital[i]`. After it finishes, the profit is added to the company's money, which can then be used to unlock projects that were previously too expensive. Projects run one after another (never in parallel), and once a project is completed it can't be chosen again.

Pick projects (up to `k` of them) to maximize the final amount of money. Return that maximum final amount.

## Examples

```text
Input:  k = 2, w = 0, profit = [1, 2, 3], capital = [0, 1, 1]
Output: 4
# Start with 0 money -> only project 0 (capital 0) is affordable, taking it gives profit 1 -> money = 1.
# Now projects 1 and 2 (capital 1) are both affordable; pick the larger profit, project 2, giving +3 -> money = 4.
# k = 2 projects used, done.
```

```text
Input:  k = 3, w = 0, profit = [1, 2, 3], capital = [0, 1, 2]
Output: 6
# money=0 -> take project 0 (capital 0, profit 1) -> money=1.
# money=1 -> take project 1 (capital 1, profit 2) -> money=3.
# money=3 -> take project 2 (capital 2, profit 3) -> money=6.
```

```text
Input:  k = 1, w = 2, profit = [1, 2, 3], capital = [1, 1, 2]
Output: 5
# money=2 already affords all three projects; with only 1 pick allowed, take the highest profit (3) -> money=5.
```

## Constraints

- 1 <= k <= 10^5
- 0 <= w <= 10^9
- n == profit.length == capital.length
- 1 <= n <= 10^5
- 0 <= profit[i] <= 10^4
- 0 <= capital[i] <= 10^9

## Follow-up

Can you avoid re-scanning every project each time you pick one — get to O(n log n + k log n) instead of O(k * n)?
