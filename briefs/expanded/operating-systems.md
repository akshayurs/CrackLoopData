# Area: Operating Systems (operating-systems)

Reference outline — 2 levels below each group (Topics, then Slide headings). Human review/approval gate before authoring.

---

## Group: OS Fundamentals (os-fundamentals)
*kernel, syscalls, user/kernel mode — the OS's basic contract with hardware and applications*

### Topic: What Is an Operating System (what-is-an-operating-system, beginner)
Scope: the OS's two jobs — resource manager and abstraction layer — and the vocabulary interviewers expect you to untangle.
- Why every computer needs an OS (concept)
- The two jobs of an OS: resource manager + abstraction layer (concept)
- Multiprogramming, multitasking, timesharing — untangling the terms (concept)
- Types of OS: batch, timesharing, real-time, distributed, embedded (compare)
- Diagram: where the OS sits — hardware, kernel, system programs, applications (diagram)
- Hard real-time vs soft real-time, briefly (concept)
- Pitfall: "OS" is not just "the kernel" (pitfall)
- Interview: "Explain what an operating system does, in one sentence" (interview)

### Topic: User Mode vs Kernel Mode (user-mode-vs-kernel-mode, beginner)
Scope: how hardware enforces privilege separation and why user code can't touch hardware directly.
- The mode bit: how hardware enforces two privilege levels (concept)
- What kernel mode can do that user mode can't (concept)
- x86 protection rings 0–3 (diagram)
- How a user process asks the kernel for help: the trap mechanism (concept)
- Diagram: user mode / kernel mode transition on a syscall (diagram)
- Why not just run everything in kernel mode? (concept)
- Kernel panics vs user process crashes (compare)
- Pitfall: treating a mode switch as free (pitfall)
- Interview: "What happens when a user program executes a privileged instruction?" (interview)

### Topic: System Calls (system-calls, beginner)
Scope: the syscall interface end to end — what it is, how it differs from a library call, and the mechanism from call to return.
- What is a system call? (concept)
- System call vs library call vs API — the layering (compare)
- Categories of syscalls: process, file, device, information, communication (concept)
- Diagram: anatomy of a syscall — application to kernel and back (diagram)
- The syscall table and syscall numbers (concept)
- Code: tracing a syscall with strace on a simple program (code)
- Common syscalls to know: fork, exec, wait, read, write, open, close, mmap (concept)
- Pitfall: confusing signals with syscalls (pitfall)
- Interview: "What happens between calling read() in C and getting your data?" (interview)

### Topic: Interrupts, Traps & Exceptions (interrupts-traps-exceptions, intermediate)
Scope: the general interrupt/trap/exception mechanism that gets control into the kernel (device-specific I/O handling lives in I/O & Device Management).
- Interrupts vs traps vs exceptions — the three ways control reaches the kernel (compare)
- Hardware interrupts: how a device gets the CPU's attention (concept)
- Interrupt Service Routines (ISR) and the interrupt vector table (concept)
- Diagram: interrupt handling timeline — device signal → CPU → ISR → resume (diagram)
- Maskable vs non-maskable interrupts (concept)
- Interrupt priority and nested interrupts (concept)
- Polling vs interrupts — why interrupts usually win (compare)
- Pitfall: doing too much work inside an ISR — top half vs bottom half (pitfall)
- Interview: "Walk me through what happens when you press a key on the keyboard" (interview)

### Topic: OS Structures & Kernel Design (os-structures-kernel-design, intermediate)
Scope: how a kernel is architected — monolithic, microkernel, hybrid — and the trade-offs each makes.
- Monolithic kernels: everything in kernel space (concept)
- Microkernels: minimal kernel, services in user space (concept)
- Diagram: monolithic vs microkernel message-passing architecture (diagram)
- Hybrid kernels: Windows NT, XNU — splitting the difference (concept)
- Performance vs isolation trade-off (compare)
- Loadable kernel modules — monolithic flexibility without a rebuild (concept)
- Exokernels and unikernels — the extremes (concept)
- Pitfall: assuming microkernels are always slower (pitfall)
- Interview: "Why is Linux monolithic and Minix a microkernel — what's the trade-off?" (interview)

### Topic: System Boot Process (system-boot-process, intermediate)
Scope: the full chain from power-on to a running shell, and where boot failures typically occur.
- The boot sequence overview: firmware → bootloader → kernel → init (concept)
- BIOS vs UEFI (compare)
- POST and hardware initialization (concept)
- Bootloaders: GRUB and the boot chain (concept)
- Diagram: full boot timeline from power button to shell prompt (diagram)
- Kernel initialization: mounting root filesystem, starting init (concept)
- init systems: SysV init vs systemd (compare) — depth on systemd continues in Linux/Unix Internals
- Pitfall: confusing bootloader failure vs kernel panic vs init failure when diagnosing (pitfall)
- Interview: "What happens between pressing the power button and seeing your desktop?" (interview)

---

## Group: Processes & Threads (processes-threads)
*PCB, context switch, IPC — the unit of execution and how units talk to each other*

### Topic: What Is a Process (what-is-a-process, beginner)
Scope: the process abstraction — program vs process, and what's inside a process's address space.
- Program vs process — code at rest vs code in execution (concept)
- What's inside a process: address space, registers, open files (concept)
- Diagram: a process's memory layout — text, data, heap, stack (diagram)
- The stack and heap within a process (concept)
- Process identifiers: PID, PPID (concept)
- Single-threaded vs multi-threaded processes, briefly (concept)
- Pitfall: assuming two processes share memory by default (pitfall)
- Interview: "What's the difference between a program and a process?" (interview)

### Topic: Process Control Block & States (process-control-block-and-states, beginner)
Scope: what the OS tracks per process and the state machine every process moves through.
- The Process Control Block: what the OS tracks per process (concept)
- The process state diagram: new, ready, running, waiting, terminated (concept)
- Diagram: state transition diagram with triggers for each arrow (diagram)
- Ready queue vs waiting/blocked queue (concept)
- Suspended states: ready-suspended, blocked-suspended (concept)
- What triggers each state transition (concept)
- Pitfall: confusing "blocked" with "terminated" (pitfall)
- Interview: "A process is stuck — how do you tell if it's blocked, running, or dead?" (interview)

