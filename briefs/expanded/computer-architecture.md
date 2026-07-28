# Area: Computer Architecture (computer-architecture)

Reference outline, pending human approval. Schema v3: `area → group → topic → slide`. This file expands two levels below each Group — Topics (L2) and a Slide outline (L3, types: concept/diagram/code/compare/pitfall). MCQs and Interview Questions attach at topic level and are out of scope for this pass. Groups and slugs are taken verbatim from `briefs/area-group-map.md §Area 5`.

---

## Group: Number Systems & Data Representation (data-representation)
*binary/hex, two's complement, IEEE-754*

### Topic: Positional Number Systems (positional-number-systems, beginner)
Binary/octal/hex representations and fast conversion between them, and why computers use base-2 at all.
- **concept:** Why base-2 — physical two-state storage, not human convenience
- **concept:** Positional notation — digit × base^position, generalizing decimal intuition
- **concept:** Binary → decimal and decimal → binary conversion, both directions
- **concept:** Hexadecimal as compressed binary — why one hex digit is exactly 4 bits
- **code:** Converting between bases in code (parsing a literal, formatting a value)
- **diagram:** Grouping a binary string into nibbles/bytes mapped onto hex digits
- **concept:** Octal — where it still appears (Unix file permissions) and why it's rarer today
- **compare:** Binary vs hex vs octal — when engineers reach for each in practice
- **pitfall:** Misreading a hex dump — nibble vs byte boundary confusion

### Topic: Signed Integer Representation (signed-integer-representation, beginner)
Sign-magnitude, one's complement, and two's complement, and why hardware standardized on the last.
- **concept:** The problem — representing negative numbers in a fixed-width register
- **concept:** Sign-magnitude — simplest scheme, but two representations of zero
- **concept:** One's complement — bitwise NOT, still has the two-zeros problem
- **concept:** Two's complement — invert-and-add-1, a single zero, one adder circuit for both signs
- **diagram:** A 4-bit two's-complement value wheel showing wraparound
- **concept:** Range asymmetry — why 8-bit signed spans -128..127, not -127..127
- **code:** Computing a two's-complement negation and verifying it against a worked example
- **compare:** Sign-magnitude vs one's complement vs two's complement — arithmetic circuit cost
- **pitfall:** Negating INT_MIN — the one value with no positive counterpart in the same width

### Topic: Integer Arithmetic & Overflow (integer-arithmetic-overflow, intermediate)
Binary add/subtract via two's complement and how hardware detects signed vs unsigned overflow.
- **concept:** Binary addition — bit-by-bit with carry, identical circuit for signed and unsigned
- **concept:** Subtraction as addition of the negation — no separate subtractor needed
- **concept:** Detecting signed overflow — the carry-into vs carry-out-of-sign-bit rule
- **diagram:** A ripple-carry adder chain producing sum, carry-out, and overflow
- **concept:** Unsigned overflow (carry flag) vs signed overflow (overflow flag) — same bits, different meaning
- **code:** A real integer-wraparound bug from unchecked arithmetic
- **compare:** Wraparound vs saturating arithmetic — general compute vs audio/DSP conventions
- **pitfall:** Assuming a compiler traps signed overflow — it's undefined behavior in C/C++, not a fault

### Topic: Fixed-Point Representation (fixed-point-representation, intermediate)
Qm.n fixed-point formats and why some domains (embedded, finance) deliberately avoid floats.
- **concept:** Fixed-point — an implicit binary point, Qm.n notation
- **concept:** Range vs precision trade-off — more fraction bits vs more integer bits
- **code:** A fixed-point multiply that needs a rescale (shift) the raw integer multiply doesn't give you
- **diagram:** Bit layout of a Qm.n value with the implicit point marked
- **compare:** Fixed-point vs floating-point — when embedded/DSP/financial systems prefer fixed
- **pitfall:** Storing money in floating point — why ledgers use integer cents or fixed-point instead

### Topic: IEEE-754 Floating Point (ieee-754-floating-point, intermediate)
The IEEE-754 bit layout, normalization, and the special values every implementation must handle.
- **concept:** The layout — sign bit, biased exponent, mantissa with an implicit leading 1
- **concept:** Why a biased exponent, not two's complement, encodes the exponent field
- **diagram:** A worked 32-bit single-precision bit pattern decoded field by field
- **code:** Decoding a float's raw bit pattern by hand
- **concept:** Normalization — the implicit leading 1 buys an extra bit of precision for free
- **concept:** Special values — signed zero, denormals, infinity, NaN, and why each exists
- **compare:** Single vs double precision — range, precision, and storage/compute cost
- **pitfall:** NaN != NaN — what that breaks in naive equality checks and sorting

### Topic: Floating-Point Arithmetic Pitfalls (floating-point-arithmetic-pitfalls, advanced)
Why floating-point math surprises engineers, and the concrete failure modes interviewers probe.
- **concept:** Why 0.1 + 0.2 != 0.3 — decimal fractions that aren't exact in binary
- **concept:** Machine epsilon — the smallest representable gap at a given magnitude
- **concept:** Catastrophic cancellation — subtracting nearly-equal floats destroys precision
- **code:** A naive running sum vs Kahan summation under heavy accumulation
- **compare:** Absolute vs relative epsilon when comparing two floats for "equality"
- **pitfall:** Using `==` on floats in a loop condition — a step that never lands exactly, infinite loop

### Topic: Character & Text Encoding (character-text-encoding, beginner)
ASCII, Unicode, and UTF-8/16 — how text becomes bytes and where the traps are.
- **concept:** ASCII — 7 bits, and why it fit early hardware (bytes, terminals) so cleanly
- **concept:** The Unicode problem — one codespace for every script and emoji in use
- **concept:** UTF-8 — variable-width, ASCII-compatible, self-synchronizing bytes
- **diagram:** UTF-8's 1–4 byte encoding rule with its continuation-byte pattern
- **compare:** UTF-8 vs UTF-16 vs UTF-32 — space efficiency vs fixed-width simplicity
- **code:** A string that looks like one visible character but is multiple bytes/codepoints
- **pitfall:** Counting "characters" by counting bytes — multi-byte codepoints and grapheme clusters

### Topic: Endianness (endianness, intermediate)
Byte ordering for multi-byte values, why it exists, and where it silently breaks real systems.
- **concept:** What endianness means — the byte order of a multi-byte value in memory
- **diagram:** The same 32-bit value laid out big-endian vs little-endian
- **concept:** Why little-endian dominates mainstream CPUs (x86, most ARM configurations)
- **concept:** Network byte order — why wire protocols standardized on big-endian
- **code:** Detecting host endianness at runtime and byte-swapping a value
- **compare:** Bi-endian architectures — CPUs that can switch modes, and why that's rare in practice
- **pitfall:** Parsing a binary file or network packet with the wrong endianness assumption

---

## Group: Digital Logic & Boolean Algebra (digital-logic)
*gates, K-maps, combinational/sequential*

### Topic: Boolean Algebra Fundamentals (boolean-algebra-fundamentals, beginner)
Core boolean operators, truth tables, and the algebraic laws used to simplify expressions by hand.
- **concept:** Boolean values and the three core operators — AND, OR, NOT
- **concept:** Truth tables — the exhaustive definition of any boolean function
- **concept:** De Morgan's laws — flipping AND/OR under negation
- **concept:** Algebraic laws — identity, distributive, absorption — simplifying by hand
- **code:** Evaluating a boolean expression and matching it against its truth table
- **compare:** Sum-of-products vs product-of-sums — the two canonical forms
- **pitfall:** Operator-precedence mistakes translating English requirements into boolean expressions

