# Area → Group map (schema v3 draft — for pruning)

Clean-sheet curriculum for CrackLoop. **Nothing here is final** — this is the buffet to prune.
Pick which **Areas** to ship, and within each, which **Groups**. Topics come after (per group).

## Locked hierarchy (schema v3)

```
area  → group → topic → { slides[], mcqs[], interviewQuestions[] }
```

| Level | Term | v3 JSON | Folder | Example |
|---|---|---|---|---|
| 1 | **Area** (domain) | `area` + index `areas[]` | `content/<area>/` | AI & Machine Learning |
| 2 | **Group** (subject) | `group` (NEW middle layer) | `content/<area>/<group>/` | Deep Learning |
| 3 | **Topic** (lesson) | `topic` | `content/<area>/<group>/<topic>/` | Introduction |
| 4 | **Slide** (page) | `slides[]` in `topic.json` | — | one screen: text / diagram / code |
| — | **MCQ** | `mcqs[]` in `mcq.json` | — | 4-option quiz |
| — | **Interview Q** | `interviewQuestions[]` in `interview.json` | — | real asked Q + model answer |

Files per topic: `topic.json` (slides) · `mcq.json` (mcqs) · `interview.json` (interview questions) · `assets/*.svg`.

**Tiers:** 🟢 Core (near-universal) · 🔵 Rec (commonly asked) · 🟡 Breadth (role/domain) · ⚪ Niche/emerging.

---

## Area 1 — Data Structures & Algorithms `data-structures-algorithms` 🟢

| Group | slug | Tier | Scope |
|---|---|---|---|
| Complexity & Big-O | `complexity` | 🟢 | asymptotic analysis, amortized, space-time trade-offs |
| Arrays & Strings | `arrays-strings` | 🟢 | in-place ops, prefix sums, string manipulation |
| Hashing | `hashing` | 🟢 | hash maps/sets, collisions, frequency patterns |
| Two Pointers & Sliding Window | `two-pointers-sliding-window` | 🟢 | window/pointer patterns on arrays & strings |
| Linked Lists | `linked-lists` | 🟢 | singly/doubly, reversal, cycle detection |
| Stacks & Queues | `stacks-queues` | 🟢 | monotonic stack, deque, queue-via-stacks |
| Trees & BSTs | `trees-bst` | 🟢 | traversals, BST ops, LCA, balanced trees |
| Heaps & Priority Queues | `heaps` | 🔵 | heapify, top-k, k-way merge |
| Tries & String Algorithms | `tries-strings` | 🔵 | trie, KMP, Rabin-Karp, suffix ideas |
| Graphs | `graphs` | 🟢 | traversal, shortest paths, MST, topological sort |
| Sorting & Searching | `sorting-searching` | 🟢 | comparison sorts, binary search & variants |
| Recursion & Backtracking | `recursion-backtracking` | 🟢 | permutations, subsets, constraint search |
| Dynamic Programming | `dynamic-programming` | 🟢 | 1D/2D, knapsack, LIS/LCS, state design |
| Greedy | `greedy` | 🔵 | exchange argument, interval scheduling |
| Intervals & Sweep Line | `intervals` | 🟡 | merge/insert, sweep, meeting rooms |
| Bit Manipulation | `bit-manipulation` | 🔵 | masks, XOR tricks, bit DP |
| Math & Number Theory | `math-number-theory` | 🟡 | gcd, primes, modular arithmetic, combinatorics |
| Coding Interview Strategy | `coding-interview-strategy` | 🔵 | pattern recognition, communication, complexity talk |

## Area 2 — Databases `databases` 🟢

