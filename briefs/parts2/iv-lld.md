# Interview Question Bank — LLD/OOD + Distributed-Systems Foundations

Scope: dedicated interview-question topics for the LLD/OOD viva and the distributed-systems
foundations that sit under HLD. Each topic teaches ANSWERING one real, commonly-asked question —
not the underlying concept (already taught elsewhere in the area) and not a full case study
(owned by a separate group/agent). Slugs prefixed `iv-` to keep this bank visually distinct.

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
- Follow-up: "give me an example where you have one without the other" (concept)
- Weak answer: "encapsulation is getters and setters" — why that loses points (pitfall)
- The 60-second version, spoken out loud (concept)

### Topic: Why is composition favored over inheritance? (iv-why-composition-over-inheritance, intermediate)
Tests whether you can justify a rule of thumb with a concrete failure mode, not just recite it.
- The question, and what "favor" is testing — judgment, not dogma (overview)
- Clarifying question: are we talking about this codebase or in general? (concept)
- The answer skeleton: state the rule, give the failure mode it prevents, give the exception (concept)
- Code: an inheritance hierarchy that breaks when a new variant arrives (code) — cross-link: composition-vs-inheritance
- Code: the same feature refactored to composition + strategy (code) — cross-link: strategy-pattern
- Follow-up: "so is inheritance ever right?" — is-a vs has-a as the actual test (concept)
- Follow-up: "what does this cost you?" — indirection, more objects to wire up (concept)
- Weak answer: reciting "favor composition" with no example — reads as memorized (pitfall)
- The 60-second version (concept)

### Topic: Can you override a static method in Java? (iv-can-you-override-static-method, intermediate)
A language-specific trap question that tests whether you actually understand dispatch, not memorized trivia.
- The question as asked, and why it's a trap (overview)
- Clarifying question: which language — this is Java/C#-specific, not universal (concept)
- The answer skeleton: no, it's hidden not overridden — then explain why (concept)
- Code: a static "override" that resolves by reference type, not object type (code)
- Diagram: static dispatch (compile-time, by type) vs dynamic dispatch (runtime, by vtable) (diagram)
- Follow-up: "what actually happens if you try?" — method hiding, not polymorphism (concept)
- Follow-up: "does this apply to other languages?" — Python/JS don't draw this line the same way (concept)
- Weak answer: saying "no" with no explanation of hiding vs overriding (pitfall)
- The 60-second version (concept)

### Topic: When would you choose an interface over an abstract class? (iv-interface-vs-abstract-class-choice, intermediate)
The design-judgment version of a definitions question.
- The question, and the design-judgment it's really testing (overview)
- Clarifying question: which language — multiple inheritance rules differ (concept)
- The answer skeleton: contract-only vs shared implementation, then the deciding question (concept) — cross-link: interfaces-vs-abstract-classes
- Code: the same capability modeled both ways, side by side (code)
- Compare: interface vs abstract class — decision table (multiple inheritance, shared state, versioning) (compare)
- Follow-up: "what changed with default methods on interfaces?" (concept)
- Follow-up: "you chose wrong initially — how do you migrate?" (concept)
- Weak answer: "interfaces are 100% abstract" — outdated in modern languages (pitfall)
- The 60-second version (concept)

### Topic: What's the difference between method overloading and overriding? (iv-overloading-vs-overriding, beginner)
The "compile-time vs runtime" answer it's fishing for.
- The question, and the compile-time vs runtime distinction it wants (overview)
- Clarifying question: are they asking definitions or asking you to spot a bug? (concept)
- The answer skeleton: overloading = same name different signature, resolved at compile time; overriding = same signature, resolved at runtime (concept) — cross-link: polymorphism
- Code: an overload-resolution surprise — the "wrong" method picked (code)
- Code: an override that changes behavior polymorphically (code)
- Follow-up: "can you overload by return type alone?" (concept)
- Follow-up: "what rules govern overriding — same signature, covariant return?" (concept)
- Weak answer: confusing the two under pressure, calling overloading "polymorphism" without qualifying compile-time (pitfall)
- The 60-second version (concept)

### Topic: What is the diamond problem and how do languages solve it? (iv-diamond-problem-explained, intermediate)
Really about ambiguity resolution, not just the shape of the diagram.
- The question, and why it's really about ambiguity resolution (overview)
- Clarifying question: single inheritance language or multiple (C++)? (concept)
- The answer skeleton: draw the diamond, name the ambiguity, name the fix (concept) — cross-link: inheritance
- Diagram: the diamond — two parents, one shared grandparent method (diagram)
- Code: the same ambiguity via multiple interface default methods, and how it's resolved (code)
- Follow-up: "why did Java ban multiple class inheritance but allow multiple interfaces?" (concept)
- Follow-up: "how does virtual inheritance solve it in C++?" (concept)
- Weak answer: only describing the shape without naming a concrete resolution mechanism (pitfall)
- The 60-second version (concept)

