# System Design — Phase C (HLD track additions)

New material for the merged `system-design` Study Area's HLD side: two new groups (Geo-Distribution
& Disaster Recovery; Security & Multi-Tenancy in Design) plus a small set of expert-tier additions to
existing HLD groups in `briefs/expanded/system-design.md`. Format matches that file exactly — see
**Boundary notes** at the end for cross-area ownership calls.

---

## Group: Geo-Distribution & Disaster Recovery (geo-distribution)
*multi-region topologies, routing, RPO/RTO, and the cost/compliance forces that drive them*

### Topic: Single-Region vs Multi-Region (single-region-vs-multi-region, intermediate)
What actually forces a system out of one region — latency to distant users, availability against a
whole-region outage, and data-residency law — versus reaching for multi-region prematurely.
- Why "one region" is the right default until a specific force breaks it (concept)
- The three forces that push you multi-region: latency, availability, residency (concept)
- Diagram: a single-region system and its one regional blast radius (diagram)
- Latency: physics sets a floor that horizontal scaling inside one region can't fix (concept)
- Availability: what a full regional outage takes down, and how often it happens (concept)
- Compare: single-region-with-backup-region vs true multi-region (compare)
- Pitfall: going multi-region to solve a scaling problem that horizontal scale-out already solves (pitfall)
- Interview: "Your service is single-region — what would make you change that?" (interview)

### Topic: Multi-Region Topologies (multi-region-topologies, advanced)
The concrete shapes a multi-region system takes — active-passive, active-active, read-local/write-global,
and follow-the-sun — and what each buys against what it costs in complexity.
- Active-passive: a warm standby region that takes over on failure (concept)
- Active-active: multiple regions serving live read *and* write traffic simultaneously (concept)
- Diagram: active-passive failover vs active-active traffic split (diagram)
- Read-local, write-global: reading from the nearest region, funneling writes through one owner (concept)
- Follow-the-sun: the active write region shifts with the working day (concept)
- Compare: the four topologies by consistency guarantees, cost, and failover complexity (compare) — cross-link: consistency-models
- Pitfall: calling a system "active-active" when every write still serializes through one region (pitfall)
- Interview: "Why not just run active-active everywhere?" (interview)

### Topic: Routing Users to a Region (geo-routing-and-failover, advanced)
Getting a request to the right region — GeoDNS, anycast, latency-based routing — and what quietly
breaks the moment a region needs to fail over.
- GeoDNS and latency-based routing: sending users to their nearest healthy region (concept) — cross-link: dns-based-and-global-load-balancing
- Anycast: one IP, many regions, routing decided by the network layer (concept)
- Diagram: a request's routing path from client to region under normal operation (diagram)
- What breaks on failover: DNS TTLs, sticky client caches, in-flight connections (concept)
- Health-based routing: pulling a region out of rotation before users notice (concept)
- Compare: DNS-based failover vs anycast failover — speed and blast radius (compare)
- Pitfall: a 60-second DNS TTL that becomes a 10-minute outage because clients and resolvers cache it longer (pitfall)
- Interview: "A region just went dark — walk me through what happens to in-flight traffic" (interview)

### Topic: RPO, RTO & Failover Drills (rpo-rto-and-failover-drills, expert)
Turning "we have backups" into a number you can defend — recovery point and recovery time
objectives — and the discipline of actually rehearsing failover before you need it for real.
- RPO vs RTO: how much data you can lose vs how long you can be down (concept)
- Diagram: RPO and RTO plotted on a timeline around a failure event (diagram)
- Backup strategies and their RPO: continuous replication vs periodic snapshot vs nightly backup (concept)
- Restore strategies and their RTO: warm standby vs cold rebuild-from-backup (concept)
- Compare: backup/restore approaches by RPO, RTO, and steady-state cost (compare)
- Running a failover drill: game days, chaos-style regional kill switches, and what "tested" means (concept)
- Pitfall: a disaster-recovery plan that has never been executed end-to-end (pitfall)
- Interview: "What's your RPO and RTO for this design, and how do you know?" (interview)

