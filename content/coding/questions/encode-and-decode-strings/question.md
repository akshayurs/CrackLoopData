Design a pair of methods that can serialize a list of strings into one single string, then reconstruct the original list from that string. The two methods run on opposite ends of a channel: `encode` turns a `List<String>` into one string that gets sent over the wire, and `decode` turns that string back into the exact same list.

The catch is that the strings may contain **any** characters — letters, digits, spaces, punctuation, and even whatever separator you were hoping to use. Your scheme has to survive strings that look like your own formatting, empty strings, and an empty list.

## Examples

```text
Input:  ["neet", "code", "love", "you"]
Output: ["neet", "code", "love", "you"]   # decode(encode(list)) == list
```

```text
Input:  ["", ""]
Output: ["", ""]                           # two empty strings survive the round trip
```

```text
Input:  ["we", "say:", "#yes#"]
Output: ["we", "say:", "#yes#"]            # a string full of separators is fine
```

## Constraints

- 0 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- `strs[i]` may contain any characters in the range [0, 255] (including your delimiter).
- `decode(encode(strs))` must equal the original `strs`.

## Follow-up

Can you make the encoding work for **any** possible character without reserving a "magic" separator that the payload is forbidden from containing?
