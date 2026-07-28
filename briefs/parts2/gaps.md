# Coverage Gap Audit — system-design area (concept groups only)

Scope: conceptual (non-case-study, non-interview-bank) groups of the merged `system-design` area.
Baseline: `briefs/parts/_existing-slugs.txt` (29 groups). Does not touch `content/`, does not author
case studies (owned by the HLD/LLD case-study agents) or interview-question-bank topics (owned by the
HLD/LLD interview-bank agents). Value filter applied per `AUTHORING.md` — additions only where a
candidate would genuinely be asked, not to hit a count.

---

## Additions to existing group: SOLID & Design Principles (design-principles)

### Topic: Law of Demeter & Tell, Don't Ask (law-of-demeter-and-tell-dont-ask, intermediate)
A coupling principle SOLID doesn't cover: talk to your immediate collaborators only, and tell an object what to do instead of asking it for data to act on yourself.
- The Law of Demeter: "don't talk to strangers" — only call methods on objects you directly hold (concept)
- The train wreck smell: `a.getB().getC().getD().doSomething()` (concept)
- Diagram: a call chain reaching through three objects vs each object exposing one call (diagram)
- Tell, Don't Ask: pushing behavior to the object that owns the data instead of pulling data out to decide elsewhere (concept)
- Code: refactoring a getter chain into a single delegated call (code)
- Compare: strict Demeter compliance vs pragmatic exceptions (DTOs, builders, fluent APIs) (compare)
- Pitfall: "fixing" a train wreck by adding a wrapper method for every chain, multiplying the API surface (pitfall)
- Interview: "Your code review flags a long method chain — what's the actual risk, and how do you fix it?" (interview)

### Topic: Design by Contract & Invariants (design-by-contract-and-invariants, intermediate)
Making a class's promises explicit — preconditions, postconditions, and invariants — instead of leaving them as unwritten assumptions a caller can violate.
- Design by Contract: preconditions, postconditions, and invariants as an explicit promise (concept)
- Where this differs from encapsulation's "protect state" — contracts are about what callers can rely on (concept) — cross-link: encapsulation
- Diagram: a method's contract as a boundary — what the caller must supply, what the method guarantees back (diagram)
- Code: a stack's `pop()` documented and enforced with a precondition check (code)
- Class invariants: a rule that must hold before and after every public method (concept)
- Compare: enforcing contracts with runtime assertions vs types vs documentation-only (compare)
- Pitfall: a documented precondition nobody actually checks, so it silently rots into a lie (pitfall)
- Interview: "How would you make it impossible to call this method incorrectly?" (interview)

---

## Additions to existing group: UML & Modeling (uml)

### Topic: UML State & Activity Diagrams (uml-state-and-activity-diagrams, intermediate)
The two UML diagram types for behavior-over-decisions, distinct from the sequence diagram's behavior-over-time — drawn when a design has real states or real branching, not by default.
- State diagrams: states, transitions, and guard conditions as their own notation (concept) — cross-link: state-pattern
- Diagram: a state diagram for an order lifecycle, transitions labeled with triggering events (diagram)
- Activity diagrams: swimlanes, decision nodes, and fork/join for a branching process (concept)
- Diagram: an activity diagram for a multi-step approval workflow with a decision branch (diagram)
- Compare: state diagram (what state am I in) vs activity diagram (what happens next) vs sequence diagram (who calls whom) (compare)
- When a state diagram earns its place: a genuinely stateful entity with non-trivial transitions (concept)
- Pitfall: drawing a state diagram for an entity that's really just a status enum with no transition logic (pitfall)
- Interview: "This entity has 5 statuses — do you need a state diagram, or is a table enough?" (interview)

---

## Additions to existing group: Load Balancing & Proxies (load-balancing)

### Topic: Service Discovery (service-discovery, intermediate)
How a caller finds a live, correctly-addressed instance of a service when instances come and go — the piece that sits upstream of every load-balancing algorithm.
- The problem: instances scale up/down and move — a caller can't hardcode addresses (concept)
- Client-side discovery: the caller queries a registry and picks an instance itself (concept)
- Diagram: client-side discovery (caller → registry → direct call) vs server-side discovery (caller → LB → registry) (diagram)
- Server-side discovery: a load balancer or gateway does the lookup on the caller's behalf (concept)
- Service registries in practice: Consul/etcd/Eureka and DNS-based discovery as the simplest form (concept) — cross-link: dns-based-and-global-load-balancing
- Registration: self-registration vs a third-party registrar watching orchestrator state (compare)
- Compare: client-side vs server-side discovery on latency, coupling, and operational complexity (compare)
- Pitfall: a stale registry entry routing traffic to an instance that already died (pitfall)
- Interview: "You deploy 3 new instances — how does traffic start reaching them?" (interview)

