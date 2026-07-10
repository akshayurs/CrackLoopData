Math & geometry problems trade algorithmic cleverness for **arithmetic and spatial reasoning**: number theory (primes, digits, modular arithmetic), 2D coordinate manipulation (matrices, grids, points), and simulation (walk a path, apply a rule repeatedly, track state changes over rounds).

There is no single data structure that unlocks this category — instead there are recurring *tricks*: work in layers for matrices, use `%` and `/` to peel digits, detect cycles with a hash set (Floyd's or otherwise), and reason about **in-place transformation** so you don't pay for extra space you don't need.

A common shape is layer-by-layer matrix traversal — rotate, spiral, or zero out a matrix by processing one ring or one pass at a time:

```
top, bottom, left, right = boundaries of the matrix
while top <= bottom and left <= right:
    walk the top row left→right
    walk the right column top→bottom
    walk the bottom row right→left (if bottom > top)
    walk the left column bottom→top (if right > left)
    shrink boundaries inward
```

Another common shape is digit-by-digit numeric processing — extract the last digit with `n % 10`, drop it with `n //= 10`, and build up a result (reversed number, digit sum, carry propagation) as you go.

The unifying idea: **simulate the physical process** the problem describes — rotating a grid, walking a spiral, multiplying by hand, applying a rule to every cell simultaneously — rather than searching for a shortcut formula. When a closed-form trick exists (like fast exponentiation for `pow(x, n)`), it usually comes from noticing repeated substructure you can halve or fold.