### Topic: Logic Gates & Circuits (logic-gates-and-circuits, beginner)
The physical gate set, universal gates, and reading small multi-gate circuits.
- **concept:** The basic gate set — AND, OR, NOT, XOR and their truth tables
- **concept:** NAND and NOR — the universal gates
- **diagram:** Building AND/OR/NOT purely from NAND gates
- **concept:** Why NAND is the physical default in CMOS fabrication
- **diagram:** A small multi-gate circuit evaluated step by step
- **code:** Simulating a logic circuit's truth table from its gate structure
- **compare:** Gate delay and fan-in cost across gate types

### Topic: Karnaugh Maps & Minimization (karnaugh-maps-minimization, intermediate)
Manual boolean minimization via K-maps, and why EDA tools use an algorithmic method at scale.
- **concept:** Why minimize — fewer gates means less delay and less power
- **concept:** K-map layout — Gray-code adjacency for 2/3/4-variable maps
- **diagram:** A worked 4-variable K-map with groupings circled
- **concept:** Grouping rules — powers of two, overlapping groups, don't-cares
- **concept:** Reading the minimized sum-of-products expression off the groups
- **compare:** K-maps vs Quine–McCluskey — manual vs algorithmic minimization
- **pitfall:** Missing a wrap-around adjacency — map edges are adjacent too

### Topic: Combinational Circuits (combinational-circuits, intermediate)
Adders, multiplexers, and decoders — the reusable building blocks composed from gates.
- **concept:** What makes a circuit combinational — output is a pure function of current inputs
- **diagram:** Half adder — XOR for sum, AND for carry
- **diagram:** Full adder — chaining half adders with a carry-in
- **concept:** Ripple-carry adder — chaining full adders, and its growing-latency problem
- **concept:** Multiplexer — select-line-driven routing, and its use as a universal function generator
- **concept:** Decoder/encoder — address-to-line and line-to-address conversion
- **compare:** Ripple-carry vs carry-lookahead adders — latency vs gate cost
- **code:** Implementing a mux-based function selector conceptually

### Topic: Sequential Circuits — Latches & Flip-Flops (sequential-circuits-latches-flipflops, intermediate)
Feedback-based memory elements, clocking, and the timing contract every flip-flop must satisfy.
- **concept:** Combinational vs sequential — adding feedback (memory) changes everything
- **concept:** SR latch — the basic feedback memory cell, and its forbidden state
- **concept:** D latch vs D flip-flop — level-triggered vs edge-triggered
- **diagram:** A clock edge triggering a flip-flop's state change
- **concept:** JK and T flip-flops — toggle behavior and where each is used
- **concept:** Setup time, hold time, and propagation delay — the timing contract
- **compare:** Latches vs flip-flops — level-sensitive vs edge-sensitive, why CPUs standardize on flip-flops
- **pitfall:** Violating setup/hold time — metastability

### Topic: Finite State Machines in Hardware (finite-state-machines-hw, advanced)
Moore vs Mealy machine design as the abstraction underlying every hardware control unit.
- **concept:** FSM as the sequential-circuit abstraction — states, transitions, outputs
- **concept:** Moore machine — output depends only on the current state
- **concept:** Mealy machine — output depends on state and input together
- **diagram:** A worked state-transition diagram for a simple sequence detector
- **concept:** State encoding — binary vs one-hot, and the area/speed trade-off
- **compare:** Moore vs Mealy — output timing and glitch behavior
- **code:** Implementing an FSM's next-state logic as a truth table / case structure

---

## Group: Instruction Set Architecture (isa)
*RISC/CISC, addressing, encoding*

### Topic: The Role of an ISA (isa-role-and-design, beginner)
What an ISA actually defines, and why it's the stable contract compilers and hardware both target.
- **concept:** The ISA as the contract between hardware and software
- **concept:** The layers below an ISA — microarchitecture can vary freely while the ISA stays fixed
- **compare:** ISA vs microarchitecture — one interface, many implementations
- **concept:** What an ISA must define — instructions, registers, memory model, calling convention
- **diagram:** The abstraction stack from high-level language down to gates
- **pitfall:** Conflating "faster CPU" with "different ISA" — most speedups are microarchitectural

### Topic: RISC vs CISC (risc-vs-cisc, beginner)
The two design philosophies, why RISC emerged, and how modern x86 blurs the line.
- **concept:** CISC philosophy — rich, variable-length instructions that do more per instruction
- **concept:** RISC philosophy — simple, fixed-length instructions, load/store architecture
- **concept:** Why RISC emerged — pipelining favors simple, uniform instructions
- **compare:** RISC vs CISC — instruction count vs cycles-per-instruction trade-off
- **concept:** Modern convergence — x86 decodes CISC instructions into RISC-like micro-ops internally
- **diagram:** The x86 front-end translating one CISC instruction into several micro-ops
- **pitfall:** Assuming "RISC" automatically means faster — compiler and workload determine the real outcome

### Topic: Instruction Formats & Encoding (instruction-formats-encoding, intermediate)
How opcode, operand, and immediate fields pack into an instruction word.
- **concept:** Fields in an instruction word — opcode, register operands, immediate/offset
- **diagram:** A worked bit-layout of a real fixed-width instruction (e.g., an R-type word)
- **concept:** Fixed-length encoding — simple decode, but limited immediates and wasted bits
- **concept:** Variable-length encoding — better density, but a harder decode stage
- **compare:** Fixed vs variable-length encoding — decode complexity vs code density
- **code:** Decoding a raw instruction word into opcode and operands by hand
- **pitfall:** An immediate field too narrow for a large constant — needing multiple instructions to build it

### Topic: Addressing Modes (addressing-modes, intermediate)
How an operand's location is computed — the modes that show up in every ISA comparison question.
- **concept:** What an addressing mode is — how an operand's location gets computed
- **concept:** Immediate and register addressing — the fastest modes
- **concept:** Direct and register-indirect addressing — pointer-style access
- **concept:** Indexed and base+offset addressing — array and struct-field access
- **concept:** PC-relative addressing — position-independent branches and data
- **diagram:** Effective-address computation for base + index + displacement
- **compare:** RISC's limited addressing modes vs CISC's rich modes — decode-cost trade-off
- **code:** Mapping a C array access (`a[i]`) onto the addressing mode it compiles to

### Topic: Registers & Register Files (registers-and-register-files, beginner)
The fastest storage tier, and the architectural-vs-physical register distinction interviewers probe.
- **concept:** The register file as the fastest storage tier — why so few architectural registers
- **concept:** General-purpose vs special-purpose registers (PC, stack pointer, flags/status)
- **diagram:** A register file with read/write ports
- **compare:** More architectural registers (RISC-V/ARM64) vs fewer (x86) — compiler impact
- **pitfall:** Confusing architectural registers (ISA-visible) with physical registers (renamed, microarchitecture-only)
- **concept:** Why register count is an ISA decision, not a free microarchitectural choice

### Topic: Instruction Types & Classes (instruction-types-and-classes, intermediate)
The families of instructions every ISA needs and how a simple `if` compiles down to them.
- **concept:** Data-movement instructions — loads, stores, register moves
- **concept:** Arithmetic and logic instructions — ALU operations and the flags they set
- **concept:** Control-flow instructions — branches, jumps, calls, returns
- **concept:** Comparison and conditional execution — how "if" compiles down
- **concept:** System/privileged instructions — syscalls, interrupts, mode switches (brief)
- **code:** Compiling a simple `if/else` in C to conditional-branch instructions
- **compare:** Conditional branches vs predicated/conditional-move instructions — avoiding branch penalty

### Topic: Assembly Language Basics (assembly-language-basics, intermediate)
Reading and writing simple assembly, and mapping familiar C constructs onto it.
- **concept:** Assembly as a human-readable, near-1:1 view of machine instructions
- **concept:** Reading a listing — labels, mnemonics, operands, comments
- **code:** A simple C loop next to its compiled assembly, line by line
- **code:** A function call in assembly — argument setup, call, return value
- **concept:** Assembler directives and pseudo-instructions — what gets expanded for you
- **compare:** AT&T vs Intel syntax — same instructions, different notation
- **pitfall:** Misreading operand order (source/destination) when switching syntaxes

