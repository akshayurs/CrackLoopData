# HLD Interview Question Bank

New material for the `system-design` Study Area: a dedicated question-bank layer for high-level-design
interview questions, one Topic per real interview question (not a slide buried inside a concept Topic).
These Topics teach **answering**, not the underlying concept — each cross-links to the concept Topic in
`briefs/expanded/system-design.md` that already teaches the theory, and to `sd-playbook` for the general
method. All slugs are prefixed `iv-` and were checked against every slug in `briefs/parts/_existing-slugs.txt`
— no collisions found (no existing slug uses the `iv-` prefix).

---

## Group: HLD Fundamentals — Interview Questions (interview-hld-fundamentals)
*applying scale, latency/throughput, availability, CAP, statefulness, and NFR elicitation to a live design question*

### Topic: How would you scale this system to handle 10x traffic? (iv-scale-to-10x, intermediate)
The most common opening deep-dive: probes whether you reach for "add more servers" or actually reason about which layer breaks first. Learner walks away able to name the bottleneck order (DB → cache → app → LB) and speak to each.
- The question as asked, and what "10x" is really testing (overview)
- Clarifying questions first: 10x of what — traffic, data, or both? Sudden or gradual? (concept)
- The answer skeleton: identify the bottleneck, scale that layer, repeat (concept)
- Walking it: read replicas, then cache, then horizontal app scaling, then re-check the DB (concept)
- Diagram: a scaling path — each layer's ceiling and what breaks it (diagram)
- Follow-up: "what if it's 100x, not 10x?" — when horizontal stops working (concept)
- Pitfall: answering "just add more servers" without saying which layer (pitfall)
- The 60-second version (concept)
- cross-link: scalability-fundamentals

### Topic: How do you decide between optimizing for latency vs throughput? (iv-latency-vs-throughput-tradeoff, intermediate)
Probes whether you understand these are often in tension, not both maximizable, and can pick correctly for a stated use case. Learner walks away with a decision rule tied to user-facing vs batch workloads.
- The question as asked, and the tension it's probing (overview)
- Clarifying questions: is this a user-facing request path or a background/batch job? (concept)
- The answer skeleton: name the SLA that matters, then optimize for that one (concept)
- Walking it: batching increases throughput but hurts tail latency — a concrete queue example (concept)
- Walking it: request coalescing and its latency cost vs its throughput win (concept)
- Follow-up: "the interviewer says both matter equally — now what?" (concept)
- Pitfall: treating "faster" as one dimension instead of naming which one (pitfall)
- The 60-second version (concept)
- cross-link: latency-vs-throughput

### Topic: How would you calculate the availability of this system end-to-end? (iv-availability-math, intermediate)
Tests whether you can chain component availabilities correctly (multiply for serial dependencies, use redundancy math for parallel) instead of quoting "five nines" without doing the arithmetic.
- The question as asked, and why interviewers ask for the actual number (overview)
- Clarifying questions: which components are on the critical path vs optional? (concept)
- The answer skeleton: multiply serial dependencies, apply 1-(1-p)^n for redundant paths (concept)
- Walking it: a worked example — LB (99.99) → app (99.95) → DB (99.9) chained (code)
- Walking it: how adding a redundant replica changes the number (code)
- Follow-up: "which component should you invest in improving first?" (concept)
- Pitfall: quoting "99.99% because that's what everyone says" with no math (pitfall)
- The 60-second version (concept)
- cross-link: availability-and-reliability

### Topic: For this system, would you pick availability or consistency, and why? (iv-cap-tradeoff-for-this-system, advanced)
The applied CAP question — not "explain CAP" but "commit to a side for this specific feature and defend it." Tests judgment, not memorization.
- The question as asked: CAP theory already assumed, now apply it (overview)
- Clarifying questions: which specific operation — read, write, or both — is in scope? (concept)
- The answer skeleton: name the partition scenario, then state your choice and its user-facing cost (concept)
- Walking it: a payments write (choose C) vs a like-counter read (choose A) — concrete contrast (compare)
- Follow-up: "what if the business says both are non-negotiable?" — PACELC and the honest answer (concept)
- Pitfall: reciting "CAP theorem says you can only have two of three" without picking a side (pitfall)
- The 60-second version (concept)
- cross-link: cap-theorem-and-pacelc

### Topic: Would you make this service stateless or stateful, and why? (iv-stateless-vs-stateful-choice, intermediate)
Probes whether you default to stateless (the safe answer) reflexively, or can name the real cases — WebSocket gateways, in-memory session caches — where statefulness is the right call.
- The question as asked, and the "always stateless" trap it's testing for (overview)
- Clarifying questions: does this service hold a live connection or per-request data only? (concept)
- The answer skeleton: default stateless; justify stateful only with a concrete reason (concept)
- Walking it: a WebSocket connection-holding gateway as the stateful counter-example (concept)
- Walking it: sticky sessions as a stateful compromise, and its failover cost (concept)
- Follow-up: "how do you scale the stateful version?" — sharding by connection (concept)
- Pitfall: saying "always stateless" and having no answer for real-time systems (pitfall)
- The 60-second version (concept)
- cross-link: sticky-sessions-and-statelessness