### Topic: Connection Pooling (connection-pooling, intermediate)
Reusing expensive-to-open connections instead of paying a new handshake for every call — and the pool-sizing mistakes that quietly cap your throughput.
- Why opening a connection (TCP handshake, TLS, DB auth) is too expensive to do per request (concept)
- Connection pool mechanics: a bounded set of warm connections, checked out and returned (concept)
- Diagram: requests borrowing and returning connections from a bounded pool (diagram)
- Sizing a pool: too small starves callers, too big overwhelms the downstream server (concept)
- Pool exhaustion: what happens to the next caller when every connection is checked out (concept) — cross-link: bulkheads-and-isolation
- Code: acquiring a connection with a timeout instead of blocking forever (code)
- Compare: per-request connections vs a shared pool vs a connection per thread (compare)
- Pitfall: a connection pool sized for one service instance, then multiplied by 50 instances against one database (pitfall)
- Interview: "Your database says 'too many connections' under load — what's your first move?" (interview)

---

## Additions to existing group: Storage at Scale (storage-scale)

### Topic: Time-Series Data at Scale (time-series-storage-at-scale, advanced)
Why metrics, logs, and sensor data get their own storage engine instead of living in a general-purpose database — write-heavy, append-mostly, and queried by time range.
- What makes time-series data different: mostly-append writes, queries almost always scoped by time range (concept)
- Diagram: a time-series write path — batched, ordered by time, and downsampled on the way in (diagram)
- Downsampling and rollups: keeping fine-grained recent data, coarse-grained old data (concept)
- Retention policies as a first-class schema decision, not an afterthought (concept) — cross-link: data-lifecycle-and-archival
- Compare: a general-purpose DB vs a purpose-built TSDB (columnar layout, time-partitioned storage) (compare)
- Cardinality: why one extra high-cardinality tag can blow up storage and query cost (concept) — cross-link: cost-aware-telemetry-at-scale
- Pitfall: modeling a metric's tags so freely that cardinality grows unbounded (pitfall)
- Interview: "Design the storage for a metrics/monitoring system ingesting millions of points/sec" (interview)

### Topic: Secondary Indexes in a Sharded System (secondary-indexes-in-sharded-systems, advanced)
Querying by anything other than the shard key means either fanning out to every shard or maintaining a second, harder-to-keep-consistent index — the part partitioning-and-sharding leaves out.
- The problem: your shard key answers one query pattern; every other query has nowhere to go (concept) — cross-link: partitioning-and-sharding
- Scatter-gather queries: asking every shard and merging, when there's no secondary index at all (concept) — cross-link: search-at-scale
- Local secondary indexes: each shard indexes only its own data — fast to write, needs a fan-out to read (concept)
- Diagram: a local secondary index per shard vs one global secondary index (diagram)
- Global secondary indexes: a separate index structure that itself must be partitioned and kept in sync (concept)
- Keeping a global index consistent: synchronous dual-write vs async, and the staleness window either way (concept) — cross-link: replication-strategies
- Compare: local vs global secondary indexes on write cost, read cost, and consistency (compare)
- Pitfall: adding a global secondary index and not noticing every write just got slower or eventually-consistent (pitfall)
- Interview: "Your table is sharded by `user_id`, but you need to query by `email` — how?" (interview)

### Topic: Data Lifecycle: TTL, Archival & Tiered Storage (data-lifecycle-and-archival, intermediate)
Most data gets cheaper to store and less useful to query as it ages — designing for that curve instead of paying hot-storage prices for it forever.
- Why data has a lifecycle: hot → warm → cold, and access patterns that justify moving it (concept)
- TTL expiry: deleting data automatically once it stops being useful (concept)
- Diagram: a record's path from primary store to warm tier to cold archive to deletion (diagram)
- Tiered storage: hot (SSD/in-memory) vs warm vs cold (object storage/archive) by cost and latency (compare) — cross-link: object-and-blob-storage
- Archival jobs: moving data out without an outage, and what stays queryable during the move (concept)
- Compliance-driven retention: some data must be kept a minimum time, not just allowed to expire (concept) — cross-link: data-residency-and-cross-region-cost
- Pitfall: a TTL that deletes data a downstream system still silently depends on (pitfall)
- Interview: "This table grows by 1TB/month and 90% of it is never queried after 30 days — what do you do?" (interview)