| Group | slug | Tier | Scope |
|---|---|---|---|
| Relational Model & Keys | `relational-model` | 🟢 | relations, keys, constraints, relational algebra |
| SQL | `sql` | 🟢 | SELECT/joins/aggregation/grouping |
| Advanced SQL | `advanced-sql` | 🔵 | window functions, CTEs, stored programs |
| Data Modeling & Normalization | `data-modeling-normalization` | 🟢 | ER/EER, functional deps, 1NF→BCNF, denorm |
| Transactions & Concurrency | `transactions-concurrency` | 🟢 | ACID, isolation levels, locking, MVCC |
| Storage & Indexing | `storage-indexing` | 🟢 | B-trees, LSM, heap/clustered, index design |
| Query Processing & Optimization | `query-optimization` | 🔵 | planning, join algorithms, statistics |
| NoSQL & Modern Databases | `nosql` | 🔵 | KV/doc/column/graph, when to use |
| Distributed Databases | `distributed-databases` | 🔵 | sharding, replication, CAP/BASE, consensus |
| Database Ops | `database-ops` | 🟡 | backup/recovery, security, tuning |
| Data Warehousing & OLAP | `data-warehousing` | 🟡 | star schema, cubes, columnar |

## Area 3 — Operating Systems `operating-systems` 🟢

| Group | slug | Tier | Scope |
|---|---|---|---|
| OS Fundamentals | `os-fundamentals` | 🟢 | kernel, syscalls, user/kernel mode |
| Processes & Threads | `processes-threads` | 🟢 | PCB, context switch, IPC |
| CPU Scheduling | `scheduling` | 🟢 | FCFS/RR/priority/MLFQ, metrics |
| Concurrency & Synchronization | `concurrency-sync` | 🟢 | races, mutex/semaphore, monitors |
| Deadlocks | `deadlocks` | 🔵 | conditions, prevention/avoidance/detection |
| Memory Management | `memory-management` | 🟢 | allocation, fragmentation, segmentation |
| Virtual Memory & Paging | `virtual-memory` | 🔵 | page tables, TLB, replacement, thrashing |
| File Systems | `file-systems` | 🔵 | inodes, journaling, layout |
| I/O & Device Management | `io-systems` | 🟡 | interrupts, DMA, buffering |
| Linux/Unix Internals | `linux-internals` | 🟡 | processes, signals, /proc, tooling |

## Area 4 — Computer Networks `computer-networks` 🟢

| Group | slug | Tier | Scope |
|---|---|---|---|
| Network Fundamentals & Models | `network-fundamentals` | 🟢 | OSI/TCP-IP layering, encapsulation |
| Physical & Data Link Layer | `link-layer` | 🟡 | framing, MAC, switching, ARP |
| IP & Addressing | `ip-addressing` | 🔵 | IPv4/IPv6, subnetting, VLSM, NAT |
| Routing | `routing` | 🔵 | intra/inter-domain, BGP basics |
| Transport Layer | `transport-layer` | 🟢 | TCP handshake/flow/congestion, UDP |
| Application Layer | `application-layer` | 🟢 | HTTP/HTTPS, DNS, REST/websockets |
| TLS & Network Security | `network-security` | 🔵 | TLS handshake, common attacks |
| Modern Protocols | `modern-protocols` | 🟡 | QUIC, HTTP/3 |
| Load Balancing & CDNs | `network-infra` | 🔵 | L4/L7 LB, CDN/edge caching |
| Wireless & Mobile | `wireless` | ⚪ | Wi-Fi, cellular basics |
| Network Tools & Troubleshooting | `network-tools` | 🟡 | ping/traceroute/tcpdump, debugging |

## Area 5 — Computer Architecture `computer-architecture` 🔵

| Group | slug | Tier | Scope |
|---|---|---|---|
| Number Systems & Data Representation | `data-representation` | 🔵 | binary/hex, two's complement, IEEE-754 |
| Digital Logic & Boolean Algebra | `digital-logic` | 🟡 | gates, K-maps, combinational/sequential |
| Instruction Set Architecture | `isa` | 🔵 | RISC/CISC, addressing, encoding |
| CPU Datapath & Control | `cpu-datapath` | 🔵 | fetch-decode-execute, control signals |
| Pipelining & Hazards | `pipelining` | 🔵 | stages, structural/data/control hazards |
| Memory Hierarchy & Caches | `caches` | 🟢 | locality, mapping, coherence, policies |
| Virtual Memory (HW view) | `hw-virtual-memory` | 🟡 | TLB, page-table walk |
| Instruction-Level Parallelism | `ilp` | 🟡 | superscalar, OoO, branch prediction |
| Multicore & Parallelism | `multicore` | 🟡 | SMP, consistency models, SIMD |
| GPUs & Accelerators | `gpus-accelerators` | ⚪ | SIMT, domain-specific arch |
| Storage & I/O Hardware | `storage-hardware` | 🟡 | disks/SSD/NVMe, buses, interrupts |
| Performance & Power | `perf-power` | 🟡 | Amdahl, roofline, power scaling |

