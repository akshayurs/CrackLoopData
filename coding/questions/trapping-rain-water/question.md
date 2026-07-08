You are given an array `height` of non-negative integers where each entry is the height of a vertical bar of unit width, laid out side by side. After it rains, water pools in the dips between taller bars. Return the total amount of water that can be trapped.

Water sits on top of a bar only if there is something taller on **both** its left and right to hold it in; the level above any position is capped by the shorter of the tallest bar to its left and the tallest bar to its right.

## Examples

```text
Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
```

```text
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
```

```text
Input:  height = [3, 0, 2]
Output: 2        # the dip holds min(3, 2) - 0 = 2 units
```

## Constraints

- 1 <= height.length <= 2 * 10^4
- 0 <= height[i] <= 10^5

## Follow-up

The prefix/suffix-max solution runs in O(n) time but uses O(n) extra space. Can you reach O(1) space?