### Topic: What's the equals/hashCode contract and why does it matter? (iv-equals-hashcode-contract, intermediate)
The bug class it's protecting against is the real point.
- The question, and the bug class it's protecting against (overview)
- Clarifying question: is this about a hash-based collection specifically? (concept)
- The answer skeleton: the contract's rules, then the consequence of breaking it (concept)
- Code: overriding `equals` without `hashCode` — an object that "disappears" from a `HashSet` (code)
- Code: a correct `equals`/`hashCode` pair for a value object (code)
- Follow-up: "what about mutable fields in the hash?" — object changes after insertion (concept)
- Follow-up: "how does this interact with immutability?" (concept) — cross-link: immutability-as-a-design-tool
- Weak answer: reciting the rule without the "why" — the broken-invariant story (pitfall)
- The 60-second version (concept)

### Topic: Why should objects be immutable, and when should you make them so? (iv-why-immutability, intermediate)
The trade-off it's testing you can articulate — not "immutability is always better."
- The question, and the trade-off it's testing you can articulate (overview)
- Clarifying question: immutability of what — a value object, a config, a whole domain model? (concept)
- The answer skeleton: name the benefits, name the cost, name when it's not worth it (concept) — cross-link: immutability-as-a-design-tool
- Code: a mutable class refactored to immutable (builder + final fields) (code)
- Compare: immutable vs mutable — thread safety, GC pressure, ergonomics (compare)
- Follow-up: "how do you 'update' an immutable object efficiently?" — copy-on-write, wither methods (concept)
- Follow-up: "is immutability enough to make something thread-safe?" (concept) — cross-link: thread-safety-fundamentals-for-objects
- Weak answer: "immutable is always better" — no cost acknowledged (pitfall)
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
- Follow-up: "which one do you reach for first in practice?" (concept)
- Follow-up: "give me a case where two principles pull in different directions" (concept)
- Weak answer: five disconnected textbook definitions, no shared example (pitfall)
- The 60-second version (concept)

### Topic: Which SOLID principle does this code violate? (iv-spot-solid-violation, intermediate)
The live-code-reading skill: name the smell first, then map it to the principle.
- The question, and the live-code-reading skill it tests (overview)
- Clarifying question: are they handing you a snippet now, or asking you to imagine one? (concept)
- The answer skeleton: name the smell first, then map it to the principle, then propose the fix (concept) — cross-link: common-code-smells
- Code: a class with three unrelated responsibilities — spot the SRP violation (code)
- Code: a subclass that throws on a parent method — spot the LSP violation (code) — cross-link: lsp-liskov-substitution
- Follow-up: "it violates two principles at once — which do you fix first?" (concept)
- Follow-up: "how would you refactor this live, in under two minutes?" (concept)
- Weak answer: naming a principle without pointing at the specific line that violates it (pitfall)
- The 60-second version (concept)

### Topic: Is SRP always the right call? (iv-is-srp-always-right, intermediate)
A confident "no, and here's the counter-case" beats parroting the principle.
- The question, and why a confident "no" beats parroting the principle (overview)
- Clarifying question: "always" in what sense — codebase size, team size? (concept)
- The answer skeleton: state the principle, then the counter-case, then the actual rule of thumb (concept) — cross-link: srp-single-responsibility
- Code: a class split into four pieces that's now harder to navigate than the original (code)
- Follow-up: "how small is too small — what's your smell test?" (concept)
- Follow-up: "how does this interact with cohesion?" (concept) — cross-link: coupling-and-cohesion
- Weak answer: "yes, always split responsibilities" — no nuance, reads junior (pitfall)
- The 60-second version (concept)

### Topic: How do you spot tight coupling in a design? (iv-spot-tight-coupling, intermediate)
The diagnostic skill: name concrete signals, not just the definition.
- The question, and the diagnostic skill behind it (overview)
- Clarifying question: coupling between classes, modules, or services? (concept)
- The answer skeleton: name 2-3 concrete signals, then a smell you'd point to in code (concept) — cross-link: coupling-and-cohesion
- Code: a class that `new`s its dependencies directly — the signal and the fix (code) — cross-link: dip-dependency-inversion
- Diagram: a dependency graph before/after decoupling via an interface (diagram)
- Follow-up: "how do you measure this, not just eyeball it?" — fan-out, change amplification (concept)
- Follow-up: "is zero coupling the goal?" — no, coupling to abstractions is fine (concept)
- Weak answer: defining coupling correctly but giving no concrete signal to look for (pitfall)
- The 60-second version (concept)

