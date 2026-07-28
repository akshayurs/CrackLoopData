## Group: Messaging & Streaming — Interview Questions (interview-hld-messaging)
*when to use a queue, guaranteeing no message loss, exactly-once, ordering, Kafka vs queue, backpressure, event-driven migration, fan-out, partitioning, schema evolution, replay, poison messages*

### Topic: When would you put a queue between these two services, and when wouldn't you? (iv-when-to-use-a-queue, intermediate)
Tests whether you can justify decoupling with a queue against a concrete need (absorbing bursts, surviving downstream outages) rather than inserting one reflexively.
- The question as asked, and the "queues are always good practice" reflex it's testing (overview)
- Clarifying questions: does the caller need an immediate response, or can the work happen asynchronously? Does downstream ever go down or slow down? (concept)
- The answer skeleton: queue when the caller doesn't need a synchronous result, or needs to survive downstream being slow/down; skip it when the caller's next step depends on the result (concept)
- Walking it: checkout flow — a synchronous inventory check (caller needs the answer now, no queue) vs an async order-confirmation email (queue it via SQS) (compare)
- Walking it: a concrete scenario — 50K orders/day, the email service goes down for 10 minutes; without a queue, ~350 emails during that window just vanish; with SQS in front of the email worker, they queue and drain automatically once it recovers (concept)
- Walking it: what the queue buys you beyond "it survives an outage" — independent deploy cadence, independent scaling of the consumer, and a natural buffer for traffic bursts (concept)
- Diagram: producer → queue → consumer, with the retry-then-DLQ path drawn alongside the happy path (diagram)
- The trade-off to name out loud: a queue buys resilience and decoupling by giving up the ability to know synchronously whether the work succeeded — every hop you move behind a queue is a hop the caller can no longer get an answer about in the same request (compare)
- Follow-up: "the caller now needs to know if the async job succeeded — how do you tell them?" — a status endpoint the caller polls, or a webhook/callback once the job finishes (concept)
- Follow-up: "what if the queue broker itself goes down — haven't you just moved the single point of failure?" — managed/clustered brokers (SQS, MSK) with multi-AZ durability, so the broker's own availability is much higher than any one service it decouples (concept)
- Follow-up: "how much retention/buffer does this queue actually need?" — size it to the longest realistic downstream outage you want to survive, not an arbitrary default (concept)
- Pitfall: adding a queue to a synchronous request/response path and creating a polling problem instead of solving the original one (pitfall)
- The 60-second version (concept)
- cross-link: queues-vs-pubsub

### Topic: How do you guarantee a message isn't lost end-to-end? (iv-guaranteeing-no-message-loss, intermediate)
Tests whether you can name the concrete durability guarantee at every hop — producer ack, broker replication, consumer ack-after-processing — rather than assuming "we used a queue" is itself a loss guarantee.
- The question as asked, and why "it's in a queue, so it's safe" is not automatically true (overview)
- Clarifying questions: what's the acceptable loss rate — zero, or "vanishingly rare and we can detect it"? Which hop is riskiest — producer send, broker durability, or consumer processing? (concept)
- The answer skeleton: never lose a message by acknowledging too early at any hop — the producer waits for a durable broker ack, the broker replicates before acking, and the consumer only acks after the work is actually done (concept)
- Walking it: a worked example — a Kafka producer set to `acks=all` so the write isn't confirmed until it's replicated to all in-sync replicas, not just the leader (code)
- Walking it: the consumer side — process the message, persist the side effect, then ack; acking first and processing second means a crash between the two silently drops the message (concept)
- Walking it: a concrete scenario — a payment-event consumer that acks on receipt instead of after writing to its ledger; a pod restart mid-processing loses the event with the broker believing it was delivered successfully (concept)
- Diagram: the three loss windows — producer-to-broker, broker replication, consumer-crash-before-ack — and the setting that closes each one (diagram)
- The trade-off to name out loud: closing every loss window costs latency and throughput (`acks=all`, synchronous replication, ack-after-persist) — you're trading speed for durability, and the right amount of each depends on what a lost message actually costs the business (compare)
- Follow-up: "your producer got a timeout — did the message make it or not?" — retry with an idempotency key rather than assuming failure, since the write may have succeeded and only the ack was lost (concept)
- Follow-up: "how do you even detect a message was lost, if it's silent by definition?" — reconciliation: compare a count/checksum on the producer side against what the consumer eventually processed (concept)
- Pitfall: conflating "the broker accepted it" with "it's durable" — an unreplicated write on a single broker node is one disk failure from gone (pitfall)
- The 60-second version (concept)
- cross-link: message-delivery-semantics

