# Interview Question Bank — LLD/OOD + Distributed-Systems Foundations (deepened, v2)

Supersedes `briefs/parts2/iv-lld.md` in full. Every existing topic below is deepened from
7-9 slides to 11-14; every group gains 6 new topics covering commonly-asked questions the
v1 pass missed. Slugs and levels for existing topics are unchanged — only their outlines
grew. New topics are `iv-`-prefixed and unique. As with v1: each topic teaches ANSWERING one
real, commonly-asked question, not the underlying concept (cross-linked instead) and not a
full case study (owned elsewhere).

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