### Topic: Process Lifecycle — fork/exec/wait (process-lifecycle-fork-exec, intermediate)
Scope: process creation and termination mechanics — fork/exec/wait/exit, zombies, orphans, copy-on-write.
- Creating a process: fork() semantics (concept)
- Code: fork() example and what prints where (code)
- exec() family: replacing a process image (concept)
- The fork+exec pattern — why Unix splits creation from loading (concept)
- wait() and exit() — how a parent reaps a child (concept)
- Diagram: parent-child timeline across fork/exec/wait/exit (diagram)
- Zombie processes: what they are and why they linger (concept)
- Orphan processes and reparenting to init/systemd (concept)
- Copy-on-write fork — how modern OSes make fork cheap (concept; cross-link: Demand Paging in Virtual Memory & Paging)
- Pitfall: forgetting to reap children → zombie accumulation (pitfall)
- Interview: "What does fork() return, and how do you use it?" (interview)

### Topic: Threads & Multithreading (threads-and-multithreading, beginner)
Scope: what a thread is, what it shares with its process, and when threads beat processes.
- What is a thread? Execution within a process (concept)
- What threads share vs what's private to each thread (concept)
- Diagram: single-threaded vs multi-threaded process memory layout (diagram)
- Why use threads: concurrency, responsiveness, cheaper than processes (concept)
- Processes vs threads — the trade-off table (compare)
- Thread creation cost vs process creation cost (concept)
- Pitfall: assuming threads are "free" — shared-state bugs are the price (pitfall)
- Interview: "When would you choose multiple threads over multiple processes?" (interview)

### Topic: Thread Implementation Models (thread-implementation-models, intermediate)
Scope: how threads map onto kernel-schedulable entities — user-level, kernel-level, and hybrid models.
- User-level threads: managed entirely in userspace (concept)
- Kernel-level threads: the OS schedules each one (concept)
- Many-to-one model and its blocking problem (concept)
- One-to-one model — what Linux/Windows actually use (concept)
- Many-to-many and two-level models (concept)
- Diagram: the three threading models side by side (diagram)
- Green threads / userland schedulers as a modern many-to-one variant (concept)
- Compare: user-level vs kernel-level — cost, blocking behavior, scheduler control (compare)
- Interview: "Why can one blocking syscall stall all threads in a many-to-one model?" (interview)

### Topic: Context Switching (context-switching, intermediate)
Scope: what a context switch actually does and why it costs what it costs.
- What a context switch saves and restores (concept)
- Diagram: context switch timeline between two processes (diagram)
- Process context switch vs thread context switch — why threads are cheaper (compare)
- What triggers a context switch: interrupt, syscall, time-slice expiry (concept)
- The hidden costs: cache/TLB flush and cold-cache effects (concept)
- Why context-switch overhead shapes scheduler design (concept)
- Pitfall: treating context-switch cost as negligible at high thread counts (pitfall)
- Interview: "Why is switching between threads of the same process cheaper than between processes?" (interview)

### Topic: Inter-Process Communication (inter-process-communication, intermediate)
Scope: the mechanisms processes use to exchange data across isolated address spaces.
- Why processes need IPC — isolated address spaces by default (concept)
- Pipes and named pipes (FIFOs) (concept)
- Code: a simple pipe between parent and child (code)
- Message queues (concept)
- Shared memory — the fastest IPC (concept)
- Diagram: shared memory vs message-passing data paths (diagram)
- Sockets as IPC (local + network) (concept)
- Signals as a lightweight notification mechanism (concept)
- Compare: pipes vs shared memory vs message queues vs sockets — when to use which (compare)
- Pitfall: shared memory needs its own synchronization — the OS doesn't serialize it for you (pitfall; cross-link: Concurrency & Synchronization)
- Interview: "How would two unrelated processes exchange a large amount of data fast?" (interview)

---

## Group: CPU Scheduling (scheduling)
*FCFS/RR/priority/MLFQ, metrics — deciding who runs next*

### Topic: Scheduling Fundamentals (scheduling-fundamentals, beginner)
Scope: why a scheduler exists and the metrics used to judge any scheduling algorithm.
- Why the CPU needs a scheduler (concept)
- Preemptive vs non-preemptive scheduling (concept)
- The dispatcher and dispatch latency (concept)
- Scheduling criteria: utilization, throughput, turnaround, waiting, response time (concept)
- Diagram: Gantt-chart timeline showing these metrics (diagram)
- Turnaround time vs response time — optimizing for different users (compare)
- Pitfall: optimizing average turnaround while starving individual jobs (pitfall)
- Interview: "What metrics would you use to compare two scheduling algorithms?" (interview)

### Topic: FCFS & Shortest Job First (fcfs-and-sjf, beginner)
Scope: the two simplest schedulers, the convoy effect, and why SJF is optimal but impractical as-is.
- First-Come-First-Served: the simplest scheduler (concept)
- Code: FCFS Gantt chart and average wait time (code)
- The convoy effect — short jobs stuck behind long ones (concept)
- Shortest Job First: minimizing average waiting time (concept)
- Why SJF is provably optimal for average wait time (concept)
- The catch: SJF needs to predict burst time (concept)
- Preemptive SJF = Shortest Remaining Time First (SRTF) (concept)
- Code: SRTF Gantt chart with a shorter job arriving mid-execution (code)
- Pitfall: starvation of long jobs under SJF/SRTF (pitfall)
- Interview: "Why isn't Shortest Job First used as-is in real operating systems?" (interview)

### Topic: Round Robin & Priority Scheduling (round-robin-and-priority-scheduling, intermediate)
Scope: time-sliced fairness, quantum sizing, priority scheduling, and the starvation/aging fix.
- Round Robin: time-sliced fairness (concept)
- Choosing the time quantum — too small vs too large (concept)
- Code: RR Gantt chart and average waiting time (code)
- Diagram: quantum size vs context-switch overhead vs responsiveness (diagram)
- Priority scheduling: running the "most important" job first (concept)
- Static vs dynamic priority (concept)
- Starvation in priority scheduling (concept)
- Aging — the fix for starvation (concept)
- Compare: Round Robin vs Priority — fairness vs importance (compare)
- Pitfall: a too-small quantum turning RR into overhead-dominated thrashing (pitfall)
- Interview: "How would you prevent a low-priority process from starving forever?" (interview)

