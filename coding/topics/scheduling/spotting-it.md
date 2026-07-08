Reach for a scheduling technique the moment a problem sounds like any of these:

- **"Jobs/tasks with a start and end (or deadline and duration)"** — Job Scheduling, Course Schedule III, Meeting Rooms. Sort by end time or deadline first.
- **"Same task cannot repeat within a cooldown / distance"** — Task Scheduler, Rearrange String k Distance Apart. A max-heap of counts, refilled after a cooldown window, is the signal.
- **"Minimum number of rooms/servers/machines needed"** — Meeting Rooms II/III. Sweep-line with a min-heap of end times, or a `+1/-1` event count.
- **"Maximum profit / maximum number of non-overlapping jobs"** — Maximum Profit in Job Scheduling, Maximum Number of Events Attended. Sort by end time, then DP + binary search for the last compatible job.
- **"Assign N people/items to two or more groups to minimize cost"** — Two City Scheduling. Sort by the *difference* between two costs, a classic exchange-argument greedy.
- **"Requests routed to the next available / least-loaded server"** — Process Tasks Using Servers, Find Servers That Handled Most Requests. Two heaps (free servers, busy servers) sorted by availability time.
- **"Prerequisites must finish before a task can start, and there's also a deadline"** — Course Schedule III blends greedy + heap: take a course, and if you're now over the deadline, evict the most expensive one taken so far.

Signal words: *"deadline"*, *"cooldown"*, *"at most k at a time"*, *"non-overlapping"*, *"minimum number of rooms/resources"*, *"maximum profit/events"*, *"earliest/latest"*. If the problem gives you intervals or (start, end, weight) triples and asks for an optimal count or arrangement, it's scheduling — the question is just which sort key and data structure to pair with it.
