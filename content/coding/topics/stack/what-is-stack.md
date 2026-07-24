A **stack** is a LIFO (last in, first out) structure: you push onto the top and pop from the top, both in O(1). Arrays back most stacks — you just track a "top" index — so there is no exotic data structure to learn, only a discipline about *what you push and when you pop*.

Stacks shine whenever the most recently seen unresolved thing is exactly what you need next. Matching brackets, undo history, and "the last open call frame" are all literally LIFO. That is why stacks show up for parsing, matching, and expression evaluation.

The other big use case is the **monotonic stack** — a stack kept strictly increasing or strictly decreasing from bottom to top. Instead of storing everything you have seen, you only keep the elements that could still matter for a future comparison, popping off anything a new element makes irrelevant. This turns an apparent O(n²) "compare everyone to everyone" scan into O(n), because each element is pushed and popped at most once.

A typical monotonic-stack shape (next greater element to the right):

```
stack = empty          # holds indices, kept decreasing by value
for i, x in enumerate(nums):
    while stack is not empty and nums[stack.top] < x:
        j = stack.pop()
        answer[j] = x        # x is the next greater element for j
    stack.push(i)
# anything left on the stack has no next greater element
```

Two families to recognize: **matching stacks** (parentheses, tags, calculator operators) where you push/pop to track nesting, and **monotonic stacks** (next greater/smaller, histogram, stock span) where the invariant on the stack's ordering does the work.