### Topic: Calling Conventions & Stack Frames (calling-conventions-stack-frames, advanced)
The agreed contract that lets separately-compiled functions call each other correctly.
- **concept:** Why a calling convention exists — a contract for independently-compiled code to interoperate
- **diagram:** A stack-frame layout — return address, saved registers, locals, arguments
- **concept:** Argument passing — registers first, then the stack, and why
- **concept:** Caller-saved vs callee-saved registers — who preserves what
- **concept:** The prologue and epilogue — setting up and tearing down a frame
- **code:** Tracing a stack frame through a recursive function call
- **pitfall:** Stack-based buffer overflow — overwriting the return address (cross-link: Security → appsec)

---

## Group: CPU Datapath & Control (cpu-datapath)
*fetch-decode-execute, control signals*

### Topic: The Fetch-Decode-Execute Cycle (fetch-decode-execute-cycle, beginner)
The instruction cycle every CPU runs, before pipelining overlaps it.
- **concept:** The instruction cycle — fetch, decode, execute, (memory), write-back
- **diagram:** The cycle as a loop feeding back into the program counter
- **concept:** The program counter — how it advances, and how branches redirect it
- **concept:** Fetch — reading the instruction word from memory via the PC
- **concept:** Decode — extracting opcode/operands, reading the register file
- **concept:** Execute — the ALU operation, memory access, or branch resolution
- **compare:** This single-instruction cycle vs the pipelined version (cross-link: Pipelining) — same steps, overlapped

### Topic: Single-Cycle Datapath (single-cycle-datapath, intermediate)
Building a complete datapath where one instruction fully completes per clock cycle.
- **concept:** What "single-cycle" means — one instruction fully completes per clock
- **diagram:** The full single-cycle datapath — PC, instruction memory, register file, ALU, data memory, muxes
- **concept:** Multiplexers as the datapath's decision points — selecting ALU operand or write-back source
- **concept:** Why the clock period must fit the slowest instruction (load), wasting time on simpler ones
- **code:** Tracing register values through the datapath for one instruction, cycle by cycle
- **compare:** Single-cycle vs multi-cycle — simplicity vs efficiency
- **pitfall:** Assuming every instruction "should" take equal time — the slowest path sets the clock

### Topic: Control Unit Design (control-unit-design, intermediate)
How an opcode becomes the control signals that steer the datapath.
- **concept:** The control unit's job — turning an opcode into the signals that steer the datapath
- **diagram:** Opcode → control-signals truth table for a small instruction subset
- **concept:** Hardwired control — combinational logic straight from opcode bits
- **concept:** Microprogrammed control — a small program (microcode) interpreting the instruction
- **compare:** Hardwired vs microprogrammed control — speed vs flexibility/ease of change
- **concept:** Why hardwired suits RISC and microprogrammed suited CISC's larger instruction sets

### Topic: Multi-Cycle Datapath (multi-cycle-datapath, advanced)
Splitting execution into steps to share hardware, and the FSM that sequences them.
- **concept:** Why break execution into multiple cycles — share one ALU/memory across steps
- **diagram:** The multi-cycle datapath with internal registers/latches added between steps
- **concept:** Per-instruction cycle counts — why loads take longer than register-register ops
- **concept:** The FSM controller (cross-link: digital-logic → finite-state-machines-hw) sequencing multi-cycle steps
- **compare:** Single-cycle vs multi-cycle vs pipelined — the evolution and why each came next
- **code:** Tracing an instruction through several clock cycles' worth of internal state

### Topic: ALU Design (alu-design, intermediate)
Building the arithmetic-logic unit and the flags every instruction downstream depends on.
- **concept:** The ALU's job — arithmetic and logic operations selected by a function code
- **diagram:** A simple ALU built from an adder plus logic-gate muxes selected by opcode
- **concept:** Flag generation — zero, carry, overflow, negative — and where each feeds back
- **concept:** Building subtraction from addition — reuse via two's complement (cross-link: data-representation)
- **compare:** Ripple-carry vs carry-lookahead adders inside the ALU — latency in the critical path
- **code:** Composing an ALU operation table (add/sub/and/or/set-less-than) and its selector bits

### Topic: Microprogramming (microprogramming, advanced)
Control as a stored program, and why modern x86 still runs microcode under the hood.
- **concept:** The control store — microcode as "a program that runs the hardware"
- **diagram:** A microinstruction format — control-signal bits plus a next-address field
- **concept:** Horizontal vs vertical microcode — wide-and-direct vs narrow-and-encoded
- **concept:** Why microprogramming let complex CISC ISAs be built without exploding gate count
- **compare:** Microcode vs hardwired control — updatability (microcode patches) vs raw speed
- **pitfall:** Assuming microcode is obsolete — modern x86 still uses it for complex/legacy instructions

### Topic: Interrupts & Exceptions at the Datapath Level (interrupts-and-exceptions-datapath, advanced)
How hardware detects and cleanly redirects on an exception, before the OS handler runs.
- **concept:** Precise exceptions — stopping cleanly at a well-defined instruction boundary
- **concept:** Detecting exception conditions per stage (overflow, invalid opcode, page fault)
- **diagram:** An exception redirecting the PC to a handler address while saving return state
- **compare:** Interrupts (external, asynchronous) vs exceptions (internal, synchronous) (cross-link: OS → processes-threads)
- **concept:** Vectored vs single-entry-point exception handling
- **pitfall:** Imprecise exceptions in deeply pipelined/OoO CPUs — why precise handling gets hard (cross-link: ILP)

---

## Group: Pipelining & Hazards (pipelining)
*stages, structural/data/control hazards*

### Topic: Pipelining Fundamentals (pipelining-fundamentals, intermediate)
The assembly-line analogy, and why pipelining raises throughput, not per-instruction latency.
- **concept:** The assembly-line analogy — overlapping independent stages of different instructions
- **concept:** Latency vs throughput — pipelining speeds up the stream, not any one instruction
- **diagram:** A pipeline diagram showing overlapped instructions across stages and cycles
- **concept:** Ideal speedup — roughly the stage count, and why it's never fully reached
- **compare:** Pipelined vs non-pipelined execution — cycle-by-cycle instruction completion
- **pitfall:** Believing pipelining reduces one instruction's latency — it doesn't

### Topic: The Classic 5-Stage Pipeline (classic-5-stage-pipeline, intermediate)
IF/ID/EX/MEM/WB and the pipeline registers that carry state between them.
- **concept:** The five stages — Fetch, Decode, Execute, Memory access, Write-back
- **diagram:** The 5-stage datapath with pipeline registers between stages
- **concept:** What each pipeline register must carry forward — control signals plus data
- **concept:** Why this exact stage split — balancing work so no stage dominates the clock period
- **code:** Tracing four back-to-back instructions through all five stages over time
- **compare:** This 5-stage pipeline vs the much deeper pipelines in modern CPUs (cross-link: ILP → superscalar-execution)

### Topic: Structural Hazards (structural-hazards, intermediate)
Resource conflicts between in-flight instructions, and the two ways to resolve them.
- **concept:** What a structural hazard is — two instructions wanting the same hardware at once
- **concept:** The classic example — a single memory port serving both fetch and data access
- **concept:** Resolving via duplication — separate instruction/data memories (or caches)
- **concept:** Resolving via stalling — inserting a bubble when duplication isn't worth the cost
- **diagram:** A pipeline bubble stalling one instruction to free a shared resource
- **compare:** Duplicating hardware vs stalling — area/power cost vs performance cost

