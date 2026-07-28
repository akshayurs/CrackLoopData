# HLD Interview Question Bank — Part 3a (deepened + expanded)

Deepened + expanded version of 5 groups from `briefs/parts2/iv-hld.md`:
`interview-hld-fundamentals`, `interview-hld-estimation`, `interview-hld-caching`, `interview-hld-data`,
`interview-hld-consistency`. Existing topics keep their slugs/levels but get deeper (11-14 slide) outlines;
new topics (`iv-` prefixed, checked against `briefs/parts/_existing-slugs.txt` and every slug already used
in `iv-hld.md`) fill gaps each group was missing. This file fully supersedes those 5 groups — the other 4
groups (apis-resilience, messaging, operations, tradeoffs) are owned by a different pass and untouched here.

---

## Group: HLD Fundamentals — Interview Questions (interview-hld-fundamentals)
*applying scale, latency/throughput, availability, CAP, statefulness, and NFR elicitation to a live design question*

### Topic: How would you scale this system to handle 10x traffic? (iv-scale-to-10x, intermediate)
The most common opening deep-dive: probes whether you reach for "add more servers" or actually reason about which layer breaks first. Learner walks away able to name the bottleneck order (DB → cache → app → LB) and speak to each.
- The question as asked, and what "10x" is really testing (overview)
- Clarifying questions: 10x of what — traffic, data, or both? Sudden or gradual? (concept)
- The answer skeleton: identify the bottleneck, scale that layer, repeat (concept)
- Walking it: start from the numbers — current QPS and server count, name what breaks first (concept)
- Walking it: read replicas absorb read load, and where they stop helping (concept)
- Walking it: adding a cache layer before adding more app servers (concept)
- Walking it: horizontal app scaling behind the LB, and the stateless assumption it needs (concept)
- Walking it: re-checking the DB after the app layer scales — it's now the new ceiling (concept)
- Diagram: the scaling path — each layer's ceiling and what breaks it (diagram)
- The trade-off to name out loud: horizontal scaling buys capacity but adds coordination and consistency cost (compare)
- Follow-up: "what if it's 100x, not 10x?" — when horizontal stops working and you need to shard (concept)
- Follow-up: "what if the 10x hits only one endpoint, not the whole system?" — targeted scaling (concept)
- Pitfall: answering "just add more servers" without naming which layer or the new bottleneck it creates (pitfall)
- The 60-second version (concept)
- cross-link: scalability-fundamentals

### Topic: How do you decide between optimizing for latency vs throughput? (iv-latency-vs-throughput-tradeoff, intermediate)
Probes whether you understand these are often in tension, not both maximizable, and can pick correctly for a stated use case. Learner walks away with a decision rule tied to user-facing vs batch workloads.
- The question as asked, and the tension it's probing (overview)
- Clarifying questions: is this a user-facing request path or a background/batch job? (concept)
- The answer skeleton: name the SLA that matters, then optimize for that one (concept)
- Walking it: batching increases throughput but hurts tail latency — a concrete queue example with real numbers (concept)
- Walking it: request coalescing and its latency cost vs its throughput win (concept)
- Walking it: connection pooling and its effect on both, at once (concept)
- Diagram: the same request path drawn optimized for latency vs optimized for throughput (diagram)
- The trade-off to name out loud: p50 vs p99 move in opposite directions when you batch (compare)
- Follow-up: "the interviewer says both matter equally — now what?" — segment the traffic and optimize each slice differently (concept)
- Follow-up: "how do you actually measure which one you're winning on?" — p50/p95/p99 and requests/sec side by side (concept)
- Pitfall: treating "faster" as one dimension instead of naming which one you're optimizing (pitfall)
- The 60-second version (concept)
- cross-link: latency-vs-throughput

### Topic: How would you calculate the availability of this system end-to-end? (iv-availability-math, intermediate)
Tests whether you can chain component availabilities correctly (multiply for serial dependencies, use redundancy math for parallel) instead of quoting "five nines" without doing the arithmetic.
- The question as asked, and why interviewers ask for the actual number (overview)
- Clarifying questions: which components are on the critical path vs optional/best-effort? (concept)
- The answer skeleton: multiply serial dependencies, apply 1-(1-p)^n for redundant paths (concept)
- Walking it: a worked example — LB (99.99) → app (99.95) → DB (99.9) chained to ~99.84% (code)
- Walking it: how adding a redundant DB replica changes the number — 1-(1-0.1)^2 (code)
- Walking it: translating the percentage into minutes of downtime/month, so it means something (code)
- Walking it: a third-party dependency (e.g. a payments API at 99.9%) capping your ceiling regardless of your own work (concept)
- The trade-off to name out loud: every extra nine costs real engineering effort — know where to stop (compare)
- Follow-up: "which component should you invest in improving first?" — the lowest-availability link on the critical path (concept)
- Follow-up: "does retrying a failed call to a dependency change this math?" — retries raise effective availability but add latency (concept)
- Pitfall: quoting "99.99% because that's what everyone says" with no math behind it (pitfall)
- The 60-second version (concept)
- cross-link: availability-and-reliability

### Topic: For this system, would you pick availability or consistency, and why? (iv-cap-tradeoff-for-this-system, advanced)
The applied CAP question — not "explain CAP" but "commit to a side for this specific feature and defend it." Tests judgment, not memorization.
- The question as asked: CAP theory already assumed, now apply it (overview)
- Clarifying questions: which specific operation — read, write, or both — is in scope? (concept)
- The answer skeleton: name the partition scenario, then state your choice and its user-facing cost (concept)
- Walking it: a payments write (choose C, reject the write) vs a like-counter read (choose A, serve stale) — concrete contrast (compare)
- Walking it: what "choosing A" actually looks like in code — serve from a replica, mark the response as possibly-stale (concept)
- Walking it: what "choosing C" actually looks like — reject or queue the write until the partition heals (concept)
- The trade-off to name out loud: PACELC — even with no partition, you still trade latency for consistency (compare)
- Follow-up: "what if the business says both are non-negotiable?" — the honest answer is you can't, name the compromise (concept)
- Follow-up: "how do you detect that a partition is actually happening right now?" (concept)
- Pitfall: reciting "CAP theorem says you can only have two of three" without picking a side (pitfall)
- The 60-second version (concept)
- cross-link: cap-theorem-and-pacelc

### Topic: Would you make this service stateless or stateful, and why? (iv-stateless-vs-stateful-choice, intermediate)
Probes whether you default to stateless (the safe answer) reflexively, or can name the real cases — WebSocket gateways, in-memory session caches — where statefulness is the right call.
- The question as asked, and the "always stateless" trap it's testing for (overview)
- Clarifying questions: does this service hold a live connection or per-request data only? (concept)
- The answer skeleton: default stateless; justify stateful only with a concrete reason (concept)
- Walking it: a WebSocket connection-holding gateway as the stateful counter-example (concept)
- Walking it: sticky sessions as a stateful compromise, and its failover cost when the node dies (concept)
- Walking it: externalizing state to Redis so the app tier stays stateless even for session data (concept)
- Diagram: a stateless app tier fronting an external session store vs a stateful gateway holding connections in-process (diagram)
- The trade-off to name out loud: statelessness buys trivial horizontal scaling, at the cost of an extra network hop for every read (compare)
- Follow-up: "how do you scale the stateful version?" — sharding by connection ID across gateway nodes (concept)
- Follow-up: "a stateful node crashes — what happens to its connections?" — clients reconnect and re-establish, own that cost explicitly (concept)
- Pitfall: saying "always stateless" and having no answer for real-time systems (pitfall)
- The 60-second version (concept)
- cross-link: sticky-sessions-and-statelessness

