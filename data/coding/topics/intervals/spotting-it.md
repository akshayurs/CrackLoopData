Reach for the intervals pattern the moment a problem gives you a list of ranges and asks you to combine, compare, or schedule them:

- **"Merge overlapping intervals"** — return the union of all ranges as the smallest possible list.
- **"Insert a new interval into a sorted list"** — merge it in place with any overlaps.
- **"Can a person attend all meetings?" / "Minimum rooms needed"** — overlap detection and counting concurrent ranges.
- **"Maximum number of non-overlapping intervals you can keep"** — greedy selection, usually by earliest end time.
- **"Minimum number of arrows/points to cover all intervals"** — same greedy-by-end-time shape in disguise.
- **"Intersection of two interval lists"** — two sorted lists, two pointers, compare overlaps pairwise.
- **"Free time" / "gaps between busy ranges"** — merge everything, then read off the holes between merged ranges.

Signal words: *"overlap"*, *"merge"*, *"schedule"*, *"conflict"*, *"free time"*, *"booked"*, *"at the same time"*, *"cover"*, *"remove the minimum number to make non-overlapping"*. Any time the input is described as a list of `[start, end]` pairs — meetings, bookings, ranges on a number line — that phrasing alone is the tell, even before you read the actual question.

If your first instinct is to compare every pair of intervals directly, that is the cue to sort first: sorting turns "does this overlap with *any* other interval" into "does this overlap with the *previous* one," which is the whole point of the pattern.
