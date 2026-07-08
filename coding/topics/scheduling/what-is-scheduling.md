**Scheduling** problems ask you to order or place a set of jobs, tasks, or events under constraints — deadlines, cooldowns, limited resources (servers, rooms, machines), or dependencies between tasks. The output is usually a count (max profit, min rooms, max events attended) or the actual assignment.

There is no single algorithm here — scheduling is a *family* built from a few recurring moves:

- **Greedy + sort**: sort by a deadline, start time, or end time, then take the locally best choice at each step (earliest deadline first, earliest finish time first). Works when a greedy exchange argument proves the local choice never hurts the global optimum.
- **Greedy + heap**: when jobs recur or compete for a limited number of "slots" at once (cooldown between identical tasks, k available servers), a max-heap of "what's most urgent right now" replaces sorting.
- **Sort + DP (or binary search)**: when jobs have weights/profits and you must pick a *non-overlapping* subset, sort by end time and binary-search for the latest job that finishes before the current one starts.
- **Sort + sweep with a counter/heap**: for "how many resources are needed at once" (meeting rooms), turn each job into a `+1` at start and `-1` at end, sort the events, and sweep while tracking the running/max count.

A typical greedy-by-deadline shape:

```
sort tasks by deadline (or start time)
for each task in order:
    if a resource/slot is free and task still meets its constraint:
        assign task to that resource
    else:
        skip, bump it, or use a heap to swap in a better choice
return the count / arrangement built along the way
```

Recognize scheduling as "sorting turns the problem into a single clean pass" — the hard part is picking the *right* sort key and proving the greedy choice is safe.