### Topic: Where are the single points of failure in this design, and how would you remove them? (iv-eliminate-single-points-of-failure, intermediate)
A design-review-style probe: can you scan a diagram (yours or the interviewer's) and spot every unreplicated component, not just the obvious ones.
- The question as asked, and why this is often asked right after your first diagram (overview)
- Clarifying questions: none needed — this is a "look at your own diagram" exercise (concept)
- The answer skeleton: walk the diagram left to right, flag anything with a count of one (concept)
- Walking it: the LB, the primary DB, and the "one service that everything calls" as the classic three (diagram)
- Walking it: fixing the LB — an active-passive pair behind a floating VIP or DNS failover (concept)
- Walking it: fixing the DB — a standby replica with automated failover, and its RPO cost (concept)
- Walking it: fixing the hot dependency — decoupling it with a queue or adding a fallback path (concept)
- The trade-off to name out loud: removing every SPOF adds real infra cost and operational surface — not all of them are worth fixing (compare)
- Follow-up: "which SPOF is cheapest to fix, and which is hardest?" (concept)
- Follow-up: "you fixed the DB SPOF — did you just move it to your failover coordinator?" — SPOFs can hide in the fix itself (concept)
- Pitfall: naming the DB as the only SPOF and missing the LB or a shared cache (pitfall)
- The 60-second version (concept)

### Topic: What questions would you ask before designing this system? (iv-nfr-elicitation-deep-dive, intermediate)
The `clarifying-requirements` topic in `sd-playbook` teaches the general method; this Topic drills the specific NFR questions interviewers expect for scale, latency, consistency, and durability before any diagram gets drawn.
- The question as asked, and why interviewers grade the first five minutes hardest (overview)
- The answer skeleton: functional scope, then scale, then latency, then consistency, then durability, in that order (concept)
- Walking it: the exact questions for scale — "DAU? read:write ratio? peak multiplier over average?" (concept)
- Walking it: the exact questions for latency — "what's the SLA for this endpoint, p99 not average?" (concept)
- Walking it: the exact questions for consistency and durability — "can we lose data? can we show stale data?" (concept)
- Walking it: a worked five-minute script, question by question, for a URL shortener as the running example (code)
- The trade-off to name out loud: asking too many questions burns the clock; asking too few builds the wrong system (compare)
- Follow-up: "the interviewer says 'you decide' — what do you assume, and do you say it out loud?" (concept)
- Follow-up: "you asked all the right questions but the interviewer contradicts your assumption later — what now?" (concept)
- Pitfall: asking questions in a random order instead of a scan that builds toward a diagram (pitfall)
- The 60-second version (concept)
- cross-link: clarifying-requirements

### Topic: Is this system read-heavy or write-heavy, and how does that change your design? (iv-read-heavy-vs-write-heavy, intermediate)
Tests whether the read:write ratio actually changes your architecture (caching, replica count, index strategy) or whether you draw the same diagram regardless of the numbers.
- The question as asked, and the ratio it wants you to reason from (overview)
- Clarifying questions: what's the approximate read:write ratio, and does it vary by time of day? (concept)
- The answer skeleton: read-heavy → cache + replicas; write-heavy → sharding + async writes (concept)
- Walking it: a social feed (100:1 read-heavy) — replicas, CDN, and aggressive caching (concept)
- Walking it: a metrics ingestion pipeline (1:100 write-heavy) — buffering, batching, and sharded writes (concept)
- Diagram: the same request path drawn for the read-heavy vs write-heavy version, side by side (diagram)
- The trade-off to name out loud: over-indexing for reads slows down the write path you actually need fast (compare)
- Follow-up: "the ratio flips during a spike — does your design still hold?" (concept)
- Follow-up: "what if it's 50:50 — does the split even matter then?" (concept)
- Pitfall: adding a read cache to a write-heavy system because "caching is always good" (pitfall)
- The 60-second version (concept)

### Topic: How do you design this service to be highly available? (iv-designing-for-high-availability, intermediate)
Tests whether "high availability" means something concrete to you — redundancy, health checks, automated failover — rather than a buzzword you attach to any design.
- The question as asked, and the buzzword-vs-mechanism gap it's probing (overview)
- Clarifying questions: what's the target — 99.9%? 99.99%? and what's the cost of an outage at that target? (concept)
- The answer skeleton: redundancy at every layer, health checks to detect failure, automated failover to act on it (concept)
- Walking it: N+1 (or N+2) redundancy at the app tier behind a load balancer with health checks (concept)
- Walking it: a DB primary-replica pair with automated failover, and the failover-detection window (concept)
- Walking it: multi-AZ placement so a single data-center failure doesn't take the whole service down (diagram)
- The trade-off to name out loud: higher availability targets need multi-region, which trades cost and consistency for uptime (compare)
- Follow-up: "your health check says healthy but the service is actually degraded — now what?" — deep health checks vs shallow pings (concept)
- Follow-up: "how fast does failover actually happen, and what does the user see during that window?" (concept)
- Pitfall: calling a design "highly available" because it "has a load balancer," with no failover story (pitfall)
- The 60-second version (concept)
- cross-link: availability-and-reliability

### Topic: What does "scalable" actually mean for this system, and how would you prove it? (iv-what-does-scalable-mean, intermediate)
Tests whether you can define scalability operationally — linear cost per added capacity, no single ceiling — instead of using it as a vague compliment for any design with more than one server.
- The question as asked, and why "scalable" without a definition is a red flag answer (overview)
- Clarifying questions: scalable to what number, and along which dimension — users, data, or requests? (concept)
- The answer skeleton: define it as "adding capacity linearly increases what the system can handle, with no hidden ceiling" (concept)
- Walking it: a design that scales linearly for a while, then hits a hard ceiling (the single DB primary) — naming exactly where (diagram)
- Walking it: proving scalability with a number — "this handles 10k QPS on N nodes; adding N more gets ~2x, not diminishing returns" (concept)
- Walking it: the same design tested against a stated target — does capacity really grow ~linearly as nodes are added? (concept)
- The trade-off to name out loud: near-linear scalability usually costs you strong consistency or simplicity (compare)
- Follow-up: "your design 'scales' — what's the actual next bottleneck, and at what number does it bite?" (concept)
- Follow-up: "is scaling reads the same problem as scaling writes here?" (concept)
- Pitfall: using "scalable" as an unexamined adjective instead of naming the axis and the ceiling (pitfall)
- The 60-second version (concept)
- cross-link: scalability-fundamentals

### Topic: When would you choose vertical scaling over horizontal scaling? (iv-vertical-vs-horizontal-scaling-choice, intermediate)
Tests whether you treat "always scale horizontally" as a reflex or actually know the real cases — a monolithic DB primary, a stateful in-memory workload — where a bigger box is genuinely the right call first.
- The question as asked, and the "horizontal is always better" reflex it's testing (overview)
- Clarifying questions: is the bottleneck a single stateful component (like a DB primary) or a stateless fleet? (concept)
- The answer skeleton: vertical first when sharding is expensive or premature; horizontal once you outgrow the biggest box available (concept)
- Walking it: a DB primary hitting CPU limits — resizing the instance before reaching for sharding (concept)
- Walking it: the ceiling vertical scaling eventually hits — biggest instance type, and its cost curve (concept)
- Walking it: a worked example — resizing a database primary from 8 to 32 cores buys 12-18 months of runway for a fraction of a sharding project's cost (code)
- The trade-off to name out loud: vertical scaling is simpler and keeps consistency easy, until you hit the ceiling and pay for it all at once (compare)
- Follow-up: "you've resized the DB three times already — when do you stop and shard instead?" (concept)
- Follow-up: "does this apply to the app tier too, or only to stateful components?" — app tiers rarely benefit from vertical scaling the same way (concept)
- Pitfall: sharding a database early "to be safe" when a bigger instance would have bought a year of runway cheaply (pitfall)
- The 60-second version (concept)
- cross-link: scalability-fundamentals

### Topic: This product just launched and got a flash crowd of new users — how does your design cope? (iv-flash-crowd-at-launch, advanced)
Distinct from a capacity-estimation question: this is about the architectural posture — queueing, waiting rooms, feature-flagged rollout — not the math of how big the spike is.
- The question as asked, and how it differs from steady 10x growth (overview)
- Clarifying questions: is the launch time known in advance, or could it go viral unpredictably? (concept)
- The answer skeleton: shed load gracefully at the edge before it reaches the DB, and roll out access gradually (concept)
- Walking it: a virtual waiting room / queue at the edge admitting users at a controlled rate (concept)
- Walking it: feature-flagged gradual rollout — 1% → 10% → 100% of users, watching each step (concept)
- Walking it: pre-warming caches and connection pools before doors open, not after (concept)
- The trade-off to name out loud: a waiting room protects the backend but costs you first-impression UX for the users stuck in line (compare)
- Follow-up: "the waiting room itself gets overwhelmed — what protects that?" — it must be the cheapest, most horizontally-scalable thing you own (concept)
- Follow-up: "how do you know it's actually working, in real time, during the launch?" (concept)
- Pitfall: relying on autoscaling alone with no gate at the edge, and getting flooded before new capacity comes online (pitfall)
- The 60-second version (concept)
- cross-link: graceful-degradation-and-load-shedding

### Topic: How do you decide whether an operation should be synchronous or asynchronous? (iv-sync-vs-async-choice, intermediate)
Tests whether you can name the concrete criterion — does the caller need the result to respond to the user right now — rather than defaulting to "async is more scalable" for everything.
- The question as asked, and the "async everything" reflex it's testing (overview)
- Clarifying questions: does the caller need the result immediately to complete its own response, or can it move on? (concept)
- The answer skeleton: sync when the caller needs the result now; async when the work can happen after you've already responded (concept)
- Walking it: a checkout flow — payment authorization is sync (you must know it succeeded), email receipt is async (concept)
- Walking it: what "going async" actually costs — a queue, a worker, and a new way for the user to learn the outcome (concept)
- Walking it: a worked example — a video-upload flow where transcoding is always async but the initial upload acknowledgment is sync (code)
- The trade-off to name out loud: async improves perceived latency and resilience, but trades away the caller's certainty of immediate success (compare)
- Follow-up: "the async job fails after you've already told the user it succeeded — now what?" — notify, retry, or reconcile (concept)
- Follow-up: "how does the client find out an async operation finished?" — polling, webhook, or push (concept)
- Pitfall: making a step async just for perceived speed, when the user actually needs to know the outcome before continuing (pitfall)
- The 60-second version (concept)
- cross-link: event-driven-architecture

---

## Group: Estimation — Interview Questions (interview-hld-estimation)
*QPS, storage, bandwidth, server/DB/shard count, cache size, cost, viral-spike capacity, and sanity-checking the numbers asked live*

### Topic: Estimate the QPS this system needs to handle (iv-estimate-qps, intermediate)
The canonical estimation opener. Tests whether you can go from a user count to a number in under a minute, out loud, without a calculator.
- The question as asked, and why interviewers care about the process, not the digit (overview)
- Clarifying questions: DAU, actions per user per day, and peak-to-average ratio (concept)
- The answer skeleton: DAU × actions/day ÷ 86400s = average QPS, then apply a peak multiplier (concept)
- Walking it: a worked example — 50M DAU, 20 actions/day → ~11.5k average QPS (code)
- Walking it: applying a 3x peak multiplier → ~35k peak QPS, and why peak is the number that sizes your fleet (code)
- Walking it: rounding cleanly (86400 ≈ 100k) so the mental math stays fast under pressure (concept)
- Walking it: splitting the QPS by endpoint when one action dominates (e.g. reads vs writes) (concept)
- The trade-off to name out loud: sizing for peak wastes capacity off-peak; sizing for average risks falling over daily (compare)
- Follow-up: "how does peak QPS change your load balancer and instance count?" (concept)
- Follow-up: "your peak multiplier assumption is wrong by 2x — how do you catch that before launch?" (concept)
- Pitfall: computing average QPS and never mentioning peak (pitfall)
- The 60-second version (concept)
- cross-link: traffic-estimation-qps

### Topic: Estimate how much storage this system needs over 5 years (iv-estimate-storage, intermediate)
Tests whether you can size one record correctly, multiply by volume and time, and sanity-check the result against something you already know (a phone's storage, a laptop's disk).
- The question as asked, and the two failure modes it catches — no method, or a wildly wrong sanity check (overview)
- Clarifying questions: size per record, write rate, and retention period (concept)
- The answer skeleton: bytes/record × records/day × 365 × years, then add a replication factor (concept)
- Walking it: a worked example — a chat message system, 500 bytes/message, 1B messages/day → raw daily volume (code)
- Walking it: scaling that to 5 years and adding a 3x replication factor for durability (code)
- Walking it: accounting for metadata and index overhead on top of raw data — often 20-30% more (concept)
- Walking it: converting the final number into a familiar unit (petabytes) and sanity-checking against a known reference (concept)
- The trade-off to name out loud: keeping everything hot forever is simple but expensive; tiering to cold storage saves money but adds retrieval latency (compare)
- Follow-up: "how would you reduce this if it's too expensive?" — TTL, cold storage tiers, compression (concept)
- Follow-up: "does this estimate change if the product adds attachments/media later?" (concept)
- Pitfall: forgetting the replication factor and understating cost by 3x (pitfall)
- The 60-second version (concept)
- cross-link: storage-estimation

### Topic: Estimate the bandwidth/network cost for this system (iv-estimate-bandwidth, intermediate)
Tests whether you can connect QPS and payload size into a bandwidth number, and spot which direction (ingress or egress) actually dominates cost.
- The question as asked, and why bandwidth is the estimate people skip (overview)
- Clarifying questions: payload size per request, and is this read-heavy (egress-dominated) or write-heavy (ingress-dominated)? (concept)
- The answer skeleton: QPS × payload size = bandwidth, computed separately for ingress and egress (concept)
- Walking it: a worked example — a video platform serving 100k concurrent streams at 5 Mbps → ~500 Gbps egress (code)
- Walking it: the same math for ingress on a write-heavy upload service, and why it's usually the smaller number (code)
- Walking it: converting bits/sec into a monthly data-transfer figure for the cost conversation (concept)
- The trade-off to name out loud: pushing egress to a CDN cuts origin bandwidth but adds cache-freshness constraints (compare)
- Follow-up: "how would a CDN change this number?" — moving most egress off origin entirely (concept)
- Follow-up: "what if traffic isn't evenly distributed across regions — does one region's origin still get hammered?" (concept)
- Pitfall: computing one combined number instead of separating ingress from egress (pitfall)
- The 60-second version (concept)
- cross-link: bandwidth-and-bottleneck-estimation

### Topic: How many servers would you need to serve this load? (iv-estimate-servers-needed, intermediate)
Tests whether you can turn a QPS number into a server count using a stated per-server capacity, and reason about headroom instead of sizing to exactly 100%.
- The question as asked, and the per-server capacity assumption it expects you to state (overview)
- Clarifying questions: what's a reasonable QPS-per-instance for this workload — CPU-bound or I/O-bound? (concept)
- The answer skeleton: peak QPS ÷ QPS-per-server, then add headroom for failover (concept)
- Walking it: a worked example — 50k peak QPS, 2k QPS/server → 25 servers, plus N+2 redundancy → 27 (code)
- Walking it: why I/O-bound workloads get a much higher per-server QPS number than CPU-bound ones (concept)
- Walking it: a worked example — running the same math for a CPU-bound image-resize service at 200 QPS/server instead of 2k (code)
- The trade-off to name out loud: more headroom protects against node failure but sits idle most of the time — a real cost (compare)
- Follow-up: "how does autoscaling change this — do you still need a fixed number?" (concept)
- Follow-up: "you're told the workload is bursty, not steady — does the headroom number change?" (concept)
- Pitfall: sizing to exactly the peak with zero headroom for a node failing (pitfall)
- The 60-second version (concept)

### Topic: Roughly what would this system cost to run per month? (iv-estimate-infra-cost, advanced)
A senior-signal estimation question — tests whether you can translate compute/storage/bandwidth estimates into a dollar figure, showing cost-awareness, not just capacity math.
- The question as asked, and why this gets asked at senior+ levels specifically (overview)
- Clarifying questions: cloud provider assumed, and is this steady-state or including the spike? (concept)
- The answer skeleton: cost = compute + storage + bandwidth + managed-service premium, summed separately (concept)
- Walking it: a worked example — 27 instance-hours priced roughly, times 730 hours/month (code)
- Walking it: adding storage GB-month and egress GB priced roughly, then summing the three lines (code)
- Walking it: the managed-service premium — a managed DB or queue costs more than self-hosting, and why that's often still the right call (concept)
- The trade-off to name out loud: managed services cost more per unit but remove an entire on-call burden — often worth it (compare)
- Follow-up: "what's the single biggest lever to cut this cost in half?" (concept)
- Follow-up: "reserved/committed-use pricing could cut this 30-40% — when do you commit to that vs staying on-demand?" (concept)
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
- Walking it: the autoscaling lag itself — instances take minutes to boot, so the first minutes are on existing capacity alone (concept)
- The trade-off to name out loud: pre-provisioning wastes money if the spike never comes; under-provisioning risks an outage if it does (compare)
- Follow-up: "autoscaling takes 5 minutes to add capacity — what covers you until then?" (concept)
- Follow-up: "how do you tell a real viral spike from a bot/DDoS spike, in the moment?" (concept)
- Pitfall: assuming autoscaling alone handles any spike size, with no plan for the gap (pitfall)
- The 60-second version (concept)
- cross-link: graceful-degradation-and-load-shedding

### Topic: How big should the cache be for this system? (iv-estimate-cache-size, intermediate)
Tests whether you can size a cache from the working set (hot data), not the full dataset, and justify the number against a hit-rate target.
- The question as asked, and the working-set-vs-full-dataset distinction it's probing (overview)
- Clarifying questions: what's the access pattern — is 80% of traffic hitting 20% of keys? (concept)
- The answer skeleton: estimate the hot working set size, not total data size, and target a hit rate (concept)
- Walking it: a worked example — sizing a cache for the hot 20% of a 10M-item, 1KB-avg product catalog → ~2GB (code)
- Walking it: adding overhead for key metadata and eviction bookkeeping — real usage runs higher than raw data size (concept)
- Walking it: a worked example — comparing the resulting cache size against a single node's available RAM to see if one node suffices (code)
- The trade-off to name out loud: a bigger cache raises hit rate but past the working-set size, returns flatten fast — know where that knee is (compare)
- Follow-up: "how do you verify the hit rate in production once it's live?" (concept)
- Follow-up: "the working set doubles overnight after a feature launch — does your cache size still hold?" (concept)
- Pitfall: sizing the cache to hold all the data "to be safe" (pitfall)
- The 60-second version (concept)
- cross-link: caching-fundamentals

### Topic: How do you sanity-check a back-of-envelope estimate in the room? (iv-sanity-check-your-numbers, intermediate)
The meta-question: after producing a number, can you tell if it's plausible — comparing it to a known reference point instead of moving on and hoping it's right.
- The question as asked, and why interviewers probe this after any estimate (overview)
- The answer skeleton: compare against a reference you already know — a known company's scale, a familiar disk size (concept)
- Walking it: "50 PB sounds like a lot — is it? Compare to a known large-scale dataset" (concept)
- Walking it: catching an off-by-1000 error from a unit mix-up (KB vs MB vs GB) (pitfall)
- Walking it: a second sanity check — does the implied server/cost count match the size of company that would run this? (concept)
- Walking it: a worked example — sanity-checking a storage estimate against a known reference, like a well-known company's publicly disclosed data volume (concept)
- The trade-off to name out loud: a quick sanity check costs 30 seconds; presenting a wrong number costs the whole deep-dive's credibility (compare)
- Follow-up: "your number implies 10,000 servers — does that pass the smell test for this company's size?" (concept)
- Follow-up: "you catch your own error mid-answer — how do you recover without losing the room?" (concept)
- Pitfall: presenting a number with false precision and no sanity check at all (pitfall)
- The 60-second version (concept)
- cross-link: estimation-in-the-interview

### Topic: How many database servers or shards would this system need? (iv-estimate-db-capacity, advanced)
A DB-specific rerun of the server-count question — tests whether you reason separately about write capacity (drives shard count) and read capacity (drives replica count), instead of one generic "server count."
- The question as asked, and why it's a different estimate from generic app-server count (overview)
- Clarifying questions: what's the write QPS and the storage-per-shard limit you're targeting? (concept)
- The answer skeleton: shard count from write throughput and data-size limits; replica count from read QPS and read:write ratio (concept)
- Walking it: a worked example — 20k write QPS, 5k writes/sec per shard capacity → 4 shards minimum (code)
- Walking it: layering read replicas on top — 100k read QPS, 10k reads/sec per replica → 10 replicas per shard (code)
- Walking it: why you round both numbers up, not to the nearest whole, and add one for failover (concept)
- The trade-off to name out loud: more shards spread load but each cross-shard query gets more expensive — shard count isn't free even when writes justify it (compare)
- Follow-up: "your data size triples next year — does your shard count still hold, or do you need to reshard?" (concept)
- Follow-up: "how does this number change if you add a caching layer in front?" (concept)
- Pitfall: sizing DB capacity from total QPS instead of separating write throughput (which drives shards) from read throughput (which drives replicas) (pitfall)
- The 60-second version (concept)
- cross-link: partitioning-and-sharding

### Topic: Estimate how many concurrent connections this system needs to support (iv-estimate-concurrent-connections, intermediate)
Distinct from QPS: for chat, notifications, or live-collaboration systems, the number that matters is concurrent open connections, not requests per second — tests whether you know when to reach for that number instead.
- The question as asked, and why QPS is the wrong number for a connection-holding system (overview)
- Clarifying questions: is this a request/response API or a persistent-connection system (WebSocket, long-poll)? (concept)
- The answer skeleton: concurrent connections ≈ DAU × average session duration ÷ total seconds in the window, not a per-request rate (concept)
- Walking it: a worked example — 10M DAU, average 15-minute session, spread over a 4-hour peak window → concurrent connection estimate (code)
- Walking it: translating that into gateway node count from a stated max-connections-per-node figure (concept)
- Walking it: a worked example — checking the resulting connection count against a stated max-connections-per-node ceiling before committing to a gateway fleet size (concept)
- The trade-off to name out loud: holding more connections per node is cheaper but each node failure now drops more users at once (compare)
- Follow-up: "connections aren't evenly spread across the day — how does your peak-window assumption hold up?" (concept)
- Follow-up: "how does this number change your load balancer choice — L4 vs L7, connection draining on deploy?" (concept)
- Pitfall: estimating a chat system's capacity using request-per-second math instead of concurrent-connection math (pitfall)
- The 60-second version (concept)

### Topic: How would you estimate the number of shards or partitions this dataset needs? (iv-estimate-shard-count, advanced)
A data-volume-driven estimate distinct from the DB-capacity question — tests whether you can go from total data size and a per-partition ceiling to a partition count, independent of QPS.
- The question as asked, and how it differs from sizing shards for write throughput (overview)
- Clarifying questions: what's the total data size, and what's the max recommended size per partition/shard for the chosen store? (concept)
- The answer skeleton: partition count = total data size ÷ max size per partition, then round up and add slack for growth (concept)
- Walking it: a worked example — 40TB of data, a 500GB-per-shard ceiling → 80 shards minimum, round to 96 for headroom (code)
- Walking it: reconciling this with the write-throughput-driven shard count from the DB-capacity estimate — take the larger of the two (concept)
- Walking it: a worked example — checking whether the query pattern, not just raw size, pushes the count higher, e.g. hot cross-shard queries (concept)
- The trade-off to name out loud: over-partitioning up front avoids a resharding project later, but adds cross-partition query cost from day one (compare)
- Follow-up: "data doubles every year — how many shards do you provision now vs add later?" (concept)
- Follow-up: "does your sharding key choice affect whether this count is achievable, or just theoretical?" (concept)
- Pitfall: sizing partition count only from data volume and ignoring that write throughput might demand more (pitfall)
- The 60-second version (concept)
- cross-link: partitioning-and-sharding

### Topic: How would you estimate the QPS hitting one specific downstream dependency? (iv-estimate-fanout-qps, advanced)
Tests whether you can reason past the front-door QPS to what a single internal service actually receives once fan-out multiplies it — the number that decides if that dependency needs its own scaling plan.
- The question as asked, and why front-door QPS understates load on internal services (overview)
- Clarifying questions: how many downstream calls does one incoming request trigger, and are any of them cached or batched? (concept)
- The answer skeleton: downstream QPS = incoming QPS × fan-out factor per request, then subtract what caching absorbs (concept)
- Walking it: a worked example — a news-feed request fanning out to 5 backend calls per page load, at 10k incoming QPS → 50k QPS on that tier before caching (code)
- Walking it: applying an 80% cache hit rate on top, bringing the real downstream load down to 10k QPS (code)
- Walking it: a worked example — the same math for a fan-out to 20 microservices in a poorly-decomposed system, and why that number alone argues for consolidation (concept)
- The trade-off to name out loud: batching fan-out calls cuts downstream QPS but adds latency to the front-door request (compare)
- Follow-up: "one of the five downstream calls is much slower than the others — does fan-out QPS even matter more than fan-out latency here?" (concept)
- Follow-up: "the dependency's own capacity is smaller than your estimate — what do you change, the fan-out or the dependency?" (concept)
- Pitfall: sizing a downstream service's capacity using the same QPS number as the front door, ignoring fan-out entirely (pitfall)
- The 60-second version (concept)

### Topic: How do you tell if this problem actually needs a distributed system, or if one strong machine would do? (iv-single-machine-vs-distributed-check, advanced)
A senior-signal gut-check question — tests whether estimation is used to avoid over-building, not just to justify scale, by checking the numbers against what a single modern machine can actually handle.
- The question as asked, and the over-engineering trap it's checking you don't fall into (overview)
- Clarifying questions: what's the actual peak QPS and data size — not the eventual aspirational scale, the real numbers now? (concept)
- The answer skeleton: compare the estimate against a single high-end machine's known capacity (RAM, cores, disk IOPS) before reaching for a cluster (concept)
- Walking it: a worked example — a dataset that fits in 256GB of RAM and 50k QPS a single well-tuned instance can serve, no cluster needed yet (code)
- Walking it: the point where a single machine genuinely stops being enough — durability (one box, one failure) as much as raw capacity (concept)
- Walking it: a worked example — checking whether the workload is CPU-bound, memory-bound, or I/O-bound, since each has a very different single-machine ceiling (concept)
- The trade-off to name out loud: a single machine is simpler and cheaper, but is itself a single point of failure the moment you're graded on availability, not just throughput (compare)
- Follow-up: "the interviewer says 'assume this must survive a machine failure' — does that change your answer even if capacity alone doesn't?" (concept)
- Follow-up: "your estimate says one machine is enough today — do you still design for a distributed future, or build it when you need it?" (concept)
- Pitfall: reaching for a distributed architecture by default because "that's what system design interviews want," without checking whether the numbers actually demand it (pitfall)
- The 60-second version (concept)
- cross-link: back-of-envelope-fundamentals

---

## Group: Caching — Interview Questions (interview-hld-caching)
*what/where to cache, TTL, warming, invalidation, stampede, cache-DB consistency, write strategy, CDN scope, eviction, local vs distributed, personalization, and hot keys*

### Topic: What would you cache in this system, and what would you never cache? (iv-what-to-cache, intermediate)
Tests judgment, not the definition of caching — can you name specific fields/endpoints to cache and specific ones (balances, anything requiring strong consistency) you'd deliberately leave uncached.
- The question as asked, and the "cache everything" reflex it's testing against (overview)
- Clarifying questions: which reads are hot and tolerant of staleness, and which must always be fresh? (concept)
- The answer skeleton: cache hot + slow-changing + read-heavy data; skip anything requiring strong consistency (concept)
- Walking it: a user profile (cache it, changes rarely) vs an account balance (don't, must be exact) — concrete contrast (compare)
- Walking it: a product listing page — cache the description and images, never the live inventory count on the same page (concept)
- Walking it: computed/aggregated results (a trending list, a leaderboard) as prime caching candidates — expensive to compute, tolerant of a few seconds' staleness (concept)
- The trade-off to name out loud: caching more cuts DB load but every cached field is a place staleness can leak into the UI (compare)
- Follow-up: "what if product wants the balance to feel instant too?" — cache with a short TTL and a visible staleness signal (concept)
- Follow-up: "how do you decide the boundary when a page mixes cacheable and non-cacheable fields?" — fragment the response, cache part of it (concept)
- Pitfall: caching a financial or inventory count "for speed" with no staleness plan (pitfall)
- The 60-second version (concept)
- cross-link: caching-fundamentals

### Topic: Where should the cache live — client, CDN, app layer, or DB layer? (iv-where-to-cache, intermediate)
Tests whether you can place a cache at the right layer for the specific data, instead of defaulting to "we'll add Redis."
- The question as asked, and the four layers it expects you to know (overview)
- Clarifying questions: is this data static assets, personalized data, or a shared computed result? (concept)
- The answer skeleton: static → CDN/client; shared computed → app-layer distributed cache; per-row lookups → DB buffer/cache (concept)
- Walking it: a worked example — a product page's images (CDN), price (app cache), and inventory count (DB) (diagram)
- Walking it: the same data cached at two layers at once — a browser cache in front of a CDN in front of an app cache (concept)
- Walking it: a worked example — a session token cached at the app layer vs a static logo cached at the CDN, on the very same page load (concept)
- The trade-off to name out loud: caching closer to the user cuts latency more but is harder to invalidate reliably (compare)
- Follow-up: "what changes if the user base is global?" — edge caching and regional cache tiers (concept)
- Follow-up: "you have four cache layers now — how do you even know which one served a stale response?" (concept)
- Pitfall: putting everything in one Redis cluster regardless of access pattern (pitfall)
- The 60-second version (concept)

### Topic: What TTL would you set for this cache, and why? (iv-cache-ttl-choice, intermediate)
Tests whether you pick a TTL from the data's actual staleness tolerance and update frequency, not a copy-pasted default like "5 minutes" for everything.
- The question as asked, and the copy-pasted-default trap it's testing against (overview)
- Clarifying questions: how often does the underlying data actually change, and how stale can the user tolerate it being? (concept)
- The answer skeleton: TTL ≈ how long a wrong answer is tolerable, bounded above by how often the data changes (concept)
- Walking it: a worked example — a weather widget (changes hourly, 10-min TTL is plenty) vs a stock price ticker (seconds matter, TTL near zero, invalidate on write instead) (compare)
- Walking it: adding jitter to the TTL (±10%) so many keys set at once don't all expire in the same instant (concept)
- Walking it: a worked example — computing the DB-load reduction from moving a TTL from 10s to 60s, and the staleness cost that buys (code)
- The trade-off to name out loud: a longer TTL cuts DB load harder but widens the window where users see wrong data (compare)
- Follow-up: "the same data has two different TTL needs depending on which screen shows it — one TTL or two caches?" (concept)
- Follow-up: "how do you find out your TTL was wrong after shipping it?" — staleness complaints and hit-rate/error dashboards (concept)
- Pitfall: setting one global default TTL across every cached key regardless of how fast that data actually changes (pitfall)
- The 60-second version (concept)
- cross-link: caching-fundamentals

### Topic: How would you warm a cold cache after a deploy or a node restart? (iv-cache-warming, advanced)
Tests whether you have a concrete plan for the moment a cache is empty and every request becomes a DB hit, instead of assuming the cache is "just always there."
- The question as asked, and the cold-start moment it's really asking about (overview)
- Clarifying questions: is this a planned restart (a deploy) or an unplanned one (a crash)? (concept)
- The answer skeleton: pre-populate the hot keys before traffic arrives, or ramp traffic in gradually while it fills naturally (concept)
- Walking it: pre-warming from a snapshot of yesterday's top-N hot keys, loaded before the node joins the pool (concept)
- Walking it: gradual traffic ramp-in behind the load balancer, giving the cache time to fill under real read-through traffic (concept)
- Walking it: a worked example — warming only the top 1000 keys by request volume from yesterday's access logs, not the whole dataset (code)
- The trade-off to name out loud: pre-warming avoids a DB spike but the snapshot may already be stale by the time it's loaded (compare)
- Follow-up: "the whole cluster restarts at once, not one node — does your plan still work?" — rolling restarts, never all-at-once (concept)
- Follow-up: "how much DB headroom do you need to survive an unplanned full cold start?" (concept)
- Pitfall: assuming the cache will "just fill up naturally fast enough," with no plan for the DB load spike in between (pitfall)
- The 60-second version (concept)

### Topic: How would you invalidate this cache when the underlying data changes? (iv-cache-invalidation-strategy, advanced)
The classic "there are only two hard problems" question — tests whether you can pick and defend a concrete invalidation strategy for the specific data, not just name that invalidation is hard.
- The question as asked, and why "cache invalidation is hard" isn't an answer by itself (overview)
- Clarifying questions: can this data tolerate a short staleness window, or must it invalidate immediately? (concept)
- The answer skeleton: pick TTL, write-through invalidation, or event-driven invalidation, and justify against the staleness tolerance (concept)
- Walking it: TTL-only for tolerant data vs explicit delete-on-write for a user's own profile (compare)
- Walking it: event-driven invalidation via a change stream (e.g. CDC off the DB's write-ahead log) for fan-out caches with many derived keys (concept)
- Walking it: a worked example — updating a product price triggers a delete on the product-page cache key and the search-index cache entry, in one event (code)
- The trade-off to name out loud: event-driven invalidation is precise but adds a dependency on the event pipeline being reliable — a bug there silently serves stale data forever (compare)
- Follow-up: "two app instances update the same key milliseconds apart — what happens to the cache?" (concept)
- Follow-up: "your invalidation event gets lost — how would you even notice?" (concept)
- Pitfall: relying on TTL alone for data users expect to see updated immediately (pitfall)
- The 60-second version (concept)
- cross-link: cache-invalidation

### Topic: What happens when your cache expires under heavy load, and how do you prevent it? (iv-cache-stampede, advanced)
Tests whether you know the thundering-herd failure mode by its mechanics, not just its name, and can name a concrete fix.
- The question as asked, and the failure it's describing without naming it (overview)
- Clarifying questions: is this one hot key expiring, or a mass expiry across many keys at once? (concept)
- The answer skeleton: name the mechanism (all requests miss at once, all hit the DB at once), then apply a fix (concept)
- Walking it: request coalescing (single-flight) so only one request repopulates the cache while others wait on it (concept)
- Walking it: staggered TTLs with jitter to avoid mass-expiry, plus stale-while-revalidate to serve the old value during the refresh (concept)
- Walking it: a worked example — a homepage banner cached for 100k concurrent readers; without coalescing, one expiry sends 100k queries to the DB at once (code)
- The trade-off to name out loud: request coalescing adds a small latency tax to the unlucky request that triggers the refill (compare)
- Follow-up: "the DB is still getting hammered even with coalescing — what else?" — a lock or a probabilistic early refresh (concept)
- Follow-up: "how is this different from a hot-key problem, and does the fix overlap?" (concept)
- Pitfall: describing the symptom (DB overload) without naming the cause (cache miss stampede) (pitfall)
- The 60-second version (concept)

### Topic: How do you keep the cache consistent with the database? (iv-cache-db-consistency, advanced)
Tests whether you can reason about the actual race conditions in cache-aside vs write-through patterns, not just name the pattern.
- The question as asked, and the write-then-read race it's really asking about (overview)
- Clarifying questions: cache-aside, write-through, or write-behind — which pattern is already in play? (concept)
- The answer skeleton: name the pattern, then walk the specific race window it leaves open (concept)
- Walking it: cache-aside's classic race — delete cache, then a concurrent read repopulates it with stale data before the write commits (diagram)
- Walking it: the fix — delete-after-write with a short delay, or versioned cache entries that reject a stale repopulation (concept)
- Walking it: a worked example — the exact interleaving of two threads that produces the stale entry, step by step (code)
- The trade-off to name out loud: delaying the delete narrows the race window but never fully closes it — perfect cache-DB consistency isn't free (compare)
- Follow-up: "how would you detect this drift is actually happening in production?" (concept)
- Follow-up: "does write-through avoid this race entirely, and what does it cost you instead?" — write latency now includes the cache write (concept)
- Pitfall: assuming cache-aside is automatically consistent because it "invalidates on write" (pitfall)
- The 60-second version (concept)
- cross-link: cache-read-write-patterns

### Topic: Which caching write strategy would you use — cache-aside, write-through, or write-behind? (iv-cache-write-strategy-choice, advanced)
A choice question that precedes the consistency-race question — tests whether you can pick the right write pattern up front for the workload's read/write ratio and durability needs.
- The question as asked, and the three named patterns it expects you to compare (overview)
- Clarifying questions: is this workload read-heavy or write-heavy, and can a cache write be allowed to lag the DB write? (concept)
- The answer skeleton: cache-aside for read-heavy and simple; write-through for consistency on every write; write-behind for write-heavy with tolerance for a durability gap (concept)
- Walking it: a worked example — a session store using write-through (must always be correct) vs an analytics counter using write-behind (batched, occasional loss acceptable) (compare)
- Walking it: what write-behind actually risks — a crash before the batched write flushes to the DB (concept)
- Walking it: a worked example — the write-latency difference measured across all three strategies for the same write, side by side (code)
- The trade-off to name out loud: write-behind gives the best write latency but is the only one of the three that can lose data on a crash (compare)
- Follow-up: "you picked cache-aside — what happens on the very first read after a cache miss, at scale?" (concept)
- Follow-up: "could you mix strategies for different fields on the same entity?" (concept)
- Pitfall: defaulting to cache-aside everywhere without checking whether the write path can tolerate its read-after-write gap (pitfall)
- The 60-second version (concept)
- cross-link: cache-read-write-patterns

### Topic: What would you put behind a CDN, and what wouldn't you? (iv-cdn-what-and-when, intermediate)
Tests scope: CDNs are for cacheable, publicly shareable content — can you draw that line correctly for personalized or write-heavy paths.
- The question as asked, and the "just CDN it" reflex it's testing (overview)
- Clarifying questions: is this content the same for every user, or personalized per request? (concept)
- The answer skeleton: CDN for static/shared/cacheable GETs; origin for personalized, write, or auth-gated requests (concept)
- Walking it: images and JS bundles (CDN) vs a personalized dashboard API response (origin) (compare)
- Walking it: setting Cache-Control and Vary headers correctly so the CDN doesn't accidentally serve one user's response to another (concept)
- Walking it: a worked example — a mostly-static blog page cached at the CDN with a 1-hour TTL, while its live comment count is fetched separately (concept)
- The trade-off to name out loud: CDN caching cuts origin load and latency hardest for global users, but every cached response is a staleness window you own (compare)
- Follow-up: "can you CDN a mostly-static page that has one personalized widget?" — edge includes / fragment caching (concept)
- Follow-up: "a misconfigured Vary header just leaked one user's cached page to another — how do you catch that class of bug?" (concept)
- Pitfall: trying to CDN an authenticated, per-user API response directly (pitfall)
- The 60-second version (concept)
- cross-link: cdn-and-edge-caching

### Topic: Which eviction policy would you choose for this cache, and why? (iv-eviction-policy-choice, intermediate)
Tests whether you can match an eviction policy to an actual access pattern instead of defaulting to "LRU, obviously."
- The question as asked, and why "LRU" isn't automatically the right answer (overview)
- Clarifying questions: is access recency- or frequency-driven — do the same few keys dominate, or does recency matter more? (concept)
- The answer skeleton: LRU for recency-driven access; LFU for a stable hot set; TTL for time-bound relevance (concept)
- Walking it: a trending-content cache where LFU beats LRU because recency is a poor proxy for what's actually hot (compare)
- Walking it: a worked example — a one-time viral read that would evict genuinely hot keys under pure LRU (concept)
- Walking it: a worked example — simulating both policies against a week of real access logs and comparing the resulting hit rates (code)
- The trade-off to name out loud: LFU tracks true popularity better but costs more bookkeeping per access than LRU (compare)
- Follow-up: "how would you verify your choice was right after shipping it?" — hit-rate monitoring (concept)
- Follow-up: "could you combine policies — LRU within a size tier, LFU for promotion into a smaller hot tier?" (concept)
- Pitfall: picking LRU by default without checking whether the access pattern actually fits it (pitfall)
- The 60-second version (concept)
- cross-link: eviction-policies

### Topic: Would you use a local (in-process) cache or a distributed cache here? (iv-local-vs-distributed-cache, intermediate)
Tests whether you know the concrete trade-off — local is faster but inconsistent across nodes; distributed is consistent but adds a network hop — and can pick per use case, including combining both.
- The question as asked, and the "just use Redis" default it's testing against (overview)
- Clarifying questions: does every app node need to see the same value, or is per-node staleness acceptable? (concept)
- The answer skeleton: local cache for data tolerant of per-node inconsistency and needing sub-millisecond access; distributed for shared, must-agree state (concept)
- Walking it: a worked example — caching a compiled config or a feature flag locally (near-zero latency, tiny inconsistency window) vs a shared rate-limit counter in Redis (must be shared) (compare)
- Walking it: a two-tier cache — a small local cache in front of the distributed cache, cutting most of the network hops for the hottest keys (diagram)
- Walking it: a worked example — measuring the latency gap between a local in-process lookup (sub-microsecond) and a network round-trip to a distributed cache (~1ms) (code)
- The trade-off to name out loud: local caching is fastest but multiplies memory use across every node and can't be invalidated in one place (compare)
- Follow-up: "you add a local cache layer — how do you invalidate it across every node when the data changes?" (concept)
- Follow-up: "a node has been up for weeks with a stale local cache entry — how would you catch that?" (concept)
- Pitfall: assuming a distributed cache alone is "fast enough" when the workload actually needs local, in-process speed (pitfall)
- The 60-second version (concept)
- cross-link: distributed-caching

### Topic: How do you cache content that's personalized per user? (iv-caching-personalized-content, advanced)
Tests whether you know techniques beyond "you can't cache personalized data" — per-user keys, fragment caching, and caching the expensive shared part separately from the cheap personal part.
- The question as asked, and the "personalized means uncacheable" myth it's testing against (overview)
- Clarifying questions: which part of the response is actually personalized, and which part is shared across users? (concept)
- The answer skeleton: split the response — cache the shared/expensive part normally, cache the personal/cheap part per-user or not at all (concept)
- Walking it: a worked example — a news feed's ranking model output (expensive, cache per-user with a short TTL) vs its "liked by 3 friends" annotation (compute live, cheap) (compare)
- Walking it: per-user cache keys and their memory-multiplication cost — N users × the cached payload size (concept)
- Walking it: fragment/edge-include caching — the page shell is shared and CDN-cached, the personalized widget is fetched separately (diagram)
- The trade-off to name out loud: per-user caching cuts compute cost but multiplies memory footprint by user count — it's only worth it if recomputing is genuinely expensive (compare)
- Follow-up: "the personalization model changes — how do you invalidate millions of per-user cache entries at once?" (concept)
- Follow-up: "would you rather recompute cheaply or cache expensively here — how do you decide?" (concept)
- Pitfall: either caching nothing because "it's personalized" or caching the entire per-user response naively and blowing up memory (pitfall)
- The 60-second version (concept)

### Topic: One key is getting 100x the traffic of others — how do you handle it? (iv-hot-key-problem, advanced)
The hot-key/hot-partition-at-the-cache-layer question — tests whether you can go beyond "add more cache nodes" since a single key can't be sharded across nodes trivially.
- The question as asked, and why simply adding nodes doesn't fix a single hot key (overview)
- Clarifying questions: is this a celebrity-user pattern, a viral post, or a misbehaving client retrying? (concept)
- The answer skeleton: detect the hot key, then replicate it locally or split it, don't just scale the cluster (concept)
- Walking it: local (in-process) caching of the hot key on top of the distributed cache, absorbing most of the read traffic before it ever reaches the cluster (concept)
- Walking it: key splitting — sharding one logical key into N physical keys (key#0..key#N) and merging on read (concept)
- Walking it: a worked example — a celebrity's profile getting 500k reads/sec against a cluster sized for 5k reads/sec/node (code)
- The trade-off to name out loud: key splitting fixes the hot-read problem but complicates every write, which must now fan out to all N physical keys (compare)
- Follow-up: "how do you even detect a hot key before it takes down the node?" (concept)
- Follow-up: "the hot key is also being written to frequently, not just read — does the same fix still work?" (concept)
- Pitfall: adding more cache nodes and being surprised the hot node is still overloaded (pitfall)
- The 60-second version (concept)

---

## Group: Data at Scale — Interview Questions (interview-hld-data)
*SQL vs NoSQL, sharding key choice, resharding, hot partitions, index design, polyglot persistence, blob vs DB, cross-service transactions, schema migration, table growth, denormalization, time-series, and NoSQL relations*

### Topic: Would you use SQL or NoSQL for this system, and why? (iv-sql-vs-nosql-choice, intermediate)
Tests whether you pick based on the actual access pattern and consistency needs of this system, not personal preference or "NoSQL scales better" as a slogan.
- The question as asked, and the slogan-answer trap it's checking for (overview)
- Clarifying questions: what are the query patterns — joins and transactions, or key-based lookups at huge scale? (concept)
- The answer skeleton: name the query pattern, consistency need, and scale target, then pick accordingly (concept)
- Walking it: an order system needing multi-table transactions (SQL) vs a session store needing raw key lookups at scale (compare)
- Walking it: a worked example — the same "get user's recent orders" query, shown as a SQL join vs a denormalized NoSQL document (code)
- Walking it: schema flexibility as a real factor — a rapidly evolving product schema favoring NoSQL's looser typing (concept)
- The trade-off to name out loud: NoSQL buys write scale and flexible schema, SQL buys strong consistency and rich queries — you're trading one for the other, not getting both for free (compare)
- Follow-up: "could you start on SQL and migrate to NoSQL later — what would that cost you?" (concept)
- Follow-up: "what if you need both — transactional order data and huge-scale session data, in the same product?" — polyglot persistence (concept)
- Pitfall: saying "NoSQL scales better" without naming which scaling dimension SQL actually struggles with (pitfall)
- The 60-second version (concept)
- cross-link: sql-vs-nosql-at-scale

### Topic: How would you choose the sharding key for this data? (iv-choosing-a-sharding-key, advanced)
Tests whether you can evaluate a specific key against query patterns and skew risk, rather than picking the obvious ID column by default.
- The question as asked, and why "shard by user ID" isn't automatically right (overview)
- Clarifying questions: what's the most common query — by user, by time, by geography? (concept)
- The answer skeleton: pick the key that keeps the most common query within one shard and avoids skew (concept)
- Walking it: sharding a chat app by conversation ID vs by user ID — which queries stay single-shard (compare)
- Walking it: a worked example — sharding by user ID sends a "get all messages in this group chat" query to every shard; conversation ID keeps it on one (code)
- Walking it: checking the candidate key for skew before committing — will one value (a huge group, a power user) dominate a shard? (concept)
- The trade-off to name out loud: a key that fits today's dominant query might create a hotspot on tomorrow's — you're picking against known queries, not all possible ones (compare)
- Follow-up: "your chosen key causes a skew for one power user — now what?" (concept)
- Follow-up: "the product adds a new query pattern your key doesn't support well — do you reshard or add a secondary index?" (concept)
- Pitfall: sharding by a monotonically increasing ID or timestamp and creating a hot last shard (pitfall)
- The 60-second version (concept)
- cross-link: partitioning-and-sharding

### Topic: How would you reshard this database as it grows, without downtime? (iv-resharding-without-downtime, advanced)
Tests whether you know the actual mechanics of live resharding — dual-writes, background migration, cutover — not just that resharding is "hard."
- The question as asked, and why "add more shards" undersells the difficulty (overview)
- Clarifying questions: is this a planned rebalance or a reaction to an already-hot shard? (concept)
- The answer skeleton: dual-write to old and new layout, backfill in the background, cut over, then stop dual-writing (concept)
- Diagram: the resharding timeline — dual-write, backfill, verify, cutover, cleanup (diagram)
- Walking it: a worked example — the exact sequence of flipping reads to the new shard layout only after backfill lag reaches zero (concept)
- Walking it: keeping the dual-write window short by throttling backfill against production traffic (concept)
- The trade-off to name out loud: dual-writing avoids downtime but doubles write cost and complexity for the whole migration window — plan for that window to be long (compare)
- Follow-up: "how do you verify the new shard layout is correct before cutting over?" (concept)
- Follow-up: "the cutover reveals a data mismatch — do you roll back, or fix forward?" (concept)
- Pitfall: doing a big-bang migration that requires taking writes offline (pitfall)
- The 60-second version (concept)
- cross-link: resharding-and-hotspots

### Topic: One shard is getting way more traffic than the others — what do you do? (iv-hot-partition-fix, advanced)
The applied hot-partition question — distinguishes a hot-key problem (one row) from a hot-shard problem (bad key design), and tests whether you can tell the two apart before proposing a fix.
- The question as asked, and how to tell a hot shard from a hot key inside it (overview)
- Clarifying questions: is the whole shard hot, or one key on it, evenly spread traffic just landing on a small shard count? (concept)
- The answer skeleton: diagnose which of the three, then split the shard, split the key, or add virtual shards (concept)
- Walking it: virtual/consistent hashing to spread a hot range across more physical nodes without a full resharding project (concept)
- Walking it: a worked example — a shard holding one viral group's data, split into a dedicated shard just for that group (concept)
- Walking it: a worked example — checking per-shard QPS to confirm it's really one hot shard, not evenly spread load landing on too few shards (code)
- The trade-off to name out loud: virtual shards fix distribution cheaply but add a lookup indirection to every request — one more hop to get right (compare)
- Follow-up: "the hot shard is hot because of one celebrity account — does resharding even help?" (concept)
- Follow-up: "how do you detect a hot shard before it pages someone at 3am?" (concept)
- Pitfall: resharding the whole dataset when the real problem is one hot key on one shard (pitfall)
- The 60-second version (concept)
- cross-link: resharding-and-hotspots

### Topic: How would you design indexes for this table at scale? (iv-index-design-at-scale, intermediate)
Tests whether you can name the specific indexes a query pattern needs and their write-cost trade-off, not just say "add an index."
- The question as asked, and the write-amplification cost it expects you to weigh (overview)
- Clarifying questions: what are the top 2-3 query patterns this table needs to serve fast? (concept)
- The answer skeleton: index the columns in your actual WHERE/ORDER BY clauses; every index is a write cost (concept)
- Walking it: a composite index ordering decision for a two-column filter — column order changes which queries the index actually serves (code)
- Walking it: a worked example — adding a covering index that lets a hot query avoid a table lookup entirely (code)
- Walking it: a worked example — using a query planner's explain output to confirm the composite index is actually used, not silently skipped (code)
- The trade-off to name out loud: every index speeds a read path but slows every write that touches that table — index count is a budget, not a free win (compare)
- Follow-up: "you now have 8 indexes on this table — what's that costing you on writes?" (concept)
- Follow-up: "how do you find out an index isn't even being used anymore?" (concept)
- Pitfall: indexing every column "just in case" instead of matching indexes to real queries (pitfall)
- The 60-second version (concept)

### Topic: Would you use one database for everything, or different databases for different parts? (iv-polyglot-persistence-choice, advanced)
Tests whether you can justify splitting storage by workload (search index, graph, blob, relational) instead of defaulting to one database for operational simplicity.
- The question as asked, and the simplicity-vs-fit trade-off it's probing (overview)
- Clarifying questions: which parts of this system have genuinely different access patterns — search, relationships, time-series? (concept)
- The answer skeleton: split storage only where the access pattern is genuinely different; justify each addition against its ops cost (concept)
- Walking it: a social app needing a relational store for accounts, a graph store for the follow graph, and a search index for posts (diagram)
- Walking it: a worked example — trying to force follow-graph traversal into the relational store, and the query complexity that results (concept)
- Walking it: a worked example — the operational runbook difference between backing up one relational instance vs three different storage systems (concept)
- The trade-off to name out loud: each specialized store fits its workload better but adds an operational surface — backups, monitoring, upgrades — that now multiplies (compare)
- Follow-up: "three databases means three things to operate — how do you justify that to your team?" (concept)
- Follow-up: "how do you keep the relational store and the search index in sync when a post is edited?" (concept)
- Pitfall: reaching for a specialized database for every feature without weighing the operational cost (pitfall)
- The 60-second version (concept)
- cross-link: polyglot-persistence

### Topic: Where do you draw the line between storing something in the DB vs blob storage? (iv-blob-vs-db, intermediate)
Tests whether you know why large binary objects don't belong in a relational row, and can name the reference-plus-blob pattern.
- The question as asked, and the "just put it in a column" mistake it's testing against (overview)
- Clarifying questions: what's the size and access pattern of this object — small structured data, or a large binary file? (concept)
- The answer skeleton: structured/queryable/small → DB; large/binary/rarely-queried → blob store with a DB reference (concept)
- Walking it: storing a user's avatar URL in the DB row, the image bytes in object storage (S3/GCS-style) (concept)
- Walking it: a worked example — the write path: upload to blob store first, then write the URL to the DB row only after the upload succeeds (code)
- Walking it: a worked example — signed/pre-signed URLs so clients upload directly to blob storage without routing bytes through the app tier (code)
- The trade-off to name out loud: blob storage is far cheaper per GB but adds an extra network hop and a two-system consistency problem (compare)
- Follow-up: "what if you need to query metadata about the blob, like its upload date?" — store metadata in DB, bytes in blob store (concept)
- Follow-up: "the DB write succeeds but the blob upload fails — what state is the record in now?" (concept)
- Pitfall: storing images or PDFs as BLOBs directly in relational rows at scale (pitfall)
- The 60-second version (concept)
- cross-link: object-and-blob-storage

### Topic: How do you keep data consistent when a transaction spans multiple services? (iv-transactions-across-services, advanced)
Tests whether you know that distributed transactions across service boundaries need a saga or 2PC-style pattern, and can pick the right one with its trade-off.
- The question as asked, and why a normal DB transaction can't reach across services (overview)
- Clarifying questions: does this need strict atomicity, or is eventual consistency with compensation acceptable? (concept)
- The answer skeleton: name the saga pattern (orchestration or choreography) and its compensating actions (concept)
- Walking it: an order-payment-inventory saga with a compensating refund step if inventory fails (diagram)
- Walking it: a worked example — orchestration (a central coordinator calls each step) vs choreography (each service reacts to the last one's event) for the same saga (compare)
- Walking it: a worked example — the exact events emitted and consumed at each saga step, including the compensating event for a failed step (code)
- The trade-off to name out loud: orchestration is easier to reason about and debug; choreography is more decoupled but harder to trace end to end (compare)
- Follow-up: "what if the compensating action itself fails?" — retries, dead-letter, and manual reconciliation (concept)
- Follow-up: "how do you test a saga's failure paths before they happen in production?" (concept)
- Pitfall: reaching for two-phase commit across services and underestimating its availability cost (pitfall)
- The 60-second version (concept)
- cross-link: distributed-transactions-and-sagas

### Topic: How would you migrate this table's schema with zero downtime? (iv-zero-downtime-schema-migration, advanced)
Tests whether you know the expand-migrate-contract pattern for live schema changes, instead of assuming a migration means a maintenance window.
- The question as asked, and why "just run the migration" undersells what breaks in production (overview)
- Clarifying questions: is this an additive change (new column) or a breaking one (rename, type change, drop)? (concept)
- The answer skeleton: expand (add the new shape, dual-write), migrate (backfill old data), contract (remove the old shape) — never a single atomic cutover (concept)
- Walking it: a worked example — renaming a column by adding the new one, writing to both, backfilling old rows, then dropping the old column weeks later (code)
- Walking it: keeping old and new application code compatible with both schema shapes during the transition window (concept)
- Walking it: a worked example — using an online-schema-change tool so a multi-million-row ALTER never locks the table (code)
- The trade-off to name out loud: expand-contract avoids downtime but stretches the migration over days or weeks, and every service must tolerate both shapes for that whole window (compare)
- Follow-up: "the backfill is still running and a new deploy needs the new column NOT NULL — what do you do?" (concept)
- Follow-up: "how do you know it's safe to finally drop the old column?" (concept)
- Pitfall: running an in-place ALTER that locks the table on a dataset too large for the maintenance window (pitfall)
- The 60-second version (concept)
- cross-link: schema-evolution-and-compatibility

### Topic: A table has grown too big — what do you do? (iv-table-too-big-fix, advanced)
Tests whether you can name concrete remedies — archiving, partitioning, tiering — for an oversized table, distinguishing "too big to query fast" from "too big to fit cheaply."
- The question as asked, and the two different problems "too big" can mean (overview)
- Clarifying questions: is the pain slow queries, expensive storage, or both — and is old data still accessed? (concept)
- The answer skeleton: partition/shard for query speed; archive cold data to cheaper storage for cost; both if both hurt (concept)
- Walking it: a worked example — partitioning an events table by month, so queries for "this month" never scan the other 23 (concept)
- Walking it: archiving rows older than a retention window to cold/blob storage, with a rehydration path if they're ever needed (concept)
- Walking it: a worked example — the size and row-count thresholds that should trigger this conversation before it becomes an incident (concept)
- The trade-off to name out loud: archiving cuts cost hard but makes old-data queries slower and more complex — decide who actually needs that data and how fast (compare)
- Follow-up: "a report needs to query across both hot and archived data — how do you serve that?" (concept)
- Follow-up: "how did the table get this big before anyone noticed — what would you monitor to catch it earlier next time?" (concept)
- Pitfall: adding more read replicas to "fix" a table that's slow because of its size and layout, not read load (pitfall)
- The 60-second version (concept)

### Topic: When would you denormalize this data model? (iv-when-to-denormalize, intermediate)
Tests whether you can justify denormalization by a specific read pattern and accept its write-side cost explicitly, rather than doing it reflexively "for performance."
- The question as asked, and the "denormalize for speed" reflex it's testing (overview)
- Clarifying questions: what's the read pattern that a normalized join is currently too slow or too expensive for? (concept)
- The answer skeleton: denormalize when reads vastly outnumber writes and the join cost is measurably too high; accept the update-anomaly risk explicitly (concept)
- Walking it: a worked example — embedding a commenter's display name on each comment document instead of joining to the users table on every read (compare)
- Walking it: what breaks when the source of truth changes — the user renames themselves, and every embedded copy is now stale (concept)
- Walking it: a worked example — measuring the join's actual latency cost under load before deciding it's worth denormalizing at all (concept)
- The trade-off to name out loud: denormalization buys read speed at the cost of update fan-out — one write becomes N writes, or you accept staleness (compare)
- Follow-up: "the user's name needs to update everywhere within a day — how do you propagate that?" (concept)
- Follow-up: "would a cache achieve the same win without denormalizing the data model itself?" (concept)
- Pitfall: denormalizing before measuring that the join is actually the bottleneck (pitfall)
- The 60-second version (concept)
- cross-link: nosql-data-models

### Topic: How would you store and query time-series data at scale? (iv-time-series-data-design, advanced)
Tests whether you know the shape time-series workloads actually take — append-only writes, time-range queries, aggressive rollup/downsampling — instead of treating it like generic relational data.
- The question as asked, and what makes time-series data a different design problem (overview)
- Clarifying questions: what's the write rate, the retention period, and the typical query — a single point, or a range/aggregate? (concept)
- The answer skeleton: partition by time range, write append-only, downsample old data instead of keeping full resolution forever (concept)
- Walking it: a worked example — metrics ingested at 1-second resolution, downsampled to 1-minute after a day and to 1-hour after a month (code)
- Walking it: choosing a store built for this shape (a time-series or wide-column database) vs forcing it into a generic relational table (compare)
- Walking it: a worked example — a query for the last 24 hours at 1-second resolution hitting the hot tier, and the last year at 1-hour resolution hitting the rolled-up tier (code)
- The trade-off to name out loud: downsampling cuts storage hard but permanently discards fine-grained history — decide upfront what resolution you'll actually need later (compare)
- Follow-up: "someone needs full 1-second resolution from six months ago for an incident review — do you have it?" (concept)
- Follow-up: "how do you handle a burst of out-of-order or late-arriving data points?" (concept)
- Pitfall: storing raw time-series data forever at full resolution in a general-purpose relational table (pitfall)
- The 60-second version (concept)

### Topic: How do you handle relationships between entities in a NoSQL data model? (iv-handling-relations-in-nosql, advanced)
Tests whether you know the two real techniques — embedding and referencing — and can pick per relationship instead of assuming NoSQL "can't do relationships."
- The question as asked, and the "NoSQL has no joins" oversimplification it's testing against (overview)
- Clarifying questions: is this a one-to-few, one-to-many, or many-to-many relationship, and how often does the related data change? (concept)
- The answer skeleton: embed for one-to-few and rarely-changing data read together; reference (and fetch separately or via application-side join) for one-to-many or many-to-many (concept)
- Walking it: a worked example — embedding a small, fixed list of order line-items inside the order document vs referencing a user ID from a post document (compare)
- Walking it: a many-to-many case — a tags-on-posts relationship modeled with a join collection, queried with two lookups instead of one join (concept)
- Walking it: a worked example — the two-lookup application-side join required to fetch a post plus its author, and where that logic lives (code)
- The trade-off to name out loud: embedding is fast to read but duplicates data and complicates updates; referencing avoids duplication but pushes the join into application code (compare)
- Follow-up: "the embedded list of line-items keeps growing unbounded — is embedding still right?" (concept)
- Follow-up: "how would you enforce something like a foreign-key constraint here, since the database won't do it for you?" (concept)
- Pitfall: embedding an unbounded, frequently-changing relationship and hitting document size limits or write amplification (pitfall)
- The 60-second version (concept)
- cross-link: nosql-data-models

---

## Group: Consistency & Replication — Interview Questions (interview-hld-consistency)
*consistency model choice, replication lag, read-your-writes, quorum tuning, conflict resolution, idempotency, distributed transactions, stale-read triage, network partitions, split-brain, and leader failover/election*

### Topic: What consistency model would you choose for this system, and why? (iv-choosing-consistency-model, advanced)
Tests whether you can pick strong, eventual, or causal consistency for a specific stated feature and defend the user-facing consequence, not just define the terms.
- The question as asked, and why naming the models isn't the same as choosing one (overview)
- Clarifying questions: which specific operation is being asked about — this system likely needs more than one model (concept)
- The answer skeleton: pick per-feature, not system-wide; state the user-visible cost of your choice (concept)
- Walking it: strong consistency for a bank balance, eventual for a view counter, causal for a comment thread (compare)
- Walking it: a worked example — implementing causal consistency for the comment thread so replies never appear before the comment they're replying to (concept)
- Walking it: a worked example — the interviewer names a fourth feature live and asks you to classify it on the spot (concept)
- The trade-off to name out loud: stronger consistency costs latency and availability during a partition; weaker consistency costs correctness the user can see (compare)
- Follow-up: "the product team wants everything to feel instant AND always correct — what do you tell them?" (concept)
- Follow-up: "how do you explain 'eventual' in a way a non-engineer stakeholder will accept?" (concept)
- Pitfall: picking one consistency model for the entire system instead of per feature (pitfall)
- The 60-second version (concept)
- cross-link: consistency-models

### Topic: Replication lag just spiked — what breaks, and how do you defend against it? (iv-replication-lag-impact, advanced)
Tests whether you can name concrete failure symptoms of replication lag (stale reads, phantom disappearing data) and a real mitigation, not just "replicas can lag."
- The question as asked, and the vague "replicas can be stale" non-answer it's testing against (overview)
- Clarifying questions: are reads going to replicas at all, or only writes — where does lag actually surface? (concept)
- The answer skeleton: name the user-visible symptom, then the mitigation — read-after-write routing, lag monitoring, replica health checks (concept)
- Walking it: a user posts a comment, refreshes, and it's gone because the read hit a lagging replica (diagram)
- Walking it: a worked example — replication lag jumping from 50ms to 8 seconds during a bulk write job, and what that does to every reader (code)
- Walking it: a worked example — a lag-monitoring alert firing when lag crosses a stated threshold (e.g. 2 seconds), before users complain (concept)
- The trade-off to name out loud: routing more reads to the primary to dodge lag protects correctness but removes the scaling benefit replicas exist for (compare)
- Follow-up: "how would you even detect that lag has grown, before users complain?" (concept)
- Follow-up: "the bulk write job is the actual cause — do you fix the symptom or the root cause?" (concept)
- Pitfall: assuming replication lag is milliseconds and never budgeting for a multi-second spike (pitfall)
- The 60-second version (concept)
- cross-link: synchronous-vs-asynchronous-replication

### Topic: How would you guarantee a user sees their own write immediately? (iv-read-your-own-writes, advanced)
The read-your-writes question — tests whether you know concrete techniques (sticky reads to primary, session tokens, client-side caching) beyond "use strong consistency everywhere."
- The question as asked, and why "just use strong consistency" is too broad an answer (overview)
- Clarifying questions: does this need to hold only for the writing user, or for every reader? (concept)
- The answer skeleton: route the writer's own subsequent reads to the primary (or a replica known to be caught up) (concept)
- Walking it: a session-pinning approach — reads within the same session go to primary for a short window after a write (concept)
- Walking it: an alternative — the client optimistically renders its own write locally, then reconciles when the read confirms it (concept)
- Walking it: a worked example — tagging each write with a version/timestamp, and routing the next read to whichever replica has caught up past it (code)
- The trade-off to name out loud: session-pinning is simple but keeps sending that user's reads to the (more loaded) primary for the whole window (compare)
- Follow-up: "what if the user switches devices right after writing?" (concept)
- Follow-up: "how long does the pinning window need to last, and how do you pick that number?" (concept)
- Pitfall: applying strong consistency to all reads system-wide just to fix this one case (pitfall)
- The 60-second version (concept)
- cross-link: consistency-models

### Topic: How would you tune read/write quorum for this system's needs? (iv-tuning-quorum, advanced)
Tests whether you can reason about the R+W>N trade-off for a specific latency/consistency target, not just recite the formula.
- The question as asked, and the formula it expects you to actually apply, not just state (overview)
- Clarifying questions: does this workload favor read latency, write latency, or strict consistency? (concept)
- The answer skeleton: pick R and W relative to N based on which side needs to be fast vs which needs to be safe (concept)
- Walking it: a worked example — N=3, W=1/R=3 for write-optimized vs W=3/R=1 for read-optimized, and R=W=2 as the balanced default (code)
- Walking it: what actually happens on a read when R=2 and the two replicas disagree — the newest timestamp wins, or a repair is triggered (concept)
- Walking it: a worked example — the measured latency difference between R=1/W=3 and R=3/W=1 for the same cluster (code)
- The trade-off to name out loud: R=W=2 balances both, but neither read nor write gets the lowest possible latency either one could have alone (compare)
- Follow-up: "a node is down — does your quorum setting still work?" (concept)
- Follow-up: "you set R+W=N instead of >N to save latency — what did you just give up, and did you mean to?" (concept)
- Pitfall: setting R+W=N (not > N) and losing the strong-consistency guarantee without realizing it (pitfall)
- The 60-second version (concept)
- cross-link: quorum-systems

### Topic: Two replicas got different writes for the same key — how do you resolve the conflict? (iv-conflict-resolution-choice, advanced)
Tests whether you can pick and justify a concrete conflict-resolution strategy (LWW, vector clocks, CRDTs, app-level merge) for the specific data type in question.
- The question as asked, and why "last write wins" isn't always the right default (overview)
- Clarifying questions: what does this data represent — is a silent overwrite acceptable, or does the merge itself matter? (concept)
- The answer skeleton: name the strategy that fits the data's semantics, not a system-wide default (concept)
- Walking it: LWW losing a legitimate concurrent edit vs a CRDT merging a shopping cart correctly by taking the union of both versions (compare)
- Walking it: a worked example — vector clocks detecting that two writes were truly concurrent (neither caused the other) before choosing how to merge (code)
- Walking it: a worked example — a shopping-cart CRDT correctly merging "added item A" and "removed item B" from two concurrent sessions (code)
- The trade-off to name out loud: CRDTs merge automatically and correctly for specific data shapes, but you can't bolt one onto arbitrary data — it constrains your data model (compare)
- Follow-up: "how would you even detect that a conflict happened, if resolution is automatic?" (concept)
- Follow-up: "the merge itself needs business logic no generic strategy can supply — what then?" — surface it to the user or app layer (concept)
- Pitfall: applying last-write-wins to data where silently dropping one write is actually a bug, like inventory counts (pitfall)
- The 60-second version (concept)
- cross-link: conflict-resolution

### Topic: How would you make this API endpoint safe to retry? (iv-idempotency-in-practice, intermediate)
Tests whether you can implement idempotency concretely — an idempotency key, a dedup table — not just say "make it idempotent."
- The question as asked, and why "just make it idempotent" needs a mechanism to back it up (overview)
- Clarifying questions: is the risk client retries, at-least-once delivery from a queue, or both? (concept)
- The answer skeleton: client generates an idempotency key, server stores it with the result, and dedupes on retry (concept)
- Walking it: a worked example — a payment endpoint using a client-generated request ID stored for 24h, keyed to the response it returned (code)
- Walking it: what the dedup store itself needs — a unique constraint and a TTL, so it doesn't grow forever (concept)
- Walking it: a worked example — the dedup table's schema itself: idempotency_key, response_body, created_at, cleaned up by a TTL job (code)
- The trade-off to name out loud: idempotency keys add a storage and lookup cost to every request in exchange for safe retries — worth it exactly where retries are expected (compare)
- Follow-up: "what if the first request is still in flight when the retry arrives?" — lock the key while processing (concept)
- Follow-up: "the client never sent an idempotency key at all — can you make the endpoint safe anyway?" — natural idempotency via upserts where possible (concept)
- Pitfall: relying on the operation being "naturally idempotent" (like a PUT) when it has side effects that aren't (pitfall)
- The 60-second version (concept)
- cross-link: idempotency-and-exactly-once

### Topic: Would you use a distributed transaction here, or avoid one — and how? (iv-distributed-transaction-tradeoff, expert)
The senior framing of the cross-service consistency question — tests whether you default to avoiding distributed transactions and can justify when (rarely) 2PC is actually worth its availability cost.
- The question as asked, and why the expected default answer is "avoid it" (overview)
- Clarifying questions: how many services are involved, and is atomicity truly required or just eventual correctness? (concept)
- The answer skeleton: prefer sagas/compensation by default; justify 2PC only for a small, tightly-coupled, low-latency set of participants (concept)
- Walking it: why 2PC's blocking coordinator becomes a new availability bottleneck at scale — every participant holds locks until the coordinator decides (concept)
- Walking it: a worked example — the one narrow case (a small number of internal, co-located services, strict atomicity required) where 2PC is defensible (concept)
- Walking it: a worked example — estimating the lock-hold duration 2PC would need here, and the throughput ceiling that implies (concept)
- The trade-off to name out loud: 2PC gives real atomicity, sagas give availability — you cannot have both fully, so name which one this feature actually needs (compare)
- Follow-up: "the business insists on 'no partial state, ever' — how do you push back or accommodate it?" (concept)
- Follow-up: "what happens if the 2PC coordinator itself crashes mid-transaction?" (concept)
- Pitfall: reaching for 2PC as the first idea instead of the last resort (pitfall)
- The 60-second version (concept)
- cross-link: distributed-transactions-and-sagas

### Topic: For this specific feature, would you pick strong or eventual consistency? (iv-strong-vs-eventual-for-this-feature, advanced)
A narrower, feature-scoped rerun of the consistency-model question — forces a binary commitment with a concrete cost, used as a rapid-fire follow-up drill across several small features in one interview.
- The question as asked, and why interviewers ask this rapid-fire across several small features (overview)
- Clarifying questions: what's the cost of showing stale data here, in concrete user terms? (concept)
- The answer skeleton: state the user-visible cost of being wrong in each direction, then commit (concept)
- Walking it: rapid-fire across three features — follower count (eventual), payment status (strong), typing indicator (eventual) (compare)
- Walking it: a worked example — walking the interviewer through *why* follower count tolerates being off by a few, second by second (concept)
- Walking it: a worked example — the interviewer adds a fourth feature (unread message count) mid-drill and asks for an instant call (concept)
- The trade-off to name out loud: choosing strong "to be safe" for a feature that doesn't need it quietly caps your scalability for no user-facing benefit (compare)
- Follow-up: "you said eventual for follower count — how eventual? Seconds? Minutes?" (concept)
- Follow-up: "the same feature needs strong consistency for one internal audience (finance) but eventual is fine for the user-facing view — one system or two?" (concept)
- Pitfall: giving the theoretically "safer" answer (strong) for everything to avoid being wrong (pitfall)
- The 60-second version (concept)
- cross-link: consistency-models

### Topic: A user says they saw stale or wrong data — how do you investigate and fix it? (iv-diagnosing-a-stale-read-complaint, advanced)
A post-incident triage question distinct from the proactive replication-lag design question — tests whether you have a concrete debugging path from "user complaint" to root cause, across the several places staleness can hide.
- The question as asked, and how it differs from designing against lag up front (overview)
- Clarifying questions: stale by how much, and does it correlate with a specific action (right after a write) or seem random? (concept)
- The answer skeleton: walk the read path backward — client cache, CDN, app cache, replica lag — checking each layer for where staleness could be introduced (concept)
- Walking it: a worked example — the complaint says "I saved my profile and it reverted" — tracing it to a cache-aside race, not replication lag at all (diagram)
- Walking it: checking replica lag metrics for the time window of the complaint, to rule that layer in or out fast (concept)
- Walking it: a worked example — a runbook checklist ordered by how cheap each check is to run, so triage starts with the fastest checks (concept)
- The trade-off to name out loud: a fast, layer-by-layer triage script gets you to root cause quickly; guessing based on the last incident you had is how you fix the wrong layer (compare)
- Follow-up: "you found the layer — is this a one-off, or does it affect every user right now?" (concept)
- Follow-up: "how do you build a dashboard so the next one of these takes minutes, not an investigation?" (concept)
- Pitfall: assuming every staleness complaint is replication lag and never checking the cache layers first (pitfall)
- The 60-second version (concept)
- cross-link: cache-invalidation

### Topic: A network partition just happened — walk me through what your system does (iv-network-partition-walkthrough, advanced)
Tests whether you can trace concrete, step-by-step behavior during a live partition — not recite CAP theory, but say what each side of the split actually does to requests arriving right now.
- The question as asked, and why this is CAP theory applied moment-by-moment, not restated (overview)
- Clarifying questions: which two components got split, and which side (if either) holds the majority for quorum purposes? (concept)
- The answer skeleton: name what the majority side does (keeps serving), what the minority side does (per your CP/AP choice), and what happens when it heals (concept)
- Walking it: a worked example — a 5-node cluster split 3/2; the 3-node majority keeps accepting writes, the 2-node minority goes read-only or rejects writes (diagram)
- Walking it: what happens the moment the partition heals — reconciling any writes the minority side accepted, if it accepted any at all (concept)
- Walking it: a worked example — a client on the minority side retrying its write every few seconds until the partition heals and it finally succeeds (concept)
- The trade-off to name out loud: letting the minority side stay available for reads risks serving stale data; refusing entirely is safer but costs those users availability (compare)
- Follow-up: "the partition lasts 10 minutes, not 10 seconds — does your answer change?" (concept)
- Follow-up: "how does the system even know a partition is happening, versus a node just being slow?" (concept)
- Pitfall: describing CAP theory in the abstract without saying what actually happens to an in-flight request during the split (pitfall)
- The 60-second version (concept)
- cross-link: split-brain-and-quorum-loss

### Topic: How would you detect and resolve split-brain in this system? (iv-detecting-split-brain, expert)
Distinct from the general partition-behavior question — this is specifically about two nodes each believing they're the leader/primary at once, and the concrete mechanism (fencing, quorum, epoch numbers) that prevents or resolves it.
- The question as asked, and the specific failure it names — not "a partition happened" but "two leaders exist right now" (overview)
- Clarifying questions: is leadership decided by a consensus system (etcd/ZooKeeper-style) or a simpler heartbeat/lease scheme? (concept)
- The answer skeleton: prevent it with a quorum-backed lease and fencing tokens; detect it by an epoch/term number that both leaders can't share (concept)
- Walking it: a worked example — a fencing token attached to every write, so a stale ex-leader's writes are rejected by storage even if it still thinks it's in charge (code)
- Walking it: how the newer leader gets elected only once it holds a majority lease — the old one can't renew its lease without that majority (concept)
- Walking it: a worked example — a monitoring alert firing the moment two nodes report holding the same epoch/term as leader simultaneously (concept)
- The trade-off to name out loud: fencing tokens fully prevent split-brain damage but require every downstream system to actually check them — one component that skips the check reopens the hole (compare)
- Follow-up: "your fencing mechanism itself needs a quorum store — what happens if that store partitions too?" (concept)
- Follow-up: "how would you have caught this in a postmortem — what signal shows split-brain happened after the fact?" (concept)
- Pitfall: relying on heartbeats and timeouts alone to prevent split-brain, with no fencing to stop a "zombie" old leader from still writing (pitfall)
- The 60-second version (concept)
- cross-link: split-brain-and-quorum-loss

### Topic: Your leader/primary just failed over — what does the client experience? (iv-leader-failover-client-view, advanced)
Tests whether you can trace the failover from the client's point of view — in-flight requests, reconnection, and the consistency gap — not just say "a new leader gets elected."
- The question as asked, and why "a new leader gets elected" skips the part that actually matters (overview)
- Clarifying questions: is the client a stateless HTTP caller, or does it hold a persistent connection to the old leader? (concept)
- The answer skeleton: name what happens to in-flight requests, how the client discovers the new leader, and what it sees on its next request (concept)
- Walking it: a worked example — an in-flight write to the old leader that never got acknowledged; the client must safely retry against the new leader without double-applying it (diagram)
- Walking it: client-side discovery of the new leader — a service registry update, a DNS change, or a client-side retry-with-redirect (concept)
- Walking it: a worked example — a client SDK's built-in retry-with-backoff automatically finding the new leader with no manual intervention (code)
- The trade-off to name out loud: fast failover minimizes client-visible downtime but raises the odds of a request being replayed against the new leader — idempotency is what makes fast failover safe (compare)
- Follow-up: "how long is the client-visible blip, and what determines that number?" — detection time plus election time plus client retry backoff (concept)
- Follow-up: "the client had a long-lived connection to the old leader — does it need special handling beyond a stateless retry?" (concept)
- Pitfall: describing failover only from the server side and never addressing what the in-flight request's caller actually experiences (pitfall)
- The 60-second version (concept)
- cross-link: consensus-basics

### Topic: How would you approach leader election for a component in this design? (iv-leader-election-approach, expert)
Tests whether you can name a concrete, off-the-shelf mechanism (a consensus store like etcd/ZooKeeper, or a lease-based scheme) rather than trying to hand-roll leader election from scratch in the interview.
- The question as asked, and why "hand-roll it with heartbeats" is the wrong first instinct (overview)
- Clarifying questions: does a component genuinely need a single leader, or would each node acting independently actually work? (concept)
- The answer skeleton: reach for an existing consensus system to hold the lease; the leader is whoever currently holds it, with a renewal deadline (concept)
- Walking it: a worked example — a component acquiring a time-bound lease in etcd/ZooKeeper, renewing it periodically, and stepping down (or losing leadership) if renewal fails (code)
- Walking it: what every follower does while waiting — watch for the lease to free up, then race to acquire it (concept)
- Walking it: a worked example — the exact consensus-store API calls (create ephemeral key, watch, campaign) used to run the election (code)
- The trade-off to name out loud: using an existing consensus store is far safer than hand-rolled election, at the cost of taking a hard dependency on that store's own availability (compare)
- Follow-up: "the consensus store itself becomes unavailable — does your component have a leader at all right now?" (concept)
- Follow-up: "how short should the lease renewal interval be, and what's the trade-off in either direction?" (concept)
- Pitfall: implementing leader election from scratch with heartbeats and timeouts instead of using a proven consensus system (pitfall)
- The 60-second version (concept)
- cross-link: consensus-basics

---
