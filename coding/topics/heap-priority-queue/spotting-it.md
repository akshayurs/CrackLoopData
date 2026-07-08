Reach for a heap the moment a problem sounds like any of these:

- **"Kth largest / smallest"** — in an array, a stream, or a matrix. A size-k heap tracks the answer without a full sort.
- **"Top K …"** — top K frequent elements/words, K closest points to origin. Bound the heap to size K.
- **"Find the median from a data stream"** — the signature two-heaps problem: elements keep arriving, you need the middle at any moment.
- **"Merge K sorted lists/arrays"** — one heap entry per list head; pop-min, push-next repeats until every list is drained.
- **"Repeatedly take the largest/smallest and combine or remove it"** — Last Stone Weight (smash the two heaviest), task/CPU scheduling by next available time.
- **"Schedule by earliest deadline / greedily pick highest value under a constraint"** — IPO, Furthest Building, meeting-room style problems where you keep pushing candidates and pulling the best one so far.

Signal words: *"kth"*, *"top K"*, *"K closest"*, *"streaming"*, *"running median"*, *"merge K"*, *"at any point in time"*, *"repeatedly pick the largest/smallest"*. If the data keeps changing and you keep asking "what's currently biggest/smallest?", that live query is the heap tell — a one-time sort will not survive new insertions cheaply.

Also watch for **k drastically smaller than n**: a size-k heap gives O(n log k), beating an O(n log n) full sort when k is small. If the problem hands you k explicitly, that is a strong nudge toward bounding your heap to that size rather than sorting everything.