### Topic: Data Hazards & Forwarding (data-hazards-and-forwarding, advanced)
RAW hazards, why forwarding fixes most of them, and the one case it can't.
- **concept:** RAW (read-after-write) — the hazard that actually occurs in an in-order pipeline
- **concept:** WAR and WAW — why they can't occur in a simple in-order pipeline (but matter later, cross-link: ILP)
- **diagram:** A dependent instruction pair hitting a hazard in the pipeline diagram
- **concept:** Forwarding/bypassing — routing a result from EX/MEM straight back into EX, skipping the register file
- **diagram:** Forwarding paths added onto the 5-stage datapath
- **concept:** The load-use hazard — the one case forwarding can't fully fix, forcing one stall cycle
- **code:** A short instruction sequence with a load-use hazard and the stall it forces
- **compare:** Full forwarding vs compiler-inserted NOPs vs hardware stalling — who resolves the hazard

### Topic: Control Hazards & Branching (control-hazards-and-branching, advanced)
The cost of not knowing the next PC, and the spectrum of fixes from stalling to prediction.
- **concept:** The control hazard — not knowing the next PC until a branch resolves
- **concept:** The naive fix — stall until the branch resolves, and its throughput cost
- **concept:** Static prediction — always-not-taken / always-taken / backward-taken-forward-not-taken
- **diagram:** A pipeline flush when a predicted branch resolves the other way
- **concept:** Delayed branch slots — a historical RISC trick, and why it fell out of favor
- **compare:** Stalling vs static prediction vs dynamic prediction (cross-link: ILP → branch-prediction owns the deep dive)
- **pitfall:** Underestimating misprediction cost in deep pipelines — the flush penalty grows with pipeline depth

### Topic: Pipeline Performance Analysis (pipeline-performance-analysis, advanced)
Quantifying real pipeline CPI once hazard stalls are accounted for.
- **concept:** CPI (cycles per instruction) as the pipeline's scorecard
- **concept:** Base CPI vs stall cycles — decomposing real CPI into ideal plus hazard penalties
- **code:** Computing effective CPI given hazard frequencies and per-hazard stall penalties
- **concept:** The speedup formula — comparing pipelined vs non-pipelined execution time
- **compare:** Deeper pipelines — higher clock-speed potential vs higher hazard/misprediction cost
- **pitfall:** Comparing CPUs by clock speed alone, ignoring CPI differences

