# Area: System Design — LLD & HLD (system-design)

Merged Study Area covering **both altitudes of design**: the classes inside a service (LLD) and the services inside a system (HLD), from beginner to expert, for interviews and for the job. Assembled from the former `system-design` (HLD) and `object-oriented-design` (LLD) briefs plus new Foundations / practice / expert material.

Group order below **is** the learning order and drives ordering in the app (`tools/regen_v3.py` reads the `## Group:` sequence). Each topic lists a kebab slug (unique across the area), title, level, a one-line scope, and its slide outline (concept / diagram / code / compare / pitfall / interview). MCQs and interview questions attach at topic level and are not enumerated here.

---

# Phase A — Foundations

## Group: System Design Fundamentals (sd-fundamentals)

*scalability, availability, trade-offs*

### Topic: Scalability Fundamentals (scalability-fundamentals, beginner)
Vertical vs horizontal scaling, statelessness, and the scale cube as the base vocabulary for every design discussion.
- What "scale" actually means in an interview (concept)
- Vertical scaling: how far it gets you, and where it breaks (concept)
- Horizontal scaling: the shift to many small nodes (concept)
- Diagram: scale-up vs scale-out (diagram)
- Statelessness: why it's the precondition for horizontal scaling (concept)
- Sharing state without sharing memory: sessions, sticky routing, external state stores (concept)
- The scale cube: x/y/z axes of scaling (AKF) (diagram)
- Compare: scaling the app tier vs scaling the data tier (compare)
- Pitfall: "just add more servers" without removing the stateful bottleneck (pitfall)
- Interview: "How would you scale this service to 10x traffic?" (interview)

### Topic: Latency vs Throughput (latency-vs-throughput, beginner)
Precise vocabulary for speed and capacity — percentiles, tail latency, and Little's Law — used to reason about every design decision.
- Latency vs throughput: two different axes of "fast" (concept)
- Percentiles: why averages lie (p50 vs p99 vs p999) (concept)
- Diagram: latency distribution and the long tail (diagram)
- Tail latency amplification: why one slow dependency ruins the whole request (concept)
- Little's Law: relating concurrency, latency, and throughput (concept)
- Compare: optimizing for latency vs optimizing for throughput (compare)
- Pitfall: quoting average latency as your SLA (pitfall)
- Interview: "Your p99 latency spiked — how do you approach it?" (interview)

### Topic: Availability & Reliability (availability-and-reliability, beginner)
Quantifying uptime, eliminating single points of failure, and the difference between fault tolerance and disaster recovery.
- Availability as a number: the "nines" and what each nine costs (concept)
- Reliability vs availability: not the same thing (concept)
- Single points of failure: finding them in a diagram (diagram)
- Redundancy patterns: active-active vs active-passive (compare)
- Fault tolerance vs graceful degradation vs disaster recovery (concept)
- Failover mechanics: detection, health checks, promotion (concept)
- Redundancy has a cost: consistency and money trade-offs (compare)
- Pitfall: redundant components that share a hidden dependency (pitfall)
- Interview: "Design for 99.99% availability — what changes?" (interview)

### Topic: CAP Theorem & PACELC (cap-theorem-and-pacelc, intermediate)
The CAP theorem's real meaning under partition, why "CP vs AP" oversimplifies, and the PACELC extension for the no-partition case.
- CAP theorem stated precisely: what C, A, P actually mean here (concept)
- Why you can't cheat CAP: an intuition/proof sketch (concept)
- Diagram: a network partition forcing the C-vs-A choice (diagram)
- CP systems vs AP systems: real examples (compare)
- The most common CAP misconception: "2 of 3, pick any two" (pitfall)
- PACELC: what happens when there's no partition (concept)
- Compare: PACELC classification of popular databases (compare)
- Interview: "Where does your design sit on CAP/PACELC, and why?" (interview)

### Topic: Trade-Offs & Non-Functional Requirements (trade-offs-and-nfrs, intermediate)
Eliciting non-functional requirements and structuring the trade-off conversation that system design interviews actually reward.
- Functional vs non-functional requirements: what to ask first (concept)
- The NFR checklist: scale, latency, availability, consistency, cost (concept)
- Reading between the lines: what the interviewer is really scoring (concept)
- Trade-off framing: "it depends" done well vs done badly (compare)
- Diagram: a requirements-to-decisions flow (diagram)
- Pitfall: designing before requirements are pinned down (pitfall)
- Pitfall: listing NFRs but never returning to them in the design (pitfall)
- Interview: "Design a system for X" — the first five minutes (interview)

### Topic: Building Blocks Overview (building-blocks-overview, beginner)
A map of the standard toolkit — load balancer, cache, database, queue, CDN — and which problem each one solves, before going deep on any single piece.
- The standard building blocks, end to end (diagram)
- What each block solves: LB, app tier, cache, DB, queue, CDN (concept)
- How a request actually flows through all of them (diagram)
- Compare: when you need each block vs when it's overkill for the scale (compare)
- Reading a system design diagram like an interviewer does (concept)
- Pitfall: reaching for every block regardless of the requirements (pitfall)
- Where to go deep: pointers to the dedicated groups (concept)

---

<!-- expert-tier additions (sd-fundamentals) -->

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

---

# Phase B — Low-Level Design: concepts

## Group: OOP Fundamentals (oop-fundamentals)

### Topic: Objects and Classes (objects-and-classes, beginner)
The substrate under the four pillars: what a class/object actually is, identity vs equality, and where state lives.
- What a class actually is: a blueprint, not a template you copy (concept)
- Objects: state + identity + behavior together (concept)
- Constructors and initialization order (concept)
- `this`/`self`: how a method finds "its" object (concept)
- Diagram: object references vs values in memory (diagram)
- Equality vs identity: `==` vs `.equals()`, value vs reference comparison (compare)
- Static vs instance members: what belongs to the class vs the object (concept)
- Code: a minimal class showing state, constructor, and a method (code)
- Pitfall: mutable default/static state accidentally shared across instances (pitfall)

### Topic: Encapsulation (encapsulation, beginner)
Bundling state with the behavior that protects it, and why that's more than "add getters and setters."
- Encapsulation defined: bundling state with the behavior that protects it (concept)
- Why public fields let callers break an object's invariants (concept)
- Access modifiers: public/private/protected/package — what each actually buys you (concept)
- Pitfall: getters/setters on every field isn't automatically encapsulation (pitfall)
- Diagram: an object as a capsule — what's exposed vs hidden (diagram)
- Invariants: rules an object must never violate, enforced in one place (concept)
- Code: encapsulating a `BankAccount` balance so it can never go negative (code)
- Compare: encapsulation vs abstraction — hiding implementation vs hiding complexity (compare) — cross-link: abstraction
- Pitfall: leaking an internal mutable collection through a getter (pitfall)

### Topic: Abstraction (abstraction, beginner)
Exposing what an object does while hiding how, and the levels of abstraction that stack up to a system.
- Abstraction: exposing what an object does, hiding how (concept)
- Levels of abstraction: a method name, an interface, a subsystem (concept)
- Abstract classes and interfaces as abstraction mechanisms (concept)
- Diagram: layers of abstraction in a real system (ORM → SQL → disk) (diagram)
- Compare: abstraction vs encapsulation, the interview-standard distinction (compare)
- Code: programming to an interface, not an implementation (code)
- Pitfall: over-abstracting — an interface with one implementation and no reason to exist (pitfall)
- Why abstraction is what lets code change without ripple effects (concept)
- Pitfall: leaky abstractions — when the hidden detail leaks through anyway (pitfall)

### Topic: Inheritance (inheritance, beginner)
The is-a relationship, method resolution, and where inheritance quietly turns fragile.
- Inheritance: the is-a relationship and code reuse through a base class (concept)
- Method overriding vs hiding/shadowing (concept)
- `super` calls: extending vs replacing base behavior (concept)
- Diagram: a class hierarchy and which method resolves where (diagram)
- Single vs multiple inheritance, and why many languages ban the latter (concept)
- Diagram: the diamond problem, worked through (diagram)
- Constructors in a hierarchy: initialization order base-to-derived (concept)
- Code: overriding a method and calling `super` for shared setup (code)
- Pitfall: the fragile base class problem — a base class change silently breaks subclasses (pitfall)

### Topic: Polymorphism (polymorphism, intermediate)
One interface, many shapes — and the runtime mechanics behind it.
- Polymorphism defined: one interface, many shapes (concept)
- Compile-time (overload) vs runtime (override) polymorphism (compare)
- How dynamic dispatch actually works: vtables/method tables (concept)
- Diagram: a vtable lookup resolving a call at runtime (diagram)
- Parametric polymorphism/generics as a third kind (concept)
- Code: a polymorphic `Shape.area()` call resolved at runtime (code)
- Pitfall: overload-resolution surprises — the "wrong" overload picked at compile time (pitfall)
- Pitfall: calling overridable methods from a constructor (pitfall)
- Why polymorphism is what makes the Open/Closed Principle possible (concept) — cross-link: ocp-open-closed

### Topic: Composition vs Inheritance (composition-vs-inheritance, intermediate)
Has-a vs is-a, and why "favor composition" became standard advice.
- Has-a vs is-a: the test for which relationship you actually have (concept)
- "Favor composition over inheritance" — where that advice comes from (concept)
- Delegation: forwarding calls to a composed object (concept)
- Diagram: the same feature modeled via inheritance vs composition, side by side (diagram)
- Compare: inheritance vs composition — reuse, coupling, runtime flexibility (compare)
- Code: refactoring an inheritance hierarchy into a composed strategy (code) — cross-link: strategy-pattern
- Pitfall: deep inheritance chains that are impossible to reason about (pitfall)
- Where the Strategy pattern replaces a hierarchy of behavior subclasses (concept) — cross-link: strategy-pattern

### Topic: Interfaces vs Abstract Classes (interfaces-vs-abstract-classes, intermediate)
Contract-only vs partial implementation, and how modern languages blurred the line.
- Interface vs abstract class: contract-only vs partial implementation (concept)
- Multiple interface implementation vs single-class inheritance (concept)
- Default/static methods on interfaces — how modern languages blurred the line (concept)
- Diagram: interface vs abstract class inside the same hierarchy (diagram)
- Compare: when to use an interface vs an abstract class (compare)
- Code: the same small design done both ways (code)
- Pitfall: a fat interface that forces classes to implement methods they don't need (pitfall) — cross-link: isp-interface-segregation
- Marker interfaces and their modern replacements (annotations/attributes) (concept)

---

## Group: SOLID & Design Principles (design-principles)

### Topic: Single Responsibility Principle (srp-single-responsibility, beginner)
One reason to change, and how to actually apply that test to a class.
- SRP defined: one reason to change, not "one method" (concept)
- The "reason to change" test — how to actually apply it (concept)
- Diagram: a God Class doing 3 jobs vs split into 3 classes (diagram) — cross-link: common-design-anti-patterns
- Code: a class mixing persistence + business logic + formatting, then split (code)
- Compare: SRP at class level vs method level vs module level (compare)
- Pitfall: over-splitting into many trivial classes ("SRP-itis") (pitfall)
- How SRP interacts with cohesion — high cohesion means few reasons to change (concept) — cross-link: coupling-and-cohesion
- Interview framing: "tell me about a class you refactored for SRP" (concept)

### Topic: Open/Closed Principle (ocp-open-closed, beginner)
Open for extension, closed for modification — and how polymorphism makes that possible.
- OCP defined: open for extension, closed for modification (concept)
- Why "closed for modification" protects already-tested code (concept)
- Diagram: adding a new `Shape` without touching existing `area()` logic (diagram)
- Code: a switch-statement violation refactored to polymorphism/strategy (code) — cross-link: strategy-pattern
- How OCP leans on abstraction and polymorphism to work (concept) — cross-link: polymorphism
- Compare: inheritance-based vs plugin/strategy-based extension (compare)
- Pitfall: speculative generality — abstracting for extension points nobody needs (pitfall)
- Where OCP shows up in framework design: hooks, plugins, middleware (concept)

### Topic: Liskov Substitution Principle (lsp-liskov-substitution, intermediate)
Subtypes must be substitutable for their base type — the classic square/rectangle trap.
- LSP defined: subtypes must be substitutable for their base type (concept)
- The classic violation: `Square extends Rectangle` (concept)
- Diagram: a client that breaks when a subtype changes behavior (diagram)
- Behavioral subtyping: preconditions can't strengthen, postconditions can't weaken (concept)
- Code: an LSP violation via a method that throws where the base didn't (code)
- Pitfall: "is-a" in English doesn't guarantee "is-a" in LSP terms (pitfall)
- Compare: an LSP violation vs a legitimate narrowing override (compare)
- How LSP violations surface in code review: type-checks, `instanceof` chains (concept)

### Topic: Interface Segregation Principle (isp-interface-segregation, intermediate)
Many small, client-specific interfaces beat one fat interface.
- ISP defined: many small client-specific interfaces over one fat interface (concept)
- The "fat interface" smell: forced no-op/throwing implementations (concept)
- Diagram: one bloated interface split into role interfaces (diagram)
- Code: a `Worker` interface forcing a `Robot` to implement `eat()` (code)
- Compare: ISP vs SRP — segregating interfaces vs segregating responsibilities (compare)
- Pitfall: interface explosion — too many micro-interfaces to track (pitfall)
- How ISP guides API design for consumers you don't control (concept)

### Topic: Dependency Inversion Principle (dip-dependency-inversion, intermediate)
Depend on abstractions, not concretions — and the direction that actually "inverts."
- DIP defined: depend on abstractions, not concretions — which direction "inverts" (concept)
- High-level vs low-level modules, and why the naive dependency runs backwards (concept)
- Diagram: dependency arrows before and after inversion (diagram)
- Code: a service hard-wired to a concrete class, then inverted via an interface (code)
- Dependency Injection as the mechanism that implements DIP (concept)
- Compare: constructor injection vs setter injection vs service locator (compare)
- Pitfall: confusing DIP (the principle) with DI (one technique for achieving it) (pitfall)
- Where an IoC container fits into this picture (concept)

### Topic: Coupling and Cohesion (coupling-and-cohesion, beginner)
The two forces every other principle in this group is ultimately fighting for.
- Coupling and cohesion defined, and why you want low/high respectively (concept)
- Types of coupling: content, common, control, data — worst to best (concept)
- Types of cohesion: coincidental to functional — worst to best (concept)
- Diagram: two modules, tightly coupled vs loosely coupled (diagram)
- Code: reducing coupling by introducing an interface boundary (code)
- Compare: coupling/cohesion vs SOLID — how the principles reinforce each other (compare)
- Pitfall: chasing zero coupling and losing all cohesion — over-decoupled indirection (pitfall)
- Measuring it in practice: code-review signals that hint at low cohesion (concept)

### Topic: DRY, YAGNI, and KISS (dry-yagni-kiss, beginner)
Three simplicity principles that sometimes pull against each other and against SOLID.
- DRY: don't repeat yourself — but repeat *knowledge*, not just text (concept)
- Pitfall: the wrong-abstraction trap — DRY-ing up coincidentally similar code too early (pitfall)
- YAGNI: you aren't gonna need it — fighting speculative features (concept)
- KISS: simplicity as a design goal, and where it tensions with SOLID (concept)
- Diagram: duplication vs premature abstraction, the two failure modes DRY sits between (diagram)
- Code: a helper extracted too early, then two callers diverge and fight the abstraction (code)
- Compare: DRY vs YAGNI vs KISS — when they pull in different directions (compare)
- Interview framing: "when have you deliberately duplicated code?" (concept)

---

<!-- expert-tier additions (design-principles) -->

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

## Group: Creational Patterns (creational-patterns)

### Topic: Design Patterns: What, Why, and the GoF Categories (design-patterns-intro, beginner)
The front door to all pattern content: what a pattern is, the three GoF categories, and the risk of overusing them.
- What a design pattern actually is: a named, reusable solution shape, not code (concept)
- The GoF three categories: creational, structural, behavioral — what each answers (concept)
- Diagram: the GoF patterns grouped by category (diagram)
- Why patterns exist: shared vocabulary for design conversations (concept)
- Pitfall: pattern-itis — forcing a named pattern where plain code would do (pitfall)
- Compare: pattern vs idiom vs framework — where the boundaries are (compare)
- How interviewers actually probe patterns: "have you used X, and why," not "recite GoF" (concept)
- Code: recognizing an unnamed pattern already sitting in a codebase (code)

### Topic: Factory Method and Abstract Factory (factory-method-and-abstract-factory, intermediate)
Delegating object creation so callers stop depending on concrete classes.
- The problem: `new` couples you to a concrete class (concept)
- Factory Method: delegate construction to a subclass-overridable method (concept)
- Diagram: Factory Method's creator/product hierarchy (diagram)
- Abstract Factory: a factory of related factories — families of products (concept)
- Diagram: Abstract Factory producing a matched UI theme (buttons + checkboxes) (diagram)
- Compare: Factory Method vs Abstract Factory vs a plain constructor (compare)
- Code: swapping a concrete factory to retarget an entire product family (code)
- Pitfall: reaching for Abstract Factory when there's only ever one product family (pitfall)
- Where this shows up in real libraries: connection/driver factories (concept)

### Topic: Builder Pattern (builder-pattern, intermediate)
Constructing complex, valid objects step by step instead of via telescoping constructors.
- The problem: telescoping constructors with many optional parameters (concept)
- Builder: construct step by step, validate at the end (concept)
- Diagram: Builder's director/builder/product roles (diagram)
- Fluent builders vs a separate director object (concept)
- Code: building an immutable `HttpRequest` via chained builder calls (code)
- Compare: Builder vs constructor overloading vs named-parameter languages (compare)
- Pitfall: a builder that allows building an invalid or half-configured object (pitfall)
- Where Builder pairs with immutability for thread-safe objects (concept) — cross-link: immutability-as-a-design-tool

### Topic: Singleton Pattern (singleton-pattern, intermediate)
Exactly one instance, globally accessible — and why that guarantee is harder (and more contested) than it looks.
- Singleton: exactly one instance, globally accessible — why that's a big claim (concept)
- Lazy vs eager initialization (concept)
- Diagram: Singleton access path from multiple callers (diagram)
- Thread-safe Singleton: double-checked locking, static holder, enum singleton (concept) — cross-link: synchronization-techniques-in-oo-design
- Code: a correct thread-safe lazy Singleton (code)
- Pitfall: Singleton as a disguised global variable — hidden dependencies, hard to test (pitfall)
- Compare: Singleton vs a dependency-injected, framework-scoped single instance (compare)
- Interview framing: "why do some consider Singleton an anti-pattern?" (concept) — cross-link: common-design-anti-patterns

### Topic: Prototype Pattern (prototype-pattern, intermediate)
Cloning an existing object instead of building one from scratch.
- Prototype: cloning an existing object instead of building from scratch (concept)
- Shallow copy vs deep copy — where clone bugs actually come from (concept)
- Diagram: shallow vs deep clone of an object graph (diagram)
- Code: implementing a correct deep-copy clone (code)
- When Prototype beats a factory: expensive construction, runtime-configured templates (concept)
- Pitfall: a "deep" clone that misses a nested mutable field (pitfall)
- Compare: Prototype vs Builder vs Factory Method for object creation (compare)

---

## Group: Structural Patterns (structural-patterns)

### Topic: Adapter Pattern (adapter-pattern, intermediate)
Making two incompatible interfaces work together without changing either.
- The problem: two incompatible interfaces that need to work together (concept)
- Adapter: wrap one interface to satisfy another, without changing either (concept)
- Diagram: an Adapter sitting between client and adaptee (diagram)
- Compare: object adapter (composition) vs class adapter (inheritance) (compare)
- Code: adapting a legacy `XmlLogger` to a new `Logger` interface (code)
- Pitfall: an adapter that leaks the adaptee's exceptions/semantics untranslated (pitfall)
- Where Adapter shows up: third-party SDK wrappers, legacy migration seams (concept)
- Compare: Adapter vs Facade — translating one interface vs simplifying many (compare) — cross-link: facade-pattern

### Topic: Decorator Pattern (decorator-pattern, intermediate)
Adding responsibilities to an object at runtime without a subclass explosion.
- The problem: adding responsibilities without a subclass explosion (concept)
- Decorator: wrap an object, add behavior, preserve the interface (concept)
- Diagram: stacked decorators around a core component (diagram)
- Code: layering `CompressedStream` and `EncryptedStream` around a base `Stream` (code)
- Compare: Decorator vs inheritance for adding behavior (compare) — cross-link: composition-vs-inheritance
- Compare: Decorator vs Proxy — both wrap, but for different reasons (compare) — cross-link: proxy-pattern
- Pitfall: decorator order changing behavior unexpectedly (pitfall)
- Where real libraries use this: I/O stream wrappers, function decorators (concept)

### Topic: Facade Pattern (facade-pattern, beginner)
One simplified entry point over a subsystem with too many moving parts.
- The problem: a subsystem with many moving parts and a painful API (concept)
- Facade: one simplified entry point over a complex subsystem (concept)
- Diagram: a Facade hiding several subsystem classes (diagram)
- Code: a `CheckoutFacade` hiding inventory/payment/shipping calls (code)
- Pitfall: Facade doesn't add behavior — don't confuse it with a manager/service class (pitfall)
- Compare: Facade vs Adapter vs Mediator (compare)
- Where Facade shows up: SDKs, internal platform APIs (concept)

### Topic: Proxy Pattern (proxy-pattern, intermediate)
A stand-in that controls access to a real object — lazily, securely, or remotely.
- Proxy: a stand-in that controls access to a real object (concept)
- Virtual proxy (lazy loading), protection proxy (access control), remote proxy (network) (concept)
- Diagram: client → proxy → real subject, same interface both sides (diagram)
- Code: a caching proxy in front of an expensive `ImageLoader` (code)
- Compare: Proxy vs Decorator — controlling access vs adding behavior (compare)
- Pitfall: a proxy that silently changes semantics the client depends on, e.g. hidden latency (pitfall)
- Where this shows up: lazy-loaded ORM associations, RPC stubs (concept)

### Topic: Composite Pattern (composite-pattern, intermediate)
Treating a single object and a group of objects through the same interface.
- The problem: treating a single object and a group of objects the same way (concept)
- Composite: a tree of components sharing one interface (leaf + composite) (concept)
- Diagram: a file-system tree modeled as Composite (diagram)
- Code: computing total size over a file/folder tree recursively (code)
- Compare: Composite vs a flat collection with type-checking (compare)
- Pitfall: leaf nodes forced to implement child-management methods they don't support (pitfall) — cross-link: isp-interface-segregation
- Where Composite shows up: UI component trees, org charts, menu systems (concept)

### Topic: Bridge and Flyweight Patterns (bridge-and-flyweight, advanced)
Two less-common but still-asked structural patterns: decoupling abstraction from implementation, and sharing state to cut memory.
- Bridge: decoupling an abstraction from its implementation so both vary independently (concept)
- Diagram: Bridge separating a `Shape` abstraction from a `Renderer` implementation (diagram)
- Code: a shape hierarchy that renders via a swappable rendering backend (code)
- Flyweight: sharing immutable state across many objects to cut memory (concept)
- Diagram: shared intrinsic state vs per-object extrinsic state (diagram)
- Code: a text editor sharing glyph objects across millions of characters (code)
- Compare: Bridge vs Adapter — designed upfront vs retrofitted (compare)
- Pitfall: Flyweight sharing mutable state by mistake, causing cross-talk bugs (pitfall)

---

## Group: Behavioral Patterns (behavioral-patterns)

### Topic: Strategy Pattern (strategy-pattern, intermediate)
Encapsulating interchangeable algorithms behind one interface so they vary independently of the client.
- The problem: an algorithm that needs to vary independently of the client using it (concept)
- Strategy: encapsulate interchangeable algorithms behind one interface (concept)
- Diagram: a context holding a swappable strategy object (diagram)
- Code: swapping sort/pricing/route strategies at runtime (code)
- Compare: Strategy vs a big if/else or switch on type (compare)
- Compare: Strategy vs State — same shape, different intent (compare) — cross-link: state-pattern
- Pitfall: strategy explosion — a class per tiny variation with no real behavior difference (pitfall)
- Where Strategy replaces subclassing for behavior variation (concept) — cross-link: composition-vs-inheritance

### Topic: Observer Pattern (observer-pattern, intermediate)
Notifying many dependents when one object's state changes, without hard-wiring them together.
- The problem: notifying many dependents when one object's state changes (concept)
- Observer: a subject maintains a list of observers and pushes/pulls updates (concept)
- Diagram: subject fan-out to multiple observers (diagram)
- Code: a stock-price subject notifying multiple display observers (code)
- Compare: push vs pull observer models (compare)
- Pitfall: memory leaks from observers that never unsubscribe (pitfall)
- Pitfall: notification-order dependencies — an observer that mutates the subject mid-notify (pitfall)
- Where this shows up: pub/sub, UI event listeners, reactive streams (concept)

### Topic: State Pattern (state-pattern, intermediate)
Letting an object's behavior change with its internal state, without a wall of conditionals.
- The problem: behavior that changes with internal state, without a wall of conditionals (concept)
- State: each state is an object; the context delegates to its current state (concept)
- Diagram: an order's state machine (placed → shipped → delivered) as State objects (diagram)
- Code: a `TrafficLight`/`Order` implemented with State instead of enum + switch (code)
- Compare: State pattern vs a plain enum + switch — when each wins (compare)
- Compare: State vs Strategy — who changes the current behavior (compare) — cross-link: strategy-pattern
- Pitfall: state explosion for a machine with many transitions (pitfall)
- Where this shows up: workflow engines, game character states (concept)

### Topic: Command Pattern (command-pattern, intermediate)
Turning a request into an object so it can be queued, logged, or undone.
- The problem: decoupling "what to do" from "when/who triggers it" (concept)
- Command: encapsulate a request as an object with `execute()` (concept)
- Diagram: invoker → command → receiver, decoupled (diagram)
- Code: an undoable `Command` with `execute()`/`undo()` for a text editor (code)
- Undo/redo stacks built from Command history (concept)
- Compare: Command vs Strategy — an action-plus-receiver vs an algorithm (compare)
- Pitfall: commands holding stale receiver state, causing wrong undo behavior (pitfall)
- Where this shows up: job queues, macro recording, GUI actions (concept)

### Topic: Template Method Pattern (template-method-pattern, intermediate)
Sharing an algorithm's skeleton in a base class while letting subclasses vary the steps.
- The problem: several algorithms share the same skeleton but differ in steps (concept)
- Template Method: define the skeleton in a base class, defer steps to subclasses (concept)
- Diagram: a base-class algorithm with hook methods overridden by subclasses (diagram)
- Code: a `DataImporter` template with `parse()`/`validate()` steps overridden per format (code)
- The Hollywood Principle: "don't call us, we'll call you" (concept)
- Compare: Template Method vs Strategy — inheritance-based vs composition-based step variation (compare)
- Pitfall: a template so rigid a new subclass ends up overriding almost everything (pitfall)

### Topic: Iterator Pattern (iterator-pattern, beginner)
Traversing a collection uniformly without exposing how it's built.
- The problem: traversing a collection without exposing its internal structure (concept)
- Iterator: a uniform `hasNext()`/`next()` contract over any collection (concept)
- Diagram: an iterator tracking traversal position separately from the collection (diagram)
- Code: implementing a custom iterator over a tree/graph structure (code)
- Compare: external vs internal iterators — for-each vs callback-based (compare)
- Pitfall: mutating a collection while iterating over it (pitfall)
- Where this shows up: language-level for-each, generators/lazy sequences (concept)

### Topic: Chain of Responsibility Pattern (chain-of-responsibility-pattern, intermediate)
Passing a request along a chain of handlers until one handles it.
- The problem: a request that might be handled by one of several possible handlers (concept)
- Chain of Responsibility: pass the request along a chain until someone handles it (concept)
- Diagram: a request traveling handler to handler (diagram)
- Code: a middleware/validation chain — auth → rate-limit → business logic (code)
- Compare: Chain of Responsibility vs a single handler with if/else branches (compare)
- Pitfall: a chain with no handler at the end, silently swallowing the request (pitfall)
- Where this shows up: HTTP middleware, exception-handler chains, logging levels (concept) — cross-link: logging-framework

### Topic: Mediator and Memento Patterns (mediator-and-memento, advanced)
Two lower-frequency-but-real behavioral patterns: centralizing object communication, and snapshotting state for undo.
- Mediator: centralize how objects talk to each other instead of a mesh of references (concept)
- Diagram: many-to-many object references replaced by a single mediator hub (diagram)
- Code: a chat-room `Mediator` routing messages between `User` objects (code)
- Pitfall: the mediator becoming a god object that knows too much (pitfall) — cross-link: common-design-anti-patterns
- Memento: capture and restore an object's internal state without breaking encapsulation (concept)
- Diagram: originator/memento/caretaker roles (diagram)
- Code: undo/redo for a text editor using Memento snapshots (code)
- Compare: Memento vs Command-based undo — snapshotting state vs replaying inverse actions (compare) — cross-link: command-pattern

---

<!-- expert-tier additions (behavioral-patterns) -->

### Topic: Visitor Pattern (visitor-pattern, advanced)
Adding a new operation across an entire object hierarchy without modifying the hierarchy itself, at the cost of the classes knowing about the visitor.
- The problem Visitor solves: adding a new operation across an object hierarchy without touching each class (concept)
- Double dispatch: how `accept`/`visit` picks the right method for both the element and the operation (concept)
- Diagram: a visitor traversing a hierarchy, method resolution shown at each node (diagram)
- Code: implementing a `Visitor` over an AST or a document object tree (code)
- Compare: Visitor vs adding a method to every class — when the pattern earns its complexity (compare)
- Pitfall: Visitor breaks encapsulation by exposing internal state to the visitor (pitfall)
- Pitfall: adding a new element type means changing every visitor — the trade-off Visitor makes (pitfall)
- Interview: "When would you reach for Visitor instead of just adding a method to each class?" (interview)

---

## Group: UML & Modeling (uml)

### Topic: UML Class Diagrams (uml-class-diagrams, beginner)
The notation interviewers expect on a whiteboard: class boxes and the relationships between them.
- Why interviewers want a diagram, not just prose (concept)
- Class box anatomy: name / attributes / methods, visibility markers (concept)
- Diagram: a fully annotated UML class box (diagram)
- Association vs aggregation vs composition — the diamond notation and lifecycle implications (concept)
- Diagram: aggregation vs composition drawn side by side (Car–Engine vs Team–Player) (diagram)
- Inheritance and realization (interface implementation) arrows (concept)
- Multiplicities: reading `1`, `0..*`, `1..*` correctly (concept)
- Code: translating a small class hierarchy into its UML diagram (code)
- Pitfall: confusing aggregation and composition when the lifecycle question is asked (pitfall)

### Topic: UML Sequence and Other Diagrams (uml-sequence-and-other-diagrams, beginner)
Showing behavior over time, and when a second diagram type is actually worth drawing.
- Sequence diagrams: lifelines, activation bars, messages, in interview shorthand (concept)
- Diagram: a sequence diagram for "place an order" across three objects (diagram)
- Sync vs async messages, and return messages (concept)
- Diagram: a brief activity diagram for a decision-heavy flow (diagram)
- When a sequence diagram is worth drawing vs when it's overkill (concept)
- Compare: class diagram (structure) vs sequence diagram (behavior over time) — which to draw first (compare)
- Pitfall: a sequence diagram so detailed it eats the whole interview clock (pitfall)

### Topic: Whiteboarding LLD Diagrams in Interviews (whiteboarding-lld-diagrams, intermediate)
The practical, time-boxed version of UML that actually gets used in a live interview.
- What interviewers actually expect: legible shorthand, not textbook-perfect UML (concept)
- A practical shorthand: boxes, arrows, and the 3 relationship types you actually need (concept)
- Diagram: a real interview-paced whiteboard sketch for a parking lot's core classes (diagram) — cross-link: parking-lot
- Sequencing the interview: when to sketch classes vs when to talk (concept)
- Pitfall: over-formatting the diagram and running out of time to code (pitfall)
- Talking while drawing: narrating decisions as you sketch (concept)

---

<!-- expert-tier additions (uml) -->

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

## Group: Anti-Patterns & Code Smells (anti-patterns)

### Topic: Common Code Smells (common-code-smells, beginner)
Local symptoms in code that predict future pain, catalogued the way refactoring literature does.
- What a code smell is: not a bug, a signal something will hurt later (concept)
- Long method / long parameter list — why they correlate with bugs (concept)
- Large Class (God Class) as a smell, distinct from the God Object anti-pattern (concept) — cross-link: common-design-anti-patterns
- Duplicate code and the shotgun-surgery smell it causes later (concept)
- Diagram: shotgun surgery — one change rippling across many files (diagram)
- Feature envy: a method more interested in another class's data than its own (concept)
- Primitive obsession and data clumps — when a group of primitives should be a type (concept)
- Code: refactoring a data clump (`street, city, zip` params) into an `Address` value object (code)
- Pitfall: smell-hunting as an excuse for premature refactoring with no test coverage (pitfall)

### Topic: Common Design Anti-Patterns (common-design-anti-patterns, intermediate)
Structural, architecture-level bad practices — bigger than a single smelly method.
- God Object: one class that knows/does too much, and why it accretes (concept)
- Diagram: a God Object with dependencies fanning out to half the codebase (diagram)
- Tight coupling: symptoms — can't change one class without touching five others (concept)
- Spaghetti code and the missing-architecture smell (concept)
- Magic numbers/strings and why they rot maintainability (concept)
- Code: a God Object decomposed into cohesive collaborators (code)
- Compare: anti-pattern vs code smell — structural/architectural vs local (compare)
- Pitfall: mistaking "big class" for "necessarily bad" — some coordinators are legitimately large (pitfall)
- Interview framing: "tell me about the messiest code you've worked in" (concept)

### Topic: Anemic vs Rich Domain Models (anemic-vs-rich-domain-models, intermediate)
Where the business logic should actually live — on the entity, or in a service around it.
- Anemic domain model: data classes with all logic pulled into service classes (concept)
- Why anemic models are still an anti-pattern even though they "work" (concept)
- Diagram: anemic model (services + data bags) vs rich model (behavior on the object) (diagram)
- Code: moving a validation/business rule from a service into the entity it belongs to (code)
- Compare: rich domain model vs anemic — testability, encapsulation, discoverability (compare)
- Pitfall: over-correcting into a "rich" model that violates SRP by doing too much (pitfall) — cross-link: srp-single-responsibility
- Where this debate shows up in interviews: DDD-flavored LLD questions (concept)

### Topic: Refactoring to Fix Smells (refactoring-to-fix-smells, intermediate)
The standard toolkit for turning a smelly method into clean ones, safely.
- Refactoring: behavior-preserving structural change, and why tests are the safety net (concept)
- Extract Method / Extract Class — the two workhorse refactors (concept)
- Replace Conditional with Polymorphism — killing a type-check switch (concept) — cross-link: ocp-open-closed
- Diagram: before/after of replacing a conditional with a Strategy object (diagram)
- Introduce Parameter Object — fixing a long parameter list (concept)
- Code: a step-by-step refactor of a smelly method into three clean ones (code)
- Pitfall: refactoring without characterization tests first, silently changing behavior (pitfall)
- How to talk through a live refactor in an interview (concept)

---

<!-- expert-tier additions (anti-patterns) -->

### Topic: Over-Engineering and Pattern-Happy Design (over-engineering-and-pattern-happy-design, expert)
Recognizing when a design applies patterns and abstraction for their own sake, and how to call it out constructively in review.
- Over-engineering defined: solving a problem you don't have yet, at a real cost to today's readers (concept)
- Symptoms: a factory that produces one implementation, a strategy with one strategy, an interface with one caller (concept) — cross-link: abstraction
- Diagram: a simple requirement buried under four layers of indirection (diagram)
- Why pattern-happy design feels like good engineering — and why that instinct misleads (concept)
- Compare: appropriate abstraction vs speculative generality — how to tell them apart in review (compare)
- Pitfall: justifying complexity with "we might need this later" without a concrete near-term driver (pitfall) — cross-link: dry-yagni-kiss
- Calling it out in code review: questions that surface unnecessary complexity without being adversarial (concept)
- Interview: "An interviewer shows you an over-engineered design and asks what you'd simplify. How do you respond?" (interview)

---

## Group: Concurrency in OO Design (oo-concurrency)

### Topic: Thread-Safety Fundamentals for Objects (thread-safety-fundamentals-for-objects, intermediate)
What "thread-safe class" precisely means, and where naive designs break.
- What "thread-safe" means for a class, precisely (concept)
- Race conditions: two threads mutating the same field without ordering (concept)
- Diagram: an interleaving that corrupts a counter's state (diagram)
- Critical sections: the code that must run one thread at a time (concept)
- Code: an unsafe `Counter.increment()` and the interleaving that breaks it (code)
- Compare: thread-safe vs "safe only if the caller synchronizes externally" (compare)
- Pitfall: assuming a class is thread-safe because each method looks atomic on its own (pitfall)
- Interview framing: "design a thread-safe X" — what's really being checked (concept)

### Topic: Immutability as a Design Tool (immutability-as-a-design-tool, intermediate)
Why an object that can't change is automatically safe to share across threads.
- Immutable objects: state fixed at construction, never changes after (concept)
- Why immutable objects are automatically thread-safe — no state to race on (concept)
- Diagram: an immutable object shared across threads with zero locking (diagram)
- Code: designing an immutable `Money`/`Point` class correctly — final fields, no setters, defensive copies (code)
- Pitfall: defensive-copying gaps that make a "mostly immutable" object mutable anyway (pitfall)
- Compare: immutable objects vs thread-safe mutable objects — cost/benefit (compare)
- The Builder pattern as the standard companion for constructing immutable objects (concept) — cross-link: builder-pattern
- Pitfall: a `final` reference whose *contents* (e.g. a `List`) can still be mutated (pitfall)

### Topic: Synchronization Techniques in OO Design (synchronization-techniques-in-oo-design, advanced)
Locks, granularity, and lock-free alternatives at the object level.
- Locks/mutexes at the object level: synchronized methods vs synchronized blocks (concept)
- Diagram: two threads contending for the same object lock (diagram)
- Lock granularity: one lock per object vs finer-grained locks per field/segment (concept)
- Code: a thread-safe cache using a read-write lock for better throughput (code)
- Atomic classes/compare-and-swap as a lock-free alternative for simple state (concept)
- Compare: coarse-grained locking vs fine-grained locking vs lock-free (compare)
- Pitfall: deadlock from two objects locking each other in opposite order (pitfall)
- Pitfall: over-synchronizing and serializing work that didn't need to be serial (pitfall)

### Topic: Designing Thread-Safe Classes (designing-thread-safe-classes, advanced)
Putting it together: a worked design walkthrough for a thread-safe class from scratch.
- A worked walkthrough: designing a thread-safe LRU cache from scratch (concept) — cross-link: lru-cache
- Diagram: the cache's internal locking boundary around its map + list (diagram)
- Thread confinement: keeping mutable state to one thread instead of sharing it (concept)
- Safe publication: handing a fully-constructed object to another thread without races (concept)
- Code: a thread-safe Singleton using a static holder/double-checked locking, revisited (code) — cross-link: singleton-pattern
- Compare: a synchronized wrapper vs a concurrent collection (e.g. `ConcurrentHashMap`) (compare)
- Pitfall: a "thread-safe" class whose compound check-then-act operations aren't atomic (pitfall)
- Interview framing: talking through the design trade-offs out loud (concept)

---

<!-- expert-tier additions (oo-concurrency) -->

### Topic: Lock-Free and Atomic Object Design (lock-free-and-atomic-object-design, expert)
Designing an object's mutation path with atomic operations instead of locks, and what that trades away.
- Why lock-free: avoiding blocking, deadlock, and priority inversion at the cost of complexity (concept)
- Compare-and-swap as the primitive: read, compute, swap-if-unchanged, retry (concept)
- Diagram: a CAS retry loop updating a shared counter (diagram)
- Code: a lock-free counter or stack built on an atomic reference (code)
- Pitfall: the ABA problem — naive CAS can silently corrupt state (pitfall)
- Compare: lock-free vs lock-based design — throughput and complexity trade-offs (compare)
- Pitfall: assuming lock-free means simpler — it usually means harder to reason about (pitfall)
- Interview: "Design a thread-safe counter without using a lock." (interview)

### Topic: Designing a Concurrent Data Structure's Contract (designing-concurrent-data-structure-contracts, expert)
Specifying what a concurrent class actually promises callers under simultaneous access, beyond "it won't crash."
- Why "thread-safe" isn't a contract by itself: what guarantee are you actually making (concept) — cross-link: designing-thread-safe-classes
- Linearizability and happens-before: what callers can assume about ordering (concept)
- Diagram: two threads racing on a concurrent map, and what the contract guarantees each sees (diagram)
- Pitfall: `if (!map.containsKey(k)) map.put(k, v)` isn't atomic unless the contract says so (pitfall)
- Code: documenting and implementing a `putIfAbsent`-style atomic compound operation (code)
- Compare: weak vs strong consistency guarantees in a concurrent collection's API (compare)
- What belongs in the contract's documentation vs what stays an implementation detail (concept)
- Interview: "What guarantees does a concurrent hash map make that a synchronized map doesn't?" (interview)

---

## Group: LLD in Practice (lld-in-practice)

### Topic: Dependency Injection & Designing for Testability (dependency-injection-and-testability, intermediate)
How to structure object construction so dependencies are supplied, not hand-built, so production and test code can substitute them freely.
- Why `new` inside a class is a design smell: hard-wired dependencies your caller can't swap (concept)
- Dependency injection defined: giving an object its dependencies instead of letting it construct them (concept)
- Constructor injection vs setter/property injection vs method injection (compare)
- Diagram: a class graph before and after extracting seams (diagram)
- Code: refactoring a hard-wired `EmailService` into a constructor-injected dependency (code)
- Injecting an abstraction, not a concrete class — the seam that makes substitution possible (concept) — cross-link: dip-dependency-inversion
- DI containers vs manual wiring: what a container buys you, and what it costs in transparency (compare)
- Pitfall: over-injecting — a constructor with twelve dependencies is a design smell too (pitfall)
- Interview: "How would you make this class testable without pulling in a DI framework?" (interview)

### Topic: Designing Errors: Exceptions, Result Types, and Error Boundaries (designing-errors, intermediate)
Choosing how a component reports failure so the caller can actually recover, not just log and re-throw.
- What an error type is really for: giving the caller something they can act on (concept)
- Exceptions vs result/either types: control-flow cost vs explicit handling (compare)
- Checked vs unchecked exceptions: what each forces the caller to do (concept)
- Diagram: an error boundary at a module edge translating internal failures into a stable contract (diagram)
- Code: a `Result<T, Error>` type replacing a thrown exception in a parsing function (code)
- Designing exception hierarchies: when a new exception type earns its place (concept)
- Pitfall: catching `Exception`/`Throwable` broadly and swallowing the signal (pitfall)
- Pitfall: leaking an implementation-specific error (a raw SQL exception) across a module boundary (pitfall)
- Interview: "When would you use exceptions vs a result type in the same codebase?" (interview)

### Topic: Designing a Public API / Library Surface (designing-public-apis, advanced)
Deciding what a class or module exposes to callers you don't control, and how to change it later without breaking them.
- Minimal surface area: expose the smallest contract that solves the caller's problem (concept)
- Public vs internal: what belongs in the API vs what's an implementation detail masquerading as one (concept)
- Diagram: a library's public surface vs its internals, and where the real seam is (diagram)
- Backwards compatibility: additive-safe changes vs breaking changes (compare)
- Deprecation as a process: marking, documenting, and giving callers a migration path before removal (concept)
- Code: adding a parameter to a public method without breaking existing callers (overload vs default vs builder) (code)
- Semantic versioning as a promise to callers, not a formality (concept)
- Pitfall: exposing a mutable internal object and losing control of your own invariants (pitfall) — cross-link: encapsulation
- Interview: "You need to change a public method's return type. Walk me through how you'd do it." (interview)

### Topic: Designing for Change: Extension Points and Configuration (designing-for-change, advanced)
Deciding where a design should flex for future requirements versus where flexibility is premature and costly.
- Extension points: a seam where new behavior plugs in without touching existing code (concept) — cross-link: ocp-open-closed
- Configuration vs code: when a behavior should be a config value instead of a new class (compare)
- Diagram: a plugin/strategy seam added at the one point that actually varies (diagram)
- Premature abstraction: the cost of an extension point nobody uses yet (concept)
- Pitfall: building a "flexible" framework for a single known use case (pitfall)
- Code: a feature-flagged behavior swap vs a hard-coded conditional (code)
- Telling speculative flexibility apart from a documented near-term need (concept) — cross-link: dry-yagni-kiss
- Interview: "How do you decide whether to add an abstraction now or wait?" (interview)

### Topic: Refactoring Legacy Code into Patterns Safely (refactoring-legacy-into-patterns, expert)
Introducing structure into an untested, tangled codebase without breaking it in the process — the actual mechanics of a safe refactor.
- Why you can't refactor what you can't verify: the safety-net problem (concept)
- Characterization tests: pinning down current behavior, bugs included, before changing anything (concept)
- Diagram: strangling a god class — extracting one responsibility at a time behind a seam (diagram)
- The seam technique: finding a point to insert a test double without a redesign (concept)
- Code: extracting an interface from a god class's most-used method, incrementally (code)
- Sequencing a refactor: smallest safe step, verify, commit, repeat (concept)
- Pitfall: a "big bang" rewrite that hides regressions until launch (pitfall) — cross-link: refactoring-to-fix-smells
- Interview: "You inherit a 2,000-line class with no tests. What's your first move?" (interview)

---

## Group: LLD Interview Framework (lld-framework)

### Topic: The LLD Interview Process, End to End (lld-interview-process, beginner)
The five-step method that structures every LLD interview, and how to pace it.
- The end-to-end method in one picture: requirements → entities → relationships → APIs → walkthrough → trade-offs (concept)
- Diagram: the 5-step method as a flow (diagram)
- How much time to spend on each step in a 45-minute interview (concept)
- What interviewers are actually scoring, not "did you name the GoF pattern" (concept)
- Compare: the LLD interview method vs the HLD/system-design method — where they differ (compare)
- Pitfall: jumping straight to classes before requirements are clear (pitfall)
- Pitfall: over-engineering for scale that was never asked for (pitfall)
- Code: a worked mini-example applying all 5 steps to "design a stack with getMin()" (code)

### Topic: Gathering and Scoping Requirements (gathering-and-scoping-requirements, beginner)
Turning an ambiguous one-line prompt into a scoped, time-boxed problem.
- Functional vs non-functional requirements, and why LLD cares about both (concept)
- The clarifying questions that unlock scope fast (concept)
- Diagram: a requirements checklist mapped to a sample prompt (parking lot) (diagram) — cross-link: parking-lot
- Deciding what's explicitly out of scope, and saying so out loud (concept)
- Code: turning a one-line prompt into a short requirements list (code)
- Pitfall: assuming requirements instead of asking, then building the wrong thing (pitfall)
- Compare: over-asking (stalling) vs under-asking (guessing) — finding the pace (compare)

### Topic: Identifying Entities and Relationships (identifying-entities-and-relationships, intermediate)
Turning requirements text into a first-pass class model.
- Noun extraction: turning requirements into candidate classes (concept)
- Verb extraction: turning requirements into candidate methods/behaviors (concept)
- Deciding is-a vs has-a for each relationship found (concept) — cross-link: composition-vs-inheritance
- Diagram: entities and relationships sketched from a sample prompt (diagram)
- Code: a first-pass class skeleton generated from a requirements list (code)
- Pitfall: modeling every noun as a class, including ones that are just attributes (pitfall)
- Compare: a too-flat model (everything on one class) vs a too-fragmented one (compare)

### Topic: Designing APIs and Class Contracts (designing-apis-and-class-contracts, intermediate)
Shaping method signatures and public surfaces that survive the rest of the interview.
- Designing method signatures: inputs, return types, and what to do on failure (concept)
- Encapsulating internal state so the implementation can change later (concept) — cross-link: encapsulation
- Diagram: a class's public API surface vs its hidden internals (diagram)
- Code: designing `ParkingLot.parkVehicle()`'s signature and error handling (code) — cross-link: parking-lot
- Designing for extension: leaving seams for features the interviewer will add later (concept) — cross-link: ocp-open-closed
- Compare: exceptions vs result/optional types for expected failure cases (compare)
- Pitfall: an API that exposes internal collections/mutability to callers (pitfall)

### Topic: Applying Patterns and Principles Live (applying-design-patterns-and-principles-live, advanced)
Recognizing pattern-shaped problems in the moment, instead of keyword-matching.
- Recognizing a pattern-shaped problem as it comes up, not pattern-matching keywords (concept)
- A quick decision guide: symptom → likely pattern, e.g. "many if/else on type" → Strategy or State (concept)
- Diagram: a cheat-sheet map from common LLD symptoms to patterns/principles (diagram)
- Code: a mid-interview refactor — spotting an OCP violation and fixing it live (code)
- Pitfall: name-dropping patterns without applying them correctly (pitfall)
- Pitfall: forcing a pattern where a plain class would be clearer — over-engineering (pitfall) — cross-link: design-patterns-intro
- Compare: "pattern-first" thinking vs "requirements-first, pattern falls out" thinking (compare)

### Topic: Evaluating and Discussing Trade-offs (evaluating-and-discussing-tradeoffs, advanced)
Defending a design under pushback, and absorbing the interviewer's curveballs.
- Why every LLD decision is a trade-off, and saying the trade-off out loud (concept)
- Handling "now add feature X" curveballs without a full redesign (concept)
- Diagram: extension points in a design that absorb a common curveball cleanly (diagram)
- Code: extending a working design for a new requirement without breaking existing classes (code)
- Discussing complexity/testability/performance trade-offs of a chosen pattern (concept)
- Compare: two valid designs for the same prompt, and how to argue for one (compare)
- Pitfall: defending a design rigidly instead of engaging with the interviewer's pushback (pitfall)

---

---

# Phase C — Low-Level Design: case studies

## Group: LLD Case Studies — Games (lld-cases-games)

*Turn-based and puzzle games: modeling a board and its rules so win/legality logic doesn't collapse into one giant switch.*

### Topic: Tic-Tac-Toe (tic-tac-toe, beginner)
A minimal game whose real test is generalizing the board and win condition instead of hardcoding 3x3.
- The tic-tac-toe prompt and how fast to scope it in an interview — 2 minutes to lock size, players, and win rule (overview)
- Requirements: board size, win condition (K-in-a-row), players; non-goals like AI difficulty tuning or networked play (concept)
- Core entities: Board, Cell, Symbol, Player, Game, WinChecker — who owns the win-check logic and why not `Board` doing everything (concept)
- Diagram: class diagram for a generalized N x N, K-in-a-row tic-tac-toe (diagram)
- Code: `Board.checkWinner(lastMove)` that generalizes beyond 3x3 by checking only the lines through the last move, not the whole board (code)
- The hard part: representing "all winning lines" as data generated once at construction (rows, columns, both diagonals) instead of four hand-written loops (concept)
- Code: `WinChecker.generateLines(n)` building the line set for an N x N board, reused unchanged for any K-in-a-row rule (code)
- Design patterns: Strategy for player type (human vs random-bot vs minimax-bot); deliberately no State pattern — turn state is one boolean flip, not worth the machinery (compare) — cross-link: strategy-pattern
- Extending to a bot player: random-legal-move vs minimax with alpha-beta pruning, and why minimax is tractable here but not for chess (concept) — cross-link: chess-game
- Deep-dive: Connect-Four variant — win condition becomes "K-in-a-row anywhere," gravity constrains where a move can land, and the line-check from `WinChecker` is reused unchanged (concept)
- Deep-dive: 3D (4x4x4) tic-tac-toe — the winning-line count grows combinatorially; show why generating lines once at construction (not per-move) is what keeps `checkWinner` cheap at any dimension (concept)
- Concurrency: this is turn-based and single-writer by construction — the actual concurrency question interviewers ask is "two players submit a move for the same turn over the network," and the fix is a server-side turn-sequence check, not locking the board (concept)
- Pitfall: win-check logic duplicated per row/column/diagonal instead of unified through one `WinChecker` (pitfall)
- Pitfall: accepting a move without validating it's that player's turn and the cell is empty, corrupting board state (pitfall)
- Follow-ups: "how do you detect a draw without scanning the whole board?" — track a remaining-empty-cells counter, decremented per move (interview)
- Follow-ups: "how would you add undo/redo?" — a move history stack replayed from an empty board, not mutable in-place edits (interview)

### Topic: Snake and Ladder (snake-and-ladder, beginner)
A simulation-style case study: decoupling board rules from the turn loop, and making the board data instead of code.
- The snake-and-ladder prompt and scoping a "simple" simulation game in an interview — the trap is under-designing it as a script (overview)
- Requirements: board, dice, snakes/ladders, players, turn order, win condition; non-goals like betting or animated movement (concept)
- Core entities: Board, Dice, Player, Jump (snake or ladder), Game — why Board should not know whose turn it is (concept)
- Diagram: class diagram plus a turn's flow through Dice → Board → Jump → Player (diagram)
- Code: `Game.playTurn()` composing dice roll + position update + jump resolution as separate calls, not one fused method (code)
- The hard part: decoupling board rules (jumps) from the turn loop so the loop never special-cases "did I land on a snake" (concept)
- Code: `Board.resolvePosition(rawPosition)` looking up a jump map and returning the final position, called unconditionally every turn (code)
- Design patterns: `Jump` unifies snakes and ladders as one signed-offset concept; deliberately no State pattern for turns — turn order is a simple rotation, not a state machine with guarded transitions (compare)
- Making the board fully data-driven: board size, jump positions, and overshoot rule loaded from config, not hardcoded constants (concept) — cross-link: ocp-open-closed
- Deep-dive: determinism for testing — injecting a seeded/fake `Dice` so a unit test can assert an exact game trace (concept)
- Extending to multiple dice, "roll again on a 6," or multiplayer-skip power cards without the turn loop knowing the details — each is a rule the `Dice` or `Jump` layer applies, the loop stays unchanged (concept)
- Concurrency: for a local hot-seat game there is none; for an online version, the real question is serializing each player's turn through a single authoritative game-state actor so two rolls never race (concept) — cross-link: oo-concurrency
- Compare: modeling snakes and ladders as one `Jump` concept vs two separate classes — one lookup table wins on extensibility (compare)
- Pitfall: hardcoding board size/jump positions in `Game` instead of making the board data-driven (pitfall)
- Pitfall: forgetting the overshoot rule (a roll past 100 doesn't move) and silently letting a player win early (pitfall)
- Follow-ups: "how would you add a 'You've Been Framed'-style power-card variant live?" — a pluggable `TurnEffect` chain consulted after every roll (interview)
- Follow-ups: "how do you replay a completed game for a UI animation?" — replay the recorded move list against a fresh board rather than storing intermediate render state (interview)

### Topic: Deck of Cards & Blackjack (deck-of-cards-and-blackjack, intermediate)
A reusable Card/Deck abstraction plus Blackjack's Ace-value ambiguity and dealer state machine.
- The prompt: "design a deck of cards" vs "design Blackjack" — why interviewers ask both (overview)
- Requirements: a reusable Card/Deck abstraction plus Blackjack's dealing, hitting, busting rules; non-goals like betting or multiplayer tournaments (concept)
- Core entities: Card, Deck, Shoe, Hand, Player, Dealer, Game (concept)
- Diagram: class diagram separating generic card-game primitives from Blackjack-specific rules (diagram)
- Code: `Deck.shuffle()`/`deal()` and `Hand.addCard()` as the shared contract other card games reuse (code)
- The hard part: scoring a Hand when an Ace can count as 1 or 11 without a special case per hand (concept)
- Code: `Hand.value()` resolving soft/hard totals cleanly (code)
- Diagram: the round's state machine — betting → dealing → player turns → dealer turn → payout (diagram)
- Designing Hand/Game so a new card game (War, Poker) reuses Deck/Card without touching Blackjack rules (concept) — cross-link: strategy-pattern
- Compare: one `Game` superclass with hooks vs a Strategy object per game variant (compare)
- Pitfall: putting Blackjack scoring logic inside `Card` instead of `Hand`, breaking reuse for other games (pitfall)
- Follow-ups: how you'd add multi-deck shoes and card-counting detection (interview)

### Topic: Sudoku Solver & Validator (sudoku-solver-and-validator, intermediate)
A pure constraint-satisfaction case study: no players or turns, just rows/columns/boxes and a backtracking solver.
- The prompt: "design a Sudoku validator" vs "design a solver" — two different interviews (overview)
- Requirements: 9x9 grid, row/column/box uniqueness constraints; solver vs validator as separate scopes (concept)
- Core entities: Grid, Cell, Region (row/column/box) — modeling one cell as a member of three regions at once (concept)
- Diagram: class diagram showing a Cell's membership in its row, column, and 3x3 box (diagram)
- Code: `Grid.isValid()` checking all constraints without triple-nested loops per rule (code)
- The hard part: designing `Region` as one abstraction reused for rows, columns, and boxes instead of three copies of the same check (concept)
- Diagram: backtracking search — trying a digit, recursing, undoing on conflict (diagram)
- Code: a backtracking `solve()` using constraint propagation to prune early (code)
- Compare: brute-force backtracking vs constraint propagation (naked singles/pairs) — when the interviewer wants which (compare)
- Extending the validator to variant puzzles (Sudoku-X, Killer Sudoku) via pluggable Region sets (concept) — cross-link: strategy-pattern
- Pitfall: re-scanning the whole grid on every single-cell update instead of incrementally tracking candidates (pitfall)
- Follow-ups: how you'd parallelize solving or estimate solver runtime on a hard puzzle (interview)

### Topic: Minesweeper (minesweeper, intermediate)
A flood-fill and lazy-generation case study: mines placed only after the first click.
- The Minesweeper prompt and the trap of designing the UI instead of the model (overview)
- Requirements: grid, mines, reveal/flag actions, win when all safe cells are revealed (concept)
- Core entities: Board, Cell, mine layout, Game (concept)
- Diagram: class diagram for the board and a cell's revealed/flagged/mine state (diagram)
- Code: `Board.reveal(cell)` triggering a flood-fill over adjacent zero-count cells (code)
- The hard part: placing mines only after the first click so you never lose on move one (concept)
- Diagram: the flood-fill's recursion/queue over neighboring cells (diagram)
- Code: computing a cell's adjacent-mine count without re-scanning the whole board each time (code)
- Compare: recursive flood-fill vs iterative BFS/queue-based reveal — stack-depth risk on huge boards (compare)
- Extending to variable board shapes or a hexagonal grid without rewriting `reveal()` (concept)
- Pitfall: checking for a win by re-scanning every cell every move instead of tracking a revealed-count (pitfall)
- Follow-ups: how you'd design an auto-solver or a "no-guess" board generator (interview)

### Topic: Chess Game (chess-game, advanced)
The canonical polymorphism-heavy case study: pieces that know their own legal moves, with a huge domain to scope down fast.
- The chess prompt and how to scope a huge domain into a 45-minute design — pick core moves + check detection, defer special moves to follow-ups (overview)
- Requirements: 8x8 board, six piece types, turns, check/checkmate, move legality; non-goals like a full UCI engine or opening book (concept)
- Core entities: Board, Piece (+ six subclasses), Move, Player, Game, MoveValidator — how a `Piece` and the `Board` divide responsibility (concept)
- Diagram: the Piece hierarchy and where move-validation logic actually lives — geometry in the piece, board-state legality in the board (diagram)
- Polymorphic `Piece.getCandidateMoves(board)` vs one giant rules engine — why per-piece polymorphism wins for this domain (concept)
- Code: `Bishop.getCandidateMoves()` vs `Knight.getCandidateMoves()`, same interface, structurally different iteration (code)
- Deep-dive: check/checkmate detection — a candidate move is legal only if, after simulating it, the mover's own king is not attacked; checkmate is "no legal move removes check" (concept)
- Code: `Game.isInCheck(color)` scanning opponent pieces' attack squares against the king's square, and `Game.isCheckmate(color)` trying every legal move to see if any escapes check (code)
- Diagram: the simulate-then-validate flow for one candidate move — apply, check king safety, revert if illegal (diagram)
- Design patterns: Command for move execution/undo (needed for check-simulation and for replay); deliberately no State pattern for "whose turn" — that's one flag, not a state machine (compare) — cross-link: command-pattern
- Deep-dive: special moves as first-class `Move` subtypes — `CastlingMove`, `EnPassantMove`, `PromotionMove` — each knows its own extra board-state side effects instead of `Board` holding if/else per case (concept)
- Code: `CastlingMove.execute(board)` moving both king and rook and marking both as having-moved, in one method the board just calls (code)
- Pitfall: special-move handling (castling, en passant, promotion) bolted on as if/else in `Board.movePiece()` instead of designed as move variants (pitfall)
- Pitfall: mutating the live board to test "does this move cause self-check" without a clean revert, corrupting game state on an illegal attempt (pitfall)
- Extending to a time-control clock (per-move budget, flag-fall loss) sitting alongside `Game` without `Piece` or `Move` knowing it exists (concept)
- Follow-ups: "how do you add move-undo/replay?" — because moves are Commands, undo is just replaying inverse side effects; replay is re-running the move list from an empty board (interview)
- Follow-ups: "how would you speed up move generation for a bot?" — bitboards instead of an 8x8 object array, trading readability for branchless bit tricks (interview)


## Group: LLD Case Studies — Machines (lld-cases-machines)

*Hardware-facing state machines: payment, dispensing, and scheduling loops where the physical device's states are the design.*

### Topic: Parking Lot (parking-lot, intermediate)
The canonical multi-entity LLD prompt: spot-assignment strategy, ticketing, pricing, and a concurrency wrinkle at the gate.
- The parking lot prompt and why it's used to test scoping speed, not cleverness — get to a working v1 in under 10 minutes (overview)
- Requirements: levels, spot types (compact/large/EV/handicap), entry/exit, ticketing, pricing; non-goals like payment-gateway integration (concept)
- Core entities: ParkingLot, Level, ParkingSpot, Vehicle, Ticket, EntryGate/ExitGate — why gates are entities, not just methods (concept)
- Diagram: class diagram for the multi-level, multi-spot-type parking lot (diagram)
- Spot-assignment as a pluggable Strategy: nearest-available vs size-matched vs custom (e.g. EV spots reserved for EVs) (concept) — cross-link: strategy-pattern
- Code: `ParkingLot.parkVehicle(vehicle)` selecting a spot via the assignment strategy and issuing a `Ticket` (code)
- Deep-dive: allocation across levels and spot types without a full-lot scan — each level keeps a free-spot index bucketed by spot type, so "find a free compact spot" is a lookup, not a search (concept)
- Diagram: the free-spot index — per-level, per-type buckets, updated on park/exit (diagram)
- Concurrency: two cars entering the same gate at once, both grabbing "the last spot" — the fix is making spot-reservation the atomic step, not spot-search, e.g. a per-bucket lock or atomic remove-and-return (concept) — cross-link: oo-concurrency
- Code: `Level.reserveSpot(type)` implemented as an atomic "pop from free-bucket" rather than "find then mark," closing the race (code)
- Pricing as its own Strategy object: hourly, flat, per-vehicle-type, first-hour-free — swapped without touching `ParkingLot` (concept) — cross-link: strategy-pattern
- Compare: a single God `ParkingLot` class handling parking, pricing, and ticketing vs decomposed Level/Spot/Ticket/PricingStrategy collaborators (compare)
- Compare: reserving a specific spot at entry vs reserving only a type and assigning the exact spot at walk-in — trade-off for multi-entrance lots (compare)
- Pitfall: modeling spot availability as a boolean scan across all spots instead of an indexed/queryable free-spot structure (pitfall)
- Pitfall: computing the fee from `exitTime - entryTime` with no rounding/grace-period rule, disputing every edge-of-hour exit (pitfall)
- Extending to reserved/EV-charging spots (a spot subtype with its own eligibility check in the assignment strategy) or a multi-lot chain sharing one pricing policy (concept)
- Follow-ups: "how do you handle the lot being full — reject entry or queue?" — a capacity check before gate-open, with an optional waiting-queue extension (interview)
- Follow-ups: "how would you support monthly subscribers with a dedicated spot?" — a `Reservation` entity that removes a spot from the general free-bucket permanently (interview)

### Topic: Vending Machine (vending-machine, intermediate)
The canonical State-pattern case study: inventory, payment, dispensing, and change-making as explicit states.
- The vending machine prompt and why interviewers use it to test State-pattern instincts specifically (overview)
- Requirements: inventory, payment (cash/card), dispensing, change-making; non-goals like a full POS or loyalty system (concept)
- Core entities: Inventory, Product, Slot, Payment, Machine, VendingState — why the state lives outside `Machine`'s own fields (concept)
- Diagram: the machine's state machine — idle → selecting → hasMoney → dispensing → returningChange, with a cancel path from every state (diagram)
- Code: implementing states as State-pattern objects (`IdleState`, `HasMoneyState`, ...), each with `selectProduct()`/`insertMoney()`/`dispense()`, not a switch on an enum (code) — cross-link: state-pattern
- The hard part: change-making — computing exact change from available denominations without a greedy algorithm that fails on odd inventories (concept)
- Code: `ChangeMaker.makeChange(amount, availableCoins)` as a small coin-change solver the machine calls, kept separate from the state machine (code)
- Handling underpayment (keep prompting) and overpayment (auto-refund the difference) as explicit transitions, not exceptions (concept)
- Design patterns: State for the machine's lifecycle, Strategy for payment method and for recipe-based dispensing — deliberately not the same pattern for both (compare) — cross-link: strategy-pattern
- Extending to multiple payment methods (cash, card, mobile wallet) via a `PaymentStrategy` consulted from `HasMoneyState`, without adding new states (concept)
- Extending to recipe-based dispensing (coffee/tea machines: a "product" is a sequence of dispense steps) without touching the state machine, only what `DispensingState` delegates to (concept)
- Concurrency: this machine is single-user by design, so there's no concurrent-purchase race — the real concurrency question is a background restocking/telemetry job reading `Inventory` while a purchase is mid-flight, which needs the inventory decrement to be atomic (concept) — cross-link: oo-concurrency
- Compare: State pattern vs enum + switch for this exact problem — switch duplicates the "what's valid here" check at every call site; State puts it once per state class (compare)
- Pitfall: a state object reaching back into the machine's internals (mutating `Machine.balance` directly) instead of going through its exposed API (pitfall)
- Pitfall: decrementing inventory before dispensing succeeds, so a jammed dispense silently loses stock (pitfall)
- Follow-ups: "what changes if the machine must support remote restocking/telemetry?" — an `Inventory` observer pushing low-stock events, independent of the purchase flow (interview)
- Follow-ups: "how would you refund a failed dispense automatically?" — `DispensingState` transitions to a `RefundingState` on a hardware-failure signal rather than silently swallowing it (interview)

### Topic: ATM System (atm-system, intermediate)
A banking-domain case study pairing a transaction state machine with undoable/auditable operations and hardware faults.
- The ATM prompt and scoping "banking" down to what the interview actually wants — authentication + balance/withdraw/deposit, not ledger internals (overview)
- Requirements: card authentication, balance/withdraw/deposit, hardware components (cash dispenser, card reader); non-goals like fraud-scoring (concept)
- Core entities: ATM, Card, Account, Transaction, CashDispenser, BankService (the boundary to core banking) (concept)
- Diagram: class diagram including the hardware-facing components and the bank-service boundary (diagram)
- Diagram: the ATM's session lifecycle as a state machine — idle → cardInserted → authenticated → transactionInProgress → dispensing/complete, with a timeout-to-idle from every state (diagram)
- Code: `Transaction.execute()` designed as a Command object so it can be logged, audited, and reversed (code) — cross-link: command-pattern
- The hard part: making a withdrawal idempotent against the bank's core system — a network timeout after the bank debits the account but before the ATM confirms must not let a retry double-dispense (concept)
- Code: `Transaction` carrying an idempotency key that `BankService.debit()` uses to detect and no-op a duplicate retry (code)
- Modeling insufficient funds and hardware failure (dispenser jam, out-of-cash) as first-class `TransactionResult` outcomes, not exceptions the caller has to guess about (concept)
- Design patterns: Command for transaction execute/undo/audit; deliberately no Observer here — a single ATM has one screen to update, not many independent subscribers (compare)
- Compare: modeling each transaction type (withdraw/deposit/balance) as its own Command vs one `Transaction` class with a type field — Command wins once undo/audit matters (compare)
- Concurrency: the ATM class talking directly to the bank's account storage instead of through a `BankService` boundary — beyond the obvious pitfall, this boundary is also where you'd add a lock/lease on the account during an in-flight withdrawal to stop a second channel (mobile app) from double-spending the same balance (concept) — cross-link: oo-concurrency
- Pitfall: the ATM class talking directly to the bank's account storage instead of through a service boundary (pitfall)
- Pitfall: dispensing cash before confirming the bank-side debit succeeded, risking cash-out with no matching debit on a late failure (pitfall)
- Follow-ups: "how does a multi-bank ATM network change the design?" — `BankService` becomes a router keyed by card-issuer BIN, with a shared idempotency-key format across banks (interview)
- Follow-ups: "how would cardless withdrawal (QR/OTP-initiated) change session start?" — authentication moves earlier (pre-authorized via the app) and the ATM session starts already-authenticated, skipping the card-read state (interview)

### Topic: Traffic Signal Controller (traffic-signal-controller, intermediate)
A timed state machine across signal groups with a hard safety invariant and emergency interrupts.
- The prompt: design a traffic light controller for one intersection (overview)
- Requirements: signal phases, timing, pedestrian crossing, emergency-vehicle override; non-goals like network-wide coordination (concept)
- Core entities: Intersection, SignalGroup, Light, Phase, Controller, Timer (concept)
- Diagram: class diagram for an intersection's signal groups and shared controller (diagram)
- Diagram: the phase state machine — NS-green/EW-red → all-red clearance → NS-red/EW-green (diagram)
- Code: `Controller.tick()` advancing phases on a timer without racing the hardware (code)
- The hard part: encoding the safety invariant "no two conflicting directions are ever green" so a bug can't violate it (concept)
- Code: a conflict-matrix check the Controller consults before switching any Light (code)
- Compare: a hardcoded phase sequence vs a data-driven phase table read at startup (compare)
- Extending to an emergency-vehicle preemption interrupt without breaking the timed cycle (concept) — cross-link: command-pattern
- Pitfall: modeling all-red clearance as an afterthought instead of a first-class phase, causing collisions (pitfall)
- Follow-ups: how you'd coordinate multiple adjacent intersections for green-wave timing (interview)

### Topic: Car Rental System (car-rental-system, intermediate)
A date-range availability and pricing case study, distinct from the ATM/vending single-transaction focus.
- The prompt: design a car rental system (Zipcar/Hertz-style) (overview)
- Requirements: vehicle catalog, reservations, pickup/return, pricing; non-goals like route optimization (concept)
- Core entities: Vehicle, VehicleCategory, Reservation, Branch, RentalAgreement (concept)
- Diagram: class diagram for vehicles, categories, and reservations across branches (diagram)
- Code: `Branch.reserve(category, dateRange)` checking availability across a date range (code)
- The hard part: checking date-range overlap efficiently across many vehicles instead of a per-day boolean grid (concept)
- Diagram: an interval-overlap check for two candidate reservations on the same vehicle (diagram)
- Pricing as a strategy composed of duration rate, category multiplier, and late/damage fees (concept) — cross-link: strategy-pattern
- Compare: locking a specific vehicle at booking time vs locking only a category and assigning at pickup (compare)
- Extending to one-way rentals (pickup at branch A, return at branch B) (concept)
- Pitfall: computing availability by scanning every reservation instead of an indexed interval structure per vehicle (pitfall)
- Follow-ups: how a rental-with-driver or subscription (monthly swap) model changes the design (interview)

### Topic: Elevator System (elevator-system, advanced)
A state-machine-plus-scheduling case study across multiple concurrent elevators — the scheduling algorithm is the actual interview.
- The elevator prompt and why it's a favorite for testing scheduling thinking, not just state machines (overview)
- Requirements: multiple elevators, multiple floors, requests from inside (destination) and outside (up/down call); non-goals like full building-traffic prediction (concept)
- Core entities: Elevator, ElevatorController, Request (external call + internal destination), Floor, Door (concept)
- Diagram: class diagram for elevators, the shared controller, and the two request types (diagram)
- Diagram: one elevator's own state machine — idle → movingUp/movingDown → doorOpen → idle, with doorOpen interruptible by a new request (diagram)
- The hard part: the scheduling algorithm itself — which elevator serves a new request, and in what order it serves its own queued requests (concept)
- Deep-dive: SCAN/LOOK scheduling — an elevator services all requests in its current direction before reversing, instead of jumping to whichever request arrived first (concept)
- Code: `Elevator.addRequest(request)` inserting into a direction-sorted queue so up-requests are served in floor order while moving up (code)
- Diagram: a scheduling decision across 3 elevators and pending requests — cost estimated per elevator (distance, direction match, current load) and the lowest-cost one wins (diagram)
- Code: `Controller.assignRequest(request)` scoring each elevator and dispatching to the minimum-cost one, as a pluggable scoring Strategy (code) — cross-link: strategy-pattern
- Concurrency: multiple requests arriving while an elevator is mid-move, and two floor-panel presses hitting the controller at the same instant — the queue insert and the cost-scoring read must be consistent, typically via a per-elevator lock plus an idempotent request-id to dedupe repeated presses (concept) — cross-link: oo-concurrency
- Compare: a single shared controller doing global optimization vs each elevator bidding independently on requests — centralized wins on optimality, decentralized wins on simplicity/fault-isolation (compare)
- Pitfall: a scheduling algorithm that always prefers the nearest elevator by distance alone, starving a far-away request indefinitely as closer requests keep arriving (pitfall)
- Pitfall: reversing direction mid-queue instead of finishing all same-direction requests first, causing needless zig-zagging (pitfall)
- Extending to a freight elevator with capacity/weight limits — `Elevator.canAccept(request)` gains a load check, but the scheduling algorithm is unchanged (concept)
- Extending to multi-car dispatch where cars share some floors but not others (double-deck or express/local zoning) — the controller partitions elevators by servable-floor-set before scoring (concept)
- Follow-ups: "how do you prevent starvation formally?" — add wait-time as a scoring factor that grows the longer a request waits, so cost eventually favors it regardless of distance (interview)
- Follow-ups: "what changes under a destination-dispatch panel (riders enter floor before boarding)?" — the controller assigns a car at request time instead of the elevator deciding door-side, enabling load-balancing across cars up front (interview)


## Group: LLD Case Studies — Booking & Marketplaces (lld-cases-booking)

*Reservation systems where the core problem is preventing double-booking or double-matching under concurrency, across seats, dates, or drivers.*

### Topic: Movie Ticket Booking (lld-movie-ticket-booking, advanced)
Seat-locking under concurrent checkout, plus show/screen/seat-layout modeling.
- The prompt: design a movie ticket booking system (BookMyShow-style), scoped against the HLD version of the same name (overview)
- Requirements: theaters, shows, seat layouts, booking, payment; non-goals like recommendations or HLD-scale concerns (concept)
- Core entities: Theater, Screen, Show, Seat, Booking, Payment (concept)
- Diagram: class diagram for theaters, screens, shows, and seat layouts (diagram)
- Code: `Show.holdSeats(seatIds)` reserving seats for the checkout window (code)
- The hard part: preventing two users from double-booking the same seat under concurrent checkout (concept) — cross-link: oo-concurrency
- Diagram: the seat's lifecycle — available → held (with TTL) → booked, and what happens on timeout (diagram)
- Code: an expiring hold implemented so an abandoned checkout releases the seat automatically (code)
- Pricing tiers per seat category and per showtime as a pluggable strategy (concept) — cross-link: strategy-pattern
- Compare: pessimistic locking on the seat row vs optimistic version-check-on-commit (compare)
- Pitfall: holding seats with no expiry, silently locking out inventory from abandoned carts (pitfall)
- Follow-ups: how you'd handle a flash sale for a blockbuster's opening show (interview)

### Topic: Cab Booking System (cab-booking-system, advanced)
Real-time driver-rider matching under location churn, plus a trip state machine and surge pricing.
- The prompt: design the LLD for a cab-booking app (Uber/Ola-style), scoped away from the HLD proximity-service problem (overview)
- Requirements: riders, drivers, trip request, matching, fare calculation; non-goals like map-routing internals (concept)
- Core entities: Rider, Driver, Trip, Location, FareCalculator (concept)
- Diagram: class diagram for riders, drivers, and a trip's lifecycle (diagram)
- Diagram: the trip's state machine — requested → matched → in-progress → completed/cancelled (diagram)
- Code: `MatchingService.findNearestDriver()` over currently-available drivers (code)
- The hard part: matching under constant driver-location churn without scanning every driver on every request (concept) — cross-link: search-index-freshness
- Compare: greedy nearest-driver matching vs a batched/optimized assignment (compare)
- Surge/dynamic pricing as a strategy consulted at trip-request time (concept) — cross-link: strategy-pattern
- Concurrency: two riders' requests matching to the same driver at once (concept) — cross-link: oo-concurrency
- Pitfall: recomputing a full driver search on every location ping instead of an indexed spatial structure (pitfall)
- Follow-ups: how you'd extend this to pooled rides or scheduled-in-advance trips (interview)

### Topic: Food Delivery System (food-delivery-system, advanced)
A three-sided marketplace (restaurant, delivery partner, customer) with an order state machine spanning all three.
- The prompt: design a food delivery system's LLD (Swiggy/DoorDash-style), scoped to the ordering + assignment core (overview)
- Requirements: restaurants, menus, orders, delivery partners; non-goals like recommendation ranking (concept)
- Core entities: Restaurant, MenuItem, Order, DeliveryPartner, Assignment (concept)
- Diagram: class diagram spanning the three actors — customer, restaurant, delivery partner (diagram)
- Diagram: the order's state machine — placed → accepted → preparing → picked-up → delivered, with cancel branches at each stage (diagram)
- Code: `OrderService.placeOrder()` validating menu availability and restaurant capacity (code)
- The hard part: assigning a delivery partner when both restaurant-ready-time and partner-availability are moving targets (concept)
- Compare: assigning a partner at order-time vs at pickup-ready-time — the trade-off in idle time vs delay (compare)
- Modeling partial fulfillment (an item goes out of stock mid-prep) as a first-class order event (concept)
- Pitfall: one `Order` class carrying restaurant-side, delivery-side, and payment logic instead of collaborating services (pitfall) — cross-link: srp-single-responsibility
- Extending to multi-restaurant single-order (mall) fulfillment (concept)
- Follow-ups: how refunds/partial-refunds change the order state machine (interview)

### Topic: Hotel Booking System (hotel-booking-system, advanced)
Date-range room-inventory overlap across room types, plus rate plans — distinct from a movie's fixed-showtime seat hold.
- The prompt: design a hotel booking system's LLD, scoped away from date-search HLD concerns (overview)
- Requirements: room types, inventory per date range, booking, cancellation, rate plans (concept)
- Core entities: Hotel, RoomType, RoomInventory, Booking, RatePlan (concept)
- Diagram: class diagram for hotels, room types, and date-ranged inventory (diagram)
- Code: `RoomType.checkAvailability(dateRange)` against existing bookings (code)
- The hard part: representing per-date inventory so a range query is fast instead of scanning every booking (concept)
- Diagram: an inventory calendar — counts per room type per night, decremented and restored on booking/cancel (diagram)
- Rate plans (refundable, non-refundable, seasonal) as a pluggable pricing strategy (concept) — cross-link: strategy-pattern
- Compare: booking against a specific room number vs against a room-type pool with late assignment (compare)
- Concurrency: two bookings racing for the last room of a type on the same night (concept) — cross-link: oo-concurrency
- Pitfall: modeling cancellation as a delete instead of a state transition, losing the audit trail (pitfall)
- Follow-ups: how overbooking policy (airline-style) or group bookings change the design (interview)

### Topic: Meeting Room & Calendar Scheduler (meeting-room-scheduler, advanced)
Multi-attendee free/busy intersection plus recurrence — a harder version of "check one resource for overlap."
- The prompt: design a meeting-room / calendar scheduling system — and why "just check for overlap" is the wrong scope (overview)
- Requirements: rooms, attendees, recurring meetings, conflict detection; non-goals like video-call integration (concept)
- Core entities: Room, Meeting, Attendee, RecurrenceRule, Calendar (concept)
- Diagram: class diagram for rooms, meetings, and each attendee's calendar (diagram)
- Code: `Calendar.hasConflict(timeRange)` checking a single resource's bookings (code)
- The hard part: finding a slot that's free for a room AND every attendee, not just one resource (concept)
- Diagram: intersecting multiple attendees' free/busy intervals to find a common slot (diagram)
- Code: expanding a `RecurrenceRule` (weekly standup) into concrete occurrences without materializing years of instances (code)
- Compare: eager materialization of recurring instances vs lazy expansion on query (compare)
- Extending to double-booking policies (allow-with-warning vs hard-block) per room type (concept)
- Pitfall: checking conflicts only at creation time, missing conflicts introduced by a later reschedule (pitfall)
- Follow-ups: how you'd support "find the next available slot" across 10 people's calendars (interview)

### Topic: Online Auction System (online-auction-system, expert)
Real-time competitive bidding: concurrency-safe bid ordering, anti-snipe timing, and proxy bidding.
- The prompt: design an online auction system (eBay-style live bidding) (overview)
- Requirements: listings, bids, auction windows, winner determination; non-goals like payment-settlement details (concept)
- Core entities: Listing, Bid, Auction, Bidder, ProxyBid (concept)
- Diagram: class diagram for listings, auctions, and the bid history (diagram)
- Diagram: the auction's state machine — scheduled → open → closing → closed, with an anti-snipe extension window (diagram)
- Code: `Auction.placeBid(amount)` rejecting bids below the current minimum increment (code)
- The hard part: handling two bids arriving in the same instant so the higher one always wins deterministically (concept) — cross-link: oo-concurrency
- Code: implementing proxy/auto-bidding that raises your bid automatically up to a max, without exposing your max to others (code)
- Compare: a hard auction-close time vs an anti-sniping extension that reopens bidding on a late bid (compare)
- Modeling the notification of an outbid user as an Observer, not a poll (concept) — cross-link: observer-pattern
- Pitfall: determining the winner by re-scanning the entire bid history instead of tracking the current-highest incrementally (pitfall)
- Follow-ups: how reserve prices or a "Buy It Now" shortcut change the bidding state machine (interview)

## Group: LLD Case Studies — Infra Building Blocks (lld-cases-infra)

*Systems-y class-level designs — cache, queue, scheduler — where the hard part is a concurrency or algorithmic invariant, not a business rule.*

### Topic: LRU Cache (lru-cache, intermediate)
A data-structure-driven LLD prompt: hashmap plus doubly linked list for O(1) access and eviction, with real thread-safety and TTL follow-ups.
- The LRU cache prompt and why it's really a data-structures interview wearing an LLD hat (overview)
- Requirements: O(1) `get`/`put`, fixed capacity, eviction on overflow; non-goals like distribution up front (concept)
- Core data structure: hashmap (key → node) plus a doubly linked list (recency order), and why each alone isn't enough — hashmap alone has no order, a list alone has no O(1) lookup (concept)
- Diagram: hashmap-to-node pointers plus the linked list's recency ordering, head = most-recent, tail = least-recent (diagram)
- Code: `get()`/`put()` maintaining O(1) by moving the accessed/inserted node to the front, evicting the tail on overflow (code)
- The hard part (O(1) proof): every operation the API needs — lookup, move-to-front, remove-tail, insert-at-front — is O(1) only because the list is doubly linked (removal needs `prev`, not just `next`) (concept)
- Pitfall: an "O(1)" implementation that's secretly O(n) because eviction scans the list for the least-recent node instead of holding a `tail` pointer (pitfall)
- Thread-safety, deep-dive: a single coarse lock around `get`/`put` is correct but serializes all readers, even though `get` conceptually only needs to move one node — discuss a read-write lock or a per-segment lock (sharding the keyspace) as the next step (concept) — cross-link: designing-thread-safe-classes
- Code: a `synchronized`/mutex-guarded `get()` that still mutates recency order, showing why LRU can't use a plain read-lock for reads (code)
- TTL + eviction interaction, deep-dive: a key can die two ways — LRU eviction (capacity) or TTL expiry (time) — and they must not fight; store `expiresAt` per node and check it on both lazy access and the periodic active-sweep, removing from both the map and the list together (concept)
- Diagram: a node holding both its LRU list position and its TTL, with lazy-expiry-on-access and active-sweep-on-timer as the two removal paths (diagram)
- Design patterns: Strategy for a pluggable eviction policy behind a generic `Cache<K,V>` interface — swap `LRUPolicy` for `LFUPolicy` without touching the map/list plumbing (concept) — cross-link: strategy-pattern
- Compare: LRU vs LFU vs FIFO eviction — LRU tracks recency (cheap, O(1)), LFU tracks frequency (needs a frequency-bucket structure for true O(1)), FIFO ignores access pattern entirely — when interviewers ask "why not just FIFO" (compare)
- Follow-ups: "how would you shard this cache across threads?" — partition keys by hash into N independent LRU instances, each with its own lock, trading global recency accuracy for parallelism (interview) — cross-link: distributed-caching
- Follow-ups: "how do you turn this into a distributed cache?" — the hashmap+list becomes per-node state behind a consistent-hash router; recency is now per-shard, not global (interview) — cross-link: distributed-caching

### Topic: Logging Framework (logging-framework, intermediate)
A deceptively deep "simple" prompt: levels, sinks, formatting, and — once probed — async delivery under load.
- The logging framework prompt and why "just print to console" fails the interview immediately (overview)
- Requirements: log levels, multiple destinations (console/file/cloud), formatting, minimal performance overhead on the caller; non-goals like a full log-aggregation backend (concept)
- Core entities: Logger, LogLevel, LogRecord, Appender/Sink, Formatter (concept)
- Diagram: a log call flowing through level-check → formatter → multiple appenders (diagram)
- Chain of Responsibility for level filtering — DEBUG → INFO → WARN → ERROR handlers, each deciding whether to pass the record on (concept) — cross-link: chain-of-responsibility-pattern
- Code: adding a new appender (e.g. `CloudAppender`) without touching `Logger` — it just implements the `Appender` interface and gets registered (code) — cross-link: ocp-open-closed
- Should `Logger` be a Singleton? The usual instinct vs the real trade-off — a global logger is convenient but makes per-module level overrides and testing harder; most real frameworks use a Logger-per-class-name registry instead (concept) — cross-link: singleton-pattern
- The hard part: synchronous logging blocks the caller on every slow sink (disk, network) — async logging fixes throughput but introduces its own design problem: what happens when producers outrun the writer (concept)
- Code: an async `Logger` pushing `LogRecord`s onto a bounded queue, with a dedicated writer thread draining it to appenders (code)
- Diagram: the producer-thread → bounded queue → writer-thread pipeline, with the queue's full-policy (block, drop, or discard-oldest) called out explicitly (diagram)
- Compare: synchronous vs asynchronous logging — sync guarantees order and durability per call but couples caller latency to I/O; async decouples latency but risks losing the tail of records on a crash unless the queue is flushed on shutdown (compare)
- Backpressure under high volume, deep-dive: sampling (log 1-in-N DEBUG records) or level-elevation-under-load (temporarily suppress DEBUG/INFO when the queue is filling) as the two standard mitigations (concept)
- Pitfall: a logging call that itself throws (a formatter bug, a full disk) and crashes the caller — logging must never propagate its own failures upward (pitfall)
- Pitfall: making every appender synchronous-by-default so one slow network sink stalls all logging application-wide (pitfall)
- Follow-ups: "how would you add structured/JSON logging?" — `Formatter` becomes pluggable per-appender, and `LogRecord` needs a structured-fields map alongside the message string (interview)
- Follow-ups: "how do you guarantee no log loss on process crash?" — periodic flush plus a shutdown hook draining the queue synchronously before exit, accepting a brief slowdown only at shutdown (interview)

### Topic: Rate Limiter (rate-limiter, advanced)
An algorithm-heavy case study comparing limiter strategies under concurrent access, single-process and distributed.
- The rate limiter prompt and the algorithm menu interviewers expect you to know before writing a line of code (overview)
- Requirements: per-user/per-API limits, configurable window and quota, defined behavior on breach (reject vs queue); non-goals like billing integration (concept)
- Algorithm options: fixed window, sliding window (log and counter variants), token bucket, leaky bucket (concept)
- Diagram: a token bucket filling at a constant rate and draining per request, rejecting when empty (diagram)
- Diagram: fixed window's boundary-burst problem — 2x the limit lands in the 1-second straddle across two windows — vs sliding window fixing it (diagram)
- Code: implementing a token bucket limiter as a pluggable `RateLimitStrategy` (code) — cross-link: strategy-pattern
- Code: a sliding-window-counter limiter approximating the sliding log with O(1) memory by weighting the previous window's count (code)
- The hard part: thread-safety — a naive check-then-act ("if tokens > 0, decrement") is not atomic and lets concurrent requests both pass when only one token remains (concept) — cross-link: oo-concurrency
- Code: making the token check-and-decrement one atomic operation via a lock or a CAS loop on the token count (code)
- Compare: the four algorithms on memory cost, burst tolerance, and boundary accuracy — token bucket allows controlled bursts, sliding window is smoothest but costlier, fixed window is cheapest but burst-prone (compare)
- Pitfall: a check-then-act limiter that isn't atomic, letting bursts through exactly at the moments load is highest (pitfall)
- Pitfall: resetting counters on a wall-clock boundary without accounting for clock skew across servers in a multi-instance deployment (pitfall)
- Distributed rate limiting, deep-dive: a single-process in-memory limiter is wrong once there's more than one API server — the counter must live in a shared store (e.g. Redis) with the check-and-decrement done atomically server-side (a Lua script or `INCR`+`EXPIRE`), not read-modify-write from the app (concept) — cross-link: distributed-rate-limiting
- Extending to per-tenant tiered limits (free vs paid) — the limiter takes a `LimitPolicy` resolved per tenant instead of one global quota, reusing the same algorithm underneath (concept)
- Follow-ups: "how do you rate-limit fairly across many small tenants without one noisy tenant starving the shared limiter's memory?" — bucket eviction/LRU on idle tenant keys (interview)
- Follow-ups: "what would you tell the client on breach?" — a `429` with a `Retry-After` derived from the bucket's refill rate, not a bare rejection (interview)

### Topic: Notification System (notification-system, intermediate)
A multi-channel fan-out prompt built on Observer plus per-user strategy — the class-level design, not the HLD fan-out service.
- The notification system prompt and disambiguating this class-level design from the HLD version of the same name (overview)
- Requirements: multiple channels (email/SMS/push/WhatsApp), templates, user preferences, delivery tracking; non-goals like the HLD-scale fan-out pipeline (concept)
- Core entities: Notification, Channel, Template, UserPreference, DeliveryStatus (concept)
- Diagram: an event fanning out to multiple channel senders through a dispatcher (diagram)
- Observer pattern: the event is the subject, channel senders are observers that each decide independently whether/how to act (concept) — cross-link: observer-pattern
- Code: adding a new channel (e.g. WhatsApp) without modifying the notification dispatcher — it registers a new `ChannelSender` implementing the same interface (code) — cross-link: ocp-open-closed
- Strategy for per-user channel preference and quiet hours — resolved per notification before dispatch, not hardcoded per channel (concept)
- The hard part: delivery isn't fire-and-forget — each channel can fail independently and needs its own retry/backoff, so one `Notification.send()` call fans out into N independently-tracked delivery attempts (concept)
- Code: `DeliveryAttempt.retry()` with exponential backoff, tracked per (notification, channel) pair so a failed SMS doesn't block a successful email (code)
- Diagram: a notification's per-channel delivery state — pending → sent → delivered/failed, with failed retriable up to a cap before landing in a dead-letter state (diagram)
- Idempotency, deep-dive: a retried send must not double-notify the user — dedupe on a stable (notification id, channel) key so a retry after a slow-but-successful first attempt is a no-op (concept)
- Compare: push-based fan-out (dispatcher calls each channel synchronously) vs queue-based fan-out (dispatcher enqueues per-channel jobs) — queue-based isolates a slow channel and enables retry without blocking the caller (compare)
- Pitfall: a `Notification` class that formats itself differently per channel via if/else instead of delegating formatting to each `Channel`'s own `Template` renderer (pitfall)
- Pitfall: treating "sent" and "delivered" as the same status, hiding real failures (bounced email, undelivered push) from the user preference logic (pitfall)
- Follow-ups: "how would you add delivery-status tracking and retry-on-failure per channel?" — already the deep-dive above; the follow-up is usually "what's your retry cap and backoff curve" — answer with a bounded exponential backoff plus dead-letter (interview)
- Follow-ups: "how do you avoid spamming a user across channels for one event?" — a per-event coalescing window that picks the user's preferred channel first and suppresses the rest unless it fails (interview)

### Topic: In-Memory Key-Value Store (in-memory-key-value-store, advanced)
A mini-Redis: generic storage, TTL expiry, and pluggable persistence — broader than a cache's eviction-only focus.
- The prompt: design an in-memory key-value store (a mini-Redis), and how it differs from "design a cache" (overview)
- Requirements: get/set/delete, TTL expiry, pluggable persistence; non-goals like distribution/replication (concept)
- Core entities: Store, Entry (value + expiry), ExpiryPolicy, PersistenceStrategy (concept)
- Diagram: class diagram for the store, its entries, and pluggable expiry/persistence (diagram)
- Code: `Store.set(key, value, ttl)` and `get()` checking expiry lazily on read (code)
- The hard part: expiring millions of keys without scanning the whole store on every access (concept)
- Diagram: active expiry via a background sweep plus lazy expiry on access — the two-pronged approach (diagram)
- Compare: lazy expiry vs active-sweep expiry vs a min-heap of expiry times (compare)
- Concurrency: readers and a background expiry sweep touching the same map (concept) — cross-link: oo-concurrency
- Extending to additional data types (list, set, hash) behind the same store without an if/else per type (concept)
- Pitfall: persistence writes blocking the main read/write path instead of running off to the side (pitfall)
- Follow-ups: how you'd add an LRU-eviction fallback when the store hits a memory cap (interview) — cross-link: lru-cache

### Topic: Message Queue (message-queue-system, advanced)
Producer/consumer decoupling with delivery-semantics guarantees — a different concurrency lesson than the KV store's indexing problem.
- The prompt: design an in-process message queue (a simplified Kafka/RabbitMQ core) (overview)
- Requirements: producers, consumers, topics/queues, ack-based delivery; non-goals like multi-broker replication (concept)
- Core entities: Queue, Message, Producer, Consumer, ConsumerGroup, Acknowledgement (concept)
- Diagram: class diagram for queues, messages in flight, and consumer acknowledgement (diagram)
- Code: `Queue.publish()`/`consume()` with an in-flight/unacked message set (code)
- The hard part: guaranteeing at-least-once delivery — what happens to a message when a consumer crashes mid-processing (concept) — cross-link: message-delivery-semantics
- Diagram: a message's lifecycle — queued → in-flight → acked/nacked → requeued or dead-lettered (diagram)
- Compare: at-most-once vs at-least-once vs exactly-once semantics for this in-process design (compare)
- Ordering guarantees per-partition/per-key vs global ordering, and what you give up for throughput (concept)
- Pitfall: acking a message before processing completes, silently losing it on crash (pitfall)
- Extending to a dead-letter queue for messages that repeatedly fail (concept)
- Follow-ups: how you'd evolve this single-process design toward a distributed broker (interview) — cross-link: queues-vs-pubsub

### Topic: Thread Pool & Task Scheduler (thread-pool-and-task-scheduler, expert)
A bounded worker-pool design: backpressure, rejection policies, and priority/delayed scheduling.
- The prompt: design a thread pool / task executor from scratch (overview)
- Requirements: submit tasks, bounded worker count, queued backlog, graceful shutdown; non-goals like distributed job scheduling (concept)
- Core entities: ThreadPool, WorkerThread, TaskQueue, Task, RejectionPolicy (concept)
- Diagram: class diagram for the pool, its workers, and the shared task queue (diagram)
- Code: `ThreadPool.submit(task)` enqueuing work that idle workers pick up (code)
- The hard part: what happens when the queue is full and a new task arrives — backpressure vs rejection vs blocking (concept)
- Diagram: a worker's loop — pull task → execute → catch/report failure → pull next (diagram)
- Code: implementing a `RejectionPolicy` (reject, caller-runs, discard-oldest) as a pluggable strategy (code) — cross-link: strategy-pattern
- Compare: a fixed-size pool vs a dynamically-growing pool with a cap — when each fits (compare)
- Extending to a delayed/priority scheduler (run at time T, or highest-priority-first) atop the same pool (concept)
- Concurrency: safely shutting down without dropping in-flight tasks or hanging forever (concept) — cross-link: designing-thread-safe-classes
- Pitfall: an unbounded task queue that "never rejects" until the process runs out of memory (pitfall)
- Follow-ups: how Java's `ThreadPoolExecutor` or Python's `ThreadPoolExecutor` map onto this design (interview)

## Group: LLD Case Studies — Business Domains (lld-cases-business)

*Domain-modeling case studies — the hard part is an aggregation, ledger, or graph algorithm sitting behind an ordinary-looking CRUD surface.*

### Topic: Library Management System (library-management-system, beginner)
A gentle first case study: modeling a catalog, its copies, members, holds, and borrowing rules.
- The library management prompt and why it's the standard "gentle first" LLD case study (overview)
- Requirements: catalog, physical copies, members, checkout/return, holds, fines; non-goals like a recommendation engine (concept)
- Core entities: Book (catalog entry), BookItem (physical copy), Member, Loan, Reservation — why "book" and "copy" differ and why conflating them breaks availability tracking (concept)
- Diagram: class diagram for the core library entities and their relationships (diagram)
- Code: `Member.checkout(bookItem)` with availability, per-member borrow-limit, and existing-fine checks (code)
- Modeling reservations/holds as their own entity, not a boolean flag on `BookItem` — a hold has a requester, a queue position, and an expiry once the copy becomes available (concept)
- Diagram: a `BookItem`'s lifecycle — available → onHold → checkedOut → available, with a returned-but-damaged branch to a `Lost/Damaged` state (diagram)
- Design patterns: Strategy for fine/loan policy per member type (student vs faculty vs guest); deliberately no Observer for hold-ready notifications at this scope — a scheduled job checking hold queues is simpler and sufficient (compare) — cross-link: strategy-pattern
- The hard part: a hold queue is FIFO per title, and when the last checked-out copy of a title is returned, the next holder must get first refusal before the item goes back to general availability (concept)
- Code: `BookItem.returnItem()` checking the title's hold queue before marking itself generally available, and starting an expiry timer on the notified holder (code)
- Compare: a single `Book` class vs `Book` + `BookItem` — catalog concerns (title, author, ISBN) vs inventory concerns (which physical copy, its condition, its current holder) (compare)
- Concurrency: the last available copy of a popular title being checked out by two members' requests at once — the fix is the same atomic reserve-then-confirm pattern as parking-lot/movie-seat holds, not a post-hoc availability re-check (concept) — cross-link: oo-concurrency
- Pitfall: fine calculation living inside `Member` instead of a dedicated `FinePolicy` object, so every member-type variant means editing `Member` (pitfall) — cross-link: srp-single-responsibility
- Pitfall: marking a returned item "available" without checking the hold queue first, silently skipping members who requested it (pitfall)
- Follow-ups: "how would you extend this to multi-branch libraries with inter-branch transfers?" — `BookItem.currentBranch` plus a `TransferRequest` entity; availability queries become per-branch with an opt-in cross-branch hold (interview)
- Follow-ups: "how do you handle a lost/damaged item mid-loan?" — a status transition on `BookItem` to `Lost`, decrementing the title's available-copy count and triggering a replacement-fee policy, distinct from an overdue fine (interview)

### Topic: Splitwise (Expense Sharing) (splitwise-expense-sharing, advanced)
A ledger-modeling case study built around split strategies and a debt-simplification algorithm, with real money-math pitfalls.
- The Splitwise prompt and why it's a favorite ledger-modeling case study — the "hard part" isn't CRUD, it's the graph algorithm hiding behind it (overview)
- Requirements: groups, expenses, split types (equal/exact/percentage/shares), settle-up; non-goals like actual payment processing (concept)
- Core entities: User, Group, Expense, Split, BalanceSheet — why balances are derived from expenses, not stored as the source of truth (concept)
- Diagram: class diagram for expenses, their splits, and the balance sheet they update (diagram)
- Strategy pattern for split types — equal, exact-amount, percentage, and share-based, each turning one `Expense` into a list of `Split`s (concept) — cross-link: strategy-pattern
- Code: `SplitStrategy.computeSplits(expense, participants)` for the equal and exact variants, showing where each can fail validation (code)
- Money-math pitfall, deep-dive: floating-point rounding across splits that never quite sums back to the original amount — the fix is storing money as integer minor units (cents) and assigning the rounding remainder to one designated participant deterministically (concept)
- Code: `splitEqually(amountInCents, n)` distributing `amount / n` plus giving the leftover cents to the first participants, so splits always sum exactly to the total (code)
- The hard part: the debt-simplification problem — a group with many pairwise debts should settle with the minimum number of transactions, not one per original expense (concept)
- Diagram: a debt graph before simplification (many pairwise edges) and after (few net-settling edges) (diagram)
- Code: a greedy debt-simplification algorithm — repeatedly match the largest debtor with the largest creditor via two heaps, settling the smaller of the two amounts each round (code)
- Compare: storing pairwise balances (who-owes-whom per pair) vs net balances per user (one number per person, positive = owed to them) — net balances are what the simplification algorithm needs and what "settle up" actually shows the user (compare)
- Concurrency: two group members adding expenses that touch the same balance sheet simultaneously — updates to a user's net balance must be applied atomically (an increment, not a read-modify-write of a cached total) or two concurrent expenses can lose one update (concept) — cross-link: oo-concurrency
- Pitfall: floating-point rounding across splits that never quite sums to the original amount (pitfall)
- Pitfall: recomputing every user's net balance by replaying the full expense history on every query instead of maintaining running balances incrementally (pitfall)
- Extending to multi-currency groups — every `Split` carries its currency, and net balances are computed per-currency-pair (or normalized to a group base currency via a stored FX rate at expense-time, never a live-lookup rate) before simplification runs (concept)
- Extending to partial settle-ups — a `Settlement` is itself a special zero-split expense between two users that reduces their net balance without needing to touch or re-simplify the whole group (concept)
- Follow-ups: "why can't you just simplify to zero transactions?" — simplification minimizes transaction count but can't always avoid person A paying person C who then pays B, because the algorithm only matches by amount, not by original relationship — that's an accepted trade-off, not a bug (interview)
- Follow-ups: "how do you show a user 'you owe X in total' across multiple groups?" — aggregate net balances per counterparty across all shared groups, kept separate from any one group's simplification run (interview)

### Topic: Payment / Wallet System (payment-wallet-system, advanced)
Double-entry ledger correctness and idempotent transaction processing — a different ledger lesson than Splitwise's debt graph.
- The prompt: design a digital wallet / payments ledger (Paytm/Venmo-style balance system) (overview)
- Requirements: wallet balance, top-up, transfer, transaction history; non-goals like card-network integration (concept)
- Core entities: Wallet, Account, Transaction, LedgerEntry (concept)
- Diagram: class diagram modeling a transfer as two linked ledger entries, not a balance mutation (diagram)
- The hard part: double-entry bookkeeping — every transaction is a debit and a credit that must always balance (concept)
- Code: `Ledger.transfer(from, to, amount)` writing both entries atomically (code)
- Diagram: the transaction's state machine — pending → completed/failed, with reversal as a new entry, never an edit (diagram)
- Idempotency: handling a retried transfer request so the user isn't charged twice (concept) — cross-link: idempotency-and-exactly-once
- Concurrency: two concurrent transfers against the same wallet balance (concept) — cross-link: oo-concurrency
- Compare: mutable balance-field design vs append-only ledger with a derived balance — why interviews want the second (compare)
- Pitfall: "fixing" a bad transaction by editing history instead of writing a compensating entry (pitfall)
- Follow-ups: how you'd add multi-currency wallets or a hold/authorize-then-capture flow (interview)

### Topic: E-commerce Cart & Order (ecommerce-cart-and-order, advanced)
Cart-to-order snapshotting (price/inventory locked at checkout) plus an order state machine spanning payment, shipping, and returns.
- The prompt: design an e-commerce cart and order system (overview)
- Requirements: cart, checkout, order, inventory reservation, returns; non-goals like search/recommendations (concept)
- Core entities: Cart, CartItem, Order, OrderItem, Inventory, Payment (concept)
- Diagram: class diagram for the cart-to-order transition (diagram)
- The hard part: snapshotting price and product details at checkout so a later price change doesn't retroactively alter a placed order (concept)
- Code: `Cart.checkout()` converting cart items into immutable `OrderItem` snapshots (code)
- Diagram: the order's state machine — placed → paid → shipped → delivered, with cancel/return branches at each stage (diagram)
- Inventory reservation at checkout vs at payment-confirmation — the trade-off in abandoned-cart lockup (concept)
- Compare: soft-reserving inventory on add-to-cart vs only at checkout (compare)
- Modeling partial shipment/partial return as first-class order events, not edits to the original order (concept)
- Pitfall: recalculating order total from current product prices instead of the checkout-time snapshot (pitfall)
- Follow-ups: how you'd extend this to multi-seller marketplace orders with split shipments (interview)

### Topic: Inventory Management System (inventory-management-system, advanced)
Multi-location stock tracking with on-hand/reserved/available separation — the warehouse-side counterpart to the cart's customer-side problem.
- The prompt: design an inventory management system for a warehouse/retail chain (overview)
- Requirements: SKUs, stock levels per location, reservations, transfers, reordering; non-goals like demand-forecasting models (concept)
- Core entities: SKU, Warehouse, StockLevel, Reservation, Transfer, ReorderRule (concept)
- Diagram: class diagram for SKUs and their stock levels across multiple warehouses (diagram)
- Code: `Inventory.reserve(sku, qty, location)` decrementing available (not on-hand) stock (code)
- The hard part: separating "on-hand," "reserved," and "available" quantities so concurrent reservations never oversell (concept)
- Diagram: a stock movement — on-hand stays fixed while available drops on reservation and on-hand drops only on fulfillment (diagram)
- Concurrency: two reservations racing for the last unit of a SKU at one location (concept) — cross-link: oo-concurrency
- Automating reorder via a threshold rule as a pluggable policy per SKU (concept) — cross-link: strategy-pattern
- Compare: reserving stock at a single location vs pooling availability across nearby locations (compare)
- Pitfall: modeling "quantity" as one field instead of on-hand/reserved/available, causing phantom oversells (pitfall)
- Follow-ups: how you'd extend this to serialized/lot-tracked inventory (expiry dates, batch recalls) (interview)

### Topic: Issue Tracker (Jira-style) (issue-tracker-system, advanced)
Configurable per-project workflow state machines — the state machine is data, not a hardcoded enum.
- The prompt: design an issue tracker (Jira/Linear-style) (overview)
- Requirements: projects, issues, custom workflows, assignment, comments; non-goals like reporting dashboards (concept)
- Core entities: Project, Issue, Workflow, Status, Transition, User, Comment (concept)
- Diagram: class diagram for issues and their configurable workflow (diagram)
- The hard part: making the workflow itself data — different projects need different status sets and transitions, not a hardcoded enum (concept)
- Code: `Workflow.canTransition(issue, targetStatus)` validated against a per-project transition table (code)
- Diagram: two different projects' workflows as distinct transition graphs over the same `Issue` model (diagram)
- Compare: a global fixed status enum vs a per-project configurable workflow — the extensibility interviewers are probing (compare)
- Modeling permissions (who can transition, assign, or comment) without an if/else per role (concept) — cross-link: dip-dependency-inversion
- Extending to sub-tasks and issue-linking (blocks/relates-to) without changing the core Issue model (concept)
- Pitfall: hardcoding "done" or "in-progress" as special-cased strings scattered through the codebase (pitfall)
- Follow-ups: how you'd add SLA timers or automatic transitions on inactivity (interview)

### Topic: URL Shortener — Class Design (lld-url-shortener, intermediate)
The encoding-scheme trade-off and the encoder/repository class boundary — the class-level version of the HLD scaling question.
- The prompt: design the class-level API for a URL shortener, and how this differs from the HLD "design a URL shortener" scale question (overview)
- Requirements: shorten, redirect, optional custom aliases, expiry; non-goals like distributed ID generation at scale (concept)
- Core entities: UrlMapping, Encoder, Repository, ExpiryPolicy (concept)
- Diagram: class diagram separating the encoding strategy from the storage repository (diagram)
- Code: `ShortenerService.shorten(longUrl)` composing an Encoder and a Repository behind one API (code)
- The hard part: choosing base62-counter vs hash-of-URL-with-collision-handling, and what each costs in code complexity (concept)
- Compare: base62 counter vs MD5/SHA hash truncation vs random-then-check — collision handling per approach (compare)
- Code: a collision-retry loop for the hash-based encoder, bounded so it can't loop forever (code)
- Extending to custom aliases and per-link expiry without changing the core `shorten`/`resolve` contract (concept) — cross-link: ocp-open-closed
- Pitfall: exposing the internal counter/ID directly instead of behind an Encoder abstraction, locking in one scheme forever (pitfall)
- Follow-ups: how this class design plugs into the distributed ID generation the HLD version needs at scale (interview) — cross-link: design-unique-id-generator

---

# Phase D — High-Level Design: concepts

## Group: Capacity Estimation (capacity-estimation)

*back-of-envelope, QPS/storage math*

### Topic: Back-of-Envelope Fundamentals (back-of-envelope-fundamentals, beginner)
The mental-math habits and reference numbers behind every estimate used later in a design.
- Why estimation matters before you design anything (concept)
- Numbers every engineer should memorize (RAM/disk/network latency) (concept)
- Powers of two and ten: fast mental math shortcuts (concept)
- Diagram: the latency numbers ladder (L1 cache to cross-region) (diagram)
- Rounding strategy: precision you don't need vs precision you do (concept)
- Pitfall: chasing decimal precision that doesn't change the design (pitfall)
- Interview: talk through an estimate out loud, not just the final number (interview)

### Topic: Traffic Estimation & QPS (traffic-estimation-qps, beginner)
Turning DAU/MAU into queries-per-second, and why the read/write ratio and peak multiplier change the design.
- From DAU/MAU to requests per second (concept)
- Read-heavy vs write-heavy: why the ratio changes your design (concept)
- Average QPS vs peak QPS: the multiplier you must not skip (concept)
- Diagram: traffic curve over a day and the peak-to-average ratio (diagram)
- Worked example: estimating QPS for a social feed, step by step (concept)
- Compare: estimating QPS for a read-heavy feed vs a write-heavy logging system (compare)
- Pitfall: forgetting fan-out multiplies effective QPS (pitfall)
- Interview: "Estimate QPS for this system" — the structure to follow (interview)

### Topic: Storage Estimation (storage-estimation, intermediate)
Sizing storage from a single record to a multi-year total, including the overhead multipliers that are easy to forget.
- From one record's size to total storage (concept)
- Accounting for growth: multi-year projections (concept)
- Diagram: storage estimate worked example, line by line (diagram)
- Don't forget the multipliers: replication factor, indexes, metadata (concept)
- Compare: raw data size vs "real" storage footprint after overhead (compare)
- Worked example: storage for a URL shortener over 5 years (concept)
- Pitfall: sizing storage but forgetting index and replica overhead (pitfall)
- Interview: "How much storage will you need?" — structuring the answer (interview)

### Topic: Bandwidth & Bottleneck Estimation (bandwidth-and-bottleneck-estimation, intermediate)
Estimating network bandwidth and identifying which resource — compute, storage, or network — actually binds the design.
- Bandwidth math: requests × payload size → Mbps/Gbps (concept)
- Diagram: where bandwidth limits actually bite (client, LB, DB) (diagram)
- Identifying the binding constraint: compute vs storage vs network (concept)
- Worked example: video streaming bandwidth estimate (concept)
- Compare: CPU-bound vs I/O-bound vs network-bound systems (compare)
- Pitfall: estimating servers needed without checking network egress cost (pitfall)
- Interview: "How many servers do you need?" — from an estimate to a number (interview)

### Topic: Estimation in the Interview (estimation-in-the-interview, intermediate)
How much precision is enough, and how to run the estimation phase as a fluent five minutes instead of a stall.
- How precise is precise enough (concept)
- A repeatable structure: traffic → storage → bandwidth → servers (concept)
- Diagram: the estimation flow as a checklist (diagram)
- Talking through assumptions out loud (concept)
- Compare: a strong estimate vs a hand-wavy guess — what the interviewer notices (compare)
- Pitfall: spending 15 minutes of a 45-minute interview on estimation (pitfall)
- Interview: sanity-checking your own numbers against known scale points (interview)

---

## Group: Load Balancing & Proxies (load-balancing)

*algorithms, reverse proxy, health checks*

### Topic: Load Balancing Fundamentals (load-balancing-fundamentals, beginner)
What a load balancer does, where it sits in the stack, and the L4 vs L7 distinction.
- What a load balancer actually does (concept)
- Diagram: where the LB sits — client, LB, app tier (diagram)
- L4 vs L7 load balancing: what each layer can see and do (compare)
- Hardware vs software vs cloud-managed LBs (concept)
- A single LB as a new single point of failure — and the fix (concept)
- Pitfall: putting one LB in front without redundancy (pitfall)
- Interview: "Where would you add a load balancer in this design?" (interview)

### Topic: Load Balancing Algorithms (load-balancing-algorithms, intermediate)
Round robin through consistent hashing — how each algorithm distributes load and which workload it fits.
- Round robin and weighted round robin: the baseline (concept)
- Least connections and least response time (concept)
- Consistent hashing: sticky routing without a central map (concept)
- Diagram: consistent hashing ring and what happens when a node joins/leaves (diagram)
- Power-of-two-choices: why it beats plain random (concept)
- Compare: which algorithm fits which workload (compare)
- Code: a minimal consistent hashing ring lookup (code)
- Pitfall: round robin with wildly uneven request costs (pitfall)
- Interview: "Why consistent hashing instead of mod-N hashing?" (interview)

### Topic: Reverse Proxies vs Forward Proxies (reverse-proxies-vs-forward-proxies, beginner)
Who each proxy type hides, and what a reverse proxy adds beyond plain load balancing.
- Forward proxy vs reverse proxy: who they hide (concept)
- Diagram: forward proxy (hides client) vs reverse proxy (hides server) (diagram)
- What a reverse proxy adds: TLS termination, compression, caching (concept)
- NGINX/HAProxy/Envoy: what each is optimized for (compare)
- API gateway vs reverse proxy: where the line blurs (concept)
- Pitfall: conflating "load balancer" and "reverse proxy" as the same thing (pitfall)
- Interview: "What does terminating TLS at the proxy buy you?" (interview)

### Topic: Health Checks & Failover (health-checks-and-failover, intermediate)
Detecting a bad node and routing around it without dropping in-flight requests.
- Active health checks vs passive health checks (concept)
- Diagram: health check loop pulling a bad node out of rotation (diagram)
- Choosing check intervals and thresholds: flapping vs slow detection (compare)
- Connection draining: removing a node without dropping in-flight requests (concept)
- Failover mechanics: how traffic re-routes when a node dies (concept)
- Pitfall: a health check that passes while the app is actually unhealthy (pitfall)
- Interview: "A node is failing intermittently — how does your LB handle it?" (interview)

### Topic: DNS-Based & Global Load Balancing (dns-based-and-global-load-balancing, intermediate)
Routing users to the nearest healthy region using DNS, GSLB, and anycast.
- DNS round robin: the simplest global load balancing (concept)
- GSLB and anycast: routing by network topology (concept)
- Diagram: geo-routing a user to the nearest region (diagram)
- DNS TTLs and the failover-speed trade-off (concept)
- Compare: DNS-based vs proxy-based global load balancing (compare)
- Pitfall: relying on DNS TTL for fast failover (pitfall)
- Interview: "How do you route users to the closest healthy region?" (interview)

### Topic: Sticky Sessions & Statelessness (sticky-sessions-and-statelessness, intermediate)
Session affinity's appeal, its real cost, and the alternatives that avoid pinning a client to one node.
- What session affinity is and why it's tempting (concept)
- Diagram: sticky session pinning a client to one node (diagram)
- The cost: uneven load, failover pain, scaling friction (concept)
- Alternatives: external session store, JWT-based state (compare)
- When stickiness is actually the right call (concept)
- Pitfall: sticky sessions silently breaking during a deploy/failover (pitfall)
- Interview: "Your app breaks when a user's node restarts — why, and how do you fix it?" (interview)

---

<!-- expert-tier additions (load-balancing) -->

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

## Group: Caching (caching)

*cache patterns, eviction, invalidation*

### Topic: Caching Fundamentals (caching-fundamentals, beginner)
Why caching exists, where caches live across the stack, and what belongs in one.
- Why caching exists: the latency/cost gap it closes (concept)
- Diagram: where caches sit — browser, CDN, app, DB (diagram)
- Cache hit, miss, and hit ratio as the metric that matters (concept)
- In-process cache vs external cache (Redis/Memcached) (compare)
- What belongs in a cache vs what doesn't (concept)
- Pitfall: caching data that changes faster than the cache is refreshed (pitfall)
- Interview: "Where would you add caching in this design, and why there?" (interview)

### Topic: Cache Read/Write Patterns (cache-read-write-patterns, intermediate)
Cache-aside, read-through, write-through, and write-behind — the trade-offs behind each.
- Cache-aside (lazy loading): the most common pattern (concept)
- Diagram: cache-aside read and write flow (diagram)
- Read-through and write-through: pushing the logic into the cache layer (concept)
- Write-behind (write-back): async writes and the risk it takes on (concept)
- Compare: all four patterns — consistency, latency, complexity (compare)
- Code: cache-aside read path in pseudocode (code)
- Pitfall: write-behind losing data on a cache crash before flush (pitfall)
- Interview: "Which caching pattern fits a read-heavy product page?" (interview)

### Topic: Eviction Policies (eviction-policies, intermediate)
LRU and its alternatives — how bounded memory forces a choice about what to keep.
- Why eviction is unavoidable: bounded memory (concept)
- LRU: the default choice and how it's implemented (concept)
- Diagram: LRU via hashmap + doubly linked list (diagram)
- LFU and FIFO: when they beat LRU (compare)
- TTL-based expiry combined with eviction (concept)
- Approximated LRU at scale (Redis' sampling approach) (concept)
- Code: LRU cache with get/put in O(1) (code)
- Pitfall: LRU thrashing under a scan-heavy access pattern (pitfall)
- Interview: "Implement an LRU cache" — the follow-ups to expect (interview)

### Topic: Cache Invalidation (cache-invalidation, advanced)
One of the two hard problems in CS — keeping a cache from lying about the current state of the data.
- Why invalidation is one of the two hard problems in CS (concept)
- TTL expiry vs explicit invalidation: the trade-off (compare)
- Diagram: a stale read after an underlying write (diagram)
- Write-through invalidation vs cache-busting on write (concept)
- Invalidating across a cache cluster: fan-out and races (concept)
- Versioned keys / cache-busting as an alternative to deletion (concept)
- Pitfall: invalidating the cache before the DB write commits (race) (pitfall)
- Interview: "A user updates their profile but sees stale data — why?" (interview)

### Topic: Distributed Caching (distributed-caching, advanced)
Sharding a cache cluster and surviving the failure modes unique to caches at scale — stampedes above all.
- Why a single cache node stops being enough (concept)
- Sharding a cache cluster with consistent hashing (concept)
- Diagram: cache cluster with consistent hashing and replica nodes (diagram)
- Cache stampede / thundering herd: when everyone misses at once (concept)
- Mitigations: request coalescing, jittered TTLs, early recompute (concept)
- Compare: client-side sharding vs proxy-based cache clusters (compare)
- Pitfall: a cold cache after deploy causing a stampede on the DB (pitfall)
- Interview: "Your cache cluster just cold-started — what happens, and how do you prevent it?" (interview)

### Topic: CDN & Edge Caching (cdn-and-edge-caching, intermediate)
Caching at the edge — what a CDN caches, how freshness is decided, and where personalized content breaks it.
- What a CDN caches and why it sits at the edge (concept)
- Diagram: request flow with a CDN in front of origin (diagram)
- Cache-Control, ETag, and how the client/CDN decide freshness (concept)
- Caching static assets vs caching dynamic/API responses (compare)
- Cache purging/invalidation across CDN edge nodes (concept)
- Pitfall: caching a personalized/authenticated response at a shared edge node (pitfall)
- Interview: "How would you use a CDN to speed up a global product?" (interview)

---

<!-- expert-tier additions (caching) -->

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

## Group: Storage at Scale (storage-scale)

*SQL vs NoSQL at scale, partitioning*

### Topic: SQL vs NoSQL at Scale (sql-vs-nosql-at-scale, intermediate)
Where relational databases strain under scale, and what NoSQL trades away to relieve it.
- Where relational databases start to strain under scale (concept)
- What NoSQL actually trades away for scale (joins, transactions, schema) (concept)
- Diagram: vertical/read-replica scaling vs horizontal partitioning (diagram)
- Compare: SQL vs NoSQL on consistency, flexibility, query power (compare)
- "NewSQL" and scale-out relational systems, briefly (concept)
- Pitfall: choosing NoSQL for scale you don't actually have yet (pitfall)
- Interview: "Would you use SQL or NoSQL here, and why?" (interview)

### Topic: NoSQL Data Models (nosql-data-models, intermediate)
Key-value, document, column-family, and graph models — picked by access pattern, not by hype.
- Key-value stores: the simplest model and its ceiling (concept)
- Document stores: nested data and flexible schema (concept)
- Column-family stores: wide rows for write-heavy, time-series-like data (concept)
- Graph databases: when relationships are the query (concept)
- Diagram: the same data modeled four ways (diagram)
- Compare: choosing a model by access pattern, not by hype (compare)
- Pitfall: modeling a document store like a relational schema (pitfall)
- Interview: "What data store would you pick for this feature, and why?" (interview)

### Topic: Partitioning & Sharding (partitioning-and-sharding, advanced)
Splitting one database across many nodes, and the shard-key decision that's hard to undo.
- Why one database eventually must be split (concept)
- Range-based partitioning: simple, but hotspot-prone (concept)
- Hash-based partitioning: even spread, loses range queries (concept)
- Diagram: range vs hash partitioning side by side (diagram)
- Directory-based / lookup-service partitioning (concept)
- Choosing a shard key: the decision that's hard to undo (concept)
- Compare: partitioning strategies on rebalancing cost and query support (compare)
- Pitfall: a shard key that creates a hot shard (e.g. sharding by date) (pitfall)
- Interview: "How would you shard this table, and what shard key?" (interview)

### Topic: Resharding & Hotspots (resharding-and-hotspots, advanced)
Rebalancing shards as data grows, and taming the celebrity/hot-key problem.
- Why shard counts change over time (growth, hotspots) (concept)
- Diagram: consistent hashing to minimize data movement on resharding (diagram)
- Live resharding without downtime: dual-write/backfill strategies (concept)
- The celebrity/hot-key problem: one key overwhelming one shard (concept)
- Mitigations: key salting, splitting hot keys, caching in front (concept)
- Compare: static shard count vs dynamic/elastic sharding (compare)
- Pitfall: resharding synchronously and taking the system down to do it (pitfall)
- Interview: "One celebrity user's data is a hotspot — what do you do?" (interview)

### Topic: Polyglot Persistence (polyglot-persistence, intermediate)
Combining multiple data stores in one system without losing track of which one owns the truth.
- Why real systems use more than one data store (concept)
- Diagram: one system, several stores, each owning its slice (diagram)
- Drawing store-ownership boundaries so data doesn't get duplicated ad hoc (concept)
- Keeping stores in sync: dual writes, CDC, event-driven updates (concept)
- Compare: one-store simplicity vs polyglot flexibility (compare)
- Pitfall: polyglot persistence without a clear source of truth per field (pitfall)
- Interview: "Why would you use both Postgres and Elasticsearch here?" (interview)

### Topic: Object & Blob Storage (object-and-blob-storage, intermediate)
Storing large, infrequently-updated files outside the database, and wiring uploads without proxying bytes through your servers.
- What object storage is for: large, immutable, infrequently-updated blobs (concept)
- Diagram: upload flow — client, app, object store, CDN (diagram)
- Object storage vs a database BLOB column vs a filesystem (compare)
- Metadata in the DB, bytes in the object store: the standard split (concept)
- Pre-signed URLs: uploading/downloading without proxying through your servers (concept)
- Pitfall: storing large binary files directly in a relational database (pitfall)
- Interview: "Design the storage for a photo/video upload feature" (interview)

---

<!-- expert-tier additions (storage-scale) -->

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

## Group: Consistency & Replication (consistency-replication)

*quorums, leader/follower, conflict resolution*

### Topic: Consistency Models (consistency-models, intermediate)
The spectrum from strong to eventual consistency, and the session guarantees users actually notice.
- The consistency spectrum: strong to eventual (concept)
- Strong consistency: what it guarantees and what it costs (concept)
- Eventual consistency: what "eventual" actually means in practice (concept)
- Diagram: a write propagating to replicas over time (diagram)
- Causal consistency and session guarantees: read-your-writes, monotonic reads (concept)
- Compare: consistency models by what a user can observe (compare)
- Pitfall: assuming "eventual" means "within milliseconds" (pitfall)
- Interview: "A user doesn't see their own post immediately — why, and is that okay?" (interview)

### Topic: Replication Strategies (replication-strategies, intermediate)
Single-leader, multi-leader, and leaderless replication — and the conflicts each one signs you up for.
- Why replication exists: durability and read scaling (concept)
- Single-leader replication: simple, with a clear bottleneck (concept)
- Diagram: single-leader with followers serving reads (diagram)
- Multi-leader replication: writes anywhere, conflicts everywhere (concept)
- Leaderless replication (Dynamo-style): writes to any replica, quorum reads (concept)
- Compare: single-leader vs multi-leader vs leaderless (compare)
- Pitfall: multi-leader replication without a conflict resolution plan (pitfall)
- Interview: "Why might you choose leaderless replication for this system?" (interview)

### Topic: Synchronous vs Asynchronous Replication (synchronous-vs-asynchronous-replication, intermediate)
The durability/latency trade-off behind every replication choice, and what replication lag does to reads.
- Synchronous replication: durability at the cost of latency (concept)
- Asynchronous replication: fast writes, replication lag risk (concept)
- Diagram: sync vs async replication timelines (diagram)
- Replication lag: what it does to read-after-write behavior (concept)
- Semi-synchronous replication as the middle ground (concept)
- Compare: sync vs async vs semi-sync on durability, latency, complexity (compare)
- Pitfall: reading from a lagging replica right after writing to the leader (pitfall)
- Interview: "Would you replicate synchronously or async here?" (interview)

### Topic: Quorum Systems (quorum-systems, advanced)
Tuning consistency vs availability with N/W/R quorums, sloppy quorums, and hinted handoff.
- Quorums: reads and writes that overlap by design (concept)
- The N/W/R formula and what W+R>N buys you (concept)
- Diagram: a quorum write and read overlapping across N replicas (diagram)
- Tuning consistency vs availability by choosing W and R (concept)
- Sloppy quorums and hinted handoff (concept)
- Compare: strict quorum vs sloppy quorum (compare)
- Pitfall: choosing W=1, R=1 and assuming you still have strong consistency (pitfall)
- Interview: "How would you tune a Dynamo-style store for read-heavy traffic?" (interview)

### Topic: Conflict Resolution (conflict-resolution, advanced)
Resolving concurrent writes with last-write-wins, vector clocks, CRDTs, or application-level merges.
- Why conflicts are inevitable once you allow concurrent writes (concept)
- Last-write-wins: simple, and what it silently throws away (concept)
- Vector clocks: detecting concurrent writes without wall-clock time (concept)
- Diagram: two concurrent writes and a vector clock detecting the conflict (diagram)
- CRDTs: data types that merge without conflict by construction (concept)
- Application-level merge (like a shopping cart union) (concept)
- Compare: LWW vs vector clocks vs CRDTs on correctness and complexity (compare)
- Pitfall: last-write-wins silently dropping a concurrent update (pitfall)
- Interview: "Two devices edit the same document offline — how do you reconcile?" (interview)

### Topic: Consensus Basics (consensus-basics, advanced)
Why distributed nodes need consensus at all, and Raft/Paxos at the depth a design interview expects.
- Why you need consensus: agreeing on one truth across unreliable nodes (concept)
- What consensus guarantees (and what it costs in latency) (concept)
- Diagram: a leader election / log replication round at a glance (diagram)
- Raft at interview depth: leader election + log replication, no more (concept)
- Paxos, briefly: why it's famous and why most systems use Raft instead (concept)
- Where consensus actually shows up: config stores, leader election, distributed locks (concept)
- Compare: consensus-based coordination vs quorum-based storage (compare)
- Pitfall: reaching for Paxos/Raft to solve a problem a quorum already solves (pitfall)
- Interview: "How does your system agree on who the leader is?" (interview)

---

<!-- expert-tier additions (consistency-replication) -->

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

## Group: Messaging & Streaming (messaging-streaming)

*queues, pub/sub, Kafka, delivery semantics*

### Topic: Messaging Fundamentals (messaging-fundamentals, beginner)
Why decoupling producers from consumers with async messaging is worth its added complexity.
- Why decouple producers and consumers at all (concept)
- Synchronous request/response vs asynchronous messaging (compare)
- Diagram: producer → queue → consumer, decoupled in time and space (diagram)
- What async buys you: load leveling, retries, isolation of failures (concept)
- What async costs you: latency, complexity, eventual consistency (concept)
- Pitfall: making everything async "for scale" when a request still needs an answer now (pitfall)
- Interview: "Would you make this call synchronous or async?" (interview)

### Topic: Queues vs Pub/Sub (queues-vs-pubsub, intermediate)
Point-to-point delivery vs fan-out — picked by who actually needs to receive the message.
- Point-to-point queues: one message, one consumer (concept)
- Pub/sub: one message, every subscriber (concept)
- Diagram: queue with competing consumers vs pub/sub fan-out (diagram)
- Competing consumers pattern for horizontal scaling of workers (concept)
- Compare: queue vs pub/sub — pick by "who should get this message" (compare)
- Topics and routing keys: filtering what a subscriber receives (concept)
- Pitfall: using pub/sub where you actually needed exactly one consumer to act (pitfall)
- Interview: "Order placed — who needs to know, and queue or pub/sub?" (interview)

### Topic: Message Delivery Semantics (message-delivery-semantics, advanced)
At-most-once, at-least-once, and exactly-once — what each really promises, and why idempotency is unavoidable.
- At-most-once, at-least-once, exactly-once: what each really promises (concept)
- Why exactly-once delivery is (almost) a myth over a network (concept)
- Diagram: a retry causing duplicate delivery (diagram)
- Idempotency keys: making at-least-once safe in practice (concept)
- Code: an idempotent consumer using a dedupe key (code)
- Compare: delivery guarantee vs processing guarantee — they're not the same (compare)
- Pitfall: assuming the broker's "exactly-once" removes the need for idempotency (pitfall)
- Interview: "Your payment consumer might get the same event twice — now what?" (interview)

### Topic: Log-Based Streaming (log-based-streaming, advanced)
Kafka's commit-log model — partitions, consumer groups, and offsets as a replayable source of truth.
- The commit log model: Kafka as an append-only, replayable log (concept)
- Partitions: how a topic scales horizontally (concept)
- Diagram: topic, partitions, and consumer groups mapped out (diagram)
- Consumer groups and offsets: parallelism without losing your place (concept)
- Ordering guarantees: per-partition order, not global order (concept)
- Compare: a traditional message queue vs a log-based stream (compare)
- Retention and replay: treating the log as a source of truth (concept)
- Pitfall: picking a partition key that skews load onto one partition (pitfall)
- Interview: "Why Kafka instead of a queue here?" (interview)

### Topic: Event-Driven Architecture (event-driven-architecture, intermediate)
Structuring services around events instead of requests, and choosing who owns the workflow.
- Event notification vs event-carried state transfer (concept)
- Diagram: a service publishing an event that others react to (diagram)
- Choreography vs orchestration: who owns the workflow (compare)
- Change data capture (CDC): turning DB writes into a stream (concept)
- Event sourcing, briefly: state as a sequence of events (concept)
- Compare: request-driven vs event-driven service communication (compare)
- Pitfall: an event-driven system with no way to trace a request end to end (pitfall)
- Interview: "Design the event flow for an order-to-shipment pipeline" (interview)

### Topic: Backpressure & Dead-Letter Handling (backpressure-and-dead-letter-handling, intermediate)
What happens when consumers fall behind, and containing the damage with backoff and dead-letter queues.
- What happens when a consumer is slower than the producer (concept)
- Backpressure strategies: buffering, dropping, slowing the producer (concept)
- Diagram: a queue building up as a consumer falls behind (diagram)
- Retry with backoff vs immediate retry storms (compare)
- Dead letter queues: quarantining messages that can't be processed (concept)
- Poison messages: detecting and handling the "always fails" case (concept)
- Pitfall: infinite retry loops amplifying an outage (pitfall)
- Interview: "Consumers are falling behind during a spike — what do you do?" (interview)

---

<!-- expert-tier additions (messaging-streaming) -->

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

## Group: Microservices & Service Mesh (microservices)

*decomposition, sagas, mesh*

### Topic: Monolith vs Microservices (monolith-vs-microservices, beginner)
What actually changes when you split a monolith, and when the trade-off is worth taking.
- What a monolith actually is (and isn't as bad as its reputation) (concept)
- What "microservices" changes: deployment, ownership, failure isolation (concept)
- Diagram: monolith vs microservices topology (diagram)
- Compare: monolith vs microservices on velocity, complexity, operational cost (compare)
- The organizational reason for microservices (Conway's Law) (concept)
- Pitfall: adopting microservices for a team too small to operate them (pitfall)
- Interview: "Would you split this into microservices? Justify it." (interview)

### Topic: Service Decomposition (service-decomposition, intermediate)
Drawing service boundaries by business capability instead of technical layer.
- Decomposing by business capability / bounded context, not by technical layer (concept)
- Diagram: wrong (layer-based) vs right (domain-based) service boundaries (diagram)
- Signs a service boundary is wrong: chatty calls, shared tables (concept)
- Sizing a service: "two-pizza team" and single-responsibility at the service level (concept)
- Compare: coarse-grained vs fine-grained service boundaries (compare)
- Pitfall: a "distributed monolith" — services that must deploy together (pitfall)
- Interview: "How would you split this e-commerce monolith into services?" (interview)

### Topic: Inter-Service Communication (inter-service-communication, intermediate)
Synchronous and asynchronous calling patterns between services, and how a caller finds a live instance.
- Synchronous REST/gRPC calls between services (concept)
- Asynchronous communication via events/queues (concept)
- Diagram: a request fanning out across three services synchronously (diagram)
- Service discovery: how a caller finds a live instance (concept)
- Compare: sync vs async inter-service communication trade-offs (compare)
- gRPC vs REST between services: why gRPC is common internally (compare)
- Pitfall: a synchronous call chain that turns one slow service into a full outage (pitfall)
- Interview: "Service A needs data from B and C — how do they talk?" (interview)

### Topic: Distributed Transactions & Sagas (distributed-transactions-and-sagas, advanced)
Why two-phase commit doesn't fit microservices, and coordinating multi-service writes with sagas instead.
- Why two-phase commit doesn't scale across services (concept)
- The saga pattern: a sequence of local transactions plus compensations (concept)
- Diagram: an order saga with a compensating action on failure (diagram)
- Choreography-based sagas vs orchestration-based sagas (compare)
- Designing compensating transactions: what "undo" means for a non-reversible step (concept)
- Code: a saga step and its compensating handler, sketched (code)
- Pitfall: a saga with a compensation that itself can fail (pitfall)
- Interview: "Payment succeeds but inventory reservation fails — walk me through it" (interview)

### Topic: Service Mesh (service-mesh, advanced)
What a sidecar-based mesh adds on top of plain service-to-service calls — mTLS, traffic control, and observability hooks.
- What a service mesh adds on top of plain service-to-service calls (concept)
- Sidecar proxy pattern: data plane vs control plane (concept)
- Diagram: sidecars intercepting all service traffic (diagram)
- mTLS between services: identity and encryption without app changes (concept)
- Traffic management: retries, timeouts, circuit breaking, canary routing at the mesh layer (concept)
- Compare: logic in the mesh vs logic in application code (compare)
- Pitfall: adopting a service mesh before you have enough services to justify the complexity (pitfall)
- Interview: "What would a service mesh give you here that your code doesn't?" (interview)

### Topic: Shared Data & the Database-per-Service Problem (shared-data-and-the-database-per-service-problem, advanced)
Why a shared database quietly defeats the point of microservices, and how to query across services once data is split.
- Database-per-service: why sharing one DB defeats the point of microservices (concept)
- Diagram: shared DB anti-pattern vs database-per-service (diagram)
- Querying across services once the data is split (API composition, CQRS) (concept)
- Keeping data in sync across services (events, CDC) (concept)
- Compare: shared DB vs database-per-service on consistency and autonomy (compare)
- Pitfall: two services silently sharing a table "just for now" (pitfall)
- Interview: "Order service needs product data — should it call or replicate?" (interview)

### Topic: Strangler Fig & Migration Patterns (strangler-fig-and-migration-patterns, intermediate)
Migrating a monolith to services incrementally instead of a risky rewrite.
- Why you can't (and shouldn't) rewrite a monolith in one shot (concept)
- The strangler fig pattern: routing slices of traffic to the new system (concept)
- Diagram: a proxy gradually shifting routes from monolith to new services (diagram)
- Extracting a service: data migration and dual-write windows (concept)
- Compare: big-bang rewrite vs incremental strangler migration (compare)
- Pitfall: leaving the strangler proxy in place forever, half-migrated (pitfall)
- Interview: "How would you migrate this monolith without a rewrite?" (interview)

---

<!-- expert-tier additions (microservices) -->

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

## Group: API Design (api-design)

*REST/gRPC/GraphQL, versioning, pagination*

### Topic: REST API Design (rest-api-design, beginner)
Resources, verbs, and status codes as the core REST mental model.
- Resources, not actions: the REST mental model (concept)
- HTTP verbs mapped to CRUD, and where that mapping breaks down (concept)
- Diagram: a resource hierarchy as URLs (diagram)
- Status codes that actually communicate the right thing (concept)
- Compare: REST vs RPC-style endpoints (compare)
- Code: a well-designed REST endpoint set for one resource (code)
- Pitfall: verbs in the URL (`/getUser`) and inconsistent status codes (pitfall)
- Interview: "Design the REST API for this feature" (interview)

### Topic: API Design Deep Practices (api-design-deep-practices, intermediate)
Idempotent writes, filtering/sorting without URL sprawl, and a consistent error format.
- Idempotency in APIs: safe retries for POST (concept)
- Idempotency keys in practice (concept)
- Filtering, sorting, and partial responses without blowing up the URL (concept)
- Diagram: a request with filter/sort/field-selection params (diagram)
- Consistent error response format across an API (concept)
- Compare: rich query params vs a dedicated query/search endpoint (compare)
- Pitfall: a non-idempotent POST that double-charges on a client retry (pitfall)
- Interview: "How do you make a 'charge card' endpoint safe to retry?" (interview)

### Topic: Pagination Strategies (pagination-strategies, intermediate)
Offset, cursor, and keyset pagination — and why offset breaks under concurrent writes.
- Offset/limit pagination: simple, and where it falls apart (concept)
- Cursor-based pagination: stable pages under concurrent writes (concept)
- Diagram: offset pagination skipping/duplicating rows during inserts (diagram)
- Keyset pagination: cursors built from the last row's sort key (concept)
- Compare: offset vs cursor vs keyset on performance and consistency (compare)
- Code: a keyset-paginated query (code)
- Pitfall: deep offset pagination scanning millions of skipped rows (pitfall)
- Interview: "Design pagination for an infinite-scroll feed" (interview)

### Topic: gRPC & Protobuf (grpc-and-protobuf, intermediate)
Contract-first, binary RPC with streaming — and when it beats REST/JSON internally.
- Contract-first APIs: defining the schema before the code (concept)
- Protocol Buffers: binary, typed, versionable messages (concept)
- Diagram: gRPC over HTTP/2 with a multiplexed connection (diagram)
- Unary, server-streaming, client-streaming, bidirectional streaming (concept)
- Compare: gRPC vs REST/JSON — performance, tooling, browser support (compare)
- Code: a minimal .proto service definition (code)
- Pitfall: using gRPC for a public browser-facing API without a gateway (pitfall)
- Interview: "Why gRPC for internal service calls but REST at the edge?" (interview)

### Topic: GraphQL Fundamentals (graphql-fundamentals, intermediate)
One endpoint, client-specified shape — and the N+1 problem that comes with it.
- One endpoint, client-specified shape: the GraphQL model (concept)
- Schema, types, and resolvers (concept)
- Diagram: a single GraphQL query resolving fields from multiple services (diagram)
- Solving REST's over-fetching and under-fetching (concept)
- The N+1 query problem and batching/dataloader fixes (concept)
- Compare: GraphQL vs REST — flexibility vs caching/simplicity (compare)
- Pitfall: a naive resolver chain causing an N+1 explosion (pitfall)
- Interview: "When would you reach for GraphQL over REST?" (interview)

### Topic: API Versioning & Evolution (api-versioning-and-evolution, intermediate)
Changing an API without breaking clients that are still on the old contract.
- Why APIs must change without breaking existing clients (concept)
- URI versioning vs header versioning vs no versioning (compare)
- Diagram: two client versions hitting compatible API versions (diagram)
- Backward-compatible changes vs breaking changes: the rule of thumb (concept)
- Deprecation strategy: sunset headers, timelines, communicating change (concept)
- Pitfall: a "breaking" field change shipped as a non-breaking patch (pitfall)
- Interview: "How do you add a required field without breaking existing clients?" (interview)

### Topic: API Gateway Patterns (api-gateway-patterns, intermediate)
Centralizing auth, rate limiting, and routing at a single entry point in front of many services.
- What an API gateway centralizes: auth, rate limiting, routing, transformation (concept)
- Diagram: gateway in front of many backend services (diagram)
- Backend-for-frontend (BFF): a gateway per client type (concept)
- Compare: API gateway vs service mesh — where each one operates (compare)
- Request/response transformation and protocol translation at the gateway (concept)
- Pitfall: the gateway becoming a monolith of business logic (pitfall)
- Interview: "Where does auth belong — gateway or each service?" (interview)

---

<!-- expert-tier additions (api-design) -->

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

## Group: Rate Limiting & Resilience (resilience)

*limiter algorithms, circuit breaker, retries*

### Topic: Rate Limiting Algorithms (rate-limiting-algorithms, intermediate)
Token bucket, leaky bucket, and window counters — the canonical algorithms behind any limiter.
- Why rate limit at all: protecting yourself and being a good API citizen (concept)
- Fixed window counter: simple, and its edge-burst flaw (concept)
- Sliding window log / sliding window counter: smoothing the edge case (concept)
- Token bucket: allowing bursts up to a cap (concept)
- Diagram: token bucket filling and draining over time (diagram)
- Leaky bucket: smoothing output to a constant rate (concept)
- Compare: all four algorithms on burst tolerance and memory cost (compare)
- Code: token bucket rate limiter (code)
- Pitfall: fixed window allowing 2x the limit right at the window boundary (pitfall)
- Interview: "Design a rate limiter for a public API" (interview)

### Topic: Distributed Rate Limiting (distributed-rate-limiting, advanced)
Enforcing one limit consistently across many app servers without the limiter becoming the new bottleneck.
- Why per-node rate limiting fails once you have many nodes (concept)
- Centralized counter in Redis: shared state for the limit (concept)
- Diagram: many app nodes checking one shared limiter (diagram)
- Race conditions in check-then-increment, and atomic fixes (concept)
- Approximate/local limiting to avoid a single limiter becoming the bottleneck (concept)
- Compare: strict centralized limiting vs eventually-consistent distributed limiting (compare)
- Pitfall: a rate limiter whose own lookup becomes the new bottleneck (pitfall)
- Interview: "How do you rate-limit consistently across 100 app servers?" (interview)

### Topic: Circuit Breakers (circuit-breakers, intermediate)
Stopping calls to an already-broken dependency instead of piling on more failing requests.
- The circuit breaker analogy: stop calling something that's already broken (concept)
- Closed, open, half-open: the state machine (concept)
- Diagram: circuit breaker state transitions over time (diagram)
- Choosing trip thresholds and recovery timing (concept)
- Compare: circuit breaker vs plain retries — different failure modes they solve (compare)
- Code: a simple circuit breaker wrapping a client call (code)
- Pitfall: a circuit breaker that flips open/closed rapidly ("flapping") (pitfall)
- Interview: "A downstream service is timing out under load — what do you add?" (interview)

### Topic: Retries, Timeouts & Backoff (retries-timeouts-and-backoff, intermediate)
Why naive retries amplify outages, and the backoff/jitter/budget discipline that prevents it.
- Why naive retries make outages worse, not better (concept)
- Exponential backoff and why linear/fixed retry intervals fail (concept)
- Jitter: preventing synchronized retry storms (concept)
- Diagram: retries without jitter synchronizing into a thundering herd (diagram)
- Setting timeouts: per-hop budgets in a multi-service call chain (concept)
- Retry budgets: capping total retries as a fraction of traffic (concept)
- Compare: retry-heavy vs fail-fast client behavior (compare)
- Pitfall: retrying a non-idempotent write on timeout (pitfall)
- Interview: "Client requests are timing out — how should the client retry?" (interview)

### Topic: Bulkheads & Isolation (bulkheads-and-isolation, intermediate)
Containing one dependency's failure to its own compartment instead of starving everything else.
- The bulkhead analogy: containing failure to one compartment (concept)
- Thread pool / connection pool isolation per dependency (concept)
- Diagram: one slow dependency exhausting a shared thread pool vs isolated pools (diagram)
- Isolating by tenant, priority, or dependency (concept)
- Compare: shared resource pool vs bulkheaded pools — cost vs blast radius (compare)
- Pitfall: one noisy tenant/dependency starving all others from a shared pool (pitfall)
- Interview: "One slow downstream call is taking down unrelated requests — why?" (interview)

### Topic: Graceful Degradation & Load Shedding (graceful-degradation-and-load-shedding, advanced)
Doing less instead of doing nothing — fallbacks, shedding, and stopping cascades before they spread.
- Graceful degradation: doing less instead of doing nothing (concept)
- Fallback responses: cached/stale/default data instead of an error (concept)
- Diagram: a feature falling back to a degraded mode under load (diagram)
- Load shedding: dropping low-priority requests to protect the core path (concept)
- Prioritizing traffic: what to shed first (concept)
- Compare: shedding at the edge vs deep in the call chain (compare)
- Cascading failure: how one overloaded service takes down its callers (concept)
- Pitfall: no fallback path, so any failure becomes a hard user-facing error (pitfall)
- Interview: "Recommendations service is down — what does the homepage show?" (interview)

---

<!-- expert-tier additions (resilience) -->

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

## Group: Search & Indexing (search-indexing)

*inverted index, ranking, autocomplete*

### Topic: Search Fundamentals (search-fundamentals, beginner)
Why full-text search needs its own system instead of a SQL `LIKE` query.
- Why `LIKE '%term%'` doesn't scale for text search (concept)
- What "search" actually requires: relevance, typo tolerance, speed (concept)
- Diagram: a search request from query box to ranked results (diagram)
- Structured queries vs full-text search: different problems (compare)
- Where search fits in a system architecture (concept)
- Pitfall: bolting search onto the primary OLTP database at scale (pitfall)
- Interview: "Why not just query the database for search?" (interview)

### Topic: Inverted Index (inverted-index, intermediate)
The term → document data structure at the core of every search engine.
- The inverted index: from documents to a term → document map (concept)
- Diagram: building an inverted index from a handful of documents (diagram)
- Tokenization, stemming, stop words: preparing text for indexing (concept)
- Posting lists and how a query intersects them (concept)
- Code: building a tiny inverted index (code)
- Compare: inverted index vs a B-tree index for text search (compare)
- Pitfall: indexing without normalization, so "Run" and "running" never match (pitfall)
- Interview: "How does a search engine find documents containing your query terms?" (interview)

### Topic: Relevance Ranking (relevance-ranking, advanced)
Scoring and ordering matches — TF-IDF, BM25, and the boosting signals layered on top.
- Why matching isn't enough — ranking is the real product (concept)
- TF-IDF: term frequency weighted by rarity (concept)
- BM25: TF-IDF's more practical successor (concept)
- Diagram: two documents scored and ranked for the same query (diagram)
- Boosting signals: recency, popularity, field weighting (concept)
- Compare: pure text relevance vs learning-to-rank with ML signals (compare)
- Pitfall: ranking by recency alone and burying the actually relevant result (pitfall)
- Interview: "Search results feel wrong — how do you debug ranking?" (interview)

### Topic: Autocomplete & Typeahead (autocomplete-and-typeahead, intermediate)
Serving ranked suggestions within a tight latency budget as the user types.
- What autocomplete optimizes for: latency over completeness (concept)
- Trie-based prefix matching (concept)
- Diagram: a trie returning top-k completions for a prefix (diagram)
- Ranking suggestions: frequency, personalization, recency (concept)
- Precomputing top-k per prefix to hit tight latency budgets (concept)
- Compare: trie-based vs index-based (search-as-you-type) autocomplete (compare)
- Pitfall: recomputing suggestions from scratch on every keystroke (pitfall)
- Interview: "Design typeahead search for a search box" (interview)

### Topic: Search at Scale (search-at-scale, advanced)
Sharding an index across nodes and merging scatter-gather results without one slow shard stalling every query.
- Why one index eventually must be sharded (concept)
- Sharding an index: partitioning documents across nodes (concept)
- Diagram: scatter-gather — query fanned out to shards, results merged (diagram)
- Replicas for search: read scaling and availability (concept)
- Merging and re-ranking results from multiple shards (concept)
- Compare: single large index vs many small shards on latency and relevance (compare)
- Pitfall: a scatter-gather query where one slow shard delays every query (pitfall)
- Interview: "How would Elasticsearch handle a billion-document index?" (interview)

### Topic: Search Index Freshness (search-index-freshness, intermediate)
Keeping a search index in sync with the source of truth, and living with the lag when it isn't.
- Batch reindexing vs near-real-time indexing (compare)
- Diagram: a write path that updates the DB and the search index (diagram)
- Keeping the index in sync: dual writes vs CDC-driven indexing (concept)
- Indexing lag: why search results can trail the source of truth (concept)
- Full reindex vs incremental reindex, and when each is needed (concept)
- Pitfall: dual writes to DB and index falling out of sync silently (pitfall)
- Interview: "A newly-created post doesn't show up in search yet — why?" (interview)

---

<!-- expert-tier additions (search-indexing) -->

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

## Group: Observability (observability)

*logs/metrics/traces, SLI/SLO*

> HLD-view boundary: this group covers what to design **into** a system so it's observable, and how observability data (SLI/SLO, traces) feeds design decisions in an interview. Hands-on tooling and ops practice (Prometheus/Grafana setup, alert-pipeline plumbing, runbooks/on-call rotations) belongs to `observability-ops` in Area 10 — cross-link there, don't duplicate.

### Topic: Observability Fundamentals (observability-fundamentals, beginner)
Logs, metrics, and traces — the three pillars, and what each one actually answers.
- Why "is it working?" needs more than a green dashboard (concept)
- The three pillars: logs, metrics, traces — what each answers (concept)
- Diagram: the same incident seen through logs, metrics, and traces (diagram)
- Compare: logs vs metrics vs traces on cost, granularity, and use case (compare)
- Where observability fits in the design conversation, not just ops (concept)
- Pitfall: having logs but no way to correlate them across services (pitfall)
- Interview: "How would you know this system is unhealthy before users complain?" (interview)

### Topic: Metrics & SLIs/SLOs (metrics-and-slis-slos, intermediate)
Turning reliability into a number you can design and negotiate around.
- SLI, SLO, SLA: the difference and why it matters (concept)
- Choosing good SLIs: latency, error rate, availability, throughput (concept)
- Diagram: an SLO budget burning down over a month (diagram)
- Error budgets: turning reliability into a number you can spend (concept)
- Compare: user-facing SLIs vs internal system metrics (compare)
- Pitfall: an SLO with no teeth — nothing changes when it's breached (pitfall)
- Interview: "What SLOs would you set for this API?" (interview)

### Topic: Distributed Tracing (distributed-tracing, advanced)
Following one request across many services to find which hop is actually slow.
- Why a single request's path across services needs its own tool (concept)
- Traces, spans, and parent-child relationships (concept)
- Diagram: one trace spanning five services, with one slow span highlighted (diagram)
- Context propagation: carrying a trace ID across service boundaries (concept)
- Sampling: tracing everything vs tracing a representative slice (concept)
- Compare: tracing overhead vs debugging value at different sample rates (compare)
- Pitfall: a trace that breaks because one service drops the propagated headers (pitfall)
- Interview: "A request is slow somewhere across six services — how do you find where?" (interview)

### Topic: Logging at Scale (logging-at-scale, intermediate)
Structured, correlated logs aggregated across many hosts into one searchable store.
- Structured logging vs free-text logs (concept)
- Correlation IDs: tying one request's logs together across services (concept)
- Diagram: log aggregation pipeline from many hosts into one searchable store (diagram)
- Log levels and sampling: keeping volume/cost under control (concept)
- Compare: centralized log aggregation vs per-host log files (compare)
- Pitfall: logging PII or secrets into a shared, widely-accessible log store (pitfall)
- Interview: "How do you debug an error report with no other context?" (interview)

### Topic: Alerting & On-Call Design (alerting-and-on-call-design, intermediate)
Designing alerts around user-facing symptoms so paging stays meaningful instead of constant noise.
- Alert on symptoms (user impact), not every possible cause (concept)
- Diagram: symptom-based alert vs cause-based alert, same incident (diagram)
- Setting thresholds that catch real problems without noise (concept)
- Alert fatigue: what happens when everything pages (concept)
- Compare: paging alerts vs ticket-queue alerts vs dashboards-only (compare)
- Pitfall: an alert that fires constantly and gets silently muted (pitfall)
- Interview: "What would you actually page a human for in this system?" (interview)

### Topic: Designing for Observability (designing-for-observability, advanced)
Building instrumentation into a design from day one instead of bolting it on after an incident.
- Designing observability in, not bolting it on after an incident (concept)
- Health checks and readiness/liveness endpoints (concept)
- Diagram: where instrumentation hooks sit in a request's path (diagram)
- What to instrument on day one: golden signals (latency, traffic, errors, saturation) (concept)
- Compare: minimal-viable observability vs everything instrumented from day one (compare)
- Pitfall: an architecture diagram in the interview with zero observability drawn in (pitfall)
- Interview: "Walk me through how you'd know if this new service is healthy" (interview)

---

<!-- expert-tier additions (observability) -->

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

---

# Phase E — High-Level Design: case studies

## Group: Core Systems (hld-cases-core)

*The fundamentals bank — small, self-contained systems that each isolate one hard distributed-systems problem.*

### Topic: Design a URL Shortener (design-url-shortener, beginner)
The classic first system design problem — encoding, redirection, and a cache in front of a hot mapping table, plus the abuse and analytics surface interviewers always probe.
- The prompt: shorten a URL, redirect on visit, at web scale (overview)
- Functional & non-functional requirements: custom aliases, expiry, redirect latency; non-goal: a full analytics dashboard (concept)
- Back-of-envelope: billions of stored URLs, ~100:1 read:write ratio, QPS and storage growth over 5 years (concept)
- The API surface: POST /shorten {longUrl, alias?, ttl?}, GET /{code} → redirect, DELETE /{code} (concept)
- Compare: counter-based vs hash-based short-code generation — collisions, predictability, reversibility (compare)
- The Key Generation Service: pre-generating unique keys offline so writes never collide-and-retry under load (concept)
- Data model and sharding the mapping table by short-code hash across many DB nodes (concept)
- Diagram: high-level architecture — API, KGS, sharded DB, cache, redirect path (diagram)
- Caching the hot redirects: cache-aside with TTL, and why redirects are almost all cache hits (concept)
- Compare: 301 vs 302 redirect — browser/CDN caching offloads load, but a cached 301 makes analytics and re-routing blind (compare)
- Custom aliases and collision handling on the write path (concept)
- Compare: expiry/TTL cleanup — lazy deletion on read vs a background reaper sweep (compare)
- Rate limiting and abuse prevention: throttling link creation, blocking malicious/phishing targets (concept)
- Analytics pipeline: async click-event capture off the redirect's critical path (concept)
- The bottleneck: a hot shard or cache-miss storm on a viral short link, and how it scales past it (concept)
- Pitfall: using an auto-increment ID directly as the short code, leaking volume and enabling enumeration (pitfall)
- Interview: the follow-ups — malicious-URL detection, link previews, multi-region writes (interview)
- Summary: encode + shard + cache + KGS, with the redirect as the only latency-critical path (concept)
— cross-link: partitioning-and-sharding, distributed-rate-limiting, design-unique-id-generator

### Topic: Design a Pastebin (design-pastebin, beginner)
Storing and serving arbitrary-size text blobs cheaply, including the read stampede when one paste goes viral.
- The prompt: paste text, get a shareable link, set expiry/visibility (overview)
- Functional & non-functional requirements: size limits, retention, public vs unlisted (concept)
- Back-of-envelope: paste sizes, read:write ratio, storage growth over a year (concept)
- The API surface: create paste, fetch paste, delete/expire (concept)
- Data model: blob storage for content vs a small metadata row per paste (compare)
- Diagram: high-level architecture — API, object store, metadata DB, cache (diagram)
- Why this isn't just a URL shortener: variable-size payloads change the storage answer (concept)
- Handling a viral paste: read stampede on one hot key (concept)
- Diagram: cache-aside in front of the hot paste, with request coalescing (diagram)
- Expiry at scale: TTL sweep vs lazy deletion on read (compare)
- Pitfall: storing every paste inline in the DB row, bloating the primary store (pitfall)
- Interview: the follow-ups — syntax highlighting, private pastes, abuse/rate limits (interview)
— cross-link: object-and-blob-storage, cache-penetration-and-negative-caching

### Topic: Design a Unique ID Generator (design-unique-id-generator, intermediate)
Generating unique, roughly-sortable IDs across many machines without a central bottleneck — clock drift and worker-ID assignment are where this actually breaks.
- The prompt: generate unique, roughly time-sortable IDs across many machines with no central bottleneck (overview)
- Functional & non-functional requirements: uniqueness, k-sortability, per-node throughput; non-goal: strict global ordering (concept)
- Back-of-envelope: IDs/sec needed platform-wide vs IDs/sec a single sequence counter can sustain (concept)
- The API surface: generateId(), and what callers can rely on — unique, roughly ordered, not sequential (concept)
- Compare: UUID vs DB auto-increment vs Snowflake-style IDs — index locality, size, sortability (compare)
- Snowflake-style anatomy: timestamp + machine ID + sequence bits (concept)
- Diagram: anatomy of a 64-bit Snowflake ID and the bit-allocation trade-offs (diagram)
- Worker-ID assignment: static config vs a coordination service handing out IDs on startup (concept)
- Compare: centralized ID-allocation service vs fully decentralized generation (compare)
- Clock drift and NTP skew: what happens when a node's clock jumps backward (concept)
- Handling clock rollback: refuse to generate or wait, and why either beats reusing a timestamp (concept)
- Code: a simplified Snowflake ID generator with sequence rollover per millisecond (code)
- The bottleneck: the sequence-bits ceiling on IDs/ms per machine, and scaling by adding machine-ID bits or nodes (concept)
- Pitfall: two machines assigned the same machine ID, silently generating colliding IDs (pitfall)
- Pitfall: a node restarting with a rolled-back clock, generating an ID that sorts before earlier ones (pitfall)
- Interview: the follow-ups — why not just a database sequence, and when UUIDs are actually fine (interview)
- Interview: the follow-ups — keeping IDs k-sortable across a multi-region deployment (interview)
- Summary: timestamp for order, machine ID for uniqueness, sequence for burst throughput (concept)
— cross-link: consensus-basics, partitioning-and-sharding

### Topic: Design a Key-Value Store (design-key-value-store, advanced)
Building a Dynamo-style KV store itself — partitioning, replication, and tunable consistency, not just using one.
- The prompt: put(key, value)/get(key) at massive scale with high availability (overview)
- Functional & non-functional requirements: durability, availability vs consistency target (concept)
- Back-of-envelope: keyspace size, request rate, replication factor and its storage multiplier (concept)
- The API surface: put/get/delete, and what a versioned value looks like (concept)
- Data model: consistent hashing ring for partitioning keys across nodes (concept)
- Diagram: the hash ring with virtual nodes and key ownership (diagram)
- Replication: writing to N replicas and reading from R with quorum (concept)
- Diagram: a write's path across the ring — coordinator, replicas, acks (diagram)
- Tunable consistency: read-your-writes vs eventual, and the R/W/N knobs (compare)
- Conflict resolution when replicas diverge: vector clocks vs last-write-wins (compare)
- The bottleneck: hot partitions from skewed key access (concept)
- Pitfall: rebalancing the ring naively, causing a mass key migration (pitfall)
- Interview: "Design a distributed key-value store like DynamoDB" (interview)
— cross-link: partitioning-and-sharding, quorum-systems, consensus-basics

### Topic: Design a Distributed Cache (design-distributed-cache, advanced)
A cache that is itself a distributed system — sharding, invalidation propagation, and the hot-key problem at cluster scale.
- The prompt: a shared cache tier in front of a database, serving many services (overview)
- Functional & non-functional requirements: hit ratio target, staleness tolerance, eviction policy (concept)
- Back-of-envelope: working-set size vs node memory, number of shards needed (concept)
- The API surface: get/set/delete plus TTL and versioned invalidation (concept)
- Sharding keys across cache nodes with consistent hashing (concept)
- Diagram: client routing to the right shard, with a hash ring (diagram)
- Cache invalidation across nodes: TTL vs explicit invalidation broadcast (compare)
- The hot-key problem: one key exceeding a single node's capacity (concept)
- Diagram: hot-key mitigation — local caching plus key-splitting in front of the shard (diagram)
- Node failure and rebalancing without a stampede on the database (concept)
- Pitfall: a full cache-cluster restart causing a thundering herd on the DB (pitfall)
- Interview: "Design Memcached/Redis Cluster from scratch" (interview)
— cross-link: distributed-caching, cache-invalidation, eviction-policies

### Topic: Design a Rate Limiter Service (design-rate-limiter-service, advanced)
Rate limiting as a shared, low-latency service every other system calls — the distributed service around the algorithm, not the algorithm itself.
- The prompt: a central service any microservice can ask "is this allowed?" (overview)
- Functional & non-functional requirements: per-user/per-API limits, latency budget, config changes without redeploy (concept)
- Back-of-envelope: check QPS across all callers vs the limiter's own capacity (concept)
- The API surface: checkAndIncrement(key, limit, window) (concept)
- Data model: where counters live — in-memory per node vs a shared store (compare)
- Diagram: architecture — client SDK, limiter service, shared counter store (diagram)
- Sharing counters across limiter instances without a single point of contention (concept)
- Propagating limit-config changes globally with low delay (concept)
- Diagram: request path through the limiter under normal and overload conditions (diagram)
- The bottleneck: the shared counter store becoming hotter than the service it protects (concept)
- Trade-off: strict global accuracy vs relaxed per-node approximate limits (compare)
- Pitfall: the limiter itself becoming a single point of failure for every downstream call (pitfall)
- Interview: "Design a rate limiter usable by every service in the company" (interview)
— cross-link: distributed-rate-limiting, rate-limiting-algorithms

### Topic: Design a Leaderboard (design-leaderboard, intermediate)
Real-time ranked scores for millions of users — sorted-set structures and rank queries, not a sorted table scan.
- The prompt: show a user's rank and the top N out of millions of scores, updated live (overview)
- Functional & non-functional requirements: update frequency, rank-query latency, tie handling (concept)
- Back-of-envelope: score updates per second vs rank-read QPS (concept)
- The API surface: updateScore(user, delta), getRank(user), getTopN() (concept)
- Data model: sorted set (skip list) vs a B-tree index vs periodic batch ranking (compare)
- Diagram: a sharded sorted-set leaderboard with a merge step for global rank (diagram)
- Getting a user's rank in a sharded leaderboard without a full scan (concept)
- Tie-breaking rules and their effect on rank stability (concept)
- The bottleneck: a single global leaderboard node under write pressure (concept)
- Trade-off: exact real-time rank vs periodically refreshed approximate rank (compare)
- Pitfall: recomputing the full sorted order on every single score update (pitfall)
- Interview: "Design a real-time leaderboard for a game with 100M players" (interview)
— cross-link: nosql-data-models, partitioning-and-sharding

### Topic: Design a Distributed Counter (design-distributed-counter, advanced)
Counting billions of increments (views, likes) without turning one row into the system's hottest lock.
- The prompt: count events (views, likes) at a rate no single DB row can absorb (overview)
- Functional & non-functional requirements: exactness vs approximate-is-fine, read latency for the count (concept)
- Back-of-envelope: increments/sec on a single hot object vs a single row's write ceiling (concept)
- The API surface: increment(key), getCount(key) — and what "get" actually returns (concept)
- Sharded counters: splitting one logical counter into N physical shards (concept)
- Diagram: writes fan out to shards, reads sum across shards (diagram)
- In-memory batching before flushing to durable storage (concept)
- Compare: strongly consistent single-row counter vs eventually-consistent sharded counter (compare)
- The bottleneck: shard count vs read-time aggregation cost (concept)
- Approximate counting (HyperLogLog-style) when exact counts aren't required (concept)
- Pitfall: a "trending" counter read on every page view, redoing the sum each time (pitfall)
- Interview: "Design a view counter for a video that gets 10M views in an hour" (interview)
— cross-link: partitioning-and-sharding, eviction-policies

---

## Group: Social & Messaging Systems (hld-cases-social)

*Feed, chat, and graph systems — the hard problems are fan-out shape, ordering, and graph scale, not any single feature.*

### Topic: Design a News Feed (design-news-feed, advanced)
Fan-out-on-write vs fan-out-on-read, and the hybrid that survives the celebrity problem.
- The prompt: show each user a feed of everyone they follow, ordered and fresh (overview)
- Functional & non-functional requirements: feed latency, staleness tolerance; non-goal: owning the ranking model itself (concept)
- Back-of-envelope: posts/sec, average follower count vs a celebrity's follower count, feed reads/sec (concept)
- The API surface: publish(post), getFeed(userId, cursor) (concept)
- Data model: a precomputed per-user feed store vs a raw post table fanned out at read time (concept)
- Fan-out-on-write (push): precomputing every follower's feed (concept)
- Fan-out-on-read (pull): assembling the feed at read time (concept)
- Diagram: push vs pull fan-out side by side (diagram)
- The celebrity problem: why pure push breaks for high-follower accounts (concept)
- Hybrid fan-out: push for most, pull-and-merge for celebrities at read time (concept)
- Compare: push vs pull vs hybrid on latency, storage, write cost (compare)
- Ranking the feed: chronological vs relevance score, and where the ranking model plugs in (concept)
- Diagram: end-to-end architecture — write path and read path (diagram)
- The bottleneck: fan-out write amplification when a mid-size account suddenly goes viral (concept)
- Pitfall: recomputing the entire feed on every read at Twitter scale (pitfall)
- Interview: the follow-ups — feed staleness and cache invalidation on edit/delete (interview)
- Interview: the follow-ups — pagination cursors that stay stable while new posts keep arriving (interview)
- Summary: hybrid fan-out plus a pluggable ranking stage (concept)
— cross-link: ml-system-design, design-follow-graph-service

### Topic: Design a Chat System (design-chat-system, advanced)
Real-time delivery, per-conversation ordering, and presence at messaging-app scale.
- The prompt: 1:1 and group messaging with reliable, ordered, real-time delivery (overview)
- Functional & non-functional requirements: at-least-once delivery, per-conversation ordering; non-goal: building a video-call layer (concept)
- Back-of-envelope: concurrent connections, messages/sec, the fan-out multiplier for group chats (concept)
- The API surface: sendMessage(), ackDelivery(), subscribe(conversationId) over a persistent connection (concept)
- Compare: real-time transport — WebSockets vs long polling vs push notifications (compare)
- Diagram: connection topology — clients, gateway servers, message store (diagram)
- Data model: message storage and per-conversation ordering via sequence numbers, not wall-clock time (concept)
- Delivery and read receipts: tracking per-recipient state without a write per recipient per message (concept)
- Online presence: heartbeat, last-seen, fan-out of status changes (concept)
- Compare: group chat fan-out vs 1:1 delivery — write amplification in large groups (compare)
- Diagram: message send path from sender to all recipients across gateway servers (diagram)
- Offline delivery: queuing for disconnected clients and replay on reconnect (concept)
- The bottleneck: a single connection server hot-spotting on a popular group's fan-out (concept)
- Pitfall: a single connection server becoming a hot spot for popular groups (pitfall)
- Pitfall: assuming exactly-once delivery and not deduplicating client-side on retry (pitfall)
- Interview: the follow-ups — end-to-end encryption, and where server-side message search then breaks (interview)
- Interview: the follow-ups — multi-device sync when one account has several open connections (interview)
- Summary: gateway fan-out plus per-conversation sequencing is the whole system (concept)
— cross-link: design-presence-service, design-notification-system

### Topic: Design a Notification System (design-notification-system, intermediate)
Fanning a single event out across channels without spamming or ignoring user preferences.
- The prompt: fan a single triggering event out across push/email/SMS reliably (overview)
- Functional & non-functional requirements: per-channel delivery SLA, per-user preferences; non-goal: the marketing-campaign UI (concept)
- Back-of-envelope: events/sec, users targeted per broadcast event, notifications/sec at peak (concept)
- The API surface: sendNotification(userId, template, channelHints), preference update API (concept)
- Data model: templates, per-user channel preferences, and a delivery-log table for dedup (concept)
- Diagram: notification pipeline — trigger, template render, channel dispatch (diagram)
- Fan-out for a notification that targets millions of users in one event (concept)
- Deduplication and throttling: avoiding notification spam from retries or duplicate triggers (concept)
- Respecting user preferences and quiet hours before dispatch (concept)
- Retry and fallback across channels — push fails, fall back to email (concept)
- Compare: synchronous send vs queued/async send (compare)
- Diagram: end-to-end architecture — event source, queue, worker pool, per-channel provider adapters (diagram)
- The bottleneck: a third-party channel provider (APNs/SMS gateway) rate-limiting the whole system (concept)
- Pitfall: a retry storm re-sending the same notification to every user (pitfall)
- Pitfall: no dedup key, so one triggering event double-enqueues under at-least-once delivery (pitfall)
- Interview: the follow-ups — getting exactly-once-feeling delivery on top of at-least-once infra (interview)
- Interview: the follow-ups — prioritizing a security-alert OTP ahead of a marketing blast in the same queue (interview)
- Summary: template + preference + queue + per-channel adapter, with dedup as the safety net (concept)
— cross-link: messaging-fundamentals, design-presence-service

### Topic: Design a Presence Service (design-presence-service, intermediate)
Fanning "who's online" out to millions of watchers cheaply, when the state changes constantly and matters least when nobody's looking.
- The prompt: show accurate online/last-seen status to anyone watching a user (overview)
- Functional & non-functional requirements: staleness tolerance, watcher fan-out size, mobile battery cost (concept)
- Back-of-envelope: concurrent connections vs status-change rate vs watchers per user (concept)
- The API surface: heartbeat(), subscribe(userId), status-change events (concept)
- Data model: ephemeral state in memory (not the durable DB) with a short TTL (concept)
- Diagram: heartbeat path — client, gateway, presence store, subscriber fan-out (diagram)
- Fan-out of one status change to a large, dynamic watcher set (concept)
- Diagram: publish-subscribe topology for status updates (diagram)
- Handling flapping connections without spamming online/offline toggles (concept)
- Compare: push-based fan-out vs watchers polling on demand (compare)
- Pitfall: writing every heartbeat to durable storage, overwhelming the DB (pitfall)
- Interview: "Design the online-status indicator for a messaging app" (interview)
— cross-link: design-chat-system, messaging-fundamentals

### Topic: Design a Comment & Like System (design-comment-like-system, intermediate)
Aggregating a huge number of small writes onto one hot object (a viral post's like count) without that object becoming a bottleneck.
- The prompt: attach likes and threaded comments to any post, at any scale (overview)
- Functional & non-functional requirements: like-count accuracy, comment ordering, edit/delete (concept)
- Back-of-envelope: likes/sec on a single viral post vs a single row's write ceiling (concept)
- The API surface: like(postId, userId), comment(postId, text), getCounts(postId) (concept)
- Data model: comments as a tree/adjacency list vs a flat list with parentId (compare)
- Diagram: write path for a like — dedup by user, async counter increment (diagram)
- Deduplicating repeated likes from the same user without a full scan (concept)
- The hot object: a single post absorbing millions of likes in minutes (concept)
- Sharded counters and async aggregation for the visible like count (concept)
- Diagram: comment thread rendering — pagination and reply nesting (diagram)
- Pitfall: incrementing a single like_count column directly on the posts table (pitfall)
- Interview: "Design the like/comment system for a viral post" (interview)
— cross-link: design-distributed-counter, partitioning-and-sharding

### Topic: Design a Follow Graph Service (design-follow-graph-service, advanced)
Storing and querying a directed graph with hundreds of millions of edges — follower lists and mutuals are graph-traversal problems, not row lookups.
- The prompt: follow/unfollow, list followers, list following, check mutual (overview)
- Functional & non-functional requirements: read-heavy skew, celebrity fan-out of edges, count consistency (concept)
- Back-of-envelope: edges for a billion-user graph, and read QPS for follower lists (concept)
- The API surface: follow(a,b), unfollow(a,b), getFollowers(a), isFollowing(a,b) (concept)
- Data model: adjacency-list tables vs a native graph store (compare)
- Diagram: sharding the edge table by follower vs by followee, and why it matters (diagram)
- The celebrity problem again, from the graph side: a followee with 100M follower-edges (concept)
- Precomputed follower-count vs counting edges live (compare)
- Diagram: fan-out of a new post using this graph — where it hands off to news feed (diagram)
- The bottleneck: fetching "who follows both A and B" without a full graph engine (concept)
- Pitfall: storing follows only as forward edges, making "who follows me" an expensive scan (pitfall)
- Interview: "Design the follow/follower system behind a social network" (interview)
— cross-link: design-news-feed, nosql-data-models, ml-system-design (who-to-follow ranking)

### Topic: Design a Content Moderation Pipeline (design-content-moderation-pipeline, advanced)
An async, multi-stage pipeline that screens user content before and after it's live — the pipeline and feedback loop are the hard part, not the classifier.
- The prompt: screen every post/comment/image for policy violations, at platform scale (overview)
- Functional & non-functional requirements: pre-publish vs post-publish screening, latency budget, appeal flow (concept)
- Back-of-envelope: content volume vs review-queue throughput vs human reviewer capacity (concept)
- The API surface: submitForReview(content), reportContent(id), reviewDecision(id, verdict) (concept)
- Pipeline design: automated classifier pass, then a human-review queue for borderline cases (concept)
- Diagram: content flow — ingest, automated filters, priority queue, human review, action (diagram)
- Prioritizing the review queue: virality risk vs first-come-first-served (concept)
- Compare: block-before-publish vs publish-then-remove, and their different risk profiles (compare)
- Feedback loop: reviewer decisions retraining/tuning the automated filters (concept)
- Diagram: appeal flow when a user disputes a takedown (diagram)
- Pitfall: a synchronous moderation check on the publish path, adding latency to every post (pitfall)
- Interview: "Design a system to detect and act on abusive content in real time" (interview)
— cross-link: ml-system-design, event-driven-architecture, abuse-and-antifraud-in-design

### Topic: Design an Ephemeral Stories System (design-ephemeral-stories-system, intermediate)
Content that must vanish after 24 hours at massive scale, plus per-viewer view-tracking — expiry and read-receipts are the hard parts, not the media itself.
- The prompt: post a photo/video that disappears after 24h, and see who viewed it (overview)
- Functional & non-functional requirements: exact vs approximate expiry timing, viewer-list size (concept)
- Back-of-envelope: stories created/day, views/story, total ephemeral storage in flight (concept)
- The API surface: postStory(media, ttl), viewStory(id, viewerId), getViewers(id) (concept)
- Data model: TTL-indexed storage vs a background expiry sweep (compare)
- Diagram: expiry path — lazy deletion on read plus a low-priority background reaper (diagram)
- Tracking viewers per story without a hot write on every single view (concept)
- Diagram: story ring fan-out to followers, similar to but simpler than a full feed (diagram)
- The bottleneck: expiring millions of stories at the same wall-clock moment (concept)
- Compare: deleting the media immediately vs soft-deleting and reaping later (compare)
- Pitfall: a cron job scanning the entire stories table every minute to find expired rows (pitfall)
- Interview: "Design Instagram/Snapchat Stories" (interview)
— cross-link: design-comment-like-system, object-and-blob-storage

*Considered and cut:* a standalone Twitter-timeline case study (same fan-out lesson as News Feed with a
different logo); a generic Instagram photo-feed case study (same lesson again); a poll/voting case study
(same hot-object-counter lesson as Comment & Like); a standalone direct-messaging case study (Chat System
already owns 1:1 delivery).

---

## Group: Media & Streaming Systems (hld-cases-media)

*Video, audio, image, and file delivery — each system has a different storage shape (huge-few-files vs tiny-many-files) and a different latency contract (live vs on-demand).*

### Topic: Design a Video Streaming Platform (design-video-streaming-platform, advanced)
Upload, transcode, and adaptive-bitrate delivery of video — the rendition pipeline and playback protocol, with global CDN strategy owned by the dedicated delivery-network case study.
- The prompt: accept uploads, transcode them, and stream video adaptively to any device (overview)
- Functional & non-functional requirements: upload SLA, startup latency; non-goal: the global CDN/multi-region strategy, covered separately (concept)
- Back-of-envelope: uploads/day, renditions per video, storage multiplier, concurrent viewers (concept)
- The API surface: initiateUpload(), getManifest(videoId), a short-lived playback session token (concept)
- Diagram: upload → transcode pipeline → storage → CDN → playback (diagram)
- Transcoding into multiple resolutions/bitrates: the rendition ladder (concept)
- Adaptive bitrate streaming: how the player picks a quality in real time from buffer/bandwidth signals (concept)
- Chunked delivery (HLS/DASH) instead of one giant file, and why that's what enables ABR (concept)
- Compare: on-the-fly transcoding vs precomputed renditions (compare)
- Data model: object storage for video segments, a DB for manifest/rendition metadata (concept)
- The bottleneck: a transcode-queue backlog during an upload spike, delaying time-to-availability (concept)
- Compare: precomputing every rendition upfront vs lazily transcoding rarely-watched resolutions (compare)
- Pitfall: serving video directly from origin without a CDN (pitfall)
- Pitfall: transcoding every rendition before publishing anything, delaying time-to-first-playback (pitfall)
- Interview: the follow-ups — recommendations and view-count accuracy living outside this pipeline (interview)
- Interview: the follow-ups — supporting live streaming without rebuilding the whole pipeline (interview)
- Summary: upload triggers a rendition ladder; chunking and ABR make playback resilient to bad networks (concept)
— cross-link: design-video-delivery-network, design-transcode-pipeline, design-live-streaming-platform

### Topic: Design a Global Video Delivery Network (design-video-delivery-network, expert)
Netflix-scale delivery — deciding which titles live on which edge caches and failing over across CDNs, not how a single video gets transcoded.
- The prompt: serve a catalog of millions of titles to a global audience with minimal buffering (overview)
- Functional & non-functional requirements: startup latency target, rebuffer rate, regional demand skew (concept)
- Back-of-envelope: catalog size vs edge cache capacity vs origin egress if every request missed (concept)
- The API surface: a playback manifest request resolving to the nearest healthy edge (concept)
- Cache placement: which titles get pre-positioned at which edge locations (concept)
- Diagram: origin, regional caches, edge caches, and the request path for a play (diagram)
- Predictive pre-positioning: pushing new/trending titles to edges before demand hits (concept)
- Compare: single-CDN vs multi-CDN with real-time routing by health and cost (compare)
- Diagram: multi-CDN failover when one CDN degrades in a region (diagram)
- The bottleneck: origin overload when a cache-miss storm hits an under-cached title (concept)
- Trade-off: cache hit ratio vs storage cost of over-provisioning every edge (compare)
- Pitfall: routing purely by geography, ignoring real-time CDN health/cost signals (pitfall)
- Interview: "Design the CDN strategy behind a global video streaming service" (interview)
— cross-link: design-video-streaming-platform, cdn-and-edge-caching, multi-region-topologies

### Topic: Design an Audio Streaming Service (design-audio-streaming-service, advanced)
A catalog of hundreds of millions of small files with high-QPS random access and offline sync — the opposite storage shape from video's few-huge-files problem.
- The prompt: stream any of hundreds of millions of songs instantly, plus offline downloads (overview)
- Functional & non-functional requirements: startup latency, offline license expiry, gapless playback (concept)
- Back-of-envelope: catalog size, concurrent streams, per-track storage vs video's per-title storage (compare)
- The API surface: getStreamUrl(trackId), download(trackId), cross-device playlist sync (concept)
- Data model: small immutable audio objects plus a metadata/catalog service (concept)
- Diagram: storage and delivery architecture — object store, CDN, metadata DB (diagram)
- Offline downloads: syncing licensed content to a device and expiring it without connectivity (concept)
- Diagram: cross-device playlist and playback-position sync (diagram)
- The bottleneck: metadata/catalog lookups at far higher QPS than video's per-title lookups (concept)
- Compare: pre-computing personalized playlists vs computing them on read (compare)
- Pitfall: treating audio like small video — over-engineering ABR for files that fit in a phone's cache (pitfall)
- Interview: "Design the backend for a music streaming app with offline mode" (interview)
— cross-link: design-video-streaming-platform, object-and-blob-storage, ml-system-design (playlist ranking)

### Topic: Design an Image Hosting Service (design-image-hosting-service, intermediate)
Content-addressable storage for billions of small immutable blobs — dedup and on-the-fly derivatives are the hard parts, not the upload form.
- The prompt: upload an image, get a URL, serve it fast at many sizes (overview)
- Functional & non-functional requirements: upload volume, read:write ratio, supported sizes/formats (concept)
- Back-of-envelope: images/day, storage growth, derivative-size multiplier per original (concept)
- The API surface: upload(image), getUrl(id, size), delete(id) (concept)
- Content-addressable storage: hashing image bytes to dedup identical uploads (concept)
- Diagram: upload path — hash, dedup check, store original, enqueue derivative generation (diagram)
- On-the-fly resizing vs precomputing common sizes at upload time (compare)
- Diagram: read path — CDN, cache, on-the-fly resize fallback (diagram)
- The bottleneck: a burst of resize requests for sizes that weren't precomputed (concept)
- Serving via CDN with cache keys that include the requested size/format (concept)
- Pitfall: hashing only the file name for dedup instead of the content, missing true duplicates (pitfall)
- Interview: "Design an image hosting service like Imgur" (interview)
— cross-link: object-and-blob-storage, cdn-and-edge-caching

### Topic: Design a File Sync Service (design-file-sync-service, advanced)
Delta sync of files across devices that go offline — chunking and conflict resolution are the hard parts, not storing a file.
- The prompt: keep a folder in sync across a laptop, phone, and the cloud, even offline (overview)
- Functional & non-functional requirements: max file size, offline edit window, conflict frequency (concept)
- Back-of-envelope: files per user, change frequency, bandwidth if every edit re-uploaded the whole file (concept)
- The API surface: uploadChunk(fileId, chunk), getChanges(since), resolveConflict(fileId) (concept)
- Chunking files into fixed or content-defined blocks for delta sync (concept)
- Diagram: block-level diff — only changed chunks travel over the wire (diagram)
- Metadata service (file tree, versions) separate from block storage (concept)
- Diagram: sync architecture — client watchers, metadata service, block store (diagram)
- Conflict resolution when two devices edit the same file offline (concept)
- Compare: this delta-sync/offline model vs the collaborative editor's live-merge model (compare)
- The bottleneck: the metadata service under a large folder with frequent small changes (concept)
- Pitfall: re-uploading the entire file on every save instead of just the changed blocks (pitfall)
- Interview: "Design Dropbox — file sync across devices" (interview)
— cross-link: design-collaborative-editor, object-and-blob-storage, conflict-resolution

### Topic: Design a Live Streaming Platform (design-live-streaming-platform, expert)
Sub-second-latency ingest-to-viewer pipeline for content that doesn't exist until the moment it's watched — the opposite of VOD's precompute-then-serve model.
- The prompt: a streamer broadcasts live, thousands watch with minimal delay (overview)
- Functional & non-functional requirements: end-to-end latency budget, concurrent viewer spikes, live chat (concept)
- Back-of-envelope: ingest bitrate, fan-out viewers per stream, total egress during a spike (concept)
- The API surface: startStream(), ingest endpoint, a playback manifest that updates as segments arrive (concept)
- Live transcoding: producing renditions in real time instead of precomputing them (concept)
- Diagram: ingest → real-time transcode → low-latency CDN distribution → viewers (diagram)
- Chunked low-latency delivery: small segment windows vs VOD's larger chunks (compare)
- Diagram: viewer fan-out during a spike — one popular stream, huge simultaneous join (diagram)
- The bottleneck: transcoding falling behind ingest under load, causing latency to climb (concept)
- Live chat at stream scale, fanning out to viewers without lagging the video (concept)
- Trade-off: lower latency vs playback stability (larger buffers smooth network jitter) (compare)
- Pitfall: applying the VOD precompute-then-cache model to live, adding minutes of delay (pitfall)
- Interview: "Design a live streaming platform like Twitch" (interview)
— cross-link: design-video-streaming-platform, design-chat-system, load-balancing-fundamentals

### Topic: Design a Media Transcode Pipeline (design-transcode-pipeline, intermediate)
The general async job system behind "process every uploaded photo/video into derivatives" — orchestration and idempotent retries are the lesson, not any one codec.
- The prompt: any uploaded media file needs one or more derivative jobs run on it (overview)
- Functional & non-functional requirements: job types, priority (user-facing vs batch), retry budget (concept)
- Back-of-envelope: uploads/sec vs worker throughput per job type (concept)
- The API surface: submitJob(mediaId, jobType), job status callback/webhook (concept)
- Data model: a job queue plus a job-state table keyed by mediaId + jobType (concept)
- Diagram: pipeline — upload triggers job, queue, worker pool, output storage, status update (diagram)
- Idempotent retries: a worker crashing mid-job must not corrupt or duplicate output (concept)
- Prioritization: a user waiting on a thumbnail vs a batch re-encode running overnight (compare)
- Diagram: worker pool autoscaling against queue depth (diagram)
- The bottleneck: one job type (e.g. 4K transcode) starving the queue for cheap jobs (thumbnails) (concept)
- Pitfall: no idempotency key, so a retried job double-charges storage or emits duplicate output (pitfall)
- Interview: "Design the system that processes every file a user uploads" (interview)
— cross-link: design-distributed-job-scheduler, messaging-fundamentals, backpressure-and-dead-letter-handling

---

## Group: Marketplace & Transactional Systems (hld-cases-marketplace)

*Two- and three-sided marketplaces plus money-movement systems — correctness under contention (double-booking, double-charging, unfair matching) is the shared hard problem, expressed differently each time.*

### Topic: Design a Ticket Booking System (design-ticket-booking-system, advanced)
Preventing double-booking under heavy contention for a fixed, scarce inventory of seats.
- The prompt: sell a fixed set of seats for an event without ever double-selling one (overview)
- Functional & non-functional requirements: hold duration, zero overselling tolerance; non-goal: the seating-chart UI itself (concept)
- Back-of-envelope: seats per event, concurrent requests in the first seconds of an on-sale, hold-table write rate (concept)
- The API surface: searchSeats(), holdSeat(seatId), confirmBooking(holdId), releaseHold() (concept)
- Data model: a seat-status table (available/held/sold) keyed for row-level contention, not a single counter (concept)
- The core problem: preventing double-booking under concurrent requests for the same seat (concept)
- Compare: pessimistic locking vs optimistic concurrency for seat reservation (compare)
- Diagram: two users racing for the same seat, and how the lock resolves it (diagram)
- Temporary holds: reserving a seat during checkout without a permanent lock (concept)
- Handling a high-demand on-sale moment: queueing users, virtual waiting rooms (concept)
- Compare: database-level locking vs a distributed lock service (compare)
- Diagram: end-to-end booking flow — search, hold, pay, confirm (diagram)
- The bottleneck: row-level contention on the same handful of good seats at the on-sale instant, smoothed by an admission-controlled queue ahead of the DB (concept)
- Pitfall: releasing a seat hold only on success, leaking seats on abandoned checkouts (pitfall)
- Pitfall: no idempotency key on confirmBooking, so a client retry double-books or double-charges (pitfall)
- Interview: the follow-ups — fairness in the waiting room, FIFO vs random admission (interview)
- Interview: the follow-ups — handling a payment failure after a hold is taken, without leaking the seat (interview)
- Summary: row-level seat state plus a time-boxed hold is what makes double-booking impossible (concept)
— cross-link: design-hotel-booking-system, idempotency-and-exactly-once

### Topic: Design a Ride-Hailing System (design-ride-hailing-system, expert)
Real-time matching, dispatch, and surge pricing on top of a live location feed — the matching/pricing loop is the hard part, not finding nearby drivers.
- The prompt: rider requests a ride, gets matched to a nearby driver in seconds (overview)
- Functional & non-functional requirements: match latency target, cancellation handling, surge fairness (concept)
- Back-of-envelope: concurrent rides, location pings/sec per driver, matches/sec in a dense city (concept)
- The API surface: requestRide(), driverLocationUpdate(), acceptMatch() (concept)
- Data model: live driver locations (ephemeral, high-write) vs ride/trip records (durable) (compare)
- Diagram: architecture — location service, matching engine, trip service, pricing service (diagram)
- The matching algorithm: nearest-available driver vs balancing marketplace-wide efficiency (concept)
- Diagram: match loop — candidate drivers from the location index, scored, offered, accepted (diagram)
- Dynamic/surge pricing: computing a price multiplier from live supply/demand per zone (concept)
- Compare: greedy nearest-match vs batched matching for better marketplace efficiency (compare)
- The bottleneck: the matching engine during a demand spike (a concert letting out) (concept)
- Pitfall: matching purely by distance, ignoring driver heading/ETA and causing bad matches (pitfall)
- Interview: "Design the rider-driver matching system behind Uber" (interview)
— cross-link: design-proximity-service, quorum-systems, geo-routing-and-failover

### Topic: Design a Food Delivery System (design-food-delivery-system, advanced)
A three-sided marketplace (customer, restaurant, courier) with a real-time order state machine and batching — different from ride-hailing's point-to-point match.
- The prompt: order from a restaurant, a courier picks up and delivers it, all parties see live status (overview)
- Functional & non-functional requirements: prep-time estimates, courier assignment latency, order accuracy (concept)
- Back-of-envelope: concurrent orders, couriers online, orders/courier during a batching window (concept)
- The API surface: placeOrder(), updateOrderStatus(), assignCourier() (concept)
- Data model: an order state machine (placed → accepted → preparing → picked up → delivered) (concept)
- Diagram: three-sided data flow — customer app, restaurant app, courier app synced off one order record (diagram)
- Courier assignment: assign per order vs batch multiple orders into one courier's route (compare)
- Diagram: batching two nearby orders onto one courier trip (diagram)
- ETA prediction feeding both the customer app and the assignment decision (concept)
- The bottleneck: restaurant-side order acceptance lag during a lunch-hour spike (concept)
- Pitfall: syncing order status via client polling instead of push, causing stale statuses (pitfall)
- Interview: "Design a food delivery system connecting customers, restaurants, and couriers" (interview)
— cross-link: design-ride-hailing-system, event-driven-architecture, design-notification-system

### Topic: Design a Hotel Booking System (design-hotel-booking-system, intermediate)
Date-range inventory (room-nights, not single seats) searched across thousands of properties — a range-overlap problem, not a single-item lock.
- The prompt: search "rooms in city X, these dates", book one, avoid overselling (overview)
- Functional & non-functional requirements: search latency across many properties, overbooking policy (concept)
- Back-of-envelope: properties, room-nights of inventory, search QPS vs booking QPS (concept)
- The API surface: searchAvailability(city, dates), holdRoom(), confirmBooking() (concept)
- Data model: per-room-per-night availability rows vs a date-range calendar structure (compare)
- Diagram: search fan-out across properties, filtered by date-range availability (diagram)
- Preventing overselling a room for overlapping date ranges under concurrent bookings (concept)
- Compare: strict no-overbooking vs deliberate overbooking with a cancellation buffer (compare)
- Diagram: booking flow — hold, payment, confirm, release-on-timeout (diagram)
- The bottleneck: search fan-out latency across a large city with thousands of properties (concept)
- Pitfall: modeling inventory as a single "rooms available" counter instead of per-date rows (pitfall)
- Interview: "Design a hotel booking system like Booking.com" (interview)
— cross-link: design-ticket-booking-system, partitioning-and-sharding

### Topic: Design an E-Commerce Checkout System (design-ecommerce-checkout-system, advanced)
A distributed transaction across inventory, payment, and shipping that must be idempotent under retries — the saga is the hard part, not the shopping cart UI.
- The prompt: cart → checkout → confirmed order, touching inventory, payment, and shipping (overview)
- Functional & non-functional requirements: no double-charge, no oversell, checkout latency under flash-sale load (concept)
- Back-of-envelope: checkouts/sec in steady state vs a flash-sale spike (concept)
- The API surface: checkout(cartId), and the idempotency key that makes retries safe (concept)
- Data model: order as a saga of steps, each with its own compensating action (concept)
- Diagram: the saga — reserve inventory, charge payment, create shipment, or compensate on failure (diagram)
- Idempotency: a client retry after a timeout must not create a second order or a second charge (concept)
- Compare: two-phase-commit-style locking vs a saga with compensation (compare)
- Diagram: flash-sale path — inventory reservation under heavy contention (diagram)
- The bottleneck: the inventory-decrement step during a flash sale on a limited-stock item (concept)
- Pitfall: charging payment before confirming inventory, leading to refund storms on oversells (pitfall)
- Interview: "Design the checkout flow for an e-commerce site during a flash sale" (interview)
— cross-link: distributed-transactions-and-sagas, design-payment-system, idempotency-and-exactly-once

### Topic: Design a Payment System (design-payment-system, expert)
Moving money exactly once and being able to prove it — ledger correctness and reconciliation matter more than throughput.
- The prompt: charge a customer, pay out a merchant, and never lose or duplicate money (overview)
- Functional & non-functional requirements: exactly-once guarantees, auditability, regulatory retention (concept)
- Back-of-envelope: transactions/sec vs the far stricter correctness bar than typical read/write systems (concept)
- The API surface: charge(idempotencyKey, amount), refund(), and why idempotency keys are non-negotiable here (concept)
- Data model: a double-entry ledger — every transaction is two balanced entries, not one balance update (concept)
- Diagram: a charge as a ledger entry pair, not a single account-balance mutation (diagram)
- Idempotency keys preventing a network retry from double-charging a card (concept)
- Reconciliation: matching your ledger against the external payment processor's records (concept)
- Diagram: end-to-end flow — client, payment service, processor, ledger, async reconciliation job (diagram)
- The bottleneck: synchronous calls to an external processor on the critical checkout path (concept)
- Compare: strong consistency on the ledger vs eventual consistency on account-balance views (compare)
- Pitfall: updating a single balance column instead of an immutable ledger, losing the audit trail (pitfall)
- Interview: "Design a payment processing system that never double-charges" (interview)
— cross-link: design-ecommerce-checkout-system, idempotency-and-exactly-once, consensus-basics

### Topic: Design an Ad Click Aggregation System (design-ad-click-aggregation-system, advanced)
Billing-accuracy-critical stream aggregation — exactly-once counting and fraud filtering matter more than raw throughput.
- The prompt: count ad clicks/impressions accurately enough to bill advertisers (overview)
- Functional & non-functional requirements: billing accuracy (no double-count), fraud/click-spam filtering, reporting freshness (concept)
- Back-of-envelope: clicks/sec at platform scale vs the cost of a 1% counting error at that volume (concept)
- The API surface: recordClick(adId, userId, ts), getAggregate(adId, window) (concept)
- Stream processing: windowed aggregation over a click event stream (concept)
- Diagram: pipeline — event ingest, dedup/fraud filter, windowed aggregation, billing store (diagram)
- Exactly-once counting despite at-least-once delivery from the ingest layer (concept)
- Handling late-arriving events: a click that lands after its window already closed (concept)
- Compare: real-time (Lambda-architecture) counts vs an end-of-day authoritative batch recount (compare)
- Diagram: fraud filtering — bot detection and click-spam rules ahead of the aggregator (diagram)
- The bottleneck: the fraud-filter stage becoming the throughput ceiling for the whole pipeline (concept)
- Pitfall: counting clicks at ingest time before fraud filtering, then billing on the inflated number (pitfall)
- Interview: "Design a system to count ad clicks for billing at scale" (interview)
— cross-link: log-based-streaming, ml-system-design (fraud/bot detection), schema-evolution-and-compatibility

### Topic: Design a Stock Exchange Matching Engine (design-stock-exchange-matching-engine, expert)
Deterministic, price-time-priority order matching at microsecond latency — a single-threaded correctness core, the opposite of "scale by adding nodes."
- The prompt: match buy and sell orders fairly and deterministically, at extreme speed (overview)
- Functional & non-functional requirements: fairness (price-time priority), determinism, microsecond-level latency (concept)
- Back-of-envelope: orders/sec per symbol vs the latency budget per match (concept)
- The API surface: submitOrder(symbol, side, price, qty), cancelOrder(), market data feed (concept)
- Data model: the order book — a price-ordered structure per symbol, not a generic DB table (concept)
- Diagram: the order book — bids and asks as two price-ordered queues (diagram)
- Why this core is single-threaded per symbol: any reordering breaks fairness and auditability (concept)
- Compare: horizontally scaling by symbol-sharding vs trying to parallelize one order book (compare)
- Diagram: the matching loop — incoming order, price-time priority match, trade emitted (diagram)
- Sequencing and audit logging every order/match for regulatory replay (concept)
- The bottleneck: a single hot symbol's order book exceeding one core's throughput (concept)
- Pitfall: introducing any nondeterminism (e.g. multi-threaded matching) that breaks trade replay (pitfall)
- Interview: "Design a simplified stock exchange matching engine" (interview)
— cross-link: consensus-basics, time-and-ordering, physical-and-cost-constraints

---

## Group: Infrastructure & Platform Systems (hld-cases-infra)

*Systems that other systems are built on — search, telemetry, scheduling, and the storage/queue/gateway primitives themselves. The lesson here is building the primitive, where the building-block groups teach using one.*

### Topic: Design a Web Crawler (design-web-crawler, advanced)
Crawling at scale politely, without duplicating work or getting blocked.
- The prompt: crawl and index a large fraction of the web, continuously and politely (overview)
- Functional & non-functional requirements: freshness target, politeness constraints; non-goal: building the search ranking itself (concept)
- Back-of-envelope: pages to crawl, crawl rate needed to refresh the corpus, storage for raw HTML (concept)
- The crawl frontier: a prioritized queue of URLs to visit, and what "priority" means here (concept)
- Data model: the frontier queue plus a URL-seen dedup store, sized for the target corpus (concept)
- Diagram: crawler architecture — frontier, fetchers, parser, dedup store (diagram)
- Politeness: per-domain rate limits and robots.txt compliance (concept)
- URL deduplication at scale with Bloom filters — the false-positive trade-off (concept)
- Distributing the crawl across many workers without duplicate work, by partitioning the frontier by domain (concept)
- Compare: breadth-first vs priority-based crawl ordering (compare)
- Handling traps: infinite URL spaces (calendar pages), near-duplicate content (concept)
- The bottleneck: DNS resolution and per-domain politeness limits capping total throughput, not fetcher count (concept)
- Compare: a single central frontier vs domain-partitioned frontiers across worker shards (compare)
- Pitfall: no per-domain rate limit, hammering one site and getting IP-blocked (pitfall)
- Pitfall: re-crawling unchanged pages on a fixed interval instead of by observed change rate (pitfall)
- Interview: the follow-ups — detecting and skipping near-duplicate/boilerplate content across pages (interview)
- Interview: the follow-ups — prioritizing re-crawl frequency by how often a page actually changes (interview)
- Summary: frontier + dedup + per-domain politeness bound the whole system's throughput (concept)
— cross-link: distributed-rate-limiting, partitioning-and-sharding

### Topic: Design a Proximity Service (design-proximity-service, intermediate)
Answering "what's nearby" fast, using a spatial index instead of scanning every location.
- The prompt: answer "what's nearby" in milliseconds against millions of moving points (overview)
- Functional & non-functional requirements: query radius range, update frequency per object; non-goal: route-planning itself (concept)
- Back-of-envelope: moving objects, location updates/sec, nearby-queries/sec in a dense area (concept)
- The API surface: updateLocation(objectId, lat, lng), findNearby(lat, lng, radius) (concept)
- Why a linear scan across all locations doesn't scale, motivating a spatial index (concept)
- Geohashing: encoding location into a sortable string prefix (concept)
- Diagram: geohash grid cells around a query point (diagram)
- Quadtrees as an alternative spatial index (concept)
- Compare: geohash vs quadtree vs a simple fixed grid — update cost, query cost, precision (compare)
- Data model: the spatial index kept in memory vs persisted, and how it's sharded (concept)
- Handling moving objects: frequent location updates at scale, and throttling/batching index writes (concept)
- Diagram: end-to-end architecture for a "nearby drivers" query (diagram)
- The bottleneck: a dense hotspot (downtown at rush hour) overloading one spatial-index shard (concept)
- Compare: expanding-ring search vs a fixed generous radius, on latency and false negatives at cell edges (compare)
- Pitfall: a geohash boundary splitting nearby points into different cells, missing true neighbors (pitfall)
- Interview: the follow-ups — keeping the index fresh when objects update location every second (interview)
- Interview: the follow-ups — expanding search radius gracefully in sparse areas (interview)
- Summary: geohash/quadtree trade update cost against query cost — the index shape is the whole design (concept)
— cross-link: design-ride-hailing-system, partitioning-and-sharding

### Topic: Design a Collaborative Editor (design-collaborative-editor, advanced)
Merging concurrent real-time edits from multiple users without clobbering anyone's changes.
- The prompt: many users edit the same document simultaneously and see a consistent result (overview)
- Functional & non-functional requirements: offline-edit support, convergence guarantee; non-goal: rich-text rendering itself (concept)
- Back-of-envelope: concurrent editors per doc, ops/sec per editor, doc size vs op-log growth (concept)
- The API surface: applyOp(docId, op), subscribe(docId) for a live op/change stream (concept)
- The core problem: merging concurrent edits without clobbering each other (concept)
- Operational Transformation (OT): transforming ops against each other to converge (concept)
- CRDTs as a newer alternative: merge by construction instead of transformation (concept)
- Diagram: two concurrent edits transformed/merged into a consistent result (diagram)
- Compare: OT vs CRDTs on complexity, server-authority requirement, and offline support (compare)
- Data model: the document as an op-log/CRDT structure, not just the latest text blob (concept)
- Real-time sync transport: WebSockets, with presence/cursor broadcast alongside content ops (concept)
- Diagram: end-to-end architecture — client, sync server, document store, op-log (diagram)
- Offline edits: buffering local ops and reconciling them on reconnect (concept)
- The bottleneck: the sync server's per-document ordering point under many simultaneous editors, and scaling by document sharding (concept)
- Pitfall: naive last-write-wins on a shared document, silently dropping edits (pitfall)
- Interview: the follow-ups — undo/redo across concurrent edits from different users (interview)
- Interview: the follow-ups — scaling one wildly popular shared document beyond one server's capacity (interview)
- Summary: an op-log/CRDT plus a per-document ordering point turns concurrent edits into one consistent result (concept)
— cross-link: design-file-sync-service, conflict-resolution

### Topic: Design a Search Typeahead System (design-search-typeahead-system, advanced)
Sub-100ms prefix suggestions ranked by popularity — a specialized prefix data structure and freshness problem, distinct from full-text search ranking.
- The prompt: as a user types, show ranked query suggestions in under 100ms (overview)
- Functional & non-functional requirements: latency budget, personalization, trending-query freshness (concept)
- Back-of-envelope: keystrokes/sec platform-wide vs suggestions-per-keystroke fan-out (concept)
- The API surface: getSuggestions(prefix, userId) (concept)
- Data model: a trie/FST of prefixes to top-K completions vs a generic inverted index (compare)
- Diagram: trie structure with precomputed top-K suggestions cached at each node (diagram)
- Ranking suggestions by historical popularity, recency, and personalization signals (concept)
- Keeping trending queries fresh without rebuilding the whole trie (concept)
- Diagram: offline aggregation job periodically refreshing the trie from query logs (diagram)
- The bottleneck: serving latency if the trie doesn't fit in memory on one node (concept)
- Compare: precomputed trie vs querying the full-text search index live for suggestions (compare)
- Pitfall: ranking suggestions by raw frequency only, surfacing stale/abandoned queries (pitfall)
- Interview: "Design the autocomplete behind a search bar" (interview)
— cross-link: autocomplete-and-typeahead, inverted-index, relevance-ranking

### Topic: Design a Logging & Metrics Pipeline (design-logging-metrics-pipeline, advanced)
Ingesting and querying telemetry at a volume far exceeding the systems it monitors — the pipeline's own scale is the design problem.
- The prompt: every service emits logs and metrics; make them queryable and alertable (overview)
- Functional & non-functional requirements: ingest volume, query latency, retention/cost tiers (concept)
- Back-of-envelope: log lines/sec and metric points/sec at fleet scale, vs storage cost (concept)
- The API surface: emit(log/metric), query(timeRange, filter), alert rule evaluation (concept)
- Data model: time-series storage for metrics vs a search index for logs (compare)
- Diagram: pipeline — agents, ingest buffer, stream processor, hot store, cold store (diagram)
- Sampling and aggregation: not every log line survives to long-term storage (concept)
- Downsampling metrics over time (raw → 1min → 1hr rollups) to control storage cost (concept)
- Diagram: hot (recent, full-resolution) vs cold (old, downsampled) storage tiers (diagram)
- The bottleneck: a logging spike from a misbehaving service drowning out everyone else's signal (concept)
- Pitfall: no per-tenant ingest limit, so one noisy service can take down the whole pipeline (pitfall)
- Interview: "Design the logging/metrics backend behind an observability platform" (interview)
— cross-link: logging-at-scale, metrics-and-slis-slos, cost-aware-telemetry-at-scale

### Topic: Design a Distributed Job Scheduler (design-distributed-job-scheduler, expert)
A distributed cron that guarantees every job runs, reliably, even as workers and leaders fail — the scheduling guarantee is the whole problem.
- The prompt: run millions of scheduled/recurring jobs across a fleet of workers, reliably (overview)
- Functional & non-functional requirements: at-least-once vs exactly-once execution, missed-job handling, priority (concept)
- Back-of-envelope: jobs scheduled/min, worker fleet size, jobs-in-flight at peak (concept)
- The API surface: scheduleJob(cronSpec/runAt), cancelJob(), job status/heartbeat (concept)
- Data model: a job table with next-run-time, lease/lock state, and retry count (concept)
- Diagram: architecture — scheduler leader, job store, worker pool, lease-based dispatch (diagram)
- Leader election for the component that decides "which jobs are due now" (concept)
- Leasing a job to a worker so a crashed worker's job gets picked up by another (concept)
- Diagram: a worker crash mid-job — lease expiry and safe re-dispatch (diagram)
- The bottleneck: the job store under a scheduling stampede (many jobs due at the same minute) (concept)
- Compare: at-least-once execution with idempotent jobs vs trying to guarantee exactly-once (compare)
- Pitfall: no lease/lock on dispatched jobs, so a slow worker's job gets run twice by two workers (pitfall)
- Interview: "Design a distributed cron system like a lightweight Airflow" (interview)
— cross-link: design-transcode-pipeline, idempotency-and-exactly-once, distributed-coordination

### Topic: Design a Blob / Object Store (design-blob-object-store, expert)
Building the durable object store itself (S3-like) — erasure coding, metadata scaling, and multi-part upload, not using one.
- The prompt: store and serve arbitrarily large immutable objects, durably, at exabyte scale (overview)
- Functional & non-functional requirements: durability target (many nines), availability, upload size limits (concept)
- Back-of-envelope: objects stored, average size, storage overhead of your durability scheme (concept)
- The API surface: putObject(key, bytes), getObject(key), multi-part upload for large objects (concept)
- Data model: metadata service (key → location) fully decoupled from the data-storage nodes (concept)
- Diagram: architecture — metadata service, storage nodes, and how a GET resolves through both (diagram)
- Durability via replication vs erasure coding, and the storage-overhead trade-off (compare)
- Diagram: erasure coding — splitting an object into data + parity shards across nodes (diagram)
- Multi-part upload: large objects uploaded as independent chunks, assembled on commit (concept)
- The bottleneck: metadata service throughput at billions of objects (concept)
- Compare: strong consistency on writes (read-after-write) vs eventual consistency on list operations (compare)
- Pitfall: colocating metadata and data on the same nodes, so a data-node failure loses lookups too (pitfall)
- Interview: "Design a durable object store like S3 from first principles" (interview)
— cross-link: object-and-blob-storage, replication-strategies, storage-engine-choice-as-a-design-decision

### Topic: Design a Distributed Message Queue (design-distributed-message-queue, expert)
Building the broker itself (Kafka/SQS-like) — the partitioned log and delivery-semantics internals, not how to use a queue.
- The prompt: a durable, ordered, at-least-once message broker that producers and consumers share (overview)
- Functional & non-functional requirements: throughput, ordering scope, delivery guarantee, retention window (concept)
- Back-of-envelope: messages/sec, average message size, retention-window storage (concept)
- The API surface: produce(topic, key, value), consume(topic, partition, offset) (concept)
- Data model: the partitioned append-only log as the core storage structure (concept)
- Diagram: topic split into partitions, each an ordered, append-only log with an offset (diagram)
- Consumer offset tracking: how a consumer resumes exactly where it left off (concept)
- Diagram: producer → partition (by key) → replicated log → consumer group offsets (diagram)
- Delivery semantics internals: how at-least-once, at-most-once, and exactly-once actually differ here (compare)
- Replication within the broker for durability if a partition leader fails (concept)
- The bottleneck: a single hot partition (skewed key) capping one topic's throughput (concept)
- Pitfall: growing partition count after the fact, silently breaking key-based ordering guarantees (pitfall)
- Interview: "Design a distributed message queue like Kafka from scratch" (interview)
— cross-link: log-based-streaming, message-delivery-semantics, replication-strategies

### Topic: Design a Feature Flag Service (design-feature-flag-service, intermediate)
Millisecond flag evaluation on every request, globally consistent rollout percentages, and instant propagation — without a central bottleneck in every request path.
- The prompt: turn features on/off, or roll out to X% of users, without a redeploy (overview)
- Functional & non-functional requirements: evaluation latency (must not slow the request), propagation delay, targeting rules (concept)
- Back-of-envelope: flag evaluations/sec across the whole fleet vs a central service's capacity (concept)
- The API surface: isEnabled(flagKey, userContext), updateFlag(config) (concept)
- Stable bucketing: hashing userId + flagKey so the same user always lands in the same bucket (concept)
- Diagram: consistent-hash bucketing deciding in/out of a percentage rollout (diagram)
- Local evaluation via an SDK with a cached config, instead of a network call per request (concept)
- Diagram: config propagation — control plane pushes updates to SDKs via streaming/polling (diagram)
- The bottleneck: the control plane during a global config push to every service instance (concept)
- Compare: server-side evaluation (central call) vs client-side SDK evaluation (local, cached) (compare)
- Pitfall: evaluating flags with a synchronous network call on the hot request path (pitfall)
- Interview: "Design a feature flag system used by every service at the company" (interview)
— cross-link: strangler-fig-and-migration-patterns, consistency-models

### Topic: Design an API Gateway (design-api-gateway-system, advanced)
The gateway as its own system with its own failure modes — routing, auth, and rate limiting at the edge, distinct from the API-design and resilience concepts it enforces.
- The prompt: one edge layer in front of many backend services, handling cross-cutting concerns (overview)
- Functional & non-functional requirements: added-latency budget, availability (it fronts everything), config agility (concept)
- Back-of-envelope: fleet-wide QPS through the gateway vs a single backend service's QPS (concept)
- The API surface: route config (path → service), plus the cross-cutting policies attached to a route (concept)
- Data model: a routing table plus per-route policy config (auth, rate limit, timeout) (concept)
- Diagram: request path — TLS termination, auth, rate limit, routing, backend, response (diagram)
- Request aggregation: composing one client-facing response from multiple backend calls (concept)
- Compare: a single monolithic gateway vs sidecar-based per-service gateways (service mesh) (compare)
- Diagram: gateway cluster behind a load balancer, stateless and horizontally scaled (diagram)
- The bottleneck: the gateway itself, since every request in the system passes through it (concept)
- Failure isolation: one slow backend must not exhaust the gateway's connection pool for everyone (concept)
- Pitfall: putting business logic in the gateway, coupling it to backends it should stay agnostic of (pitfall)
- Interview: "Design an API gateway for a company with dozens of backend services" (interview)
— cross-link: api-gateway-patterns, service-mesh, bulkheads-and-isolation

---

---

# Phase F — Design craft & the interview method

## Group: Design in the Real World (design-in-practice)

*designing on the job, not just in the interview room — docs, migrations, rollouts, review, and org cost*

### Topic: Writing a Design Doc / RFC (writing-a-design-doc, intermediate)
Structuring and writing a design doc that survives review and gets approved — stating the problem before the solution, writing alternatives considered so the rejections teach something, and making non-goals explicit. Boundary: general writing craft and doc templates belong to `engineering-craft`'s `technical-communication`; this Topic covers only the design-doc-specific structure and argument.
- Why design docs exist: forcing a design to survive contact with reviewers (concept)
- The anatomy of an approvable doc: problem, goals, non-goals, alternatives, decision (overview)
- Stating the problem before the solution: the mistake reviewers spot first (concept)
- Alternatives considered: writing them so the rejection reasons teach, not just list (concept)
- Diagram: a design doc as an argument tree, not a report (diagram)
- Explicit non-goals: what you're deliberately not solving, and why that's a feature (concept)
- Compare: a doc written to get sign-off vs a doc written to look thorough (compare)
- Pitfall: the doc that hides the real decision inside implementation detail (pitfall)
- Interview: "Walk me through how you'd get a risky design approved" (interview)

### Topic: Brownfield System Design (brownfield-system-design, advanced)
Designing changes inside a live system that can't be rewritten — mapping blast radius, maintaining backwards compatibility, and the mechanics of dual-writes and backfills without breaking things mid-flight. Boundary: the pattern catalog (strangler fig, etc.) lives in `system-design`'s microservices group; this Topic is the practitioner's playbook for executing a migration safely.
- Greenfield vs brownfield: why "just redesign it" is rarely the real option (concept)
- Mapping the blast radius: who and what depends on the thing you're changing (concept)
- Diagram: an expand-contract migration in stages (diagram)
- Backwards compatibility: versioning the contract while the old caller still exists (concept)
- Dual-writes: keeping two systems consistent during a cutover, and where they drift (concept)
- Backfills: safely rewriting historical data without an outage (concept)
- Compare: big-bang cutover vs incremental migration — when each is actually right (compare)
- Pitfall: the migration with no way to tell if it's actually done (pitfall)
- Interview: "How would you migrate this system's data store with zero downtime?" (interview)

### Topic: Rolling Out a Design (rolling-out-a-design, advanced)
Getting a new design live safely — phased rollout, feature flags, shadow traffic, dark launches — and having a real rollback plan before you ship, not after something breaks. Boundary: pipeline/automation mechanics belong to `engineering-craft`'s `cicd`; this Topic covers the design-time rollout strategy and how to reverse it, not the tooling.
- Why the rollout is part of the design, not an afterthought (concept)
- Phased rollout: percentage ramps and the metrics that gate each step (concept)
- Feature flags as a design tool: decoupling deploy from release (concept)
- Shadow traffic and dark launches: testing the real path without real consequences (concept)
- Diagram: a rollout plan as a decision tree with abort points (diagram)
- Writing a rollback plan before launch, not during the incident (concept)
- Compare: canary release vs blue-green vs shadow traffic — what each actually protects against (compare)
- Pitfall: a rollout with no kill switch because "it should be fine" (pitfall)
- Interview: "How would you roll out a change to a payment path safely?" (interview)

### Topic: Reviewing Someone Else's Design (reviewing-a-design, intermediate)
Giving useful architectural feedback on a design doc — what to look for, how to phrase pushback so it lands, and spotting the assumption the author never wrote down. Boundary: line-by-line code review is `engineering-craft`'s `code-review`; this Topic is review of the design/architecture layer, before code exists.
- What a design review is actually checking: correctness, cost, and blast radius (concept)
- The unstated assumption: finding what the author didn't write down (concept)
- A checklist for reading a design doc critically (overview)
- Giving feedback that changes the design, not just the wording (concept)
- Diagram: separating "must fix" from "consider" comments (diagram)
- Compare: a nitpicking reviewer vs a reviewer who asks the one question that matters (compare)
- Pitfall: approving a design because pushing back feels adversarial (pitfall)
- Interview: "Review this design doc and tell me what concerns you" (interview)

### Topic: Cost- and Org-Aware Design (cost-and-org-aware-design, expert)
Designing with organizational constraints as first-class inputs — build vs buy, the operational burden a design creates, who ends up on call for it, and designing for the team you actually have. Boundary: cross-team org trade-offs at the staff/principal level are covered by the `sd-playbook` addition below; this Topic is the cost/ownership/team-fit lens applied to any single design decision.
- Build vs buy: the real cost of "we could build that ourselves" (concept)
- Operational burden as a design cost, not an implementation detail (concept)
- Who's on call for this: designing with the owning team's reality in mind (concept)
- Diagram: total cost of ownership across build, run, and maintain (diagram)
- Designing for the team you have: skills, headcount, and time horizon as constraints (concept)
- Compare: the "correct" design vs the design this team can actually operate (compare)
- Pitfall: choosing the interesting technology over the boring one that fits (pitfall)
- Interview: "Would you build or buy this, and why?" (interview)

**Flagged overlap (unavoidable, kept thin):** "operational burden"/"on-call" here necessarily brushes against `engineering-craft`'s `debugging` (incident response) and `clean-architecture`/DDD — this group states the design-time cost/ownership question only, and defers "how you actually debug/operate it" and "how you structure the domain model" to those groups.

---

## Group: System Design Interview Playbook (sd-playbook)

*the interview framework/method*

> Canonical home for the system design interview method. `sd-interview-playbook` in Area 17 is the same group by another name — point it here rather than duplicating content.

### Topic: The Interview Framework (the-interview-framework, beginner)
The standard shape of a 45-minute system design interview, end to end.
- The standard 45-minute shape: requirements, estimation, HLD, deep dive, wrap-up (concept)
- Diagram: the framework as a timeline with minutes allocated (diagram)
- Why skipping requirements is the most common failure mode (concept)
- How much time to spend on each phase, and adjusting on the fly (concept)
- Compare: a rigid framework vs a natural conversation — using the framework without sounding scripted (compare)
- Pitfall: jumping straight to a detailed architecture before requirements are clear (pitfall)
- Interview: watching for interviewer cues that it's time to move to the next phase (interview)

### Topic: Clarifying Requirements (clarifying-requirements, beginner)
The questions worth asking in the first five minutes, and the ones that stall the interview.
- Functional requirements: what must the system do, precisely (concept)
- Non-functional requirements: scale, latency, availability, consistency (concept)
- Diagram: a requirements checklist mapped to design decisions later (diagram)
- Scoping down: what to explicitly exclude and say out loud (concept)
- Good questions vs questions that stall the interview (compare)
- Pitfall: asking so many questions the interviewer runs out of patience (pitfall)
- Interview: "Design Twitter" — the first two minutes of questions to ask (interview)

### Topic: Driving the High-Level Design (driving-the-high-level-design, intermediate)
Turning requirements into a first-pass architecture diagram, and iterating it live.
- Going from requirements straight to a first-pass architecture (concept)
- Diagram: a first-draft high-level diagram — boxes and arrows only (diagram)
- Naming components by responsibility, not by product name (concept)
- Iterating the diagram as new requirements surface (concept)
- Compare: starting broad-then-narrow vs deep-then-broad (compare)
- Pitfall: drawing a polished diagram that never gets revisited or challenged (pitfall)
- Interview: narrating the diagram as you draw it, out loud (interview)

### Topic: Deep Dives & Trade-Off Discussions (deep-dives-and-trade-off-discussions, advanced)
Choosing what to go deep on, and defending a choice under pushback without getting defensive.
- Choosing what to go deep on: what the interviewer is probing for (concept)
- Structuring a trade-off answer: options, criteria, decision (concept)
- Diagram: one component "exploded" into its internal design (diagram)
- Defending a choice under pushback without becoming defensive (concept)
- Compare: "textbook correct" answer vs a defensible, requirements-driven answer (compare)
- Pitfall: giving one option with no alternative considered (pitfall)
- Interview: "Why not just use a cache for everything?" — handling a challenge question (interview)

### Topic: Communication & Whiteboarding (communication-and-whiteboarding, intermediate)
Thinking out loud and keeping a diagram readable as the design grows under time pressure.
- Thinking out loud: narrating trade-offs as you reason through them (concept)
- Diagramming conventions that stay readable as the design grows (concept)
- Diagram: a clean, labeled system diagram vs a cluttered one (diagram)
- Managing time across a 45-minute conversation (concept)
- Compare: silent thinking vs collaborative thinking with the interviewer (compare)
- Pitfall: a diagram so dense the interviewer can't follow the conversation (pitfall)
- Interview: recovering when you realize an earlier decision was wrong (interview)

### Topic: Common Mistakes in System Design Interviews (common-mistakes-in-system-design-interviews, intermediate)
The recurring, avoidable ways candidates lose points, and the self-checks that catch them in the moment.
- Designing before requirements are pinned down (concept)
- Over-engineering for scale the requirements never asked for (concept)
- Diagram: an over-engineered design vs a right-sized one for the same requirements (diagram)
- Never mentioning trade-offs — presenting one option as the only option (concept)
- Ignoring the interviewer's hints and steering questions (concept)
- Compare: common failure patterns and the fix for each (compare)
- Pitfall: memorized architecture recited without adapting to the given constraints (pitfall)
- Interview: self-check questions to catch these mistakes mid-interview (interview)

### Topic: Leveling Expectations (leveling-expectations, intermediate)
What separates a mid-level answer from a senior or staff+ answer to the same question.
- What a mid-level answer looks like: correct, standard patterns (concept)
- What a senior answer adds: trade-off ownership, edge cases, failure modes (concept)
- What a staff+ answer adds: organizational/product judgment, cost, migration paths (concept)
- Diagram: the same question answered at three depths (diagram)
- Compare: breadth vs depth expectations by level (compare)
- Pitfall: a senior candidate giving a mid-level answer — technically fine, but thin (pitfall)
- Interview: calibrating your answer's depth to the level you're interviewing for (interview)

---

<!-- expert-tier additions (sd-playbook) -->

The existing group already covers the framework, clarifying requirements, driving the HLD, deep dives,
communication/whiteboarding, common mistakes, and leveling expectations. These three add the tiers above
that, none restated:

### Topic: Designing Under Ambiguity (designing-under-ambiguity, advanced)
Handling the deliberate flavor of interview where the interviewer withholds requirements or context on purpose, and making progress by stating and testing assumptions instead of stalling on a fourth clarifying question.
- Why interviewers withhold information on purpose (concept)
- Stating an assumption out loud instead of asking a fourth clarifying question (concept)
- Diagram: the assumption → decision → checkpoint loop under ambiguity (diagram)
- Making a defensible call with incomplete information (concept)
- Compare: guessing silently vs narrating your reasoning under uncertainty (compare)
- Pitfall: freezing up when the interviewer won't just answer the question (pitfall)
- Interview: "I don't have that number — what would you assume, and why?" (interview)

### Topic: Handling Interviewer Pushback (handling-interviewer-pushback, advanced)
Responding well when the interviewer challenges a choice, disagrees, or introduces a curveball mid-design — defending a decision with reasoning, and knowing when to actually change your mind.
- Why pushback is a deliberate test, not a sign you're wrong (concept)
- Defending a decision with the trade-off you already made, not by repeating it louder (concept)
- Recognizing a genuinely good counterpoint and updating your design (concept)
- Diagram: the pushback exchange as propose → challenge → resolve (diagram)
- Compare: caving immediately vs digging in — the middle path that scores well (compare)
- Pitfall: treating every objection as an attack on your competence (pitfall)
- Interview: "What if I told you that database won't scale to that load?" (interview)

### Topic: The Staff/Principal Signal (staff-level-system-design-signal, expert)
What separates a senior-passing answer from a staff/principal-passing one — org-level thinking: the migration story, cross-team trade-offs, and decisions that outlive a single team's roadmap.
- What "staff signal" actually means beyond a bigger diagram (concept)
- Narrating the migration story: how the org gets from here to there, not just the end state (concept)
- Cross-team trade-offs: whose roadmap absorbs the cost of your design (concept)
- Diagram: a design's blast radius across team boundaries (diagram)
- Compare: a senior answer (one system, right) vs a staff answer (one system, right, and it fits the org) (compare)
- Pitfall: designing an elegant system nobody else's team can adopt (pitfall)
- Interview: "How would this decision play out across three teams over two years?" (interview)

*(Considered and cut: a remote/virtual-whiteboard-mechanics topic — it's tooling/logistics, not design judgment; doesn't clear the value filter as its own Topic. Fold a line on it into `communication-and-whiteboarding` if desired.)*

---
### Topic: The Remote / Virtual Design Round (sd-remote-mechanics, beginner)
The logistics of designing over a video call — tool fluency, a diagram that stays legible for 45 minutes, and recovering from lag without losing the thread.
- Why the remote round is a different skill: you lose the whiteboard's shared physical space (overview)
- The tools you'll actually be handed — Excalidraw, Miro, FigJam, a shared doc, or plain text — and the baseline fluency to have before the call (concept)
- Rehearsing with the real tool beforehand, not for the first time live (concept)
- Screen and window layout so you can see the interviewer, your diagram, and your notes at once (concept)
- Keeping a diagram legible as it grows: box discipline, naming, whitespace, and when to start a second canvas (concept)
- Diagram: the same architecture drawn well vs drawn as a hairball over 45 minutes (diagram)
- Narrating while you draw — the remote substitute for pointing at a board (concept)
- Recovering from lag, a frozen canvas, or a dropped call without losing the thread of the design (concept)
- The text-only fallback: designing in a shared doc when the whiteboard dies (concept)
- Pitfall: spending the first five minutes fighting the tool instead of designing — and how to pre-empt it (pitfall)

---

# Phase G — Interview question bank: LLD & OOD

## Group: LLD Interview Bank — OOP (interview-lld-oop)

*The classic OOP viva — answering the "explain X" and "can you Y" questions cleanly under pressure.*

### Topic: What's the difference between abstraction and encapsulation? (iv-abstraction-vs-encapsulation-answer, beginner)
The single most-repeated OOP interview question; walk away with a one-line answer plus a concrete example that survives a follow-up.
- The question as asked, and why interviewers keep asking it (overview)
- Clarifying question: do they want the textbook definition or a code example? (concept)
- The answer skeleton: one sentence each, then a shared example (concept)
- Encapsulation in one line + the `BankAccount` example (concept) — cross-link: encapsulation
- Abstraction in one line + the same example, one level up (concept) — cross-link: abstraction
- Diagram: encapsulation hides data, abstraction hides complexity, on the same class (diagram)
- Code: a class that violates both — public fields and a leaky interface — refactored to respect both (code)
- Compare: abstraction vs encapsulation — what problem each solves, and where they overlap (compare)
- Follow-up: "give me an example where you have one without the other" (concept)
- Follow-up: "does an interface alone give you both, or just one?" (concept)
- Weak answer: "encapsulation is getters and setters" — why that loses points (pitfall)
- Wrong answer: treating the two as interchangeable — "abstraction is just hiding implementation, same thing" (pitfall)
- The 60-second version, spoken out loud (concept)

### Topic: Why is composition favored over inheritance? (iv-why-composition-over-inheritance, intermediate)
Tests whether you can justify a rule of thumb with a concrete failure mode, not just recite it.
- The question, and what "favor" is testing — judgment, not dogma (overview)
- Clarifying question: are we talking about this codebase or in general? (concept)
- The answer skeleton: state the rule, give the failure mode it prevents, give the exception (concept)
- Code: an inheritance hierarchy that breaks when a new variant arrives (code) — cross-link: composition-vs-inheritance
- Code: the same feature refactored to composition + strategy (code) — cross-link: strategy-pattern
- Code: adding a second, orthogonal behavior by composing another small object — the combinatorial win (code)
- Compare: composition vs inheritance — reuse, testability in isolation, runtime flexibility (compare)
- Follow-up: "so is inheritance ever right?" — is-a vs has-a as the actual test (concept)
- Follow-up: "what does this cost you?" — indirection, more objects to wire up (concept)
- Follow-up: "how many collaborator objects is too many before composition itself gets tangled?" (concept)
- Weak answer: reciting "favor composition" with no example — reads as memorized (pitfall)
- Wrong answer: "never use inheritance" stated as an absolute rule (pitfall)
- The 60-second version (concept)

### Topic: Can you override a static method in Java? (iv-can-you-override-static-method, intermediate)
A language-specific trap question that tests whether you actually understand dispatch, not memorized trivia.
- The question as asked, and why it's a trap (overview)
- Clarifying question: which language — this is Java/C#-specific, not universal (concept)
- The answer skeleton: no, it's hidden not overridden — then explain why (concept)
- Code: a static "override" that resolves by reference type, not object type (code)
- Diagram: static dispatch (compile-time, by type) vs dynamic dispatch (runtime, by vtable) (diagram)
- Compare: hiding vs overriding — what changes at compile time vs runtime (compare)
- Follow-up: "what actually happens if you try?" — method hiding, not polymorphism (concept)
- Follow-up: "does this apply to other languages?" — Python/JS don't draw this line the same way (concept)
- Follow-up: "what about a static method called through an instance reference — which one runs?" (concept)
- Weak answer: saying "no" with no explanation of hiding vs overriding (pitfall)
- Wrong answer: claiming the subclass's static method is polymorphically dispatched at runtime (pitfall)
- The 60-second version (concept)

### Topic: When would you choose an interface over an abstract class? (iv-interface-vs-abstract-class-choice, intermediate)
The design-judgment version of a definitions question.
- The question, and the design-judgment it's really testing (overview)
- Clarifying question: which language — multiple inheritance rules differ (concept)
- The answer skeleton: contract-only vs shared implementation, then the deciding question (concept) — cross-link: interfaces-vs-abstract-classes
- Code: the same capability modeled both ways, side by side (code)
- Compare: interface vs abstract class — decision table (multiple inheritance, shared state, versioning) (compare)
- Code: mixing both — an abstract class implementing an interface, when that combined shape is right (code)
- Follow-up: "what changed with default methods on interfaces?" (concept)
- Follow-up: "you chose wrong initially — how do you migrate?" (concept)
- Follow-up: "can an abstract class have zero implementation — is that still meaningfully different from an interface?" (concept)
- Weak answer: "interfaces are 100% abstract" — outdated in modern languages (pitfall)
- Wrong answer: claiming a class can extend multiple abstract classes the way it implements multiple interfaces (pitfall)
- The 60-second version (concept)

### Topic: What's the difference between method overloading and overriding? (iv-overloading-vs-overriding, beginner)
The "compile-time vs runtime" answer it's fishing for.
- The question, and the compile-time vs runtime distinction it wants (overview)
- Clarifying question: are they asking definitions or asking you to spot a bug? (concept)
- The answer skeleton: overloading = same name different signature, resolved at compile time; overriding = same signature, resolved at runtime (concept) — cross-link: polymorphism
- Code: an overload-resolution surprise — the "wrong" method picked (code)
- Code: an override that changes behavior polymorphically (code)
- Compare: overloading vs overriding — binding time, class relationship, return-type rules (compare)
- Follow-up: "can you overload by return type alone?" (concept)
- Follow-up: "what rules govern overriding — same signature, covariant return?" (concept)
- Follow-up: "what happens with autoboxing or widening — how does the compiler pick between 'close enough' overloads?" (concept)
- Weak answer: confusing the two under pressure, calling overloading "polymorphism" without qualifying compile-time (pitfall)
- Wrong answer: claiming private or static methods can be overridden by a subclass (pitfall)
- The 60-second version (concept)

### Topic: What is the diamond problem and how do languages solve it? (iv-diamond-problem-explained, intermediate)
Really about ambiguity resolution, not just the shape of the diagram.
- The question, and why it's really about ambiguity resolution (overview)
- Clarifying question: single inheritance language or multiple (C++)? (concept)
- The answer skeleton: draw the diamond, name the ambiguity, name the fix (concept) — cross-link: inheritance
- Diagram: the diamond — two parents, one shared grandparent method (diagram)
- Code: the same ambiguity via multiple interface default methods, and how it's resolved (code)
- Code: what happens when you DON'T resolve it explicitly — the compile error the language forces on you (code)
- Follow-up: "why did Java ban multiple class inheritance but allow multiple interfaces?" (concept)
- Follow-up: "how does virtual inheritance solve it in C++?" (concept)
- Follow-up: "Python allows multiple class inheritance directly — how does MRO resolve it instead?" (concept)
- Weak answer: only describing the shape without naming a concrete resolution mechanism (pitfall)
- Wrong answer: claiming the diamond problem is "solved" by the language silently picking whichever parent it finds first (pitfall)
- The 60-second version (concept)

### Topic: What's the equals/hashCode contract and why does it matter? (iv-equals-hashcode-contract, intermediate)
The bug class it's protecting against is the real point.
- The question, and the bug class it's protecting against (overview)
- Clarifying question: is this about a hash-based collection specifically? (concept)
- The answer skeleton: the contract's rules, then the consequence of breaking it (concept)
- Code: overriding `equals` without `hashCode` — an object that "disappears" from a `HashSet` (code)
- Code: a correct `equals`/`hashCode` pair for a value object (code)
- Code: a mutable field used in `hashCode` — the object silently becomes unfindable after being inserted, then mutated (code)
- Follow-up: "what about mutable fields in the hash?" — object changes after insertion (concept)
- Follow-up: "how does this interact with immutability?" (concept) — cross-link: immutability-as-a-design-tool
- Follow-up: "what's the actual difference between `==`, `equals`, and a `Comparator`?" (concept)
- Weak answer: reciting the rule without the "why" — the broken-invariant story (pitfall)
- Wrong answer: overriding `equals` alone "for performance," leaving the default `hashCode` untouched (pitfall)
- The 60-second version (concept)

### Topic: Why should objects be immutable, and when should you make them so? (iv-why-immutability, intermediate)
The trade-off it's testing you can articulate — not "immutability is always better."
- The question, and the trade-off it's testing you can articulate (overview)
- Clarifying question: immutability of what — a value object, a config, a whole domain model? (concept)
- The answer skeleton: name the benefits, name the cost, name when it's not worth it (concept) — cross-link: immutability-as-a-design-tool
- Code: a mutable class refactored to immutable (builder + final fields) (code)
- Compare: immutable vs mutable — thread safety, GC pressure, ergonomics (compare)
- Code: a "wither" method returning a new instance with one field changed, instead of mutating in place (code)
- Follow-up: "how do you 'update' an immutable object efficiently?" — copy-on-write, wither methods (concept)
- Follow-up: "is immutability enough to make something thread-safe?" (concept) — cross-link: thread-safety-fundamentals-for-objects
- Follow-up: "what's the memory/GC cost story once this is on a hot path at scale?" (concept)
- Weak answer: "immutable is always better" — no cost acknowledged (pitfall)
- Wrong answer: calling a class immutable because its fields are `final`, while one field is a mutable list callers can reach into (pitfall)
- The 60-second version (concept)

### Topic: Is inheritance always bad? (iv-is-inheritance-always-bad, intermediate)
The pushback question after "favor composition" advice — defend the cases where inheritance is still the right tool.
- The question, as a pushback on "favor composition," and what it's really probing (overview)
- Clarifying question: bad in what sense — deep hierarchies specifically, or any use of it at all? (concept)
- The answer skeleton: no — name the is-a test, then the two failure modes that actually make it bad (concept) — cross-link: iv-why-composition-over-inheritance
- Code: a case where inheritance is genuinely the clean fit — a closed shape hierarchy sharing one real invariant (code)
- Code: the same domain forced into composition instead, and why it's worse here — more indirection, no real gain (code)
- Compare: when inheritance wins vs when composition wins — a decision checklist (compare)
- Follow-up: "how deep is too deep for a hierarchy?" (concept)
- Follow-up: "what does the Liskov substitution principle add to the is-a test?" (concept) — cross-link: lsp-liskov-substitution
- Follow-up: "how do you fix a hierarchy that's already three levels deep and wrong?" (concept)
- Weak answer: "inheritance is bad, always use composition" — parroting advice as dogma (pitfall)
- Wrong answer: claiming inheritance is fine anywhere the types are "related," without ever checking the is-a test (pitfall)
- The 60-second version (concept)

### Topic: What is polymorphism really buying you? (iv-what-does-polymorphism-buy-you, beginner)
Beyond the mechanism — the actual maintenance win a candidate should be able to point at.
- The question, and why "runtime method dispatch" alone is a weak answer (overview)
- Clarifying question: are they asking about the mechanism or the payoff? (concept) — cross-link: polymorphism
- The answer skeleton: name the mechanism in one line, then the payoff — callers stop branching on type (concept)
- Code: a type-switch if/else chain calling different behavior per type (code)
- Code: the same code made polymorphic — one call site, no branching (code)
- Diagram: adding a new type — the if/else version needs an edit at every call site, the polymorphic version needs none (diagram) — cross-link: ocp-open-closed
- Follow-up: "what's the actual runtime cost — a vtable lookup?" (concept)
- Follow-up: "does this only apply to inheritance, or does an interface give you the same thing?" (concept)
- Weak answer: defining dynamic dispatch correctly but never naming the payoff (pitfall)
- Wrong answer: claiming polymorphism "removes the need for any conditionals," ignoring cases where type-checking is still the right tool (pitfall)
- The 60-second version (concept)

### Topic: How do you decide what belongs in a class? (iv-how-do-you-decide-what-belongs-in-a-class, intermediate)
The cohesion judgment call, phrased as a design question rather than a SOLID recital.
- The question, and the cohesion judgment it's testing behind a simple phrasing (overview)
- Clarifying question: designing from scratch, or deciding whether to add a method to an existing class? (concept)
- The answer skeleton: group by what changes together and what data the behavior actually needs (concept) — cross-link: srp-single-responsibility
- Code: a method that takes a `Foo` and works entirely on its fields — it belongs on `Foo` (code)
- Code: a method that reaches into three unrelated classes' internals — it belongs on none of them; extract a new class (code)
- Compare: "feature envy" vs a well-placed method — the tell-tale signs (compare) — cross-link: common-code-smells
- Follow-up: "what if two classes both plausibly own this behavior?" (concept)
- Follow-up: "does a class with only static/utility methods count as a class at all?" (concept)
- Weak answer: "if it's related to the class, put it there" — too vague to apply live (pitfall)
- Wrong answer: defaulting new behavior into an existing "Manager"/"Util" class instead of asking where it actually belongs (pitfall)
- The 60-second version (concept)

### Topic: Explain the Liskov substitution violation in this code (iv-liskov-violation-in-this-code, advanced)
The live-code-reading version of LSP — spot it, name the consequence, fix it.
- The question, and the live-code-reading skill behind it (overview)
- Clarifying question: the classic Square-extends-Rectangle, or a business-domain example? (concept)
- The answer skeleton: find the override that strengthens a precondition or weakens a postcondition, then name the caller that breaks (concept) — cross-link: lsp-liskov-substitution
- Code: `Square extends Rectangle`, overriding `setWidth` — breaks an invariant the base class promised (code)
- Code: the caller that breaks — a loop assuming `setWidth` and `setHeight` vary independently (code)
- Diagram: substitutability as a contract — the subtype must honor every promise the base type made (diagram)
- Code: the fix — model `Square` and `Rectangle` as siblings under a `Shape` interface instead of one extending the other (code)
- Follow-up: "is throwing `UnsupportedOperationException` in an override always an LSP violation?" (concept)
- Follow-up: "how do you catch this in review before it ships?" — look for overrides that narrow behavior (concept)
- Weak answer: naming "LSP violation" correctly but never pointing at the specific broken caller (pitfall)
- Wrong answer: "fixing" it by adding a type-check in the caller instead of fixing the hierarchy (pitfall)
- The 60-second version (concept)

### Topic: Deep copy vs shallow copy — when does the difference actually bite? (iv-deep-vs-shallow-copy, intermediate)
The bug story, not the definition — a shared mutable reference silently corrupting two "independent" objects.
- The question, and the bug story it's fishing for over the definition (overview)
- Clarifying question: copying a flat object, or one with nested mutable collections? (concept)
- The answer skeleton: shallow copies the reference, deep copies the structure — then the concrete bug (concept)
- Code: a shallow-copied object whose nested list mutation leaks into the "original" (code)
- Code: the same class with a correct deep copy (constructor copy or copy-on-write) (code)
- Diagram: two objects pointing at one shared mutable list vs two independent lists (diagram)
- Follow-up: "does every field need deep copying, or only the mutable ones?" (concept)
- Follow-up: "how does this interact with immutability — do immutable objects need copying at all?" (concept) — cross-link: immutability-as-a-design-tool
- Follow-up: "what does a language's default `clone()`/copy constructor give you — shallow or deep?" (concept)
- Weak answer: "always deep copy to be safe" — no cost acknowledged, and not always possible (pitfall)
- Wrong answer: assuming a language's built-in clone is deep by default (pitfall)
- The 60-second version (concept)

### Topic: When do you make a class final, or seal a hierarchy? (iv-when-to-make-a-class-final, intermediate)
The design-intent signal a final/sealed keyword sends, not just the syntax.
- The question, and the design-intent signal it's really asking about (overview)
- Clarifying question: final to prevent inheritance entirely, or sealed to allow a closed, known set of subtypes? (concept)
- The answer skeleton: name the intent — this class's invariants aren't safe to extend — then the two situations where it's the right call (concept)
- Diagram: final (no subclassing at all) vs sealed (a fixed, known set of subclasses) — the shape of each (diagram)
- Code: an immutable value class marked `final` so a subclass can't reintroduce mutability (code)
- Code: a sealed hierarchy enumerating every subtype, enabling exhaustive pattern matching (code)
- Follow-up: "doesn't this hurt testability — you can't subclass to mock?" — compose an interface instead (concept) — cross-link: dependency-injection-and-testability
- Follow-up: "how does this differ from just documenting 'don't extend this'?" — compiler-enforced vs convention (concept)
- Follow-up: "is there a runtime/JIT benefit to final, or is it purely a design signal?" (concept)
- Weak answer: marking everything final "for safety" with no actual invariant at risk (pitfall)
- Wrong answer: sealing a hierarchy that's expected to grow with plugins contributed from outside the codebase (pitfall)
- The 60-second version (concept)

## Group: LLD Interview Bank — Principles (interview-lld-principles)

*Applying SOLID and its neighbors under interview pressure — naming a violation, defending a call, knowing when a principle doesn't apply.*

### Topic: Can you explain SOLID with a real example? (iv-explain-solid-with-example, beginner)
One example per letter is weak; one example threading through all five is the strong answer.
- The question, and why "one example" beats five definitions (overview)
- Clarifying question: one example per letter, or one example threading through all five? (concept)
- The answer skeleton: pick one small domain (a notification sender) and thread it through all five letters (concept)
- Code: the same class shown before/after each principle is applied (code) — cross-link: srp-single-responsibility
- Diagram: the five principles as five separate refactors on one class (diagram)
- Code: the fully-refactored version with all five applied together, and how it reads end to end (code)
- Compare: which principle addresses which smell — a quick lookup table (compare)
- Follow-up: "which one do you reach for first in practice?" (concept)
- Follow-up: "give me a case where two principles pull in different directions" (concept)
- Follow-up: "how would you explain SOLID to someone who's never heard the acronym, in one breath?" (concept)
- Weak answer: five disconnected textbook definitions, no shared example (pitfall)
- Wrong answer: treating all five as strict rules that must always apply equally, regardless of context (pitfall)
- The 60-second version (concept)

### Topic: Which SOLID principle does this code violate? (iv-spot-solid-violation, intermediate)
The live-code-reading skill: name the smell first, then map it to the principle.
- The question, and the live-code-reading skill it tests (overview)
- Clarifying question: are they handing you a snippet now, or asking you to imagine one? (concept)
- The answer skeleton: name the smell first, then map it to the principle, then propose the fix (concept) — cross-link: common-code-smells
- Code: a class with three unrelated responsibilities — spot the SRP violation (code)
- Code: a subclass that throws on a parent method — spot the LSP violation (code) — cross-link: lsp-liskov-substitution
- Code: a `switch` that grows a case every time a new type ships — spot the OCP violation (code)
- Follow-up: "it violates two principles at once — which do you fix first?" (concept)
- Follow-up: "how would you refactor this live, in under two minutes?" (concept)
- Follow-up: "what if you're not sure which letter it is — does it matter for the fix?" (concept)
- Weak answer: naming a principle without pointing at the specific line that violates it (pitfall)
- Wrong answer: naming a violation that isn't actually there, to look sharp under pressure (pitfall)
- The 60-second version (concept)

### Topic: Is SRP always the right call? (iv-is-srp-always-right, intermediate)
A confident "no, and here's the counter-case" beats parroting the principle.
- The question, and why a confident "no" beats parroting the principle (overview)
- Clarifying question: "always" in what sense — codebase size, team size? (concept)
- The answer skeleton: state the principle, then the counter-case, then the actual rule of thumb (concept) — cross-link: srp-single-responsibility
- Code: a class split into four pieces that's now harder to navigate than the original (code)
- Code: the same class kept as one cohesive unit, and why that's the right call at this size (code)
- Follow-up: "how small is too small — what's your smell test?" (concept)
- Follow-up: "how does this interact with cohesion?" (concept) — cross-link: coupling-and-cohesion
- Follow-up: "does team size change where you draw this line?" (concept)
- Weak answer: "yes, always split responsibilities" — no nuance, reads junior (pitfall)
- Wrong answer: "SRP is overrated, keep everything in one class" — the opposite overcorrection (pitfall)
- The 60-second version (concept)

### Topic: How do you spot tight coupling in a design? (iv-spot-tight-coupling, intermediate)
The diagnostic skill: name concrete signals, not just the definition.
- The question, and the diagnostic skill behind it (overview)
- Clarifying question: coupling between classes, modules, or services? (concept)
- The answer skeleton: name 2-3 concrete signals, then a smell you'd point to in code (concept) — cross-link: coupling-and-cohesion
- Code: a class that `new`s its dependencies directly — the signal and the fix (code) — cross-link: dip-dependency-inversion
- Diagram: a dependency graph before/after decoupling via an interface (diagram)
- Code: a class coupled to a concrete data format — parsing raw JSON deep inside business logic — a second signal (code)
- Follow-up: "how do you measure this, not just eyeball it?" — fan-out, change amplification (concept)
- Follow-up: "is zero coupling the goal?" — no, coupling to abstractions is fine (concept)
- Follow-up: "how do you catch this without a metrics tool, just reading a diff?" (concept)
- Weak answer: defining coupling correctly but giving no concrete signal to look for (pitfall)
- Wrong answer: "coupling is always bad, eliminate every dependency" (pitfall)
- The 60-second version (concept)

### Topic: Give an example of DRY taken too far (iv-dry-gone-wrong, intermediate)
Tests judgment over rule-following — premature abstraction is the real answer.
- The question, and why this tests judgment over rule-following (overview)
- Clarifying question: DRY on code, or DRY on concepts that only look similar? (concept)
- The answer skeleton: describe premature abstraction, then the concrete failure (concept) — cross-link: dry-yagni-kiss
- Code: two unrelated features merged into one "shared" function that now has four boolean flags (code)
- Code: the fix — split back into two small functions, and accept the duplication (code)
- Follow-up: "how do you tell accidental duplication from essential duplication?" (concept)
- Follow-up: "what's the rule of three, and do you follow it strictly?" (concept)
- Follow-up: "what's the actual tell that an abstraction is premature versus genuinely needed?" (concept)
- Weak answer: "DRY is always good, just do it more carefully" — dodges the actual question (pitfall)
- Wrong answer: fixing an overloaded shared function by adding a fifth boolean flag instead of splitting it (pitfall)
- The 60-second version (concept)

### Topic: YAGNI vs designing for extensibility — how do you balance them? (iv-yagni-vs-extensibility, intermediate)
The tension between the two is the point; picking a side absolutely is the wrong answer.
- The question, and the tension it's asking you to hold (overview)
- Clarifying question: extensibility for a known near-term requirement, or speculative? (concept)
- The answer skeleton: YAGNI kills speculation, but seams for known variation are cheap — state the line (concept) — cross-link: dry-yagni-kiss
- Code: a design with one cheap seam (an interface) vs one expensive one (an unused plugin framework) (code)
- Code: the actual cost paid later when the speculative framework's guess about future variation turns out wrong (code)
- Follow-up: "how do you tell a cheap seam from an expensive one before building it?" (concept)
- Follow-up: "your PM says 'we'll definitely need X in Q3' — does that change your answer?" (concept)
- Follow-up: "what's a seam you can add later for near-zero cost if you get the boundary right today?" (concept)
- Weak answer: picking a side absolutely ("always YAGNI" or "always extensible") (pitfall)
- Wrong answer: building the generic plugin framework "just in case," before a second real use case exists (pitfall)
- The 60-second version (concept)

### Topic: What does dependency inversion look like in practice? (iv-dependency-inversion-in-practice, intermediate)
The "in practice" qualifier means they want code, not the definition.
- The question, and the "in practice" qualifier — they want code, not the definition (overview)
- Clarifying question: DIP the principle, or DI the pattern/framework? (concept) — cross-link: dip-dependency-inversion
- The answer skeleton: high-level module depends on an abstraction, low-level module implements it, wiring happens outside both (concept)
- Code: a service depending on a concrete `MySqlRepository` refactored to depend on a `Repository` interface (code)
- Diagram: the dependency arrow flipped — before and after (diagram)
- Code: the wiring — a small composition root that constructs the concrete instance and hands it in (code)
- Follow-up: "where does the wiring happen — who constructs the concrete instance?" (concept) — cross-link: dependency-injection-and-testability
- Follow-up: "does this always need a DI framework?" — no, constructor injection is enough (concept)
- Follow-up: "what changes at test time — how does this make the service unit-testable?" (concept)
- Weak answer: describing DIP correctly but calling it "the same thing as dependency injection" with no distinction (pitfall)
- Wrong answer: inverting the dependency on paper but still `new`-ing the concrete class inside the high-level module (pitfall)
- The 60-second version (concept)

### Topic: How do you decide which design principle applies when two conflict? (iv-resolving-conflicting-principles, advanced)
The senior-signal version of the SOLID questions.
- The question, and why this is the senior-signal version of the SOLID questions (overview)
- Clarifying question: can they give a concrete pair that's conflicting, e.g. SRP vs simplicity? (concept)
- The answer skeleton: name the conflict, name the actual cost of each choice, decide by the cost the codebase can least afford (concept)
- Code: a real conflict — ISP wants many small interfaces, but that fragments a cohesive API (code) — cross-link: isp-interface-segregation
- Code: the resolution actually chosen, and the cost that was accepted rather than eliminated (code)
- Follow-up: "walk me through how you'd explain this trade-off to a teammate who disagrees" (concept)
- Follow-up: "does team size or codebase age change the answer?" (concept)
- Follow-up: "how do you keep this from becoming a purely subjective argument in review?" (concept)
- Weak answer: treating principles as unbreakable laws instead of heuristics (pitfall)
- Wrong answer: treating the conflict as something to be "solved" perfectly instead of traded off (pitfall)
- The 60-second version (concept)

### Topic: What are the signs a class does too much? (iv-signs-a-class-does-too-much, intermediate)
The diagnostic checklist you name before you've even seen the code — distinct from spotting a violation in a given snippet.
- The question, and why it wants a checklist, not a definition of SRP (overview)
- Clarifying question: a mental checklist in general, or are they about to show you a specific class? (concept)
- The answer skeleton: name 3-4 concrete signals, not "it violates SRP" (concept) — cross-link: srp-single-responsibility
- Code: a class with an unrelated grab-bag of methods, annotated with which signal each one trips (code)
- Code: naming two different actors who'd each ask to change this class for unrelated reasons (code)
- Compare: the signals — constructor argument count, import count, reasons to change, test-setup complexity (compare)
- Follow-up: "which signal do you trust most when they disagree with each other?" (concept)
- Follow-up: "does a long class with one clear responsibility still count as 'too much'?" (concept)
- Follow-up: "how do you apply this signal-check live, in under a minute?" (concept)
- Weak answer: "it has too many lines" — line count isn't a responsibility signal (pitfall)
- Wrong answer: "count the methods — more than N is too many" as a hard rule (pitfall)
- The 60-second version (concept)

### Topic: How do you reduce coupling between two modules? (iv-reducing-coupling-between-modules, intermediate)
The practical toolkit — interfaces, events, a shared contract — not just "decouple it."
- The question, and why "just decouple it" isn't itself an answer (overview)
- Clarifying question: coupling between two classes, two modules, or two services? (concept)
- The answer skeleton: name the coupling type (data, control, temporal), then the specific tool that breaks it (concept) — cross-link: coupling-and-cohesion
- Code: module A calling module B's internals directly (code)
- Code: the same modules decoupled through a narrow interface owned by A, not B (code) — cross-link: dip-dependency-inversion
- Diagram: two modules going from a tangled two-way dependency to a one-way dependency on an abstraction (diagram)
- Follow-up: "what if the two modules genuinely need to react to each other's state changes?" — events/pub-sub as the decoupling tool (concept)
- Follow-up: "how do you decouple without adding a network hop when they're actually in the same process?" (concept)
- Follow-up: "how do you know when you've decoupled enough — is there a point of diminishing returns?" (concept)
- Weak answer: adding an interface with exactly one implementation and calling it "decoupled" while both still change together (pitfall)
- Wrong answer: "communicate through a shared database table" as the decoupling mechanism (pitfall)
- The 60-second version (concept)

### Topic: What does "open for extension, closed for modification" look like in practice? (iv-open-closed-in-practice, intermediate)
OCP as a design habit — add behavior without editing existing, tested code.
- The question, and why adding code beats editing existing code (overview)
- Clarifying question: closed against what kind of change — a new type, or a new rule? (concept) — cross-link: ocp-open-closed
- The answer skeleton: identify the axis of variation, then put an extension point there instead of a conditional (concept)
- Code: a `switch` on type that grows a new case every time a variant is added (code)
- Code: the same feature refactored so a new variant is a new class, zero edits to existing code (code) — cross-link: strategy-pattern
- Diagram: adding a fifth case — the switch version touches one file everywhere it's used; the OCP version touches nothing (diagram)
- Follow-up: "is OCP realistic for every kind of change, or only some axes?" (concept)
- Follow-up: "doesn't this just move the problem — now the registry/factory needs to know about the new class?" (concept)
- Follow-up: "how much abstraction do you build in before you actually have a second variant?" (concept)
- Weak answer: reciting "open for extension, closed for modification" with no example of the extension point (pitfall)
- Wrong answer: pre-building an extension point for an axis that has never actually varied (pitfall)
- The 60-second version (concept)

### Topic: Is inheritance a violation of encapsulation? (iv-does-inheritance-violate-encapsulation, advanced)
The real fragile-base-class argument, not a gotcha.
- The question, and the fragile-base-class argument it's actually asking about (overview)
- Clarifying question: field visibility specifically, or behavioral coupling to the base class's implementation? (concept)
- The answer skeleton: yes, partially — a subclass depends on the base class's implementation details, not just its contract (concept) — cross-link: encapsulation
- Code: a base class change that silently breaks a subclass relying on call order between two base methods (code)
- Diagram: the subclass's real dependency surface — the declared contract plus every implementation detail it happens to rely on (diagram)
- Code: the fix — the base class documents and freezes the call-order contract explicitly via template method (code) — cross-link: template-method-pattern
- Follow-up: "does composition fully avoid this?" — mostly, since you depend only on the public contract (concept) — cross-link: iv-why-composition-over-inheritance
- Follow-up: "what's `protected` actually for, then, if it leaks encapsulation?" (concept)
- Follow-up: "how do library authors protect public base classes from this?" — final methods, documented contracts (concept)
- Weak answer: "no, inheritance is fine, encapsulation is only about private fields" — misses the fragile-base-class problem (pitfall)
- Wrong answer: "yes, so never use inheritance" — overcorrecting past the actual, narrower claim (pitfall)
- The 60-second version (concept)

### Topic: How do you handle cross-cutting concerns like logging and auth checks? (iv-handling-cross-cutting-concerns, advanced)
Logging/auth/metrics scattered everywhere — name the tool that centralizes it.
- The question, and why cross-cutting concerns don't fit neatly into any one class (overview)
- Clarifying question: one specific concern (logging), or the general pattern? (concept)
- The answer skeleton: name 2-3 mechanisms (decorator, middleware/interceptor, AOP) and when each fits (concept) — cross-link: decorator-pattern
- Code: a business method with logging, auth check, and metrics all inlined, drowning the actual logic (code)
- Code: the same method with the concerns pulled into decorators/middleware around a clean core (code)
- Diagram: a request pipeline — auth, logging, metrics as stages wrapping the handler, not inside it (diagram)
- Follow-up: "what's the cost of this indirection — how do you debug through five wrapper layers?" (concept)
- Follow-up: "does this apply outside web request pipelines — what about a batch job?" (concept)
- Follow-up: "how does dependency injection help wire these consistently instead of by hand each time?" (concept)
- Weak answer: naming "logging is a cross-cutting concern" without naming a mechanism to centralize it (pitfall)
- Wrong answer: solving it with a global mutable logger/context object reached from everywhere (pitfall)
- The 60-second version (concept)

### Topic: When do you break a design principle on purpose? (iv-when-to-break-a-principle-on-purpose, advanced)
The senior-signal question — a principle you deliberately violated, and the reasoning that made it right.
- The question, and why this is one of the clearest senior-vs-mid signals in the room (overview)
- Clarifying question: a hypothetical, or a real story from your own work? (concept)
- The answer skeleton: name the principle, name the constraint that made following it worse, name what you did instead (concept)
- Code: a deliberately "impure" method mixing I/O and logic because splitting it added three files for no real benefit at this scale (code)
- Compare: the "by the book" version vs the pragmatic version — cost of each, at this team's actual size (compare)
- Follow-up: "how do you know this wasn't just laziness dressed up as pragmatism?" (concept)
- Follow-up: "would you make the same call in a codebase ten times bigger?" (concept)
- Follow-up: "how do you leave a trail so the next person knows this was deliberate, not an oversight?" (concept)
- Weak answer: "I never break principles" — reads as rigid, not senior (pitfall)
- Wrong answer: naming a violation that was actually just a mistake, retroactively dressed up as "a deliberate trade-off" (pitfall)
- The 60-second version (concept)

## Group: LLD Interview Bank — Design Patterns (interview-lld-patterns)

*Picking, defending, and critiquing design patterns live — not reciting the GoF catalog.*

### Topic: Given this scenario, which design pattern would you use? (iv-which-pattern-would-you-use, intermediate)
The pattern-matching skill: name what varies before naming a pattern.
- The question, and the pattern-matching skill it's actually testing (overview)
- Clarifying question: what's varying — behavior, construction, or structure? (concept)
- The answer skeleton: name what varies, map it to a pattern family, name the specific pattern (concept)
- Code: a scenario (pluggable payment methods) walked from problem to Strategy (code) — cross-link: strategy-pattern
- Diagram: a pattern-family map — creational vs structural vs behavioral, and which question each answers (diagram)
- Code: a second scenario (runtime-selectable notification channels) landing on the same Strategy shape (code)
- Compare: Strategy vs Factory vs Observer — which axis of variation each one actually addresses (compare)
- Follow-up: "what if two patterns both fit — how do you choose?" (concept)
- Follow-up: "what would make you NOT reach for a pattern here?" (concept) — cross-link: over-engineering-and-pattern-happy-design
- Follow-up: "how do you say the pattern name out loud without sounding like keyword-matching?" (concept)
- Weak answer: naming a pattern by vibe without explaining why it fits this scenario (pitfall)
- Wrong answer: naming a pattern whose structure doesn't actually match what's varying in this scenario (pitfall)
- The 60-second version (concept)

### Topic: Strategy vs State pattern — what's the actual difference? (iv-strategy-vs-state-pattern, intermediate)
Same class diagram, different intent — who changes it, when, and why.
- The question, and why they look identical in a class diagram (overview)
- Clarifying question: do they want the structural difference or the intent difference? (concept)
- The answer skeleton: same shape, different intent — caller picks vs object transitions itself (concept) — cross-link: strategy-pattern
- Code: the same class diagram used for a Strategy (sort algorithm) and a State (order lifecycle) (code) — cross-link: state-pattern
- Code: the State version actually transitioning itself — the `next()` call that swaps the current state object (code)
- Compare: Strategy vs State — who changes it, when, and why (compare)
- Follow-up: "can a state also change its own strategy?" — yes, and that's a hybrid, not a bug (concept)
- Follow-up: "how do you tell, from the requirement's wording alone, whether it's describing states or strategies?" (concept)
- Weak answer: "they're basically the same pattern" with no intent distinction (pitfall)
- Wrong answer: implementing a lifecycle with a `state` enum and a giant `switch`, instead of real State objects (pitfall)
- The 60-second version (concept)

### Topic: Factory vs Builder — when do you reach for each? (iv-factory-vs-builder, intermediate)
The "when," not the definitions, is what separates a strong answer.
- The question, and the "when" that separates it from a definitions question (overview)
- Clarifying question: simple object creation, or an object with many optional parts? (concept)
- The answer skeleton: Factory hides which class, Builder hides how assembly happens step by step (concept) — cross-link: factory-method-and-abstract-factory
- Code: a telescoping constructor refactored to a Builder (code) — cross-link: builder-pattern
- Code: a Factory picking between subclasses by input type (code)
- Code: a Builder that validates required fields and throws only at `build()`, not on every setter call (code)
- Follow-up: "can you combine them — a Factory that returns a Builder pre-seeded for a variant?" (concept)
- Follow-up: "when is a plain static factory method — `of()`/`from()` — enough, with no full Factory class needed?" (concept)
- Weak answer: "Builder is just a fancier constructor" — misses the immutability/validation angle (pitfall)
- Wrong answer: reaching for a Builder on a class with only two optional fields — machinery you don't need yet (pitfall)
- The 60-second version (concept)

### Topic: What's wrong with Singleton, and how do you make it thread-safe? (iv-singleton-problems-and-thread-safety, advanced)
One of the most-asked pattern questions in LLD rounds — smell first, then the fix.
- The question, and why it's one of the most-asked pattern questions in LLD rounds (overview)
- Clarifying question: are they asking about the pattern's design smell, or the thread-safety mechanics? (concept)
- The answer skeleton: name the smells (hidden dependency, untestable, global state), then the thread-safety fix (concept) — cross-link: singleton-pattern
- Code: a naive singleton race condition under concurrent first access (code)
- Code: the fixed version — double-checked locking or an eager holder class (code) — cross-link: synchronization-techniques-in-oo-design
- Code: the enum-based singleton — the idiomatic fix that sidesteps the whole race entirely (code)
- Follow-up: "how do you unit test code that depends on a singleton?" (concept) — cross-link: dependency-injection-and-testability
- Follow-up: "what does a DI container replace this with?" (concept)
- Follow-up: "construction is now thread-safe — what still breaks if the singleton holds mutable state accessed by multiple threads later?" (concept)
- Weak answer: fixing thread safety but never addressing why Singleton is a smell in the first place (pitfall)
- Wrong answer: "just make every field volatile" as a substitute for actually protecting the invariant (pitfall)
- The 60-second version (concept)

### Topic: Decorator vs inheritance for extending behavior — which and why? (iv-decorator-vs-inheritance, intermediate)
The combinatorial-explosion story is what the interviewer wants to hear.
- The question, and the combinatorial-explosion story it's fishing for (overview)
- Clarifying question: is the behavior added at compile time or does it need to vary at runtime? (concept)
- The answer skeleton: inheritance explodes combinatorially, Decorator composes at runtime — show the counting (concept) — cross-link: decorator-pattern
- Code: a beverage/topping-style class hierarchy that explodes with N toppings (code)
- Code: the same feature as stacked Decorators (code)
- Code: a Decorator that needs to add a new method beyond the shared interface — where the pattern starts to strain (code)
- Follow-up: "does this always beat inheritance — what's the cost of decorators?" — many small wrapper objects, harder to debug the stack (concept)
- Follow-up: "how do you debug a five-layer decorator stack when something's wrong?" (concept)
- Weak answer: reciting the pattern name without showing the combinatorial blow-up it solves (pitfall)
- Wrong answer: stacking decorators in an order that silently changes behavior, without documenting that order matters (pitfall)
- The 60-second version (concept)

### Topic: Observer pattern and memory leaks — what goes wrong? (iv-observer-pattern-memory-leaks, advanced)
A production-bug story you've actually hit, not a definition.
- The question, and the production-bug story it's testing you've actually hit (overview)
- Clarifying question: are we talking a GC'd language or one with manual memory management? (concept)
- The answer skeleton: name the leak mechanism (subject holds a strong ref to a dead observer), then the fix (concept) — cross-link: observer-pattern
- Code: an observer that's never unsubscribed, keeping a whole UI screen alive (code)
- Code: the fix — weak references or explicit unsubscribe in a lifecycle hook (code)
- Code: a subject that snapshots its observer list before notifying, avoiding a mutation-during-iteration crash when an observer unsubscribes mid-notify (code)
- Follow-up: "how do reactive/event-bus frameworks handle this for you?" (concept)
- Follow-up: "how would you detect this leak happened, after the fact — what does the heap dump look like?" (concept)
- Weak answer: describing the pattern correctly but never naming why it leaks (pitfall)
- Wrong answer: "just trigger garbage collection manually" instead of removing the dangling reference (pitfall)
- The 60-second version (concept)

### Topic: When is a design pattern the wrong answer? (iv-when-patterns-are-the-wrong-answer, advanced)
Why senior candidates get asked this specifically — the cost of a pattern, not just its benefit.
- The question, and why senior candidates get asked this specifically (overview)
- Clarifying question: wrong for this codebase, or wrong in general for the problem shape? (concept)
- The answer skeleton: name the cost of a pattern (indirection, more files, cognitive load) and the threshold where it's not worth paying (concept) — cross-link: over-engineering-and-pattern-happy-design
- Code: a one-line conditional turned into a four-class Strategy hierarchy for no reason (code)
- Follow-up: "how do you walk that back once it's already in the codebase?" (concept) — cross-link: refactoring-to-fix-smells
- Code: the walked-back version, collapsed back to the plain conditional (code)
- Follow-up: "what's the actual cost of the over-engineered version — onboarding time, file count, review time?" (concept)
- Follow-up: "how do you tell a pattern applied preemptively from one applied because it was actually needed?" (concept)
- Weak answer: "patterns are always good practice" — the opposite of the senior signal they want (pitfall)
- Wrong answer: refusing to ever use a named pattern out of fear of over-engineering, even when one genuinely fits (pitfall)
- The 60-second version (concept)

### Topic: Name a design pattern you've used in a real framework and explain it (iv-pattern-in-a-real-framework, intermediate)
"I've actually seen this" beats a textbook answer.
- The question, and why "I've actually seen this" beats a textbook answer (overview)
- Clarifying question: framework you've used personally, or any well-known one? (concept)
- The answer skeleton: name the framework, name the pattern, explain the mechanism in your own words (concept)
- Code: sketch of the pattern as it appears in a familiar framework (a builder-style config API, or an observer-based event system) (code)
- Code: a second, different example from another layer — a DI container using a Factory internally to build the object graph (code)
- Follow-up: "why did the framework authors choose that pattern over the alternative?" (concept)
- Follow-up: "what would you change about it if you designed it today?" (concept)
- Follow-up: "how do you spot these patterns quickly in an unfamiliar codebase?" (concept)
- Weak answer: naming a pattern you can't actually trace through real code (pitfall)
- Wrong answer: calling something a Factory pattern just because a class name contains the word "Factory" (pitfall)
- The 60-second version (concept)

### Topic: Refactor this if/else chain (iv-refactor-this-if-else-chain, intermediate)
The live-refactor skill: recognize the axis of variation, apply the smallest pattern that fits.
- The question, the live-refactoring format it comes in, and what it's really testing (overview)
- Clarifying question: is the chain branching on type, on state, or on a config flag? (concept)
- The answer skeleton: name the axis, name the smallest pattern that fits, don't over-apply (concept)
- Code: the original if/else chain branching on a type field (code)
- Code: step one — extract each branch into its own method (code)
- Code: step two — replace the chain with polymorphic dispatch or a lookup map of Strategy objects (code) — cross-link: strategy-pattern
- Diagram: the refactor as three steps — extract, classify, replace (diagram)
- Compare: a lookup map of lambdas vs a full Strategy class hierarchy — when each is enough (compare)
- Follow-up: "what if the branches share 80% of their logic?" — template method pulls the shared part up (concept) — cross-link: iv-template-method-vs-strategy
- Follow-up: "how do you do this live without breaking existing tests mid-refactor?" (concept)
- Weak answer: refactoring correctly but never naming the pattern you landed on (pitfall)
- Wrong answer: replacing a two-branch if/else that will never grow with a full Strategy hierarchy (pitfall)
- The 60-second version (concept)

### Topic: How would you make this extensible without editing it? (iv-extensible-without-editing-existing-code, intermediate)
The live design move behind Open/Closed — building the actual seam, not just naming the principle.
- The question, and how it differs from the OCP-definition question — this wants a live design move (overview) — cross-link: iv-open-closed-in-practice
- Clarifying question: extensible for a known, similar-shaped future case, or genuinely open-ended? (concept)
- The answer skeleton: find the seam, add an extension point (interface + registry), keep discovery separate from behavior (concept)
- Code: the closed, unextendable version — behavior baked into one method with no seam (code)
- Code: the same feature with a `Handler` interface and a registry callers register against (code)
- Diagram: a new handler being added — zero edits to the dispatch code, one new registration line (diagram)
- Follow-up: "how do handlers get registered — hardcoded list, config, or auto-discovery?" (concept)
- Follow-up: "what happens if two handlers both claim they can handle the same input?" (concept)
- Follow-up: "does this still work if handlers must run in a specific order?" (concept) — cross-link: chain-of-responsibility-pattern
- Weak answer: adding an `if isNewCase` branch "for now" instead of building the seam (pitfall)
- Wrong answer: building a fully generic plugin framework for a feature that only ever needed two variants (pitfall)
- The 60-second version (concept)

### Topic: Template Method vs Strategy — what's the actual difference? (iv-template-method-vs-strategy, intermediate)
Both let one step vary; the distinction is inheritance vs composition, and who controls the algorithm's shape.
- The question, and why they look like the same idea from a distance (overview)
- Clarifying question: is the varying step a small piece of a fixed algorithm, or the whole algorithm? (concept)
- The answer skeleton: Template Method fixes the skeleton in the base class and lets a subclass override one step; Strategy delegates the entire algorithm to a composed object (concept) — cross-link: template-method-pattern
- Code: a Template Method — an abstract `process()` calling `validate()`, an overridden `transform()`, then `save()` (code)
- Code: the same feature as Strategy — the whole transform step injected as a collaborator (code) — cross-link: strategy-pattern
- Diagram: the call structure — base class calling back into itself (Template Method) vs delegating out to a collaborator (Strategy) (diagram)
- Compare: Template Method vs Strategy — inheritance vs composition, compile-time vs runtime swap (compare)
- Follow-up: "can you have both — a template method whose one step is itself a Strategy?" (concept)
- Follow-up: "which one is easier to unit test in isolation?" (concept)
- Follow-up: "how does the Hollywood principle — 'don't call us, we'll call you' — show up specifically in Template Method?" (concept)
- Weak answer: "Template Method is just Strategy with inheritance" — misses that the algorithm's shape lives in different places (pitfall)
- Wrong answer: using Template Method for a step that must change at runtime per request, when the structure actually demands composition (pitfall)
- The 60-second version (concept)

### Topic: How do you avoid a pattern explosion? (iv-avoiding-pattern-explosion, advanced)
Too many small classes from over-applying GoF patterns — the senior fix is consolidation, not more patterns.
- The question, and the "too many small classes" complaint it's responding to (overview)
- Clarifying question: is the complaint about class count, or about actually losing the control flow? (concept)
- The answer skeleton: name the cause — a pattern applied per method instead of per real axis of variation — then the consolidation fix (concept) — cross-link: over-engineering-and-pattern-happy-design
- Code: five tiny Strategy/Factory/Decorator classes for what's really one axis of variation (code)
- Code: the consolidated version — one parameterized class or a small set of functions replacing the five (code)
- Diagram: a class diagram with twelve boxes for three real concepts — the pattern-per-method anti-pattern (diagram)
- Follow-up: "how do you tell a real axis of variation from an imagined one before applying a pattern?" (concept)
- Follow-up: "does this mean fewer patterns are always better?" — no, name the actual trade-off (concept)
- Follow-up: "how do you walk this back in a codebase you didn't design, without a big-bang rewrite?" (concept) — cross-link: refactoring-to-fix-smells
- Weak answer: "just use fewer patterns" with no criterion for which ones to cut (pitfall)
- Wrong answer: merging unrelated concepts into one "generic" class to cut the count, creating a new coupling problem (pitfall)
- The 60-second version (concept)

### Topic: Which pattern is behind dependency injection? (iv-pattern-behind-dependency-injection, intermediate)
Checks that you understand DI isn't magic — a container running a Factory for you.
- The question, and why interviewers ask it to check DI isn't magic to you (overview)
- Clarifying question: the container's internals, or the pattern DI itself embodies? (concept) — cross-link: dependency-injection-and-testability
- The answer skeleton: DI is Dependency Inversion applied via a Factory (or Abstract Factory) the container runs for you (concept) — cross-link: factory-method-and-abstract-factory
- Code: manual dependency wiring — a hand-written factory function doing what a container automates (code)
- Code: the same wiring expressed as constructor injection, with a container resolving the graph (code)
- Code: the anti-pattern — a static Service Locator called from deep inside business logic, hiding the real dependencies (code)
- Diagram: the DI container as a large Factory building a dependency graph from registrations (diagram)
- Follow-up: "is Service Locator the same thing?" — no, and here's the difference that matters (concept)
- Follow-up: "why does Service Locator make unit testing harder than constructor injection?" (concept)
- Follow-up: "what pattern handles object lifetime — singleton vs per-request scope — inside the container?" (concept)
- Weak answer: "DI is a pattern" — DI is a technique; the container's mechanism is what implements a pattern (pitfall)
- Wrong answer: conflating Service Locator (pull) with Dependency Injection (push) as the same approach (pitfall)
- The 60-second version (concept)

### Topic: Adapter vs Facade — in a real migration, which and why? (iv-adapter-vs-facade-real-migration, intermediate)
A real migration story — Adapter bridges an old interface to a new one, Facade simplifies a complex subsystem.
- The question, and why "in a real migration" pushes past textbook definitions (overview)
- Clarifying question: replacing one dependency with another, or hiding a complex subsystem behind one entry point? (concept)
- The answer skeleton: Adapter makes an incompatible interface fit an expected one; Facade simplifies a complex API into one — name which problem you actually have (concept)
- Code: an old `LegacyPaymentGateway` interface adapted to the app's new `PaymentProvider` interface without touching either (code) — cross-link: adapter-pattern
- Code: the migration's second half — a `PaymentFacade` hiding retries, logging, and provider selection behind one call (code) — cross-link: facade-pattern
- Diagram: the migration path — callers → Facade → Adapter → legacy gateway, swapped incrementally (diagram)
- Compare: Adapter vs Facade — interface incompatibility vs interface complexity (compare)
- Follow-up: "can you strangle the legacy system out entirely using this same seam?" — the strangler-fig approach (concept)
- Follow-up: "what if you need to adapt more than one legacy provider at once?" (concept)
- Follow-up: "how do you test the adapter without hitting the real legacy system?" (concept)
- Weak answer: using "Adapter" and "Facade" interchangeably because both "wrap" something (pitfall)
- Wrong answer: putting business logic inside the Adapter instead of keeping it a pure interface translation (pitfall)
- The 60-second version (concept)

## Group: LLD Interview Bank — Concurrency (interview-lld-concurrency)

*Making a class thread-safe on the whiteboard — the concurrency questions LLD rounds actually ask.*

### Topic: How would you make this class thread-safe? (iv-make-this-class-thread-safe, advanced)
The open-ended live-coding format: name the invariant at risk before reaching for a lock.
- The question, and the open-ended live-coding format it usually comes in (overview)
- Clarifying question: what's the actual race — shared mutable state, or just visibility? (concept)
- The answer skeleton: identify the invariant at risk, name the smallest fix that protects it (concept) — cross-link: designing-thread-safe-classes
- Code: an unsafe counter/cache class with the race made explicit (code)
- Code: the fixed version with the minimal synchronized region (code)
- Code: an alternative fix using `AtomicInteger`/`ConcurrentHashMap` instead of a lock, for comparison (code)
- Follow-up: "can you make this lock-free instead?" (concept) — cross-link: lock-free-and-atomic-object-design
- Follow-up: "what's the performance cost of your fix under contention?" (concept)
- Follow-up: "what invariant would still break if two fields must update together atomically?" (concept)
- Weak answer: synchronizing every method "to be safe" — coarse locking that kills throughput (pitfall)
- Wrong answer: "just use a `ConcurrentHashMap`" when the real bug is a check-then-act race across two calls, which no thread-safe collection alone fixes (pitfall)
- The 60-second version (concept)

### Topic: synchronized vs Lock vs atomic — how do you choose? (iv-synchronized-vs-lock-vs-atomic, advanced)
A decision table, not a preference — pick by what's actually shared.
- The question, and the decision-table it's really asking for (overview)
- Clarifying question: single variable, or multiple fields that must change together? (concept)
- The answer skeleton: atomic for a single variable, synchronized for simple mutual exclusion, explicit Lock for advanced control (concept)
- Code: the same increment problem solved three ways (code)
- Compare: synchronized vs Lock vs atomic — fairness, interruptibility, composability (compare) — cross-link: synchronization-techniques-in-oo-design
- Code: a case where none of the three alone is enough — a compound check-and-update across two atomics that still needs a lock (code)
- Follow-up: "when would you need tryLock or a timeout?" (concept)
- Follow-up: "what does 'composability' actually mean here — why can't you compose two atomic ops into one atomic op?" (concept)
- Weak answer: picking one tool for everything without naming the trade-off (pitfall)
- Wrong answer: replacing a `synchronized` block with a `Lock` for no reason other than "Lock is newer" (pitfall)
- The 60-second version (concept)

### Topic: How does immutability answer a concurrency question? (iv-immutability-as-concurrency-answer, intermediate)
"Just make it immutable" is a legitimate answer — up to a boundary you must name.
- The question, and why "just make it immutable" is a legitimate concurrency answer (overview)
- Clarifying question: is the whole object immutable, or just the parts that need to be shared? (concept)
- The answer skeleton: no shared mutable state means no race, full stop — then the boundary case (concept) — cross-link: immutability-as-a-design-tool
- Code: a mutable shared config replaced by an immutable snapshot swapped atomically (code)
- Diagram: a mutable object needing a lock on every read vs an immutable one needing none (diagram)
- Code: the boundary case — an object too large to copy cheaply on every update (code)
- Follow-up: "what if the object is too big to copy on every update?" — persistent data structures, copy-on-write (concept)
- Follow-up: "what if the object references something mutable underneath — is it really immutable?" (concept)
- Weak answer: claiming immutability solves concurrency for a class that still has a mutable field inside it (pitfall)
- Wrong answer: "immutable objects never need any synchronization" — ignoring safe-publication requirements for the reference itself (pitfall)
- The 60-second version (concept)

### Topic: Walk me through a deadlock in this object graph (iv-deadlock-in-object-graph, advanced)
The tracing skill: name the cycle in THIS graph, not the four conditions in the abstract.
- The question, and the tracing skill it tests over pure definition (overview)
- Clarifying question: two threads, two locks — or is this a bigger graph? (concept)
- The answer skeleton: name the four deadlock conditions, then trace the specific cycle in this graph (concept)
- Diagram: two threads acquiring two locks in opposite order — the wait-for cycle (diagram)
- Code: the deadlocking transfer-between-accounts example (code)
- Code: the fix — a global lock ordering by account ID that removes the cycle (code)
- Follow-up: "how do you prevent it — ordering, timeout, or a single lock?" (concept)
- Follow-up: "how would you detect this happened in production?" — thread dumps, lock contention metrics (concept)
- Follow-up: "what's livelock, and how is it different from deadlock?" (concept)
- Weak answer: naming "deadlock" without tracing the actual cycle in the given graph (pitfall)
- Wrong answer: "fixing" it by wrapping everything in one giant lock, killing concurrency entirely (pitfall)
- The 60-second version (concept)

### Topic: What is double-checked locking and why is it tricky? (iv-double-checked-locking-explained, advanced)
The historical bug is the actual answer, not just the shape of the pattern.
- The question, and the historical bug it's actually about (overview)
- Clarifying question: which language/memory model — this was a real bug pre-Java-5 (concept)
- The answer skeleton: the naive version, the subtle half-constructed-object bug, the fix (concept)
- Code: double-checked locking without `volatile` — the reordering hazard (code)
- Code: the corrected version with `volatile` (code)
- Code: the simpler eager-holder alternative that sidesteps the whole problem (code) — cross-link: iv-thread-safe-singleton-implementation
- Follow-up: "why does volatile fix it — what does it actually guarantee?" (concept)
- Follow-up: "why did this only become reliably fixable in Java 5 — what changed in the memory model?" (concept)
- Weak answer: describing the pattern's shape without explaining why it was ever broken (pitfall)
- Wrong answer: assuming double-checked locking is unnecessary "in every language" because Java fixed its memory model — other runtimes have their own rules (pitfall)
- The 60-second version (concept)

### Topic: How do you implement a thread-safe singleton? (iv-thread-safe-singleton-implementation, intermediate)
Name 2-3 approaches, then pick the one you'd actually ship.
- The question, and why it's a rite-of-passage LLD question (overview)
- Clarifying question: lazy or eager initialization — does it matter here? (concept)
- The answer skeleton: name 2-3 approaches, pick the one you'd actually ship (concept) — cross-link: singleton-pattern
- Code: eager static holder (simplest, thread-safe by classloading) (code)
- Code: double-checked locking version, contrasted (code) — cross-link: iv-double-checked-locking-explained
- Code: the enum-based singleton as a third, simplest-of-all option (code)
- Follow-up: "which one would you actually use in production, and why?" (concept)
- Follow-up: "how does classloading itself guarantee thread safety for the eager/holder versions?" (concept)
- Weak answer: reaching for the most complex version by default instead of the simplest correct one (pitfall)
- Wrong answer: claiming lazy initialization is always necessary "for performance," when eager costs nothing for a cheap object (pitfall)
- The 60-second version (concept)

### Topic: Design a producer-consumer setup (iv-producer-consumer-design, advanced)
The bounded-buffer problem, solved with a tested primitive, not hand-rolled wait/notify.
- The question, and the bounded-buffer problem it's really asking you to solve (overview)
- Clarifying question: single or multiple producers/consumers? Bounded or unbounded queue? (concept)
- The answer skeleton: a shared bounded queue, block-on-full and block-on-empty, the coordination primitive (concept)
- Code: a producer-consumer with a blocking queue (code)
- Diagram: the buffer with wait conditions on both ends (diagram)
- Code: what hand-rolled wait/notify looks like, and the spurious-wakeup bug when the guard is an `if` instead of a `while` (code)
- Follow-up: "what if you can't block — how do you handle backpressure instead?" (concept) — cross-link: backpressure-and-dead-letter-handling
- Follow-up: "how would you scale this to multiple consumers safely?" (concept)
- Follow-up: "how do you size the bounded buffer — what happens if it's too small, or too large?" (concept)
- Weak answer: hand-rolling wait/notify incorrectly (missing the loop, spurious wakeup) instead of using a tested primitive (pitfall)
- Wrong answer: using an unbounded queue "to never block producers," trading a deadlock risk for an OOM risk (pitfall)
- The 60-second version (concept)

### Topic: volatile vs synchronized — what's the actual difference? (iv-volatile-vs-synchronized, advanced)
Visibility vs atomicity — the distinction that trips people up on a compound operation.
- The question, and the visibility-vs-atomicity distinction it's testing (overview)
- Clarifying question: are they asking about a single flag, or a compound operation? (concept)
- The answer skeleton: `volatile` guarantees visibility only, `synchronized` guarantees visibility and atomicity (concept)
- Code: a volatile boolean flag used correctly to stop a thread (code)
- Code: a volatile counter used incorrectly — increment is not atomic (code)
- Compare: volatile vs synchronized — what each actually guarantees (compare)
- Code: the fix for the counter — `AtomicInteger`, contrasted with the broken volatile version (code)
- Follow-up: "when is volatile enough, and when do you need more?" (concept)
- Follow-up: "does volatile give any ordering guarantee for other variables written before it — happens-before?" (concept)
- Weak answer: using volatile for a compound read-modify-write and thinking it's safe (pitfall)
- Wrong answer: assuming synchronized is always slower than volatile, so preferring volatile everywhere regardless of correctness (pitfall)
- The 60-second version (concept)

### Topic: Spot the race condition in this code (iv-spot-the-race-condition, intermediate)
The "spot it" skill, distinct from "make it thread-safe" — identify the exact interleaving before touching a fix.
- The question, the spot-the-bug format, and why naming it precisely beats a vague "not thread-safe" (overview)
- Clarifying question: a specific interleaving they want traced, or general hardening? (concept)
- The answer skeleton: find the shared mutable state, find the check-then-act or read-modify-write gap, narrate the exact interleaving (concept)
- Code: a `hasNext()`/`next()`-style check-then-act race between two threads (code)
- Diagram: an interleaving timeline — thread A checks, thread B acts, thread A then acts on stale information (diagram)
- Code: a lazy-initialization race — two threads both see null and both construct (code)
- Follow-up: "how do you reproduce this race reliably enough to write a test for it?" (concept)
- Follow-up: "does adding `synchronized` to just one of the two methods fix it?" — no, both sides of the race need protection (concept)
- Follow-up: "what tools would flag this automatically — a race detector, a linter?" (concept)
- Weak answer: saying "there's a race condition" without naming which two operations interleave (pitfall)
- Wrong answer: fixing only the read path with a lock, leaving the write path unprotected (pitfall)
- The 60-second version (concept)

### Topic: How do you design an object that's safe to share across threads? (iv-designing-an-object-safe-to-share, advanced)
Designing FOR safe publication from the start, not retrofitting a lock onto a broken class.
- The question, and the "design for it" framing — different from "fix this broken class" (overview)
- Clarifying question: shared read-mostly, or shared read-write? (concept)
- The answer skeleton: name the three strategies — immutability, confinement, synchronization — and pick by access pattern (concept) — cross-link: designing-thread-safe-classes
- Code: a class published safely via a `final` field set once in the constructor (safe publication) (code)
- Code: the unsafe version — a reference escaping through a non-final field before construction fully completes (code)
- Diagram: the three strategies laid out — immutable, confined to one thread, or synchronized (diagram)
- Follow-up: "what does 'safe publication' actually mean — why can a half-constructed object leak?" (concept)
- Follow-up: "how does thread confinement work in a UI framework, concretely?" (concept)
- Follow-up: "if you can't make it immutable, what's the smallest change that makes it safe to share?" (concept)
- Weak answer: adding `synchronized` everywhere as the default answer regardless of the access pattern (pitfall)
- Wrong answer: assuming a `final` field alone guarantees safe publication of everything the object transitively reaches (pitfall)
- The 60-second version (concept)

### Topic: When do you use a concurrent collection vs a lock? (iv-concurrent-collection-vs-lock, intermediate)
A concurrent collection protects itself — not your multi-step invariant across calls.
- The question, and the decision it's really testing — collection-level safety vs your own invariant (overview)
- Clarifying question: a single collection call, or several calls that must be atomic together? (concept)
- The answer skeleton: a concurrent collection protects itself, not a multi-step invariant spanning calls (concept)
- Code: a `ConcurrentHashMap` used safely for independent single-key operations (code)
- Code: the same map used unsafely for a check-then-act spanning two calls — still racy despite being "concurrent" (code)
- Code: the fix — `computeIfAbsent`/`compute` for atomic compound operations, or an external lock (code)
- Follow-up: "when would you reach for `CopyOnWriteArrayList` specifically?" — read-heavy, rarely-mutated lists (concept)
- Follow-up: "what's the cost of a concurrent collection over a plain one, even single-threaded?" (concept)
- Follow-up: "how do you decide between a concurrent collection and just synchronizing a plain one?" (concept)
- Weak answer: "I used a `ConcurrentHashMap` so it's thread-safe," as if that alone covers the surrounding logic (pitfall)
- Wrong answer: wrapping a `ConcurrentHashMap` in `synchronized` on every access, paying for two safety mechanisms at once for no gain (pitfall)
- The 60-second version (concept)

### Topic: How do you avoid blocking in a hot path? (iv-avoiding-blocking-in-a-hot-path, advanced)
Contention on a hot path — the senior answer is redesign, not "use a faster lock."
- The question, and why "use a faster lock" is the wrong altitude to answer at (overview)
- Clarifying question: is the bottleneck lock contention, I/O, or CPU work under the lock? (concept)
- The answer skeleton: name 2-3 redesign options — sharding the lock, lock-free structures, moving work off the hot path (concept)
- Code: a single global lock around a counter/cache under heavy contention (code)
- Code: the sharded version — striped locks, each protecting a slice of the state (code)
- Diagram: one lock serializing every thread vs N shards letting most threads proceed in parallel (diagram)
- Code: the lock-free version using a compare-and-swap loop instead of a lock (code) — cross-link: lock-free-and-atomic-object-design
- Follow-up: "when is a lock-free structure actually worth the complexity over sharding?" (concept)
- Follow-up: "what if the slow part is I/O, not the lock itself?" — move the I/O outside the critical section (concept)
- Weak answer: "just make the critical section shorter" with no concrete technique for how (pitfall)
- Wrong answer: reaching for a lock-free CAS loop before checking whether the critical section could simply be made smaller or sharded (pitfall)
- The 60-second version (concept)

### Topic: How do you test thread-safety? (iv-how-do-you-test-thread-safety, advanced)
The honest answer — tests can't prove absence of races, but a layered toolkit still helps.
- The question, and why "write a test and run it" is an incomplete answer (overview)
- Clarifying question: testing for a known suspected race, or general hardening before ship? (concept)
- The answer skeleton: name that tests can't prove absence of races, then the layered toolkit that actually helps (concept)
- Code: a stress test spinning up N threads hammering the same object to surface a race under load (code)
- Code: the same test made more reliable with a `CountDownLatch` forcing all threads to start simultaneously, maximizing interleaving (code)
- Diagram: the interleaving space a stress test samples vs the full space of possible thread schedules (diagram)
- Follow-up: "what does a race detector tool actually catch that a stress test might miss?" (concept)
- Follow-up: "how does code review catch races that testing can't?" — look for shared mutable state and missing synchronization (concept)
- Follow-up: "how do you make a flaky-under-load test reproducible enough to debug?" (concept)
- Weak answer: "I ran it in a loop 1000 times and it passed" as proof of thread safety (pitfall)
- Wrong answer: claiming a passing stress test proves the class is race-free (pitfall)
- The 60-second version (concept)

### Topic: When would you use a ReadWriteLock instead of a plain lock? (iv-readers-writer-lock-when-to-use, intermediate)
The read-heavy, write-rare access pattern it's built for.
- The question, and the read-heavy access pattern it's built for (overview)
- Clarifying question: what's the actual read:write ratio in this workload? (concept)
- The answer skeleton: multiple readers run concurrently, a writer gets exclusive access — pick it when reads dominate (concept)
- Code: a cache using a plain lock — readers block each other unnecessarily (code)
- Code: the same cache using a `ReadWriteLock` — readers proceed in parallel, writers still exclusive (code)
- Diagram: three readers holding the read lock simultaneously vs one writer holding the write lock alone (diagram)
- Follow-up: "what if writes become more frequent later — does this still pay off?" (concept)
- Follow-up: "can a reader upgrade to a writer safely?" — most implementations don't allow it directly, and why (concept)
- Follow-up: "how does this compare to just using a `ConcurrentHashMap` instead?" (concept) — cross-link: iv-concurrent-collection-vs-lock
- Weak answer: reaching for a `ReadWriteLock` without checking the actual read:write ratio first (pitfall)
- Wrong answer: assuming a `ReadWriteLock` is always faster than a plain lock, even under heavy write contention where it isn't (pitfall)
- The 60-second version (concept)

## Group: LLD Interview Bank — Small Design Probes (interview-lld-design-questions)

*The small "design this class/API" probes — not full case studies, just a clean class or interface sketch under 10 minutes.*

### Topic: Design a thread-safe cache API (iv-design-thread-safe-cache-api, advanced)
The API shape, not the eviction algorithm, is what's being scored here.
- The question, and how it differs from "design an LRU cache" — API shape over algorithm (overview)
- Clarifying question: what eviction policy, what's the concurrency requirement — reads >> writes? (concept)
- The answer skeleton: the interface first (get/put/remove), then the concurrency strategy (concept)
- Code: a minimal `Cache<K,V>` interface (code)
- Code: the implementation using a concurrent map plus a lock only around eviction (code) — cross-link: designing-thread-safe-classes
- Code: a thundering-herd fix — a per-key lock or a `computeIfAbsent`-based loader so concurrent misses for the same key don't all recompute (code)
- Follow-up: "how do you avoid a thundering herd on a cache miss?" (concept)
- Follow-up: "how does this differ from the LRU cache case study?" (concept) — cross-link: lru-cache
- Follow-up: "should `get` block on a miss, or return a future/promise?" (concept)
- Weak answer: designing the eviction algorithm in detail while ignoring the API contract asked for (pitfall)
- Wrong answer: exposing the internal lock or backing map directly on the public interface, breaking encapsulation (pitfall)
- The 60-second version (concept)

### Topic: Design an audit log API (iv-design-audit-log-api, intermediate)
Append-only, immutable records — mutability here defeats the point.
- The question, and the append-only, who-what-when shape it's testing (overview)
- Clarifying question: who consumes this — compliance queries, or just a write sink? (concept)
- The answer skeleton: an immutable `AuditEvent`, an append-only writer, a read side kept separate (concept)
- Code: the `AuditEvent` record and the `AuditLogger.record()` method signature (code) — cross-link: designing-public-apis
- Code: an append-only storage sketch — why update/delete methods are deliberately absent from the API (code)
- Follow-up: "how do you guarantee events aren't lost if the write fails mid-request?" (concept)
- Follow-up: "should this API be synchronous or fire-and-forget?" (concept)
- Follow-up: "how do you let compliance query 'who changed X' efficiently without scanning the whole log?" (concept)
- Weak answer: designing mutable audit records — defeats the point of an audit trail (pitfall)
- Wrong answer: logging the full before/after object graph on every event "to be thorough," bloating storage and risking leaked sensitive fields (pitfall)
- The 60-second version (concept)

### Topic: Design a plugin system (iv-design-plugin-system, advanced)
The extension-point design: a `Plugin` interface, a registry, and a lifecycle.
- The question, and the extension-point design it's testing (overview)
- Clarifying question: plugins loaded at startup, or hot-loaded at runtime? (concept)
- The answer skeleton: a `Plugin` interface, a registry, a lifecycle (register → init → execute → shutdown) (concept)
- Code: the `Plugin` interface and a registry that discovers/loads implementations (code)
- Diagram: the plugin lifecycle and where the host app calls in (diagram)
- Code: isolating a plugin's failure — a try/catch and timeout boundary around each call so one bad plugin can't take down the host (code)
- Follow-up: "how do you isolate a misbehaving plugin from crashing the host?" (concept)
- Follow-up: "how does this compare to just using Strategy?" (concept) — cross-link: strategy-pattern
- Follow-up: "how do you version the plugin interface without breaking already-shipped plugins?" (concept)
- Weak answer: designing a rigid plugin interface that requires a new host release for every plugin type (pitfall)
- Wrong answer: giving plugins direct access to host internals instead of a narrow, versioned interface (pitfall)
- The 60-second version (concept)

### Topic: Design a retry utility (iv-design-retry-utility, intermediate)
Resilience thinking packed into a small, pluggable API.
- The question, and why it's really testing resilience thinking in a small API (overview)
- Clarifying question: retry any failure, or only specific exception types? (concept)
- The answer skeleton: a `retry(operation, policy)` shape, backoff strategy as a pluggable policy (concept)
- Code: a `RetryPolicy` interface (maxAttempts, backoff) and the retry loop (code) — cross-link: retries-timeouts-and-backoff
- Code: jitter added to the backoff calculation, and why a fixed backoff causes a thundering herd of retries (code)
- Follow-up: "how do you avoid retrying a non-idempotent operation?" (concept) — cross-link: idempotency-and-exactly-once
- Follow-up: "how would you add jitter, and why does it matter?" (concept)
- Follow-up: "how do you decide which exceptions are retryable vs which should fail fast?" (concept)
- Weak answer: hardcoding the backoff instead of making it pluggable — fails the "utility" bar (pitfall)
- Wrong answer: retrying indiscriminately on every exception type, including ones that mean "don't retry" (e.g. a 400 Bad Request) (pitfall)
- The 60-second version (concept)

### Topic: Design a configuration abstraction (iv-design-config-abstraction, intermediate)
The goal is "callers never know the source" — file, env var, or remote service.
- The question, and the "don't leak the source" design goal it's testing (overview)
- Clarifying question: static config only, or does it need to support live reload? (concept)
- The answer skeleton: a `ConfigProvider` interface, callers never know if it's a file, env var, or remote service (concept) — cross-link: dip-dependency-inversion
- Code: a `ConfigProvider.get(key)` interface with a typed accessor, and two implementations (code)
- Code: a live-reload implementation swapping the underlying source without callers noticing (code)
- Follow-up: "how do you handle a config value changing while the app is running?" (concept)
- Follow-up: "how do you keep this testable without hitting a real config source?" (concept)
- Follow-up: "how do you handle a missing key — a default, an exception, or an optional?" (concept)
- Weak answer: reading `System.getenv()` directly all over the codebase instead of behind an abstraction (pitfall)
- Wrong answer: caching config values inside application code instead of behind the provider, so live reload silently stops working (pitfall)
- The 60-second version (concept)

### Topic: Design an undo mechanism (iv-design-undo-mechanism, intermediate)
The textbook Command-pattern application — an inverse operation, not a snapshot.
- The question, and why it's the textbook Command-pattern application (overview)
- Clarifying question: single-level undo, or a full undo/redo stack? (concept)
- The answer skeleton: encapsulate each action as a command with an inverse, keep a history stack (concept) — cross-link: command-pattern
- Code: a `Command` interface with `execute()`/`undo()`, and a `CommandHistory` stack (code)
- Code: a compound/macro command that groups several commands into one undoable unit (code)
- Follow-up: "what about actions that can't be cleanly inverted, like sending an email?" (concept)
- Follow-up: "how do you support redo after an undo?" (concept)
- Follow-up: "does undo need to survive a process restart, or is history purely in-memory?" (concept)
- Weak answer: storing full object snapshots for every action instead of an inverse operation, wasting memory (pitfall)
- Wrong answer: implementing undo by re-running the entire action history from scratch instead of storing per-command inverses (pitfall)
- The 60-second version (concept)

### Topic: Design a validation framework (iv-design-validation-framework, intermediate)
Composability is the point: rules combine, errors aggregate, nothing throws on the first miss.
- The question, and the composability it's really testing (overview)
- Clarifying question: field-level validation, or cross-field rules too? (concept)
- The answer skeleton: a `Rule<T>` interface, rules composed and run together, errors collected not thrown early (concept)
- Code: a `ValidationRule<T>` interface and a composite validator that runs all rules and aggregates errors (code) — cross-link: designing-errors
- Code: a cross-field rule that needs the whole object, not just one field, to evaluate (code)
- Follow-up: "how do you support rules that depend on more than one field?" (concept)
- Follow-up: "should validation throw or return a result object?" (concept)
- Follow-up: "how do you localize or template a validation error message?" (concept)
- Weak answer: throwing on the first failed rule instead of collecting all violations — poor UX for the caller (pitfall)
- Wrong answer: mixing validation logic into the domain object's constructor instead of a separate, composable validator (pitfall)
- The 60-second version (concept)

### Topic: Design an event bus (iv-design-event-bus, advanced)
Observer at API-design scale: publish/subscribe decoupling publishers from subscribers.
- The question, and how it's Observer at API-design scale (overview)
- Clarifying question: in-process only, or does this need to survive a process restart? (concept)
- The answer skeleton: a `publish`/`subscribe` API keyed by event type, decoupling publishers from subscribers (concept) — cross-link: observer-pattern
- Code: an `EventBus` interface (`publish(event)`, `subscribe(Class<T>, handler)`) and a simple in-memory implementation (code)
- Diagram: publishers and subscribers decoupled through the bus, neither knowing the other exists (diagram)
- Follow-up: "sync or async dispatch — what breaks if a handler throws?" (concept)
- Follow-up: "how does this differ from a message queue, and when do you need the queue instead?" (concept) — cross-link: queues-vs-pubsub
- Follow-up: "how do you avoid a memory leak from subscribers who never unsubscribe?" (concept) — cross-link: iv-observer-pattern-memory-leaks
- Weak answer: letting one slow subscriber block every other subscriber synchronously (pitfall)
- Wrong answer: having the bus swallow handler exceptions silently instead of surfacing or isolating the failure (pitfall)
- The 60-second version (concept)

### Topic: Design a rate-limiter class (iv-design-rate-limiter-class, advanced)
Class scope: a single-process `RateLimiter`, not the distributed system — the algorithm and the API around it.
- The question, and the class-scope framing — a single-process limiter, not the distributed version (overview) — cross-link: rate-limiter
- Clarifying question: per-key (per-user) limiting, or one global limiter? (concept)
- The answer skeleton: pick an algorithm (token bucket), define the API (`tryAcquire`), name what state it needs (concept)
- Code: a `RateLimiter` interface — `tryAcquire()` / `tryAcquire(n)` (code)
- Code: a token-bucket implementation — capacity, refill rate, last-refill timestamp (code)
- Diagram: the bucket filling over time and draining on each acquire (diagram)
- Code: making it thread-safe — the refill-then-acquire compound operation under a lock or CAS loop (code)
- Follow-up: "how do you extend this to per-user limiting without one lock per user exploding memory?" (concept)
- Follow-up: "token bucket vs sliding window — what's the actual behavioral difference at the boundary?" (concept)
- Follow-up: "what should `tryAcquire` do when it fails — throw, return false, or block?" (concept)
- Weak answer: hardcoding the algorithm with no interface, unable to swap token bucket for sliding window later (pitfall)
- Wrong answer: using a naive fixed-window counter that allows roughly 2x the limit right at the window boundary (pitfall)
- The 60-second version (concept)

### Topic: Design a connection pool (iv-design-connection-pool, advanced)
Class scope: the borrow/return API, sizing, and health checks — not a specific driver's implementation.
- The question, and the class-scope framing — a generic `ConnectionPool`, not a specific DB driver's pool (overview)
- Clarifying question: fixed size, or elastic between a min and max? (concept)
- The answer skeleton: the API (`borrow`/`release`), the internal free list, and what happens when the pool is exhausted (concept)
- Code: a `ConnectionPool<T>` interface — `borrow()`, `release(T)`, `close()` (code)
- Code: the implementation — a blocking queue of idle connections, created up to a max size (code)
- Diagram: the lifecycle of one connection — idle → borrowed → returned → idle, with periodic health checks (diagram)
- Code: a health check evicting a stale or broken connection instead of returning it to the pool (code)
- Follow-up: "what should `borrow()` do when the pool is exhausted — block with a timeout, or throw immediately?" (concept)
- Follow-up: "how do you prevent a caller who forgets to call `release()` from starving the pool?" (concept)
- Follow-up: "how do you size the pool — what's the actual formula, not just a guess?" (concept)
- Weak answer: a pool with no upper bound, letting it grow unbounded under load (pitfall)
- Wrong answer: handing out the raw connection with no wrapper, so a caller can close it directly and corrupt the pool's bookkeeping (pitfall)
- The 60-second version (concept)

### Topic: Design an ID generator class (iv-design-id-generator-class, intermediate)
Class scope: an in-process, thread-safe ID generator — a building block, distinct from a distributed Snowflake-style service.
- The question, and the class-scope framing — one process, not a distributed cluster (overview) — cross-link: design-unique-id-generator
- Clarifying question: do IDs need to be sortable/monotonic, or just unique? (concept)
- The answer skeleton: pick the property that matters (uniqueness, monotonicity, or both), then the smallest mechanism that gives it (concept)
- Code: a thread-safe monotonic counter-based generator using an atomic long (code)
- Code: a UUID-based generator, contrasted — uniqueness without coordination, but not sortable (code)
- Compare: counter vs UUID vs a composite (timestamp + counter) — sortability, size, coordination needed (compare)
- Follow-up: "what happens to a counter-based generator across a process restart?" (concept)
- Follow-up: "how does this change once more than one process needs to generate IDs?" (concept) — cross-link: design-unique-id-generator
- Follow-up: "does the ID need to be safe to expose to end users, or is it internal-only?" (concept)
- Weak answer: using a non-thread-safe counter with a plain increment, assuming single-threaded access that isn't guaranteed (pitfall)
- Wrong answer: using a random number generator "for uniqueness" without checking or handling the small but real collision case (pitfall)
- The 60-second version (concept)

### Topic: Design a state machine (iv-design-state-machine, intermediate)
A small class-level state machine — states, transitions, guards — the State pattern as a concrete, general-purpose API.
- The question, and why almost every domain object (order, ticket, connection) eventually needs one of these (overview)
- Clarifying question: a fixed, small set of states known upfront, or one that needs to be data-driven/configurable? (concept)
- The answer skeleton: model states and transitions explicitly, reject invalid transitions instead of silently allowing them (concept) — cross-link: state-pattern
- Code: a naive version — a `status` field mutated directly from anywhere, with no guard against invalid transitions (code)
- Code: the fix — a `StateMachine` with an explicit transition table and a `canTransition`/`transition` API (code)
- Diagram: the transition table as a graph — valid edges only, invalid ones rejected (diagram)
- Code: a guard condition on a transition — e.g. "can't ship an order that hasn't been paid" (code)
- Follow-up: "how do you handle a transition that has side effects, like sending an email?" (concept)
- Follow-up: "should this be one instance per object, or a shared machine definition all objects reference?" (concept)
- Weak answer: encoding states as separate booleans (`isPaid`, `isShipped`) instead of one explicit state field (pitfall)
- Wrong answer: allowing any transition and just logging a warning on an invalid one, instead of rejecting it outright (pitfall)
- The 60-second version (concept)

### Topic: Design a scheduler/cron abstraction (iv-design-scheduler-cron-abstraction, advanced)
Class scope: an in-process `schedule(task, trigger)` API — not a distributed job scheduler.
- The question, and the class-scope framing — an in-process task scheduler, not a distributed cron service (overview)
- Clarifying question: fixed-interval tasks, cron-expression tasks, or both? (concept)
- The answer skeleton: the API (`schedule(task, trigger)`), an internal priority queue by next-run-time, and the worker loop (concept)
- Code: a `Scheduler` interface — `schedule(Runnable, Trigger)`, `cancel(handle)` (code)
- Code: the implementation — a min-heap of next-fire-times, a single loop thread waking at the next deadline (code)
- Diagram: the priority queue reordering as tasks fire and reschedule themselves (diagram)
- Code: handling a task that takes longer than its own interval — skip, queue, or run concurrently (code)
- Follow-up: "what happens if the process was down when a scheduled time passed — catch up, or skip?" (concept)
- Follow-up: "how do you make one misbehaving task not block every other scheduled task?" (concept)
- Weak answer: using `Thread.sleep()` in a loop per task instead of a shared scheduling data structure (pitfall)
- Wrong answer: running every task on the same single thread with no isolation, so one slow task delays all others (pitfall)
- The 60-second version (concept)

### Topic: Design a feature-flag client (iv-design-feature-flag-client, intermediate)
Client scope: the SDK a service calls — `isEnabled`, caching, safe defaults — not the flag-management backend.
- The question, and the client-scope framing — the SDK a service calls, not the flag-management backend (overview)
- Clarifying question: simple on/off flags, or targeting rules by user/context? (concept)
- The answer skeleton: the API (`isEnabled(flag, context)`), a local cache with periodic refresh, a safe default on failure (concept)
- Code: a `FeatureFlagClient` interface — `isEnabled(String flag, Context ctx)` (code)
- Code: the implementation — cached flag definitions refreshed on an interval, evaluated locally without a network call per check (code)
- Diagram: the client refreshing from the backend on an interval, callers hitting the local cache in between (diagram)
- Follow-up: "what does `isEnabled` return if the backend is unreachable and the cache is stale?" — a safe default, never an exception (concept)
- Follow-up: "how do you support percentage rollouts deterministically, so the same user always gets the same result?" — hash the user ID (concept)
- Follow-up: "how do you test code behind a flag without hitting the real flag service?" (concept)
- Weak answer: calling the backend synchronously on every `isEnabled` check, adding latency and a new failure mode to every call site (pitfall)
- Wrong answer: letting a flag-evaluation failure throw and take down the calling code path, instead of degrading to a safe default (pitfall)
- The 60-second version (concept)

## Group: Distributed Systems Interview Bank — Foundations (interview-distributed-fundamentals)

*The distributed-systems viva underneath HLD — short, sharp questions probing whether you actually understand the primitives, not just the buzzwords.*

### Topic: Explain CAP theorem without the clichés (iv-explain-cap-without-cliches, intermediate)
"Pick two of three" as a universal law is the wrong answer — a partition is what forces the choice.
- The question, and why "pick two of three" is the wrong answer they're listening for (overview)
- Clarifying question: are they asking for the theorem, or for how you'd apply it to a specific system? (concept)
- The answer skeleton: define partition first, then show C and A are the only real choice during one (concept) — cross-link: cap-theorem-and-pacelc
- Diagram: a network partition forcing a choice between answering and staying consistent (diagram)
- Code: a request handler choosing to serve a possibly-stale read vs reject the request during a partition (code)
- Follow-up: "name a real system and which side of CAP it picked, and why" (concept)
- Follow-up: "what does PACELC add that CAP doesn't cover?" (concept)
- Follow-up: "does CAP even apply when there's no partition — what governs the trade-off then?" (concept)
- Weak answer: "you can only pick two of three" stated as a universal law, with no partition scenario (pitfall)
- Wrong answer: claiming a system can be "CA" — consistent and available, no partition tolerance — as a real deployable choice in a distributed system (pitfall)
- The 60-second version (concept)

### Topic: Strong vs eventual consistency in one sentence — then defend it (iv-strong-vs-eventual-one-sentence, intermediate)
The follow-up ("defend it") is the actual test — a concrete case where eventual is genuinely fine.
- The question, and why the follow-up ("defend it") is the actual test (overview)
- Clarifying question: one sentence for the definition, or for when to use each? (concept)
- The answer skeleton: the one-liner, then the concrete case where eventual is actually fine (concept)
- Code: a read-after-write staleness example a user would actually notice (code)
- Code: the fix — read-your-writes, routing reads to the primary right after a write, or a session token (code)
- Follow-up: "give an example where eventual consistency is a real bug, not just a UX nit" (concept)
- Follow-up: "what's the practical middle ground — read-your-writes, bounded staleness?" (concept)
- Follow-up: "how do you decide, per endpoint, which consistency level to actually use in a real system?" (concept)
- Weak answer: treating strong consistency as strictly "better" instead of a cost trade-off (pitfall)
- Wrong answer: assuming "eventual" means "eventually, within milliseconds" — no bound is guaranteed unless the system explicitly states one (pitfall)
- The 60-second version (concept)

### Topic: What's the first thing that breaks at scale? (iv-what-breaks-first-at-scale, intermediate)
An open-ended probe for scaling instincts — name the specific first bottleneck, not "everything."
- The question, and why it's an open-ended probe for scaling instincts (overview)
- Clarifying question: scale in what dimension — traffic, data volume, or team size? (concept)
- The answer skeleton: name the bottleneck category (usually the database), then the specific failure mode (concept)
- Diagram: a single database instance saturating connections as QPS grows (diagram)
- Code: a connection-pool-exhaustion error under load — the actual symptom engineers see first (code)
- Follow-up: "what's the very next thing that breaks after you fix that one?" (concept)
- Follow-up: "how do you find this before it breaks in production?" — load testing, capacity planning (concept)
- Follow-up: "does the answer change if the bottleneck is write-heavy vs read-heavy traffic?" (concept)
- Weak answer: a generic "everything breaks at scale" with no concrete first bottleneck named (pitfall)
- Wrong answer: jumping straight to "add a cache" without first diagnosing whether the database is actually the bottleneck (pitfall)
- The 60-second version (concept)

### Topic: Why is exactly-once delivery so hard? (iv-why-exactly-once-is-hard, advanced)
The impossibility result: an ack can always be lost after the effect, so you fall back to at-least-once + idempotency.
- The question, and the impossibility result it's actually testing (overview)
- Clarifying question: exactly-once processing, or exactly-once delivery specifically? (concept)
- The answer skeleton: the network can always fail after the effect but before the ack, so you get at-least-once + idempotency instead (concept) — cross-link: idempotency-and-exactly-once
- Diagram: the ack-lost-after-effect race that breaks true exactly-once (diagram)
- Code: a dedup-key check before applying an effect — the idempotent-consumer pattern in practice (code)
- Follow-up: "so what do real systems actually claim, and how?" — dedup keys, idempotent consumers (concept)
- Follow-up: "does a transactional outbox solve this?" (concept)
- Follow-up: "what happens if the dedup-key store itself is unavailable — do you drop the message or block?" (concept)
- Weak answer: claiming a specific queue technology "guarantees exactly-once" with no idempotency layer (pitfall)
- Wrong answer: deduping purely on message content instead of a unique ID, silently dropping legitimately repeated but distinct messages (pitfall)
- The 60-second version (concept)

### Topic: How do you detect a dead node? (iv-how-to-detect-a-dead-node, intermediate)
"You can't, for sure" is part of the correct answer — heartbeats are a heuristic, not proof.
- The question, and why "you can't, for sure" is part of the correct answer (overview)
- Clarifying question: detecting a crash, or a network partition that looks like a crash? (concept)
- The answer skeleton: heartbeats/timeouts as a heuristic, phi-accrual as the refinement, and the fundamental ambiguity (concept) — cross-link: failure-detection
- Diagram: a heartbeat timeout that could mean "dead" or "just slow/partitioned" (diagram)
- Code: a phi-accrual-style detector adapting its timeout threshold from observed heartbeat variance, instead of a fixed timeout (code)
- Follow-up: "what's the risk of declaring a live node dead too early?" — split-brain, duplicate work (concept) — cross-link: split-brain-and-quorum-loss
- Follow-up: "how does phi-accrual improve on a fixed timeout?" (concept)
- Follow-up: "what does the cluster do differently once it decides a node is dead — who takes over its work?" (concept)
- Weak answer: "ping it, if it doesn't respond it's dead" — no acknowledgment of the ambiguity (pitfall)
- Wrong answer: treating a single missed heartbeat as proof of death instead of requiring a sustained pattern (pitfall)
- The 60-second version (concept)

### Topic: What is a fencing token and why do you need one? (iv-what-is-a-fencing-token, advanced)
Built for the "the old leader isn't really dead" scenario — a lock timeout alone doesn't solve it.
- The question, and the "the old leader isn't really dead" scenario it's built for (overview)
- Clarifying question: is this in the context of a lock, or leader election? (concept)
- The answer skeleton: a monotonically increasing token issued on each lease grant, checked by the resource before applying a write (concept) — cross-link: distributed-coordination
- Diagram: a paused-then-resumed old leader writing with a stale token, rejected by the resource (diagram)
- Code: a storage layer rejecting a write whose token is behind the latest seen (code)
- Code: the lock/lease service issuing monotonically increasing tokens on each grant (code)
- Follow-up: "why doesn't a simple lock timeout alone solve this?" (concept)
- Follow-up: "does every resource need to check the token, or just some?" (concept)
- Weak answer: describing a lock/lease without the token check that actually prevents the stale write (pitfall)
- Wrong answer: using a timestamp as the fencing token instead of a monotonically increasing counter — clock skew can make it non-monotonic (pitfall)
- The 60-second version (concept)

### Topic: What is split-brain and how do you prevent it? (iv-what-is-split-brain, advanced)
Quorum is the answer they're steering toward — a partition producing two leaders.
- The question, and why quorum is the answer they're steering toward (overview)
- Clarifying question: split-brain in a leader-election system, or in replicated storage? (concept)
- The answer skeleton: a partition where both sides think they're the leader, then quorum as the fix (concept) — cross-link: split-brain-and-quorum-loss
- Diagram: a network partition producing two leaders, each accepting writes (diagram)
- Code: a quorum check before accepting a write — refusing when the minority side can't reach a majority (code)
- Follow-up: "what happens if you can't reach quorum on either side?" — the system should refuse writes (concept)
- Follow-up: "how does this relate to fencing tokens?" (concept) — cross-link: iv-what-is-a-fencing-token
- Follow-up: "what's the actual quorum formula, and why does it need to be more than half?" (concept) — cross-link: quorum-systems
- Weak answer: "just add more replicas" without explaining the quorum mechanism that actually prevents it (pitfall)
- Wrong answer: using an even number of nodes for the quorum group, which can still tie and can't always resolve a majority (pitfall)
- The 60-second version (concept)

### Topic: How does clock skew break distributed systems? (iv-clock-skew-problems, advanced)
"Just use NTP" is incomplete — wall-clock ordering across nodes stays unreliable regardless.
- The question, and why "just use NTP" is an incomplete answer (overview)
- Clarifying question: wall-clock ordering, or clock-based expiry/leases specifically? (concept)
- The answer skeleton: clocks drift and jump, so wall-clock ordering across nodes is unreliable — name the fix (logical clocks, bounded uncertainty) (concept) — cross-link: time-and-ordering
- Diagram: two events on different nodes whose wall-clock timestamps disagree with true order (diagram)
- Code: a lease expiry computed from local wall-clock time that's wrong on a skewed node (code)
- Code: the fix — using a monotonic clock for durations/timeouts, reserving wall-clock time only for display (code)
- Follow-up: "how do vector clocks or hybrid logical clocks help?" (concept)
- Follow-up: "how does Spanner's TrueTime approach this differently?" (concept)
- Follow-up: "what's the difference between a monotonic clock and a wall clock, and why does it matter here?" (concept)
- Weak answer: assuming NTP-synced clocks are close enough for correctness-critical ordering (pitfall)
- Wrong answer: using a wall-clock read to measure an elapsed duration instead of a monotonic clock (pitfall)
- The 60-second version (concept)

### Topic: What is idempotency and how do you implement it? (iv-what-is-idempotency-and-how, intermediate)
Define it precisely, then name the concrete mechanism to actually implement it.
- The question, and why it's asked right after "how do you retry safely" (overview)
- Clarifying question: idempotency of the whole request, or of one specific side effect within it? (concept) — cross-link: idempotency-and-exactly-once
- The answer skeleton: define it precisely — the same request applied N times has the same effect as once — then name the mechanism (concept)
- Code: a non-idempotent "charge card" endpoint that double-charges on a retried request (code)
- Code: the fix — an idempotency key stored with the result, short-circuiting a repeated request (code)
- Diagram: the idempotency-key table — request ID mapped to the result already produced (diagram)
- Follow-up: "does idempotency mean the response is identical, or just the side effect?" (concept)
- Follow-up: "how long do you keep an idempotency key around, and what happens after it expires?" (concept)
- Follow-up: "is a `PUT` idempotent by HTTP convention — does your implementation actually honor that?" (concept)
- Weak answer: "idempotent means safe to retry" — true but too vague to implement from (pitfall)
- Wrong answer: deduping on the request body's content instead of an explicit idempotency key, breaking on two legitimately identical-looking requests (pitfall)
- The 60-second version (concept)

### Topic: Why can't you just retry? (iv-why-cant-you-just-retry, intermediate)
The naive instinct challenged — retries alone can duplicate effects, worsen overload, and hide the real failure.
- The question, and the naive instinct it's pushing back on (overview)
- Clarifying question: retrying a read, or a write with a side effect? (concept)
- The answer skeleton: name three failure modes a bare retry introduces, then the fix each needs (concept)
- Code: a retry loop that double-submits a non-idempotent write on a timeout (code) — cross-link: idempotency-and-exactly-once
- Diagram: a retry storm — every client backing off at the same interval, hammering a recovering service in sync (diagram)
- Follow-up: "how does exponential backoff with jitter fix the retry-storm problem specifically?" (concept)
- Follow-up: "what's the difference between retrying at the client vs at a proxy/gateway layer?" (concept)
- Follow-up: "when should you NOT retry at all — fail fast instead?" (concept) — cross-link: circuit-breakers
- Weak answer: "just retry a few times with backoff" with no mention of idempotency (pitfall)
- Wrong answer: retrying indefinitely with no cap, turning a transient failure into an unbounded pile of in-flight requests (pitfall)
- The 60-second version (concept)

### Topic: What's a quorum, in one sentence? (iv-what-is-quorum-one-sentence, intermediate)
The one-sentence definition, then why it must be a majority — tied to split-brain and consistency.
- The question, and why interviewers want the one-sentence version first (overview)
- Clarifying question: quorum for reads/writes in a data store, or quorum for leader election? (concept) — cross-link: quorum-systems
- The answer skeleton: the one-liner — enough nodes agree that no two disjoint groups can both claim it — then the formula (concept)
- Code: a `write succeeds if acks >= (N/2)+1` check in a replication client (code)
- Diagram: two possible majority groups out of five nodes — why they must always overlap by at least one node (diagram)
- Follow-up: "why must read quorum + write quorum exceed N — what does that overlap guarantee?" (concept)
- Follow-up: "what happens to availability as you increase the quorum size?" (concept)
- Follow-up: "does an even number of nodes cause a problem here?" (concept)
- Weak answer: "quorum means most of the nodes agree" — true but missing the overlap guarantee that makes it useful (pitfall)
- Wrong answer: using exactly half the nodes as the quorum threshold, which can't prevent two disjoint halves from both succeeding (pitfall)
- The 60-second version (concept)

### Topic: How does a distributed lock actually fail? (iv-how-does-a-distributed-lock-fail, advanced)
The failure modes beyond "just use Redis/ZooKeeper" — the actual traps that show up under pressure.
- The question, and why it's the natural follow-up to "how would you implement a distributed lock" (overview) — cross-link: distributed-coordination
- Clarifying question: failing to acquire, or failing after already acquiring? (concept)
- The answer skeleton: name the three failure modes — lease expiry while still working, a partition hiding the holder, and no fencing on the resource (concept)
- Code: a client that pauses (GC, scheduling) past its lease expiry and keeps writing, unaware it lost the lock (code)
- Diagram: the paused-client timeline — lease expires, a second client acquires, both now believe they hold the lock (diagram)
- Code: the fencing-token fix at the resource, rejecting the stale writer (code) — cross-link: iv-what-is-a-fencing-token
- Follow-up: "does a longer lease TTL fix this?" — no, it just changes the size of the window, not whether the bug exists (concept)
- Follow-up: "how does this play out differently with a single Redis node vs a Redlock-style multi-node scheme?" (concept)
- Follow-up: "what's the safest thing to do if you're not sure whether you still hold the lock?" (concept)
- Weak answer: "use Redis with a TTL" as the complete answer, with no fencing and no pause-awareness (pitfall)
- Wrong answer: extending the lease from inside the critical section without checking whether it already expired (pitfall)
- The 60-second version (concept)

### Topic: What is back-pressure? (iv-what-is-back-pressure, intermediate)
The mechanism, not just the word — how a system signals "slow down" instead of silently queuing until it falls over.
- The question, and why "it's when a system is overloaded" is too vague to pass (overview)
- Clarifying question: back-pressure between two in-process components, or across a network boundary? (concept) — cross-link: backpressure-and-dead-letter-handling
- The answer skeleton: the receiver signals capacity back to the sender, and the sender slows down or sheds load instead of the queue growing unbounded (concept)
- Code: an unbounded queue between a fast producer and slow consumer, growing until it OOMs (code)
- Code: the fix — a bounded queue where `offer()` blocks or rejects once full, propagating the signal upstream (code)
- Diagram: back-pressure propagating up a chain of three services, each slowing the one before it (diagram)
- Follow-up: "what's the difference between back-pressure and just rate limiting?" (concept)
- Follow-up: "what should happen when back-pressure reaches the very first hop — the end user's request?" — reject with a clear error, don't silently drop (concept)
- Follow-up: "how does this show up in a reactive-streams API specifically?" (concept)
- Weak answer: "back-pressure means the system is slow" — describes a symptom, not the mechanism (pitfall)
- Wrong answer: "solving" overload by adding an unbounded buffer, which delays the crash instead of preventing it (pitfall)
- The 60-second version (concept)

### Topic: What does "at-least-once" force you to build? (iv-at-least-once-forces-what-you-build, advanced)
Given you're stuck with at-least-once delivery, name everything that forces you to build on top of it.
- The question, and why it's the practical follow-up to "why is exactly-once so hard" (overview) — cross-link: iv-why-exactly-once-is-hard
- Clarifying question: at-least-once delivery of messages, or at-least-once execution of a side-effecting handler? (concept)
- The answer skeleton: name the obligations it creates — idempotent handlers, no ordering guarantee either, and dedup storage (concept) — cross-link: idempotency-and-exactly-once
- Code: a handler processing the same message twice, once safely (idempotent) and once unsafely, side by side (code)
- Diagram: a message redelivered after a processing timeout, even though the first attempt actually succeeded (diagram)
- Follow-up: "does at-least-once also mean out-of-order delivery, or are those separate problems?" (concept)
- Follow-up: "how long do you need to remember 'already processed' IDs before it's safe to forget them?" (concept)
- Follow-up: "what's the cost of getting this wrong in production — what does the bug actually look like to a user?" (concept)
- Weak answer: "at-least-once just means messages might duplicate, that's fine" — no plan for handling the duplicates (pitfall)
- Wrong answer: assuming the message broker's offset/ack tracking alone prevents duplicate processing, without an idempotent handler (pitfall)
- The 60-second version (concept)

---

# Phase H — Interview question bank: HLD

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
- Walking it: layering read replicas on top — 100k read QPS, 10k reads/sec per replica → 10 replicas total, distributed across the shards (code)
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

---

# Phase I — Interview question bank: experience & round formats

## Group: Talking About Your Own Designs (design-experience-questions)

*The design-specific behavioral layer — questions about a real system you actually built, distinct from the generic STAR/leadership behavioral round (that lives in `behavioral`, Area 9 / `behavioral-interview`, Area 17). Cross-link: `sd-playbook` for the from-scratch design method; this group is "tell me about a design you already shipped," not "design X for me now."*

### Topic: Walk Me Through the Architecture of Something You Built (iv-walk-through-your-architecture, intermediate)
The opening question of nearly every senior+ system-design loop, and why a chronological build-log answer scores worse than a structured one.
- The question, verbatim, and why it's asked before any whiteboard prompt (overview)
- What's really being probed: can you own and explain a real system, not recite a textbook one (concept)
- Why "we used microservices and Kafka" name-dropping scores low without the why (concept)
- Structuring the answer: problem → constraints → key decisions → what changed over time (concept)
- Diagram: the answer shape as problem → decisions → outcome, not a feature timeline (diagram)
- Picking which system to talk about: the one with real trade-offs, not the biggest one (concept)
- Going deep on one decision when the interviewer asks "why" instead of restating the diagram (concept)
- Compare: a resume-recitation answer vs a decisions-and-trade-offs answer to the same prompt (compare)
- Follow-up: "what was the scale, actually?" — having real numbers ready (concept)
- Pitfall: an answer with no numbers, no trade-off, and no owned decision (pitfall)
- Interview: "Walk me through the architecture of the last system you designed" (interview)

### Topic: What's the Hardest Technical Decision You've Made? (iv-hardest-technical-decision, advanced)
Distinguishing a genuinely hard trade-off from a hard *implementation* problem, and why interviewers can tell the difference immediately.
- What "hard" means here: a decision with real costs on both sides, not a bug that took a while (concept)
- Why picking a decision with an obvious right answer undersells you (concept)
- Structuring the answer: the options actually considered, the axis you decided on, the cost you accepted (concept)
- Diagram: two real options with their costs laid out side by side (diagram)
- Concrete example: choosing eventual consistency for a feature and living with the support cost (concept)
- Compare: a technically-hard story vs a trade-off-hard story — which one this question wants (compare)
- Follow-up: "would you make the same call again?" — showing judgment, not defensiveness (concept)
- Pitfall: a decision that was actually made by your manager or the team, retold as yours (pitfall)
- Interview: "Tell me about the hardest technical trade-off you've had to make" (interview)

### Topic: Tell Me About a Design That Failed (iv-a-design-that-failed, advanced)
Why interviewers deliberately ask for a failure, and how a real one — told with an honest cause and a fix — reads stronger than a disguised success.
- Why this question exists: judgment under a failure signal is harder to fake (concept)
- Picking a real failure, not a "worked too hard" non-failure in disguise (concept)
- Structuring the answer: what you designed, what assumption broke, what it cost, what you changed (concept)
- Diagram: the assumption that broke and the blast radius it caused (diagram)
- Concrete example: a schema decision that didn't survive a 10x traffic increase (concept)
- Compare: a defensive retelling vs an owned, specific retelling of the same failure (compare)
- Follow-up: "what would have caught this earlier?" — process, not just the fix (concept)
- Pitfall: blaming the requirements, the team, or "we didn't have time" with no self-reflection (pitfall)
- Interview: "Tell me about a system you designed that didn't hold up" (interview)

### Topic: What Would You Redo, Knowing What You Know Now? (iv-what-would-you-redo, advanced)
The retrospective-judgment question that separates "I'd change nothing" candidates from ones who show real hindsight.
- Why "nothing, it worked out fine" is the answer that costs you the most points (concept)
- Distinguishing a redo you'd make from a redo that's just complaining about constraints (concept)
- Structuring the answer: what you knew then, what you know now, what specifically changes (concept)
- Diagram: then-vs-now decision points on the same system (diagram)
- Concrete example: redoing a synchronous integration as async after seeing it under load (concept)
- Compare: "I'd rewrite everything" (red flag — no judgment) vs one targeted, justified change (compare)
- Follow-up: "why didn't you know that at the time?" — reasoning about what information was actually available (concept)
- Pitfall: a redo that's really just relitigating someone else's decision (pitfall)
- Interview: "If you could redesign that system today, what would you change?" (interview)

### Topic: Questions to Ask About Their Architecture and Team (iv-questions-to-ask-about-their-system, intermediate)
The design-specific version of "any questions for me?" — asking about their actual scaling story, on-call reality, and technical debt instead of generic culture questions (which are covered in `behavioral-questions-to-ask`, Area 17).
- Why this moment is still evaluated, and why generic questions waste it (concept)
- Cross-link: `behavioral-questions-to-ask` for the general two-way-signal framing this Topic assumes (concept)
- Questions that read as senior: "what's the part of the system you'd redesign if you could?" (concept)
- Questions that surface real signal: on-call load, biggest recent incident, how architecture decisions get made (concept)
- Diagram: question categories — scale, ownership, debt, decision process (diagram)
- Concrete example: asking about a specific technology mentioned earlier in the loop, not a generic one (concept)
- Compare: a question that signals genuine technical curiosity vs one that signals you didn't listen (compare)
- Pitfall: asking a question the job description already answered (pitfall)
- Interview: "Do you have any questions about how we've built this?" (interview)

---

## Group: Interview Formats Beyond the Standard Loop (design-round-formats)

*Round-specific mechanics that differ from the standard 45-60 minute HLD round already covered end-to-end by `sd-playbook` and `sd-interview-playbook` (Area 17). Each Topic here covers what changes about the *format*, not the design method itself — cross-link back to `sd-playbook` for the method that still applies inside each format.*

### Topic: The Rapid-Fire Trade-off Screen (iv-rapid-fire-tradeoff-screen, intermediate)
The phone-screen format of 8-10 quick trade-off questions in 15-20 minutes, and why rambling through the standard framework fails it.
- What this round looks like: quick-fire questions, no whiteboard, 60-90 seconds each (overview)
- Why the full requirements-gathering framework doesn't fit here (concept)
- The pattern that scores: name the axis, pick a side, give one sentence of why (concept)
- Diagram: a rapid-fire answer shape vs a full deep-dive answer shape, side by side (diagram)
- Concrete example: "SQL or NoSQL for a shopping cart?" answered in three sentences (concept)
- Compare: hedging with "it depends, well, both have trade-offs..." vs committing to a side (compare)
- Cross-link: `sd-tradeoff-articulation` (Area 17) for the underlying trade-off-naming skill this format compresses (concept)
- Pitfall: treating a 90-second question like a 10-minute deep dive and running out the clock (pitfall)
- Pitfall: giving a one-word answer with no reasoning, which reads as a guess (pitfall)
- Interview: "Quick one — would you use a queue or direct call here, and why?" (interview)

### Topic: The Bar-Raiser and Hiring-Manager Design Round (iv-bar-raiser-design-round, advanced)
How a bar-raiser or hiring-manager-led design round differs in intent from a peer round, even when the prompt looks identical.
- What a bar-raiser is actually calibrating: consistency across candidates, not just this one's skill (concept)
- Why the hiring manager's round often probes ownership and judgment over raw technique (concept)
- Diagram: what a peer interviewer scores vs what a bar-raiser scores on the same answer (diagram)
- Why bar-raisers often let you struggle longer before offering a hint (concept)
- Concrete example: the same "why this trade-off" question landing differently depending on who's asking (concept)
- Compare: optimizing an answer for a peer's checklist vs for a bar-raiser's calibration bar (compare)
- Follow-up: a hiring-manager question about how you'd staff or sequence building the system (concept)
- Pitfall: assuming the bar-raiser is hostile because their questions feel less structured (pitfall)
- Interview: "As the hiring manager, I want to know how you'd sequence building this with a team of three" (interview)

### Topic: The Take-Home Architecture Exercise (iv-take-home-architecture-exercise, intermediate)
The async design-doc or architecture-proposal exercise some senior/staff loops use instead of (or alongside) a live whiteboard round.
- What this format asks for: a written design doc or diagram set, not working code (overview)
- Why it's graded on the same axes as a live round, minus the time pressure (concept)
- Cross-link: `writing-a-design-doc` (`design-in-practice`) for the doc structure itself — this Topic covers using it as an interview artifact (concept)
- Structuring the submission: problem, requirements, options considered, chosen design, trade-offs (concept)
- Diagram: an architecture exercise submission outline (diagram)
- Time-boxing the exercise instead of polishing it for days (concept)
- Compare: a live round's ability to probe follow-ups vs a take-home's need to preempt them in writing (compare)
- Pitfall: submitting a diagram with no written rationale, leaving the evaluator to guess your reasoning (pitfall)
- Pitfall: over-scoping the design far beyond what the prompt's constraints call for (pitfall)
- Interview: "Send us a one-page design for this system by Friday" (interview)

---

---

# Boundary & merge notes

## Boundary notes — phase-a

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

## Boundary notes — phase-b

- **`engineering-craft`** owns DDD, clean-architecture layering, and unit-testing mechanics (mocking frameworks, test pyramid, how to write a test). `dependency-injection-and-testability` (this file) stays at the design level — *why* a seam makes testing possible — not test-writing mechanics; recommend `engineering-craft` for the latter. Likewise `refactoring-legacy-into-patterns`'s characterization-tests slide references the *technique* only; the mechanics of writing those tests belong to `engineering-craft`.
- **`languages-compilers`** owns language-specific exception mechanics (Java checked exceptions, Rust `Result`/`?`, Go's error-value convention). `designing-errors` (this file) stays language-agnostic — the design decision of exceptions vs result types vs error boundaries — and should cross-link into `languages-compilers` for the concrete language implementation rather than duplicate it.
- **`anti-patterns` (existing) vs `refactoring-legacy-into-patterns` (new)**: the existing `refactoring-to-fix-smells` topic fixes a *local* smell with a pattern; the new topic is the *process* of refactoring an untested legacy codebase at scale (sequencing, safety net, strangling). Kept as separate topics with a cross-link rather than merged.

## Boundary notes — phase-c

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

## Merge notes — phase-d

**Boundary/dedupe decisions for the merged `system-design` area:**
1. **`sd-playbook` (this area) vs `interview-prep`'s `sd-interview-playbook`, and `engineering-craft`'s `behavioral` vs `interview-prep`'s `behavioral-interview`.** Both pairs are flagged in `briefs/area-group-map.md` as the same content under two names. Recommendation: home the full design-interview playbook (including this phase's 3 additions) in `system-design`'s `sd-playbook`, and have `interview-prep` delete `sd-interview-playbook` and point to this group instead; same pattern for `behavioral` — keep it in `engineering-craft`, delete `interview-prep`'s `behavioral-interview` duplicate. `interview-prep` keeps its genuinely distinct groups (`coding-playbook`, `take-home`, `negotiation`).
2. `design-in-practice` (this phase) is new and doesn't duplicate any existing group in either source brief — verified via full slug/group scan above.
3. Every cross-link flagged in this phase's group/Topic scope lines (`technical-communication`, `cicd`, `code-review`, `debugging`, `clean-architecture`, all in `engineering-craft`) should render as an explicit "see also" in the authored content, not get re-explained.

**Suggested group order for the merged area** (group order in the brief file drives app ordering per `tools/regen_v3.py`'s relevance-ordering rule):

1. `sd-fundamentals` → `capacity-estimation` *(Foundations)*
2. `oop-fundamentals` → `design-principles` → `creational-patterns` → `structural-patterns` → `behavioral-patterns` → `uml` → `anti-patterns` → `oo-concurrency` → `lld-framework` → `lld-case-studies` *(LLD)*
3. `load-balancing` → `caching` → `storage-scale` → `consistency-replication` → `messaging-streaming` → `microservices` → `api-design` → `resilience` → `search-indexing` → `observability` → `case-studies` *(HLD)*
4. `design-in-practice` → `sd-playbook` *(Craft & Interview — real-world practice before the interview meta-layer, since the playbook now leans on Phase D's design-doc/rollout/review vocabulary)*

## Boundary notes — hld-cases

- **`ml-system-design` (in the separate `ai-ml` area) owns the ranking/recommendation models.**
  Several case studies here touch a ranking or scoring signal but should stop at "here's the
  slot in the architecture where a model plugs in" and cross-link out rather than re-teach it:
  `design-news-feed` (feed ranking), `design-follow-graph-service` (who-to-follow suggestions),
  `design-audio-streaming-service` (playlist ranking), `design-content-moderation-pipeline`
  (the classifier itself), `design-ad-click-aggregation-system` (fraud/bot-detection model).
- **LLD case studies vs this group's service-scale case studies share a name, not a lesson.**
  `lld-case-studies` has `rate-limiter` (an in-process class/algorithm) and `notification-system`
  (an OOP class design); this brief's `design-rate-limiter-service` and `design-notification-system`
  are the distributed *service* versions — different hard part (shared state, fan-out, config
  propagation) at a different altitude. No slug collision; keep the framing distinct in both places.
- **Building-block groups teach the concept; the matching infra case study teaches building the
  primitive.** `design-blob-object-store` builds what `object-and-blob-storage` teaches you to use;
  `design-distributed-message-queue` builds what `messaging-fundamentals`/`queues-vs-pubsub` teach
  you to use; `design-distributed-cache` builds what `caching`/`distributed-caching` teach you to
  use. Each case study's cross-links point at the *usage*-level group so slides don't re-derive it.
- **Resilience group overlap.** `design-rate-limiter-service` cross-links `distributed-rate-limiting`
  for the algorithms; the original `hld-case-studies` brief explicitly skipped a rate-limiter case
  study "to avoid duplicating" that group. Per this task's brief (more depth/coverage), it's added
  back here but scoped strictly to the service-architecture problem, not the token-bucket/sliding-
  window mechanics, which stay owned by `resilience`.
- **Merged/cut, with reasoning inline near each group above:** Twitter timeline, generic Instagram
  photo-feed, poll/voting, and standalone direct-messaging case studies — each would have re-taught
  an existing topic's lesson with a different product name attached.

## Boundary notes — iv-hld

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

## Boundary notes — iv-lld

- **vs `lld-framework`:** that group teaches the *method* (how to run any LLD interview — scoping,
  entity identification, live trade-off talk). This bank applies that method to *specific, named
  questions*. No overlap in content; `iv-*` topics assume the method and jump straight to the answer.
- **vs `oop-fundamentals` / `design-principles` / `*-patterns` / `oo-concurrency`:** those groups
  teach the *concept* (what SRP is, how Strategy works, what a vtable is). This bank teaches
  *answering the interview question about it* — never re-derives the concept, always cross-links
  to it instead. If a topic here starts re-explaining a concept from scratch, that's scope creep —
  trim it back to a cross-link.
- **vs `languages-compilers` (not in this area):** `iv-can-you-override-static-method`,
  `iv-double-checked-locking-explained`, `iv-volatile-vs-synchronized`, and
  `iv-equals-hashcode-contract` lean on Java/JVM-specific mechanics (classloading, the JMM,
  `volatile`'s reordering guarantee). I kept the *interview framing and code sketch* here since
  that's how these are actually asked in LLD rounds, but the deep "why the JMM works this way"
  belongs to a language-mechanics area if one exists — recommend a light cross-link there once
  that area's slugs are known, not a duplicate explanation.
- **vs `lld-case-studies` (parking lot, elevator, chess, etc.):** deliberately excluded full case
  studies from `interview-lld-design-questions` — those 8 topics are small class/API sketches
  (a cache API, a retry utility, an event bus) that resolve in code, not a 30-minute system.
- **Recommendation:** ship as-is; the one open question is whether `iv-design-thread-safe-cache-api`
  should instead cross-link to a *new* small-probe entry rather than the full `lru-cache` case
  study — I linked to `lru-cache` since it's the closest existing concept anchor, but a reviewer
  who owns case studies should confirm that's not a duplicate surface.
</content>

## Boundary notes — lld-cases

**HLD/LLD same-name overlaps (kept, disambiguated):**
- `notification-system` (here) vs `design-notification-system` (HLD `hld-case-studies`): this one is the Observer/Strategy class design for one service instance; the HLD topic is the queue-based fan-out architecture at scale. Slugs already distinct in the source brief — preserved as-is.
- `rate-limiter` (here) vs `distributed-rate-limiting` (HLD `resilience`): this one is the single-process algorithm choice (token bucket, sliding window); the HLD topic is coordinating limits across nodes (Redis, clock skew). Cross-linked from the LLD topic's last slide.
- `lld-movie-ticket-booking` vs `design-ticket-booking-system` (HLD `hld-case-studies`): prefixed `lld-` specifically to avoid collision and signal altitude — this one is the seat-hold/concurrency class model; the HLD topic is the booking system's consistency/scale architecture.
- `lld-url-shortener` vs `design-url-shortener` (HLD `hld-case-studies`): prefixed `lld-` for the same reason — this one is the encoding-scheme/class-boundary decision; the HLD topic is distributed ID generation, sharding, and caching at scale. Cross-linked to `design-unique-id-generator`.
- `cab-booking-system` vs `design-proximity-service` (HLD `hld-case-studies`): no slug collision, but conceptually adjacent — this one is the trip/match/fare class model; the HLD topic is the geo-indexing infra behind nearby-search. Cross-linked via the LLD topic's "hard part" slide.

**Merged or cut under the value filter (not enough of a distinct modelling lesson to justify a separate flagship topic):**
- *Coffee/tea machine* — cut as a standalone topic; its hard core (inventory + payment + dispensing state machine) is near-identical to `vending-machine`. Folded the recipe/ingredient-composition angle into `vending-machine`'s extensibility slide instead.
- *Amazon locker system* — cut; its slot-allocation problem overlaps heavily with `parking-lot`. Revisit only if a genuinely distinct angle (pickup-code security, size-bucket packing) is developed later.
- *Calendar/event scheduler* — merged into `meeting-room-scheduler` rather than kept separate; both reduce to multi-party free/busy intersection plus recurrence, so splitting them would duplicate the same lesson under two names.
- *Generic dice/board-game engine* — cut as a standalone topic; folded into `snake-and-ladder`'s extensibility slide (multiple dice, multiplayer-skip rules) since it has no hard core beyond what that topic already teaches.
- *Plugin/DI container* — cut; it's a pattern-application exercise, not a case study with its own state machine, concurrency problem, or pricing axis, and it overlaps with the existing `dependency-injection-and-testability` topic in `lld-in-practice`.
- *In-memory file system* — cut; its storage/indexing lesson overlaps with `in-memory-key-value-store`. Deferred rather than authored as filler.
- *Spreadsheet with undo/redo* — cut; the Command-pattern undo lesson is already covered via `atm-system`'s cross-link and the `command-pattern` topic itself. Deferred as lower-frequency relative to the 32 chosen.

**Net result:** 13 preserved (same slugs/outlines, each gained an `overview` and `interview` bookend slide since the flagship skeleton requires both and the originals had neither) + 19 new = **32 topics across 5 groups.**