### Topic: Give an example of DRY taken too far (iv-dry-gone-wrong, intermediate)
Tests judgment over rule-following — premature abstraction is the real answer.
- The question, and why this tests judgment over rule-following (overview)
- Clarifying question: DRY on code, or DRY on concepts that only look similar? (concept)
- The answer skeleton: describe premature abstraction, then the concrete failure (concept) — cross-link: dry-yagni-kiss
- Code: two unrelated features merged into one "shared" function that now has four boolean flags (code)
- Follow-up: "how do you tell accidental duplication from essential duplication?" (concept)
- Follow-up: "what's the rule of three, and do you follow it strictly?" (concept)
- Weak answer: "DRY is always good, just do it more carefully" — dodges the actual question (pitfall)
- The 60-second version (concept)

### Topic: YAGNI vs designing for extensibility — how do you balance them? (iv-yagni-vs-extensibility, intermediate)
The tension between the two is the point; picking a side absolutely is the wrong answer.
- The question, and the tension it's asking you to hold (overview)
- Clarifying question: extensibility for a known near-term requirement, or speculative? (concept)
- The answer skeleton: YAGNI kills speculation, but seams for known variation are cheap — state the line (concept) — cross-link: dry-yagni-kiss
- Code: a design with one cheap seam (an interface) vs one expensive one (an unused plugin framework) (code)
- Follow-up: "how do you tell a cheap seam from an expensive one before building it?" (concept)
- Follow-up: "your PM says 'we'll definitely need X in Q3' — does that change your answer?" (concept)
- Weak answer: picking a side absolutely ("always YAGNI" or "always extensible") (pitfall)
- The 60-second version (concept)

### Topic: What does dependency inversion look like in practice? (iv-dependency-inversion-in-practice, intermediate)
The "in practice" qualifier means they want code, not the definition.
- The question, and the "in practice" qualifier — they want code, not the definition (overview)
- Clarifying question: DIP the principle, or DI the pattern/framework? (concept) — cross-link: dip-dependency-inversion
- The answer skeleton: high-level module depends on an abstraction, low-level module implements it, wiring happens outside both (concept)
- Code: a service depending on a concrete `MySqlRepository` refactored to depend on a `Repository` interface (code)
- Diagram: the dependency arrow flipped — before and after (diagram)
- Follow-up: "where does the wiring happen — who constructs the concrete instance?" (concept) — cross-link: dependency-injection-and-testability
- Follow-up: "does this always need a DI framework?" — no, constructor injection is enough (concept)
- Weak answer: confusing dependency inversion with dependency injection as the same thing (pitfall)
- The 60-second version (concept)

### Topic: How do you decide which design principle applies when two conflict? (iv-resolving-conflicting-principles, advanced)
The senior-signal version of the SOLID questions.
- The question, and why this is the senior-signal version of the SOLID questions (overview)
- Clarifying question: can they give a concrete pair that's conflicting, e.g. SRP vs simplicity? (concept)
- The answer skeleton: name the conflict, name the actual cost of each choice, decide by the cost the codebase can least afford (concept)
- Code: a real conflict — ISP wants many small interfaces, but that fragments a cohesive API (code) — cross-link: isp-interface-segregation
- Follow-up: "walk me through how you'd explain this trade-off to a teammate who disagrees" (concept)
- Follow-up: "does team size or codebase age change the answer?" (concept)
- Weak answer: treating principles as unbreakable laws instead of heuristics (pitfall)
- The 60-second version (concept)

## Group: LLD Interview Bank — Design Patterns (interview-lld-patterns)
*Picking, defending, and critiquing design patterns live — not reciting the GoF catalog.*

### Topic: Given this scenario, which design pattern would you use? (iv-which-pattern-would-you-use, intermediate)
The pattern-matching skill: name what varies before naming a pattern.
- The question, and the pattern-matching skill it's actually testing (overview)
- Clarifying question: what's varying — behavior, construction, or structure? (concept)
- The answer skeleton: name what varies, map it to a pattern family, name the specific pattern (concept)
- Code: a scenario (pluggable payment methods) walked from problem to Strategy (code) — cross-link: strategy-pattern
- Follow-up: "what if two patterns both fit — how do you choose?" (concept)
- Follow-up: "what would make you NOT reach for a pattern here?" (concept) — cross-link: over-engineering-and-pattern-happy-design
- Weak answer: naming a pattern by vibe without explaining why it fits this scenario (pitfall)
- The 60-second version (concept)

### Topic: Strategy vs State pattern — what's the actual difference? (iv-strategy-vs-state-pattern, intermediate)
Same class diagram, different intent — who changes it, when, and why.
- The question, and why they look identical in a class diagram (overview)
- Clarifying question: do they want the structural difference or the intent difference? (concept)
- The answer skeleton: same shape, different intent — caller picks vs object transitions itself (concept) — cross-link: strategy-pattern
- Code: the same class diagram used for a Strategy (sort algorithm) and a State (order lifecycle) (code) — cross-link: state-pattern
- Compare: Strategy vs State — who changes it, when, and why (compare)
- Follow-up: "can a state also change its own strategy?" — yes, and that's a hybrid, not a bug (concept)
- Weak answer: "they're basically the same pattern" with no intent distinction (pitfall)
- The 60-second version (concept)

