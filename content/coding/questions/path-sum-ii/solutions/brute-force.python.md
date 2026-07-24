The most direct reading: find *every* root-to-leaf path first, ignoring the target entirely, then go back and keep only the ones that happen to add up to `targetSum`. Recording a path is just a depth-first walk that appends the current value, recurses, and pops it back off before returning to the parent — classic backtracking to reuse one buffer for every branch.

Once every path has been collected, filtering is a second, separate pass: sum each stored path and compare it to `targetSum`. It works, but it does strictly more work than necessary since most collected paths are usually discarded.

```python
def path_sum(root, target_sum):
    all_paths = []

    def collect(node, path):
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None:
            all_paths.append(list(path))
        else:
            collect(node.left, path)
            collect(node.right, path)
        path.pop()

    collect(root, [])
    return [p for p in all_paths if sum(p) == target_sum]
```

## Why it works

`collect` performs a standard DFS, growing `path` on the way down and shrinking it on the way back up, so by the time a leaf is reached `path` holds exactly the values from the root to that leaf. Copying it into `all_paths` at each leaf preserves left-to-right, root-to-leaf order across the whole tree. The final list comprehension then re-derives each path's sum independently and keeps only the matches.

## Complexity

- Time: O(n^2) — the DFS visits every node once, but each of the up to O(n) leaf paths can be O(n) long, and both copying and summing a path cost O(path length).
- Space: O(n^2) — `all_paths` retains every root-to-leaf path, not just the matching ones, before filtering.
