# Phase A — Foundations (new material for the merged `system-design` area)

New material only. `briefs/expanded/system-design.md` (HLD, 14 groups) and
`briefs/expanded/object-oriented-design.md` (LLD, 10 groups) are reused verbatim by the merge step.
This file adds (a) a new group `distributed-systems-core` and (b) 1-2 expert-tier additions to the
existing `sd-fundamentals` group. Format matches `briefs/expanded/system-design.md` lines 1-60.

---

## Group: Distributed Systems Core (distributed-systems-core)
*partial failure, time, coordination — the theory both existing briefs assume but never teach*

### Topic: Partial Failure & Failure Models (partial-failure-and-failure-models, intermediate)
Why distributed failure isn't a binary up/down, the taxonomy of failure modes, and why "it's just a slow network" is the hardest case to design for.
- Partial failure: the one idea that makes distributed systems different from single-machine ones (concept)
- The failure taxonomy: crash-stop, omission, timing, byzantine (concept)
- Diagram: a request failing partway through a multi-hop call chain (diagram)
- Byzantine-lite in practice: nodes that respond incorrectly, not just go silent (concept)
- Gray failure: the node that passes health checks but is degraded for real traffic (concept)
- Compare: crash-stop vs crash-recovery vs byzantine failure assumptions, and what each costs to defend against (compare)
- Pitfall: treating "no response" as proof the request never happened (pitfall)
- Interview: "A downstream call times out — what actually could have happened, and what do you do?" (interview)

### Topic: Failure Detection: Heartbeats, Phi-Accrual & Its Limits (failure-detection, intermediate)
How systems decide a peer is dead, why perfect failure detection is provably impossible over an asynchronous network, and the heartbeat/phi-accrual mechanics behind real detectors.
- Heartbeats: the simplest failure detector, and why it produces false positives (concept)
- Fixed timeouts: the tension between detecting fast and crying wolf (concept)
- Diagram: a heartbeat missing a beat under GC pause vs. an actual crash (diagram)
- Phi-accrual failure detection: a continuous suspicion level instead of a binary verdict (concept)
- The impossibility result: no failure detector can be both accurate and complete over an unreliable network (concept)
- Compare: fixed timeout vs. phi-accrual vs. gossip-based detection on speed, false-positive rate, and cost (compare)
- Pitfall: one global timeout tuned for the happy path, wrong for every slow dependency (pitfall)
- Interview: "How would you detect a dead node without falsely evicting one that's just slow?" (interview)

### Topic: Time & Ordering Without a Shared Clock (time-and-ordering, advanced)
Physical clocks vs. logical clocks vs. vector clocks for establishing causality across machines, and how hybrid logical clocks and TrueTime close the gap in production systems.
- Why wall-clock time lies across machines: clock skew, drift, and NTP's limits (concept)
- Lamport clocks: ordering events with a single counter and a simple rule (concept)
- Diagram: Lamport timestamps ordering a chain of causally related events (diagram)
- Vector clocks: capturing causality a single counter can't — and detecting true concurrency (concept)
- Hybrid Logical Clocks: keeping the intuition of wall time with the safety of logical time (concept)
- Google TrueTime: bounding clock uncertainty instead of eliminating it (concept)
- Compare: Lamport vs. vector clocks vs. HLC vs. TrueTime on what each can and can't order (compare)
- Pitfall: using `System.currentTimeMillis()` to decide which of two events happened first (pitfall)
- Interview: "Two events land on different servers — how do you know which happened first?" (interview)
- — cross-link: conflict-resolution (vector clocks applied specifically to detecting concurrent replica writes)

### Topic: Idempotency & the Exactly-Once Illusion (idempotency-and-exactly-once, advanced)
Why exactly-once delivery doesn't exist at the network layer, and how idempotency keys and dedup windows fake "effectively once" well enough to matter.
- Exactly-once delivery: why it's unachievable once a network can drop or duplicate packets (concept)
- At-most-once vs. at-least-once: the two honest options, and why most systems pick the second (concept)
- Diagram: a client's retry racing an in-flight duplicate at the receiver (diagram)
- Idempotency keys: turning "at-least-once delivery" into "exactly-once effect" (concept)
- Dedup windows: how long you remember a key, and what happens once you forget it (concept)
- Code: an idempotent payment handler keyed on a client-generated request ID (code)
- Compare: operations idempotent by construction (e.g. `SET`) vs. idempotency bolted on with a key (compare)
- Pitfall: an idempotency key that covers the write but not the side effect it triggers (payment succeeds, confirmation email fires twice) (pitfall)
- Interview: "A client retries a payment request after a timeout — how do you guarantee it's charged exactly once?" (interview)
- — cross-link: message-delivery-semantics (queue-level at-least-once vs. exactly-once framing)