### Topic: Exceptions in Pipelines (exceptions-in-pipelines, advanced)
Keeping exceptions precise once multiple instructions are in flight at once.
- **concept:** Precise exceptions — state must look as if execution stopped cleanly at one instruction
- **concept:** Detecting a mid-pipeline exception (e.g., an earlier instruction's fault surfacing late)
- **diagram:** Flushing younger, in-flight instructions once an older instruction's exception is confirmed
- **concept:** In-order commit as the mechanism that preserves precise exceptions
- **pitfall:** Two in-flight instructions both raising exceptions — the older one must be reported first
- **compare:** Precise exceptions in a simple pipeline vs the much harder out-of-order case (cross-link: ILP)

---

## Group: Memory Hierarchy & Caches (caches)
*locality, mapping, coherence, policies*

### Topic: Memory Hierarchy & Locality (memory-hierarchy-and-locality, beginner)
Why the hierarchy exists at all, grounded in temporal and spatial locality.
- **concept:** The memory hierarchy — registers → cache → RAM → disk, trading capacity for speed
- **concept:** Temporal locality — recently accessed data tends to be accessed again soon
- **concept:** Spatial locality — nearby addresses tend to be accessed together
- **diagram:** The hierarchy pyramid with rough latency/size numbers at each level
- **concept:** Why the hierarchy works — real programs exhibit locality, so a small fast cache captures most accesses
- **code:** A loop with strong spatial locality (row-major scan) vs one without (column-major scan)
- **pitfall:** Assuming more RAM alone fixes performance — a locality-unfriendly access pattern still thrashes cache

### Topic: Cache Basics — Hits & Misses (cache-basics-hits-misses, beginner)
The cache line, hit/miss mechanics, and the single-level AMAT formula.
- **concept:** The cache line/block — the unit of transfer between cache and memory
- **concept:** Hit vs miss — and why a miss costs so much more than a hit
- **concept:** Hit rate / miss rate as the cache's headline metric
- **concept:** Average Memory Access Time (AMAT) — the single-level formula
- **diagram:** A memory request flowing through cache, hitting or missing, fetching a block on miss
- **code:** Computing hit rate from a short trace of memory accesses
- **pitfall:** Chasing hit rate in isolation — a 99% hit rate can lose to 90% if the miss penalties differ enough

### Topic: Cache Placement Policies (cache-placement-policies, intermediate)
Direct-mapped, fully associative, and set-associative placement, and the tag/index/offset split.
- **concept:** The placement question — where in the cache can a given memory block go?
- **concept:** Direct-mapped — one possible slot, simplest hardware, most conflicts
- **concept:** Fully associative — any slot, no conflicts, expensive comparison hardware
- **concept:** Set-associative — the practical middle ground, N-way sets
- **diagram:** Splitting an address into tag/index/offset for each placement scheme
- **code:** Computing the index and tag for a given address under direct-mapped vs 4-way set-associative
- **compare:** Direct-mapped vs set-associative vs fully-associative — hit rate vs hardware cost vs latency

### Topic: Cache Replacement Policies (cache-replacement-policies, intermediate)
LRU and its cheaper approximations, and why true LRU doesn't scale to high associativity.
- **concept:** The replacement question — which line to evict when a set is full
- **concept:** LRU — evict the least-recently-used line, and why it approximates optimal well
- **concept:** FIFO and Random — simpler, cheaper approximations and when they're used
- **concept:** Approximating LRU in hardware — clock/pseudo-LRU bits, since true LRU is costly at high associativity
- **diagram:** An LRU stack updating across a sequence of accesses in a 4-way set
- **code:** Simulating LRU eviction over a small access trace
- **compare:** LRU vs Belady's optimal (MIN) — why optimal isn't implementable online (cross-link: OS → memory-management)

### Topic: Cache Write Policies (cache-write-policies, intermediate)
Write-through vs write-back, and the allocate-on-write-miss decision.
- **concept:** The write problem — keeping cache and memory consistent on a write
- **concept:** Write-through — every write goes to memory immediately, simple but bandwidth-heavy
- **concept:** Write-back — writes stay in cache until eviction, needs a dirty bit
- **concept:** Write-allocate vs no-write-allocate — what happens on a write miss
- **diagram:** A dirty bit's lifecycle — set on write, checked and cleared on eviction/write-back
- **compare:** Write-through+no-allocate vs write-back+write-allocate — the two common pairings and why
- **pitfall:** Forgetting the dirty bit — a write-back cache can silently lose data if evicted incorrectly

### Topic: Multi-Level Caches (multi-level-caches, intermediate)
Why L1/L2/L3 exist, and the inclusion policy that governs what each level must hold.
- **concept:** Why multiple levels — one cache can't be both very fast and very large
- **concept:** L1 — split I-cache/D-cache, smallest and fastest, per-core
- **concept:** L2 — larger, usually per-core, a few cycles slower
- **concept:** L3 — shared across cores, largest, closest to memory latency
- **diagram:** The L1/L2/L3/memory hierarchy with typical sizes and latencies per level
- **concept:** Inclusive vs exclusive vs non-inclusive multi-level policies
- **compare:** Inclusive vs exclusive caches — capacity waste vs coherence simplicity

### Topic: Cache Miss Classification — the 3 Cs (cache-misses-classification, advanced)
Compulsory, capacity, and conflict misses, and which fix addresses each.
- **concept:** The 3 Cs framework — compulsory, capacity, and conflict misses
- **concept:** Compulsory (cold) misses — the unavoidable first-touch cost
- **concept:** Capacity misses — the working set simply doesn't fit
- **concept:** Conflict misses — misses a fully-associative cache of the same size wouldn't have
- **diagram:** The same access trace producing different miss types under direct-mapped vs associative caches
- **concept:** The 4th C — coherence misses in multiprocessor caches (cross-link: cache-coherence-protocols)
- **compare:** Which C dominates for a given workload, and the matching fix (bigger cache, more associativity, prefetch)

### Topic: Cache Coherence Protocols (cache-coherence-protocols, advanced)
The multicore coherence problem and the MESI protocol that solves it.
- **concept:** The coherence problem — multiple per-core caches holding copies of the same line
- **concept:** What coherence guarantees — single-writer-or-multiple-readers, writes eventually visible
- **concept:** Snooping-based coherence — every cache watches a shared bus
- **concept:** The MESI protocol — Modified/Exclusive/Shared/Invalid states and their transitions
- **diagram:** A MESI state-transition walk for one cache line across a read/write sequence from two cores
- **concept:** Directory-based coherence — replacing broadcast with a directory as core counts scale up
- **compare:** Snooping vs directory-based coherence — bus-broadcast cost vs directory storage/indirection cost
- **pitfall:** Confusing cache coherence (one address, consistent value) with memory consistency (ordering across addresses) (cross-link: Multicore → memory-consistency-models)

### Topic: Cache-Conscious Programming (cache-conscious-programming, advanced)
Writing code that respects the memory hierarchy — where "mechanical sympathy" pays off.
- **concept:** Writing code that respects the memory hierarchy — the "mechanical sympathy" idea
- **concept:** Loop tiling/blocking — reordering nested loops so a working set fits in cache
- **code:** A cache-blocked matrix multiply vs the naive triple loop
- **concept:** Array-of-structs vs struct-of-arrays — layout changes what a cache line actually holds
- **concept:** False sharing — independent variables on the same cache line thrash performance on multicore (cross-link: Multicore)
- **code:** A false-sharing example — two threads updating adjacent counters in one cache line
- **pitfall:** Trusting Big-O alone to predict real performance — cache-driven constant factors can dominate

### Topic: AMAT & Cache Performance Analysis (amat-and-cache-performance-analysis, advanced)
Extending AMAT across a real multi-level hierarchy and using it to guide design trade-offs.
- **concept:** Extending AMAT to multiple levels — each level's miss penalty is the next level's AMAT
- **code:** Computing overall AMAT given L1/L2/L3 hit rates and latencies
- **concept:** Local vs global miss rate — what each measures, and why L2+ is usually reported as global
- **compare:** Where to spend transistor budget — bigger L1 vs bigger L2/L3 vs more associativity, using AMAT to decide
- **concept:** Miss penalty vs miss rate — which one a given optimization actually reduces
- **pitfall:** Improving hit rate while increasing hit latency (bigger/more-associative cache) and losing on overall AMAT

---

## Group: Virtual Memory (HW view) (hw-virtual-memory)
*TLB, page-table walk*

*Scope boundary: hardware translation mechanism only. Replacement policy, thrashing, and OS-level page management live in Area 3 (Operating Systems) → `virtual-memory`.*

### Topic: Why Hardware Needs Virtual Memory (virtual-memory-hw-motivation, intermediate)
The three jobs hardware must support: translation, protection, isolation.
- **concept:** The three jobs virtual memory gives hardware — translation, protection, isolation
- **concept:** Every process getting its own address space — the illusion hardware maintains
- **diagram:** Virtual address → MMU → physical address, with a process boundary drawn
- **concept:** The Memory Management Unit (MMU) — the hardware block sitting between the core and memory
- **compare:** What's a hardware concern (translation mechanism) vs an OS concern (page-replacement policy) (cross-link: OS → virtual-memory)
- **pitfall:** Thinking virtual memory is only "more RAM via disk" — protection and isolation are equally core motivations

### Topic: Page Tables & Translation (page-tables-and-translation, intermediate)
The lookup structure hardware walks to turn a virtual address into a physical one.
- **concept:** The page table as a lookup structure — virtual page number to physical frame number
- **concept:** Why multi-level (hierarchical) page tables — a flat table for a 64-bit space is absurd
- **diagram:** A multi-level page-table walk from virtual address to physical frame (x86-64 style)
- **concept:** The page-table entry (PTE) — frame number plus valid/protection/dirty/accessed bits
- **code:** Splitting a virtual address into page-table indices and offset for a given page size
- **compare:** Hierarchical vs inverted page tables — space trade-off at large address-space sizes
- **pitfall:** Underestimating page-table memory overhead itself for sparse address spaces

### Topic: TLB Design (tlb-design, intermediate)
The translation cache that makes virtual memory affordable, and why it matters so much for performance.
- **concept:** The TLB as a cache for translations — why translation itself needs caching
- **concept:** TLB hit — skip the page-table walk entirely, the common case
- **concept:** TLB miss — trigger a page-table walk (hardware- or software-walked)
- **diagram:** The TLB sitting between the CPU and the cache/memory system in the translation path
- **concept:** TLB reach — how coverage (entries × page size) limits how much memory avoids walks
- **compare:** Hardware-managed TLB (x86) vs software-managed TLB (some RISC/MIPS) — flexibility vs miss cost
- **pitfall:** A TLB flush on every context switch being expensive — motivating ASIDs/tagged TLBs

### Topic: Hardware Page-Table Walk (hardware-page-table-walk, advanced)
What happens, step by step, on a TLB miss.
- **concept:** What happens on a TLB miss — the hardware (or OS) must walk the page table
- **diagram:** A step-by-step walk through several page-table levels to resolve one address
- **concept:** The hardware page-table walker — a dedicated state machine that walks without trapping to software
- **concept:** Caching intermediate page-table levels to reduce repeated walk cost
- **compare:** Hardware walker vs software-handled TLB miss (a trap plus OS routine) — latency vs flexibility
- **pitfall:** A page-table walk itself causing more cache misses — walks touch memory too

### Topic: Memory Protection in Hardware (memory-protection-hw, intermediate)
Permission bits and privilege levels as hardware-enforced, not software-trusted.
- **concept:** Protection bits in the PTE — read/write/execute, user/supervisor
- **concept:** Privilege levels/rings — hardware-enforced boundaries between user and kernel code
- **diagram:** A protection violation triggering a fault that traps into the OS
- **concept:** Segmentation's remnants — base/limit checks still present alongside paging in some architectures
- **compare:** Paging-only protection vs segmentation+paging — why most systems dropped pure segmentation
- **pitfall:** Assuming "user mode" is a software convention — it's enforced in hardware on every memory access

### Topic: Huge Pages — Hardware Support (huge-pages-hw-support, advanced)
Trading page granularity for TLB reach.
- **concept:** The TLB-reach problem — small pages mean a large working set can't fit in the TLB
- **concept:** Huge pages (2MB/1GB) — far fewer TLB entries needed, at coarser granularity
- **diagram:** The same memory region covered by many 4KB entries vs one 2MB entry
- **concept:** Hardware support for multiple simultaneous page sizes in one page table
- **compare:** Huge pages vs regular pages — TLB-pressure reduction vs internal fragmentation and allocation flexibility
- **pitfall:** Assuming huge pages always help — sparse or short-lived allocations can waste memory instead

---

## Group: Instruction-Level Parallelism (ilp)
*superscalar, OoO, branch prediction*

### Topic: ILP Fundamentals (ilp-fundamentals, advanced)
The dependence types that cap how much parallelism a program actually has.
- **concept:** Instruction-level parallelism — executing multiple instructions per cycle from one stream
- **concept:** True data dependence (RAW) — the fundamental limiter, worked around but never removed
- **concept:** Name dependences — WAR and WAW, artifacts of register reuse, not real dependencies
- **concept:** Control dependence — instructions whose execution depends on a branch outcome
- **diagram:** A dependence graph for a short instruction sequence, marking which pairs can run in parallel
- **compare:** Dependence types and which technique addresses each (forwarding, renaming, prediction)

### Topic: Superscalar Execution (superscalar-execution, advanced)
Issuing multiple instructions per cycle, and what limits how wide that can go.
- **concept:** Superscalar — fetching, decoding, and issuing multiple instructions per cycle
- **concept:** Issue width — how many instructions per cycle, and the diminishing returns of going wider
- **diagram:** A superscalar pipeline with duplicated fetch/decode/execute paths
- **concept:** Structural limits — duplicated functional units, register-file ports, issue-logic complexity
- **compare:** Scalar vs superscalar pipelines — throughput ceiling and the cost of reaching it
- **pitfall:** Assuming issue width alone determines performance — dependences and stalls leave slots empty

### Topic: Out-of-Order Execution (out-of-order-execution, advanced)
Dynamic scheduling and Tomasulo's algorithm as the mechanism that hides stalls.
- **concept:** The motivation — an in-order stall (e.g., a cache miss) blocks independent later instructions too
- **concept:** Dynamic scheduling — issuing instructions as operands become ready, not in program order
- **concept:** Reservation stations — buffering instructions until operands and functional units are ready
- **diagram:** Tomasulo's algorithm's data flow — reservation stations, common data bus, register status
- **concept:** The reorder buffer — restoring in-order appearance for commit despite out-of-order execution
- **compare:** In-order vs out-of-order — hardware complexity/power vs achieved ILP

### Topic: Register Renaming (register-renaming, advanced)
Eliminating false dependences so the hardware can reorder more aggressively.
- **concept:** Why WAR/WAW hazards block reordering even though they aren't true dependences
- **concept:** Register renaming — mapping architectural registers onto a larger pool of physical registers
- **diagram:** The same architectural register, reused by two instructions, renamed to two different physical registers
- **concept:** The physical register file and rename (map) table that make this possible
- **compare:** Renaming eliminates WAR/WAW but not RAW — what it does and doesn't solve
- **pitfall:** Confusing architectural register count (ISA-visible, cross-link: ISA → registers-and-register-files) with physical register count (microarchitecture-only)

### Topic: Branch Prediction (branch-prediction, advanced)
Why deep, wide pipelines demand highly accurate dynamic prediction.
- **concept:** Why prediction matters more as pipelines deepen and issue width grows
- **concept:** Static prediction recap and its ceiling (cross-link: Pipelining → control-hazards-and-branching)
- **concept:** Dynamic prediction — a branch-history table of 2-bit saturating counters per branch
- **diagram:** A 2-bit saturating counter's state transitions across a taken/not-taken sequence
- **concept:** Correlating/global predictors — using other branches' history, not just this branch's own
- **concept:** The branch target buffer (BTB) — predicting where a taken branch goes, not just whether
- **compare:** Local vs global vs hybrid (tournament) predictors — accuracy vs hardware cost
- **pitfall:** A well-predicted branch direction still costing performance if the BTB mispredicts the target

### Topic: Speculative Execution (speculative-execution, advanced)
Executing past uncertain points before they resolve, and what happens when the guess is wrong.
- **concept:** Speculation — executing past an uncertain point (branch, sometimes a load) before it resolves
- **concept:** What "committing" speculative results means — nothing is visible until confirmed correct
- **diagram:** A misprediction rolling back speculative state via the reorder buffer/checkpoint
- **concept:** Speculative load execution — predicting a store won't alias, and recovering if wrong
- **concept:** Why speculation pays off — most predictions are right, so most speculative work is useful
- **pitfall:** Speculative execution leaving observable side effects (cache state) even after rollback — the root of Spectre-class attacks (cross-link: Security → appsec, brief mention only)

### Topic: VLIW & Static ILP (vliw-and-static-ilp, advanced)
The compiler-scheduled alternative to dynamic out-of-order execution.
- **concept:** VLIW — bundling multiple operations into one long instruction word, scheduled by the compiler
- **concept:** Why VLIW moves the scheduling burden from hardware to the compiler
- **diagram:** A VLIW instruction bundle with independent slots for different functional units
- **compare:** VLIW vs superscalar/OoO — simpler hardware vs the compiler needing perfect static knowledge
- **concept:** Why VLIW struggles with unpredictable latencies (cache misses) that dynamic scheduling handles gracefully
- **pitfall:** Assuming VLIW failed outright — it thrives where timing is predictable (DSPs, some accelerators)

---

## Group: Multicore & Parallelism (multicore)
*SMP, consistency models, SIMD*

### Topic: Multicore Motivation & SMP (multicore-motivation-and-smp, intermediate)
Why the industry pivoted from faster single cores to more cores.
- **concept:** The power wall — why clock speeds stopped climbing around the mid-2000s
- **concept:** The shift to multicore — more cores instead of one faster core
- **concept:** Symmetric multiprocessing (SMP) — identical cores sharing memory, each able to run any task
- **diagram:** An SMP layout — multiple cores, private L1/L2, shared L3 and memory
- **concept:** Why software had to change — the free-lunch era ends, parallel programming becomes necessary
- **compare:** Multicore vs a hypothetical faster single core — power/heat vs software-complexity trade-off
- **pitfall:** Assuming more cores means proportionally faster programs — Amdahl's law and contention say otherwise (cross-link: perf-power → amdahls-law-fundamentals)

### Topic: Memory Consistency Models (memory-consistency-models, advanced)
Ordering guarantees across addresses — the model coherence alone doesn't give you.
- **concept:** Consistency vs coherence — coherence is per-address, consistency is about ordering across addresses (cross-link: caches → cache-coherence-protocols)
- **concept:** Sequential consistency — the intuitive model: one global interleaving matching program order
- **concept:** Why hardware relaxes consistency — buffering and reordering for performance
- **diagram:** A classic reordering example (two writes, two reads, two cores) that breaks under a relaxed model
- **concept:** Memory barriers/fences — the tool that forces ordering back where a programmer needs it
- **compare:** Strong (x86 TSO) vs weak/relaxed (ARM, RISC-V default) consistency models — programmer burden vs hardware freedom
- **pitfall:** Lock-free code that "works in testing" but breaks on a weaker memory model

### Topic: Synchronization Primitives in Hardware (synchronization-primitives-hw, advanced)
The atomic instructions that every lock and lock-free structure is built from.
- **concept:** Why ordinary loads/stores can't safely implement a lock — the read-modify-write race
- **concept:** Test-and-set — the earliest atomic primitive, and its busy-waiting cost
- **concept:** Compare-and-swap (CAS) — the workhorse atomic behind most modern lock-free code
- **concept:** Load-linked/store-conditional (LL/SC) — the alternative used by RISC-style ISAs
- **diagram:** A CAS-based spinlock's acquire/release sequence
- **code:** Implementing a simple spinlock using an atomic compare-and-swap
- **compare:** CAS vs LL/SC — how each does (or doesn't) sidestep the ABA problem

### Topic: Interconnects & Networks-on-Chip (interconnects-and-noc, advanced)
Why the on-chip communication fabric becomes the scaling bottleneck at high core counts.
- **concept:** Why the interconnect matters — cores are only as parallel as their ability to communicate
- **concept:** Shared bus — simplest, but a single point of contention that doesn't scale
- **concept:** Crossbar — any-to-any connectivity, better bandwidth, quadratic cost
- **concept:** Mesh / Network-on-Chip (NoC) — routing packets hop-by-hop between tiles, the scalable choice
- **diagram:** Bus vs crossbar vs mesh topology for 8 cores
- **compare:** Interconnect choice vs core count — why large core counts force a move to NoC

### Topic: SIMD & Vector Processing (simd-and-vector-processing, intermediate)
One instruction, many data elements — the ISA extensions and the code shapes that benefit.
- **concept:** SIMD — one instruction operating on multiple data elements at once
- **concept:** Vector registers — wide registers holding several packed values at once
- **diagram:** A SIMD add operating on 4 packed integers in one instruction vs 4 scalar instructions
- **concept:** Real ISA extensions — SSE/AVX (x86), NEON (ARM) — what they added and why
- **code:** A loop auto-vectorized by the compiler vs its scalar equivalent
- **compare:** SIMD vs scalar loops — throughput gain vs the data-layout/alignment requirements it demands
- **compare:** SIMD (lockstep lanes, one thread) vs SIMT (GPU, cross-link: gpus-accelerators) — related but distinct models
- **pitfall:** Branchy, data-dependent loops resisting vectorization — SIMD wants uniform control flow

### Topic: Parallel Scalability Limits (parallel-scalability-limits, advanced)
Applying Amdahl's Law to real multicore scaling, and the overheads the law itself ignores.
- **concept:** Applying Amdahl's Law to core count — diminishing returns as the serial fraction dominates (cross-link: perf-power → amdahls-law-fundamentals owns the law itself)
- **concept:** Synchronization overhead — locks and barriers eating into the theoretical speedup
- **concept:** Load imbalance — idle cores waiting on busy ones, capping real-world speedup
- **diagram:** A speedup-vs-core-count curve flattening out, annotated with where each overhead source bites
- **concept:** Gustafson's Law — the counterpoint: scale the problem size with the core count instead of holding it fixed
- **compare:** Amdahl's (fixed problem size) vs Gustafson's (scaled problem size) — when each framing is the right lens

---

## Group: GPUs & Accelerators (gpus-accelerators)
*SIMT, domain-specific arch*

### Topic: GPU Architecture Fundamentals (gpu-architecture-fundamentals, intermediate)
Why a GPU's die looks nothing like a CPU's, and what workloads that shape is built for.
- **concept:** CPU optimizes latency (one thing, fast); GPU optimizes throughput (many things, at once)
- **concept:** Why GPUs devote far more silicon to ALUs and far less to control logic/cache than CPUs
- **diagram:** A rough CPU-die vs GPU-die area breakdown (control/cache vs ALU area)
- **concept:** The workloads that fit — massively data-parallel, uniform-control-flow problems (graphics, ML)
- **compare:** CPU vs GPU — when a problem is "GPU-shaped" and when branchy/sequential work resists it
- **concept:** Clock speed and per-core complexity — why GPU cores run slower and simpler than CPU cores

### Topic: The SIMT Execution Model (simt-execution-model, advanced)
Warps, lockstep threads, and the divergence penalty unique to GPU execution.
- **concept:** SIMT (Single Instruction, Multiple Threads) — many threads executing the same instruction in lockstep
- **concept:** Warps/wavefronts — the actual hardware group of threads that moves together
- **diagram:** A warp of threads executing one instruction together across many ALU lanes
- **concept:** Branch divergence — when threads in a warp disagree on a branch, both paths execute, masked
- **compare:** SIMD (single thread, wide vector, cross-link: multicore → simd-and-vector-processing) vs SIMT (many threads, warp-scheduled)
- **pitfall:** Writing GPU kernels with heavy per-thread branching — divergence serializes what should be parallel

### Topic: GPU Memory Hierarchy (gpu-memory-hierarchy, advanced)
Global, shared, and per-thread memory, and the coalescing rule that governs bandwidth.
- **concept:** Global memory — large, high-latency, shared across every thread on the GPU
- **concept:** Shared memory — a fast, programmer-managed scratchpad local to a thread block
- **concept:** Registers and local memory — per-thread private storage
- **diagram:** The GPU memory hierarchy layered against the thread/block/grid execution hierarchy
- **concept:** Memory coalescing — adjacent threads accessing adjacent addresses collapse into one wide transaction
- **pitfall:** A strided or scattered access pattern turning one coalesced transaction into many, wrecking bandwidth

### Topic: GPU Programming Model Basics (gpu-programming-model-basics, intermediate)
The host/device split and the thread/block/grid hierarchy every GPU kernel is built on.
- **concept:** The host-device split — the CPU orchestrates, the GPU executes the parallel kernel
- **concept:** The kernel — the function that runs once per thread across a huge number of threads
- **concept:** The thread hierarchy — thread, block, grid — and why it's structured, not flat
- **diagram:** A grid of blocks of threads mapped onto physical SIMT execution units
- **code:** A minimal vector-add kernel sketch and how thread/block indices map to data elements
- **compare:** Data-parallel (map-style) GPU kernels vs general-purpose CPU code — what maps well and what doesn't

### Topic: Domain-Specific Accelerators (domain-specific-accelerators, intermediate)
Where the specialization spectrum goes past the GPU, and why.
- **concept:** The specialization spectrum — general-purpose CPU → programmable GPU → fixed-function ASIC
- **concept:** Why specialize at all — a fixed-function unit can be far more power/area-efficient for one job
- **concept:** TPUs and matrix-multiply accelerators — systolic arrays exploiting a fixed dataflow pattern
- **diagram:** The specialization spectrum from CPU to GPU to ASIC, flexibility vs efficiency as opposing axes
- **compare:** GPU vs TPU/ASIC for ML workloads — programmability vs raw efficiency at the one operation it's built for
- **pitfall:** Assuming an ASIC is "just a faster GPU" — it typically supports a much narrower set of operations

---

## Group: Storage & I/O Hardware (storage-hardware)
*disks/SSD/NVMe, buses, interrupts*

*Scope boundary: physical device and protocol mechanics only. OS-managed buffering/scheduling lives in Area 3 → `io-systems`; filesystem layout lives in Area 3 → `file-systems`.*

### Topic: HDD Mechanics & Performance (hdd-mechanics-and-performance, beginner)
The mechanical realities that put a hard floor under random-access latency.
- **concept:** The physical mechanism — spinning platters, a moving read/write head, tracks and sectors
- **concept:** Seek time — moving the head to the right track, the dominant cost for random access
- **concept:** Rotational latency — waiting for the right sector to spin under the head
- **diagram:** A disk platter with track/sector layout and the head arm sweeping across it
- **concept:** Sequential vs random access — why sequential throughput vastly outperforms random IOPS on HDDs
- **compare:** HDD vs SSD performance characteristics — the mechanical-latency wall HDDs can't cross

### Topic: SSD & Flash Internals (ssd-and-flash-internals, intermediate)
Why flash can't simply overwrite a page, and what that constraint does to write behavior.
- **concept:** NAND flash cells — storing bits as trapped electric charge, no moving parts
- **concept:** The page/block structure — reads and writes at page granularity, erases at block granularity
- **concept:** Why you can't overwrite a page in place — a page must be erased (at block level) before rewriting
- **diagram:** Pages grouped into a block, with the erase-before-rewrite constraint illustrated
- **concept:** Why SSDs are fast at random reads while writes are more involved than they look
- **compare:** SLC vs MLC vs TLC/QLC — bits per cell trading cost/density against endurance and speed

### Topic: SSD Controller Management (ssd-controller-management, advanced)
The flash translation layer, garbage collection, and wear leveling that hide flash's quirks.
- **concept:** The flash translation layer (FTL) — mapping logical addresses to physical cells, hiding erase-before-write
- **concept:** Write amplification — one logical write triggering extra physical writes/erases
- **concept:** Garbage collection — reclaiming blocks with stale pages by relocating live data
- **concept:** Wear leveling — spreading writes evenly since flash cells wear out after finite erase cycles
- **diagram:** Garbage collection relocating live pages out of a fragmented block before erasing it
- **concept:** TRIM — the OS telling the SSD which blocks are logically free, so GC doesn't preserve garbage
- **pitfall:** Ignoring write amplification when estimating SSD lifespan or write-heavy workload performance

### Topic: NVMe & Storage Protocols (nvme-and-storage-protocols, advanced)
Why NVMe replaced AHCI/SATA once the storage medium itself got fast.
- **concept:** Why SATA/AHCI became the bottleneck once storage (SSD) itself got fast enough
- **concept:** NVMe's core idea — talk to storage directly over PCIe, cutting protocol overhead
- **concept:** Massive parallel queueing — thousands of queues, each with thousands of commands, vs AHCI's single queue
- **diagram:** NVMe's multi-queue submission/completion model vs AHCI's single command queue
- **compare:** SATA/AHCI vs NVMe — queue depth and interrupt/protocol overhead differences
- **pitfall:** Treating NVMe as a connector standard — it's a protocol, and can run over PCIe or over a network (NVMe-oF)

### Topic: I/O Buses & Interfaces (io-buses-and-interfaces, intermediate)
The physical highways between the CPU and its peripherals, and their bandwidth ceilings.
- **concept:** The bus as the highway between CPU/memory and peripherals — bandwidth and topology matter
- **concept:** PCIe — point-to-point lanes, scalable bandwidth by lane count and generation
- **concept:** SATA and USB — typical use cases and bandwidth ceilings relative to PCIe
- **diagram:** A simplified system topology — CPU, memory controller, PCIe lanes fanning out to devices
- **compare:** PCIe generations (3/4/5) — bandwidth-per-lane doubling and what it unlocks for storage/GPUs
- **pitfall:** Bottlenecking a fast NVMe SSD by plugging it into a narrower or older-generation PCIe link

### Topic: DMA & Interrupt-Driven I/O (dma-and-interrupt-driven-io, intermediate)
Polling, interrupts, and DMA as three points on a CPU-involvement spectrum.
- **concept:** Polling — the CPU repeatedly checks device status, simple but wasteful
- **concept:** Interrupt-driven I/O — the device signals the CPU only when ready, freeing it meanwhile
- **concept:** DMA (Direct Memory Access) — a device transfers to/from memory without per-byte CPU involvement
- **diagram:** A DMA transfer sequence — CPU sets it up, the DMA controller moves data, an interrupt signals completion
- **compare:** Polling vs interrupts vs DMA — CPU cycles spent vs latency vs implementation complexity
- **pitfall:** Assuming interrupts always beat polling — very high-frequency I/O can make interrupt overhead worse than polling

---

## Group: Performance & Power (perf-power)
*Amdahl, roofline, power scaling*

### Topic: Amdahl's Law Fundamentals (amdahls-law-fundamentals, intermediate)
The canonical law bounding parallel speedup — its home topic within the area.
- **concept:** Amdahl's Law — overall speedup is capped by the fraction of work that can't be sped up
- **concept:** The formula — speedup = 1 / ((1-p) + p/s), and what each term means
- **diagram:** A speedup-vs-processor-count curve for several serial fractions, showing the ceiling
- **code:** Computing Amdahl speedup for a given serial fraction and improvement factor
- **concept:** The uncomfortable implication — even infinite parallel resources can't beat 1/(1-p)
- **compare:** Amdahl's Law vs Gustafson's Law — fixed workload vs scaled workload (cross-link: multicore → parallel-scalability-limits)
- **pitfall:** Applying the law with the wrong "p" — forgetting synchronization/communication overhead isn't part of the original serial fraction

### Topic: Performance Metrics & Benchmarking (performance-metrics-and-benchmarking, beginner)
Why clock speed alone never settles a performance comparison.
- **concept:** Why clock speed alone doesn't measure performance — CPI and instruction count matter equally
- **concept:** The performance equation — Time = Instructions × CPI × Clock period
- **concept:** MIPS and FLOPS — what they measure, and why they mislead across different ISAs/workloads
- **concept:** Benchmark suites (SPEC-style) — standardized workloads for fairer cross-system comparison
- **code:** Computing execution time from instruction count, CPI, and clock period for two candidate designs
- **pitfall:** Optimizing for a benchmark score instead of real workload performance ("benchmarketing")
- **pitfall:** Comparing two CPUs by clock speed alone across different microarchitectures or ISAs

### Topic: The Roofline Model (roofline-model, advanced)
Diagnosing whether a workload is compute-bound or memory-bound before you optimize it.
- **concept:** The roofline model's question — is this workload limited by compute or by memory bandwidth?
- **concept:** Arithmetic intensity — FLOPs performed per byte moved from memory
- **diagram:** A roofline plot — the compute ceiling (flat) and memory-bandwidth slope (diagonal) with a workload point placed
- **concept:** Reading the plot — points under the diagonal are memory-bound, points under the flat line are compute-bound
- **concept:** What each region implies for optimization — more compute doesn't help a memory-bound point, and vice versa
- **code:** Computing arithmetic intensity for a simple kernel (e.g., a dot product) and placing it on the roofline
- **compare:** Optimizing a memory-bound kernel (cache blocking, cross-link: caches → cache-conscious-programming) vs a compute-bound one (vectorization, cross-link: multicore → simd-and-vector-processing)

### Topic: Power & Energy Fundamentals (power-and-energy-fundamentals, intermediate)
Dynamic vs static power, and why voltage is the lever engineers reach for first.
- **concept:** Dynamic power — the switching-activity cost, proportional to C·V²·f
- **concept:** Static (leakage) power — drawn even without switching, growing as transistors shrink
- **concept:** Why voltage matters quadratically — the single biggest lever for power reduction
- **diagram:** A rough dynamic-vs-static power breakdown across process generations
- **concept:** Energy vs power — instantaneous draw vs power integrated over time
- **compare:** Reducing frequency vs voltage vs switched capacitance — which lever costs least performance per watt saved

### Topic: Power-Performance Scaling (power-performance-scaling, advanced)
Why Dennard scaling broke down, and how DVFS manages the power budget that resulted.
- **concept:** Dennard scaling — the historical assumption that smaller transistors stay equally power-dense at higher frequency
- **concept:** Why Dennard scaling broke down (roughly mid-2000s) — leakage current stopped shrinking with voltage
- **diagram:** A timeline of clock speed, power, and core count showing the post-Dennard inflection point
- **concept:** The consequence — the industry pivoted to multicore instead of ever-faster single cores (cross-link: multicore → multicore-motivation-and-smp)
- **concept:** Dynamic voltage and frequency scaling (DVFS) — trading performance for power at runtime based on load
- **compare:** "Race to idle" vs sustained lower-power operation — two DVFS strategies and when each wins
- **pitfall:** Assuming you can always clock higher for more performance — thermal/power limits and turbo-boost duration say otherwise

---

## Cross-links (noted, not duplicated)

- **`hw-virtual-memory`** (this area, mechanism) ↔ **OS Area 3 `virtual-memory`** (policy: replacement, thrashing). Kept strictly separated by scope.
- **`storage-hardware`** (this area, device/protocol physics) ↔ **OS Area 3 `io-systems`** (buffering/scheduling) and **`file-systems`** (on-disk layout).
- **`caches`** (this area, hardware L1/L2/L3, coherence) ↔ **System Design Area 7 `caching`** (application/distributed cache patterns — different layer entirely).
- **`cache-coherence-protocols`** (per-address consistency) ↔ **`memory-consistency-models`** in `multicore` (cross-address ordering) — commonly conflated, kept as two topics.
- **`amdahls-law-fundamentals`** (perf-power, owns the law) ↔ **`parallel-scalability-limits`** (multicore, applies it plus real-world overheads).
- **Branch prediction basics** in `pipelining` → **`branch-prediction`** in `ilp` owns the full dynamic-predictor deep dive.
- **`simd-and-vector-processing`** (multicore, lockstep vector lanes) ↔ **`simt-execution-model`** (gpus-accelerators, warp-scheduled threads) — related but distinct execution models, cross-linked rather than merged.
- **`speculative-execution`** (ilp) mentions Spectre/Meltdown only briefly — the security deep dive belongs to Area 13 `appsec`.
- **`calling-conventions-stack-frames`** (isa) flags stack-overflow exploitation briefly — owned in depth by Area 13 `appsec`.
- No internal overlaps found among the area's own 12 groups; each topic list above was checked against sibling groups for duplication before finalizing.