### Topic: Factory vs Builder — when do you reach for each? (iv-factory-vs-builder, intermediate)
The "when," not the definitions, is what separates a strong answer.
- The question, and the "when" that separates it from a definitions question (overview)
- Clarifying question: simple object creation, or an object with many optional parts? (concept)
- The answer skeleton: Factory hides which class, Builder hides how assembly happens step by step (concept) — cross-link: factory-method-and-abstract-factory
- Code: a telescoping constructor refactored to a Builder (code) — cross-link: builder-pattern
- Code: a Factory picking between subclasses by input type (code)
- Follow-up: "can you combine them — a Factory that returns a Builder?" (concept)
- Weak answer: "Builder is just a fancier constructor" — misses the immutability/validation angle (pitfall)
- The 60-second version (concept)

### Topic: What's wrong with Singleton, and how do you make it thread-safe? (iv-singleton-problems-and-thread-safety, advanced)
One of the most-asked pattern questions in LLD rounds — smell first, then the fix.
- The question, and why it's one of the most-asked pattern questions in LLD rounds (overview)
- Clarifying question: are they asking about the pattern's design smell, or the thread-safety mechanics? (concept)
- The answer skeleton: name the smells (hidden dependency, untestable, global state), then the thread-safety fix (concept) — cross-link: singleton-pattern
- Code: a naive singleton race condition under concurrent first access (code)
- Code: the fixed version — double-checked locking or an eager holder class (code) — cross-link: synchronization-techniques-in-oo-design
- Follow-up: "how do you unit test code that depends on a singleton?" (concept) — cross-link: dependency-injection-and-testability
- Follow-up: "what does a DI container replace this with?" (concept)
- Weak answer: fixing thread safety but never addressing why Singleton is a smell in the first place (pitfall)
- The 60-second version (concept)

### Topic: Decorator vs inheritance for extending behavior — which and why? (iv-decorator-vs-inheritance, intermediate)
The combinatorial-explosion story is what the interviewer wants to hear.
- The question, and the combinatorial-explosion story it's fishing for (overview)
- Clarifying question: is the behavior added at compile time or does it need to vary at runtime? (concept)
- The answer skeleton: inheritance explodes combinatorially, Decorator composes at runtime — show the counting (concept) — cross-link: decorator-pattern
- Code: a beverage/topping-style class hierarchy that explodes with N toppings (code)
- Code: the same feature as stacked Decorators (code)
- Follow-up: "does this always beat inheritance — what's the cost of decorators?" — many small wrapper objects, harder to debug the stack (concept)
- Weak answer: reciting the pattern name without showing the combinatorial blow-up it solves (pitfall)
- The 60-second version (concept)

### Topic: Observer pattern and memory leaks — what goes wrong? (iv-observer-pattern-memory-leaks, advanced)
A production-bug story you've actually hit, not a definition.
- The question, and the production-bug story it's testing you've actually hit (overview)
- Clarifying question: are we talking a GC'd language or one with manual memory management? (concept)
- The answer skeleton: name the leak mechanism (subject holds a strong ref to a dead observer), then the fix (concept) — cross-link: observer-pattern
- Code: an observer that's never unsubscribed, keeping a whole UI screen alive (code)
- Code: the fix — weak references or explicit unsubscribe in a lifecycle hook (code)
- Follow-up: "how do reactive/event-bus frameworks handle this for you?" (concept)
- Weak answer: describing the pattern correctly but never naming why it leaks (pitfall)
- The 60-second version (concept)

### Topic: When is a design pattern the wrong answer? (iv-when-patterns-are-the-wrong-answer, advanced)
Why senior candidates get asked this specifically — the cost of a pattern, not just its benefit.
- The question, and why senior candidates get asked this specifically (overview)
- Clarifying question: wrong for this codebase, or wrong in general for the problem shape? (concept)
- The answer skeleton: name the cost of a pattern (indirection, more files, cognitive load) and the threshold where it's not worth paying (concept) — cross-link: over-engineering-and-pattern-happy-design
- Code: a one-line conditional turned into a four-class Strategy hierarchy for no reason (code)
- Follow-up: "how do you walk that back once it's already in the codebase?" (concept) — cross-link: refactoring-to-fix-smells
- Weak answer: "patterns are always good practice" — the opposite of the senior signal they want (pitfall)
- The 60-second version (concept)

### Topic: Name a design pattern you've used in a real framework and explain it (iv-pattern-in-a-real-framework, intermediate)
"I've actually seen this" beats a textbook answer.
- The question, and why "I've actually seen this" beats a textbook answer (overview)
- Clarifying question: framework you've used personally, or any well-known one? (concept)
- The answer skeleton: name the framework, name the pattern, explain the mechanism in your own words (concept)
- Code: sketch of the pattern as it appears in a familiar framework (a builder-style config API, or an observer-based event system) (code)
- Follow-up: "why did the framework authors choose that pattern over the alternative?" (concept)
- Follow-up: "what would you change about it if you designed it today?" (concept)
- Weak answer: naming a pattern you can't actually trace through real code (pitfall)
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
- Follow-up: "can you make this lock-free instead?" (concept) — cross-link: lock-free-and-atomic-object-design
- Follow-up: "what's the performance cost of your fix under contention?" (concept)
- Weak answer: synchronizing every method "to be safe" — coarse locking that kills throughput (pitfall)
- The 60-second version (concept)

