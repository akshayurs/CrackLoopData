## Replacements

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