## Area 6 — Programming Languages & Compilers `languages-compilers` 🔵

| Group | slug | Tier | Scope |
|---|---|---|---|
| Language Paradigms | `paradigms` | 🔵 | imperative/OO/functional/logic |
| Type Systems | `type-systems` | 🔵 | static/dynamic, inference, generics, variance |
| Memory Management & GC | `memory-gc` | 🔵 | stack/heap, ref-counting, tracing GC |
| Compilers & Interpreters | `compilers` | 🔵 | lexing/parsing, IR, codegen, optimization |
| Runtimes & Virtual Machines | `runtimes` | 🟡 | JVM/CLR, JIT, bytecode |
| Concurrency Models | `concurrency-models` | 🔵 | threads, async/await, actors, CSP |
| Functional Programming | `functional` | 🟡 | immutability, higher-order, monads |

## Area 7 — System Design: LLD & HLD `system-design` 🟢

**Merged area** (former Area 7 *System Design (HLD)* + former Area 8 *Object-Oriented & Low-Level Design*). Both altitudes of design — the classes inside a service and the services inside a system — beginner to expert, for interviews and for the job.

54 groups · 472 topics. Group order below is the learning order and is read from `briefs/expanded/system-design.md` by `tools/regen_v3.py`. Full topic-level detail lives in that brief.

### Phase A — Foundations

| Group | slug | Topics |
|---|---|---|
| System Design Fundamentals | `sd-fundamentals` | 7 |
| Distributed Systems Core | `distributed-systems-core` | 6 |

### Phase B — Low-Level Design: concepts

| Group | slug | Topics |
|---|---|---|
| OOP Fundamentals | `oop-fundamentals` | 7 |
| SOLID & Design Principles | `design-principles` | 9 |
| Creational Patterns | `creational-patterns` | 5 |
| Structural Patterns | `structural-patterns` | 6 |
| Behavioral Patterns | `behavioral-patterns` | 9 |
| UML & Modeling | `uml` | 4 |
| Anti-Patterns & Code Smells | `anti-patterns` | 5 |
| Concurrency in OO Design | `oo-concurrency` | 6 |
| LLD in Practice | `lld-in-practice` | 5 |
| LLD Interview Framework | `lld-framework` | 6 |

### Phase C — Low-Level Design: case studies

| Group | slug | Topics |
|---|---|---|
| LLD Case Studies — Games | `lld-cases-games` | 6 |
| LLD Case Studies — Machines | `lld-cases-machines` | 6 |
| LLD Case Studies — Booking & Marketplaces | `lld-cases-booking` | 6 |
| LLD Case Studies — Infra Building Blocks | `lld-cases-infra` | 7 |
| LLD Case Studies — Business Domains | `lld-cases-business` | 7 |

### Phase D — High-Level Design: concepts

| Group | slug | Topics |
|---|---|---|
| Capacity Estimation | `capacity-estimation` | 5 |
| Load Balancing & Proxies | `load-balancing` | 8 |
| Caching | `caching` | 7 |
| Storage at Scale | `storage-scale` | 10 |
| Consistency & Replication | `consistency-replication` | 8 |
| Messaging & Streaming | `messaging-streaming` | 10 |
| Microservices & Service Mesh | `microservices` | 8 |
| API Design | `api-design` | 10 |
| Rate Limiting & Resilience | `resilience` | 8 |
| Search & Indexing | `search-indexing` | 8 |
| Observability | `observability` | 7 |
| Geo-Distribution & Disaster Recovery | `geo-distribution` | 5 |
| Security & Multi-Tenancy in Design | `design-security` | 5 |

