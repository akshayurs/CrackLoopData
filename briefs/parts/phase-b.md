# Phase B — LLD track additions (system-design merge)

New material only. Reused verbatim alongside this: `briefs/expanded/object-oriented-design.md` (LLD/OOD)
and `briefs/expanded/system-design.md` (HLD). This file adds (a) a new group, **LLD in Practice**, and
(b) a small set of expert-tier topics appended to three existing LLD groups. Format matches
`object-oriented-design.md`: kebab slugs unique within their group, one-line scope (not a restated title),
bulleted slide outline `- <heading> (<type>)` with optional `— cross-link: <topic-slug>`.

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

## Additions to existing group: Behavioral Patterns (behavioral-patterns)

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

## Additions to existing group: Concurrency in OO Design (oo-concurrency)

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

## Additions to existing group: Anti-Patterns & Code Smells (anti-patterns)

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

## Boundary notes

- **`engineering-craft`** owns DDD, clean-architecture layering, and unit-testing mechanics (mocking frameworks, test pyramid, how to write a test). `dependency-injection-and-testability` (this file) stays at the design level — *why* a seam makes testing possible — not test-writing mechanics; recommend `engineering-craft` for the latter. Likewise `refactoring-legacy-into-patterns`'s characterization-tests slide references the *technique* only; the mechanics of writing those tests belong to `engineering-craft`.
- **`languages-compilers`** owns language-specific exception mechanics (Java checked exceptions, Rust `Result`/`?`, Go's error-value convention). `designing-errors` (this file) stays language-agnostic — the design decision of exceptions vs result types vs error boundaries — and should cross-link into `languages-compilers` for the concrete language implementation rather than duplicate it.
- **`anti-patterns` (existing) vs `refactoring-legacy-into-patterns` (new)**: the existing `refactoring-to-fix-smells` topic fixes a *local* smell with a pattern; the new topic is the *process* of refactoring an untested legacy codebase at scale (sequencing, safety net, strangling). Kept as separate topics with a cross-link rather than merged.