### Topic: Multilevel Queue & MLFQ (multilevel-queue-and-mlfq, advanced)
Scope: partitioning processes into queues and letting a feedback queue infer job behavior without knowing burst times.
- Multilevel queue scheduling: partitioning processes by type (concept)
- Limits of a static multilevel queue (concept)
- Multilevel Feedback Queue: letting processes move between queues (concept)
- Diagram: MLFQ queue structure with priority levels and quantum sizes (diagram)
- The core MLFQ rules: demote CPU-bound, promote I/O-bound behavior (concept)
- How MLFQ approximates SJF without knowing burst times in advance (concept)
- Preventing starvation/gaming: periodic priority boost (concept)
- Pitfall: a process gaming the scheduler by yielding just before quantum expiry (pitfall)
- Interview: "Design a scheduler that favors interactive jobs without starving batch jobs" (interview)

### Topic: Real-Time Scheduling (real-time-scheduling, advanced)
Scope: scheduling for deadlines, not just fairness — Rate Monotonic and Earliest Deadline First.
- Real-time scheduling goals: meeting deadlines, not just fairness (concept)
- Hard real-time vs soft real-time systems (compare)
- Rate Monotonic Scheduling: fixed priority by period (concept)
- Earliest Deadline First: dynamic priority by deadline (concept)
- Diagram: RM vs EDF schedule for the same task set (diagram)
- Schedulability tests — can this task set meet its deadlines? (concept)
- Pitfall: assuming a general-purpose scheduler can give real-time guarantees (pitfall)
- Interview: "Why can't you just use Linux's default scheduler for a pacemaker?" (interview)

### Topic: Scheduling in Practice — Linux CFS (scheduling-in-practice, intermediate)
Scope: a production scheduler case study, contrasted with the textbook algorithms above.
- Why Linux moved to a Completely Fair Scheduler (concept)
- The core CFS idea: virtual runtime and the red-black tree (concept)
- Diagram: CFS picking the leftmost (least vruntime) task (diagram)
- Nice values and weighted fairness in CFS (concept)
- How CFS handles I/O-bound vs CPU-bound processes without explicit queues (concept)
- Compare: CFS's approach vs textbook MLFQ (compare)
- Pitfall: assuming "nice -20" guarantees real-time-like behavior (pitfall)
- Interview: "How does Linux decide which process to run next?" (interview)

---

## Group: Concurrency & Synchronization (concurrency-sync)
*races, mutex/semaphore, monitors — coordinating shared state safely*

### Topic: Race Conditions & Critical Sections (race-conditions-and-critical-sections, beginner)
Scope: what a race condition is and the formal critical-section problem it motivates.
- What is a race condition? A concrete counter example (concept)
- Code: two threads incrementing a shared counter — the wrong answer (code)
- Why "i++" isn't atomic — the three hidden steps (concept)
- The critical section problem, formally (concept)
- Diagram: entry section / critical section / exit section (diagram)
- The three requirements: mutual exclusion, progress, bounded waiting (concept)
- Data race vs race condition — are they the same thing? (compare)
- Pitfall: races that only show up under load/interleaving (pitfall)
- Interview: "Two threads each increment a shared counter 1M times — why isn't the result 2M?" (interview)

### Topic: Locks & Mutexes (locks-and-mutexes, beginner)
Scope: how a mutex provides mutual exclusion, and the spinlock vs blocking-lock trade-off.
- What a mutex actually is: lock/unlock and ownership (concept)
- Code: fixing the counter race with a mutex (code)
- Spinlocks: busy-waiting for a lock (concept)
- Blocking locks: sleeping instead of spinning (concept)
- Compare: spinlock vs blocking mutex — when each wins (compare)
- Reentrant (recursive) locks (concept)
- Reader-writer locks as a refinement (concept)
- Pitfall: holding a lock across a blocking call (pitfall)
- Interview: "When would you choose a spinlock over a regular mutex?" (interview)

### Topic: Semaphores (semaphores, intermediate)
Scope: the counting-semaphore abstraction and how it differs from a mutex.
- The semaphore abstraction: a counter with atomic wait/signal (concept)
- Binary semaphore vs mutex — the subtle difference (compare)
- Counting semaphores for resource pools (concept)
- Code: bounded-buffer producer-consumer with semaphores (code)
- Diagram: semaphore value over time as producers/consumers run (diagram)
- Using semaphores for signaling/ordering, not just exclusion (concept)
- Pitfall: semaphores have no ownership — anyone can signal (pitfall)
- Interview: "What's the actual difference between a mutex and a binary semaphore?" (interview)

### Topic: Monitors & Condition Variables (monitors-and-condition-variables, intermediate)
Scope: bundling a lock with its data, and waiting on a condition rather than just a lock.
- The monitor: bundling a lock with the data it protects (concept)
- Why raw semaphores get error-prone at scale (concept)
- Condition variables: waiting for a condition, not just a lock (concept)
- wait(), signal(), broadcast() semantics (concept)
- Code: producer-consumer with a mutex + condition variable (code)
- Diagram: thread states around a condition variable wait queue (diagram)
- Why you re-check the condition in a while-loop, not an if — spurious wakeups (concept)
- Hoare vs Mesa monitor semantics (compare)
- Pitfall: signaling before the waiter checks — a lost wakeup (pitfall)
- Interview: "Why wrap wait() in a while loop instead of an if?" (interview)

### Topic: Classic Synchronization Problems (classic-synchronization-problems, advanced)
Scope: producer-consumer, readers-writers, and dining philosophers as the standard worked case studies.
- Why these three problems are the standard interview vocabulary (concept)
- Producer-consumer / bounded buffer — full solution recap (concept)
- Readers-writers problem: the requirement (concept)
- First readers-writers solution and writer starvation (concept)
- Fixing writer starvation — the second readers-writers problem (concept)
- Dining philosophers: the setup and the deadlock risk (concept)
- Diagram: dining philosophers table with forks (diagram)
- Breaking the symmetry: resource ordering, arbitrator, odd/even solutions (concept)
- Compare: what each classic problem teaches (compare)
- Interview: "How do you stop the dining philosophers from deadlocking?" (interview)