### Phase E — High-Level Design: case studies

| Group | slug | Topics |
|---|---|---|
| Core Systems | `hld-cases-core` | 8 |
| Social & Messaging Systems | `hld-cases-social` | 8 |
| Media & Streaming Systems | `hld-cases-media` | 7 |
| Marketplace & Transactional Systems | `hld-cases-marketplace` | 8 |
| Infrastructure & Platform Systems | `hld-cases-infra` | 10 |

### Phase F — Design craft & the interview method

| Group | slug | Topics |
|---|---|---|
| Design in the Real World | `design-in-practice` | 5 |
| System Design Interview Playbook | `sd-playbook` | 10 |

### Phase G — Interview question bank: LLD & OOD

| Group | slug | Topics |
|---|---|---|
| LLD Interview Bank — OOP | `interview-lld-oop` | 14 |
| LLD Interview Bank — Principles | `interview-lld-principles` | 14 |
| LLD Interview Bank — Design Patterns | `interview-lld-patterns` | 14 |
| LLD Interview Bank — Concurrency | `interview-lld-concurrency` | 14 |
| LLD Interview Bank — Small Design Probes | `interview-lld-design-questions` | 14 |
| Distributed Systems Interview Bank — Foundations | `interview-distributed-fundamentals` | 14 |

### Phase H — Interview question bank: HLD

| Group | slug | Topics |
|---|---|---|
| HLD Fundamentals — Interview Questions | `interview-hld-fundamentals` | 13 |
| Estimation — Interview Questions | `interview-hld-estimation` | 13 |
| Caching — Interview Questions | `interview-hld-caching` | 13 |
| Data at Scale — Interview Questions | `interview-hld-data` | 13 |
| Consistency & Replication — Interview Questions | `interview-hld-consistency` | 13 |
| Messaging & Streaming — Interview Questions | `interview-hld-messaging` | 13 |
| APIs & Resilience — Interview Questions | `interview-hld-apis-resilience` | 13 |
| Operations — Interview Questions | `interview-hld-operations` | 13 |
| Senior/Staff Trade-off Signal — Interview Questions | `interview-hld-tradeoffs` | 14 |

### Phase I — Interview question bank: experience & round formats

| Group | slug | Topics |
|---|---|---|
| Talking About Your Own Designs | `design-experience-questions` | 5 |
| Interview Formats Beyond the Standard Loop | `design-round-formats` | 3 |

> Area 8 is intentionally absent — it was merged into this area. Area numbering keeps its
> original values; `regen_v3.py` derives area order from the *sequence* of `## Area` headings,
> not the numbers, so the gap is cosmetic.

## Area 9 — Software Engineering & Craft `engineering-craft` 🟢

| Group | slug | Tier | Scope |
|---|---|---|---|
| Version Control & Git | `git` | 🔵 | branching, rebase/merge, workflows |
| Testing & Quality | `testing` | 🟢 | unit/integration/e2e, TDD, mocking, coverage |
| CI/CD & Release Engineering | `cicd` | 🔵 | pipelines, deploys, feature flags |
| Debugging & Incident Response | `debugging` | 🔵 | systematic debugging, on-call, postmortems |
| Code Review & Collaboration | `code-review` | 🔵 | review practices, giving/receiving feedback |
| Clean Architecture & DDD | `clean-architecture` | 🔵 | layering, boundaries, domain modeling |
| Performance Engineering | `performance-engineering` | 🔵 | profiling, benchmarking, optimization |
| Technical Communication | `technical-communication` | 🟡 | design docs, RFCs, writing |
| Behavioral & Staff+ Competencies | `behavioral` | 🟢 | STAR, leadership, scope/impact |

## Area 10 — Cloud, DevOps & SRE `cloud-devops-sre` 🔵