### Topic: Distributed Coordination: Locks, Leases & Fencing (distributed-coordination, advanced)
Using an external coordination service for mutual exclusion and leadership, and why a naive distributed lock is unsafe under a process pause without a fencing token.
- Why you need coordination: mutual exclusion and leadership across independent processes (concept)
- The naive distributed lock: acquire, do work, release — and how a pause breaks it (concept)
- Diagram: a paused lock-holder still "holding" the lock while a second worker acquires it (diagram)
- Leases: a lock with a built-in expiry instead of a promise to release (concept)
- Fencing tokens: making a stale lock-holder's writes harmless instead of just arriving late (concept)
- Coordination services in practice: what ZooKeeper and etcd actually give you (concept)
- Compare: DIY heartbeat-based leader election vs. a coordination-service election (compare)
- Pitfall: assuming "my lock hasn't expired" means "I'm still safe to act" (pitfall)
- Interview: "How do you guarantee only one instance of a scheduled job runs across your fleet?" (interview)
- — cross-link: consensus-basics (the consensus algorithm a coordination service runs underneath)

### Topic: Split-Brain & Quorum Loss (split-brain-and-quorum-loss, expert)
What happens when a partition leaves two sides each believing they're in charge, and how to recover without silently corrupting data.
- Split-brain: a partition that produces two "leaders," each convinced it's the only one (concept)
- Diagram: a network partition splitting a cluster into a majority side and a minority side (diagram)
- Quorum loss: what a cluster should do when no side holds a majority (concept)
- Fencing the losing side: cutting it off (e.g. STONITH) rather than trusting it to step down (concept)
- Compare: preventing split-brain with quorum rules vs. reconciling it after the fact (compare)
- Safe recovery: rejoining a healed partition without triggering a second split (concept)
- Pitfall: "fixing" a split-brain by manually picking whichever side has more recent-looking data (pitfall)
- Interview: "Your cluster just healed from a partition — what do you check before it serves traffic again?" (interview)
- — cross-link: quorum-systems (the N/W/R math that determines whether a side even has quorum)

---

## Additions to existing group: System Design Fundamentals (sd-fundamentals)

### Topic: Designing Under Physical & Cost Constraints (physical-and-cost-constraints, expert)
Treating the speed of light and the monthly bill as design inputs, not afterthoughts — the constraints a senior engineer names before proposing a fix.
- The speed-of-light floor: why cross-region latency has a hard minimum no engineering fixes (concept)
- Diagram: an irreducible round-trip-time budget across regions vs. what the product actually needs (diagram)
- Cost as a design variable: egress, storage class, and idle compute as real trade-offs, not footnotes (concept)
- Compare: paying in latency (fewer regions) vs. paying in cost (more replication, more regions) (compare)
- Build vs. buy under cost pressure: when a managed service is cheaper than the engineering to replace it (concept)
- Pitfall: a design that "solves" latency by adding replicas without pricing the replication and egress cost (pitfall)
- Interview: "Your design meets every functional requirement but costs 5x budget — what do you cut first, and why?" (interview)

---

## Boundary notes

- **consistency-replication (existing HLD group)** is the hard boundary this brief was told to respect:
  consistency models, replication strategies, quorum math, conflict resolution/CRDTs, and consensus
  basics all stay there. `time-and-ordering`, `distributed-coordination`, and `split-brain-and-quorum-loss`
  cross-link into it (`conflict-resolution`, `consensus-basics`, `quorum-systems`) rather than re-deriving
  those mechanics.
- **computer-networks** owns the network layer itself (packet loss, retransmission, TCP/UDP behavior).
  `partial-failure-and-failure-models` and `failure-detection` assume that layer and reason about it from
  the distributed-systems side — recommend keeping them here, not moving to computer-networks.
- **operating-systems** — `distributed-coordination` (locks, leases) has a single-machine cousin in
  OS-level mutexes/semaphores; this topic is scoped to *cross-process, cross-machine* coordination only,
  so no overlap in practice, but worth a reviewer's eye if operating-systems ever adds a concurrency-primitives topic.
- **cloud-devops-sre** — `physical-and-cost-constraints` brushes against FinOps/cost-optimization territory
  that a dedicated SRE/cloud brief might also want to own. Recommend keeping it in `sd-fundamentals` since
  it's framed as a design-interview trade-off (what to cut, not how to run a cost-optimization program), but
  flagging in case cloud-devops-sre later adds a cost-management group — dedupe at that point.
- **databases** — none identified; `idempotency-and-exactly-once` and `time-and-ordering` stay at the
  distributed-systems level (delivery semantics, causality) rather than the storage-engine level that a
  databases brief would own (e.g. MVCC, WAL) — no slug or scope collision expected.