---

## Additions to existing group: Consistency & Replication (consistency-replication)

### Topic: CRDTs in Depth (crdts-in-depth, advanced)
Conflict Resolution's one-slide mention of CRDTs, expanded into the actual data types and the guarantee that makes them mergeable without coordination.
- The guarantee CRDTs make: any two replicas' states merge into the same result, regardless of order (concept) — cross-link: conflict-resolution
- State-based (CvRDT) vs operation-based (CmRDT) CRDTs: sending state vs sending operations (compare)
- Diagram: two replicas diverging under concurrent updates, then converging after a merge (diagram)
- Common CRDTs: G-Counter/PN-Counter, OR-Set, and LWW-Register (concept)
- Code: implementing a PN-Counter that merges correctly under concurrent increments and decrements (code)
- Where CRDTs actually get used: collaborative editors, offline-first mobile apps, shopping carts (concept) — cross-link: design-collaborative-editor
- Compare: CRDTs vs operational transformation (OT) for collaborative editing (compare)
- Pitfall: reaching for a CRDT for data where "merge both" is actually the wrong business answer (pitfall)
- Interview: "Design offline-first note-taking that syncs across devices without a server round-trip" (interview)

### Topic: Read Repair & Anti-Entropy (read-repair-and-anti-entropy, advanced)
How leaderless, quorum-based stores like Cassandra and Dynamo heal stale replicas — one opportunistically on the read path, one continuously in the background.
- Why replicas drift even with quorum writes: a node that missed a write, or was down (concept) — cross-link: quorum-systems
- Read repair: a read notices a stale replica and fixes it as a side effect (concept)
- Diagram: a quorum read comparing replica versions and pushing the newest value to the stale one (diagram)
- Anti-entropy: background comparison (often via Merkle trees) to find and fix drift nobody happened to read (concept)
- Diagram: two replicas' Merkle trees compared top-down to find the exact diverged range (diagram)
- Compare: read repair (reactive, needs a read to trigger it) vs anti-entropy (proactive, runs regardless) (compare)
- Pitfall: relying on read repair alone for cold data nobody reads, so it drifts forever (pitfall)
- Interview: "Two replicas in your Dynamo-style store disagree — how does the system notice and fix it?" (interview)

---

## Additions to existing group: Messaging & Streaming (messaging-streaming)

### Topic: Transactional Outbox & Change Data Capture (outbox-and-cdc, advanced)
The dual-write problem — updating your database and publishing an event are two separate operations that can't both succeed atomically without a trick — and the two standard tricks.
- The dual-write problem: a crash between the DB commit and the publish loses or duplicates the event (concept) — cross-link: distributed-transactions-and-sagas
- Diagram: a service writing to its DB, then crashing before publishing — the event that never went out (diagram)
- The outbox pattern: write the event to an outbox table in the same local transaction as the data change (concept)
- A relay process (or CDC) tails the outbox table and publishes to the broker, then marks it sent (concept)
- Change Data Capture (CDC): tailing the database's own replication/commit log instead of a dedicated outbox table (concept) — cross-link: polyglot-persistence
- Compare: outbox-table-plus-relay vs log-based CDC (e.g. Debezium) — extra table vs extra infra (compare)
- Pitfall: publishing the event first and writing to the DB second "to be safe" — now a publish failure loses the write instead (pitfall)
- Interview: "How do you guarantee an 'order confirmed' event is published if and only if the order actually saved?" (interview)

### Topic: Stream Processing & Windowing (stream-processing-and-windowing, advanced)
Turning an unbounded stream into aggregates — counts, sums, averages — by defining a window of time to aggregate over, and what happens when events arrive late.
- Why you can't aggregate an infinite stream without first bounding it somehow (concept) — cross-link: log-based-streaming
- Tumbling windows: fixed, non-overlapping time buckets (concept)
- Diagram: tumbling vs sliding vs session windows over the same event stream (diagram)
- Sliding windows: overlapping buckets for a "last N minutes" style metric (concept)
- Session windows: grouped by activity gaps instead of fixed time (concept)
- Event time vs processing time, and why late-arriving events break naive windowing (concept) — cross-link: time-and-ordering
- Watermarks: a stream processor's way of deciding "late enough that we close the window" (concept)
- Compare: windowing choice by use case — dashboards (tumbling), trending (sliding), user sessions (session) (compare)
- Pitfall: windowing by processing time and getting wrong counts whenever consumers fall behind (pitfall)
- Interview: "Design a real-time leaderboard that updates every 10 seconds from a click stream" (interview)