### Topic: synchronized vs Lock vs atomic — how do you choose? (iv-synchronized-vs-lock-vs-atomic, advanced)
A decision table, not a preference — pick by what's actually shared.
- The question, and the decision-table it's really asking for (overview)
- Clarifying question: single variable, or multiple fields that must change together? (concept)
- The answer skeleton: atomic for a single variable, synchronized for simple mutual exclusion, explicit Lock for advanced control (concept)
- Code: the same increment problem solved three ways (code)
- Compare: synchronized vs Lock vs atomic — fairness, interruptibility, composability (compare) — cross-link: synchronization-techniques-in-oo-design
- Follow-up: "when would you need tryLock or a timeout?" (concept)
- Weak answer: picking one tool for everything without naming the trade-off (pitfall)
- The 60-second version (concept)

### Topic: How does immutability answer a concurrency question? (iv-immutability-as-concurrency-answer, intermediate)
"Just make it immutable" is a legitimate answer — up to a boundary you must name.
- The question, and why "just make it immutable" is a legitimate concurrency answer (overview)
- Clarifying question: is the whole object immutable, or just the parts that need to be shared? (concept)
- The answer skeleton: no shared mutable state means no race, full stop — then the boundary case (concept) — cross-link: immutability-as-a-design-tool
- Code: a mutable shared config replaced by an immutable snapshot swapped atomically (code)
- Follow-up: "what if the object is too big to copy on every update?" — persistent data structures, copy-on-write (concept)
- Weak answer: claiming immutability solves concurrency for a class that still has a mutable field inside it (pitfall)
- The 60-second version (concept)

### Topic: Walk me through a deadlock in this object graph (iv-deadlock-in-object-graph, advanced)
The tracing skill: name the cycle in THIS graph, not the four conditions in the abstract.
- The question, and the tracing skill it tests over pure definition (overview)
- Clarifying question: two threads, two locks — or is this a bigger graph? (concept)
- The answer skeleton: name the four deadlock conditions, then trace the specific cycle in this graph (concept)
- Diagram: two threads acquiring two locks in opposite order — the wait-for cycle (diagram)
- Code: the deadlocking transfer-between-accounts example (code)
- Follow-up: "how do you prevent it — ordering, timeout, or a single lock?" (concept)
- Follow-up: "how would you detect this happened in production?" — thread dumps, lock contention metrics (concept)
- Weak answer: naming "deadlock" without tracing the actual cycle in the given graph (pitfall)
- The 60-second version (concept)

### Topic: What is double-checked locking and why is it tricky? (iv-double-checked-locking-explained, advanced)
The historical bug is the actual answer, not just the shape of the pattern.
- The question, and the historical bug it's actually about (overview)
- Clarifying question: which language/memory model — this was a real bug pre-Java-5 (concept)
- The answer skeleton: the naive version, the subtle half-constructed-object bug, the fix (concept)
- Code: double-checked locking without `volatile` — the reordering hazard (code)
- Code: the corrected version with `volatile` (code)
- Follow-up: "why does volatile fix it — what does it actually guarantee?" (concept)
- Weak answer: describing the pattern's shape without explaining why it was ever broken (pitfall)
- The 60-second version (concept)

### Topic: How do you implement a thread-safe singleton? (iv-thread-safe-singleton-implementation, intermediate)
Name 2-3 approaches, then pick the one you'd actually ship.
- The question, and why it's a rite-of-passage LLD question (overview)
- Clarifying question: lazy or eager initialization — does it matter here? (concept)
- The answer skeleton: name 2-3 approaches, pick the one you'd actually ship (concept) — cross-link: singleton-pattern
- Code: eager static holder (simplest, thread-safe by classloading) (code)
- Code: double-checked locking version, contrasted (code) — cross-link: iv-double-checked-locking-explained
- Follow-up: "which one would you actually use in production, and why?" (concept)
- Weak answer: reaching for the most complex version by default instead of the simplest correct one (pitfall)
- The 60-second version (concept)

