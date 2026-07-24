You are walking down a single row of fruit trees, represented by an integer array `fruits`, where `fruits[i]` is the type of fruit the `i`-th tree produces. You carry exactly **two baskets**, and each basket can hold only **one type** of fruit (but an unlimited quantity of it).

Starting from any tree you choose, you must pick exactly one fruit from every tree as you move right, and you must stop the moment you reach a tree whose fruit does not fit in either basket. Return the **maximum number of fruits** you can collect — that is, the length of the longest contiguous subarray containing at most two distinct values.

## Examples

```text
Input:  fruits = [1, 2, 1]
Output: 3        # all three trees use only types {1, 2}
```

```text
Input:  fruits = [0, 1, 2, 2]
Output: 3        # pick [1, 2, 2]; starting at 0 would need a third basket
```

```text
Input:  fruits = [1, 2, 3, 2, 2]
Output: 4        # pick [2, 3, 2, 2], using types {2, 3}
```

## Constraints

- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

## Follow-up

Can you find the answer in a single pass over the array, using memory proportional only to the number of allowed baskets?