### Topic: Batch vs Stream Processing & Lambda Architecture (batch-vs-stream-processing, advanced)
Why some pipelines still process data in batches on purpose, and the two-layer (batch + stream) architecture that hedges between correctness and freshness.
- Batch processing: correct, complete, and slow — reprocessing all data on a schedule (concept)
- Stream processing: fast and fresh, at the cost of approximate or eventually-corrected results (concept)
- Diagram: the same raw data flowing through a batch layer and a speed layer, merged in a serving layer (diagram)
- Lambda architecture: batch layer for ground truth, speed layer for low-latency approximate results (concept)
- Kappa architecture: treating the log as the only source of truth, reprocessing by replaying it (concept) — cross-link: log-based-streaming
- Compare: Lambda (two codepaths, reconciled) vs Kappa (one codepath, replayed) on operational complexity (compare)
- Pitfall: a speed-layer result and a batch-layer result disagreeing, with no reconciliation step defined (pitfall)
- Interview: "Your real-time dashboard and your nightly report show different numbers for the same day — why, and how do you design around it?" (interview)

---

## Additions to existing group: API Design (api-design)

### Topic: Webhooks & Callback APIs (webhooks-and-callback-apis, intermediate)
Pushing events to a consumer's own endpoint instead of making them poll — and the reliability problems (retries, ordering, forged calls) that come with handing delivery to someone else's server.
- Why webhooks exist: notifying a consumer without them polling you (concept)
- Diagram: an event triggering a signed HTTP callback to a registered consumer URL (diagram)
- At-least-once delivery: retries with backoff when the consumer's endpoint is down or slow (concept) — cross-link: message-delivery-semantics
- Signing payloads (HMAC) so the consumer can verify the call really came from you (concept)
- Ordering isn't guaranteed across retries — designing consumers to be idempotent and order-tolerant (concept) — cross-link: idempotency-and-exactly-once
- Compare: webhooks (you push) vs polling (they pull) vs long-lived connections (SSE/WebSocket) (compare)
- Pitfall: a webhook consumer's slow endpoint blocking your delivery worker pool for every other consumer (pitfall) — cross-link: bulkheads-and-isolation
- Interview: "Design a webhook delivery system for a payments platform with thousands of merchant endpoints" (interview)

### Topic: Designing Long-Running & Async APIs (long-running-and-async-apis, intermediate)
Some operations take minutes, not milliseconds — designing an API contract where the response is a "started" acknowledgment, not the actual result.
- Why a synchronous request/response contract breaks for operations that take minutes (concept) — cross-link: messaging-fundamentals
- The 202-Accepted-plus-status pattern: return a job ID immediately, let the client check progress (concept)
- Diagram: client submits, gets a job ID, polls a status endpoint until done (diagram)
- Polling vs webhook-on-completion vs a status stream for notifying the client (compare) — cross-link: webhooks-and-callback-apis
- Designing the status resource: states, progress, and a result location once done (concept)
- Code: a job-status endpoint's response shape across pending/running/done/failed (code)
- Pitfall: a "long-running" endpoint that's just a synchronous call with a very long timeout, tying up a connection the whole time (pitfall)
- Interview: "Design the API for a video-transcoding or report-generation feature" (interview)

### Topic: Designing API Error Contracts (api-error-contract-design, intermediate)
A consistent, structured error format is a design decision on its own — not a leftover detail — because it's what tells a caller whether to retry, fix their request, or give up.
- Why "just return a message string" fails every client that needs to branch on the error (concept)
- A structured error shape: machine-readable code, human message, and per-field validation detail (concept)
- Diagram: one error response shape reused across a 400, a 404, and a 429 (diagram)
- Retryable vs non-retryable errors: the one bit of information that matters most to a client (concept) — cross-link: retries-timeouts-and-backoff
- Compare: a flat error code enum vs a structured problem-details format (e.g. RFC 7807-style) (compare)
- Code: a shared error envelope reused across every endpoint in a service (code)
- Pitfall: leaking an internal exception's message and stack trace into a public error response (pitfall)
- Interview: "A client keeps retrying a request that will never succeed — what does that tell you about your error contract?" (interview)

---

## Additions to existing group: Rate Limiting & Resilience (resilience)