| Group | slug | Tier | Scope |
|---|---|---|---|
| Cloud Computing Fundamentals | `cloud-fundamentals` | 🔵 | IaaS/PaaS/SaaS, regions/AZs, core services |
| Containers & Docker | `containers` | 🔵 | images, layers, namespaces/cgroups |
| Kubernetes & Orchestration | `kubernetes` | 🔵 | pods/deployments/services, scheduling |
| Infrastructure as Code | `iac` | 🟡 | Terraform, declarative infra |
| CI/CD Pipelines (infra) | `cicd-infra` | 🟡 | build/deploy automation, GitOps |
| Observability & Monitoring | `observability-ops` | 🔵 | metrics/logs/traces, alerting |
| Site Reliability Engineering | `sre` | 🔵 | SLI/SLO/error budgets, toil |
| API Gateways & Service Mesh | `api-gateway-mesh` | 🟡 | gateway patterns, Istio/Envoy |
| Cost & Capacity Engineering | `cost-capacity` | ⚪ | rightsizing, autoscaling economics |
| Serverless & Edge | `serverless` | 🟡 | FaaS, cold starts, edge compute |

## Area 11 — Data Engineering & Big Data `data-engineering` 🔵

| Group | slug | Tier | Scope |
|---|---|---|---|
| Data Engineering Fundamentals | `de-fundamentals` | 🔵 | pipelines, OLTP vs OLAP, formats |
| Batch Processing & ETL | `batch-etl` | 🔵 | ETL/ELT, orchestration, idempotency |
| Stream Processing | `stream-processing` | 🔵 | event time, windowing, exactly-once |
| Data Warehousing & Lakes | `warehousing-lakes` | 🔵 | warehouse/lake/lakehouse, columnar |
| Analytics Data Modeling | `analytics-modeling` | 🟡 | star/snowflake, slowly-changing dims |
| Big Data Frameworks | `big-data-frameworks` | 🔵 | MapReduce, Spark, partitioning |
| Data Quality & Governance | `data-governance` | ⚪ | lineage, contracts, quality checks |

## Area 12 — AI & Machine Learning `ai-ml` 🔵

| Group | slug | Tier | Scope |
|---|---|---|---|
| ML Fundamentals | `ml-fundamentals` | 🔵 | train/test, bias-variance, metrics |
| Supervised Learning | `supervised-learning` | 🔵 | regression, trees, SVM, ensembles |
| Unsupervised Learning | `unsupervised-learning` | 🟡 | clustering, dimensionality reduction |
| Deep Learning | `deep-learning` | 🔵 | NNs, backprop, CNNs/RNNs, training |
| Natural Language Processing | `nlp` | 🔵 | embeddings, transformers, tasks |
| Computer Vision | `computer-vision` | 🟡 | detection/segmentation basics |
| LLMs & Generative AI | `llms` | 🔵 | architecture, prompting, RAG, fine-tuning |
| Applied AI / AI Engineering | `applied-ai` | 🔵 | building AI apps, agents, evals |
| MLOps | `mlops` | 🟡 | serving, monitoring, feature stores |
| Recommender Systems | `recommender-systems` | ⚪ | collaborative/content filtering |
| Reinforcement Learning | `reinforcement-learning` | ⚪ | MDPs, Q-learning, policy methods |
| ML System Design | `ml-system-design` | 🔵 | design a recommender/feed/fraud system |

## Area 13 — Security `security` 🔵

| Group | slug | Tier | Scope |
|---|---|---|---|
| Security Fundamentals | `security-fundamentals` | 🔵 | CIA triad, threat modeling, defense-in-depth |
| Cryptography | `cryptography` | 🔵 | symmetric/asymmetric, hashing, signatures |
| Application Security | `appsec` | 🔵 | OWASP Top 10, injection, XSS/CSRF |
| Authentication & Authorization | `authn-authz` | 🔵 | OAuth2/OIDC, JWT, sessions, RBAC |
| Network & Infra Security | `netsec` | 🟡 | firewalls, TLS, zero-trust |
| Cloud Security | `cloud-security` | 🟡 | IAM, secrets, shared responsibility |
| Secure Coding | `secure-coding` | 🟡 | input validation, safe defaults |

## Area 14 — Web & Frontend `web-frontend` 🟡

