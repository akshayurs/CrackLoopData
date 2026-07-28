# Area: Programming Languages & Compilers (languages-compilers)

Reference outline for human review. Groups and slugs are taken verbatim from `briefs/area-group-map.md` § Area 6. Each Topic lists a one-line scope and a slide-heading outline (6–14 headings, content-driven). Cross-links to other Areas/Groups are noted inline instead of duplicating material.

---

## Group: Language Paradigms (paradigms)

*Scope: the paradigm-level mental models (imperative, OO, functional, logic, event-driven) and how to choose between them. Deep OOP design principles live in Area 8 (`object-oriented-design`); deep functional mechanics (monads, laziness) live in this area's `functional` group; async/event-loop mechanics live in `concurrency-models`.*

### Topic: Imperative & Procedural Programming (imperative-procedural-programming, beginner)
The default execution model — programs as sequences of state-changing statements — that every other paradigm reacts against.
- What "imperative" means: programs as sequences of state-changing statements
- The core building blocks: variables, assignment, control flow (if/while/for)
- Procedures & functions as named, reusable statement sequences
- Diagram: program state evolving step by step through a mutation timeline
- Structured programming: why `goto` fell out of favor (Dijkstra's argument)
- Code: a loop-based sum vs its accumulator-mutation trace
- Why imperative code is easy to write but hard to reason about at scale (aliasing, hidden state)
- Pitfall: mutating shared state across function calls causes order-dependent bugs
- Compare: procedural (C) vs structured procedural with modules (Pascal/Modula) vs modern imperative (Go)
- Where imperative thinking still wins: performance-critical, hardware-adjacent code
- Interview framing: "walk me through how this loop mutates state" trace-the-code questions

### Topic: Object-Oriented Programming as a Paradigm (object-oriented-paradigm, beginner)
OOP as one language-design paradigm — objects, messages, dynamic dispatch, encapsulation as a mental model; SOLID/patterns/deep design are Area 8, not here.
- The core idea: bundling state and behavior, computation as objects sending messages
- Encapsulation as an information-hiding contract, not just "private fields"
- Diagram: message passing between objects vs a function call in imperative code
- Dynamic dispatch: how "the same call" resolves to different code at runtime
- Code: a small polymorphic example (`shape.area()`) and what happens under the hood
- Classes vs prototypes: class-based (Java) vs prototype-based (JavaScript) object models
- Where this Topic's boundary sits: paradigm mental model here; SOLID/patterns/UML are Area 8 (`object-oriented-design`)
- Pitfall: deep inheritance hierarchies vs composition — why "favor composition" became conventional wisdom
- Compare: OOP vs procedural for modeling the same problem (a shape-area calculator)
- Interview framing: "is Python/JavaScript truly OOP?" — object models across languages

### Topic: Functional Programming as a Paradigm (functional-programming-paradigm, beginner)
The paradigm-level pitch for FP — pure functions, immutability, computing by expression evaluation; deep mechanics (monads, laziness, ADTs) live in the `functional` group.
- The core idea: computing by evaluating expressions, not executing mutating statements
- Pure functions and referential transparency, in one worked example
- Why "no side effects" makes code easier to test and to parallelize
- Diagram: imperative mutation trace vs functional expression-substitution trace for the same problem
- First-class functions as the paradigm's key mechanism (depth in `functional` group)
- Code: "sum of squares of evens," imperative vs functional
- Pitfall: mistaking "uses map/filter" for "is a functional program" (hidden mutation still counts)
- Compare: pure FP languages (Haskell) vs FP-influenced multi-paradigm languages (Scala, JS, Python)
- Cross-link: immutability, higher-order functions, and monads are covered in depth in the `functional` group
- Interview framing: "why would you choose a functional style for this function?"

### Topic: Logic & Declarative Programming (logic-and-declarative-programming, intermediate)
Programming by stating what's true or wanted and letting a solver find how — logic programming (Prolog) and declarative querying (SQL) as one family.
- The core idea: describe the goal/relation, not the steps to reach it
- Facts, rules, and queries in a logic program (Prolog-style unification)
- Diagram: a query resolving via backtracking search over rules
- Unification and backtracking as the "engine" behind declarative results
- Code: a tiny family-relations Prolog snippet and how a query resolves
- SQL as a mainstream declarative language: "what" (`SELECT`) vs "how" (query plan)
- Constraint programming: describing constraints and letting a solver satisfy them
- Compare: declarative vs imperative solutions to the same problem (a sorting rule vs a loop)
- Pitfall: declarative code can hide expensive search — "it's short" doesn't mean "it's fast"
- Interview framing: recognizing when a declarative reframe (SQL, regex, constraint) simplifies imperative code

### Topic: Event-Driven & Reactive Programming (event-driven-reactive-programming, intermediate)
The paradigm where control flow is driven by events/streams rather than top-down execution; the concurrency machinery underneath (event loop, async/await) is `concurrency-models`.
- The core idea: computation reacts to events/streams instead of running top to bottom
- Callbacks as the simplest event-driven mechanism, and "callback hell"
- Diagram: an event loop dispatching callbacks vs a linear imperative call stack
- Observer pattern and pub/sub as the classic event-driven building block
- Reactive streams: data as a first-class stream with operators (`map`/`filter`/`debounce`)
- Code: a button-click handler vs the same logic expressed as a reactive stream
- Cross-link: async/await and the event loop's concurrency mechanics are covered in `concurrency-models`
- Pitfall: losing a linear mental model makes debugging event chains hard ("callback spaghetti")
- Compare: event-driven UI programming (DOM events) vs reactive data pipelines (RxJS/Reactor)
- Interview framing: "how would you model a live price feed updating a UI?"

### Topic: Comparing Paradigms & Choosing One (comparing-paradigms-and-choosing-one, intermediate)
Synthesis Topic — how paradigm choice trades off testability, concurrency-safety, and performance; most real languages are multi-paradigm.
- Why most modern languages are multi-paradigm (Python, Scala, Rust, Kotlin)
- Decision lens: does this problem need shared mutable state, or can it be expressed as data transforms?
- Diagram: "process a list of orders" solved imperatively, OO, and functionally
- How paradigm choice affects testability (pure functions vs stateful objects)
- How paradigm choice affects concurrency safety (immutability sidesteps whole bug classes)
- Compare table: imperative vs OOP vs functional vs declarative — strengths, weaknesses, typical use
- Pitfall: forcing one paradigm everywhere (e.g., "everything is a class") when the problem doesn't fit
- Interview framing: "which paradigm would you use for X, and why" — structuring a strong answer

---

## Group: Type Systems (type-systems)

*Scope: how languages classify, check, and infer types — the compile-time/runtime axis, generics and variance, and the type-theoretic view of algebraic data types. Idiomatic FP usage of ADTs lives in `functional`.*

### Topic: Static vs Dynamic Typing (static-vs-dynamic-typing, beginner)
When type checks happen — compile-time vs runtime — and what that trades off; the most foundational type-system distinction.
- Definition: static typing checks types before running; dynamic typing checks at runtime
- Diagram: compile-time type-check gate vs runtime type-tag check, same buggy call in both
- Code: the same type error caught at compile time (TypeScript) vs blowing up at runtime (Python)
- What static typing buys you: earlier error detection, IDE tooling, refactor safety
- What dynamic typing buys you: flexibility, less ceremony, faster prototyping
- Gradual typing as the middle ground: TypeScript, Python type hints, mypy/Sorbet
- Pitfall: "static" doesn't mean "no runtime errors" — null derefs and bad casts still happen
- Compare: statically typed (Java, Rust) vs dynamically typed (Python, Ruby, JS) language families
- Interview framing: "what bugs would a type checker have caught here?" on a broken snippet

### Topic: Strong vs Weak Typing & Coercion (strong-vs-weak-typing-and-coercion, beginner)
The axis orthogonal to static/dynamic — how strictly a language enforces type rules and when it silently converts between types.
- Strong vs weak typing is orthogonal to static vs dynamic (four-quadrant framing)
- Implicit coercion examples: `"5" + 3` across JS, Python, and Java
- Diagram: the four-quadrant grid (static/dynamic × strong/weak) with example languages placed
- Code: JavaScript's `==` coercion surprises vs `===`
- Why weak typing trades safety for convenience — and where that bites in production
- Pitfall: relying on implicit coercion for correctness (e.g., truthy/falsy checks hiding bugs)
- Compare: Python (strong, dynamic) vs JavaScript (weak, dynamic) vs Java (strong, static)
- Interview framing: explaining a JS coercion gotcha and how to guard against it

### Topic: Type Inference (type-inference, intermediate)
How a compiler deduces types without explicit annotations — the mechanics behind `var`/`auto`/`let` and Hindley–Milner-style inference.
- Why inference exists: full type safety without writing every type by hand
- Local inference: `var`/`auto`/`let` inferring from the right-hand side (Java, C++, Kotlin)
- Diagram: unification solving type variables across an expression tree
- Global inference: Hindley–Milner in ML/Haskell inferring whole-function signatures
- Code: a generic identity function whose type is inferred purely from usage
- Where inference breaks down: ambiguous call sites, public API boundaries
- Pitfall: over-relying on inference hurts readability of public function signatures
- Compare: local inference (Java `var`) vs full inference (Haskell) — what each can and can't do
- Interview framing: "why did the compiler infer this type, and why did it fail here?"

### Topic: Generics & Parametric Polymorphism (generics-and-parametric-polymorphism, intermediate)
Writing code once that works safely across types — generic functions/classes and how different runtimes implement them.
- The problem generics solve: type-safe reuse without duplicating code per type or casting from `Object`/`Any`
- Diagram: a generic `Box<T>` compiling to specialized vs erased representations
- Code: a generic `max(a: T, b: T)` constrained by a `Comparable<T>` bound
- Bounded type parameters: constraining a generic to types with certain capabilities
- Type erasure (Java/C#) vs reification (Rust monomorphization)
- Cost/benefit: erasure's runtime simplicity vs monomorphization's code bloat and speed
- Pitfall: Java generic-array creation and raw-type interop surprises from erasure
- Compare: Java generics (erased) vs Rust generics (monomorphized) vs Go generics (recent addition)
- Interview framing: "why can't you do `new T()` in Java generics?"

### Topic: Subtyping & Variance (subtyping-and-variance, advanced)
When one type can safely substitute for another, especially through generic containers — covariance, contravariance, invariance, and Liskov substitution.
- Subtyping basics: when `Dog` can be used wherever `Animal` is expected
- The Liskov Substitution Principle stated precisely (behavioral, not just structural)
- Diagram: covariant vs contravariant vs invariant arrows for `List<Dog>` vs `List<Animal>`
- Why arrays are covariant in Java (historical) and the runtime `ArrayStoreException` trap
- Function-type variance: parameters are contravariant, return types are covariant
- Code: Kotlin/C# `out`/`in` declaration-site variance vs Java's `? extends`/`? super` use-site variance
- Pitfall: assuming generic containers are covariant "because subtyping is" — mutable containers can't be
- Compare: declaration-site variance (Kotlin, C#) vs use-site variance (Java wildcards)
- Interview framing: "why won't this `List<Dog>` compile where `List<Animal>` is expected?"

### Topic: Structural vs Nominal Typing (structural-vs-nominal-typing, intermediate)
Whether type compatibility is decided by shape (structural) or by declared name/hierarchy (nominal) — duck typing's formal cousin.
- Nominal typing: compatibility by declared type name/hierarchy (Java, C#)
- Structural typing: compatibility by shape — "if it has the right members" (Go interfaces, TypeScript)
- Diagram: two unrelated classes satisfying the same structural interface without declaring it
- Code: a TypeScript function accepting any object with a `.length`, no interface implemented
- Duck typing in dynamic languages as structural typing with no static check at all
- Go's implicit interface satisfaction as a mainstream structural-typing example
- Pitfall: accidental structural matches — a type "fits" an interface it was never meant to implement
- Compare: nominal (Java) vs structural (Go, TypeScript) — flexibility vs intentional-contract safety
- Interview framing: "how does Go achieve polymorphism without `implements`?"

### Topic: Null Safety & Optional Types (null-safety-and-optional-types, intermediate)
The "billion-dollar mistake" and how modern type systems eliminate null-pointer bugs at compile time via Option/Maybe and non-nullable-by-default types.
- Tony Hoare's null reference as "the billion-dollar mistake" — why it's a type-system problem
- Diagram: a nullable reference sneaking past the type checker into a runtime crash
- The Option/Maybe pattern: making "absence" an explicit, checked type instead of a hidden state
- Code: `Optional<T>`/`Option<T>` forcing a handle-both-cases check
- Non-nullable-by-default type systems: Kotlin, Swift, TypeScript strict mode
- Pitfall: `Optional.get()` without a check just moves the crash, it doesn't remove it
- Compare: null-permissive (Java, loose TS) vs null-safe-by-default (Kotlin, Swift, Rust)
- Interview framing: "redesign this API so null bugs are impossible, not just less likely"

### Topic: Algebraic Data Types & Exhaustive Matching (algebraic-data-types-and-exhaustive-matching, advanced)
Sum types and product types as a type-system feature, and compiler-checked exhaustiveness; idiomatic FP usage of ADTs lives in the `functional` group.
- Product types: structs/tuples/records as "AND" combinations of values
- Sum types: enums-with-data as "OR" — exactly one of several shapes, each with its own payload
- Diagram: a `Result<T, E>` sum type as a box holding either a success or an error value
- Code: a pattern match over a sum type (Rust `enum`, Kotlin `sealed class`, TS discriminated union)
- Exhaustiveness checking: the compiler forces handling every case, catching missed branches
- Modeling illegal states as unrepresentable: replacing a bag of nullable fields with a sum type
- Pitfall: simulating sum types with flags/nullable fields — the states the type system can't rule out
- Cross-link: idiomatic map/fold/pattern-matching usage of ADTs is covered in the `functional` group
- Interview framing: "redesign this state-as-booleans struct so invalid combinations can't compile"

---

## Group: Memory Management & GC (memory-gc)

*Scope: language/runtime-level object-lifetime management — who decides when memory is freed, and how. OS-level paging/segmentation is Area 3's `memory-management`/`virtual-memory`; hardware cache hierarchy is Area 5's `caches` — neither is re-taught here.*

### Topic: Stack vs Heap Allocation (stack-vs-heap-allocation, beginner)
Where values live at runtime and why it matters — the allocation model everything else in this group builds on.
- Stack: LIFO frames for function calls, automatic and fast alloc/dealloc
- Heap: long-lived, arbitrarily-sized allocations that outlive a single call
- Diagram: a call stack growing/shrinking with frames vs a heap of scattered objects
- Code: a local `int` (stack) vs a heap-allocated object, traced through a function call
- Why stack allocation is fast: pointer-bump, no bookkeeping vs the heap allocator's bookkeeping
- Escape analysis: how modern compilers promote heap objects to the stack when they don't escape
- Pitfall: returning a pointer/reference to a stack frame that has already been popped
- Compare: languages that expose the stack/heap choice (C, Rust, C++) vs those that hide it (Java, Python)
- Interview framing: "why is this recursive function blowing the stack, and how would you fix it?"

### Topic: Manual Memory Management (manual-memory-management, beginner)
Explicit alloc/free discipline (C-style) — the bugs it enables, motivating why GC and ownership models exist.
- The contract: every `malloc` needs exactly one `free`, never more
- Diagram: a leak (never freed) vs a double-free (freed twice) vs a dangling pointer (used after free)
- Code: a classic use-after-free bug that compiles fine but corrupts memory
- Fragmentation: how alloc/free patterns leave unusable gaps over time
- RAII as C++'s answer: tying free to scope exit via destructors, no manual `free` calls
- Pitfall: manual-management bugs are often silent until they crash somewhere unrelated
- Compare: raw manual management (C) vs RAII-scoped (C++) vs smart pointers (`unique_ptr`/`shared_ptr`)
- Interview framing: "find the memory bug in this C snippet" — a live-coding staple

### Topic: Reference Counting (reference-counting, intermediate)
Automatic memory management by counting owners — how it works, its one fatal flaw (cycles), and where it's used in production.
- The mechanism: each object carries a count of live references; free when it hits zero
- Diagram: two objects incrementing/decrementing each other's counts as references are made/dropped
- Code: Python's refcounting reclaiming an object the instant its last reference drops
- The cycles problem: two objects referencing each other never reach zero
- Breaking cycles: weak references, and why they don't count toward the total
- Real systems: CPython's refcounting (+ cycle-detecting backstop), Swift's ARC, C++ `shared_ptr`
- Pitfall: assuming refcounting means "no GC pauses" — cycle collection and atomic increments both cost
- Compare: refcounting (deterministic, immediate) vs tracing GC (batched, pause-based)
- Interview framing: "why does Swift still need a `weak` keyword if reference counting is automatic?"

### Topic: Tracing Garbage Collection — Mark-Sweep & Mark-Compact (tracing-gc-mark-sweep-and-compact, intermediate)
The core tracing-GC algorithm family — how "reachability from roots" replaces refcounting, and its stop-the-world cost.
- Reachability: an object is garbage if it's unreachable from a root set (stack, globals, registers)
- Diagram: mark phase flood-filling reachable objects from roots, sweep phase reclaiming the rest
- Pseudocode: the mark phase as a graph traversal (DFS/BFS from roots)
- Stop-the-world: why the mutator must pause while marking/sweeping
- Mark-sweep's fragmentation problem, and mark-compact's fix (sliding live objects together)
- Cost model: GC pause time scales with live-heap size (mark) and heap size (sweep/compact)
- Pitfall: assuming "has a GC" means "never leaks" — reachable-but-unused references still leak
- Compare: mark-sweep (fast, fragments) vs mark-compact (slower, no fragmentation) vs refcounting
- Interview framing: "why did this GC pause spike after we cached more objects than we needed?"

### Topic: Generational & Concurrent Garbage Collectors (generational-and-concurrent-gc, advanced)
How production GCs make tracing collection fast enough for real workloads — the generational hypothesis and low-pause concurrent designs.
- The weak generational hypothesis: most objects die young — optimize for that
- Diagram: young generation (frequent, cheap minor GC) promoting survivors into an old generation
- Write barriers: how the collector tracks old-to-young references cheaply between GCs
- Minor vs major (full) GC: why minor GCs are fast and major GCs are the ones that hurt
- Concurrent/incremental collectors: marking alongside the running program instead of stopping it
- Real collectors: JVM's G1/ZGC/Shenandoah and .NET's GC, at a "what problem each solves" level
- Pitfall: generational GC assumes short-lived garbage — long-lived caches full of churn defeat it
- Compare: throughput-optimized (older JVM GCs) vs latency-optimized (ZGC/Shenandoah) design goals
- Interview framing: "our p99 latency has 200ms GC pauses — what would you look at first?"

### Topic: Ownership & Borrowing — Memory Safety Without GC (ownership-and-borrowing, advanced)
Rust's compile-time memory-safety model — ownership, moves, and the borrow checker — as a third path beyond manual management and GC.
- The pitch: memory safety and determinism without a garbage collector or manual free calls
- Ownership rule: exactly one owner at a time; assignment moves, it doesn't copy by default
- Diagram: a value moving between owners, the old owner becoming invalid ("moved-from")
- Code: a use-after-move compile error, and the borrow-checker message explaining why
- Borrowing rules: many immutable borrows, or exactly one mutable borrow — never both
- How this rules out data races and use-after-free at compile time, not runtime
- Pitfall: fighting the borrow checker by cloning everywhere — losing the performance benefit it exists for
- Compare: GC (Java) vs manual (C) vs ownership (Rust) — where each puts the safety/cost trade-off
- Interview framing: "why doesn't Rust need a garbage collector, and what does it cost the programmer?"

### Topic: GC Tuning & Memory Leaks in Managed Languages (gc-tuning-and-memory-leaks, intermediate)
Practical diagnosis — how "leaks" happen even with a GC, and how to reason about collector behavior in production.
- How you leak memory in a garbage-collected language: reachable-but-forgotten references
- Common culprits: unbounded caches, static collections, unclosed listeners/subscriptions
- Diagram: a cache holding strong references that keep a whole object graph alive past its useful life
- Code: an event-listener leak pattern (subscribe without unsubscribe) and the fix
- Heap-dump analysis mental model: dominator trees, retained size vs shallow size
- GC tuning levers: heap sizing, generation sizing, choosing a collector for throughput vs latency
- Pitfall: chasing GC tuning flags before finding the actual retained-reference root cause
- Interview framing: "this service's memory grows until it OOMs after a few days — how do you debug it?"

---

## Group: Compilers & Interpreters (compilers)

*Scope: the static, compile-time pipeline from source text to (optimized) low-level code or bytecode. Execution-time behavior of that output — bytecode VMs, JIT, class loading — is `runtimes`.*

### Topic: The Compilation Pipeline (the-compilation-pipeline, beginner)
The end-to-end map from source text to running machine code — the scaffold every later Topic in this group slots into.
- The pipeline: source → lexer → parser → AST → semantic analysis → IR → optimization → codegen → machine code
- Diagram: the pipeline as stages with the artifact each stage produces/consumes
- Compiler vs interpreter vs JIT, positioned on one spectrum (depth in `runtimes`)
- Front end vs back end: language-specific analysis vs target-specific code generation
- Why splitting into stages matters: retargetable back ends, multiple front ends sharing one back end (LLVM)
- Code: a one-line expression traced through each pipeline stage's output
- Pitfall: treating "compiling" as one atomic step hides where a given bug/error actually originates
- Interview framing: "walk me through what happens when you run `gcc` on this file"

### Topic: Lexical Analysis (lexical-analysis, beginner)
Turning raw source text into a token stream — regular languages, DFAs, and where lexical errors are caught.
- Tokens: the atomic units (keywords, identifiers, literals, operators) a lexer produces
- Regular expressions as the specification language for token patterns
- Diagram: an NFA/DFA scanning characters and transitioning to a token match
- Code: a hand-rolled lexer loop tokenizing a small arithmetic expression
- Maximal munch: why `<=` isn't lexed as `<` then `=`
- Handling whitespace, comments, and lexical errors (invalid characters)
- Pitfall: keyword-vs-identifier conflicts, and why lexers use a keyword table after matching identifiers
- Interview framing: "write a tokenizer for a simple calculator expression"

### Topic: Parsing & Grammars (parsing-and-grammars, intermediate)
Turning a token stream into structure using context-free grammars — top-down vs bottom-up parsing strategies.
- Context-free grammars: productions, terminals/non-terminals, derivations
- Diagram: a parse tree built from a grammar for a small expression language
- Top-down parsing: recursive descent, and why left recursion breaks it
- Operator precedence via precedence climbing / Pratt parsing (a practical favorite)
- Bottom-up parsing: the shift-reduce intuition behind LR parsers (conceptual, not table construction)
- Code: a recursive-descent parser for arithmetic expressions with `+ - * /`
- Ambiguity: the dangling-else problem and how grammars/parsers resolve it
- Pitfall: a grammar that looks right but is ambiguous or needs unbounded lookahead
- Compare: hand-written recursive descent vs parser generators (yacc/ANTLR) — control vs dev speed
- Interview framing: "extend this expression parser to support parentheses and precedence"

### Topic: ASTs & Semantic Analysis (asts-and-semantic-analysis, intermediate)
What happens after parsing but before code generation — building a usable tree and checking that it makes sense (scope, types).
- AST vs parse tree: why compilers discard grammar noise and keep only meaningful structure
- Diagram: a parse tree for `2 + 3 * 4` collapsing into its AST
- Symbol tables: tracking declarations, scopes, and resolving names to their definitions
- Scope resolution: nested scopes, shadowing, and how a compiler picks the right binding
- Type checking as a semantic-analysis pass walking the AST
- Code: a small AST-walking type checker rejecting `"a" + 3` in a statically typed toy language
- Pitfall: conflating "parses" with "valid" — a program can be syntactically perfect and semantically wrong
- Interview framing: "why is this variable 'undefined' error caught at compile time here, but not there?"

### Topic: Intermediate Representations (intermediate-representations, intermediate)
Why compilers don't go straight from AST to machine code — three-address code, control-flow graphs, and SSA form.
- Why an IR exists: decoupling front ends (languages) from back ends (targets), enabling reuse (LLVM IR)
- Three-address code: breaking complex expressions into simple, uniform instructions
- Diagram: an AST lowered into a basic-block control-flow graph
- Basic blocks and control-flow graphs: the unit optimizations reason about
- Static Single Assignment (SSA): every variable assigned exactly once, and why that simplifies analysis
- Code: a small function's IR before and after conversion to SSA form (phi nodes included)
- Pitfall: trying to optimize directly on an AST instead of a lowered IR — much harder to reason about
- Compare: stack-based IR (JVM bytecode) vs register-based/SSA IR (LLVM) — depth in `runtimes`
- Interview framing: "why would a compiler introduce a phi node here?"

### Topic: Code Generation (code-generation, intermediate)
Turning optimized IR into real machine instructions — instruction selection, register allocation, and calling conventions.
- Instruction selection: matching IR patterns to available machine instructions
- Diagram: an IR expression tree tiled into machine instructions via pattern matching
- Register allocation: mapping unlimited virtual registers to a small set of physical ones
- Graph-coloring intuition: register allocation as coloring an interference graph
- Spilling: what happens when there aren't enough registers, and its performance cost
- Calling conventions: how arguments, return values, and saved registers cross function boundaries
- Code: a simple expression compiled to x86/ARM-like assembly, register by register
- Pitfall: ignoring calling conventions when hand-writing/inlining assembly — corrupting caller state
- Interview framing: "why did adding one more local variable slow this hot loop down?" (register pressure)

### Topic: Compiler Optimizations (compiler-optimizations, advanced)
The standard optimization passes that turn correct-but-naive IR into fast code, and what each buys you.
- Constant folding and constant propagation: computing what's already known at compile time
- Dead code elimination: removing computations whose results are never used
- Common subexpression elimination: computing a repeated expression once
- Diagram: a control-flow graph before/after dead-code and CSE passes
- Inlining: trading code size for removing call overhead, and when it backfires (bloat, cache pressure)
- Loop optimizations: invariant code motion, unrolling, strength reduction
- Code: a before/after snippet showing what an optimizer does to a small loop
- Pitfall: optimizations must preserve observable behavior — reordering across I/O or `volatile` is illegal
- Interview framing: "the compiler removed my benchmark loop entirely — why, and how do you stop it?"

### Topic: Interpreters — Tree-Walking vs Bytecode (interpreters-tree-walking-vs-bytecode, intermediate)
How execution works without producing native machine code — the interpreter side of the pipeline, bridging into `runtimes`.
- Tree-walking interpretation: directly executing the AST node by node
- Diagram: a tree-walk evaluating `2 + 3 * 4` by recursive descent over the AST
- Why tree-walking is slow: repeated dispatch overhead, no reusable compiled form
- Bytecode interpretation: compiling once to a compact instruction set, then executing that in a loop
- Code: a tiny stack-based bytecode program (`PUSH 2, PUSH 3, ADD`) and its execution trace
- Dispatch techniques: switch-based vs computed-goto vs direct-threaded interpreters
- Compare: tree-walking (simple, slow) vs bytecode (more work, much faster) vs JIT (depth in `runtimes`)
- Interview framing: "why is a bytecode VM faster than directly walking the AST?"

### Topic: Building a Toy Language — Tools of the Trade (building-a-toy-language-tools, beginner)
The practical "how would you actually build one" angle — parser generators vs hand-written, and where to draw that line.
- Parser-generator tools: lex/yacc, ANTLR — grammar in, parser out
- Parser combinators: building parsers by composing small functions (a modern, code-first alternative)
- Diagram: a grammar file feeding a generator that emits a parser, vs hand-written recursive descent
- Code: a minimal calculator grammar in a parser-combinator or PEG-style form
- When to hand-write a parser vs reach for a generator (error messages, control, learning curve)
- Real-world toy-language exercises interviewers use: JSON parser, calculator, tiny config language
- Pitfall: over-engineering a grammar for a problem a few regexes would solve
- Interview framing: "implement a parser for a simple arithmetic expression language" — full walkthrough

---

## Group: Runtimes & Virtual Machines (runtimes)

*Scope: what happens while compiled/bytecode output actually executes — bytecode VMs, JIT compilation, and concrete runtimes (JVM, CLR, V8, CPython). Builds on `compilers`' static pipeline; GC mechanics live in `memory-gc` and are referenced, not re-taught.*

### Topic: What a Runtime Provides (what-a-runtime-provides, beginner)
The services a language runtime layers over the OS/hardware — framing for the rest of this group.
- Definition: the runtime is what's running while your program runs, not just "the interpreter"
- Core services: memory management, type/safety enforcement, standard library, exception handling
- Diagram: a running program sitting atop its runtime, atop the OS, atop hardware
- Compile-time (compiler) vs run-time (runtime) responsibilities — where the line is drawn
- Managed runtimes (JVM, CLR, V8) vs "no separate runtime" languages (C) — gain vs cost
- Startup cost and footprint: why a runtime-backed app is slower to start than a native binary
- Pitfall: blaming "the language" for a slowdown that's actually a runtime warm-up/JIT effect
- Interview framing: "what's actually running when you launch a Java program?"

### Topic: Bytecode & Virtual Machines (bytecode-and-virtual-machines, intermediate)
The intermediate, portable instruction format most managed runtimes execute, and the VM designs that run it.
- Why bytecode: portability (compile once, run anywhere a VM exists) and a stable execution target
- Diagram: source compiling to bytecode, then a VM interpreting/JIT-compiling that bytecode
- Stack-based VMs: JVM and CLR bytecode operating on an implicit operand stack
- Register-based VMs: Lua and Dalvik/ART operating on virtual registers instead
- Code: a small Java method's bytecode (`javap`-style), read instruction by instruction
- Compare: stack-based (simpler bytecode, more instructions) vs register-based (fewer instructions)
- Pitfall: assuming bytecode execution is "interpreted and therefore always slow" — ignores JIT
- Interview framing: "what does `javap -c` show you, and why does the JVM use a stack machine?"

### Topic: Just-In-Time Compilation (just-in-time-compilation, intermediate)
How runtimes get native-code speed from bytecode by compiling hot paths while running — profiling, tiering, deoptimization.
- The spectrum: pure interpretation → JIT → ahead-of-time (AOT) compilation, and the trade-offs
- Diagram: cold code running interpreted while a profiler counts hot methods, then swapping in compiled code
- Profiling and hot-path detection: how the runtime decides what's worth compiling
- Tiered compilation: a fast unoptimized JIT tier first, a slower highly-optimized tier for hot code
- Speculative optimization: compiling for the common case observed so far (e.g., a monomorphic call site)
- Deoptimization: falling back to interpretation when a speculative assumption breaks
- Diagram: an inline cache going monomorphic → polymorphic → megamorphic as call-site types vary
- Pitfall: benchmarking a JIT'd language without a warm-up phase measures the interpreter, not the JIT
- Interview framing: "why was this microbenchmark 10x slower in the first 100ms than after?"

### Topic: The JVM Deep Dive (the-jvm-deep-dive, advanced)
A concrete, thorough walk through one real runtime — class loading, memory areas, and HotSpot's JIT tiers.
- Class loading: loading, linking (verify/prepare/resolve), and initialization phases
- Diagram: the classloader delegation hierarchy (bootstrap → platform → application)
- JVM memory areas: heap, per-thread stack, metaspace, and what lives in each
- HotSpot's JIT tiers: C1 (client, fast-compiling) and C2 (server, highly optimizing)
- The JIT compiling hot methods identified by invocation/back-edge counters
- Code: reading a `-XX:+PrintCompilation` trace to see tiering happen live
- Pitfall: confusing "out of memory: heap space" with "out of memory: metaspace" — different fixes
- Interview framing: "explain what happens from `java Main` to your first line of output"

### Topic: The CLR & .NET Runtime (the-clr-and-dotnet-runtime, intermediate)
.NET's answer to the JVM — Intermediate Language, assemblies, and RyuJIT — framed as a compare against the JVM.
- Assemblies and Intermediate Language (IL): .NET's equivalent of `.class` files and JVM bytecode
- Diagram: C# source → IL → RyuJIT-compiled native code at runtime
- RyuJIT: .NET's JIT compiler, and its tiered compilation (quick JIT then optimized)
- The CLR's generational garbage collector (mechanics are `memory-gc`; this Topic covers CLR specifics)
- ReadyToRun/AOT images: precompiling IL to native code to cut JIT warm-up cost
- Compare: JVM vs CLR — bytecode format, JIT strategy, GC, cross-language story
- Pitfall: assuming .NET is "Windows-only" — cross-platform CoreCLR changed this
- Interview framing: "how is compiling C# different from compiling Java, end to end?"

### Topic: Dynamic Language Runtimes — V8 & CPython (dynamic-language-runtimes-v8-and-cpython, advanced)
How runtimes make dynamically-typed languages fast (or don't) — V8's hidden classes and CPython's GIL-bound bytecode interpreter.
- The dynamic-typing tax: every property access/operation must handle "what if the type changes"
- V8 hidden classes (shapes): giving dynamically-typed objects a static-like layout under the hood
- Diagram: two objects with the same "shape" sharing a hidden class, enabling fast property access
- Inline caches: caching "last seen shape at this call site" to skip repeated lookups
- CPython's execution model: compiling to bytecode, then a straightforward interpreter loop
- The GIL: why CPython serializes bytecode execution across threads, and what it means for CPU-bound code
- Pitfall: adding threads to CPU-bound Python code expecting speedup, then hitting the GIL wall
- Compare: V8's JIT-heavy approach vs CPython's interpreter-first approach
- Interview framing: "why doesn't multithreading speed up this CPU-bound Python function?" (cross-link `concurrency-models`)

### Topic: Ahead-of-Time Compilation & Native Images (ahead-of-time-compilation-and-native-images, advanced)
Compiling a managed-language program fully to native code before it runs — trading runtime flexibility for startup speed and footprint.
- The AOT pitch: no JIT warm-up, smaller footprint, faster cold start — at a cost
- Diagram: JIT's "compile as you go" timeline vs AOT's "all compiled before first run" timeline
- What AOT gives up: reflection/dynamic class loading becomes limited or must be declared upfront
- GraalVM native-image as a concrete example: the closed-world assumption and its implications
- Statically compiled by default: Go and Rust ship native binaries with no separate runtime step
- Compare: JIT (peak throughput after warm-up) vs AOT (instant start, lower ceiling) — serverless vs long-running
- Pitfall: assuming AOT is strictly better — it can lose the headroom adaptive JIT profiling captures
- Interview framing: "why would a serverless function benefit from a native image over a JIT'd runtime?"

### Topic: Foreign Function Interfaces & Native Interop (foreign-function-interfaces-and-native-interop, intermediate)
How managed runtimes call into (and are called from) native code — JNI, P/Invoke, and the practical costs of crossing that boundary.
- Why FFI exists: reusing native libraries, performance-critical code, OS-level access
- JNI: Java calling into C/C++, and the boilerplate/marshaling it demands
- P/Invoke: .NET's simpler declarative approach to calling native functions
- Diagram: a call crossing from managed code, through marshaling, into native code and back
- Marshaling costs: converting managed strings/objects to native representations and back
- Pitfall: an FFI boundary that leaks native memory the GC doesn't know about
- Compare: JNI's verbosity vs P/Invoke's simplicity vs Rust's near-zero-cost C FFI
- Interview framing: "call a native image-processing library from your Java service — plan and risk?"

---

## Group: Concurrency Models (concurrency-models)

*Scope: language/runtime-level concurrency abstractions — how a program expresses "do things at once" and what safety it gets for free. OS-level scheduling and primitives (mutex/semaphore/monitor mechanics) are Area 3's `concurrency-sync`, referenced not re-taught.*

### Topic: Threads & the Shared-Memory Model (threads-and-the-shared-memory-model, beginner)
Language-level threading and the shared-mutable-state problem every other model in this group tries to avoid.
- What a language-level thread gives you: concurrent execution sharing the same memory space
- Concurrency vs parallelism: interleaved progress on one core vs simultaneous execution on many
- Diagram: multiple threads reading/writing the same heap object with interleaved execution
- Code: a non-atomic counter increment race condition across two threads
- Why shared mutable state is the root problem every other model in this group tries to avoid
- The language APIs: `Thread`/`Runnable` (Java), `threading` (Python), `std::thread` (C++) — same idea
- Cross-link: mutexes/semaphores/monitors as the fix are OS/language primitives in `concurrency-sync` (Area 3)
- Pitfall: "it works on my machine" races — non-deterministic bugs that vanish under a debugger
- Interview framing: "find the race condition in this multi-threaded counter" — a live-coding staple

### Topic: Async/Await & Cooperative Concurrency (async-await-and-cooperative-concurrency, intermediate)
Single-threaded concurrency via an event loop — how async/await sugars futures/promises into linear-looking code.
- The core idea: one thread, many in-flight operations, switching at await points instead of OS preemption
- Diagram: an event loop dispatching callbacks/continuations as I/O operations complete
- Futures/promises as a value representing "a result that isn't ready yet"
- Async/await as syntax sugar: what the compiler desugars it into (state machine/continuation)
- Code: a promise-chain vs the equivalent async/await version of the same logic
- Why async shines for I/O-bound work and does nothing for CPU-bound work
- Pitfall: an accidentally-blocking call inside async code stalls the entire event loop
- Compare: Node.js's single-threaded event loop vs Python's `asyncio` (cross-link CPython's GIL in `runtimes`)
- Interview framing: "why does one slow synchronous call in this async handler freeze all other requests?"

### Topic: The Actor Model (the-actor-model, intermediate)
Concurrency via isolated actors that only communicate by message — no shared state, ever — with Erlang/Akka as the reference implementations.
- The core rule: actors have private state and communicate only via asynchronous messages
- Diagram: actors as mailboxes — each processes one message at a time from its own queue
- Why "no shared state" eliminates data races by construction, not by discipline
- Code: a simple counter actor handling `Increment`/`GetCount` messages
- Supervision trees: parent actors restarting failed children — Erlang/Akka's "let it crash" philosophy
- Location transparency: actors can be local or remote without changing the calling code
- Pitfall: message ordering and backpressure — unbounded mailboxes can hide a failing consumer
- Compare: actor model (Erlang/Akka) vs shared-memory threads — which bug classes disappear entirely
- Interview framing: "design a chat-room service's concurrency model using actors"

### Topic: CSP & Channels (csp-and-channels, intermediate)
Go's concurrency model — goroutines and channels as typed pipes, and "don't communicate by sharing memory."
- The core idea: independent processes/goroutines communicating over explicit, typed channels
- Diagram: goroutines connected by channels, passing values instead of sharing a mutable variable
- Code: a producer/consumer pair coordinated by an unbuffered channel
- Buffered vs unbuffered channels: synchronous handoff vs a bounded queue
- The `select` statement: waiting on multiple channels, timeouts, non-blocking checks
- Go's mantra: "don't communicate by sharing memory; share memory by communicating"
- Pitfall: a goroutine leak — blocked forever on a channel nobody will ever write to or read from
- Compare: CSP channels (Go) vs actors (Erlang) — explicit pipes vs addressed mailboxes
- Interview framing: "use goroutines and channels to fan out work to N workers and collect results"

### Topic: Lock-Free Programming & Software Transactional Memory (lock-free-programming-and-stm, advanced)
Alternatives to blocking locks for shared-memory concurrency — CAS-based structures and STM's optimistic transactions.
- Why avoid locks: contention, priority inversion, deadlock risk under composition
- Compare-and-swap (CAS) as the atomic primitive underneath lock-free structures
- Diagram: a lock-free stack's push via a CAS retry loop
- The ABA problem: why "the value looks unchanged" doesn't mean "nothing happened"
- Code: a CAS-based lock-free counter/stack push, including the retry loop
- Software Transactional Memory: wrapping shared-state updates in optimistic, retryable transactions
- Pitfall: lock-free code is notoriously hard to get right — reordering bugs that need memory-model reasoning
- Compare: locks (simple, can deadlock) vs lock-free (composable-ish, hard to write) vs STM (retry overhead)
- Interview framing: "why would you reach for a CAS loop instead of just wrapping this in a mutex?"

### Topic: Structured Concurrency (structured-concurrency, advanced)
The modern discipline of scoping concurrent work to a lexical block so it can't outlive or leak past its caller.
- The problem: unstructured async spawns tasks nobody tracks, and cancellation/errors get lost
- Diagram: a parent scope owning child tasks vs a detached task outliving its logical owner
- The core rule: a concurrent scope doesn't exit until all its child tasks finish (or are cancelled)
- Code: a structured-concurrency block (Kotlin `coroutineScope`, or Java's structured concurrency API)
- Cancellation propagation: cancelling the parent cancels every child automatically
- Error propagation: one child's failure surfaces to the scope instead of vanishing silently
- Pitfall: a "fire and forget" background task that leaks, keeps running, or silently swallows an error
- Compare: unstructured futures/promises vs structured scopes — same power, contained lifetime
- Interview framing: "why did this cancelled request keep doing background work for 30 more seconds?"

### Topic: Comparing Concurrency Models (comparing-concurrency-models, intermediate)
Synthesis — how to choose threads vs async vs actors vs CSP for a given system, and what each protects you from.
- A decision framework: I/O-bound vs CPU-bound, and shared-state vs message-passing needs
- Compare table: threads, async/await, actors, CSP — memory model, failure isolation, typical use case
- Diagram: "handle 10,000 concurrent connections" solved by each model's approach
- Why "no shared state" models (actors, CSP) sidestep entire classes of races that threads must guard against
- Cost of abstraction: actors/CSP add message-passing overhead that raw shared-memory threads don't pay
- How production systems mix models (e.g., an actor system built on top of a thread pool)
- Interview framing: "you're designing a matching engine — which concurrency model, and why not the others?"

---

## Group: Functional Programming (functional)

*Scope: the mechanics and idioms of functional style in depth — immutability, higher-order functions, ADT usage, and monads. The paradigm-level pitch lives in `paradigms`; type-theoretic ADT mechanics live in `type-systems`.*

### Topic: Pure Functions & Immutability (pure-functions-and-immutability, beginner)
The two foundational disciplines FP is built on — referential transparency and never mutating shared data.
- Pure function definition: same input always gives same output, no observable side effects
- Referential transparency: replacing a call with its result never changes program behavior
- Diagram: a pure function as a black box with no hidden inputs/outputs (no ambient state)
- Code: a function that mutates an argument vs its pure, copy-returning equivalent
- Why immutability simplifies concurrency: no shared mutable state means no races to guard against
- Persistent data structures: sharing structure between "copies" instead of deep-copying
- Pitfall: "pure" functions that secretly log, mutate a captured variable, or throw — not actually pure
- Compare: mutating in place (imperative) vs returning a new value (functional) for the same list update
- Interview framing: "why is this function hard to unit test, and how would purity fix that?"

### Topic: Higher-Order Functions & Composition (higher-order-functions-and-composition, beginner)
Functions as values — passing, returning, and composing them — the mechanical toolkit of functional style.
- Functions as first-class values: passed as arguments, returned from functions, stored in data
- The classic trio: `map`, `filter`, `reduce`/`fold` as the building blocks of data transformation
- Diagram: a pipeline of `map → filter → reduce` transforming a list step by step
- Code: rewriting an imperative loop as a `map`/`filter`/`reduce` chain
- Currying and partial application: turning a multi-arg function into a chain of single-arg ones
- Function composition: building a new function by chaining smaller ones (`f . g`)
- Pitfall: composing so many small functions that stack traces and debugging get harder, not easier
- Compare: an imperative for-loop vs a composed pipeline solving the same transformation
- Interview framing: "rewrite this nested-loop data transformation using higher-order functions"

### Topic: Closures & Lexical Scope (closures-and-lexical-scope, intermediate)
How functions capture their defining environment — the mechanism that makes higher-order functions and callbacks actually work.
- What a closure is: a function bundled with the environment it was defined in
- Diagram: a returned inner function still holding a reference to its outer function's finished scope
- Code: a counter-generator closure (`makeCounter()`) that keeps private state between calls
- Lexical scope: variables resolve based on where code is written, not where it's called from
- The classic loop-variable capture bug (`var` in a loop) and why block scope (`let`) fixes it
- Practical uses: memoization, private state without classes, event-handler factories
- Pitfall: capturing a large object by reference in a closure that outlives its usefulness — a memory leak
- Interview framing: "why do all three callbacks print the same final value, and how do you fix it?"

### Topic: Recursion & Tail-Call Optimization (recursion-and-tail-call-optimization, intermediate)
Recursion as the functional replacement for loops, and the compiler trick (TCO) that makes it safe at scale.
- Why functional style favors recursion over mutable loop counters
- Diagram: a call stack growing one frame per recursive call vs staying flat under TCO
- The accumulator pattern: turning a non-tail-recursive function into a tail-recursive one
- Code: a factorial function rewritten with an accumulator parameter for tail-call form
- Tail-call optimization: how a compiler reuses the current frame instead of pushing a new one
- Which languages guarantee TCO (Scheme, Elixir) vs which don't (JavaScript, Python)
- Pitfall: assuming a recursive function is safe on large input without checking whether TCO actually applies
- Interview framing: "this recursive solution stack-overflows on large input — fix it without a loop"

### Topic: Algebraic Data Types in Functional Style (algebraic-data-types-in-functional-style, intermediate)
How FP idiomatically uses sum/product types day to day — mapping, folding, and pattern-matching over them.
- Quick recap: sum types (OR) and product types (AND) as the two data-shaping primitives (cross-link `type-systems`)
- Modeling a domain with ADTs instead of booleans/nullable fields: `Result<T, E>`, `Option<T>`
- Diagram: a `Shape` sum type (Circle/Rectangle/Triangle) and a function pattern-matching over all three
- Code: an exhaustive `match`/`when` computing area across every `Shape` variant
- Mapping and folding over a data type as the functional replacement for if/else chains on tags
- Making illegal states unrepresentable — the FP design habit, in a concrete before/after
- Pitfall: an "almost-ADT" using inheritance + `instanceof` checks — loses exhaustiveness checking
- Interview framing: "model a traffic light or payment status as a type so invalid states can't compile"

### Topic: Functors, Applicatives & Monads (functors-applicatives-and-monads, advanced)
The "explain monads" interview classic, built bottom-up from a concrete container type rather than category theory.
- Start concrete: `Option`/`Maybe` as a box that might be empty — the running example for this whole Topic
- Functor: anything with a `map` — applying a function inside the box without unwrapping it
- Diagram: `map` applying a plain function to a wrapped value, staying wrapped
- Applicative: applying a wrapped function to a wrapped value — combining two independent boxed values
- Monad: `flatMap`/`bind` — chaining operations that themselves return a wrapped value, avoiding nested boxes
- Code: chaining several `Optional`-returning lookups with `flatMap` vs the nested-if alternative
- The real-world monads you already use: `Optional`/`Maybe`, `Result`/`Either`, Promises/Futures, Lists
- Pitfall: reaching for "monad" as jargon instead of explaining it via concrete `map`/`flatMap` behavior
- Interview framing: "explain a monad without saying the word 'monad'" — the answer that actually lands

### Topic: Lazy Evaluation (lazy-evaluation, intermediate)
Deferring computation until its result is actually needed — thunks, infinite structures, and the space-leak trade-off.
- Strict (eager) vs lazy evaluation: compute now vs compute only when the value is demanded
- Diagram: a lazy list's thunks resolving one at a time only as they're consumed
- Code: an infinite sequence (natural numbers) that only lazy evaluation can represent meaningfully
- Where mainstream languages already use laziness: Python generators, Java Streams, JS generators
- Memoizing lazy values: computing once, caching the result for every later access
- Pitfall: space leaks — an unevaluated chain of thunks building up instead of running as it goes
- Compare: Haskell's default laziness vs mainstream languages' opt-in laziness (generators/streams)
- Interview framing: "why does this generator-based pipeline use constant memory on a huge input file?"

### Topic: Functional Programming in Mainstream Languages (functional-programming-in-mainstream-languages, intermediate)
Grounding this group in reality — how Java, Python, JavaScript, and Kotlin borrowed FP idioms, and how to mix FP with OOP pragmatically.
- Why "pure" FP languages (Haskell) stayed niche while FP idioms went mainstream everywhere else
- Java Streams and lambdas: `map`/`filter`/`collect` bringing FP style into an OOP language
- Python's functional side: comprehensions, `functools`, generator expressions
- JavaScript's array methods and first-class functions as its FP toolkit
- Diagram: a data pipeline written imperative-OOP-style vs the same pipeline in each language's FP style
- Kotlin/Scala as deliberately multi-paradigm: FP idioms with full OOP interop
- Pitfall: forcing a fully FP style into a codebase/team that isn't ready for it — readability regressions
- Interview framing: "refactor this imperative data-processing method into a Streams/functional pipeline"

---

## Cross-area boundaries (flagged, not duplicated)

- `object-oriented-paradigm` (this area) vs Area 8 `object-oriented-design` — paradigm mental model here; SOLID, patterns, UML stay in Area 8.
- `functional-programming-paradigm` (this area, `paradigms` group) vs the `functional` group (this area) — light pitch there, full mechanics (monads, laziness, closures) here.
- `algebraic-data-types-and-exhaustive-matching` (`type-systems`) vs `algebraic-data-types-in-functional-style` (`functional`) — type-theoretic mechanics/variance there, idiomatic map/fold/match usage here; cross-linked both ways.
- `memory-gc` group vs Area 3 `memory-management`/`virtual-memory` and Area 5 `caches` — language-level object lifetime here; OS paging/segmentation and hardware cache hierarchy stay in those areas.
- `concurrency-models` group vs Area 3 `concurrency-sync` — language/runtime concurrency abstractions here; OS-level mutex/semaphore/monitor mechanics stay there.
- `event-driven-reactive-programming` (`paradigms`) vs `async-await-and-cooperative-concurrency` (`concurrency-models`) — paradigm-level event mental model there vs event-loop/async mechanics here; cross-linked.
- `compilers` group vs `runtimes` group — static compile-time pipeline there, execution-time bytecode/JIT/runtime behavior here; several Topics cross-link explicitly (compilation pipeline, IR vs bytecode, interpreters vs JIT).
- `dynamic-language-runtimes-v8-and-cpython` (`runtimes`) GIL discussion cross-links `concurrency-models` for the concurrency-model implications.

No gaps identified against the group's stated scope (`imperative/OO/functional/logic`, `static/dynamic, inference, generics, variance`, `stack/heap, ref-counting, tracing GC`, `lexing/parsing, IR, codegen, optimization`, `JVM/CLR, JIT, bytecode`, `threads, async/await, actors, CSP`, `immutability, higher-order, monads`) — every scope keyword in `area-group-map.md` maps to at least one Topic above.