### Topic: Data Residency & Cross-Region Cost (data-residency-and-cross-region-cost, expert)
Locality law and network egress as first-class design constraints, not afterthoughts bolted on
once legal or finance objects.
- Data residency: why some data legally cannot leave a region or country (concept)
- GDPR-style locality constraints as a system design input, not a legal footnote (concept)
- Diagram: a design partitioned by residency boundary rather than by load (diagram)
- Cross-region replication traffic and egress cost: the bill multi-region actually generates (concept)
- Compare: replicate-everything vs replicate-only-what-residency-requires (compare)
- Pitfall: designing the ideal active-active topology, then discovering residency law forbids it (pitfall)
- Interview: "This system must keep EU user data in the EU — how does that change your design?" (interview)

---

## Group: Security & Multi-Tenancy in Design (design-security)
*the design-level decisions — where auth lives, how tenants are isolated — not cryptography internals*

> Boundary: this group covers the *design decision*, not the underlying mechanism. Cryptographic
> primitives, OWASP Top 10, and appsec vulnerability mechanics belong to the `security` area
> (`cryptography`, `appsec`); the TLS handshake belongs to `computer-networks`' `network-security`.
> Reference those, don't re-teach them here.

### Topic: Designing Authentication & Sessions (designing-authentication-and-sessions, intermediate)
Where auth lives in an architecture, token vs session as an architectural choice, and how services
prove their identity to each other — not the cryptography behind any of it.
- Where authentication lives: client, edge/gateway, or each service (concept)
- Token-based vs session-based auth as an architectural trade-off, not just an implementation detail (compare)
- Diagram: a login request's path from client through gateway to an issued token (diagram)
- Service-to-service auth: mTLS and service identity vs passing a user's token downstream (concept) — cross-link: authn-authz
- Session invalidation and logout in a distributed, multi-service system (concept)
- Pitfall: a monolith's session model lifted unchanged into a microservices split (pitfall)
- Interview: "How would you design auth for a system with 20 internal services?" (interview)

### Topic: Designing Authorization at Scale (designing-authorization-models, advanced)
RBAC, ABAC, and ReBAC as design choices, and where the permission-check decision actually gets made
when a request has to clear it in single-digit milliseconds.
- RBAC vs ABAC vs ReBAC: three ways to model "can this user do this" (compare) — cross-link: authn-authz
- Diagram: a policy decision point (PDP) consulted by many policy enforcement points (PEP) (diagram)
- Centralizing authorization: one decision service vs authorization logic embedded per-service (concept)
- Permission checks at scale: caching decisions, latency budget, and staleness risk (concept)
- Modeling relationship-based access (ReBAC) for "who can see whose data" (concept)
- Compare: centralized policy service vs library-embedded policy checks (compare)
- Pitfall: an authorization check re-implemented slightly differently in every service (pitfall)
- Interview: "Design the permission system for a Google-Docs-style sharing model" (interview)

### Topic: Multi-Tenancy Isolation Models (multi-tenancy-isolation-models, advanced)
The three standard ways to isolate tenants in a shared system, and the noisy-neighbor problem that
decides which one you actually need.
- Shared table with a `tenant_id` column: cheapest, leakiest (concept)
- Schema-per-tenant and database-per-tenant: stronger isolation, higher operational cost (concept)
- Diagram: the isolation spectrum from shared-table to cluster-per-tenant (diagram)
- The noisy-neighbor problem: one tenant's load degrading every other tenant (concept)
- Compare: the three isolation models by isolation strength, cost, and operational burden (compare)
- Migrating a tenant between isolation tiers as it grows (concept)
- Pitfall: a missing `tenant_id` filter turning into a cross-tenant data leak (pitfall)
- Interview: "Design a multi-tenant SaaS backend for customers ranging from 10 to 10M users" (interview)

### Topic: Secrets, Keys & Encryption as Design Decisions (secrets-and-key-management-in-design, advanced)
Where secrets and encryption keys live in an architecture and who is allowed to touch them — the
design question, not the cipher.
- Secrets management: why credentials don't belong in config files or environment images (concept)
- Key management as a service: a KMS issuing and rotating keys instead of code hardcoding them (concept)
- Diagram: a service fetching a secret from a vault at boot vs baking it into the image (diagram)
- Encryption at rest vs in transit as two separate design decisions with different threat models (compare) — cross-link: cryptography
- Key rotation and the blast radius of a leaked key (concept)
- Pitfall: one shared master key protecting every tenant's data (pitfall)
- Interview: "How does this design handle a leaked database credential?" (interview)