### Topic: Hedged Requests (hedged-requests, advanced)
Cutting tail latency by firing a second request to a different replica when the first one is running late, instead of just waiting it out — the trick behind Google's "Tail at Scale" latency numbers.
- The problem: at high fan-out, someone's p99 becomes your p50 (concept) — cross-link: latency-vs-throughput
- Hedged requests: send a duplicate request to a second replica if the first hasn't returned by a threshold, take whichever answers first (concept)
- Diagram: a hedged request racing the original after a short delay, first response wins (diagram)
- Setting the hedging delay: too short wastes capacity, too long doesn't help tail latency (concept)
- Tied requests: a stronger variant where both replicas know about each other and one cancels the other (concept)
- Compare: hedged requests vs plain retries — proactive duplication vs reactive retry-on-failure (compare) — cross-link: retries-timeouts-and-backoff
- Pitfall: hedging a non-idempotent write and getting it applied twice (pitfall) — cross-link: idempotency-and-exactly-once
- Interview: "Your p99 latency is 5x your p50 even though every server is healthy — what do you try?" (interview)

### Topic: Chaos Engineering & Fault Injection (chaos-engineering-and-fault-injection, advanced)
Designing a system on the assumption that its resilience mechanisms will be tested by deliberately breaking things in production, not just reasoned about on a whiteboard.
- The core idea: you don't know a resilience mechanism works until you've triggered the failure it's for (concept)
- Steady-state hypothesis: define what "normal" looks like before you break anything (concept)
- Diagram: an experiment — steady state, inject a fault, observe, compare against the hypothesis (diagram)
- Blast radius control: starting in staging, then a tiny percentage of production traffic (concept)
- What to inject: killed instances, added latency, dropped packets, exhausted disk/memory (concept)
- Compare: chaos engineering (continuous, deliberate fault injection) vs a DR failover drill (a specific, scheduled scenario) (compare) — cross-link: rpo-rto-and-failover-drills
- Pitfall: running a chaos experiment with no automatic abort when it's actually causing user-facing harm (pitfall)
- Interview: "How would you gain confidence that your circuit breakers actually trip in production, not just in a unit test?" (interview)

---

## Additions to existing group: Search & Indexing (search-indexing)

### Topic: Vector & Semantic Search (vector-and-semantic-search, advanced)
Matching by meaning instead of matching by keyword — embeddings, similarity search, and where an inverted index stops being enough.
- Why keyword search misses "meaning": synonyms, paraphrases, and cross-language matches (concept) — cross-link: search-fundamentals
- Embeddings: representing text/images as vectors where distance means semantic similarity (concept)
- Diagram: two differently-worded queries landing near the same document in vector space (diagram)
- Approximate nearest neighbor (ANN) search: HNSW and why exact nearest-neighbor doesn't scale (concept)
- Vector databases and vector indexes bolted onto existing stores (concept)
- Hybrid search: combining keyword (BM25) and vector similarity, and re-ranking the merged results (concept) — cross-link: relevance-ranking
- Compare: pure keyword search vs pure vector search vs hybrid — when each wins (compare)
- Pitfall: shipping vector search with no keyword fallback, so exact-match queries (SKUs, IDs) get worse (pitfall)
- Interview: "Design semantic search over a company's internal documents" (interview)

### Topic: Geospatial Indexing (geospatial-indexing, advanced)
Indexing "what's near this point" efficiently — the structures behind every proximity/nearby-search feature, and the concept the proximity-service case study assumes but never teaches.
- Why a normal index can't answer "find everything within 2km" efficiently (concept)
- Geohashing: encoding 2D coordinates into a sortable string so nearby points share a prefix (concept)
- Diagram: a geohash grid and the edge case where two nearby points land in different cells (diagram)
- Quadtrees: recursively subdividing space into denser cells where points are denser (concept)
- R-trees: bounding boxes that group nearby objects for fast range queries (concept)
- Compare: geohashing vs quadtree vs R-tree on query pattern and update cost (compare) — cross-link: design-proximity-service
- Pitfall: a geohash prefix search missing a nearby point that falls just across a cell boundary (pitfall)
- Interview: "How would you find the 10 nearest drivers to a rider's location?" (interview)

---

## Audit notes

**(a) Groups judged already complete — no additions:**
`sd-fundamentals`, `distributed-systems-core`, `oop-fundamentals`, `creational-patterns`,
`structural-patterns`, `behavioral-patterns`, `anti-patterns`, `oo-concurrency`, `lld-in-practice`,
`lld-framework`, `capacity-estimation`, `caching`, `microservices`, `observability`, `geo-distribution`,
`design-security`, `design-in-practice`, `sd-playbook`. These were spot-read in full and already cover
their obvious candidates (including several expert-tier passes with explicit cross-links) — adding more
would pad rather than teach. `capacity-estimation` in particular already drills the "numbers to memorize"
(latency ladder, powers of two) the brief specifically asked to check.

