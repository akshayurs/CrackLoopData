A phrase is a **palindrome** if, after removing every character that is not a letter or digit and treating uppercase and lowercase letters as the same, it reads identically forwards and backwards.

Given a string `s`, return `true` if it is a palindrome under those rules, and `false` otherwise.

## Examples

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: true          # cleaned form "amanaplanacanalpanama" reads the same both ways
```

```text
Input:  s = "race a car"
Output: false         # cleaned form "raceacar" is not symmetric
```

```text
Input:  s = " "
Output: true          # no alphanumeric characters remain, so it is trivially a palindrome
```

## Constraints

- 1 <= s.length <= 2 * 10^5
- `s` consists of printable ASCII characters.

## Follow-up

Can you decide the answer without building a separate cleaned copy of the string — using O(1) extra space?