### Topic: Where are the single points of failure in this design, and how would you remove them? (iv-eliminate-single-points-of-failure, intermediate)
A design-review-style probe: can you scan a diagram (yours or the interviewer's) and spot every unreplicated component, not just the obvious ones.
- The question as asked, and why this is often asked right after your first diagram (overview)
- Clarifying questions: none needed — this is a "look at your own diagram" exercise (concept)
- The answer skeleton: walk the diagram left to right, flag anything with a count of one (concept)
- Walking it: the LB, the primary DB, and the "one service that everything calls" as the classic three (diagram)
- Walking it: fixing each — LB pair + VIP, DB replica + failover, and decoupling the hot dependency (concept)
- Follow-up: "which SPOF is cheapest to fix, and which is hardest?" (concept)
- Pitfall: naming the DB as the only SPOF and missing the LB or a shared cache (pitfall)
- The 60-second version (concept)

### Topic: What questions would you ask before designing this system? (iv-nfr-elicitation-deep-dive, intermediate)
The `clarifying-requirements` topic in `sd-playbook` teaches the general method; this Topic drills the specific NFR questions interviewers expect for scale, latency, consistency, and durability before any diagram gets drawn.
- The question as asked, and why interviewers grade the first five minutes hardest (overview)
- The answer skeleton: functional scope, then scale, then latency, then consistency, then durability, in that order (concept)
- Walking it: the exact questions to ask for scale ("DAU? read:write ratio? peak multiplier?") (concept)
- Walking it: the exact questions for consistency and durability ("can we lose data? can we show stale data?") (concept)
- Follow-up: "the interviewer says 'you decide' — what do you assume, and do you say it out loud?" (concept)
- Pitfall: asking questions in a random order instead of a scan that builds toward a diagram (pitfall)
- The 60-second version (concept)
- cross-link: clarifying-requirements

### Topic: Is this system read-heavy or write-heavy, and how does that change your design? (iv-read-heavy-vs-write-heavy, intermediate)
Tests whether the read:write ratio actually changes your architecture (caching, replica count, index strategy) or whether you draw the same diagram regardless of the numbers.
- The question as asked, and the ratio it wants you to reason from (overview)
- Clarifying questions: what's the approximate read:write ratio, and does it vary by time of day? (concept)
- The answer skeleton: read-heavy → cache + replicas; write-heavy → sharding + async writes (concept)
- Walking it: a social feed (100:1 read-heavy) vs a metrics ingestion pipeline (1:100 write-heavy) contrast (compare)
- Follow-up: "the ratio flips during a spike — does your design still hold?" (concept)
- Pitfall: adding a read cache to a write-heavy system because "caching is always good" (pitfall)
- The 60-second version (concept)

---

## Group: Estimation — Interview Questions (interview-hld-estimation)
*QPS, storage, bandwidth, server count, cost, and viral-spike capacity — the back-of-envelope questions asked live*

### Topic: Estimate the QPS this system needs to handle (iv-estimate-qps, intermediate)
The canonical estimation opener. Tests whether you can go from a user count to a number in under a minute, out loud, without a calculator.
- The question as asked, and why interviewers care about the process, not the digit (overview)
- Clarifying questions: DAU, actions per user per day, and peak-to-average ratio (concept)
- The answer skeleton: DAU × actions/day ÷ 86400s = average QPS, then apply a peak multiplier (concept)
- Walking it: a worked example — 50M DAU, 20 actions/day → average and peak QPS (code)
- Walking it: rounding cleanly (86400 ≈ 100k) so the mental math stays fast (concept)
- Follow-up: "how does peak QPS change your load balancer and instance count?" (concept)
- Pitfall: computing average QPS and never mentioning peak (pitfall)
- The 60-second version (concept)
- cross-link: traffic-estimation-qps

### Topic: Estimate how much storage this system needs over 5 years (iv-estimate-storage, intermediate)
Tests whether you can size one record correctly, multiply by volume and time, and sanity-check the result against something you already know (a phone's storage, a laptop's disk).
- The question as asked, and the two failure modes it catches — no method, or a wildly wrong sanity check (overview)
- Clarifying questions: size per record, write rate, and retention period (concept)
- The answer skeleton: bytes/record × records/day × 365 × years, then add a replication factor (concept)
- Walking it: a worked example — a chat message system, 500 bytes/message, at scale (code)
- Walking it: accounting for metadata, indexes, and replicas on top of raw data (concept)
- Follow-up: "how would you reduce this if it's too expensive?" — TTL, cold storage tiers, compression (concept)
- Pitfall: forgetting the replication factor and understating cost by 3x (pitfall)
- The 60-second version (concept)
- cross-link: storage-estimation

### Topic: Estimate the bandwidth/network cost for this system (iv-estimate-bandwidth, intermediate)
Tests whether you can connect QPS and payload size into a bandwidth number, and spot which direction (ingress or egress) actually dominates cost.
- The question as asked, and why bandwidth is the estimate people skip (overview)
- Clarifying questions: payload size per request, and is this read-heavy (egress-dominated) or write-heavy (ingress-dominated)? (concept)
- The answer skeleton: QPS × payload size = bandwidth, separately for ingress and egress (concept)
- Walking it: a worked example — a video platform's egress bandwidth at peak (code)
- Follow-up: "how would a CDN change this number?" — moving egress off origin (concept)
- Pitfall: computing one combined number instead of separating ingress from egress (pitfall)
- The 60-second version (concept)
- cross-link: bandwidth-and-bottleneck-estimation

### Topic: How many servers would you need to serve this load? (iv-estimate-servers-needed, intermediate)
Tests whether you can turn a QPS number into a server count using a stated per-server capacity, and reason about headroom instead of sizing to exactly 100%.
- The question as asked, and the per-server capacity assumption it expects you to state (overview)
- Clarifying questions: what's a reasonable QPS-per-instance for this workload — CPU-bound or I/O-bound? (concept)
- The answer skeleton: peak QPS ÷ QPS-per-server, then add headroom for failover (concept)
- Walking it: a worked example — 50k peak QPS, 2k QPS/server → server count with N+2 redundancy (code)
- Follow-up: "how does autoscaling change this — do you still need a fixed number?" (concept)
- Pitfall: sizing to exactly the peak with zero headroom for a node failing (pitfall)
- The 60-second version (concept)

### Topic: Roughly what would this system cost to run per month? (iv-estimate-infra-cost, advanced)
A senior-signal estimation question — tests whether you can translate compute/storage/bandwidth estimates into a dollar figure, showing cost-awareness, not just capacity math.
- The question as asked, and why this gets asked at senior+ levels specifically (overview)
- Clarifying questions: cloud provider assumed, and is this steady-state or including the spike? (concept)
- The answer skeleton: cost = compute + storage + bandwidth + managed-service premium, summed separately (concept)
- Walking it: a worked example — instance-hours, storage GB-month, and egress GB priced roughly (code)
- Follow-up: "what's the single biggest lever to cut this cost in half?" (concept)
- Pitfall: giving a precise-looking number ("$47,382/month") instead of an order of magnitude (pitfall)
- The 60-second version (concept)
- cross-link: cost-and-org-aware-design

### Topic: How would you plan capacity for a sudden viral spike? (iv-capacity-for-viral-event, advanced)
Tests whether you can reason about a 50-100x transient spike differently from steady 10x growth — pre-provisioning, autoscaling limits, and what degrades gracefully instead of falling over.
- The question as asked, and how it differs from the steady-growth scaling question (overview)
- Clarifying questions: is the spike predictable (a scheduled launch) or truly sudden (going viral)? (concept)
- The answer skeleton: pre-provision for predictable spikes; for sudden ones, rely on autoscaling plus load shedding (concept)
- Walking it: a worked example — a ticket-drop event, provisioned 20x ahead of the on-sale time (concept)
- Walking it: what sheds first when autoscaling can't keep up — feature flags, queueing, degraded responses (concept)
- Follow-up: "autoscaling takes 5 minutes to add capacity — what covers you until then?" (concept)
- Pitfall: assuming autoscaling alone handles any spike size, with no plan for the gap (pitfall)
- The 60-second version (concept)
- cross-link: graceful-degradation-and-load-shedding

### Topic: How big should the cache be for this system? (iv-estimate-cache-size, intermediate)
Tests whether you can size a cache from the working set (hot data), not the full dataset, and justify the number against a hit-rate target.
- The question as asked, and the working-set-vs-full-dataset distinction it's probing (overview)
- Clarifying questions: what's the access pattern — is 80% of traffic hitting 20% of keys? (concept)
- The answer skeleton: estimate the hot working set size, not total data size, and target a hit rate (concept)
- Walking it: a worked example — sizing a cache for the hot 20% of a product catalog (code)
- Follow-up: "how do you verify the hit rate in production once it's live?" (concept)
- Pitfall: sizing the cache to hold all the data "to be safe" (pitfall)
- The 60-second version (concept)
- cross-link: caching-fundamentals

### Topic: How do you sanity-check a back-of-envelope estimate in the room? (iv-sanity-check-your-numbers, intermediate)
The meta-question: after producing a number, can you tell if it's plausible — comparing it to a known reference point instead of moving on and hoping it's right.
- The question as asked, and why interviewers probe this after any estimate (overview)
- The answer skeleton: compare against a reference you already know — a known company's scale, a familiar disk size (concept)
- Walking it: "50 PB sounds like a lot — is it? Compare to a known large-scale dataset" (concept)
- Walking it: catching an off-by-1000 error from a unit mix-up (KB vs MB vs GB) (pitfall)
- Follow-up: "your number implies 10,000 servers — does that pass the smell test for this company's size?" (concept)
- Pitfall: presenting a number with false precision and no sanity check at all (pitfall)
- The 60-second version (concept)
- cross-link: estimation-in-the-interview

---

## Group: Caching — Interview Questions (interview-hld-caching)
*what/where to cache, invalidation, stampede, cache-DB consistency, CDN scope, eviction choice, and hot keys*

### Topic: What would you cache in this system, and what would you never cache? (iv-what-to-cache, intermediate)
Tests judgment, not the definition of caching — can you name specific fields/endpoints to cache and specific ones (balances, anything requiring strong consistency) you'd deliberately leave uncached.
- The question as asked, and the "cache everything" reflex it's testing against (overview)
- Clarifying questions: which reads are hot and tolerant of staleness, and which must always be fresh? (concept)
- The answer skeleton: cache hot + slow-changing + read-heavy data; skip anything requiring strong consistency (concept)
- Walking it: a user profile (cache it) vs an account balance (don't) — concrete contrast (compare)
- Follow-up: "what if product wants the balance to feel instant too?" — cache with a short TTL and a visible staleness signal (concept)
- Pitfall: caching a financial or inventory count "for speed" with no staleness plan (pitfall)
- The 60-second version (concept)
- cross-link: caching-fundamentals

### Topic: Where should the cache live — client, CDN, app layer, or DB layer? (iv-where-to-cache, intermediate)
Tests whether you can place a cache at the right layer for the specific data, instead of defaulting to "we'll add Redis."
- The question as asked, and the four layers it expects you to know (overview)
- Clarifying questions: is this data static assets, personalized data, or a shared computed result? (concept)
- The answer skeleton: static → CDN/client; shared computed → app-layer distributed cache; per-row lookups → DB buffer/cache (concept)
- Walking it: a worked example — a product page's images (CDN), price (app cache), and inventory count (DB) (diagram)
- Follow-up: "what changes if the user base is global?" — edge caching and regional cache tiers (concept)
- Pitfall: putting everything in one Redis cluster regardless of access pattern (pitfall)
- The 60-second version (concept)

### Topic: How would you invalidate this cache when the underlying data changes? (iv-cache-invalidation-strategy, advanced)
The classic "there are only two hard problems" question — tests whether you can pick and defend a concrete invalidation strategy for the specific data, not just name that invalidation is hard.
- The question as asked, and why "cache invalidation is hard" isn't an answer by itself (overview)
- Clarifying questions: can this data tolerate a short staleness window, or must it invalidate immediately? (concept)
- The answer skeleton: pick TTL, write-through invalidation, or event-driven invalidation, and justify against the staleness tolerance (concept)
- Walking it: TTL-only for tolerant data vs explicit delete-on-write for a user's own profile (compare)
- Walking it: event-driven invalidation via a change stream for fan-out caches (concept)
- Follow-up: "two app instances update the same key milliseconds apart — what happens to the cache?" (concept)
- Pitfall: relying on TTL alone for data users expect to see updated immediately (pitfall)
- The 60-second version (concept)
- cross-link: cache-invalidation

### Topic: What happens when your cache expires under heavy load, and how do you prevent it? (iv-cache-stampede, advanced)
Tests whether you know the thundering-herd failure mode by its mechanics, not just its name, and can name a concrete fix.
- The question as asked, and the failure it's describing without naming it (overview)
- Clarifying questions: is this one hot key expiring, or a mass expiry across many keys at once? (concept)
- The answer skeleton: name the mechanism (all requests miss at once, all hit the DB at once), then apply a fix (concept)
- Walking it: request coalescing (single-flight) so only one request repopulates the cache (concept)
- Walking it: staggered TTLs with jitter to avoid mass-expiry, plus stale-while-revalidate (concept)
- Follow-up: "the DB is still getting hammered even with coalescing — what else?" — a lock or a probabilistic early refresh (concept)
- Pitfall: describing the symptom (DB overload) without naming the cause (cache miss stampede) (pitfall)
- The 60-second version (concept)

### Topic: How do you keep the cache consistent with the database? (iv-cache-db-consistency, advanced)
Tests whether you can reason about the actual race conditions in cache-aside vs write-through patterns, not just name the pattern.
- The question as asked, and the write-then-read race it's really asking about (overview)
- Clarifying questions: cache-aside, write-through, or write-behind — which pattern is already in play? (concept)
- The answer skeleton: name the pattern, then walk the specific race window it leaves open (concept)
- Walking it: cache-aside's classic race — delete cache, then a concurrent read repopulates stale data (diagram)
- Walking it: the fix — delete-after-write with a short delay, or versioned cache entries (concept)
- Follow-up: "how would you detect this drift is actually happening in production?" (concept)
- Pitfall: assuming cache-aside is automatically consistent because it "invalidates on write" (pitfall)
- The 60-second version (concept)
- cross-link: cache-read-write-patterns

### Topic: What would you put behind a CDN, and what wouldn't you? (iv-cdn-what-and-when, intermediate)
Tests scope: CDNs are for cacheable, publicly shareable content — can you draw that line correctly for personalized or write-heavy paths.
- The question as asked, and the "just CDN it" reflex it's testing (overview)
- Clarifying questions: is this content the same for every user, or personalized per request? (concept)
- The answer skeleton: CDN for static/shared/cacheable GETs; origin for personalized, write, or auth-gated requests (concept)
- Walking it: images and JS bundles (CDN) vs a personalized dashboard API response (origin) (compare)
- Follow-up: "can you CDN a mostly-static page that has one personalized widget?" — edge includes / fragment caching (concept)
- Pitfall: trying to CDN an authenticated, per-user API response directly (pitfall)
- The 60-second version (concept)
- cross-link: cdn-and-edge-caching

### Topic: Which eviction policy would you choose for this cache, and why? (iv-eviction-policy-choice, intermediate)
Tests whether you can match an eviction policy to an actual access pattern instead of defaulting to "LRU, obviously."
- The question as asked, and why "LRU" isn't automatically the right answer (overview)
- Clarifying questions: is access recency- or frequency-driven — do the same few keys dominate, or does recency matter more? (concept)
- The answer skeleton: LRU for recency-driven access; LFU for a stable hot set; TTL for time-bound relevance (concept)
- Walking it: a trending-content cache where LFU beats LRU because recency is a poor proxy (compare)
- Follow-up: "how would you verify your choice was right after shipping it?" — hit-rate monitoring (concept)
- Pitfall: picking LRU by default without checking whether the access pattern actually fits it (pitfall)
- The 60-second version (concept)
- cross-link: eviction-policies

### Topic: One key is getting 100x the traffic of others — how do you handle it? (iv-hot-key-problem, advanced)
The hot-key/hot-partition-at-the-cache-layer question — tests whether you can go beyond "add more cache nodes" since a single key can't be sharded across nodes trivially.
- The question as asked, and why simply adding nodes doesn't fix a single hot key (overview)
- Clarifying questions: is this a celebrity-user pattern, a viral post, or a misbehaving client retrying? (concept)
- The answer skeleton: detect the hot key, then replicate it locally or split it, don't just scale the cluster (concept)
- Walking it: local (in-process) caching of the hot key on top of the distributed cache (concept)
- Walking it: key splitting — sharding one logical key into N physical keys and merging on read (concept)
- Follow-up: "how do you even detect a hot key before it takes down the node?" (concept)
- Pitfall: adding more cache nodes and being surprised the hot node is still overloaded (pitfall)
- The 60-second version (concept)

---

## Group: Data at Scale — Interview Questions (interview-hld-data)
*SQL vs NoSQL, sharding key choice, resharding, hot partitions, index design, polyglot persistence, blob vs DB, cross-service transactions*

### Topic: Would you use SQL or NoSQL for this system, and why? (iv-sql-vs-nosql-choice, intermediate)
Tests whether you pick based on the actual access pattern and consistency needs of this system, not personal preference or "NoSQL scales better" as a slogan.
- The question as asked, and the slogan-answer trap it's checking for (overview)
- Clarifying questions: what are the query patterns — joins and transactions, or key-based lookups at huge scale? (concept)
- The answer skeleton: name the query pattern, consistency need, and scale target, then pick accordingly (concept)
- Walking it: an order system needing multi-table transactions (SQL) vs a session store needing raw key lookups at scale (compare)
- Follow-up: "could you start on SQL and migrate to NoSQL later — what would that cost you?" (concept)
- Pitfall: saying "NoSQL scales better" without naming which scaling dimension SQL actually struggles with (pitfall)
- The 60-second version (concept)
- cross-link: sql-vs-nosql-at-scale

### Topic: How would you choose the sharding key for this data? (iv-choosing-a-sharding-key, advanced)
Tests whether you can evaluate a specific key against query patterns and skew risk, rather than picking the obvious ID column by default.
- The question as asked, and why "shard by user ID" isn't automatically right (overview)
- Clarifying questions: what's the most common query — by user, by time, by geography? (concept)
- The answer skeleton: pick the key that keeps the most common query within one shard and avoids skew (concept)
- Walking it: sharding a chat app by conversation ID vs by user ID — which queries stay single-shard (compare)
- Follow-up: "your chosen key causes a skew for one power user — now what?" (concept)
- Pitfall: sharding by a monotonically increasing ID or timestamp and creating a hot last shard (pitfall)
- The 60-second version (concept)
- cross-link: partitioning-and-sharding

### Topic: How would you reshard this database as it grows, without downtime? (iv-resharding-without-downtime, advanced)
Tests whether you know the actual mechanics of live resharding — dual-writes, background migration, cutover — not just that resharding is "hard."
- The question as asked, and why "add more shards" undersells the difficulty (overview)
- Clarifying questions: is this a planned rebalance or a reaction to an already-hot shard? (concept)
- The answer skeleton: dual-write to old and new layout, backfill in the background, cut over, then stop dual-writing (concept)
- Diagram: the resharding timeline — dual-write, backfill, verify, cutover, cleanup (diagram)
- Follow-up: "how do you verify the new shard layout is correct before cutting over?" (concept)
- Pitfall: doing a big-bang migration that requires taking writes offline (pitfall)
- The 60-second version (concept)
- cross-link: resharding-and-hotspots

### Topic: One shard is getting way more traffic than the others — what do you do? (iv-hot-partition-fix, advanced)
The applied hot-partition question — distinguishes a hot-key problem (one row) from a hot-shard problem (bad key design), and tests whether you can tell the two apart before proposing a fix.
- The question as asked, and how to tell a hot shard from a hot key inside it (overview)
- Clarifying questions: is the whole shard hot, or one key on it, evenly spread traffic just landing on a small shard count? (concept)
- The answer skeleton: diagnose which of the three, then split the shard, split the key, or add virtual shards (concept)
- Walking it: virtual/consistent hashing to spread a hot range across more physical nodes (concept)
- Follow-up: "the hot shard is hot because of one celebrity account — does resharding even help?" (concept)
- Pitfall: resharding the whole dataset when the real problem is one hot key on one shard (pitfall)
- The 60-second version (concept)
- cross-link: resharding-and-hotspots

### Topic: How would you design indexes for this table at scale? (iv-index-design-at-scale, intermediate)
Tests whether you can name the specific indexes a query pattern needs and their write-cost trade-off, not just say "add an index."
- The question as asked, and the write-amplification cost it expects you to weigh (overview)
- Clarifying questions: what are the top 2-3 query patterns this table needs to serve fast? (concept)
- The answer skeleton: index the columns in your actual WHERE/ORDER BY clauses; every index is a write cost (concept)
- Walking it: a composite index ordering decision for a two-column filter (code)
- Follow-up: "you now have 8 indexes on this table — what's that costing you on writes?" (concept)
- Pitfall: indexing every column "just in case" instead of matching indexes to real queries (pitfall)
- The 60-second version (concept)

### Topic: Would you use one database for everything, or different databases for different parts? (iv-polyglot-persistence-choice, advanced)
Tests whether you can justify splitting storage by workload (search index, graph, blob, relational) instead of defaulting to one database for operational simplicity.
- The question as asked, and the simplicity-vs-fit trade-off it's probing (overview)
- Clarifying questions: which parts of this system have genuinely different access patterns — search, relationships, time-series? (concept)
- The answer skeleton: split storage only where the access pattern is genuinely different; justify each addition against its ops cost (concept)
- Walking it: a social app needing a relational store for accounts, a graph store for the follow graph, and a search index for posts (diagram)
- Follow-up: "three databases means three things to operate — how do you justify that to your team?" (concept)
- Pitfall: reaching for a specialized database for every feature without weighing the operational cost (pitfall)
- The 60-second version (concept)
- cross-link: polyglot-persistence

### Topic: Where do you draw the line between storing something in the DB vs blob storage? (iv-blob-vs-db, intermediate)
Tests whether you know why large binary objects don't belong in a relational row, and can name the reference-plus-blob pattern.
- The question as asked, and the "just put it in a column" mistake it's testing against (overview)
- Clarifying questions: what's the size and access pattern of this object — small structured data, or a large binary file? (concept)
- The answer skeleton: structured/queryable/small → DB; large/binary/rarely-queried → blob store with a DB reference (concept)
- Walking it: storing a user's avatar URL in the DB row, the image bytes in object storage (concept)
- Follow-up: "what if you need to query metadata about the blob, like its upload date?" — store metadata in DB, bytes in blob store (concept)
- Pitfall: storing images or PDFs as BLOBs directly in relational rows at scale (pitfall)
- The 60-second version (concept)
- cross-link: object-and-blob-storage

### Topic: How do you keep data consistent when a transaction spans multiple services? (iv-transactions-across-services, advanced)
Tests whether you know that distributed transactions across service boundaries need a saga or 2PC-style pattern, and can pick the right one with its trade-off.
- The question as asked, and why a normal DB transaction can't reach across services (overview)
- Clarifying questions: does this need strict atomicity, or is eventual consistency with compensation acceptable? (concept)
- The answer skeleton: name the saga pattern (orchestration or choreography) and its compensating actions (concept)
- Walking it: an order-payment-inventory saga with a compensating refund step if inventory fails (diagram)
- Follow-up: "what if the compensating action itself fails?" — retries, dead-letter, and manual reconciliation (concept)
- Pitfall: reaching for two-phase commit across services and underestimating its availability cost (pitfall)
- The 60-second version (concept)
- cross-link: distributed-transactions-and-sagas

---

## Group: Consistency & Replication — Interview Questions (interview-hld-consistency)
*consistency model choice, replication lag, read-your-writes, quorum tuning, conflict resolution, idempotency, distributed transactions*

### Topic: What consistency model would you choose for this system, and why? (iv-choosing-consistency-model, advanced)
Tests whether you can pick strong, eventual, or causal consistency for a specific stated feature and defend the user-facing consequence, not just define the terms.
- The question as asked, and why naming the models isn't the same as choosing one (overview)
- Clarifying questions: which specific operation is being asked about — this system likely needs more than one model (concept)
- The answer skeleton: pick per-feature, not system-wide; state the user-visible cost of your choice (concept)
- Walking it: strong consistency for a bank balance, eventual for a view counter, causal for a comment thread (compare)
- Follow-up: "the product team wants everything to feel instant AND always correct — what do you tell them?" (concept)
- Pitfall: picking one consistency model for the entire system instead of per feature (pitfall)
- The 60-second version (concept)
- cross-link: consistency-models

### Topic: Replication lag just spiked — what breaks, and how do you defend against it? (iv-replication-lag-impact, advanced)
Tests whether you can name concrete failure symptoms of replication lag (stale reads, phantom disappearing data) and a real mitigation, not just "replicas can lag."
- The question as asked, and the vague "replicas can be stale" non-answer it's testing against (overview)
- Clarifying questions: are reads going to replicas at all, or only writes — where does lag actually surface? (concept)
- The answer skeleton: name the user-visible symptom, then the mitigation — read-after-write routing, lag monitoring, replica health checks (concept)
- Walking it: a user posts a comment, refreshes, and it's gone because the read hit a lagging replica (diagram)
- Follow-up: "how would you even detect that lag has grown, before users complain?" (concept)
- Pitfall: assuming replication lag is milliseconds and never budgeting for a multi-second spike (pitfall)
- The 60-second version (concept)
- cross-link: synchronous-vs-asynchronous-replication

### Topic: How would you guarantee a user sees their own write immediately? (iv-read-your-own-writes, advanced)
The read-your-writes question — tests whether you know concrete techniques (sticky reads to primary, session tokens, client-side caching) beyond "use strong consistency everywhere."
- The question as asked, and why "just use strong consistency" is too broad an answer (overview)
- Clarifying questions: does this need to hold only for the writing user, or for every reader? (concept)
- The answer skeleton: route the writer's own subsequent reads to the primary (or a replica known to be caught up) (concept)
- Walking it: a session-pinning approach — reads within the same session go to primary for a short window (concept)
- Walking it: an alternative — the client optimistically renders its own write locally, then reconciles (concept)
- Follow-up: "what if the user switches devices right after writing?" (concept)
- Pitfall: applying strong consistency to all reads system-wide just to fix this one case (pitfall)
- The 60-second version (concept)
- cross-link: consistency-models

### Topic: How would you tune read/write quorum for this system's needs? (iv-tuning-quorum, advanced)
Tests whether you can reason about the R+W>N trade-off for a specific latency/consistency target, not just recite the formula.
- The question as asked, and the formula it expects you to actually apply, not just state (overview)
- Clarifying questions: does this workload favor read latency, write latency, or strict consistency? (concept)
- The answer skeleton: pick R and W relative to N based on which side needs to be fast vs which needs to be safe (concept)
- Walking it: a worked example — N=3, W=1/R=3 for write-optimized vs W=3/R=1 for read-optimized, and R=W=2 as the balanced default (code)
- Follow-up: "a node is down — does your quorum setting still work?" (concept)
- Pitfall: setting R+W=N (not > N) and losing the strong-consistency guarantee without realizing it (pitfall)
- The 60-second version (concept)
- cross-link: quorum-systems

### Topic: Two replicas got different writes for the same key — how do you resolve the conflict? (iv-conflict-resolution-choice, advanced)
Tests whether you can pick and justify a concrete conflict-resolution strategy (LWW, vector clocks, CRDTs, app-level merge) for the specific data type in question.
- The question as asked, and why "last write wins" isn't always the right default (overview)
- Clarifying questions: what does this data represent — is a silent overwrite acceptable, or does the merge itself matter? (concept)
- The answer skeleton: name the strategy that fits the data's semantics, not a system-wide default (concept)
- Walking it: LWW losing a legitimate concurrent edit vs a CRDT merging a shopping cart correctly (compare)
- Follow-up: "how would you even detect that a conflict happened, if resolution is automatic?" (concept)
- Pitfall: applying last-write-wins to data where silently dropping one write is actually a bug, like inventory counts (pitfall)
- The 60-second version (concept)
- cross-link: conflict-resolution

### Topic: How would you make this API endpoint safe to retry? (iv-idempotency-in-practice, intermediate)
Tests whether you can implement idempotency concretely — an idempotency key, a dedup table — not just say "make it idempotent."
- The question as asked, and why "just make it idempotent" needs a mechanism to back it up (overview)
- Clarifying questions: is the risk client retries, at-least-once delivery from a queue, or both? (concept)
- The answer skeleton: client generates an idempotency key, server stores it with the result, and dedupes on retry (concept)
- Walking it: a worked example — a payment endpoint using a client-generated request ID stored for 24h (code)
- Follow-up: "what if the first request is still in flight when the retry arrives?" — lock the key while processing (concept)
- Pitfall: relying on the operation being "naturally idempotent" (like a PUT) when it has side effects that aren't (pitfall)
- The 60-second version (concept)
- cross-link: idempotency-and-exactly-once

### Topic: Would you use a distributed transaction here, or avoid one — and how? (iv-distributed-transaction-tradeoff, expert)
The senior framing of the cross-service consistency question — tests whether you default to avoiding distributed transactions and can justify when (rarely) 2PC is actually worth its availability cost.
- The question as asked, and why the expected default answer is "avoid it" (overview)
- Clarifying questions: how many services are involved, and is atomicity truly required or just eventual correctness? (concept)
- The answer skeleton: prefer sagas/compensation by default; justify 2PC only for a small, tightly-coupled, low-latency set of participants (concept)
- Walking it: why 2PC's blocking coordinator becomes a new availability bottleneck at scale (concept)
- Follow-up: "the business insists on 'no partial state, ever' — how do you push back or accommodate it?" (concept)
- Pitfall: reaching for 2PC as the first idea instead of the last resort (pitfall)
- The 60-second version (concept)
- cross-link: distributed-transactions-and-sagas

### Topic: For this specific feature, would you pick strong or eventual consistency? (iv-strong-vs-eventual-for-this-feature, advanced)
A narrower, feature-scoped rerun of the consistency-model question — forces a binary commitment with a concrete cost, used as a rapid-fire follow-up drill across several small features in one interview.
- The question as asked, and why interviewers ask this rapid-fire across several small features (overview)
- Clarifying questions: what's the cost of showing stale data here, in concrete user terms? (concept)
- The answer skeleton: state the user-visible cost of being wrong in each direction, then commit (concept)
- Walking it: rapid-fire across three features — follower count (eventual), payment status (strong), typing indicator (eventual) (compare)
- Follow-up: "you said eventual for follower count — how eventual? Seconds? Minutes?" (concept)
- Pitfall: giving the theoretically "safer" answer (strong) for everything to avoid being wrong (pitfall)
- The 60-second version (concept)
- cross-link: consistency-models

---

## Group: Messaging & Streaming — Interview Questions (interview-hld-messaging)
*when to use a queue, exactly-once, ordering, Kafka vs queue, backpressure, event-driven vs request-response, replay/reprocessing*

### Topic: When would you put a queue between these two services, and when wouldn't you? (iv-when-to-use-a-queue, intermediate)
Tests whether you can justify decoupling with a queue against a concrete need (absorbing bursts, surviving downstream outages) rather than inserting one reflexively.
- The question as asked, and the "queues are always good practice" reflex it's testing (overview)
- Clarifying questions: does the caller need an immediate response, or can the work happen asynchronously? (concept)
- The answer skeleton: queue when the caller doesn't need a synchronous result, or needs to survive downstream being slow/down (concept)
- Walking it: an email-send step (queue it) vs a price check needed for the response itself (don't) (compare)
- Follow-up: "the caller now needs to know if the async job succeeded — how do you tell them?" (concept)
- Pitfall: adding a queue to a synchronous request/response path and creating a polling problem instead (pitfall)
- The 60-second version (concept)
- cross-link: queues-vs-pubsub

### Topic: How would you actually achieve exactly-once processing here? (iv-exactly-once-in-practice, advanced)
Tests whether you know exactly-once is really at-least-once-delivery plus idempotent processing, not a delivery guarantee the broker gives you for free.
- The question as asked, and the misconception that a broker setting alone provides this (overview)
- Clarifying questions: is duplication a delivery-layer risk, a processing-layer risk, or both? (concept)
- The answer skeleton: accept at-least-once delivery, then make processing idempotent with a dedup key (concept)
- Walking it: a worked example — a payment consumer storing processed message IDs before acting (code)
- Follow-up: "what if the dedup store itself is unavailable when the message arrives?" (concept)
- Pitfall: setting a broker's "exactly-once" config and assuming duplicate processing is now impossible (pitfall)
- The 60-second version (concept)
- cross-link: message-delivery-semantics

### Topic: Does this system need strict ordering, and how would you provide it? (iv-ordering-guarantees-needed, advanced)
Tests whether you can identify which specific data needs ordering (per-key, not global) and name the mechanism (partition key) that provides it without sacrificing all parallelism.
- The question as asked, and the false choice between "totally ordered" and "no order at all" (overview)
- Clarifying questions: does ordering need to hold globally, or just per user/entity? (concept)
- The answer skeleton: per-key ordering via a consistent partition key almost always suffices; global ordering rarely does (concept)
- Walking it: partitioning a Kafka topic by user ID so one user's events stay ordered, across users stay parallel (diagram)
- Follow-up: "a message for a key fails and blocks that partition — what now?" (concept)
- Pitfall: assuming a single-partition topic is required for "ordering" and killing throughput (pitfall)
- The 60-second version (concept)
- cross-link: log-based-streaming

### Topic: Would you use Kafka or a traditional queue (SQS/RabbitMQ) for this? (iv-kafka-vs-traditional-queue, intermediate)
Tests whether the choice is grounded in replay needs and consumer count (Kafka's log model) vs simple task distribution (a queue's delete-on-ack model).
- The question as asked, and the "Kafka is just a better queue" misconception it's testing (overview)
- Clarifying questions: do multiple independent consumers need the same events, and do you need replay? (concept)
- The answer skeleton: Kafka for multi-consumer/replayable event logs; a queue for simple work distribution with delete-on-ack (concept)
- Walking it: a worked example — order-created events needed by 3 different services (Kafka) vs an image-resize task queue (SQS) (compare)
- Follow-up: "your queue-based job now also needs an audit trail of every message — does that change the choice?" (concept)
- Pitfall: picking Kafka by default when there's exactly one consumer and no need to replay (pitfall)
- The 60-second version (concept)

### Topic: Your consumer can't keep up with the producer — what do you do? (iv-handling-backpressure, advanced)
Tests whether you know concrete backpressure mechanisms (buffer-then-shed, slow the producer, scale the consumer) instead of just saying "add more consumers."
- The question as asked, and why "add more consumers" alone doesn't always fix it (overview)
- Clarifying questions: is the bottleneck consumer throughput, or a downstream dependency the consumer calls? (concept)
- The answer skeleton: buffer within limits, then either scale consumers, slow the producer, or shed load — pick based on the cause (concept)
- Walking it: a worked example — a queue depth alarm triggering consumer autoscaling, with a shed-oldest fallback if depth keeps growing (diagram)
- Follow-up: "the producer can't be slowed and consumers can't scale further — now what?" — drop or degrade (concept)
- Pitfall: letting an unbounded queue grow indefinitely instead of applying a depth limit with a shedding policy (pitfall)
- The 60-second version (concept)
- cross-link: backpressure-and-dead-letter-handling

### Topic: Would you make this interaction event-driven or request-response? (iv-event-driven-vs-request-response, intermediate)
Tests whether you can pick based on whether the caller needs an answer now versus just needs the side effect to eventually happen.
- The question as asked, and the coupling trade-off underneath the choice (overview)
- Clarifying questions: does the initiating flow need the result to proceed, or just needs to know the action was accepted? (concept)
- The answer skeleton: request-response when the caller blocks on the result; event-driven when it doesn't (concept)
- Walking it: checkout needing an immediate inventory check (request-response) vs notifying other services an order was placed (event-driven) (compare)
- Follow-up: "how do you debug a chain of five event-driven services when something silently didn't happen?" (concept)
- Pitfall: making everything event-driven and losing the ability to reason about a request's end-to-end outcome (pitfall)
- The 60-second version (concept)
- cross-link: event-driven-architecture

### Topic: A bug corrupted a day of processed events — how do you replay/reprocess safely? (iv-replaying-and-reprocessing, advanced)
Tests whether you can name the mechanics of safe replay — retained log offsets, idempotent consumers, and isolating replay traffic from live traffic.
- The question as asked, and why replay is only safe if you designed for it upfront (overview)
- Clarifying questions: is the log/topic retention long enough to still have that day's events? (concept)
- The answer skeleton: reset consumer offset to before the bug, reprocess through idempotent consumers, isolate replay output from live output (concept)
- Walking it: a worked example — replaying into a shadow table first, diffing against production, then promoting (diagram)
- Follow-up: "what if downstream systems already double-counted from the bad run — do you need to undo anything?" (concept)
- Pitfall: replaying directly into production without idempotent consumers, doubling every side effect (pitfall)
- The 60-second version (concept)

### Topic: A message keeps failing and blocking the queue — how do you handle it? (iv-poison-message-handling, intermediate)
The poison-message question — tests whether you know retry-with-limit plus a dead-letter queue, not just "retry until it works."
- The question as asked, and why infinite retry is itself the failure mode (overview)
- Clarifying questions: is the failure transient (downstream blip) or permanent (malformed message)? (concept)
- The answer skeleton: retry with backoff up to a limit, then move to a dead-letter queue for manual/automated triage (concept)
- Walking it: a worked example — a max-retry count on the consumer, then a DLQ with alerting (code)
- Follow-up: "the DLQ is filling up — how do you decide what to do with those messages?" (concept)
- Pitfall: retrying forever and letting one bad message block every message behind it in the same partition (pitfall)
- The 60-second version (concept)
- cross-link: backpressure-and-dead-letter-handling

---

## Group: APIs & Resilience — Interview Questions (interview-hld-apis-resilience)
*REST vs gRPC vs GraphQL, pagination, versioning, rate limiter design, retry storms, circuit breakers, timeout budgets, graceful degradation*

### Topic: Would you use REST, gRPC, or GraphQL for this API, and why? (iv-rest-vs-grpc-vs-graphql, intermediate)
Tests whether the choice is grounded in the actual caller (browser vs internal service), payload shape, and over/under-fetching concerns, not familiarity alone.
- The question as asked, and the "REST because that's what I know" answer it's testing against (overview)
- Clarifying questions: who's the caller — a browser client, a mobile app, or another internal service? (concept)
- The answer skeleton: REST for public/simple CRUD; gRPC for internal low-latency service-to-service; GraphQL when clients need flexible, varying shapes (concept)
- Walking it: a mobile app with many screens needing different subsets of a user object — GraphQL avoiding over-fetching (compare)
- Follow-up: "what does gRPC cost you that REST doesn't?" — browser support, human-readability, tooling maturity (concept)
- Pitfall: picking GraphQL for a simple internal service-to-service call where it adds needless complexity (pitfall)
- The 60-second version (concept)
- cross-link: grpc-and-protobuf

### Topic: How would you paginate this endpoint at scale? (iv-pagination-strategy-choice, intermediate)
Tests whether you know offset pagination breaks down at scale (skipped/duplicated rows under concurrent writes, slow OFFSET scans) and can name cursor-based pagination as the fix.
- The question as asked, and the offset-pagination problems it's checking you know (overview)
- Clarifying questions: is the underlying data being written to concurrently while users page through it? (concept)
- The answer skeleton: cursor/keyset pagination using a stable sort key, not OFFSET, for anything at scale (concept)
- Walking it: a worked example — paginating by (created_at, id) as a compound cursor (code)
- Follow-up: "a user jumps to page 50 directly — does cursor pagination support that?" — trade-off vs offset (concept)
- Pitfall: using OFFSET/LIMIT on a large, actively-written table and returning skipped or duplicate rows (pitfall)
- The 60-second version (concept)
- cross-link: pagination-strategies

### Topic: How would you version this API without breaking existing clients? (iv-api-versioning-strategy, intermediate)
Tests whether you can name a concrete versioning mechanism (URI, header) and, more importantly, a deprecation process — not just "we'd version it."
- The question as asked, and why "we'd add v2" alone doesn't answer it (overview)
- Clarifying questions: how many external clients exist, and can you force them to upgrade, or must old versions run indefinitely? (concept)
- The answer skeleton: pick a versioning mechanism, then describe the deprecation timeline and how you detect who's still on the old version (concept)
- Walking it: a worked example — URI versioning (/v1, /v2) plus a sunset header and usage telemetry per client (concept)
- Follow-up: "one big customer refuses to migrate off v1 — what do you do?" (concept)
- Pitfall: adding a breaking change to an existing endpoint without bumping the version at all (pitfall)
- The 60-second version (concept)
- cross-link: api-versioning-and-evolution

### Topic: Design a rate limiter for this API (iv-design-a-rate-limiter, advanced)
A deep-dive probe on the algorithm and distributed-counting mechanics behind rate limiting — distinct from the standalone LLD case study, which asks for the full class design; here the focus is choosing and defending an algorithm for a stated API's traffic pattern.
- The question as asked, and how this differs from the LLD version of the same prompt (overview)
- Clarifying questions: per-user, per-IP, or per-API-key; and does the limit need to allow bursts? (concept)
- The answer skeleton: pick an algorithm (token bucket for bursts, sliding window for smoothness), then say where the counter lives (concept)
- Walking it: token bucket vs fixed window vs sliding window log — the burst-handling difference (compare)
- Follow-up: "the limiter itself needs to be distributed across 50 app servers — where does the counter state live?" (concept)
- Pitfall: implementing a fixed window and missing the edge-boundary burst problem (2x limit at the window seam) (pitfall)
- The 60-second version (concept)
- cross-link: rate-limiting-algorithms
- cross-link: distributed-rate-limiting

### Topic: Everyone's retrying at once and now the downstream service is dead — what happened, and how do you prevent it? (iv-retry-storm, advanced)
Tests whether you know retry storms are self-reinforcing (retries add load to an already-struggling service) and can name jittered backoff plus a circuit breaker as the fix.
- The question as asked, and the feedback loop it's describing (overview)
- Clarifying questions: are clients retrying with no backoff, fixed backoff, or already jittered? (concept)
- The answer skeleton: name the feedback loop, then apply exponential backoff with jitter and a circuit breaker to cut retries off (concept)
- Diagram: the retry storm feedback loop — failure causes retries, retries cause more failure (diagram)
- Follow-up: "you fix the clients, but they're deployed slowly — what protects you in the meantime?" — server-side load shedding (concept)
- Pitfall: adding retries to a client without backoff, turning a blip into an outage (pitfall)
- The 60-second version (concept)
- cross-link: retries-timeouts-and-backoff

### Topic: How would you configure a circuit breaker for this dependency? (iv-circuit-breaker-tuning, intermediate)
Tests whether you can pick concrete thresholds (failure rate, open duration, half-open probe count) for a stated dependency, not just say "we'd add a circuit breaker."
- The question as asked, and the specific thresholds it expects you to name (overview)
- Clarifying questions: what's this dependency's normal failure rate, and how costly is a false trip vs a missed trip? (concept)
- The answer skeleton: set a failure-rate threshold to open, a cooldown before half-open, and a probe count before fully closing (concept)
- Walking it: a worked example — open at 50% failure over 20 requests, half-open probe with 5 requests after 30s (code)
- Follow-up: "the breaker is flapping open and closed — what's wrong with the tuning?" (concept)
- Pitfall: setting the threshold so sensitive that normal transient blips trip the breaker constantly (pitfall)
- The 60-second version (concept)
- cross-link: circuit-breakers

### Topic: How do you set timeouts across a call chain so they actually add up? (iv-setting-timeout-budgets, advanced)
Tests whether you understand timeout budgets must decrease down a call chain (each hop leaves room for the next), not be set identically at every layer.
- The question as asked, and the "just set every timeout to 5 seconds" mistake it's testing (overview)
- Clarifying questions: how many hops deep is this call chain, and what's the end-to-end SLA at the top? (concept)
- The answer skeleton: allocate a total budget at the entry point, then divide it down the chain, each hop shorter than its caller (concept)
- Diagram: a 4-hop call chain with a shrinking timeout budget at each layer (diagram)
- Follow-up: "hop 3 times out but hop 1's timeout hasn't expired yet — what does the caller see?" (concept)
- Pitfall: setting the same timeout at every layer, so a deep hop can hang long after the caller gave up (pitfall)
- The 60-second version (concept)

### Topic: This dependency is down — what does the system do instead of failing outright? (iv-graceful-degradation-choice, advanced)
Tests whether you can name a specific fallback for the specific dependency (cached/stale data, a default value, a reduced feature set) rather than a generic "we'd degrade gracefully."
- The question as asked, and the vague non-answer it's testing against (overview)
- Clarifying questions: which dependency, and is its output on the critical path or an enhancement? (concept)
- The answer skeleton: name the concrete fallback for this specific dependency — stale cache, sensible default, or hide the feature (concept)
- Walking it: a recommendations service failing — fall back to a generic "trending" list instead of an empty page (compare)
- Follow-up: "how does the system know to switch back once the dependency recovers?" (concept)
- Pitfall: saying "we'd degrade gracefully" without naming what the fallback actually shows the user (pitfall)
- The 60-second version (concept)
- cross-link: graceful-degradation-and-load-shedding

---

## Group: Operations — Interview Questions (interview-hld-operations)
*detecting failure, SLO negotiation, safe deploys, debugging a p99 spike, capacity planning, on-call design, multi-region failover*

### Topic: How do you know this system is broken before your users tell you? (iv-detecting-its-broken, intermediate)
Tests whether you can name the specific signals (error rate, latency percentiles, saturation) and alert thresholds that catch a problem early, not just "we'd have monitoring."
- The question as asked, and why "we'd have monitoring" alone doesn't satisfy it (overview)
- Clarifying questions: is this about full outages, or gradual degradation too? (concept)
- The answer skeleton: name the golden signals — latency, traffic, errors, saturation — and alert on the ones that predict user pain (concept)
- Walking it: a worked example — alerting on p99 latency and error-rate burn rate, not just "server is up" (concept)
- Follow-up: "your error rate is normal but users are still complaining — what did you miss?" — a client-side or partial-degradation signal (concept)
- Pitfall: alerting only on uptime/health-check pings and missing slow-but-technically-up failures (pitfall)
- The 60-second version (concept)
- cross-link: metrics-and-slis-slos

### Topic: How would you set the SLO for this service? (iv-negotiating-an-slo, advanced)
Tests whether you can negotiate an SLO from actual user impact and error budget math, not pick an arbitrary "five nines" number to sound rigorous.
- The question as asked, and the "just promise 99.99%" trap it's testing against (overview)
- Clarifying questions: what does the business actually lose when this service is degraded for a minute, an hour? (concept)
- The answer skeleton: derive the SLO from user impact and cost of achieving it, then define the error budget it implies (concept)
- Walking it: a worked example — 99.9% SLO implying ~43 minutes/month error budget, and what that buys engineering-wise (code)
- Follow-up: "the business wants 99.99% but that's 10x your current infra cost — what do you say?" (concept)
- Pitfall: promising a stricter SLO than the current architecture can actually support (pitfall)
- The 60-second version (concept)
- cross-link: metrics-and-slis-slos

### Topic: How do you deploy a change to this system without risking an outage? (iv-safe-deploys, intermediate)
Tests whether you can name a concrete rollout mechanism (canary, gradual ramp) plus the metric that gates each step, not just "we'd test it first."
- The question as asked, and why "we test before deploying" doesn't cover production-only failure modes (overview)
- Clarifying questions: is this a stateless service, a stateful one, or a schema change — each needs a different approach (concept)
- The answer skeleton: canary a small percentage, watch the gating metric, ramp up, with a fast rollback path (concept)
- Diagram: a canary rollout with a gate metric and an automatic rollback trigger (diagram)
- Follow-up: "the canary looks fine but the full rollout breaks — what did the canary miss?" (concept)
- Pitfall: deploying to 100% at once because "it passed staging" (pitfall)
- The 60-second version (concept)
- cross-link: rolling-out-a-design

### Topic: p99 latency just spiked — walk me through how you'd debug it (iv-debug-p99-spike, advanced)
The live-debugging probe: tests whether you have a systematic narrowing process (which endpoint, which dependency, which resource) instead of guessing at causes.
- The question as asked, and the "check the logs" non-answer it's testing against (overview)
- Clarifying questions: is this every endpoint or one; did it start suddenly or drift up gradually? (concept)
- The answer skeleton: narrow by endpoint, then by dependency call, then by resource (CPU/GC/lock contention), using tracing at each step (concept)
- Walking it: a worked example — a trace showing time spent in a downstream DB call that itself has a lock wait (diagram)
- Follow-up: "the spike correlates with a deploy 10 minutes earlier — what's your next move?" (concept)
- Pitfall: jumping straight to "scale up the servers" before identifying where the time is actually going (pitfall)
- The 60-second version (concept)
- cross-link: distributed-tracing

### Topic: How would you plan capacity for this service over the next year? (iv-capacity-planning-for-growth, advanced)
Distinct from the estimation-bank's spike question — this is steady, forecasted growth: tests whether you can build a growth-rate-driven plan with lead-time awareness for hardware/licensing, not just react when limits hit.
- The question as asked, and how planned growth differs from a sudden spike (overview)
- Clarifying questions: what's the historical growth rate, and what's the lead time to add capacity (hardware, licenses, approvals)? (concept)
- The answer skeleton: project forward from growth rate, add a buffer for lead time, and set a trigger threshold to act early (concept)
- Walking it: a worked example — 15%/quarter growth projected against current headroom to find the "we need to act by" date (code)
- Follow-up: "growth is not linear — how do you plan for an uncertain forecast?" (concept)
- Pitfall: waiting until you're at 90% utilization to start the capacity conversation with long lead-time infra (pitfall)
- The 60-second version (concept)

### Topic: How would you design the on-call rotation and paging for this system? (iv-designing-oncall, advanced)
Tests whether you think about on-call as a design input (who gets paged for what, how alerts map to ownership) rather than an afterthought bolted on post-launch.
- The question as asked, and why on-call design is asked as a system design question at all (overview)
- Clarifying questions: how many teams/services are involved, and does ownership map cleanly to alerting? (concept)
- The answer skeleton: alerts route to the team that owns the failing component, with clear escalation if unacknowledged (concept)
- Walking it: a worked example — a paging policy with primary/secondary rotation and a 15-minute escalation timer (concept)
- Follow-up: "an alert fires for a shared dependency three teams depend on — who gets paged?" (concept)
- Pitfall: routing every alert to one catch-all on-call person regardless of which component actually failed (pitfall)
- The 60-second version (concept)
- cross-link: alerting-and-on-call-design

### Topic: How would you fail this system over to another region? (iv-multi-region-failover-design, expert)
Tests whether you can name the concrete failover mechanics — data replication lag tolerance, DNS/traffic cutover, and the decision of active-active vs active-passive — for a stated RTO/RPO.
- The question as asked, and the RTO/RPO numbers it expects you to anchor the design to (overview)
- Clarifying questions: what data-loss window (RPO) and downtime window (RTO) is acceptable? (concept)
- The answer skeleton: choose active-active or active-passive based on RTO/RPO, then describe the traffic cutover mechanism (concept)
- Diagram: active-passive failover — replication, health check, DNS/traffic shift, promote (diagram)
- Follow-up: "how do you test this failover works, without waiting for a real outage?" — failover drills (concept)
- Pitfall: claiming "zero RPO, zero RTO" without naming the synchronous-replication cost that requires (pitfall)
- The 60-second version (concept)
- cross-link: geo-routing-and-failover
- cross-link: rpo-rto-and-failover-drills

### Topic: The on-call engineer is getting paged constantly for non-issues — what do you do? (iv-alert-fatigue-fix, intermediate)
Tests whether you can diagnose alert-fatigue causes (wrong thresholds, alerting on causes instead of symptoms) and fix the alerting design, not just tell the engineer to "ignore the noise."
- The question as asked, and why "just tune it out" is the wrong answer (overview)
- Clarifying questions: are the alerts false positives, or true but non-actionable? (concept)
- The answer skeleton: alert on user-facing symptoms, not internal causes; raise thresholds where noise correlates with no real impact (concept)
- Walking it: replacing a per-server CPU alert (noisy, not actionable) with an SLO burn-rate alert (actionable) (compare)
- Follow-up: "you've cut the alert volume in half — how do you know you didn't also cut real signal?" (concept)
- Pitfall: silencing or deprioritizing alerts wholesale instead of fixing what they alert on (pitfall)
- The 60-second version (concept)
- cross-link: alerting-and-on-call-design

---

## Group: Senior/Staff Trade-off Signal — Interview Questions (interview-hld-tradeoffs)
*"what would you do differently," build vs buy, when NOT to use microservices, over-engineering, defending under pushback, migration under load*

### Topic: What would you do differently if you designed this again? (iv-what-would-you-do-differently, expert)
The self-critique question — tests whether you can name a real weakness in your own design unprompted, showing judgment under no pressure, before the interviewer has to find it for you.
- The question as asked, and why volunteering a real weakness scores higher than claiming the design is perfect (overview)
- The answer skeleton: pick a decision you made under uncertainty, name what you'd revisit with more information or time (concept)
- Walking it: a worked example — "I chose eventual consistency for the leaderboard; with more traffic data I'd revisit whether users actually notice the lag" (concept)
- Follow-up: "why didn't you just design it that way from the start?" — defending the original trade-off honestly (concept)
- Pitfall: saying "I wouldn't change anything" or picking a trivial, low-stakes nitpick to avoid real self-critique (pitfall)
- The 60-second version (concept)
- cross-link: staff-level-system-design-signal

### Topic: Would you build this yourself or buy/use a managed service? (iv-build-vs-buy-call, advanced)
Tests whether you weigh differentiation, operational burden, and total cost concretely for the component in question, rather than defaulting to "build" (control) or "buy" (speed) reflexively.
- The question as asked, and the reflexive answer (always build, or always buy) it's testing against (overview)
- Clarifying questions: is this component core to the product's differentiation, or commodity infrastructure? (concept)
- The answer skeleton: buy commodity/undifferentiated pieces; build only where it's core to what makes this product distinct (concept)
- Walking it: buying a managed queue/search service vs building a proprietary recommendation engine (compare)
- Follow-up: "the managed service doesn't support a feature you need — do you still buy it?" (concept)
- Pitfall: defaulting to "build" for everything because "we might need custom behavior someday" (pitfall)
- The 60-second version (concept)
- cross-link: cost-and-org-aware-design

### Topic: When would you NOT use microservices for this? (iv-when-not-microservices, advanced)
Tests whether you can argue against the trendy default and name concrete costs (operational overhead, network hops, distributed debugging) microservices impose on a small team or simple domain.
- The question as asked, and the "microservices are just best practice" assumption it's testing (overview)
- Clarifying questions: what's the team size, and how tightly coupled are the actual business capabilities? (concept)
- The answer skeleton: a monolith wins when the team is small, the domain isn't clearly separable, or low-latency in-process calls matter more than independent deployability (concept)
- Walking it: a 5-person startup choosing a modular monolith over microservices, and what it saves them (concept)
- Follow-up: "the team is now 50 people — has the calculus changed?" (concept)
- Pitfall: adopting microservices for a small team because "that's what big companies do" (pitfall)
- The 60-second version (concept)
- cross-link: monolith-vs-microservices

### Topic: Is this design over-engineered for what's actually needed? (iv-spotting-over-engineering, advanced)
Tests whether you can look at a design (yours or a given one) and identify speculative complexity added for imagined future scale that the stated requirements don't justify.
- The question as asked, and why over-engineering is graded as a real flaw, not just "being thorough" (overview)
- Clarifying questions: which requirements are stated, and which parts of the design serve a requirement no one asked for? (concept)
- The answer skeleton: check every component against a stated requirement; cut anything justified only by "future scale" (concept)
- Walking it: a worked example — event sourcing and CQRS added to a low-write internal admin tool that never needed it (concept)
- Follow-up: "the interviewer says 'but what if we do need that scale later?' — how do you respond?" (concept)
- Pitfall: adding complexity to "future-proof" a design against a scale that isn't in the stated requirements (pitfall)
- The 60-second version (concept)

### Topic: The interviewer disagrees with your design choice — how do you respond? (iv-defending-design-under-pushback, expert)
Tests composure and reasoning under direct challenge — can you either defend the choice with a concrete reason, or genuinely update, without getting defensive or caving reflexively.
- The question as asked, and the two failure modes it's checking for — caving instantly, or refusing to budge (overview)
- The answer skeleton: restate the trade-off you weighed, ask what changed in their framing, then either defend or revise with a stated reason (concept)
- Walking it: a worked example — pushback on "why not just shard by user ID," responding with the specific skew risk you were avoiding (concept)
- Follow-up: "what if the interviewer is right and you missed something?" — updating gracefully without over-apologizing (concept)
- Pitfall: abandoning a well-reasoned choice the moment it's challenged, signaling no real conviction behind it (pitfall)
- The 60-second version (concept)
- cross-link: handling-interviewer-pushback

### Topic: How would you migrate this system to a new architecture while it's serving live traffic? (iv-migrating-under-load, expert)
The hardest applied brownfield question — tests whether you can sequence a live migration (dual-write, shadow traffic, phased cutover) for a system that cannot go down, and name what you'd monitor to know it's safe to proceed at each stage.
- The question as asked, and why "just switch over one weekend" isn't a viable answer at this level (overview)
- Clarifying questions: can any downtime be tolerated at all, and what's the rollback point if the new system misbehaves? (concept)
- The answer skeleton: shadow the new system with live traffic first, then dual-write, then phase reads over, verifying at each gate (concept)
- Diagram: a live migration staged as shadow → dual-write → phased read cutover → decommission old (diagram)
- Follow-up: "the new system's data has drifted from the old one mid-migration — how do you catch that?" (concept)
- Pitfall: cutting over all traffic at once "since testing looked good," with no staged verification (pitfall)
- The 60-second version (concept)
- cross-link: brownfield-system-design

### Topic: What's the question a staff engineer would ask that a mid-level engineer wouldn't think to? (iv-staff-level-followups, expert)
A meta-question testing calibration itself — can you name organizational, cost, and long-horizon questions (ownership, migration cost, blast radius across teams) beyond the technical design.
- The question as asked, and why this is really asking "do you know what you don't know yet" (overview)
- The answer skeleton: name questions about ownership, long-term cost, org boundaries, and reversibility — not more technical detail (concept)
- Walking it: "who owns this once it's live, and what happens when that team's priorities shift?" as a staff-level question (concept)
- Walking it: "how expensive is it to reverse this decision in a year?" as a staff-level question (concept)
- Follow-up: "you named three — which one actually matters most for this specific system?" (concept)
- Pitfall: answering with a deeper technical question instead of an organizational or cost one (pitfall)
- The 60-second version (concept)
- cross-link: staff-level-system-design-signal

### Topic: Two of your requirements conflict — which do you sacrifice, and how do you justify it? (iv-tradeoff-under-conflicting-constraints, expert)
Tests whether you can make and defend an explicit sacrifice under genuinely incompatible constraints (cost vs latency, consistency vs availability) instead of hand-waving that you'll "balance" both.
- The question as asked, and why "we'll balance both" is a non-answer to a genuine conflict (overview)
- Clarifying questions: which constraint was set by the business and which by convention — is either one actually negotiable? (concept)
- The answer skeleton: name both constraints explicitly, state which one you're sacrificing and by how much, and why (concept)
- Walking it: a worked example — a hard cost ceiling vs a hard latency SLA that can't both be met with the given budget (concept)
- Follow-up: "the business says both are truly non-negotiable — what's your actual next move?" — escalate the conflict, don't paper over it (concept)
- Pitfall: describing a "balanced" design that quietly fails one of the two constraints without saying so (pitfall)
- The 60-second version (concept)

---

## Boundary notes

- **`sd-playbook` overlap (kept thin by design):** every Topic here assumes the general interview *method*
  (`the-interview-framework`, `clarifying-requirements`, `driving-the-high-level-design`,
  `deep-dives-and-trade-off-discussions`, `handling-interviewer-pushback`, `staff-level-system-design-signal`)
  is already taught there. Topics like `iv-nfr-elicitation-deep-dive`, `iv-defending-design-under-pushback`,
  `iv-what-would-you-do-differently`, and `iv-staff-level-followups` are the *closest* to `sd-playbook` and
  cross-link into it rather than re-teaching the method — they apply it to a named, scoped question instead.
- **Case-study overlap (`hld-case-studies` / `lld-case-studies`):** `iv-design-a-rate-limiter` sits closest to
  a full case study since `rate-limiter` already exists as an LLD case study — I scoped it to the *algorithm
  and distributed-counter choice* only, not the full class/API design, and flagged it explicitly in its own
  Topic description. `iv-multi-region-failover-design` and `iv-migrating-under-load` are deep-dive probes on
  a *mechanism*, not "design system X" end-to-end prompts — no case-study overlap there, but they're the two
  most case-study-adjacent Topics in the bank and worth a second look.
- **Concept-group overlap (intentional, by design):** every Topic cross-links its underlying concept Topic
  (e.g. `iv-cache-invalidation-strategy` → `cache-invalidation`, `iv-choosing-a-sharding-key` →
  `partitioning-and-sharding`) rather than re-explaining the theory — this was the instructed pattern, not
  an accident, but worth confirming during review that the cross-link targets still match after any renames.
- **Recommendation:** land as-is. The one item I'd want a second pair of eyes on is `iv-design-a-rate-limiter`
  — worth confirming with whoever owns the LLD case-study bank that the split (algorithm choice here vs full
  class design there) is the right line, since it's the single clearest candidate for accidental duplication.