### Topic: Design a producer-consumer setup (iv-producer-consumer-design, advanced)
The bounded-buffer problem, solved with a tested primitive, not hand-rolled wait/notify.
- The question, and the bounded-buffer problem it's really asking you to solve (overview)
- Clarifying question: single or multiple producers/consumers? Bounded or unbounded queue? (concept)
- The answer skeleton: a shared bounded queue, block-on-full and block-on-empty, the coordination primitive (concept)
- Code: a producer-consumer with a blocking queue (code)
- Diagram: the buffer with wait conditions on both ends (diagram)
- Follow-up: "what if you can't block — how do you handle backpressure instead?" (concept)
- Follow-up: "how would you scale this to multiple consumers safely?" (concept)
- Weak answer: hand-rolling wait/notify incorrectly (missing the loop, spurious wakeup) instead of using a tested primitive (pitfall)
- The 60-second version (concept)

### Topic: volatile vs synchronized — what's the actual difference? (iv-volatile-vs-synchronized, advanced)
Visibility vs atomicity — the distinction that trips people up on a compound operation.
- The question, and the visibility-vs-atomicity distinction it's testing (overview)
- Clarifying question: are they asking about a single flag, or a compound operation? (concept)
- The answer skeleton: `volatile` guarantees visibility only, `synchronized` guarantees visibility and atomicity (concept)
- Code: a volatile boolean flag used correctly to stop a thread (code)
- Code: a volatile counter used incorrectly — increment is not atomic (code)
- Compare: volatile vs synchronized — what each actually guarantees (compare)
- Follow-up: "when is volatile enough, and when do you need more?" (concept)
- Weak answer: using volatile for a compound read-modify-write and thinking it's safe (pitfall)
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
- Follow-up: "how do you avoid a thundering herd on a cache miss?" (concept)
- Follow-up: "how does this differ from the LRU cache case study?" (concept) — cross-link: lru-cache
- Weak answer: designing the eviction algorithm in detail while ignoring the API contract asked for (pitfall)
- The 60-second version (concept)

### Topic: Design an audit log API (iv-design-audit-log-api, intermediate)
Append-only, immutable records — mutability here defeats the point.
- The question, and the append-only, who-what-when shape it's testing (overview)
- Clarifying question: who consumes this — compliance queries, or just a write sink? (concept)
- The answer skeleton: an immutable `AuditEvent`, an append-only writer, a read side kept separate (concept)
- Code: the `AuditEvent` record and the `AuditLogger.record()` method signature (code) — cross-link: designing-public-apis
- Follow-up: "how do you guarantee events aren't lost if the write fails mid-request?" (concept)
- Follow-up: "should this API be synchronous or fire-and-forget?" (concept)
- Weak answer: designing mutable audit records — defeats the point of an audit trail (pitfall)
- The 60-second version (concept)

### Topic: Design a plugin system (iv-design-plugin-system, advanced)
The extension-point design: a `Plugin` interface, a registry, and a lifecycle.
- The question, and the extension-point design it's testing (overview)
- Clarifying question: plugins loaded at startup, or hot-loaded at runtime? (concept)
- The answer skeleton: a `Plugin` interface, a registry, a lifecycle (register → init → execute → shutdown) (concept)
- Code: the `Plugin` interface and a registry that discovers/loads implementations (code)
- Diagram: the plugin lifecycle and where the host app calls in (diagram)
- Follow-up: "how do you isolate a misbehaving plugin from crashing the host?" (concept)
- Follow-up: "how does this compare to just using Strategy?" (concept) — cross-link: strategy-pattern
- Weak answer: designing a rigid plugin interface that requires a new host release for every plugin type (pitfall)
- The 60-second version (concept)

### Topic: Design a retry utility (iv-design-retry-utility, intermediate)
Resilience thinking packed into a small, pluggable API.
- The question, and why it's really testing resilience thinking in a small API (overview)
- Clarifying question: retry any failure, or only specific exception types? (concept)
- The answer skeleton: a `retry(operation, policy)` shape, backoff strategy as a pluggable policy (concept)
- Code: a `RetryPolicy` interface (maxAttempts, backoff) and the retry loop (code) — cross-link: retries-timeouts-and-backoff
- Follow-up: "how do you avoid retrying a non-idempotent operation?" (concept) — cross-link: idempotency-and-exactly-once
- Follow-up: "how would you add jitter, and why does it matter?" (concept)
- Weak answer: hardcoding the backoff instead of making it pluggable — fails the "utility" bar (pitfall)
- The 60-second version (concept)

### Topic: Design a configuration abstraction (iv-design-config-abstraction, intermediate)
The goal is "callers never know the source" — file, env var, or remote service.
- The question, and the "don't leak the source" design goal it's testing (overview)
- Clarifying question: static config only, or does it need to support live reload? (concept)
- The answer skeleton: a `ConfigProvider` interface, callers never know if it's a file, env var, or remote service (concept) — cross-link: dip-dependency-inversion
- Code: a `ConfigProvider.get(key)` interface with a typed accessor, and two implementations (code)
- Follow-up: "how do you handle a config value changing while the app is running?" (concept)
- Follow-up: "how do you keep this testable without hitting a real config source?" (concept)
- Weak answer: reading `System.getenv()` directly all over the codebase instead of behind an abstraction (pitfall)
- The 60-second version (concept)