### Topic: Lock-Free Programming & Atomics (lock-free-programming-and-atomics, advanced)
Scope: atomic operations and compare-and-swap as an alternative to locking, and their real costs.
- Why go lock-free — contention and priority-inversion costs of locks (concept)
- Atomic operations: what the hardware actually guarantees (concept)
- Compare-and-swap (CAS): the building block (concept)
- Code: a lock-free counter with CAS (code)
- The ABA problem (concept)
- Diagram: CAS retry loop for a lock-free stack push (diagram)
- Memory ordering — why atomics alone aren't always enough (concept)
- Compare: lock-based vs lock-free — throughput, complexity, correctness risk (compare)
- Pitfall: assuming lock-free means simpler (it's usually harder to get right) (pitfall)
- Interview: "What is the ABA problem and how do you avoid it?" (interview)

### Topic: Concurrency Hazards — Livelock & Starvation (concurrency-hazards-races-livelock-starvation, intermediate)
Scope: the hazard family beyond simple races — livelock, starvation, priority inversion. (Deadlock gets full treatment in the Deadlocks group.)
- The concurrency hazard family: race, deadlock, livelock, starvation (concept)
- Livelock: busy but making no progress (concept)
- Diagram: two threads politely "after you" — livelock illustrated (diagram)
- Starvation: always losing the race for a resource (concept)
- Priority inversion: a low-priority task blocking a high-priority one (concept)
- The Mars Pathfinder priority-inversion story as a worked example (concept)
- Priority inheritance as the fix (concept)
- Compare: race vs deadlock vs livelock vs starvation — telling them apart (compare)
- Interview: "What's the difference between deadlock and livelock?" (interview)

---

## Group: Deadlocks (deadlocks)
*conditions, prevention/avoidance/detection — when coordination itself gets stuck*

### Topic: Deadlock Fundamentals (deadlock-fundamentals, intermediate)
Scope: the definition of deadlock, the four necessary conditions, and modeling it with a resource allocation graph.
- What deadlock is: a cycle of waiting (concept)
- The four necessary (Coffman) conditions (concept)
- Code: two threads, two locks, opposite acquisition order (code)
- Resource Allocation Graphs: modeling who-holds-what/who-waits-for-what (concept)
- Diagram: a resource allocation graph showing a cycle (diagram)
- Cycle in the graph — necessary but not always sufficient with multi-instance resources (concept)
- Compare: deadlock vs starvation vs livelock, recap (compare)
- Pitfall: assuming any lock-ordering violation immediately deadlocks (pitfall)
- Interview: "What are the four necessary conditions for deadlock?" (interview)

### Topic: Deadlock Prevention (deadlock-prevention, intermediate)
Scope: structurally guaranteeing one of the four conditions can never hold.
- The prevention strategy: guarantee one condition can never hold (concept)
- Attacking mutual exclusion — not always possible (concept)
- Attacking hold-and-wait — acquire upfront or release before requesting (concept)
- Attacking no-preemption — forcibly taking resources back (concept)
- Attacking circular wait — global lock ordering (concept)
- Code: fixing the two-lock deadlock with consistent ordering (code)
- Diagram: lock ordering as a DAG that prevents cycles (diagram)
- Compare: cost/practicality of attacking each of the four conditions (compare)
- Pitfall: partial lock ordering — one code path forgets the convention (pitfall)
- Interview: "How do you fix a deadlock from two threads locking two mutexes in opposite order?" (interview)

### Topic: Deadlock Avoidance & Banker's Algorithm (deadlock-avoidance-bankers-algorithm, advanced)
Scope: using advance knowledge of maximum resource claims to stay in a safe state.
- Avoidance vs prevention — using future knowledge vs structural rules (concept)
- Safe state vs unsafe state (concept)
- The Banker's Algorithm setup: max, allocation, need matrices (concept)
- Diagram: matrices for a worked Banker's Algorithm example (diagram)
- The safety algorithm: finding a safe sequence (concept)
- Code: checking whether a request can be safely granted (code)
- Why avoidance needs advance knowledge of max resource claims (concept)
- Compare: avoidance vs prevention — flexibility vs practicality (compare)
- Pitfall: assuming an unsafe state means immediate deadlock (pitfall)
- Interview: "Walk me through the Banker's Algorithm on a small example" (interview)

### Topic: Deadlock Detection & Recovery (deadlock-detection-and-recovery, advanced)
Scope: letting deadlock happen and reacting — detection algorithm and recovery strategies.
- Why some systems allow deadlock and detect it instead of avoiding it (concept)
- The detection algorithm: reducing the resource allocation graph (concept)
- Diagram: wait-for graph and detecting a cycle (diagram)
- When to run detection — the frequency trade-off (concept)
- Recovery by process termination: one victim vs all (concept)
- Recovery by resource preemption: rollback and victim selection (concept)
- The starvation risk of always picking the same victim (concept)
- Compare: detection+recovery vs avoidance vs prevention — which real systems use which (compare)
- Interview: "Your database detects a deadlock between two transactions — what happens next?" (interview; cross-link: Databases area, Transactions & Concurrency)

---

## Group: Memory Management (memory-management)
*allocation, fragmentation, segmentation — giving processes memory before paging enters the picture*

### Topic: Address Binding & Address Spaces (address-binding-and-address-spaces, beginner)
Scope: logical vs physical addresses and when/how binding happens, before paging is introduced.
- Logical (virtual) address vs physical address (concept)
- Why programs don't use physical addresses directly (concept)
- Address binding: compile time, load time, execution time (concept)
- The MMU: translating logical to physical at runtime (concept)
- Diagram: MMU translation with base and limit registers (diagram)
- Base and limit registers — the simplest relocation + protection scheme (concept)
- Pitfall: confusing "address binding" with "paging" (binding is the general concept) (pitfall)
- Interview: "Why can two different processes both think their code starts at 0x400000?" (interview)

### Topic: Contiguous Memory Allocation (contiguous-memory-allocation, beginner)
Scope: giving each process one unbroken chunk of memory, and the classic placement algorithms.
- Contiguous allocation: one unbroken chunk per process (concept)
- Fixed partitioning and its limits (concept)
- Variable (dynamic) partitioning (concept)
- First-fit, best-fit, worst-fit allocation strategies (concept)
- Code: allocating requests to free blocks under each strategy (code)
- Diagram: memory map of free/allocated blocks over time (diagram)
- Compare: first-fit vs best-fit vs worst-fit — speed vs fragmentation (compare)
- Pitfall: assuming best-fit minimizes wasted space overall (pitfall)
- Interview: "Why doesn't best-fit actually give the best memory utilization in practice?" (interview)

### Topic: Fragmentation (fragmentation, intermediate)
Scope: internal vs external fragmentation, why it worsens over time, and compaction as a fix.
- Internal fragmentation: wasted space inside an allocated block (concept)
- External fragmentation: wasted space between allocated blocks (concept)
- Diagram: internal vs external fragmentation side by side (diagram)
- Why external fragmentation gets worse over time (the 50% rule) (concept)
- Compaction: defragmenting by relocating processes (concept)
- Why paging was invented partly to kill external fragmentation (concept; cross-link: Virtual Memory & Paging)
- Compare: fixed-size allocation vs variable-size allocation — which fragmentation type each trades for (compare)
- Interview: "Why does paging eliminate external fragmentation but not internal?" (interview)

### Topic: Segmentation (segmentation, intermediate)
Scope: memory divided by logical meaning rather than fixed size, and how it compares to paging.
- Segmentation: memory divided by logical meaning, not fixed size (concept)
- Segments: code, data, stack, heap as separate units (concept)
- The segment table: base + limit per segment (concept)
- Diagram: logical address (segment, offset) to physical translation (diagram)
- Protection and sharing benefits of segmentation (concept)
- External fragmentation returns with pure segmentation (concept)
- Segmentation with paging (combining both) (concept)
- Compare: segmentation vs paging — logical vs physical view of memory (compare)
- Interview: "What's the practical difference between segmentation and paging?" (interview)

### Topic: Swapping (swapping, intermediate)
Scope: moving whole processes between memory and disk — distinct from page-level swapping detail in Virtual Memory.
- Swapping: moving an entire process between memory and disk (concept)
- Why swapping exists: overcommitting memory across processes (concept)
- Diagram: a process swapped out to backing store and back (diagram)
- Swap space vs regular file storage (concept)
- The cost of swapping — why it's slow (concept)
- Swapping vs paging-based demand paging, briefly (compare; cross-link: Virtual Memory & Paging)
- Pitfall: confusing "swap usage" with "thrashing" (full detail in Virtual Memory & Paging) (pitfall)
- Interview: "Your server's swap usage is climbing — what does that tell you?" (interview)

### Topic: Dynamic Memory Allocation — the Heap (dynamic-memory-allocation-heap, advanced)
Scope: how malloc/free work under the hood — allocator algorithms and the bugs they enable.
- What malloc() actually does: OS memory vs the allocator's job (concept)
- brk/sbrk and mmap — how allocators get memory from the OS (concept)
- Free list management: tracking available chunks (concept)
- Diagram: a heap with allocated/free chunks and a free list (diagram)
- Allocation strategies inside allocators: first-fit, segregated free lists, buddy system (concept)
- The buddy allocation algorithm (concept)
- Code: a minimal free-list allocator sketch (code)
- Fragmentation inside the heap and why allocators coalesce free blocks (concept)
- Common heap bugs: use-after-free, double-free, heap overflow (concept)
- Pitfall: memory leaks are a lost pointer, not "the OS forgetting" (pitfall)
- Interview: "How does malloc decide where to get memory, and what happens on free()?" (interview)

---

## Group: Virtual Memory & Paging (virtual-memory)
*page tables, TLB, replacement, thrashing — the illusion of more memory than exists*

### Topic: Paging Fundamentals (paging-fundamentals, intermediate)
Scope: pages/frames and basic address translation via a single-level page table.
- Paging: fixed-size chunks solving external fragmentation (concept)
- Pages vs frames (concept)
- The page table: mapping virtual pages to physical frames (concept)
- Diagram: virtual address split into page number + offset, translated via page table (diagram)
- Code: translating a virtual address by hand (code)
- Why paging keeps internal fragmentation but kills external (concept)
- The page table size problem — why a flat table doesn't scale (concept)
- Pitfall: assuming contiguous virtual addresses are physically contiguous (pitfall)
- Interview: "How does the OS translate a virtual address to a physical one, at a high level?" (interview)

### Topic: Page Table Structures (page-table-structures, advanced)
Scope: how real systems keep page tables small and fast — multi-level and inverted designs.
- The problem: a flat page table for a 64-bit address space is absurd (concept)
- Multi-level (hierarchical) page tables (concept)
- Diagram: a 2-level page table walk (diagram)
- Why multi-level tables save space (concept)
- The translation cost: multiple memory accesses per lookup (concept)
- Inverted page tables: one entry per physical frame (concept)
- Compare: hierarchical vs inverted page tables — space vs lookup complexity (compare)
- Hashed page tables as another alternative (concept)
- Interview: "Why not just use one giant page table per process?" (interview)

### Topic: TLB & Translation Caching (tlb-and-translation-caching, advanced)
Scope: caching address translations, and the performance implications of misses and flushes.
- The TLB: caching recent virtual-to-physical translations (concept)
- Diagram: address translation with a TLB hit vs a TLB miss (diagram)
- TLB hit ratio and why it dominates memory access performance (concept)
- What happens on a TLB miss: hardware-walked vs software-walked page tables (concept)
- TLB flushes on context switch — the cost (concept)
- Address Space IDs (ASID) — avoiding full flushes (concept)
- Compare: TLB miss cost vs cache miss cost (compare)
- Pitfall: frequent context switches quietly degrading performance via TLB churn (pitfall)
- Interview: "Why might a context switch hurt performance even after the switch itself is done?" (interview)

### Topic: Demand Paging (demand-paging, intermediate)
Scope: lazily loading pages on first touch, and the mechanics of a page fault.
- Demand paging: loading pages only when touched (concept)
- The valid/invalid bit in a page table entry (concept)
- Page fault: what happens on a first touch (concept)
- Diagram: full page-fault handling sequence, step by step (diagram)
- Effective access time with page faults — the math (concept)
- Code: computing effective access time given a fault rate (code)
- Copy-on-write as an application of demand paging (concept; cross-link: Process Lifecycle fork/exec)
- Pitfall: a high page-fault rate silently tanking performance (pitfall)
- Interview: "What actually happens, hardware and OS, in the moment a page fault occurs?" (interview)

### Topic: Page Replacement Algorithms (page-replacement-algorithms, advanced)
Scope: choosing which page to evict when memory is full — FIFO, optimal, LRU, and cheap approximations.
- Why we need page replacement — memory is smaller than all pages in use (concept)
- FIFO replacement (concept)
- Code: FIFO on a reference string (code)
- Belady's Anomaly — more frames, more faults? (concept)
- Optimal (OPT/MIN) replacement — the theoretical best (concept)
- Least Recently Used (LRU) — approximating optimal with history (concept)
- Diagram: LRU stack update across a reference string (diagram)
- Implementing LRU cheaply: the clock (second-chance) algorithm (concept)
- Code: clock algorithm walkthrough (code)
- Compare: FIFO vs LRU vs Clock — accuracy vs implementation cost (compare)
- Interview: "Why is true LRU rarely implemented exactly, and what do real OSes use instead?" (interview)

### Topic: Thrashing & Working Set (thrashing-and-working-set, advanced)
Scope: why systems collapse under over-multiprogramming and how to detect/control it.
- Thrashing: spending more time paging than computing (concept)
- Diagram: CPU utilization vs degree of multiprogramming, the thrashing cliff (diagram)
- Why increasing multiprogramming can cause thrashing, not fix it (concept)
- The working set model: the pages a process actually needs "now" (concept)
- Working set size and the window parameter (concept)
- Page-Fault Frequency (PFF) as an alternative control strategy (concept)
- Compare: working set vs PFF approaches to controlling thrashing (compare)
- Pitfall: adding more processes to a thrashing system to "use the CPU better" (pitfall)
- Interview: "Throughput just collapsed as load increased — how do you tell if it's thrashing?" (interview)

---

## Group: File Systems (file-systems)
*inodes, journaling, layout — persistent storage as a usable abstraction*

### Topic: File System Fundamentals (file-system-fundamentals, beginner)
Scope: what a file system provides on top of raw disk blocks — files, attributes, operations.
- What a file system actually provides: naming, persistence, organization (concept)
- File attributes: name, size, type, permissions, timestamps (concept)
- File operations: create, open, read, write, seek, close, delete (concept)
- Diagram: the file system as a layer between apps and raw disk blocks (diagram)
- File types: regular, directory, special/device files (concept)
- Sequential vs direct (random) access (compare)
- Pitfall: assuming "delete" immediately frees disk space (pitfall)
- Interview: "What does the OS actually do when you call open() on a file?" (interview)

### Topic: File Allocation Methods (file-allocation-methods, intermediate)
Scope: how a file's blocks are tracked on disk — contiguous, linked, and indexed allocation.
- The allocation problem: which disk blocks belong to which file (concept)
- Contiguous allocation: simple but fragmentation-prone (concept)
- Linked allocation: each block points to the next (concept)
- Diagram: linked allocation with block pointers (diagram)
- The problem with linked allocation for random access (concept)
- Indexed allocation: an index block listing all data blocks (concept)
- Multilevel and combined indexing for large files (concept)
- Diagram: indexed allocation with a single index block (diagram)
- Compare: contiguous vs linked vs indexed — speed vs fragmentation vs overhead (compare)
- Interview: "Why can seeking to the middle of a file be slow on some file systems and not others?" (interview)

### Topic: Inodes & Unix File Systems (inodes-and-unix-file-systems, intermediate)
Scope: the inode structure, how filenames map to inodes, and hard vs soft links.
- The inode: everything about a file except its name (concept)
- What's inside an inode: metadata + block pointers (concept)
- Direct, single-indirect, double-indirect, triple-indirect pointers (concept)
- Diagram: an inode's pointer structure reaching data blocks (diagram)
- Why this design supports huge files with a small fixed-size inode (concept)
- How a filename maps to an inode via a directory entry (concept)
- Hard links: two names, one inode (concept)
- Symbolic (soft) links: a name pointing to a path (concept)
- Compare: hard link vs soft link — what breaks when the target moves or is deleted (compare)
- Pitfall: assuming deleting a file with 2 hard links frees the data immediately (pitfall)
- Interview: "What's the difference between a hard link and a symbolic link, concretely?" (interview)

### Topic: Directory Structures & Mounting (directory-structures-and-mounting, beginner)
Scope: how directories organize names into a tree and how separate file systems get grafted together.
- Directories as a special file: a table of name-to-inode mappings (concept)
- Single-level vs tree-structured directories (concept)
- Absolute vs relative paths and path resolution (concept)
- Diagram: resolving a multi-component path through nested directories (diagram)
- Mount points: grafting one file system onto another's tree (concept)
- Why Unix has one tree while Windows has drive letters (compare)
- Pitfall: a path resolution failing partway — permission vs missing component (pitfall)
- Interview: "What happens, step by step, when you run `cat /a/b/c.txt`?" (interview)

### Topic: Free Space Management (free-space-management, intermediate)
Scope: how a file system tracks which blocks are available for allocation.
- The free space problem: knowing which blocks are available (concept)
- Bit vector (bitmap) approach (concept)
- Diagram: a block bitmap with allocated/free bits (diagram)
- Linked free list approach (concept)
- Grouping and counting optimizations over a naive free list (concept)
- Compare: bitmap vs free list — space overhead vs scan speed (compare)
- Interview: "How would you quickly find a run of N free contiguous blocks?" (interview)

### Topic: Journaling & Crash Consistency (journaling-and-crash-consistency, advanced)
Scope: the crash consistency problem and how write-ahead logging solves it for file systems.
- The crash consistency problem: a multi-step update interrupted mid-way (concept)
- Worked example: a crash during file append leaving inconsistent metadata (concept)
- Write-ahead logging (journaling): the core idea (concept)
- Diagram: journal transaction lifecycle — write, commit, checkpoint (diagram)
- Journaling modes: data journaling vs ordered vs writeback (compare)
- Metadata-only journaling — why most file systems don't journal data (concept)
- Replaying the journal after a crash (concept)
- fsck: the older, slower alternative to journaling (concept)
- Pitfall: assuming journaling means zero data loss ever (pitfall)
- Interview: "Why does ext4 journal metadata but not always file data?" (interview)

### Topic: Modern File Systems (modern-file-systems, advanced)
Scope: extent-based allocation and copy-on-write file systems as the current state of the art.
- Extents: allocating in ranges instead of block-by-block (concept)
- Diagram: extent-based allocation vs block pointer allocation (diagram)
- Copy-on-write file systems: never overwrite in place (concept)
- How CoW gives cheap snapshots (concept)
- ZFS and Btrfs — what they add: checksums, pooling (concept)
- Checksumming for silent data corruption detection (concept)
- Compare: traditional journaling FS (ext4) vs CoW FS (ZFS/Btrfs) (compare)
- Interview: "Why can ZFS snapshots be nearly instant regardless of file size?" (interview)

---

## Group: I/O & Device Management (io-systems)
*interrupts, DMA, buffering — getting bytes to and from the real world*

### Topic: I/O Hardware & Device Controllers (io-hardware-and-device-controllers, beginner)
Scope: the hardware layer between the CPU and a physical device.
- The device controller: hardware between the CPU and the device (concept)
- Device registers: status, control, data (concept)
- Memory-mapped I/O vs port-mapped I/O (compare)
- Diagram: CPU, bus, controller, device relationship (diagram)
- How the CPU checks device status: reading a status register (concept)
- Pitfall: assuming all I/O uses "special" instructions (memory-mapped I/O looks like normal memory access) (pitfall)
- Interview: "What's the difference between memory-mapped I/O and port-mapped I/O?" (interview)

### Topic: I/O Techniques — Polling, Interrupts, DMA (io-techniques-polling-interrupts-dma, intermediate)
Scope: the three strategies for moving data between devices and memory, and their CPU-involvement trade-offs.
- Programmed I/O: the CPU does all the work, including moving data (concept)
- Polling: repeatedly checking if the device is ready (concept)
- Why polling wastes CPU cycles (concept)
- Interrupt-driven I/O: the device signals when ready (concept; cross-link: OS Fundamentals, Interrupts/Traps/Exceptions)
- Diagram: polling vs interrupt-driven I/O timelines (diagram)
- Direct Memory Access (DMA): a controller moves data without the CPU (concept)
- Diagram: DMA transfer bypassing the CPU for the data path (diagram)
- Why DMA matters for high-throughput devices (disk, network) (concept)
- Compare: programmed I/O vs interrupt-driven vs DMA — CPU involvement vs complexity (compare)
- Pitfall: assuming DMA removes the CPU from the loop entirely (pitfall)
- Interview: "Why is DMA important for a disk controller transferring a large file?" (interview)

### Topic: Device Drivers & the I/O Subsystem (device-drivers-and-the-io-subsystem, intermediate)
Scope: the driver's role as translator, and the unified I/O interface the kernel presents to applications.
- What a device driver actually is: the kernel's translator per device (concept)
- Block devices vs character devices (compare)
- Diagram: the kernel I/O stack — app, syscall layer, generic I/O, driver, device (diagram)
- The device-independent I/O interface — why read() works the same everywhere (concept)
- Loading drivers: built-in vs loadable kernel modules (concept)
- Where drivers run: kernel space vs userspace drivers (concept)
- Pitfall: a buggy driver crashing the whole kernel (pitfall)
- Interview: "Why does one bad device driver crash your entire OS instead of just failing that device?" (interview)

### Topic: Buffering, Caching & Spooling (buffering-caching-spooling, intermediate)
Scope: how the OS smooths speed mismatches between devices and the CPU.
- Why I/O needs buffering: speed mismatch between devices and CPU (concept)
- Single buffering vs double buffering (concept)
- Diagram: double buffering keeping production and consumption overlapped (diagram)
- Circular buffering for streaming I/O (concept)
- The disk/page cache: buffering reads and writes in memory (concept)
- Write-back vs write-through caching policies (compare)
- Spooling: queuing output for a device that serves one client at a time (concept)
- Pitfall: assuming a completed write() means data is safely on disk (pitfall)
- Interview: "You called write() and it returned — is your data safe on disk?" (interview)

### Topic: Disk Scheduling Algorithms (disk-scheduling-algorithms, advanced)
Scope: ordering disk-arm movement to minimize seek time on rotational media.
- Why disk scheduling matters: seek time dominates HDD performance (concept)
- FCFS disk scheduling — simple but potentially wasteful (concept)
- Shortest Seek Time First (SSTF) — and its starvation risk (concept)
- SCAN (the elevator algorithm) (concept)
- Diagram: SCAN sweeping across cylinders like an elevator (diagram)
- C-SCAN — uniform wait time via one-direction scanning (concept)
- LOOK and C-LOOK — not going all the way to the end (concept)
- Code: total head movement compared across algorithms for one request queue (code)
- Compare: SSTF vs SCAN vs C-SCAN — fairness vs total seek time (compare)
- Pitfall: applying HDD scheduling logic to SSDs, where seek time is ~0 (pitfall)
- Interview: "Why doesn't seek-minimizing disk scheduling matter much for SSDs?" (interview)

### Topic: SSDs & Modern Storage I/O (ssd-and-modern-storage-io, advanced)
Scope: how flash storage breaks HDD-era assumptions — erase-before-write, wear leveling, TRIM.
- How SSDs are physically different: no moving parts, page/block erase structure (concept)
- Why you can't overwrite a flash page in place — erase-before-write (concept)
- Write amplification: a small write causing a much larger internal write (concept)
- Diagram: SSD block/page layout and the erase cycle (diagram)
- Wear leveling: spreading writes to avoid wearing out one region (concept)
- The TRIM command: telling the SSD which blocks are actually free (concept)
- Garbage collection inside an SSD's controller (concept)
- Compare: HDD scheduling assumptions vs SSD reality (compare)
- Interview: "Why do SSDs slow down over time if you never TRIM them?" (interview)

---

## Group: Linux/Unix Internals (linux-internals)
*processes, signals, /proc, tooling — the same concepts, hands-on on a real system*

### Topic: Signals (signals, intermediate)
Scope: the async-notification mechanism — common signals, handlers, and the safety rules around them.
- What a signal is: async notification to a process (concept)
- Common signals: SIGINT, SIGTERM, SIGKILL, SIGSEGV, SIGCHLD (concept)
- Default actions: terminate, ignore, core dump, stop (concept)
- Installing a signal handler (concept)
- Code: catching SIGINT to clean up before exit (code)
- Why SIGKILL and SIGSTOP can't be caught or ignored (concept)
- Diagram: signal delivery timeline — sender, kernel, handler execution (diagram)
- Async-signal-safety: why most functions are unsafe inside a handler (concept)
- Compare: SIGTERM vs SIGKILL — why you try SIGTERM first (compare)
- Pitfall: doing non-trivial work (malloc, printf) inside a signal handler (pitfall)
- Interview: "Why does `kill -9` always work but plain `kill` sometimes doesn't?" (interview)

### Topic: The /proc Filesystem (the-proc-filesystem, intermediate)
Scope: /proc as a live, file-shaped view into kernel and process state.
- /proc: a virtual file system exposing kernel state as files (concept)
- /proc/[pid]/ — status, cmdline, fd, maps (concept)
- Code: reading /proc/[pid]/status to inspect a process (code)
- /proc/meminfo, /proc/cpuinfo — system-wide info (concept)
- Diagram: how ps/top are really just /proc readers (diagram)
- /proc/[pid]/fd — inspecting open file descriptors live (concept)
- /proc/[pid]/maps — reading a process's memory layout live (concept)
- Pitfall: treating /proc reads as free — some are computed on read (pitfall)
- Interview: "How would you find which files a running process has open, without stopping it?" (interview)

### Topic: Process & System Monitoring Tools (process-and-system-monitoring-tools, beginner)
Scope: reading and correctly interpreting ps/top/htop/vmstat/free output.
- ps: snapshotting process state from the command line (concept)
- Code: useful ps invocations and reading their columns (code)
- top/htop: live, continuously refreshing process views (concept)
- Reading load average correctly (concept)
- vmstat and free: memory and CPU at a glance (concept)
- Diagram: mapping "load average 8 on a 4-core box" to what's actually happening (diagram)
- Compare: CPU-bound vs I/O-bound symptoms in these tools (compare)
- Pitfall: treating high "used" memory as a problem without accounting for page cache (pitfall)
- Interview: "Load average is 12 on a 4-core machine — is the system in trouble?" (interview)

### Topic: Permissions & Users (permissions-and-users, beginner)
Scope: the Unix permission model, uid/gid, and setuid — foundational and security-adjacent.
- The Unix permission model: owner/group/other × read/write/execute (concept)
- Reading permission bits: rwxr-xr-- and what it means (concept)
- uid/gid: real vs effective vs saved IDs (concept)
- Diagram: how effective UID changes across a setuid execution (diagram)
- The setuid bit: running as the file owner, not the caller (concept)
- Why setuid root binaries are a classic security concern (concept)
- umask: how default permissions on new files are computed (concept)
- Directory execute permission — the "search" bit that trips people up (concept)
- Pitfall: assuming no read permission on a directory blocks access to files inside it by path (pitfall)
- Interview: "What does the setuid bit do, and why is it risky on a root-owned binary?" (interview)

### Topic: Shell & Process Groups (shell-and-process-groups, intermediate)
Scope: job control — process groups, sessions, and what happens to background jobs on logout.
- Process groups: why the shell groups related processes together (concept)
- Sessions and the controlling terminal (concept)
- Foreground vs background jobs (concept)
- Diagram: session → process groups → processes hierarchy (diagram)
- Job control signals: Ctrl+C (SIGINT) and Ctrl+Z (SIGTSTP) (concept)
- What happens to background jobs when you close the terminal — SIGHUP (concept)
- nohup and disown — surviving terminal close on purpose (concept)
- Pitfall: assuming `&` alone survives a logout (pitfall)
- Interview: "Why does closing your SSH session kill a background job unless you used nohup?" (interview)

### Topic: Containers — Namespaces & cgroups (containers-namespaces-cgroups, advanced)
Scope: how Linux containers are built from kernel primitives — no VM involved.
- The big idea: a container is a regular process with a restricted view, not a VM (concept)
- Namespaces: giving a process its own view of a global resource (concept)
- The namespace types: PID, network, mount, UTS, IPC, user (concept)
- Diagram: a containerized process's PID namespace vs the host's (diagram)
- cgroups: limiting and accounting for resource usage (concept)
- What cgroups control: CPU, memory, I/O limits (concept)
- Diagram: how a container runtime composes namespaces + cgroups + a root filesystem (diagram)
- Union/layered filesystems (e.g., overlayfs) for container images (concept)
- Compare: containers vs virtual machines — isolation boundary and overhead (compare)
- Pitfall: assuming container isolation is as strong as VM isolation (pitfall)
- Interview: "How is a Docker container different from a lightweight VM, mechanically?" (interview)

### Topic: strace & Debugging Tools (strace-and-debugging-tools, advanced)
Scope: diagnosing a running or misbehaving process with strace, ltrace, and lsof.
- strace: watching every syscall a process makes (concept)
- Code: strace output on a simple program, reading the trace (code)
- Attaching strace to an already-running process (concept)
- ltrace: tracing library calls instead of syscalls (concept)
- lsof: listing open files (and sockets) held by processes (concept)
- Diagram: choosing the right tool — syscalls vs library calls vs open resources (diagram)
- Code: a worked diagnosis — using strace to find why a process hangs on a file read (code)
- Pitfall: strace's overhead changing timing-sensitive bugs (the observer effect) (pitfall)
- Interview: "A process is hung and you don't have its source — how do you start diagnosing it?" (interview)

---

## Cross-links & overlap notes

- **Interrupts, Traps & Exceptions** (OS Fundamentals) covers the general mechanism once; **I/O Techniques — Polling, Interrupts, DMA** (I/O & Device Management) reuses it for device I/O without re-deriving it.
- **Concurrency Hazards — Livelock & Starvation** (Concurrency & Synchronization) mentions deadlock only to place it in the hazard family; full conditions/prevention/avoidance/detection live in the **Deadlocks** group.
- **Fragmentation** and **Swapping** (Memory Management) both hand off to **Virtual Memory & Paging** for the paging-based fixes (no external fragmentation, page-level swap/thrashing) rather than duplicating them.
- **Process Lifecycle — fork/exec** (Processes & Threads) introduces copy-on-write; the mechanics of the underlying page fault are owned by **Demand Paging** (Virtual Memory & Paging).
- **Deadlock Detection & Recovery** interview slide cross-links to the Databases area's Transactions & Concurrency group (DB deadlock handling is a worked application of this group's theory).
- **Scheduling in Practice — Linux CFS** (CPU Scheduling) is theory-of-one-scheduler; broader Linux process/tooling material lives in **Linux/Unix Internals**, and **System Boot Process**'s init-system slide (`systemd`) is expanded operationally in that same group.
- No group duplicates another's core mechanism; overlaps above are intentional single-owner + reference, per the non-overlap rule.
