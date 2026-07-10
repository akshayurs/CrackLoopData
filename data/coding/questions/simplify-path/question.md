You are given an absolute Unix-style file path as a string `path`. Return the **canonical** form of that path.

In a Unix path, `/` separates directory names, `.` refers to the current directory, and `..` moves up one level to the parent directory. Multiple consecutive slashes count as a single separator. A canonical path starts with a single `/`, joins directory names with single slashes, has no trailing slash (unless it is the root `/`), and contains no `.` or `..` components.

## Examples

```text
Input:  path = "/home//user/./docs/../"
Output: "/home/user"
```

```text
Input:  path = "/../"
Output: "/"                # cannot go above the root
```

```text
Input:  path = "/a/./b/../../c/"
Output: "/c"
```

## Constraints

- 1 <= path.length <= 3000
- `path` consists of English letters, digits, `.`, `/`, and `_`.
- `path` is a valid absolute Unix path — it begins with `/`.

## Follow-up

Can you avoid materializing the array of split components and instead tokenize the string in a single scan?
