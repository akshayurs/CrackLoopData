Reach for a hash map or set the moment a problem sounds like any of these:

- **"Find two/three items that combine to X"** — pair sums, complements, "numbers that add up to target". You want O(1) "have I seen the complement?" lookups.
- **"Has this appeared before?" / "Are there duplicates?"** — a set of seen values.
- **"Group things that share a property"** — anagrams (sorted string as the key), words by length, numbers by remainder. The shared property *is* the map key.
- **"How many times does each … appear?"** — frequency counting, then read off the counts.
- **"Count / longest subarray with sum = k"** — a running-sum → seen map.

Signal words: *"exactly one"*, *"distinct"*, *"count of"*, *"group by"*, *"seen"*, *"has appeared"*. If your first instinct is a nested loop over pairs, that is the cue to ask whether a map removes the inner loop.