**(b) Considered and deliberately NOT added, with reasoning:**
- *BFF pattern* (microservices) — already a slide in `api-gateway-patterns` (api-design); a dedicated
  topic would restate it.
- *Distributed tracing of a request* (microservices) — fully owned by `distributed-tracing`
  (observability); cross-linked there already.
- *Orchestration vs choreography depth* (microservices) — already a compare slide in both
  `distributed-transactions-and-sagas` and `event-driven-architecture`; sufficient depth for the interview bar.
- *Consumer-driven contract testing* (microservices) — real practice, but it's a testing-mechanics topic,
  not a design decision; better homed in `engineering-craft` (see boundary calls below).
- *Batch/bulk API endpoints* (api-design) — genuine but thinner than webhooks/async/error-contracts;
  didn't clear the "would a candidate really be asked this as its own topic" bar.
- *API auth (keys/OAuth scopes for public APIs)* (api-design) — already covered at the architecture
  level by `designing-authentication-and-sessions` (design-security) and one slide in
  `api-gateway-patterns`; a third pass would be redundant.
- *Queue-based load leveling as its own resilience topic* — the pattern is already taught (just not
  by that name) via `messaging-fundamentals`'s "what async buys you" slide plus
  `backpressure-and-dead-letter-handling`; naming it again would duplicate, not add.
- *Fallback design* (resilience) — already the spine of `graceful-degradation-and-load-shedding`.
- *Health checks vs deep checks* — covered twice already (a pitfall slide in `health-checks-and-failover`,
  a slide in `designing-for-observability`); cumulative coverage is sufficient.
- *RED/USE method by name* (observability) — the content is already taught as Google's "golden signals"
  in `designing-for-observability`; RED/USE is the same idea under a different label, not new content.
- *Leader election vs consensus split* (consistency-replication) — `consensus-basics` already frames
  leader election as one consensus application, and `distributed-coordination` (distributed-systems-core)
  covers lease-based election without full consensus; the split is already visible across the two, cross-linked.
- *Generics/variance in design* (oop-fundamentals) — one slide already exists in `polymorphism`; deeper
  generics/variance mechanics are language-specific and belong to `languages-compilers`, not this area.
- *Multi-model databases* (storage-scale) — `polyglot-persistence` already covers combining stores;
  a single-engine-multi-model topic would mostly restate the same trade-off from the other side.
- *Stream/table duality* (messaging-streaming) — genuinely niche; it's a Kafka Streams/KSQL framework
  detail more than a system-design interview topic. Skipped on the value filter.
- *Exactly-once end-to-end pipelines* (messaging-streaming) — `message-delivery-semantics` and
  `idempotency-and-exactly-once` (distributed-systems-core) already cover the idempotency-based answer;
  a third pass narrows to a framework-specific detail (Kafka transactions) not worth its own topic here.

**(c) Topics recommended for a SPLIT (carrying too much for one topic):**
- None identified in the existing brief. Every existing Topic reviewed stays within a coherent single
  claim; the brief has clearly already been through a "don't restate, cross-link instead" pass, and
  splitting further would fragment rather than clarify. (New additions above were sized 7-9 slides each
  to stay within the same house shape, not accidentally re-introduce this problem.)

**(d) Cross-area boundary calls surfaced during this audit:**
- *Consumer-driven contract testing* (flagged in (b)) — recommend `engineering-craft`, alongside its
  existing ownership of DDD/testing mechanics, not `system-design`'s `microservices`.
- *Chaos engineering tooling* (game-day runbooks, fault-injection platforms like a Chaos Monkey
  equivalent) — the new `chaos-engineering-and-fault-injection` topic here is deliberately the
  design-time discipline/principles only; hands-on tooling and on-call/runbook mechanics stay
  `cloud-devops-sre`'s territory, per the pattern already set by `observability`'s existing boundary note.
- *ER diagrams / entity-relationship modeling notation* — considered for the `uml` group given its
  thinness, but recommend it stays with `databases` (schema design is that area's territory); added
  UML state/activity diagrams instead, which are LLD-object-model notation, not data-model notation.
- *Incident-driven design / postmortems shaping future design decisions* — considered for `observability`;
  recommend `cloud-devops-sre` (incident response ownership), not duplicated here.
