**Concurrency** problems ask you to coordinate two or more threads so that shared state stays correct and operations happen in a required order, even though the OS can interleave thread execution in almost any way. The core question is never "what does the code compute?" — it is "what stops thread A from stomping on thread B, or running before B is ready?"

Two families of tool do the coordinating:

- **Mutual exclusion** — a `Lock` / `synchronized` block / `Mutex` lets only one thread touch a critical section at a time. Use it to protect shared data (a counter, a buffer, a shared list).
- **Signaling** — a `Semaphore`, condition variable, `wait`/`notify`, or a bounded queue lets one thread *tell* another "your turn now" or "a resource is available." Use it to enforce ordering or hand off work.

A typical shape for ordering two threads (`Print In Order`-style) uses a semaphore as a one-shot signal:

```
sem = Semaphore(0)          // starts locked

threadA():
    doFirstThing()
    sem.release()            // signal "I'm done"

threadB():
    sem.acquire()            // block until A signals
    doSecondThing()
```

For a shared resource with limited slots (bounded queue, producer/consumer), you typically pair **two semaphores** — one counting empty slots, one counting filled slots — with a lock guarding the actual buffer mutation.

Because these questions are `runnable:false`, you reason about correctness on paper: identify the shared state, the ordering constraint, and pick the primitive whose job matches — lock for exclusion, semaphore/condition-variable for signaling, both together when you need exclusion *and* ordering.
