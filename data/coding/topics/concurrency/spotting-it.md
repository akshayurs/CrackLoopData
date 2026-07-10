Reach for locks/semaphores/condition variables the moment a problem sounds like any of these:

- **"N threads must run in a specific order"** — Print In Order, Print FooBar Alternately, Print Zero Even Odd. You want a chain of signals (semaphores or condition flags), one per hand-off.
- **"Multiple threads share a counter/buffer/resource"** — a lock around the critical section so increments/writes don't race.
- **"Producers put items, consumers take them"** — Design Bounded Blocking Queue, Web Crawler Multithreaded. Two semaphores (empty slots, filled slots) plus a lock on the buffer.
- **"Several threads need the same resource but only K can use it at once"** — Traffic Light Controlled Intersection, Dining Philosophers. A counting semaphore sized to K, or a lock per resource plus a strategy to avoid deadlock.
- **"Print/build something character-by-character where threads must alternate"** — Building H2O, Fizz Buzz Multithreaded. Model each role as a semaphore that releases the next role's permit.

Signal words: *"threads"*, *"in order"*, *"alternately"*, *"simultaneously"*, *"at most K at a time"*, *"blocking"*, *"race condition"*, *"deadlock"*, *"starvation"*. If the problem describes multiple actors that must take turns or share a bounded resource, that is the cue — don't reach for a single-threaded loop.

Also watch the phrasing "prevent deadlock" or "avoid starvation" (classic in Dining Philosophers) — that's a hint the interviewer wants you to discuss ordering resource acquisition or bounding concurrent access, not just get one correct interleaving.

Since these problems are display-only in this app, the interview signal is the same as in a real interview: name the primitive, explain what it protects or signals, and describe *one* valid interleaving — you are not expected to execute the code.