### Topic: Abuse & Anti-Fraud in Design (abuse-and-antifraud-in-design, expert)
Designing the system to resist bots and abuse from day one — quotas, audit trails, and minimizing
the personal data you even collect — rather than bolting on defenses after an incident.
- Bot and abuse defense as an architectural concern: rate limits, challenge flows, device signals (concept) — cross-link: rate-limiting-algorithms
- Per-tenant and per-user quotas as a design primitive, not an afterthought (concept)
- Diagram: a request pipeline with an abuse-signal check inserted before the core path (diagram)
- Audit trails: designing for "who did what, when" before you need to answer that question (concept)
- PII minimization: designing to collect and retain the least data that does the job (concept)
- Compare: blocking suspicious activity in real time vs flagging it for async review (compare)
- Pitfall: an audit log that exists but can't answer "who deleted this row" fast enough to matter (pitfall)
- Interview: "How would you detect and stop a credential-stuffing attack against this login system?" (interview)

---

## Additions to existing group: Caching (caching)

### Topic: Cache Penetration & Negative Caching at Scale (cache-penetration-and-negative-caching, expert)
Beyond the stampede mitigations already covered — the traffic that never had a cache entry to miss
in the first place, and the probabilistic techniques that keep a hot cache from collapsing at extreme
fan-out.
- Cache penetration: repeated lookups for keys that don't exist, bypassing the cache every time (concept)
- Negative caching: caching the "not found" result itself, with a short TTL (concept)
- Diagram: a penetration attack hammering the DB vs the same traffic absorbed by negative caching (diagram)
- Probabilistic early expiration (e.g. XFetch-style): recomputing before expiry to avoid synchronized misses (concept) — cross-link: distributed-caching
- Compare: negative caching vs a bloom filter in front of the cache for existence checks (compare)
- Pitfall: negative-caching a transient error as if it were a permanent "not found" (pitfall)
- Interview: "Your cache hit rate looks fine but the DB is still getting hammered — why?" (interview)

## Additions to existing group: Storage at Scale (storage-scale)

### Topic: Storage Engine Choice as a Design Decision (storage-engine-choice-as-a-design-decision, expert)
B-tree vs LSM-tree isn't a database-internals footnote — it's a read/write amplification trade-off
that should drive which storage system you pick for a given workload.
- Why storage engine choice belongs in a system design conversation, not just a DBA's job (concept)
- B-tree engines: read-optimized, in-place updates, predictable point-lookup latency (concept)
- LSM-tree engines: write-optimized, append-then-compact, better write throughput at a compaction cost (concept) — cross-link: storage-indexing
- Diagram: the write path and read path shapes for a B-tree engine vs an LSM engine (diagram)
- Compare: B-tree vs LSM by write amplification, read amplification, and space amplification (compare)
- Matching engine choice to workload: write-heavy ingestion vs read-heavy lookup services (concept)
- Pitfall: picking a database for its feature set while ignoring that its engine is wrong for your write pattern (pitfall)
- Interview: "You're choosing a datastore for a write-heavy event-ingestion pipeline — how does the storage engine factor in?" (interview)

## Additions to existing group: Microservices & Service Mesh (microservices)

### Topic: Service Boundaries Under Organizational Constraints (service-boundaries-and-conways-law, expert)
Conway's Law means your org chart shows up in your architecture whether you plan for it or not —
and platform-vs-product framing changes where a boundary should sit.
- Conway's Law: systems mirror the communication structure of the organizations that build them (concept)
- Diagram: a service boundary that matches team ownership vs one that cuts across three teams (diagram)
- Designing boundaries for team autonomy, not just for domain purity (concept) — cross-link: service-decomposition
- Platform architecture vs product architecture: shared capability teams vs feature teams (concept)
- Compare: optimizing boundaries for Conway's Law alignment vs optimizing for the "ideal" domain model (compare)
- Pitfall: a technically clean service split that forces two teams into constant cross-team coordination (pitfall)
- Interview: "Your org just split one team into three — should your service boundaries change?" (interview)

## Additions to existing group: Observability (observability)