### Topic: How would you actually achieve exactly-once processing here? (iv-exactly-once-in-practice, advanced)
Tests whether you know exactly-once is really at-least-once-delivery plus idempotent processing, not a delivery guarantee the broker gives you for free.
- The question as asked, and the misconception that a broker setting alone provides this (overview)
- Clarifying questions: is duplication a delivery-layer risk, a processing-layer risk, or both? What's the actual side effect that must not happen twice — a charge, an email, a row insert? (concept)
- The answer skeleton: accept at-least-once delivery as the reality, then make processing idempotent with a dedup key so a duplicate delivery is a no-op (concept)
- Walking it: a worked example — a payment consumer storing processed message IDs in a table with a unique constraint, checking-then-inserting inside the same transaction as the side effect (code)
- Walking it: a concrete scenario — a network blip causes the consumer's ack to be lost after it already charged the card; the broker redelivers the message 4 seconds later; the dedup check on `payment_intent_id` short-circuits before a second charge fires (concept)
- Walking it: where the dedup key should come from — a client-generated idempotency key when one exists, otherwise a stable hash of the message's business-meaningful fields, not the broker's own offset (concept)
- Diagram: at-least-once delivery + idempotent consumer = effectively-once outcome, drawn as two separate layers (diagram)
- The trade-off to name out loud: exactly-once processing costs you a dedup store and a lookup on every message — for high-volume, low-stakes events (view counts, impressions) that overhead may not be worth it versus tolerating rare duplicates (compare)
- Follow-up: "what if the dedup store itself is unavailable when the message arrives?" — fail closed (don't process, let it retry) rather than fail open and risk a double side effect, if the side effect is costly enough to justify it (concept)
- Follow-up: "the dedup table is growing forever — how do you bound it?" — TTL the dedup keys to the maximum realistic redelivery window, not forever (concept)
- Pitfall: setting a broker's "exactly-once" config (e.g., Kafka idempotent producer + transactions) and assuming duplicate *processing* is now impossible — that config only covers duplicate *writes from the producer*, not a consumer crashing after acting but before acking (pitfall)
- The 60-second version (concept)
- cross-link: message-delivery-semantics

### Topic: Does this system need strict ordering, and how would you provide it? (iv-ordering-guarantees-needed, advanced)
Tests whether you can identify which specific data needs ordering (per-key, not global) and name the mechanism (partition key) that provides it without sacrificing all parallelism.
- The question as asked, and the false choice between "totally ordered" and "no order at all" (overview)
- Clarifying questions: does ordering need to hold globally, or just per user/entity? What actually breaks if two events for *different* keys arrive out of order? (concept)
- The answer skeleton: per-key ordering via a consistent partition key almost always suffices; global ordering rarely does and costs you nearly all your parallelism (concept)
- Walking it: partitioning a Kafka topic by user ID so one user's events (e.g., `balance_debited` then `balance_credited`) stay ordered, while different users' events process fully in parallel across partitions (diagram)
- Walking it: a concrete scenario — an inventory system partitioned by `sku_id`; two updates to the same SKU always land on the same partition and process in order, while updates to 10,000 different SKUs fan out across 50 partitions (concept)
- Walking it: what happens if you pick the wrong key — partitioning by `region` when the real ordering dependency is per-`sku_id` gives you ordering you don't need and none of the ordering you do need (concept)
- Diagram: single-partition "totally ordered" topic vs 50-partition topic keyed by entity ID — throughput and ordering scope side by side (diagram)
- The trade-off to name out loud: ordering scope and parallelism trade off directly — the smaller and more granular your ordering key, the more parallelism you keep, but only within that key's guarantee (compare)
- Follow-up: "a message for a key fails and blocks that partition — what now?" — a per-key retry/DLQ so one poisoned key doesn't stall every other key sharing its partition (concept)
- Follow-up: "you need to repartition this topic later — does ordering survive that?" — it doesn't automatically; repartitioning can scatter a previously-ordered key across new partitions unless you migrate carefully (concept)
- Pitfall: assuming a single-partition topic is required for "ordering" and killing throughput for a guarantee the data didn't actually need at that scope (pitfall)
- The 60-second version (concept)
- cross-link: log-based-streaming

### Topic: Would you use Kafka or a traditional queue (SQS/RabbitMQ) for this? (iv-kafka-vs-traditional-queue, intermediate)
Tests whether the choice is grounded in replay needs and consumer count (Kafka's log model) vs simple task distribution (a queue's delete-on-ack model).
- The question as asked, and the "Kafka is just a better queue" misconception it's testing (overview)
- Clarifying questions: do multiple independent consumers need the same events, and do you need replay or an audit trail? Or is this one producer, one job, done once? (concept)
- The answer skeleton: Kafka for multi-consumer/replayable event logs; a queue for simple work distribution with delete-on-ack (concept)
- Walking it: a worked example — an `order_placed` event needed by 3 different services (billing, shipping, analytics) — Kafka, since each consumer group reads independently and can replay — vs an image-resize task queue with one producer and one worker pool — SQS, since each task is consumed once and discarded (compare)
- Walking it: a concrete scenario — analytics needs to reprocess 30 days of `order_placed` events after a bug in their aggregation; because Kafka retains the log, they replay from an earlier offset without asking the producer to resend anything; an SQS-based pipeline would have nothing left to replay (concept)
- Walking it: the operational cost difference — Kafka needs partition/consumer-group management and a cluster to run (or MSK to manage it); SQS is a fully managed, near-zero-ops primitive for a single work queue (concept)
- Diagram: Kafka's retained log with multiple independent consumer groups vs a queue's single logical consumer deleting on ack (diagram)
- The trade-off to name out loud: Kafka's replayability and fan-out come at the cost of operational complexity and a steeper mental model (offsets, consumer groups, partitions) that a plain queue doesn't ask of you (compare)
- Follow-up: "your queue-based job now also needs an audit trail of every message — does that change the choice?" — that requirement (replay/audit) is exactly Kafka's strength, so yes, it's worth reconsidering (concept)
- Follow-up: "could you get Kafka-like replay out of SQS without switching?" — only partially, e.g. archiving processed messages to S3 for replay tooling you build yourself, versus getting it for free from Kafka's log (concept)
- Pitfall: picking Kafka by default when there's exactly one consumer and no need to replay — you've bought cluster-operations overhead for nothing the use case needed (pitfall)
- The 60-second version (concept)

### Topic: Your consumer can't keep up with the producer — what do you do? (iv-handling-backpressure, advanced)
Tests whether you know concrete backpressure mechanisms (buffer-then-shed, slow the producer, scale the consumer) instead of just saying "add more consumers."
- The question as asked, and why "add more consumers" alone doesn't always fix it (overview)
- Clarifying questions: is the bottleneck consumer throughput itself, or a downstream dependency the consumer calls (e.g., a DB write it's waiting on)? Is the producer rate spiky or sustained? (concept)
- The answer skeleton: buffer within limits, then either scale consumers, slow the producer, or shed load — pick based on where the actual bottleneck is (concept)
- Walking it: a worked example — a queue depth alarm at 10,000 messages triggering consumer autoscaling from 5 to 20 pods, with a shed-oldest-first fallback if depth keeps climbing past 50,000 (diagram)
- Walking it: a concrete scenario — a notification consumer processes 200 msg/sec but a marketing blast produces 5,000 msg/sec for 3 minutes; scaling consumers 10x handles the burst in this case because the bottleneck really is consumer count, not a downstream limit (concept)
- Walking it: the case where scaling consumers doesn't help — if the real bottleneck is a downstream DB that maxes out at 200 writes/sec regardless of how many consumer pods call it, more consumers just shift the queue to the DB's connection pool instead of fixing anything (concept)
- Walking it: slowing the producer as an option — a rate limit or backoff signal sent back to the producer when the consumer signals it's saturated, rather than only ever buffering on the consumer side (concept)
- The trade-off to name out loud: buffering trades memory/latency for smoothing bursts, but an unbounded buffer just delays the failure and hides it as "everything's fine" until it OOMs or breaches an SLA on staleness (compare)
- Follow-up: "the producer can't be slowed and consumers can't scale further — now what?" — drop or degrade: shed the least valuable messages (e.g., non-critical notifications) rather than fail everything indiscriminately (concept)
- Follow-up: "how do you tell 'temporary burst' from 'the consumer is now permanently too slow'?" — trend the queue depth over the autoscaling window, not a single alarm firing; sustained growth despite max scale-out means capacity, not burst, is the problem (concept)
- Pitfall: letting an unbounded queue grow indefinitely instead of applying a depth limit with a shedding policy (pitfall)
- The 60-second version (concept)
- cross-link: backpressure-and-dead-letter-handling

### Topic: Would you make this interaction event-driven or request-response? (iv-event-driven-vs-request-response, intermediate)
Tests whether you can pick based on whether the caller needs an answer now versus just needs the side effect to eventually happen.
- The question as asked, and the coupling trade-off underneath the choice (overview)
- Clarifying questions: does the initiating flow need the result to proceed, or just needs to know the action was accepted? How many other services need to react to this same event? (concept)
- The answer skeleton: request-response when the caller blocks on the result; event-driven when it doesn't and/or multiple independent parties need to react (concept)
- Walking it: checkout needing an immediate inventory check (request-response — the UI can't proceed without the answer) vs notifying shipping, billing, and analytics that an order was placed (event-driven — none of them block the checkout flow) (compare)
- Walking it: a concrete scenario — adding a 4th consumer (fraud-scoring) to the "order placed" flow; with events, it's a new subscriber to an existing topic with zero changes to checkout; with request-response, checkout's code has to grow a new synchronous call to the fraud service, adding its latency and its failure mode to every checkout (concept)
- Walking it: the coupling cost that comes with event-driven — checkout no longer knows or controls what happens downstream, which is the point, but it also means checkout can't answer "did the fraud check pass" synchronously if a later requirement needs that (concept)
- Diagram: a request-response call chain vs a pub/sub fan-out from one event to N independent subscribers (diagram)
- The trade-off to name out loud: event-driven buys you loose coupling and easy fan-out at the cost of end-to-end traceability — you can no longer follow one causal chain in a single trace without stitching it back together (compare)
- Follow-up: "how do you debug a chain of five event-driven services when something silently didn't happen?" — correlation IDs propagated through every event, plus distributed tracing across the async boundary (concept)
- Follow-up: "the business now wants a single 'order status' view spanning all five services — how do you build that without going back to request-response?" — a materialized view/read model that subscribes to all the events and aggregates state, rather than querying each service synchronously (concept)
- Pitfall: making everything event-driven and losing the ability to reason about a request's end-to-end outcome, or the opposite — chaining five synchronous calls that should have been decoupled (pitfall)
- The 60-second version (concept)
- cross-link: event-driven-architecture

### Topic: How would you migrate this system from synchronous calls to an event-driven design? (iv-migrating-sync-to-async, advanced)
Tests whether you can sequence an incremental migration off a synchronous call chain — dual-publishing, a strangler consumer, verifying parity — rather than proposing a risky big-bang cutover.
- The question as asked, and why "just rewrite the call as a publish" isn't a safe answer on a live system (overview)
- Clarifying questions: which specific synchronous calls are the pain point — latency, coupling, or a downstream that can't scale to your caller's traffic? Can the caller tolerate any change in response shape during migration? (concept)
- The answer skeleton: introduce the event alongside the existing synchronous call first, prove the new consumer behaves correctly against real traffic, then remove the synchronous path once parity holds (concept)
- Walking it: a worked example — a checkout service currently calling the loyalty-points service synchronously; step 1 adds an `order_placed` event published in parallel with the existing call, with a shadow consumer that computes points but doesn't act on them yet (concept)
- Walking it: verifying parity — diffing the shadow consumer's computed points against the synchronous service's actual output for a week before trusting it (concept)
- Walking it: the cutover — once parity holds, flip the loyalty service to consume the event as its primary path, keep the old synchronous endpoint alive but unused for one more release as a rollback option, then delete it (diagram)
- The trade-off to name out loud: this migration path is slower and more expensive to run (dual-write period, shadow consumer, diffing) than a cutover, but it's the only version that doesn't bet the whole migration on a single weekend (compare)
- Follow-up: "the caller's flow currently depends on knowing loyalty points landed before showing a confirmation screen — how does that UX survive the async version?" — the confirmation screen shows immediately and points appear via a follow-up update (websocket/poll), which is itself a product conversation, not just an engineering one (concept)
- Follow-up: "how long do you run the old and new paths in parallel before you trust the cutover?" — until you've seen the new path hold up through your highest-traffic period (e.g., one full peak day or a full week), not an arbitrary fixed number of days (concept)
- Follow-up: "what if the old synchronous consumer's behavior can't be exactly replicated by an event, e.g., it returned an error the caller acted on?" — that's a case where async isn't a drop-in replacement and might mean the interaction should stay synchronous (concept)
- Pitfall: switching the publish path and removing the synchronous call in the same release, with no shadow-verification step to catch a behavioral mismatch before it's live (pitfall)
- The 60-second version (concept)
- cross-link: event-driven-architecture
- cross-link: strangler-fig-and-migration-patterns

### Topic: Multiple services need to react to the same event — how do you design that fan-out? (iv-designing-fanout-pubsub, intermediate)
Tests whether you can name the pub/sub mechanics (topic, independent consumer groups, per-subscriber retry) that let N services react to one event without coupling to each other or to the producer.
- The question as asked, and the anti-pattern (the producer calling each consumer directly) it's implicitly checking you avoid (overview)
- Clarifying questions: how many subscribers exist today, and is that number expected to grow? Does each subscriber need every event, or a filtered subset? (concept)
- The answer skeleton: publish once to a topic; each subscriber gets its own consumer group with its own offset, so one slow or failing subscriber never blocks another (concept)
- Walking it: a worked example — an `order_placed` topic with three consumer groups (billing, shipping, analytics), each tracking its own offset independently, using SNS→SQS fan-out or Kafka consumer groups (diagram)
- Walking it: a concrete scenario — analytics' consumer falls behind by 2 hours during a batch job; because it has its own offset, billing and shipping are completely unaffected and keep processing in near-real-time (concept)
- Walking it: filtering — when a new subscriber only cares about a subset of events (e.g., only orders over $500), filter at the subscriber (or via topic filter policies in SNS) rather than asking the producer to know about every consumer's needs (concept)
- The trade-off to name out loud: pub/sub fan-out decouples the producer from ever knowing who's listening, but that same decoupling means the producer can't tell you at publish time whether all the "important" subscribers actually received and processed the event — you need per-subscriber monitoring for that (compare)
- Follow-up: "a new, 4th subscriber needs to be added — does the producer need to change?" — no, that's the whole point; it just subscribes to the existing topic, which is the strongest signal this pattern is working (concept)
- Follow-up: "one subscriber needs the event delivered exactly once and another can tolerate duplicates — do they need different infrastructure?" — no, same topic; the stricter subscriber adds its own idempotent processing/dedup, the looser one doesn't bother (concept)
- Pitfall: having the producer call each subscriber's API directly "for now" — every new subscriber becomes a change to the producer and a new failure mode on its critical path (pitfall)
- The 60-second version (concept)
- cross-link: queues-vs-pubsub

### Topic: How many partitions would you use, and how do you scale consumers as load grows? (iv-partition-count-and-consumer-scaling, advanced)
Tests whether you understand that partition count is the hard ceiling on consumer parallelism, and can reason about picking a count with room to grow without over-provisioning.
- The question as asked, and why this number can't just be "however many you want later" (overview)
- Clarifying questions: what's the expected peak throughput, and what's the per-partition throughput ceiling for your message size and processing cost? Can consumers scale out, or is this a fixed pool? (concept)
- The answer skeleton: pick partition count from target throughput divided by per-partition capacity, with headroom for growth, because you can't shrink partitions later without a migration (concept)
- Walking it: a worked example — a topic needing 50,000 msg/sec, each partition sustaining roughly 5,000 msg/sec — that's 10 partitions minimum; picking 24 leaves room to scale consumers to 24 without a repartition (concept)
- Walking it: the hard constraint this creates — one partition can only be read by one consumer within a consumer group at a time, so consumer parallelism is capped at the partition count no matter how many pods you add beyond it (diagram)
- Walking it: a concrete scenario — a consumer group scaled from 10 to 30 pods on a 10-partition topic; the extra 20 pods sit completely idle because there's nothing left to assign them (concept)
- The trade-off to name out loud: more partitions buys you future consumer headroom but costs you more open file handles/replicas on the broker side and can hurt per-partition ordering guarantees if you didn't need that many keys — pick from projected load, not "as many as possible" (compare)
- Follow-up: "you're at your partition ceiling and still need more throughput — what now?" — repartition (a real migration with a consumer-side cutover plan), or reduce per-message cost so each partition does more work in the same time (concept)
- Follow-up: "does adding partitions to an existing topic break ordering for keys already in flight?" — yes, potentially — messages for the same key can start landing on a different partition after repartitioning unless you plan the transition carefully (concept)
- Pitfall: starting with a low partition count "since that's all we need today" on a topic you know will need to scale 10x within the year, guaranteeing a disruptive repartition later (pitfall)
- The 60-second version (concept)
- cross-link: log-based-streaming

### Topic: The producer changed its message format — how do you avoid breaking every consumer? (iv-message-schema-evolution, intermediate)
Tests whether you can name concrete compatibility rules (additive-only changes, a schema registry, versioned schemas) instead of just "we'd coordinate the deploy."
- The question as asked, and why "we'll just deploy consumers and producers together" doesn't scale past one team (overview)
- Clarifying questions: how many independent consumers read this topic, and are they all owned by your team or by others you can't force to redeploy on your schedule? (concept)
- The answer skeleton: make changes backward-compatible by default (add optional fields, never remove or repurpose a field), and enforce that with a schema registry that rejects incompatible changes at publish time (concept)
- Walking it: a worked example — adding an optional `promo_code` field to an `order_placed` event; old consumers that don't know about it simply ignore it and keep working unmodified (code)
- Walking it: a concrete scenario — a producer team renames `user_id` to `customer_id` without warning; three consumer teams start seeing null values for a field they depend on and their pipelines silently produce wrong aggregates for two days before anyone notices (concept)
- Walking it: how a schema registry (e.g., Confluent Schema Registry, AWS Glue Schema Registry) prevents this — it validates a new schema against compatibility rules before allowing the producer to publish with it, catching a breaking change at deploy time instead of at every consumer's runtime (diagram)
- The trade-off to name out loud: strict backward-compatibility rules slow down producer-side changes (you can't just remove that field you regret adding) in exchange for consumers never breaking without warning — for a topic with many external consumers, that trade is almost always worth it (compare)
- Follow-up: "you genuinely need to remove a field everyone agreed is legacy — how do you do that safely?" — deprecate it first (stop writing meaningful values, keep it present), confirm via consumer-side monitoring that nothing reads it anymore, then remove it in a new schema version (concept)
- Follow-up: "how do you even know which consumers depend on which fields before you make a change?" — schema registry usage/lineage tooling, or a lighter-weight team convention of documenting field consumers, since the broker itself doesn't track this (concept)
- Pitfall: treating the message schema as an internal implementation detail you can change freely because "it's just JSON," when in practice it's a public contract with every consumer team (pitfall)
- The 60-second version (concept)

### Topic: A bug corrupted a day of processed events — how do you replay/reprocess safely? (iv-replaying-and-reprocessing, advanced)
Tests whether you can name the mechanics of safe replay — retained log offsets, idempotent consumers, and isolating replay traffic from live traffic.
- The question as asked, and why replay is only safe if you designed for it upfront (overview)
- Clarifying questions: is the log/topic retention long enough to still have that day's events? Did the bug corrupt the events themselves, or just how a consumer processed them? (concept)
- The answer skeleton: reset the consumer offset to before the bug, reprocess through idempotent consumers, and isolate replay output from live output until it's verified (concept)
- Walking it: a worked example — replaying into a shadow table first, diffing row-by-row against what production actually wrote, then promoting the corrected data only after the diff comes back clean (diagram)
- Walking it: a concrete scenario — a billing aggregation bug double-counted refunds for 6 hours; the fix replays that 6-hour window from Kafka (7-day retention covers it) into a shadow aggregation table, confirms the corrected totals against a manual sample, then swaps the shadow table in as the source of truth (concept)
- Walking it: what happens if retention had already expired — without the log, you're reconstructing from whatever secondary source exists (a data warehouse copy, an audit log), which is strictly worse and is the argument for setting retention with replay scenarios in mind, not just normal operation (concept)
- The trade-off to name out loud: replaying into a shadow location and diffing before promoting costs you time and a temporary doubling of storage/compute, but replaying straight into production trades that cost for the risk of a second, live-traffic-visible incident on top of the first one (compare)
- Follow-up: "what if downstream systems already double-counted from the bad run — do you need to undo anything?" — yes, likely a targeted correction/compensating write to those downstream systems, which is often the harder half of the incident, not the replay itself (concept)
- Follow-up: "how do you replay without also re-triggering side effects like duplicate emails to customers?" — replay through a path where non-idempotent side effects are suppressed or the dedup key is honored, not the exact same live consumer code path unmodified (concept)
- Pitfall: replaying directly into production without idempotent consumers, doubling every side effect the first bad run already caused (pitfall)
- The 60-second version (concept)

### Topic: A message keeps failing and blocking the queue — how do you handle it? (iv-poison-message-handling, intermediate)
The poison-message question — tests whether you know retry-with-limit plus a dead-letter queue, not just "retry until it works."
- The question as asked, and why infinite retry is itself the failure mode (overview)
- Clarifying questions: is the failure transient (a downstream blip) or permanent (a malformed message that will never succeed)? Is this message blocking others behind it, or processing independently? (concept)
- The answer skeleton: retry with backoff up to a limit, then move it to a dead-letter queue for manual or automated triage instead of retrying forever (concept)
- Walking it: a worked example — a max-retry count of 5 with exponential backoff on the consumer, then a DLQ with a CloudWatch/Datadog alert firing the moment anything lands in it (code)
- Walking it: a concrete scenario — a malformed JSON payload from a buggy upstream client fails deserialization every single time; without a retry limit, it retries forever and, on a FIFO/ordered queue, blocks every message behind it; with a 5-retry cap and a DLQ, it's isolated within seconds and the queue keeps moving (concept)
- Walking it: what "triage" actually looks like — an on-call runbook step that inspects the DLQ payload, decides fix-and-replay vs discard, and either republishes a corrected message or documents why it's safe to drop (diagram)
- The trade-off to name out loud: a low retry limit isolates poison messages fast but risks DLQ-ing a message that would have succeeded on the 6th try during a longer blip — tune the limit and backoff to the failure patterns you actually see, not a guess (compare)
- Follow-up: "the DLQ is filling up — how do you decide what to do with those messages?" — bucket by failure reason (schema error vs downstream timeout) since each bucket has a different fix, rather than triaging one-by-one (concept)
- Follow-up: "can you automate any of the DLQ triage instead of a human looking at every message?" — yes for known failure signatures (auto-republish on a known-transient error code), but a novel failure reason should still page a human the first time it's seen (concept)
- Pitfall: retrying forever and letting one bad message block every message behind it in the same partition/ordered queue (pitfall)
- The 60-second version (concept)
- cross-link: backpressure-and-dead-letter-handling

---

## Group: APIs & Resilience — Interview Questions (interview-hld-apis-resilience)
*REST vs gRPC vs GraphQL, pagination, versioning, long-running requests, rate limiter design, protecting/isolating dependencies, retry storms, circuit breakers, timeout budgets, partial failure, webhook delivery, graceful degradation*

### Topic: Would you use REST, gRPC, or GraphQL for this API, and why? (iv-rest-vs-grpc-vs-graphql, intermediate)
Tests whether the choice is grounded in the actual caller (browser vs internal service), payload shape, and over/under-fetching concerns, not familiarity alone.
- The question as asked, and the "REST because that's what I know" answer it's testing against (overview)
- Clarifying questions: who's the caller — a browser client, a mobile app, or another internal service? How many different "shapes" of data do callers need from the same resource? (concept)
- The answer skeleton: REST for public/simple CRUD; gRPC for internal low-latency service-to-service; GraphQL when clients need flexible, varying shapes (concept)
- Walking it: a mobile app with a feed screen needing 5 fields and a profile screen needing 40 fields off the same user object — GraphQL lets each screen ask for exactly what it needs instead of over-fetching the full object every time (compare)
- Walking it: a concrete scenario — an internal order-service-to-inventory-service call happening 20,000 times/sec; switching from REST/JSON to gRPC/protobuf cuts payload size roughly 3-5x and serialization cost noticeably, which matters at that call volume in a way it wouldn't at 20 calls/sec (concept)
- Walking it: what GraphQL costs you operationally — a single endpoint means you lose per-resource HTTP caching and rate limiting, and you now need query complexity limits so one nested query can't fan out into thousands of backend calls (concept)
- The trade-off to name out loud: each option trades something for flexibility — GraphQL trades simple caching/rate-limiting for flexible shapes, gRPC trades human-readability/browser support for speed, REST trades some flexibility for the simplest possible mental model (compare)
- Follow-up: "what does gRPC cost you that REST doesn't?" — no native browser support (needs gRPC-Web plus a proxy), binary payloads aren't human-readable in a debugger, and tooling maturity for gRPC is less universal (concept)
- Follow-up: "your GraphQL API just got a query that joins 8 nested resources and timed out — what do you do?" — a query complexity/depth limit enforced at the gateway, and dataloader-style batching so nested resolvers don't turn into N+1 backend calls (concept)
- Pitfall: picking GraphQL for a simple internal service-to-service call where it adds needless complexity over a plain REST or gRPC call (pitfall)
- The 60-second version (concept)
- cross-link: grpc-and-protobuf

### Topic: How would you paginate this endpoint at scale? (iv-pagination-strategy-choice, intermediate)
Tests whether you know offset pagination breaks down at scale (skipped/duplicated rows under concurrent writes, slow OFFSET scans) and can name cursor-based pagination as the fix.
- The question as asked, and the offset-pagination problems it's checking you know (overview)
- Clarifying questions: is the underlying data being written to concurrently while users page through it? How deep do users typically page — a few pages, or thousands? (concept)
- The answer skeleton: cursor/keyset pagination using a stable sort key, not OFFSET, for anything at scale (concept)
- Walking it: a worked example — paginating by a compound cursor of `(created_at, id)`, encoding the last row's values into an opaque cursor token returned to the client (code)
- Walking it: a concrete scenario — a feed with 50 new rows/sec; a user on `OFFSET 10000` gets rows shifted by every insert ahead of their position, silently skipping or duplicating rows between page loads; the same feed with a `(created_at, id)` cursor is immune, because it's anchored to a specific row, not a shifting position (concept)
- Walking it: the query-performance side — `OFFSET 100000 LIMIT 20` still has to scan and discard 100,000 rows on most engines; a keyset `WHERE (created_at, id) > (?, ?) LIMIT 20` uses the index directly regardless of how deep the page is (diagram)
- The trade-off to name out loud: cursor pagination is strictly better for infinite-scroll/feed use cases but gives up direct jump-to-page-N navigation, which some UIs genuinely need (compare)
- Follow-up: "a user jumps to page 50 directly — does cursor pagination support that?" — not natively; that needs either a hybrid (offset for shallow, cursor for deep) or accepting an approximate jump, which is a real product trade-off to surface (concept)
- Follow-up: "how do you paginate when the sort is by a field that isn't unique, like `likes_count`?" — append a unique tiebreaker (e.g., `id`) to the cursor so ties don't produce ambiguous or repeated pages (concept)
- Pitfall: using OFFSET/LIMIT on a large, actively-written table and returning skipped or duplicate rows to the user without realizing why (pitfall)
- The 60-second version (concept)
- cross-link: pagination-strategies

### Topic: How would you version this API without breaking existing clients? (iv-api-versioning-strategy, intermediate)
Tests whether you can name a concrete versioning mechanism (URI, header) and, more importantly, a deprecation process — not just "we'd version it."
- The question as asked, and why "we'd add v2" alone doesn't answer it (overview)
- Clarifying questions: how many external clients exist, and can you force them to upgrade, or must old versions run indefinitely? Is the change additive or genuinely breaking? (concept)
- The answer skeleton: pick a versioning mechanism, then describe the deprecation timeline and how you detect who's still on the old version (concept)
- Walking it: a worked example — URI versioning (`/v1`, `/v2`) plus a `Sunset` HTTP header on v1 responses once v2 ships, and per-API-key usage telemetry to see who's still calling v1 (concept)
- Walking it: a concrete scenario — v2 changes a field from a string to a structured object; v1 stays fully functional and unchanged, v2 is a genuinely new contract, and clients migrate on their own schedule rather than being broken mid-flight (concept)
- Walking it: the additive case that doesn't need a new version at all — adding an optional new field to a response is backward-compatible by construction if clients are written to ignore unknown fields, so it ships on the existing version (compare)
- The trade-off to name out loud: running multiple API versions indefinitely is a real ongoing cost (double the code paths to maintain and test) — the versioning mechanism is the easy part; the expensive part is the organizational discipline to actually sunset old versions (compare)
- Follow-up: "one big customer refuses to migrate off v1 — what do you do?" — negotiate a concrete sunset date backed by usage data and business leverage, or in the worst case maintain a bespoke compatibility shim for just that customer rather than block the whole platform's evolution (concept)
- Follow-up: "how do you catch a breaking change before it ships, not after a client complains?" — contract tests against a stored schema/OpenAPI spec in CI that fail the build on an incompatible change (concept)
- Pitfall: adding a breaking change to an existing endpoint without bumping the version at all, silently breaking every client on the next deploy (pitfall)
- The 60-second version (concept)
- cross-link: api-versioning-and-evolution

### Topic: Design a rate limiter for this API (iv-design-a-rate-limiter, advanced)
A deep-dive probe on the algorithm and distributed-counting mechanics behind rate limiting — distinct from the standalone LLD case study, which asks for the full class design; here the focus is choosing and defending an algorithm for a stated API's traffic pattern.
- The question as asked, and how this differs from the LLD version of the same prompt (overview)
- Clarifying questions: per-user, per-IP, or per-API-key; and does the limit need to allow bursts, or be perfectly smooth? (concept)
- The answer skeleton: pick an algorithm (token bucket for bursts, sliding window for smoothness), then say where the counter lives (concept)
- Walking it: token bucket vs fixed window vs sliding window log — the burst-handling difference, with a concrete example at 100 req/min per key (compare)
- Walking it: a concrete scenario — a mobile client that batches and sends 40 requests in one burst then goes quiet for a minute; a fixed-window limiter of 100/min can wrongly reject that burst near a window boundary, while a token bucket sized to allow a 50-request burst handles it correctly (concept)
- Walking it: where the counter lives at scale — a shared Redis instance with an atomic `INCR`+`EXPIRE` (or a Lua script for token bucket math) so 50 app servers all see the same count instead of each maintaining its own local, inconsistent one (code)
- Follow-up: "the limiter itself needs to be distributed across 50 app servers — where does the counter state live?" — centralized (Redis) for correctness at some added latency/dependency risk, or approximate/local-with-sync for lower latency at the cost of temporarily over-admitting requests (concept)
- Follow-up: "Redis is now a single point of failure for every API call — how do you protect against that?" — fail open (allow requests through) rather than fail closed (reject everything) if the rate-limiter's own dependency is down, since an outage in your safety net shouldn't become an outage in the product (concept)
- Follow-up: "how do you rate-limit fairly when one tenant sends 1000x the traffic of everyone else?" — per-key limits scoped to the tenant/API-key, not a single global counter, so one noisy tenant can't exhaust the whole limiter's headroom for everyone (concept)
- Pitfall: implementing a fixed window and missing the edge-boundary burst problem (up to 2x the limit at the window seam) (pitfall)
- The 60-second version (concept)
- cross-link: rate-limiting-algorithms
- cross-link: distributed-rate-limiting

### Topic: How do you handle a request that takes way longer than a normal API call? (iv-handling-long-running-requests, intermediate)
Tests whether you know a synchronous HTTP call is the wrong shape for genuinely long work, and can name the async pattern (202 + status endpoint, or webhook) that replaces it.
- The question as asked, and why "just raise the timeout" is a losing answer (overview)
- Clarifying questions: how long does the work actually take, and does the caller need the result immediately or can they be notified later? Is the caller a browser, a mobile client, or a server that can receive a callback? (concept)
- The answer skeleton: don't hold the HTTP connection open — accept the request, return immediately with a reference, and let the caller check back or be notified (concept)
- Walking it: a worked example — a video-transcoding endpoint returns `202 Accepted` with a `job_id` immediately, and the client polls `GET /jobs/{job_id}` for status, or a webhook fires when it's done if the caller registered a callback URL (code)
- Walking it: a concrete scenario — a report-generation endpoint that used to take 2 seconds now takes 90 seconds for a large customer's data; keeping it synchronous means the client's HTTP client library times out at 30s and retries, generating the same expensive report twice for a request that was actually still running (concept)
- Walking it: why raising the client and server timeouts to "just wait longer" doesn't scale — it ties up a request-handling thread/connection for the full duration, and every layer in between (load balancer, gateway, proxy) needs its timeout raised to match, propagating one slow endpoint's needs onto the whole stack (diagram)
- The trade-off to name out loud: async job patterns add real complexity — a job store, a status API, retry/idempotency for job creation — that a simple synchronous call didn't need; only worth it once "just wait" genuinely stops working (compare)
- Follow-up: "the client polls every second for 90 seconds — is that OK?" — usually not at scale; recommend polling backoff, or a webhook/websocket push instead of naive tight polling (concept)
- Follow-up: "the job fails halfway through — what does the status endpoint return, and can the client retry just the failed part?" — a status enum that distinguishes retryable failure from terminal failure, and, if the work is resumable, enough job state to restart from a checkpoint rather than from scratch (concept)
- Pitfall: raising every timeout up the stack to accommodate one slow operation instead of moving that operation off the synchronous request path entirely (pitfall)
- The 60-second version (concept)

### Topic: How do you protect a downstream service you don't own from being overwhelmed by your own calls? (iv-protecting-a-downstream-dependency, advanced)
Tests whether you can name outbound-side protections (client-side rate limiting, bulkheads, backoff) that protect a dependency from you, distinct from protecting yourself from a dependency's failure.
- The question as asked, and how this is the mirror image of the more commonly asked "protect yourself from a failing dependency" question (overview)
- Clarifying questions: is this dependency a partner API with a contractual rate limit, or an internal service you could in principle ask to scale? What happens to *them* if you send more than they can handle? (concept)
- The answer skeleton: rate-limit your own outbound calls to a level the dependency has told you it can sustain, and isolate that traffic so a burst from one internal caller can't consume the whole shared budget (concept)
- Walking it: a worked example — a partner shipping-rate API caps you at 50 req/sec; a client-side token-bucket limiter enforces that ceiling before requests ever leave your service, rather than relying on the partner to reject the excess (code)
- Walking it: a concrete scenario — a batch job inside your own company starts calling a shared internal geocoding service at 10x its normal rate during a one-time data backfill, degrading it for every other team relying on it; a per-caller quota on the geocoding service (or a bulkhead limiting how much of your own outbound budget the batch job can use) prevents one internal user from starving the rest (concept)
- Walking it: what happens without this protection — you get rate-limited or blocked by the partner entirely, which now looks identical to *them* being down, even though you caused it (concept)
- Diagram: your service's outbound calls passing through a client-side limiter before reaching a rate-capped partner API, with a queue absorbing the excess instead of firing it all at once (diagram)
- The trade-off to name out loud: self-imposed outbound limits mean you sometimes queue or defer your own work even when you have spare capacity to send more — you're protecting the relationship with the dependency over your own short-term throughput (compare)
- Follow-up: "your queued outbound work is backing up behind the rate cap — is that itself a problem?" — yes, it becomes a backpressure problem on your own side, which is why this pairs directly with a backpressure/shedding strategy for the work waiting to go out (concept)
- Follow-up: "how is this different from a circuit breaker?" — a circuit breaker reacts to the dependency already failing; a client-side limiter proactively prevents you from ever sending more than agreed, so the dependency doesn't fail in the first place (concept)
- Pitfall: assuming rate limiting is only something you receive from others, not something you also owe a dependency you call (pitfall)
- The 60-second version (concept)
- cross-link: bulkheads-and-isolation

### Topic: Part of this request succeeded and part failed — what do you return, and how does the design handle it? (iv-designing-for-partial-failure, advanced)
Tests whether you can design an API operation's contract for partial success (a batch write, a multi-step action) instead of assuming every request is atomically all-or-nothing.
- The question as asked, and why "just wrap it in a transaction" doesn't work once the operation spans services (overview)
- Clarifying questions: does this operation touch one system, or does it span multiple services/databases that can't share a single transaction? Can any of the sub-steps be safely retried independently? (concept)
- The answer skeleton: for anything spanning multiple systems, design the response to report per-item status rather than a single success/fail, and make each sub-step idempotent so the caller can safely retry just the failed parts (concept)
- Walking it: a worked example — a bulk `POST /orders/batch` creating 100 orders returns a 207-style response with a per-order status array (`created`, `failed: insufficient_stock`, ...) instead of a single 200 or 500 for the whole batch (code)
- Walking it: a concrete scenario — an order triggers inventory decrement (succeeds), then payment charge (succeeds), then a loyalty-points award (fails because that service is down); the design needs to decide and clearly document: does the order still count as placed, and does loyalty get retried out-of-band, or does the whole thing need to unwind? (concept)
- Walking it: the saga-style answer for the multi-service case — each step either succeeds or triggers a compensating action for the steps already done (e.g., refund the charge if points can't be awarded and the business rule requires all-or-nothing) (diagram)
- The trade-off to name out loud: reporting partial success is more honest and often more useful to the caller, but it pushes real complexity onto every caller, who now has to handle a mixed-result response instead of a simple success/fail — that's only worth it when partial success is actually a valid outcome for the business (compare)
- Follow-up: "the caller retries the whole batch after a partial failure — do the already-succeeded items get duplicated?" — only if each item isn't idempotent; this is why partial-failure design and idempotent operations are the same conversation (concept)
- Follow-up: "who decides whether partial success is acceptable here — engineering or the business?" — the business; "is a half-placed order OK to show the user as placed" is a product decision that changes the whole design, not a purely technical one (concept)
- Pitfall: designing a batch endpoint that returns a single success/failure for the whole request when the underlying operations are actually independent and partially succeed in practice (pitfall)
- The 60-second version (concept)

### Topic: How would you configure a circuit breaker for this dependency? (iv-circuit-breaker-tuning, intermediate)
Tests whether you can pick concrete thresholds (failure rate, open duration, half-open probe count) for a stated dependency, not just say "we'd add a circuit breaker."
- The question as asked, and the specific thresholds it expects you to name (overview)
- Clarifying questions: what's this dependency's normal failure rate, and how costly is a false trip vs a missed trip? (concept)
- The answer skeleton: set a failure-rate threshold to open, a cooldown before half-open, and a probe count before fully closing (concept)
- Walking it: a worked example — open at 50% failure over a rolling window of 20 requests, half-open after a 30-second cooldown, letting 5 probe requests through before deciding to fully close or re-open (code)
- Walking it: a concrete scenario — a payment gateway that normally has a 0.5% failure rate starts failing 60% of calls; the breaker trips open within seconds of crossing 50% over the 20-request window, stopping the flood of calls that would otherwise pile up as timeouts on your own service's threads (concept)
- Walking it: why the thresholds have to be dependency-specific — a flaky third-party API with a naturally noisier 5% baseline failure rate needs a higher open-threshold than a normally rock-solid internal service, or it'll trip on ordinary noise (concept)
- The trade-off to name out loud: a sensitive threshold trips fast and protects you sooner but risks false trips on normal variance; a lenient threshold avoids false trips but lets more real failures through before acting — tune from the dependency's actual failure-rate distribution, not a one-size-fits-all number (compare)
- Follow-up: "the breaker is flapping open and closed — what's wrong with the tuning?" — the half-open probe count is likely too small relative to the dependency's variance, so a couple of unlucky probes re-open it repeatedly; widen the probe window or add a minimum stay-closed duration (concept)
- Follow-up: "should every caller of this dependency share one breaker, or does each caller get its own?" — depends on whether the dependency's failure is caller-specific (a bad payload from one caller) or systemic (the dependency itself is down) — a shared breaker protects against the systemic case but can wrongly punish every caller for one caller's bad behavior (concept)
- Pitfall: setting the threshold so sensitive that normal transient blips trip the breaker constantly, causing more availability loss than the failures it was meant to contain (pitfall)
- The 60-second version (concept)
- cross-link: circuit-breakers

### Topic: One slow dependency is eating your whole thread pool — how do you stop it from taking everything else down? (iv-isolating-a-slow-dependency, advanced)
Tests whether you know the bulkhead pattern — isolating resource pools per dependency — as distinct from a circuit breaker, which reacts to failure rather than isolating resource consumption.
- The question as asked, and why a circuit breaker alone doesn't solve this specific failure mode (overview)
- Clarifying questions: are calls to this dependency sharing a thread/connection pool with calls to other, healthy dependencies? How many concurrent calls does the slow dependency typically hold open when it's degraded? (concept)
- The answer skeleton: give each dependency its own bounded resource pool (threads, connections, or a semaphore) so one dependency running slow can only exhaust its own allocation, never the shared one (concept)
- Walking it: a worked example — a service calling both a fast internal cache and a slow third-party enrichment API from the same 100-thread pool; when the enrichment API starts taking 30 seconds per call instead of 200ms, all 100 threads fill up waiting on it and even the cache calls — completely unrelated to the slow dependency — start queuing and timing out (concept)
- Walking it: the fix — a dedicated 15-thread bulkhead for the enrichment API calls; when it degrades, at most 15 threads are stuck, and the other 85 keep serving every other dependency's calls normally (diagram)
- Walking it: bulkheads at the connection-pool level too — a separate DB connection pool per major query pattern/dependency so one runaway query pattern can't starve connections needed by unrelated, healthy queries (concept)
- The trade-off to name out loud: bulkheads waste some capacity by design — the 15 threads reserved for the enrichment API sit idle when it's healthy and traffic is light elsewhere — you're trading maximum resource utilization for a hard ceiling on blast radius (compare)
- Follow-up: "how do you size each bulkhead's pool?" — from the dependency's normal concurrency needs plus enough headroom for expected load, not an even split across all dependencies regardless of how much traffic each one actually gets (concept)
- Follow-up: "does a bulkhead replace the need for a circuit breaker on the same dependency?" — no, they solve different problems together: the bulkhead caps the damage while it's failing, the circuit breaker stops sending it calls once it's clearly failing, so use both (concept)
- Pitfall: relying on a circuit breaker alone and assuming it also protects the shared thread/connection pool — it only stops new calls after the pool may already be exhausted by calls already in flight (pitfall)
- The 60-second version (concept)
- cross-link: bulkheads-and-isolation

### Topic: Everyone's retrying at once and now the downstream service is dead — what happened, and how do you prevent it? (iv-retry-storm, advanced)
Tests whether you know retry storms are self-reinforcing (retries add load to an already-struggling service) and can name jittered backoff plus a circuit breaker as the fix.
- The question as asked, and the feedback loop it's describing (overview)
- Clarifying questions: are clients retrying with no backoff, fixed backoff, or already jittered? Are all clients retrying on the same schedule, e.g., after a synchronized timeout? (concept)
- The answer skeleton: name the feedback loop, then apply exponential backoff with jitter and a circuit breaker to cut retries off (concept)
- Diagram: the retry storm feedback loop — failure causes retries, retries cause more failure, more failure causes more retries (diagram)
- Walking it: a concrete scenario — 10,000 clients all set a fixed 5-second timeout and retry immediately on failure; when the dependency has a 2-second blip, all 10,000 requests fail at once and all 10,000 retry at the same instant, multiplying the load exactly when the dependency is most fragile (concept)
- Walking it: how jitter breaks the synchronization — instead of retrying at exactly `t+5s`, each client retries at a randomized point in a window (e.g., `t + random(3s, 8s)`), spreading the retry load out instead of re-concentrating it (code)
- The trade-off to name out loud: backoff-with-jitter and circuit breakers add latency to the failing request path (you wait longer, and sometimes fail fast instead of eventually succeeding) in exchange for not making a partial outage into a total one (compare)
- Follow-up: "you fix the clients, but they're deployed slowly — what protects you in the meantime?" — server-side load shedding on the dependency itself, rejecting excess requests before they cause more damage, independent of whether clients behave (concept)
- Follow-up: "should every client retry the same number of times?" — no — retries should decrease or stop for lower-priority callers first (load shedding by priority) so critical traffic gets whatever retry budget remains during a partial outage (concept)
- Pitfall: adding retries to a client without backoff or jitter, turning a 2-second blip into a sustained outage (pitfall)
- The 60-second version (concept)
- cross-link: retries-timeouts-and-backoff

### Topic: How do you set timeouts across a call chain so they actually add up? (iv-setting-timeout-budgets, advanced)
Tests whether you understand that timeout budgets must decrease down a call chain (each hop leaves room for the next), not be set identically at every layer.
- The question as asked, and the "just set every timeout to 5 seconds" mistake it's testing (overview)
- Clarifying questions: how many hops deep is this call chain, and what's the end-to-end SLA at the top? (concept)
- The answer skeleton: allocate a total budget at the entry point, then divide it down the chain, each hop shorter than its caller (concept)
- Diagram: a 4-hop call chain with a shrinking timeout budget at each layer — 5000ms at the gateway, 4000ms at the API, 2500ms at the service, 1000ms at the DB call (diagram)
- Walking it: a concrete scenario — every layer set independently to "5 seconds, seems safe": the gateway waits 5s, the service it calls also waits 5s, and the DB call inside that also waits 5s; a slow DB call can now make the gateway wait up to 15 seconds total, blowing past whatever SLA the gateway promised its own caller (concept)
- Walking it: the fix applied — the gateway's 5s budget leaves 4s for the downstream API after its own overhead, which leaves 2.5s for the service after network/serialization, which leaves 1s for the DB call — each hop explicitly aware it's spending from a shared, shrinking budget (concept)
- The trade-off to name out loud: propagating a shrinking deadline (e.g., via a `deadline` field in the request context) is more correct but requires every service in the chain to cooperate and respect it — one uncooperative hop that ignores the incoming deadline breaks the whole scheme (compare)
- Follow-up: "hop 3 times out but hop 1's timeout hasn't expired yet — what does the caller see?" — hop 1 should propagate the failure immediately rather than waiting out its own full timeout once it knows a required downstream call has already failed (concept)
- Follow-up: "how do you enforce that every service actually respects its allotted slice instead of just hoping they do?" — pass the remaining deadline explicitly in the request (a header or context deadline) so each hop can check "do I even have time left to attempt this" before starting work, not just trust local config (concept)
- Pitfall: setting the same timeout at every layer, so a deep hop can hang long after the caller at the top has already given up and moved on (pitfall)
- The 60-second version (concept)

### Topic: How would you design reliable webhook delivery to a client's endpoint? (iv-webhook-delivery-design, advanced)
Tests whether you can name the concrete mechanics of webhook delivery — retries with backoff, signing for authenticity, idempotency keys, and ordering — that make an outbound callback as reliable as an inbound API.
- The question as asked, and why webhooks are actually harder to get right than the inbound API they complement (overview)
- Clarifying questions: can the client's endpoint be temporarily down or slow, and for how long should you keep retrying before giving up? Does delivery order across events matter to the client? (concept)
- The answer skeleton: retry failed deliveries with backoff up to a bounded window, sign every payload so the client can verify it's really from you, and give every event an idempotency key so a retried delivery is safe to process twice (concept)
- Walking it: a worked example — a `payment.succeeded` webhook signed with an HMAC over the payload and a timestamp in a `Webhook-Signature` header, so the client rejects forged or replayed requests (code)
- Walking it: a concrete scenario — a client's endpoint returns 500s for 20 minutes during their own deploy; your delivery system retries with exponential backoff (1m, 5m, 15m, 1h...) up to a 24-hour window instead of giving up after the first failure or hammering them every second (concept)
- Walking it: the ordering problem — two events for the same object fire close together and the second delivery attempt for event 1 lands after event 2 already arrived (because event 1 needed a retry); the client needs each event's own sequence number or timestamp to detect and handle out-of-order arrival, since HTTP delivery order isn't guaranteed (diagram)
- The trade-off to name out loud: retrying aggressively maximizes delivery but risks delivering the same event multiple times to a client that isn't idempotent on their end — that's why the idempotency key is not optional, it's what makes "retry until it lands" safe to do at all (compare)
- Follow-up: "the client's endpoint has been down for the entire 24-hour retry window — what happens to that event?" — it lands in a dead-letter state visible to the client (e.g., in a dashboard) so they can manually replay it once their endpoint is back, rather than being silently lost (concept)
- Follow-up: "how does the client know a webhook update didn't just fail silently on their end?" — they don't, unless you also expose a polling/list API as a fallback source of truth — webhooks should be a convenience layer over data the client can still pull directly (concept)
- Pitfall: firing a webhook once, treating a non-2xx response as "delivered," and giving the client no way to recover a missed event (pitfall)
- The 60-second version (concept)

### Topic: This dependency is down — what does the system do instead of failing outright? (iv-graceful-degradation-choice, advanced)
Tests whether you can name a specific fallback for the specific dependency (cached/stale data, a default value, a reduced feature set) rather than a generic "we'd degrade gracefully."
- The question as asked, and the vague non-answer it's testing against (overview)
- Clarifying questions: which dependency, and is its output on the critical path or an enhancement? What's the actual cost to the business of showing something wrong vs showing nothing? (concept)
- The answer skeleton: name the concrete fallback for this specific dependency — stale cache, sensible default, or hide the feature (concept)
- Walking it: a recommendations service failing — fall back to a generic "trending" list served from cache instead of an empty page or a 500 (compare)
- Walking it: a concrete scenario — a personalization service that ranks search results goes down; the fallback isn't "show an error," it's "show unranked/default-ranked results" — a strictly worse but still fully functional experience, versus a broken page (concept)
- Walking it: the critical-path case where there really is no safe fallback — a payment-authorization dependency failing can't be "degraded" to a fake success; here the right answer is fail the specific request clearly and fast, not silently proceed (concept)
- The trade-off to name out loud: degrading gracefully means shipping and maintaining a second, simpler code path that's rarely exercised — it's easy for that fallback path to silently rot and fail exactly when you need it, unless it's tested regularly (compare)
- Follow-up: "how does the system know to switch back once the dependency recovers?" — a health check or the circuit breaker's own half-open state driving the switch back, not a manual flag someone has to remember to flip (concept)
- Follow-up: "how do you test that the fallback path actually works, given it almost never runs?" — exercise it deliberately and regularly (a feature flag that forces the fallback in staging, or periodic chaos-style drills in production) rather than discovering it's broken during a real outage (concept)
- Pitfall: saying "we'd degrade gracefully" without naming what the fallback actually shows the user, or shipping a fallback path that's never been tested since it was written (pitfall)
- The 60-second version (concept)
- cross-link: graceful-degradation-and-load-shedding

---

## Group: Operations — Interview Questions (interview-hld-operations)
*detecting failure, SLO negotiation, runbooks, safe deploys, finding a latency regression, debugging a live p99 spike, incident response, failure-injection testing, capacity planning for growth and for a known launch, on-call design, alert fatigue, multi-region failover*

### Topic: How do you know this system is broken before your users tell you? (iv-detecting-its-broken, intermediate)
Tests whether you can name the specific signals (error rate, latency percentiles, saturation) and alert thresholds that catch a problem early, not just "we'd have monitoring."
- The question as asked, and why "we'd have monitoring" alone doesn't satisfy it (overview)
- Clarifying questions: is this about full outages, or gradual degradation too? What's the cost of a 5-minute-late detection versus a 5-second-late one for this system? (concept)
- The answer skeleton: name the golden signals — latency, traffic, errors, saturation — and alert on the ones that predict user pain, not just server health (concept)
- Walking it: a worked example — alerting on p99 latency crossing 500ms and on a 5xx error-rate burn rate, not just "is the server up" (concept)
- Walking it: a concrete scenario — a checkout service where CPU and memory look completely normal but p99 latency has crept from 200ms to 3 seconds because of DB connection pool exhaustion; a health-check-only setup shows all-green while every real user is stuck (concept)
- Walking it: saturation as the leading indicator — connection pool usage at 95%, queue depth climbing, disk approaching full — these predict a future outage before latency or errors even move, giving you lead time to act (diagram)
- The trade-off to name out loud: more signals catch more failure modes but raise the ceiling on what a human has to triage during an incident — start from the signals that map directly to user pain (the four golden signals) before adding infrastructure-internal ones (compare)
- Follow-up: "your error rate is normal but users are still complaining — what did you miss?" — a client-side signal (real user monitoring, JS error rates, mobile crash rates) or a partial-degradation signal your server-side metrics average away (concept)
- Follow-up: "how do you catch a slow, gradual degradation instead of only sudden spikes?" — trend-based alerting (week-over-week comparison, anomaly detection) rather than a single static threshold that a slow creep never crosses in one alarm-worthy jump (concept)
- Pitfall: alerting only on uptime/health-check pings and missing slow-but-technically-up failures that hurt users just as much as an outage (pitfall)
- The 60-second version (concept)
- cross-link: metrics-and-slis-slos

### Topic: How would you set the SLO for this service? (iv-negotiating-an-slo, advanced)
Tests whether you can negotiate an SLO from actual user impact and error budget math, not pick an arbitrary "five nines" number to sound rigorous.
- The question as asked, and the "just promise 99.99%" trap it's testing against (overview)
- Clarifying questions: what does the business actually lose when this service is degraded for a minute, an hour? Is this service on the critical path for revenue, or an internal tool? (concept)
- The answer skeleton: derive the SLO from user impact and the cost of achieving it, then define the error budget that SLO implies (concept)
- Walking it: a worked example — a 99.9% SLO implying roughly 43 minutes/month of allowed downtime, and what that error budget actually buys engineering-wise (permission to ship riskier changes as long as the budget isn't spent) (code)
- Walking it: a concrete scenario — a checkout service currently running at 99.5% (about 3.6 hours/month down) proposes jumping straight to 99.99% (about 4 minutes/month); getting there requires multi-region active-active and synchronous cross-region replication, a multi-million-dollar infra and engineering investment the traffic and revenue at stake doesn't justify (concept)
- Walking it: what the error budget changes day-to-day — once you're within budget, teams can deploy more freely; once the budget's nearly spent, deploys freeze and reliability work takes priority, giving the SLO real operational teeth instead of being a number on a slide (diagram)
- The trade-off to name out loud: every additional nine of reliability costs disproportionately more than the last one — going from 99% to 99.9% might double infra cost, while 99.9% to 99.99% might 5-10x it — the SLO conversation is really a cost conversation wearing a reliability hat (compare)
- Follow-up: "the business wants 99.99% but that's 10x your current infra cost — what do you say?" — quantify the cost, tie it to the actual revenue/user impact of the gap, and let the business make an informed trade-off rather than silently overcommitting (concept)
- Follow-up: "you've hit your error budget for the month — what actually happens next?" — a change freeze on risky deploys, reprioritizing the team's roadmap toward reliability work until the budget resets, not just an ignored dashboard number (concept)
- Pitfall: promising a stricter SLO than the current architecture can actually support, setting up a guaranteed future breach (pitfall)
- The 60-second version (concept)
- cross-link: metrics-and-slis-slos

### Topic: What would go in the runbook for this service? (iv-writing-a-runbook, intermediate)
Tests whether you can name concrete, actionable runbook content (symptom → diagnosis steps → mitigation) tied to this system's actual failure modes, not a generic "we'd document things" answer.
- The question as asked, and why a runbook is judged on whether a 2am on-call engineer who's never touched this service could follow it (overview)
- Clarifying questions: who's the audience — the team that owns this service, or a generalist on-call rotation covering many services? What are this service's most common historical failure modes? (concept)
- The answer skeleton: structure each entry as symptom → how to confirm it → the specific mitigation steps → who/what to escalate to if the mitigation doesn't work (concept)
- Walking it: a worked example — a runbook entry for "checkout p99 latency alert fires": check the DB connection pool dashboard first (most common cause), if saturated restart the leaked-connection pods, if that doesn't resolve it within 10 minutes escalate to the database on-call (concept)
- Walking it: a concrete scenario — without a runbook, a new on-call engineer facing a payment-gateway timeout alert spends 25 minutes rediscovering that this specific alert almost always means the gateway's sandbox environment leaked into prod config — a runbook entry turns that into a 2-minute fix (concept)
- Walking it: what belongs in a runbook versus what doesn't — concrete, repeatable diagnostic steps and mitigations belong; open-ended "investigate the root cause" tasks don't, because a runbook is for restoring service fast, not for the follow-up postmortem work (compare)
- The trade-off to name out loud: a runbook that's too detailed goes stale the moment the architecture changes and nobody trusts it anymore; too sparse and it doesn't actually help at 2am — keep it to the handful of failure modes that actually recur, and review it after every incident that wasn't already in it (compare)
- Follow-up: "how do you keep a runbook from going stale as the system evolves?" — tie runbook updates to the incident postmortem process itself, so every new failure mode discovered gets added as part of closing out the incident, not as a separate forgotten chore (concept)
- Follow-up: "the on-call engineer followed every step and it still didn't fix it — what then?" — a clear escalation path and a 'stop and page someone with more context' threshold baked into the runbook itself, rather than letting them thrash indefinitely (concept)
- Pitfall: writing a runbook once at launch and never updating it, so it actively misleads on-call engineers once the architecture has moved on (pitfall)
- The 60-second version (concept)

### Topic: How do you deploy a change to this system without risking an outage? (iv-safe-deploys, intermediate)
Tests whether you can name a concrete rollout mechanism (canary, gradual ramp) plus the metric that gates each step, not just "we'd test it first."
- The question as asked, and why "we test before deploying" doesn't cover production-only failure modes (overview)
- Clarifying questions: is this a stateless service, a stateful one, or a schema change — each needs a different approach? Can this deploy be rolled back cleanly, or does it involve an irreversible step (like a migration)? (concept)
- The answer skeleton: canary a small percentage, watch the gating metric, ramp up, with a fast rollback path at every step (concept)
- Diagram: a canary rollout with a gate metric and an automatic rollback trigger — 1% → 10% → 50% → 100%, each step held until the gate metric holds steady (diagram)
- Walking it: a concrete scenario — a new caching layer is deployed to 1% of traffic first; error rate and p99 latency on that 1% are compared against the control group for 15 minutes before promoting to 10%, catching a subtle cache-serialization bug affecting 3% of requests before it ever reaches most users (concept)
- Walking it: the schema-change case, which canarying alone doesn't cover — an additive, backward-compatible migration deployed and verified before the code that depends on it ships, so old and new code can both run safely during the rollout window (concept)
- The trade-off to name out loud: a slow, staged canary catches more problems before they're widespread but delays how fast a fix or feature actually reaches all users — for a critical hotfix, you might accept more risk and move faster; for a routine feature, take the full staged path (compare)
- Follow-up: "the canary looks fine but the full rollout breaks — what did the canary miss?" — a scale-dependent failure mode the 1% traffic slice never triggered (e.g., a resource leak that only matters under full load, or an edge case only present in traffic segments underrepresented in the canary slice) (concept)
- Follow-up: "the gate metric looks fine but a slower-forming problem shows up an hour later — how do you catch that?" — hold each canary stage for longer than the shortest failure mode you care about, and keep watching key metrics for a window even after full rollout, not just during the ramp (concept)
- Pitfall: deploying to 100% at once because "it passed staging," skipping any production-traffic verification step (pitfall)
- The 60-second version (concept)
- cross-link: rolling-out-a-design

### Topic: How do you find the cause of a latency regression after a release? (iv-finding-a-latency-regression, advanced)
Distinct from live p99 triage during an active incident — this is a slower, deploy-correlated investigation: comparing metrics before and after a release and bisecting across recent changes to find which one is responsible.
- The question as asked, and how it differs from debugging a spike you're seeing right now (overview)
- Clarifying questions: how many changes shipped between the last-known-good period and now — one deploy, or a week of them? Is the regression uniform across all traffic, or isolated to one endpoint/segment? (concept)
- The answer skeleton: compare before/after metrics at the deploy boundary first; if multiple changes shipped in the window, bisect by rolling back or feature-flagging changes one at a time against the same metric (concept)
- Walking it: a worked example — dashboards overlaying p50/p95/p99 latency for the 24 hours before and after a deploy, isolating exactly which endpoint's percentile shifted and by how much (diagram)
- Walking it: a concrete scenario — p99 for the search endpoint rose from 180ms to 640ms after a release that bundled three unrelated changes; feature-flagging each one off independently in a canary shows the new relevance-scoring model (not the two other changes shipped alongside it) is responsible, because it added a synchronous call to a scoring service that wasn't there before (concept)
- Walking it: what to do when you can't cleanly bisect because changes were deployed together without flags — a targeted rollback of the whole release to confirm the regression disappears, buying time to bisect properly in a follow-up deploy with each change flagged independently (concept)
- The trade-off to name out loud: bisecting via feature flags is precise but only works if changes were flagged at deploy time — after the fact, your only options are a coarser full rollback or a slower forensic trace-level investigation, which is the argument for flagging risky changes before you need this (compare)
- Follow-up: "the regression started 2 hours after the deploy, not immediately — does that change your suspect?" — yes, look for something that ramps rather than an instant cause: a cache warming up cold, a gradual traffic ramp exposing an N+1 query, or a resource leak that takes time to matter (concept)
- Follow-up: "you found the responsible change — do you roll it back or fix forward?" — roll back first to stop user impact immediately, then fix and re-deploy with the fix verified in canary, rather than trying to patch a live regression under pressure (concept)
- Pitfall: assuming the most recent or most visible change is the cause without actually isolating it, and rolling back the wrong thing while the real cause ships again in the next release (pitfall)
- The 60-second version (concept)
- cross-link: rolling-out-a-design

### Topic: p99 latency just spiked — walk me through how you'd debug it (iv-debug-p99-spike, advanced)
The live-debugging probe: tests whether you have a systematic narrowing process (which endpoint, which dependency, which resource) instead of guessing at causes.
- The question as asked, and the "check the logs" non-answer it's testing against (overview)
- Clarifying questions: is this every endpoint or one; did it start suddenly or drift up gradually? Is traffic volume also elevated, or is this happening at normal load? (concept)
- The answer skeleton: narrow by endpoint, then by dependency call, then by resource (CPU/GC/lock contention), using tracing at each step (concept)
- Walking it: a worked example — a distributed trace showing 2.8 of a 3-second request spent inside a single downstream DB call, and that DB call itself spending most of its time in a lock wait, not query execution (diagram)
- Walking it: a concrete scenario — dashboards show the spike is isolated to the `/checkout` endpoint, not global; tracing that endpoint shows the added time is entirely inside a single Redis call; checking Redis's own metrics shows a sudden spike in slow commands correlating with a teammate running a `KEYS *` scan against production moments earlier (concept)
- Walking it: what to check when tracing shows time spent in your own service rather than a downstream call — CPU throttling, GC pause frequency/duration, or thread/lock contention, in that rough order of likelihood for most latency spikes (concept)
- The trade-off to name out loud: a full distributed trace on every request gives you the fastest path to the answer but costs real overhead and storage at high volume — most teams sample traces and rely on aggregate percentile dashboards to first localize where to look before pulling individual traces (compare)
- Follow-up: "the spike correlates with a deploy 10 minutes earlier — what's your next move?" — treat the deploy as prime suspect, check its canary/rollout metrics if it's mid-rollout, and be ready to roll it back immediately rather than continuing the trace-level investigation under active user impact (concept)
- Follow-up: "there's no recent deploy and no obvious dependency slowdown — what's left?" — check for a traffic pattern change (a new heavy client, a bot, a viral spike) and infrastructure-level events (an autoscaling lag, a noisy neighbor on shared infra, a certificate/DNS issue) (concept)
- Pitfall: jumping straight to "scale up the servers" before identifying where the time is actually going, which fixes nothing if the bottleneck is a lock or a single downstream dependency (pitfall)
- The 60-second version (concept)
- cross-link: distributed-tracing

### Topic: How do you run an incident and the postmortem after it? (iv-incident-response-and-postmortems, advanced)
Tests whether you know the shape of a real incident-response process (severity levels, a single incident commander, blameless postmortems with concrete action items) rather than describing an ad hoc scramble.
- The question as asked, and why "we'd fix it and move on" undersells what's actually expected here (overview)
- Clarifying questions: does this org already have a severity/on-call framework, or are you designing the process itself? Is the postmortem meant to assign fault or to find systemic fixes? (concept)
- The answer skeleton: declare severity, assign a single incident commander to coordinate (not necessarily fix), mitigate first and root-cause later, then run a blameless postmortem with concrete, owned action items (concept)
- Walking it: a worked example — a Sev1 incident channel spun up automatically from the paging alert, with a designated incident commander whose job is coordinating responders and communicating status, explicitly not being the one hands-on-keyboard fixing it (concept)
- Walking it: a concrete scenario — during a payment outage, three engineers independently try different fixes at once with no one coordinating, and one engineer's rollback undoes another's in-progress mitigation, extending the outage by 20 minutes; an incident commander would have sequenced those actions instead of letting them collide (concept)
- Walking it: what "mitigate first, root-cause later" means in practice — restoring service (rollback, failover, scaling) takes priority over understanding exactly why it broke; the full root-cause investigation happens in the postmortem, off the clock of user impact (diagram)
- The trade-off to name out loud: a heavyweight incident process (severity levels, a formal commander role, a structured postmortem template) is overhead you don't want for every minor blip — calibrate the process to severity, not apply the Sev1 machinery to a 30-second error-rate blip that self-resolved (compare)
- Follow-up: "the postmortem's action items never get done because they compete with feature work — how do you fix that?" — track them as a required category of work with its own visibility (e.g., counted against the team's error budget or given explicit roadmap slots), not just a hopeful list at the bottom of a doc (concept)
- Follow-up: "an engineer is afraid to be named in the postmortem as the one who pushed the bad change — how do you handle that?" — blameless by design: the postmortem documents what happened and why the system allowed it, not who to blame — the real fix is almost always a process or safeguard gap, not an individual's mistake (concept)
- Pitfall: running a postmortem that identifies root causes but produces no owned, tracked action items, guaranteeing the same incident recurs (pitfall)
- The 60-second version (concept)

### Topic: How do you test that your system actually survives a dependency outage, without waiting for a real one? (iv-testing-failure-injection, advanced)
Tests whether you know deliberate failure injection (chaos engineering, game days) as a practice distinct from unit/integration testing, and can scope it safely.
- The question as asked, and why "we tested the failure-handling code" in a unit test doesn't answer it (overview)
- Clarifying questions: is this a controlled game-day exercise in a staging-like environment, or genuinely injecting failure into live production traffic? What's the blast-radius limit you're willing to accept if the test goes wrong? (concept)
- The answer skeleton: deliberately inject the specific failure (kill a dependency, add latency, drop network) in a controlled, scoped, and reversible way, and verify the system's actual behavior matches what the design assumed (concept)
- Walking it: a worked example — using a chaos tool (e.g., Chaos Monkey-style, or a service mesh fault-injection rule) to inject a 5-second delay on 5% of calls to the recommendations service, then verifying the graceful-degradation fallback actually engages instead of just timing out the whole page (code)
- Walking it: a concrete scenario — a team assumed their circuit breaker would protect them from a downstream outage, but a game day killing that dependency in staging reveals the breaker's threshold was misconfigured and never actually trips, something no unit test caught because the unit tests mocked the dependency as instantly failing, not realistically slow-then-failing (concept)
- Walking it: scoping a safe test in production — start with a tiny percentage of traffic, a pre-agreed abort condition, and a fast kill-switch to stop the injected failure immediately if real user impact exceeds the plan (diagram)
- The trade-off to name out loud: testing in staging is safer but staging traffic patterns and scale rarely match production closely enough to catch every real failure mode — testing in production against real traffic finds more real problems but requires much more careful blast-radius control and organizational buy-in to attempt (compare)
- Follow-up: "leadership is nervous about deliberately breaking things in production — how do you get buy-in?" — start in staging or with an internal-only game day to build confidence and process, then graduate to small, tightly-scoped production experiments with clear rollback authority (concept)
- Follow-up: "how often should you run these tests?" — regularly enough that "does our failure handling still work" isn't answered for the first time during a real outage — after major architecture changes at minimum, and ideally as a recurring practice (concept)
- Pitfall: writing resilience code (circuit breakers, fallbacks, retries) and trusting it works because it compiled and passed a mocked unit test, never observing it under a real, realistic failure (pitfall)
- The 60-second version (concept)

### Topic: How would you plan capacity for this service over the next year? (iv-capacity-planning-for-growth, advanced)
Distinct from the estimation-bank's spike question — this is steady, forecasted growth: tests whether you can build a growth-rate-driven plan with lead-time awareness for hardware/licensing, not just react when limits hit.
- The question as asked, and how planned growth differs from a sudden spike (overview)
- Clarifying questions: what's the historical growth rate, and what's the lead time to add capacity (hardware, licenses, approvals)? (concept)
- The answer skeleton: project forward from growth rate, add a buffer for lead time, and set a trigger threshold to act early (concept)
- Walking it: a worked example — 15%/quarter growth projected against current headroom to find the "we need to act by" date, working backward from when new capacity would actually be available (code)
- Walking it: a concrete scenario — current infra handles 100K QPS with 40% headroom (140K ceiling); at 15%/quarter growth from a 90K QPS baseline, you cross 140K in roughly 4 quarters — but ordering and provisioning new database read replicas takes 2 quarters of lead time, so the trigger to start that procurement needs to fire 2 quarters before the projected crossing, not at the crossing itself (concept)
- Walking it: what's different about licensed or vendor-managed components in this plan — a managed database's tier upgrade might take a support ticket and a maintenance window, while an on-prem hardware order might take a full procurement cycle; each has a different lead time to bake into the same growth curve (concept)
- The trade-off to name out loud: provisioning ahead of the growth curve costs money sitting mostly idle in the meantime; provisioning right at the curve risks a capacity crunch if growth outpaces the forecast even slightly — the buffer size is a direct trade between idle cost and outage risk (compare)
- Follow-up: "growth is not linear — how do you plan for an uncertain forecast?" — plan against a range (conservative/expected/aggressive growth curves) and set the action trigger off the more conservative one, revisiting the forecast on a regular cadence rather than trusting a single static projection for the full year (concept)
- Follow-up: "your capacity plan says you need budget approval 6 months out, but the business won't commit that far ahead — what do you do?" — build in a more modular scaling path (smaller, more frequent capacity additions) that reduces how far ahead any single commitment has to be made, even if it's less cost-efficient per unit (concept)
- Pitfall: waiting until you're at 90% utilization to start the capacity conversation with a component that has a multi-quarter lead time, guaranteeing you'll hit the ceiling before more capacity arrives (pitfall)
- The 60-second version (concept)

### Topic: How would you plan capacity for a known upcoming launch? (iv-planning-for-a-known-launch, advanced)
Distinct from both steady growth planning and a surprise viral spike — this is a scheduled event with a known date: tests whether you can load-test to a target, pre-provision ahead of it, and design a same-day fallback if the estimate is wrong.
- The question as asked, and how a known launch date changes the planning problem versus organic growth or an unpredictable spike (overview)
- Clarifying questions: is there a firm estimate of expected traffic (from marketing spend, a comparable past launch), and how much of a safety margin is the business willing to pay for? (concept)
- The answer skeleton: load-test to a target well above the estimate, pre-provision that capacity ahead of the date (not auto-scaled reactively, since reactive scaling may be too slow for a step-function traffic jump), and have a pre-agreed same-day fallback if reality exceeds the estimate (concept)
- Walking it: a worked example — a launch expected to drive 5x normal traffic based on a comparable prior campaign; the team load-tests to 8x as a safety margin, pre-provisions database read capacity and app servers to that level starting the day before, and holds the extra capacity through the launch window before scaling back down (concept)
- Walking it: a concrete scenario — the actual launch drives 12x traffic, beyond even the 8x tested ceiling, because the marketing campaign went more viral than expected; the pre-agreed fallback (a waiting-room/queueing page for excess traffic, and a feature-flag to disable non-critical features like recommendations) kicks in automatically once load crosses the tested ceiling, protecting the core purchase flow instead of the whole site falling over (diagram)
- Walking it: why relying purely on auto-scaling isn't enough here — a launch can be a step function (traffic jumps 10x in the first minute the announcement goes live), and auto-scaling reacting to that after the fact can be too slow to prevent an initial overload window (concept)
- The trade-off to name out loud: pre-provisioning for a launch means paying for capacity that sits idle before and after the event — the cost of that idle capacity is the price of confidence for a date you can't afford to fail on (compare)
- Follow-up: "the launch is a huge success and traffic is 3x even your tested ceiling — what happens live?" — the pre-agreed degradation plan (queueing, disabling non-critical features, prioritizing the core transaction) executes automatically rather than being improvised live under pressure (concept)
- Follow-up: "how do you decide the safety margin — why 8x and not 20x?" — balance the realistic uncertainty in the estimate (informed by how comparable the reference launch actually is) against the cost of over-provisioning; an important, unrepeatable launch justifies a bigger margin than a routine one (concept)
- Pitfall: relying solely on auto-scaling for a known step-function traffic event instead of pre-provisioning ahead of the date it's guaranteed to happen (pitfall)
- cross-link: back-of-envelope-fundamentals
- The 60-second version (concept)

### Topic: How would you design the on-call rotation and paging for this system? (iv-designing-oncall, advanced)
Tests whether you think about on-call as a design input (who gets paged for what, how alerts map to ownership) rather than an afterthought bolted on post-launch.
- The question as asked, and why on-call design is asked as a system design question at all (overview)
- Clarifying questions: how many teams/services are involved, and does ownership map cleanly to alerting? (concept)
- The answer skeleton: alerts route to the team that owns the failing component, with clear escalation if unacknowledged (concept)
- Walking it: a worked example — a paging policy with primary/secondary rotation and a 15-minute escalation timer before it pages the secondary, then the team lead if still unacknowledged (concept)
- Walking it: a concrete scenario — a checkout-service alert firing pages the checkout team directly rather than a generic "backend on-call," because the alert was defined with clear component ownership, cutting the time-to-first-response from an average of 12 minutes (waiting for the generic on-call to route it correctly) to under 2 (concept)
- Walking it: sizing the rotation itself — a single-person rotation burns out fast and has no coverage for illness/vacation; most teams run a rotation of at least 4-6 engineers to keep any one person's on-call burden to roughly one week a month or less (concept)
- The trade-off to name out loud: narrower, per-team ownership of alerts gets the right person paged faster but requires more alert-routing setup and can create gaps at team boundaries; a single catch-all on-call is simpler to set up but routes almost every page to someone who then has to figure out who actually owns the problem (compare)
- Follow-up: "an alert fires for a shared dependency three teams depend on — who gets paged?" — the team that owns the shared dependency itself, with the affected teams notified (not paged) so they have visibility without diluting responsibility for the actual fix (concept)
- Follow-up: "how do you know if your on-call load is sustainable versus burning people out?" — track pages-per-shift and off-hours pages per person over time; a sustained rise, especially in low-value pages, is the leading indicator to fix before you lose the engineer, not after (concept)
- Pitfall: routing every alert to one catch-all on-call person regardless of which component actually failed, guaranteeing slow response and eventual burnout (pitfall)
- The 60-second version (concept)
- cross-link: alerting-and-on-call-design

### Topic: The on-call engineer is getting paged constantly for non-issues — what do you do? (iv-alert-fatigue-fix, intermediate)
Tests whether you can diagnose alert-fatigue causes (wrong thresholds, alerting on causes instead of symptoms) and fix the alerting design, not just tell the engineer to "ignore the noise."
- The question as asked, and why "just tune it out" is the wrong answer (overview)
- Clarifying questions: are the alerts false positives, or true but non-actionable? How many pages per shift is this engineer currently getting, and how many led to an actual action? (concept)
- The answer skeleton: alert on user-facing symptoms, not internal causes; raise thresholds where noise correlates with no real impact (concept)
- Walking it: replacing a per-server CPU alert (noisy, fires on every routine batch job, not actionable on its own) with an SLO burn-rate alert (fires only when it's actually consuming user-facing error budget, and is directly actionable) (compare)
- Walking it: a concrete scenario — an on-call engineer is paged 8 times overnight for "disk usage above 80%" on a service where that's completely normal steady-state behavior thanks to log rotation timing, none of which required any action; removing that alert entirely (or moving it to a non-paging dashboard) is the correct fix, not tuning the threshold up by 5% (concept)
- Walking it: distinguishing symptom-based from cause-based alerts — "checkout error rate above 1%" (symptom, page immediately) versus "one of 50 pods restarted" (cause, usually self-heals, shouldn't page on its own unless it recurs or correlates with a symptom) (diagram)
- The trade-off to name out loud: cutting noisy alerts risks cutting a rare-but-real signal along with the noise — the fix isn't "alert on less," it's "alert on what's actually actionable and tied to user impact," which sometimes means adding a better alert, not just removing a bad one (compare)
- Follow-up: "you've cut the alert volume in half — how do you know you didn't also cut real signal?" — review incidents retroactively for the next month and check whether any of them would have been caught earlier by an alert you removed; that's the actual measure of whether the cut was safe (concept)
- Follow-up: "some of the paged alerts really were 'true' — they indicated a real, if minor, problem — how do you handle those?" — route true-but-non-actionable alerts to a non-paging channel (a dashboard, a daily digest) rather than a 2am page, reserving paging for what genuinely needs immediate human action (concept)
- Pitfall: silencing or deprioritizing alerts wholesale instead of fixing what they alert on and why (pitfall)
- The 60-second version (concept)
- cross-link: alerting-and-on-call-design

### Topic: How would you fail this system over to another region? (iv-multi-region-failover-design, expert)
Tests whether you can name the concrete failover mechanics — data replication lag tolerance, DNS/traffic cutover, and the decision of active-active vs active-passive — for a stated RTO/RPO.
- The question as asked, and the RTO/RPO numbers it expects you to anchor the design to (overview)
- Clarifying questions: what data-loss window (RPO) and downtime window (RTO) is acceptable? Is the workload read-heavy (easier to serve multi-region) or write-heavy (harder to keep consistent across regions)? (concept)
- The answer skeleton: choose active-active or active-passive based on RTO/RPO, then describe the traffic cutover mechanism (concept)
- Diagram: active-passive failover — replication, health check, DNS/traffic shift, promote (diagram)
- Walking it: a concrete scenario — an RPO of 5 minutes and RTO of 15 minutes is achievable with asynchronous cross-region replication (accepting up to ~5 minutes of potential data loss) and automated health-check-triggered DNS failover (Route 53 health checks flipping traffic within a couple minutes of detecting the primary region down); a demand for zero RPO would instead require synchronous cross-region replication, adding meaningful write latency to every request, all the time, to protect against an event that (hopefully) never happens (concept)
- Walking it: active-active's added complexity once you commit to it — writes can now land in either region, so you need a conflict-resolution strategy (or partition writes by user/region) in addition to the failover mechanics themselves, which active-passive never has to solve (concept)
- The trade-off to name out loud: active-active gives you both regions serving live traffic (no failover event needed, better latency for geographically distant users) at the cost of solving multi-region write consistency; active-passive is operationally simpler but wastes the standby region's capacity and has an actual failover event with its own risk (compare)
- Follow-up: "how do you test this failover works, without waiting for a real outage?" — scheduled failover drills, actually cutting traffic to the standby region on a regular cadence, since an untested failover path is often the least reliable part of the whole design (concept)
- Follow-up: "the failover just happened — how do you fail back to the primary region without losing data written during the failover window?" — replicate the standby's writes-during-failover back to the primary before flipping traffic back, verified before the cutback, not a same-day snap-back the moment the primary looks healthy again (concept)
- Pitfall: claiming "zero RPO, zero RTO" without naming the synchronous-replication cost (and the latency tax on every write, everywhere, all the time) that requires (pitfall)
- The 60-second version (concept)
- cross-link: geo-routing-and-failover
- cross-link: rpo-rto-and-failover-drills

---

## Group: Senior/Staff Trade-off Signal — Interview Questions (interview-hld-tradeoffs)
*"what would you do differently," build vs buy, why not one big database, when NOT to use microservices, over-engineering, starting simple, scoping under a deadline, knowingly taking on debt, defending under pushback, disagreeing with a senior engineer, migration under load, selling a re-architecture, staff-level meta-questions, conflicting constraints*

### Topic: What would you do differently if you designed this again? (iv-what-would-you-do-differently, expert)
The self-critique question — tests whether you can name a real weakness in your own design unprompted, showing judgment under no pressure, before the interviewer has to find it for you.
- The question as asked, and why volunteering a real weakness scores higher than claiming the design is perfect (overview)
- Clarifying questions: is the interviewer asking about a decision you made under genuine uncertainty, or fishing for whether you noticed a specific flaw already visible in the design? (concept)
- The answer skeleton: pick a decision you made under uncertainty, name what you'd revisit with more information or time, and say specifically what evidence would have changed your original call (concept)
- Walking it: a worked example — "I chose eventual consistency for the leaderboard because I assumed users wouldn't notice a few seconds of lag; with real traffic data I'd want to check whether competitive players actually do notice and complain, and revisit toward stronger consistency for just that feature if so" (concept)
- Walking it: a concrete scenario — naming a capacity assumption instead of an architecture choice: "I sized the cache for 10x read traffic based on a rough estimate; I'd want real production numbers before committing that much memory, since I might be over- or under-provisioning by a lot" (concept)
- Walking it: why a *specific, falsifiable* weakness lands better than a vague one — "I'd add more monitoring" is vague and safe; "I'd specifically watch replication lag on the leaderboard writes, because that's the one number that would tell me if eventual consistency was the wrong call" shows you know exactly what you don't know yet (compare)
- The trade-off to name out loud: naming a real weakness costs you a moment of looking less than perfect, in exchange for showing the interviewer you can evaluate your own work — the alternative (claiming no regrets) reads as either dishonest or lacking judgment, both worse outcomes (compare)
- Follow-up: "why didn't you just design it that way from the start?" — defend the original trade-off honestly: it was the right call given the information and constraints you had at the time, and say what specifically would have needed to be true for you to choose differently upfront (concept)
- Follow-up: "if you had unlimited time before this interview, what's the one thing you'd have researched more?" — name a genuine unknown (a specific access pattern, a real traffic distribution) rather than a generic "I'd study more system design," showing the self-critique is really about the problem, not a rehearsed line (concept)
- Pitfall: saying "I wouldn't change anything," or picking a trivial, low-stakes nitpick (a variable name, a minor endpoint shape) to perform humility without any real self-critique (pitfall)
- The 60-second version (concept)
- cross-link: staff-level-system-design-signal

### Topic: Would you build this yourself or buy/use a managed service? (iv-build-vs-buy-call, advanced)
Tests whether you weigh differentiation, operational burden, and total cost concretely for the component in question, rather than defaulting to "build" (control) or "buy" (speed) reflexively.
- The question as asked, and the reflexive answer (always build, or always buy) it's testing against (overview)
- Clarifying questions: is this component core to the product's differentiation, or commodity infrastructure? What's the team's actual capacity to operate something it builds, long-term, not just to ship it once? (concept)
- The answer skeleton: buy commodity/undifferentiated pieces; build only where it's core to what makes this product distinct (concept)
- Walking it: buying a managed queue (SQS) or managed search (Elasticsearch Service) versus building a proprietary recommendation engine that's the actual product differentiator (compare)
- Walking it: a concrete scenario — a 15-person startup considers building its own message queue for "full control"; the honest total cost includes the ongoing operational burden (patching, scaling, on-call for the queue itself) on top of the build cost, which a team that size can't absorb without taking time away from the actual product — buying is the right call not because building is impossible, but because of what it would cost elsewhere (concept)
- Walking it: the counter-case — a company whose entire value proposition is search relevance building its own ranking system rather than using an off-the-shelf managed search product, because the ranking logic *is* the differentiation, not commodity infrastructure around it (concept)
- The trade-off to name out loud: buying trades long-term flexibility and unit economics at scale for speed and reduced operational burden now — at high enough volume, a managed service's per-unit cost can exceed what an in-house equivalent would cost to run, which is exactly why some companies migrate from bought to built later, not because buying was wrong initially (compare)
- Follow-up: "the managed service doesn't support a feature you need — do you still buy it?" — check whether the missing feature is genuinely a hard blocker or a workaround-able gap; a hard blocker on a differentiating capability tips toward build, a minor gap on commodity infra usually doesn't (concept)
- Follow-up: "you bought a managed service two years ago and now it's your biggest infra cost line — was that the wrong call?" — not necessarily; it may have been the correct call for that stage (speed mattered more than unit cost) and the correct call now is a deliberate migration, evaluated with today's constraints, not evidence the original decision was a mistake (concept)
- Pitfall: defaulting to "build" for everything because "we might need custom behavior someday," paying an ongoing operational tax for flexibility that's never used (pitfall)
- The 60-second version (concept)
- cross-link: cost-and-org-aware-design

### Topic: Why not just use one big database for everything? (iv-why-not-one-big-database, advanced)
Tests whether you can justify the complexity of decomposing storage (sharding, polyglot persistence, service boundaries) against the honest simplicity of a single database, instead of assuming decomposition is always correct.
- The question as asked, and why this is a legitimate challenge, not just a naive question to brush aside (overview)
- Clarifying questions: what's actually driving you away from one database — write throughput a single instance can't sustain, a data shape (graph, full-text, time-series) the relational model handles poorly, or organizational boundaries between teams? (concept)
- The answer skeleton: start from one database as the default; only decompose when a specific, named limit of a single instance is actually being hit — not preemptively (concept)
- Walking it: a worked example — a single well-tuned Postgres instance can comfortably handle tens of thousands of QPS and terabytes of data for most applications; the decision to shard or split databases should point at the specific number this system will exceed, not a generic belief that "one database doesn't scale" (concept)
- Walking it: a concrete scenario — a social app's single Postgres instance is fine for the relational core (users, posts, follows) but full-text search across posts is slow and awkward in SQL at scale; adding Elasticsearch *just* for search (polyglot persistence) is justified by a specific, named gap, not a wholesale abandonment of the single database (concept)
- Walking it: the organizational case for decomposition, distinct from the technical one — two teams that both need to evolve their own schema independently and deploy on their own schedule may justify separate databases even before either team's technical load requires it, because shared-database coupling is itself the bottleneck (diagram)
- The trade-off to name out loud: one database gives you transactions, joins, and a single mental model for free; splitting trades all of that away for independent scaling and independent team ownership — you're not avoiding complexity by splitting, you're relocating it from the database into your application and operational layers (compare)
- Follow-up: "you've split into three databases — how do you now do a query that used to be a simple join across them?" — either denormalize/duplicate the needed data into each service, or accept a slower, application-level join (fetch from each and merge in code), both real costs the single database didn't have (concept)
- Follow-up: "at what point does 'one big database' actually become the wrong call?" — when you can point to a specific, measured limit (write throughput ceiling, a data-shape mismatch, or a genuine team-autonomy bottleneck) rather than a general anxiety about scale (concept)
- Pitfall: decomposing into multiple databases preemptively "for scale" before any specific limit of a single database has actually been identified, paying the complexity cost with none of the benefit yet earned (pitfall)
- The 60-second version (concept)
- cross-link: sql-vs-nosql-at-scale
- cross-link: polyglot-persistence

### Topic: When would you NOT use microservices for this? (iv-when-not-microservices, advanced)
Tests whether you can argue against the trendy default and name concrete costs (operational overhead, network hops, distributed debugging) microservices impose on a small team or simple domain.
- The question as asked, and the "microservices are just best practice" assumption it's testing (overview)
- Clarifying questions: what's the team size, and how tightly coupled are the actual business capabilities? Does the domain actually have clean, stable seams, or would a service split cut through something that changes together constantly? (concept)
- The answer skeleton: a monolith wins when the team is small, the domain isn't clearly separable, or low-latency in-process calls matter more than independent deployability (concept)
- Walking it: a 5-person startup choosing a modular monolith over microservices — one deployable, one on-call rotation, in-process function calls instead of network hops between "services" that would otherwise be owned by the same two engineers anyway (concept)
- Walking it: a concrete scenario — that same startup, still pre-product-market-fit, is redesigning its core domain model every few weeks as they learn what customers actually want; splitting into microservices now would mean renegotiating service boundaries and API contracts on the same weekly cadence, which is far more expensive across service boundaries than inside one codebase (concept)
- Walking it: what it costs specifically — every service boundary you add turns a function call into a network call (new latency, new failure mode), and a single logical transaction that used to be one database transaction now needs a saga or eventual consistency across services (diagram)
- The trade-off to name out loud: microservices buy independent scaling and independent deployability at the direct cost of operational complexity (more moving parts to monitor, deploy, and debug) and distributed-systems failure modes a monolith never has to deal with — that trade only pays off once you actually have the team scale or the scaling needs that justify it (compare)
- Follow-up: "the team is now 50 people — has the calculus changed?" — likely yes; at that scale a monolith becomes a deployment and ownership bottleneck (everyone blocked on the same release train, unclear ownership of shared code) that microservices' independent deployability directly solves (concept)
- Follow-up: "can you get some of microservices' benefits without paying the full network-hop cost?" — a modular monolith with strict internal module boundaries (enforced via code structure, not network calls) captures a lot of the organizational-clarity benefit while keeping calls in-process, as a middle ground (concept)
- Pitfall: adopting microservices for a small team because "that's what big companies do," without the team scale or domain separability that made it the right call for those companies (pitfall)
- The 60-second version (concept)
- cross-link: monolith-vs-microservices

### Topic: Is this design over-engineered for what's actually needed? (iv-spotting-over-engineering, advanced)
Tests whether you can look at a design (yours or a given one) and identify speculative complexity added for imagined future scale that the stated requirements don't justify.
- The question as asked, and why over-engineering is graded as a real flaw, not just "being thorough" (overview)
- Clarifying questions: which requirements are stated, and which parts of the design serve a requirement no one actually asked for? Is there a real, near-term signal that the imagined future scale is coming, or is it purely speculative? (concept)
- The answer skeleton: check every component against a stated requirement; cut anything justified only by "future scale" that isn't backed by an actual signal (concept)
- Walking it: a worked example — event sourcing and CQRS added to a low-write internal admin tool serving 50 employees, when a straightforward CRUD service with a normal relational database would have shipped in a fraction of the time and been far easier for the next engineer to understand (concept)
- Walking it: a concrete scenario — a design proposes sharding a database from day one for a product with zero users yet, adding real complexity (choosing a shard key, cross-shard query limitations) to solve a scaling problem that doesn't exist and might never materialize in the product's current form (concept)
- Walking it: what a right-sized version looks like instead — build the simple version first, but leave the specific seam that would make it easy to add sharding *later* (e.g., a shard-key-shaped column present from day one, even if there's only one shard), which costs almost nothing now and preserves the option (diagram)
- The trade-off to name out loud: preparing for imagined future scale costs real velocity and complexity today for a benefit that may never be needed; under-preparing risks a genuinely painful migration later — the resolution isn't "always simple" or "always future-proof," it's matching the investment to the actual likelihood and cost of the future scenario (compare)
- Follow-up: "the interviewer says 'but what if we do need that scale later?' — how do you respond?" — name the concrete, cheap seam you'd leave for that future need instead of building the whole future-proofed system now, showing you've thought about it without paying for it prematurely (concept)
- Follow-up: "how do you tell the difference between over-engineering and reasonable defensive design?" — reasonable defensive design solves a problem you can point to evidence for (a stated NFR, a known growth trajectory); over-engineering solves a problem justified only by "just in case" (concept)
- Pitfall: adding complexity to "future-proof" a design against a scale that isn't in the stated requirements and has no supporting signal (pitfall)
- The 60-second version (concept)

### Topic: What's the simplest thing that could actually work here? (iv-simplest-thing-that-could-work, advanced)
Tests whether you default to starting simple and adding complexity only when justified — a proactive design stance, distinct from spotting over-engineering after the fact in an existing design.
- The question as asked, and why leading with the simple answer signals more seniority than leading with the impressive one (overview)
- Clarifying questions: what's the actual current scale and the realistic near-term scale, as opposed to the scale the problem statement's *name* makes you imagine? (concept)
- The answer skeleton: state the simplest architecture that meets the actual stated requirements first, explicitly, before layering in complexity — and only add each piece of complexity tied to a specific requirement it solves (concept)
- Walking it: a worked example — asked to "design a URL shortener," the simplest thing that could work is a single service with a relational database and a base62-encoded auto-increment ID — no distributed ID generation, no sharding, no CDN — stated plainly as the starting point before discussing what changes at scale (concept)
- Walking it: a concrete scenario — a candidate jumps straight to a multi-region, sharded, cache-everywhere design for a problem whose stated scale is 10,000 users; the interviewer has to redirect them back to something reasonable for the actual numbers given, costing the candidate time and signaling they don't calibrate complexity to requirements (concept)
- Walking it: how you *use* the simple starting point in the interview — state it, then proactively walk forward: "this works fine until X, at which point I'd add Y" — showing the escalation path rather than skipping straight to the complex end state (diagram)
- The trade-off to name out loud: starting simple risks looking like you don't know the advanced techniques if you never get to layer them in — the fix is stating the simple answer *and* immediately naming what would break it and what you'd add, so the simplicity reads as calibration, not as a knowledge gap (compare)
- Follow-up: "so you'd really ship this without a cache or a CDN at all?" — yes, if the stated scale doesn't need one yet; naming the exact metric that would trigger adding one is a stronger answer than adding it preemptively "to be safe" (concept)
- Follow-up: "what's the risk of starting simple if you're wrong about the scale?" — name the migration cost of adding the complexity later versus the cost of carrying it unused now — for most components, adding it later is cheaper than most candidates assume, which is the actual argument for starting simple (concept)
- Pitfall: opening with the most sophisticated architecture you know regardless of the stated scale, because it feels like it demonstrates more knowledge (pitfall)
- The 60-second version (concept)

### Topic: If you had to ship this in a month, what would you cut? (iv-scoping-for-a-deadline, advanced)
Tests whether you can separate must-have from nice-to-have under real deadline pressure and articulate the user-facing cost of each cut, rather than vaguely promising to "move faster."
- The question as asked, and why "we'd just work harder/faster" isn't a real answer to a scoping question (overview)
- Clarifying questions: what's the one thing this system absolutely cannot fail to do even in a minimal version? Is the deadline truly fixed, or is there room to negotiate scope with the business first? (concept)
- The answer skeleton: identify the core user-facing capability that must ship, and name specific pieces you'd cut or downgrade — each with the concrete cost of cutting it, not just "we'd simplify" (concept)
- Walking it: a worked example — for a ticket-booking system, the core that must ship is "a user can search, select, and pay for a seat without double-booking it"; cut for launch: multi-currency support (ship USD-only), seat-map visualization (ship a simple list of available seats), and email receipts (ship an in-app confirmation only, add email post-launch) (concept)
- Walking it: a concrete scenario — the team is tempted to cut the double-booking prevention logic itself to save a week, since it's the hardest part to build correctly; that's the wrong cut, because it's the one thing that actually protects the business from real financial and reputational damage — the discipline here is cutting *features*, never cutting the core correctness guarantee (concept)
- Walking it: what "downgrade, don't cut" looks like for something that can't be fully dropped — instead of building auto-scaling infrastructure in month one, launch on a fixed, generously-sized instance and monitor manually, with auto-scaling as a fast-follow once real traffic patterns are known (diagram)
- The trade-off to name out loud: cutting scope to hit a deadline trades completeness now for technical or product debt later (the fast-follow work has to actually happen) — the real skill isn't cutting, it's cutting the *right* things and being explicit about what's deferred, not silently dropped (compare)
- Follow-up: "the business insists nothing can be cut and the deadline can't move — what do you say?" — make the trade-off explicit and force the conversation: name what quality or scope will actually suffer if both constraints are held, rather than silently absorbing an impossible ask and having it surface as a worse outcome later (concept)
- Follow-up: "you shipped the cut-down version — how do you make sure the deferred pieces actually get built later and don't just get forgotten?" — track deferred scope as committed backlog items with an owner and rough timeline at launch time, not a vague "we'll get to it," because deprioritized-forever is the default outcome otherwise (concept)
- Pitfall: cutting the core correctness or safety guarantee to save time, rather than cutting peripheral features, because the core is usually the hardest and most tempting thing to defer (pitfall)
- The 60-second version (concept)

### Topic: What technical debt would you knowingly take on to hit this deadline? (iv-knowingly-taking-on-technical-debt, advanced)
Tests whether you can name a specific, deliberate corner cut (not a vague "we'd take on some debt") and describe how you'd track and eventually repay it, distinct from the scope-cutting question, which trims features rather than incurring debt inside a feature you still ship.
- The question as asked, and how it differs from cutting scope — this is shipping the full feature but with an intentionally worse implementation underneath (overview)
- Clarifying questions: is the pressure a one-time deadline, or an ongoing pace that would make this debt compound indefinitely if never repaid? Which corner, if cut, is genuinely reversible later versus one that gets more expensive to fix the longer it's live? (concept)
- The answer skeleton: name a specific implementation shortcut, state explicitly why it's safe to take *now*, and say what would trigger paying it back (concept)
- Walking it: a worked example — hardcoding a single-region deployment to hit launch instead of building multi-region from day one, explicitly because the business's initial user base is entirely in one geography, with a clear trigger to revisit (international expansion plans) rather than an open-ended "we'll get to it" (concept)
- Walking it: a concrete scenario — a team ships a feature using synchronous polling instead of the properly event-driven design they know they eventually want, because building the event infrastructure would blow the deadline; they explicitly log this as debt with a follow-up ticket, and revisit it once polling load actually becomes a measurable cost, rather than replacing it preemptively or forgetting about it (concept)
- Walking it: the kind of debt that's *not* safe to take on even under deadline pressure — skipping data-integrity safeguards (e.g., no idempotency key on a payment write) is a debt that gets more expensive and riskier the longer it's live, not less, and shouldn't be on the "acceptable to defer" list regardless of the deadline (diagram)
- The trade-off to name out loud: technical debt is a legitimate tool, not automatically a mistake — the difference between good and bad debt is whether it's named, tracked, and has a clear repayment trigger, versus silent and indefinite (compare)
- Follow-up: "how do you make sure this debt actually gets paid down instead of becoming permanent?" — the same discipline as deferred scope: a tracked ticket with an owner and a concrete trigger condition, revisited at a regular cadence (e.g., every planning cycle), not a mental note that quietly disappears (concept)
- Follow-up: "the deadline moved up again and there's pressure to take on more debt in the same area — where's the line?" — the line is whatever debt compounds or touches correctness/safety; debt that stays isolated and doesn't get more expensive to fix over time is more acceptable to stack than debt that does (concept)
- Pitfall: describing "we'd take on some technical debt" with no specific corner named and no repayment plan, which is indistinguishable from just building it badly with no intention of ever fixing it (pitfall)
- The 60-second version (concept)

### Topic: The interviewer disagrees with your design choice — how do you respond? (iv-defending-design-under-pushback, expert)
Tests composure and reasoning under direct challenge — can you either defend the choice with a concrete reason, or genuinely update, without getting defensive or caving reflexively.
- The question as asked, and the two failure modes it's checking for — caving instantly, or refusing to budge (overview)
- Clarifying questions: is this genuine disagreement pointing at something you missed, or a deliberate pressure-test to see how you handle challenge? (concept)
- The answer skeleton: restate the trade-off you weighed, ask what changed in their framing, then either defend or revise with a stated reason (concept)
- Walking it: a worked example — pushback on "why not just shard by user ID," responding with the specific skew risk you were avoiding: "I considered that, but our access pattern has a small number of power users generating a disproportionate share of writes, which would create a hot shard — I chose a composite key to spread that load instead" (concept)
- Walking it: a concrete scenario — the interviewer pushes back on a caching choice with a scenario you hadn't considered (cold-start after a region failover); rather than defending the original answer reflexively, acknowledging the gap directly — "that's a real gap, cold-start after failover would hit the DB hard; I'd add a cache-warming step to the failover procedure" — while still standing behind the parts of the original design that hold up (concept)
- Walking it: the tone that lands well versus poorly — matter-of-fact and specific ("here's the exact scenario I was optimizing for") reads as confident; over-explaining or getting visibly flustered reads as insecure even if the underlying reasoning is sound (diagram)
- The trade-off to name out loud: conceding too easily under any pushback signals no real conviction behind your choices; never conceding signals you can't actually update your thinking with new information — the balance is genuinely evaluating each specific challenge on its merits, live (compare)
- Follow-up: "what if the interviewer is right and you missed something?" — say so plainly and specifically ("you're right, I hadn't accounted for that") and update the design concretely, without over-apologizing or spending the next five minutes re-litigating the original mistake (concept)
- Follow-up: "what if you're confident you're right but the interviewer keeps pushing?" — restate your reasoning once, clearly, with the specific evidence or scenario behind it — you don't need to escalate the disagreement or repeat yourself defensively, and a confident, calm restatement is itself part of what's being evaluated (concept)
- Pitfall: abandoning a well-reasoned choice the moment it's challenged, signaling no real conviction behind it — or the opposite, digging in on a choice that's actually wrong once shown a scenario it doesn't handle (pitfall)
- The 60-second version (concept)
- cross-link: handling-interviewer-pushback

### Topic: You disagree with a senior engineer's design choice — how do you raise it? (iv-disagreeing-with-a-senior-engineer, expert)
Tests real-world influence-without-authority — distinct from the interviewer-pushback question, which is about defending your own answer under a live interview challenge; this is about surfacing disagreement with someone else's design in an actual working context.
- The question as asked, and why this is really a question about how you disagree productively, not whether you're right (overview)
- Clarifying questions: is the disagreement about a reversible implementation detail or a hard-to-undo architectural commitment? Has the design already shipped, or is it still a proposal you can influence before commitment? (concept)
- The answer skeleton: lead with the specific concern and its concrete cost, frame it as a question or a trade-off worth discussing rather than a verdict, and pick the venue (a design review, not a hallway ambush) that gives the disagreement a fair hearing (concept)
- Walking it: a worked example — "I noticed the proposal uses synchronous calls between these three services — I'm worried about the added latency and coupling; have we considered making the notification step async, given it's not on the critical path?" instead of "this design is wrong, it should be event-driven" (concept)
- Walking it: a concrete scenario — a senior engineer proposes a schema that will be very expensive to change once real data is in it; raising the concern *before* the migration ships (in the design review) costs a few minutes of debate, while raising it after ships means a costly data migration to fix — timing the disagreement to before the irreversible commitment is the actual skill being tested (concept)
- Walking it: what happens if the senior engineer disagrees back and holds their position — voicing the concern once, clearly, with the reasoning and its cost, is often enough; escalating repeatedly past a genuine hearing starts to cost more in team dynamics than the design point is usually worth, unless the risk is severe enough to justify pushing further (diagram)
- The trade-off to name out loud: raising disagreement risks the relationship and your own political capital if done poorly, and staying silent risks a design flaw shipping unchallenged — the resolution is scaling how hard you push to how severe and how reversible the consequence actually is (compare)
- Follow-up: "you raised it, they still disagree, and you think they're genuinely wrong — what now?" — if the decision is reversible and low-stakes, defer to their seniority and move on, noting it as something to revisit if your concern materializes; if it's high-stakes and hard to reverse, escalate to a broader review or a shared decision-maker rather than either silently complying or unilaterally overriding them (concept)
- Follow-up: "what if you're the one who's actually wrong?" — treat it as a real possibility going in, not a formality — asking "what am I missing?" genuinely, rather than only asserting your position, is what makes the disagreement collaborative instead of adversarial (concept)
- Pitfall: either staying silent to avoid friction on a real, costly concern, or pushing the disagreement repeatedly past a fair hearing in a way that reads as undermining rather than collaborating (pitfall)
- The 60-second version (concept)

### Topic: How would you migrate this system to a new architecture while it's serving live traffic? (iv-migrating-under-load, expert)
The hardest applied brownfield question — tests whether you can sequence a live migration (dual-write, shadow traffic, phased cutover) for a system that cannot go down, and name what you'd monitor to know it's safe to proceed at each stage.
- The question as asked, and why "just switch over one weekend" isn't a viable answer at this level (overview)
- Clarifying questions: can any downtime be tolerated at all, and what's the rollback point if the new system misbehaves? Is the hard part the data migration, the traffic cutover, or both? (concept)
- The answer skeleton: shadow the new system with live traffic first, then dual-write, then phase reads over, verifying at each gate before proceeding (concept)
- Diagram: a live migration staged as shadow → dual-write → phased read cutover → decommission old (diagram)
- Walking it: a concrete scenario — migrating an orders database from a monolithic Postgres instance to a sharded design: stage one, the new sharded store is written to in shadow alongside the real writes, with nothing reading from it yet; stage two, a small percentage of reads are served from the new store and diffed against the old store's answer for the same query; stage three, once the diff rate is near zero for a sustained window, reads are phased over fully; stage four, the old store is decommissioned only after a safety window with zero incidents (concept)
- Walking it: what "verifying at each gate" actually means concretely — an automated diff rate threshold (e.g., proceed only if mismatches stay under 0.01% over 48 hours), not a subjective "looks good" call from the team (concept)
- The trade-off to name out loud: this staged approach is far slower than a cutover weekend and costs real engineering time running two systems and a diffing pipeline in parallel — that cost buys you the ability to catch a correctness or performance problem while it's still low-blast-radius, instead of discovering it at 100% cutover (compare)
- Follow-up: "the new system's data has drifted from the old one mid-migration — how do you catch that?" — the same diffing pipeline used to gate the cutover, run continuously during the dual-write period, not just as a one-time check before flipping reads (concept)
- Follow-up: "how do you handle a schema difference between old and new that can't be dual-written identically?" — a translation layer at the write path that maps the old shape to the new one during the transition, accepting that layer as temporary migration-only complexity that gets deleted once the old system is decommissioned (concept)
- Pitfall: cutting over all traffic at once "since testing looked good," with no staged, gated verification against real production data and traffic (pitfall)
- The 60-second version (concept)
- cross-link: brownfield-system-design
- cross-link: strangler-fig-and-migration-patterns

### Topic: How would you convince leadership to invest in a costly re-architecture? (iv-selling-a-rearchitecture, expert)
Tests whether you can make a business case for an expensive, non-feature-shipping investment in terms non-technical stakeholders act on — cost, risk, and opportunity cost — rather than only technical justification.
- The question as asked, and why "the current architecture is bad" is not itself a business case (overview)
- Clarifying questions: what's the concrete, measurable pain the current architecture is causing today — lost revenue, missed deals, engineering velocity, incident frequency? Who's the actual audience for this pitch, and what do they already care about? (concept)
- The answer skeleton: translate the technical problem into the business terms the audience already tracks — cost, risk, or speed — with real numbers, and present the re-architecture as the cheaper option relative to a named alternative, not in isolation (concept)
- Walking it: a worked example — instead of "our monolith is hard to maintain," present "we've had 6 Sev1 outages in the current architecture this quarter, each costing an estimated $50K in lost transactions, and our own postmortems trace 4 of them to the same underlying coupling problem that this re-architecture directly fixes" (concept)
- Walking it: a concrete scenario — pitching a data-store migration by quantifying the *opportunity cost* of not doing it: "our current database can't support the multi-region expansion the roadmap needs for next year; without this migration, that roadmap item isn't achievable at all, not just slower" — tying the technical investment directly to a business initiative leadership already wants (concept)
- Walking it: what to bring to make the pitch credible instead of speculative — a phased plan with a cheaper first milestone that delivers partial value quickly, rather than asking for the full budget upfront for a multi-quarter effort with no visible progress until the end (diagram)
- The trade-off to name out loud: framing in pure business terms risks oversimplifying real technical nuance that matters for the actual execution; framing in pure technical terms risks losing the audience that controls the budget — the pitch has to hold both, technical accuracy for the team executing it and business framing for the people funding it (compare)
- Follow-up: "leadership says the ROI isn't clear enough — what do you do?" — narrow the ask to the smallest phase that produces a measurable result, proving the case with real data before asking for the rest of the investment, rather than re-arguing the same full pitch louder (concept)
- Follow-up: "you get the budget, but 6 months in, a critical feature deadline threatens to pull the team off the re-architecture — how do you protect it?" — the same tool as an error budget for reliability: pre-agree what a pause versus an outright cancellation looks like, and protect at minimum whatever partial milestone is already in flight rather than letting it fully unwind (concept)
- Pitfall: pitching a re-architecture purely on technical merit or "best practice," without quantifying the business cost of the status quo or the cost of the alternative (pitfall)
- The 60-second version (concept)
- cross-link: writing-a-design-doc
- cross-link: cost-and-org-aware-design

### Topic: What's the question a staff engineer would ask that a mid-level engineer wouldn't think to? (iv-staff-level-followups, expert)
A meta-question testing calibration itself — can you name organizational, cost, and long-horizon questions (ownership, migration cost, blast radius across teams) beyond the technical design.
- The question as asked, and why this is really asking "do you know what you don't know yet" (overview)
- Clarifying questions: is the interviewer looking for one sharp example or a broader sense of the categories of questions you'd reach for? (concept)
- The answer skeleton: name questions about ownership, long-term cost, org boundaries, and reversibility — not more technical detail (concept)
- Walking it: "who owns this once it's live, and what happens when that team's priorities shift?" as a staff-level question — a mid-level engineer optimizes the design for launch; a staff engineer asks who's still accountable for it two reorgs from now (concept)
- Walking it: "how expensive is it to reverse this decision in a year?" as a staff-level question — distinguishing a cheap, reversible choice (a caching strategy) from an expensive, hard-to-reverse one (a primary data store or a public API contract), and investing proportionally more scrutiny in the latter (concept)
- Walking it: a third example grounding it further — "what does this design cost a *different* team we're not talking to right now?" (e.g., a new required field that every downstream consumer of an event now has to handle), surfacing blast radius outside the room the design conversation is happening in (concept)
- The trade-off to name out loud: asking these organizational and cost questions takes real interview time away from technical depth — the staff-level judgment is knowing when a design decision is significant enough to warrant spending that time, versus one that's clearly reversible and low-stakes enough to just decide and move on (compare)
- Follow-up: "you named three — which one actually matters most for this specific system?" — pick based on which answer, if it went badly, would be hardest to undo for *this* system specifically, not a generically "most important" sounding one (concept)
- Follow-up: "how do you avoid this turning into analysis paralysis, asking organizational questions about everything?" — reserve them for decisions with real cost or reversibility stakes; a routine, cheap, reversible choice doesn't need an ownership-and-blast-radius review (concept)
- Pitfall: answering with a deeper technical question (e.g., a more advanced caching strategy) instead of an organizational, cost, or reversibility one, missing what the meta-question is actually probing (pitfall)
- The 60-second version (concept)
- cross-link: staff-level-system-design-signal

### Topic: Two of your requirements conflict — which do you sacrifice, and how do you justify it? (iv-tradeoff-under-conflicting-constraints, expert)
Tests whether you can make and defend an explicit sacrifice under genuinely incompatible constraints (cost vs latency, consistency vs availability) instead of hand-waving that you'll "balance" both.
- The question as asked, and why "we'll balance both" is a non-answer to a genuine conflict (overview)
- Clarifying questions: which constraint was set by the business and which by convention or habit — is either one actually negotiable, or are both truly fixed? What's the real cost of missing each one, not just which sounds more important? (concept)
- The answer skeleton: name both constraints explicitly, state which one you're sacrificing and by how much, and justify it against the actual cost of each (concept)
- Walking it: a worked example — a hard $10K/month infra budget cap versus a 100ms p99 latency SLA that, together, aren't both achievable with the given traffic; naming both explicitly and stating "I'd hold the budget and relax latency to 250ms, because the product's users tolerate that latency band based on our current analytics, and the budget constraint came directly from finance with no flexibility" (concept)
- Walking it: a concrete scenario — consistency versus availability during a network partition on a payments ledger; explicitly choosing consistency (reject writes during the partition) because an incorrect balance is a worse outcome than a temporarily unavailable write path, and saying so plainly rather than describing a vague "highly available and consistent" design that quietly can't exist under partition (concept)
- Walking it: what a *bad* answer sounds like for contrast — "we'd use a hybrid approach that balances both" with no specific mechanism or number, which under questioning reveals one constraint is silently being dropped without anyone deciding to drop it (diagram)
- The trade-off to name out loud: making the sacrifice explicit is itself the trade-off being tested — an implicit, unstated sacrifice reads as either not understanding the conflict exists, or hoping no one asks; a stated one reads as ownership of a hard call (compare)
- Follow-up: "the business says both are truly non-negotiable — what's your actual next move?" — escalate the conflict explicitly to whoever owns both constraints, forcing an actual decision, rather than quietly building something that fails one of them and hoping it isn't noticed (concept)
- Follow-up: "how do you know you picked the right one to sacrifice?" — trace each constraint back to its actual cost if violated (revenue impact, user trust, compliance risk) and sacrifice the one with the smaller real cost — a judgment call you should be able to defend with a reason, not a coin flip (concept)
- Pitfall: describing a "balanced" design that quietly fails one of the two constraints without saying so, leaving the interviewer to discover the gap themselves (pitfall)
- The 60-second version (concept)

---