### Topic: Design an undo mechanism (iv-design-undo-mechanism, intermediate)
The textbook Command-pattern application — an inverse operation, not a snapshot.
- The question, and why it's the textbook Command-pattern application (overview)
- Clarifying question: single-level undo, or a full undo/redo stack? (concept)
- The answer skeleton: encapsulate each action as a command with an inverse, keep a history stack (concept) — cross-link: command-pattern
- Code: a `Command` interface with `execute()`/`undo()`, and a `CommandHistory` stack (code)
- Follow-up: "what about actions that can't be cleanly inverted, like sending an email?" (concept)
- Follow-up: "how do you support redo after an undo?" (concept)
- Weak answer: storing full object snapshots for every action instead of an inverse operation, wasting memory (pitfall)
- The 60-second version (concept)

### Topic: Design a validation framework (iv-design-validation-framework, intermediate)
Composability is the point: rules combine, errors aggregate, nothing throws on the first miss.
- The question, and the composability it's really testing (overview)
- Clarifying question: field-level validation, or cross-field rules too? (concept)
- The answer skeleton: a `Rule<T>` interface, rules composed and run together, errors collected not thrown early (concept)
- Code: a `ValidationRule<T>` interface and a composite validator that runs all rules and aggregates errors (code) — cross-link: designing-errors
- Follow-up: "how do you support rules that depend on more than one field?" (concept)
- Follow-up: "should validation throw or return a result object?" (concept)
- Weak answer: throwing on the first failed rule instead of collecting all violations — poor UX for the caller (pitfall)
- The 60-second version (concept)

### Topic: Design an event bus (iv-design-event-bus, advanced)
Observer at API-design scale: publish/subscribe decoupling publishers from subscribers.
- The question, and how it's Observer at API-design scale (overview)
- Clarifying question: in-process only, or does this need to survive a process restart? (concept)
- The answer skeleton: a `publish`/`subscribe` API keyed by event type, decoupling publishers from subscribers (concept) — cross-link: observer-pattern
- Code: an `EventBus` interface (`publish(event)`, `subscribe(Class<T>, handler)`) and a simple in-memory implementation (code)
- Follow-up: "sync or async dispatch — what breaks if a handler throws?" (concept)
- Follow-up: "how does this differ from a message queue, and when do you need the queue instead?" (concept) — cross-link: queues-vs-pubsub
- Weak answer: letting one slow subscriber block every other subscriber synchronously (pitfall)
- The 60-second version (concept)

## Group: Distributed Systems Interview Bank — Foundations (interview-distributed-fundamentals)
*The distributed-systems viva underneath HLD — short, sharp questions probing whether you actually understand the primitives, not just the buzzwords.*

### Topic: Explain CAP theorem without the clichés (iv-explain-cap-without-cliches, intermediate)
"Pick two of three" as a universal law is the wrong answer — a partition is what forces the choice.
- The question, and why "pick two of three" is the wrong answer they're listening for (overview)
- Clarifying question: are they asking for the theorem, or for how you'd apply it to a specific system? (concept)
- The answer skeleton: define partition first, then show C and A are the only real choice during one (concept) — cross-link: cap-theorem-and-pacelc
- Diagram: a network partition forcing a choice between answering and staying consistent (diagram)
- Follow-up: "name a real system and which side of CAP it picked, and why" (concept)
- Follow-up: "what does PACELC add that CAP doesn't cover?" (concept)
- Weak answer: "you can only pick two of three" stated as a universal law, with no partition scenario (pitfall)
- The 60-second version (concept)

### Topic: Strong vs eventual consistency in one sentence — then defend it (iv-strong-vs-eventual-one-sentence, intermediate)
The follow-up ("defend it") is the actual test — a concrete case where eventual is genuinely fine.
- The question, and why the follow-up ("defend it") is the actual test (overview)
- Clarifying question: one sentence for the definition, or for when to use each? (concept)
- The answer skeleton: the one-liner, then the concrete case where eventual is actually fine (concept)
- Code: a read-after-write staleness example a user would actually notice (code)
- Follow-up: "give an example where eventual consistency is a real bug, not just a UX nit" (concept)
- Follow-up: "what's the practical middle ground — read-your-writes, bounded staleness?" (concept)
- Weak answer: treating strong consistency as strictly "better" instead of a cost trade-off (pitfall)
- The 60-second version (concept)

### Topic: What's the first thing that breaks at scale? (iv-what-breaks-first-at-scale, intermediate)
An open-ended probe for scaling instincts — name the specific first bottleneck, not "everything."
- The question, and why it's an open-ended probe for scaling instincts (overview)
- Clarifying question: scale in what dimension — traffic, data volume, or team size? (concept)
- The answer skeleton: name the bottleneck category (usually the database), then the specific failure mode (concept)
- Diagram: a single database instance saturating connections as QPS grows (diagram)
- Follow-up: "what's the very next thing that breaks after you fix that one?" (concept)
- Follow-up: "how do you find this before it breaks in production?" — load testing, capacity planning (concept)
- Weak answer: a generic "everything breaks at scale" with no concrete first bottleneck named (pitfall)
- The 60-second version (concept)