### Topic: Cost-Aware Telemetry at Scale (cost-aware-telemetry-at-scale, expert)
Observability data itself becomes a scaling and cost problem — sampling strategy and cardinality
are design decisions, not a monitoring-team afterthought.
- Why "instrument everything" stops working once telemetry volume becomes its own bill (concept)
- Sampling strategies: head-based, tail-based, and adaptive sampling for traces (concept) — cross-link: distributed-tracing
- Diagram: a trace pipeline with a sampling decision point before storage (diagram)
- Cardinality explosions: how one high-cardinality label multiplies your metrics cost (concept)
- Compare: sampling to cut volume vs aggregating to cut cardinality — different problems, different fixes (compare)
- Pitfall: adding a user-ID label to a metric and 100x'ing the time-series count overnight (pitfall)
- Interview: "Your observability bill tripled after a launch — how do you diagnose and fix it?" (interview)

## Additions to existing group: Messaging & Streaming (messaging-streaming)

### Topic: Schema Evolution Across an Event Bus (schema-evolution-and-compatibility, expert)
Producers and consumers deploy independently, so a message schema has to change without breaking
whoever hasn't upgraded yet.
- Why schema change is harder on an event bus than behind a single API (concept) — cross-link: api-versioning-and-evolution
- Backward-compatible vs forward-compatible schema changes: who breaks if you get it wrong (compare)
- Diagram: an old consumer and a new consumer reading the same stream after a schema change (diagram)
- Schema registries: enforcing compatibility rules before a producer is allowed to publish (concept)
- Safe changes vs breaking changes: adding an optional field vs renaming or removing one (concept)
- Pitfall: a producer ships a "small" field rename that silently breaks every downstream consumer (pitfall)
- Interview: "How do you evolve an event's schema without a coordinated deploy of every consumer?" (interview)

---

## Boundary notes

- **`security` area** — owns cryptographic primitives (`cryptography`), OWASP Top 10 and vulnerability
  mechanics (`appsec`), and the general authn/authz mental model (`authn-authz`). `design-security`
  here covers only where those decisions get placed in an architecture (token vs session, PDP/PEP
  placement, KMS-as-a-service, isolation models) — cross-linked to `authn-authz` and `cryptography`
  rather than re-teaching them. Recommended home for the mechanism-level material stays `security`.
- **`databases` area** — owns storage-engine internals (`storage-indexing`: B-tree/LSM structure,
  write-ahead logs, compaction mechanics). The new `storage-engine-choice-as-a-design-decision` topic
  (added to `storage-scale`) treats engine choice as a *selection* decision for a system design
  interview and cross-links `storage-indexing` for the internals — recommended home for "how an
  LSM-tree actually compacts" stays `databases`.
- **`computer-networks` area** — owns the TLS handshake and protocol-level network security
  (`network-security`). `secrets-and-key-management-in-design` references encryption-in-transit as a
  design decision but does not re-teach TLS; recommended home for handshake mechanics stays
  `computer-networks`.
- **`cloud-devops-sre` area** — owns hands-on observability tooling and cost/capacity operations
  (`observability-ops`, `cost-capacity`). `cost-aware-telemetry-at-scale` (added to `observability`)
  is the *design-time* view — sampling and cardinality as architecture decisions before an incident
  forces the question; recommended home for Prometheus/Grafana setup, alert-pipeline plumbing, and
  ongoing cost-optimization operations stays `cloud-devops-sre`.
- **Within `system-design` itself** — `geo-routing-and-failover` cross-links `load-balancing`'s
  `dns-based-and-global-load-balancing` rather than repeating GeoDNS mechanics; `cdn-and-edge-caching`
  (in `caching`) remains the home for edge/CDN routing. `cache-penetration-and-negative-caching`
  cross-links `distributed-caching` for baseline stampede mitigations already covered there and adds
  only the incremental expert material (penetration, negative caching, probabilistic early expiration).
  `service-boundaries-and-conways-law` cross-links `service-decomposition` rather than re-deriving
  domain-boundary basics. `schema-evolution-and-compatibility` cross-links `api-design`'s
  `api-versioning-and-evolution` since both are instances of the same "independent deploys, shared
  contract" problem.
- **Considered and deliberately skipped:** an expert addition to `resilience` for "capacity-aware
  degradation / brownout / priority load shedding" — the existing `graceful-degradation-and-load-shedding`
  (advanced) topic already covers prioritizing traffic and what to shed first in enough depth that a
  separate expert topic would mostly restate it. Flagging for reviewer in case a genuinely distinct
  angle (e.g. quantitative admission control) is wanted later.