| Group | slug | Tier | Scope |
|---|---|---|---|
| Web Fundamentals | `web-fundamentals` | 🔵 | HTTP, browser, DOM, rendering path |
| HTML/CSS & Layout | `html-css` | 🟡 | box model, fl[ex/grid, responsive |
| JavaScript & TypeScript | `javascript` | 🔵 | event loop, closures, async, types |
| Frontend Frameworks | `frameworks` | 🟡 | component model, state, reactivity |
| Frontend System Design | `frontend-system-design` | 🔵 | design a large SPA, perf budgets |
| Browser Internals & Performance | `browser-performance` | 🟡 | reflow/repaint, Core Web Vitals |
| Accessibility | `accessibility` | ⚪ | ARIA, semantic HTML, WCAG |
| Client-Side Security | `web-security` | 🟡 | XSS/CSRF/CSP from the frontend |

## Area 15 — Mobile `mobile` 🟡

| Group | slug | Tier | Scope |
|---|---|---|---|
| Mobile Fundamentals | `mobile-fundamentals` | 🟡 | lifecycle, storage, networking, battery |
| Android Development | `android` | 🟡 | activities, Jetpack, Kotlin patterns |
| iOS Development | `ios` | 🟡 | UIKit/SwiftUI, memory, lifecycle |
| Cross-Platform | `cross-platform` | ⚪ | Flutter/React Native trade-offs |
| Mobile System Design | `mobile-system-design` | 🔵 | offline-first, sync, design a mobile client |

## Area 16 — CS Theory & Math `cs-theory-math` 🟡 (breadth — often prunable)

| Group | slug | Tier | Scope |
|---|---|---|---|
| Discrete Mathematics | `discrete-math` | 🟡 | logic, sets, graph theory, combinatorics |
| Probability & Statistics | `probability-stats` | 🟡 | distributions, Bayes, expectation |
| Linear Algebra for CS | `linear-algebra` | 🟡 | vectors/matrices, used in ML/graphics |
| Theory of Computation | `theory-of-computation` | ⚪ | automata, Turing machines, P/NP |
| Information Theory | `information-theory` | ⚪ | entropy, coding, compression |

## Area 17 — Interview Prep & Career `interview-prep` 🔵 (meta — overlaps others)

| Group | slug | Tier | Scope |
|---|---|---|---|
| Coding Interview Playbook | `coding-playbook` | 🔵 | end-to-end method, mindset, pitfalls |
| System Design Interview Playbook | `sd-interview-playbook` | 🔵 | overlaps Area 7 — pick one home |
| Behavioral Interview | `behavioral-interview` | 🔵 | overlaps Area 9 — pick one home |
| Take-Home & Pair Programming | `take-home` | ⚪ | approach, time-boxing |
| Negotiation & Offer | `negotiation` | ⚪ | leveling, comp, closing |

---

## Overlap flags (pick one home each)
- `caching` (A7) vs cache material in A5/A2
- `api-design` (A7) — keep in System Design, not a separate area
- `observability` (A7) vs `observability-ops` (A10) — dedupe or split HLD-view vs ops-view
- `sd-playbook` (A7) = `sd-interview-playbook` (A17); `behavioral` (A9) = `behavioral-interview` (A17); `coding-interview-strategy` (A1) ⊂ `coding-playbook` (A17)
- `design-patterns` sits in both A8 (OOD) and A9 (craft) — home in A8
- `web-security` (A14) / `netsec` (A13) / `network-security` (A4) — decide granularity

## Totals (draft): 17 Areas · ~140 Groups
Core-only (🟢) ≈ 9 areas. 🟢+🔵 ≈ everything commonly interviewed.

## How to prune
1. **Cut whole Areas** you don't want (e.g. drop 14/15/16/17).
2. Within kept Areas, **cut Groups** — quickest: "keep 🟢🔵, drop 🟡⚪" per area, or name specific slugs.
3. Resolve the overlap flags.
4. Approved map → I write per-area Briefs, then authoring agents generate topics/slides/mcqs/interview per group.