### Topic: Why is exactly-once delivery so hard? (iv-why-exactly-once-is-hard, advanced)
The impossibility result: an ack can always be lost after the effect, so you fall back to at-least-once + idempotency.
- The question, and the impossibility result it's actually testing (overview)
- Clarifying question: exactly-once processing, or exactly-once delivery specifically? (concept)
- The answer skeleton: the network can always fail after the effect but before the ack, so you get at-least-once + idempotency instead (concept) — cross-link: idempotency-and-exactly-once
- Diagram: the ack-lost-after-effect race that breaks true exactly-once (diagram)
- Follow-up: "so what do real systems actually claim, and how?" — dedup keys, idempotent consumers (concept)
- Follow-up: "does a transactional outbox solve this?" (concept)
- Weak answer: claiming a specific queue technology "guarantees exactly-once" with no idempotency layer (pitfall)
- The 60-second version (concept)

### Topic: How do you detect a dead node? (iv-how-to-detect-a-dead-node, intermediate)
"You can't, for sure" is part of the correct answer — heartbeats are a heuristic, not proof.
- The question, and why "you can't, for sure" is part of the correct answer (overview)
- Clarifying question: detecting a crash, or a network partition that looks like a crash? (concept)
- The answer skeleton: heartbeats/timeouts as a heuristic, phi-accrual as the refinement, and the fundamental ambiguity (concept) — cross-link: failure-detection
- Diagram: a heartbeat timeout that could mean "dead" or "just slow/partitioned" (diagram)
- Follow-up: "what's the risk of declaring a live node dead too early?" — split-brain, duplicate work (concept) — cross-link: split-brain-and-quorum-loss
- Follow-up: "how does phi-accrual improve on a fixed timeout?" (concept)
- Weak answer: "ping it, if it doesn't respond it's dead" — no acknowledgment of the ambiguity (pitfall)
- The 60-second version (concept)

### Topic: What is a fencing token and why do you need one? (iv-what-is-a-fencing-token, advanced)
Built for the "the old leader isn't really dead" scenario — a lock timeout alone doesn't solve it.
- The question, and the "the old leader isn't really dead" scenario it's built for (overview)
- Clarifying question: is this in the context of a lock, or leader election? (concept)
- The answer skeleton: a monotonically increasing token issued on each lease grant, checked by the resource before applying a write (concept) — cross-link: distributed-coordination
- Diagram: a paused-then-resumed old leader writing with a stale token, rejected by the resource (diagram)
- Code: a storage layer rejecting a write whose token is behind the latest seen (code)
- Follow-up: "why doesn't a simple lock timeout alone solve this?" (concept)
- Weak answer: describing a lock/lease without the token check that actually prevents the stale write (pitfall)
- The 60-second version (concept)

### Topic: What is split-brain and how do you prevent it? (iv-what-is-split-brain, advanced)
Quorum is the answer they're steering toward — a partition producing two leaders.
- The question, and why quorum is the answer they're steering toward (overview)
- Clarifying question: split-brain in a leader-election system, or in replicated storage? (concept)
- The answer skeleton: a partition where both sides think they're the leader, then quorum as the fix (concept) — cross-link: split-brain-and-quorum-loss
- Diagram: a network partition producing two leaders, each accepting writes (diagram)
- Follow-up: "what happens if you can't reach quorum on either side?" — the system should refuse writes (concept)
- Follow-up: "how does this relate to fencing tokens?" (concept) — cross-link: iv-what-is-a-fencing-token
- Weak answer: "just add more replicas" without explaining the quorum mechanism that actually prevents it (pitfall)
- The 60-second version (concept)

### Topic: How does clock skew break distributed systems? (iv-clock-skew-problems, advanced)
"Just use NTP" is incomplete — wall-clock ordering across nodes stays unreliable regardless.
- The question, and why "just use NTP" is an incomplete answer (overview)
- Clarifying question: wall-clock ordering, or clock-based expiry/leases specifically? (concept)
- The answer skeleton: clocks drift and jump, so wall-clock ordering across nodes is unreliable — name the fix (logical clocks, bounded uncertainty) (concept) — cross-link: time-and-ordering
- Diagram: two events on different nodes whose wall-clock timestamps disagree with true order (diagram)
- Code: a lease expiry computed from local wall-clock time that's wrong on a skewed node (code)
- Follow-up: "how do vector clocks or hybrid logical clocks help?" (concept)
- Follow-up: "how does Spanner's TrueTime approach this differently?" (concept)
- Weak answer: assuming NTP-synced clocks are close enough for correctness-critical ordering (pitfall)
- The 60-second version (concept)

## Boundary notes

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
