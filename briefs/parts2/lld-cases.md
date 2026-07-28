# LLD Case Studies — restructured (Phase B replacement for `lld-case-studies`)

Replaces the single 13-topic `lld-case-studies` group with 5 domain-split groups covering 32
end-to-end LLD case studies. The 13 original topics are **preserved** (same slugs, same core
outline) and redistributed by domain; each gets an added framing (`overview`) slide and a
closing follow-ups (`interview`) slide since the canonical flagship skeleton requires both and
the originals had neither. 19 new topics fill out the domains the owner called out plus
commonly-asked systems added during authoring. See `## Boundary notes` at the end for
HLD-overlap disambiguation and what was merged/cut under the value filter.

## Group: LLD Case Studies — Games (lld-cases-games)
*Turn-based and puzzle games: modeling a board and its rules so win/legality logic doesn't collapse into one giant switch.*

### Topic: Tic-Tac-Toe (tic-tac-toe, beginner)
A minimal game to practice generalizing a board and its win condition.
- The tic-tac-toe prompt and how fast to scope it in an interview (overview)
- Requirements: board size, win condition, players — keeping v1 minimal (concept)
- Core entities: Board, Cell/Symbol, Player, Game — who owns the win-check logic (concept)
- Diagram: class diagram for a generalized N x N tic-tac-toe (diagram)
- Code: a `Board.checkWinner()` that generalizes beyond 3x3 (code)
- Strategy for pluggable win conditions or player types (human vs bot) (concept) — cross-link: strategy-pattern
- Compare: hardcoded 3x3 rules vs a generalized N x N design — the extensibility question (compare)
- Pitfall: win-check logic duplicated per row/column/diagonal instead of unified (pitfall)
- Follow-ups: what changes for a 3D or Connect-Four variant (interview)

### Topic: Snake and Ladder (snake-and-ladder, beginner)
A simulation-style case study: decoupling board rules from the turn loop.
- The snake-and-ladder prompt and scoping a "simple" simulation game in an interview (overview)
- Requirements: board, dice, snakes/ladders, players, turn order (concept)
- Core entities: Board, Dice, Player, Jump (snake/ladder), Game (concept)
- Diagram: class diagram plus a turn's flow through the entities (diagram)
- Code: a `Game.playTurn()` loop composing dice roll + position update + jump resolution (code)
- Decoupling board rules (jumps) from player/turn logic (concept)
- Compare: modeling snakes and ladders as one `Jump` concept vs two separate classes (compare)
- Pitfall: hardcoding board size/jump positions instead of making the board data-driven (pitfall)
- Extending to multiple dice or multiplayer-skip rules without breaking the core loop (concept)
- Follow-ups: how you'd add a "You've Been Framed"-style power-card variant live (interview)

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
The canonical polymorphism-heavy case study: pieces that know their own legal moves.
- The chess prompt and how to scope a huge domain into a 45-minute design (overview)
- Requirements: board, pieces, turns, check/checkmate, move legality (concept)
- Core entities: Board, Piece (+ subclasses), Move, Player, Game (concept)
- Diagram: the Piece hierarchy and where move-validation logic actually lives (diagram)
- Polymorphic `Piece.getValidMoves()` vs one giant rules engine (concept)
- Code: `Bishop.getValidMoves()` vs `Knight.getValidMoves()`, same interface (code)
- Modeling check/checkmate detection as a concern separate from per-piece movement (concept)
- Compare: polymorphism-per-piece vs a centralized rules table — the trade-offs interviewers probe (compare)
- Pitfall: special-move handling (castling, en passant, promotion) bolted on as if/else instead of designed for (pitfall)
- Follow-ups: adding a time-control clock or move-undo/replay without touching `Piece` (interview)

## Group: LLD Case Studies — Machines (lld-cases-machines)
*Hardware-facing state machines: payment, dispensing, and scheduling loops where the physical device's states are the design.*

### Topic: Parking Lot (parking-lot, intermediate)
The canonical multi-entity LLD prompt: spot-assignment strategy, ticketing, and a concurrency wrinkle.
- The parking lot prompt and why it's used to test scoping speed, not cleverness (overview)
- Requirements: levels, spot types, entry/exit, pricing — scoping a huge prompt fast (concept)
- Core entities: ParkingLot, Level, ParkingSpot, Vehicle, Ticket (concept)
- Diagram: class diagram for the multi-level parking lot (diagram)
- Spot-assignment strategy: nearest-available vs size-matched vs custom (concept) — cross-link: strategy-pattern
- Code: `ParkingLot.parkVehicle()` selecting a spot via a pluggable strategy (code)
- Concurrency: two cars racing for the last spot — locking the assignment step (concept) — cross-link: oo-concurrency
- Pricing as its own strategy object: hourly, flat, per-vehicle-type (concept)
- Compare: a single God `ParkingLot` class vs decomposed Level/Spot/Ticket collaborators (compare)
- Pitfall: modeling spot availability as a boolean scan instead of an indexed/queryable structure (pitfall)
- Follow-ups: how you'd extend this to reserved/EV-charging spots or a multi-lot chain (interview)

### Topic: Vending Machine (vending-machine, intermediate)
The canonical State-pattern case study: inventory, payment, and dispensing as explicit states.
- The vending machine prompt and why interviewers use it to test State-pattern instincts (overview)
- Requirements: inventory, payment, dispensing, change — scoping v1 (concept)
- Core entities: Inventory, Product, Slot, Payment, Machine (concept)
- Diagram: the machine's state machine — idle → selecting → paid → dispensing (diagram)
- Code: implementing states as State-pattern objects, not a switch on an enum (code) — cross-link: state-pattern
- Handling underpayment/overpayment and change-making as a separate concern (concept)
- Compare: State pattern vs enum + switch for this exact problem — the canonical comparison (compare)
- Pitfall: a state object reaching back into the machine's internals instead of using its exposed API (pitfall)
- Extending to multiple payment methods via Strategy, and to recipe-based dispensing (coffee/tea) without touching the state machine (concept) — cross-link: strategy-pattern
- Follow-ups: what changes if the machine must support remote restocking/telemetry (interview)

### Topic: ATM System (atm-system, intermediate)
A banking-domain case study pairing a transaction state machine with undoable/auditable operations.
- The ATM prompt and scoping "banking" down to what the interview actually wants (overview)
- Requirements: authentication, balance/withdraw/deposit, hardware components (concept)
- Core entities: ATM, Card, Account, Transaction, CashDispenser (concept)
- Diagram: class diagram including the hardware-facing components (diagram)
- Diagram: the ATM's transaction lifecycle as a state machine — idle → authenticated → transaction → dispensing (diagram)
- Code: `Transaction.execute()` designed so it can be logged/audited/undone (code) — cross-link: command-pattern
- Modeling insufficient funds/hardware failure as first-class outcomes, not careless exceptions (concept)
- Compare: modeling each transaction type as a Command vs one `Transaction` class with a type field (compare)
- Pitfall: the ATM class talking directly to the bank's account storage instead of through a service boundary (pitfall)
- Follow-ups: how a multi-bank ATM network or cardless withdrawal changes the design (interview)

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
A state-machine-plus-scheduling case study across multiple concurrent elevators.
- The elevator prompt and why it's a favorite for testing scheduling thinking (overview)
- Requirements: multiple elevators, multiple floors, requests from inside and outside (concept)
- Core entities: Elevator, ElevatorController, Request, Floor (concept)
- Diagram: the elevator's own state machine — idle/moving-up/moving-down/door-open (diagram)
- Scheduling algorithm: how the controller picks which elevator serves a request (concept)
- Diagram: a scheduling decision across 3 elevators and pending requests (diagram)
- Code: `Controller.assignRequest()` implementing a simple scheduling strategy (code) — cross-link: strategy-pattern
- Concurrency: multiple requests arriving while an elevator is mid-move (concept) — cross-link: oo-concurrency
- Compare: a single shared controller vs each elevator deciding independently (compare)
- Pitfall: a scheduling algorithm that starves far-away requests indefinitely (pitfall)
- Follow-ups: how you'd extend this to a freight elevator with capacity limits or a SCAN-style scheduling variant (interview)

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
A data-structure-driven LLD prompt: hashmap plus doubly linked list for O(1) access and eviction.
- The LRU cache prompt and why it's really a data-structures interview wearing an LLD hat (overview)
- Requirements: O(1) get/put, fixed capacity, eviction on overflow (concept)
- Core data structure: hashmap + doubly linked list, and why each alone isn't enough (concept)
- Diagram: hashmap-to-node pointers plus the linked list's recency ordering (diagram)
- Code: `get()`/`put()` maintaining O(1) by moving nodes to the front (code)
- Thread-safety: what changes if `get`/`put` are called concurrently (concept) — cross-link: designing-thread-safe-classes
- Compare: LRU vs LFU vs FIFO eviction — when interviewers ask "why not just FIFO" (compare)
- Pitfall: an "O(1)" implementation that's secretly O(n) because eviction scans the list (pitfall)
- Extending to a generic `Cache<K,V>` interface with a pluggable eviction policy (concept) — cross-link: strategy-pattern
- Follow-ups: how you'd shard this cache across threads or turn it into a distributed cache (interview) — cross-link: distributed-caching

### Topic: Logging Framework (logging-framework, intermediate)
A deceptively deep "simple" prompt: levels, sinks, and formatting as pluggable pieces.
- The logging framework prompt and why "just print to console" fails the interview (overview)
- Requirements: log levels, multiple destinations, formatting — a deceptively deep "simple" prompt (concept)
- Core entities: Logger, LogLevel, Appender/Sink, Formatter (concept)
- Diagram: a log call flowing through level-check → formatter → multiple appenders (diagram)
- Chain of Responsibility for level filtering — DEBUG → INFO → ERROR handlers (concept) — cross-link: chain-of-responsibility-pattern
- Code: adding a new appender (e.g. `CloudAppender`) without touching `Logger` (code) — cross-link: ocp-open-closed
- Should `Logger` be a Singleton? The trade-offs, revisited in a real design (concept) — cross-link: singleton-pattern
- Compare: synchronous vs asynchronous logging — why async needs its own design care (compare)
- Pitfall: a logging call that itself throws and crashes the caller (pitfall)
- Follow-ups: how you'd add structured/JSON logging or sampling under high volume (interview)

### Topic: Rate Limiter (rate-limiter, advanced)
An algorithm-heavy case study comparing limiter strategies under concurrent access.
- The rate limiter prompt and the algorithm menu interviewers expect you to know (overview)
- Requirements: per-user/per-API limits, what happens on breach (concept)
- Algorithm options: fixed window, sliding window, token bucket, leaky bucket (concept)
- Diagram: a token bucket filling and draining over time (diagram)
- Diagram: fixed window's boundary-burst problem vs sliding window fixing it (diagram)
- Code: implementing a token bucket limiter as a pluggable Strategy (code) — cross-link: strategy-pattern
- Thread-safety: concurrent requests checking/decrementing the same bucket (concept) — cross-link: oo-concurrency
- Compare: the four algorithms — memory cost, burst handling, accuracy (compare)
- Pitfall: a check-then-act limiter that isn't atomic, letting bursts through under load (pitfall)
- Where this single-process design sits vs a distributed rate limiter (concept) — cross-link: distributed-rate-limiting
- Follow-ups: how you'd extend this to per-tenant tiered limits (free vs paid) (interview)

### Topic: Notification System (notification-system, intermediate)
A multi-channel fan-out prompt built on Observer plus per-user strategy — the class-level design, not the HLD fan-out service.
- The notification system prompt and disambiguating this class-level design from the HLD version of the same name (overview)
- Requirements: multiple channels (email/SMS/push), templates, user preferences (concept)
- Core entities: Notification, Channel, Template, User Preference (concept)
- Diagram: an event fanning out to multiple channel senders (diagram)
- Observer pattern: subjects (events) and observers (channel senders) (concept) — cross-link: observer-pattern
- Code: adding a new channel (e.g. WhatsApp) without modifying the notification dispatcher (code) — cross-link: ocp-open-closed
- Strategy for per-user channel preference and quiet hours (concept)
- Compare: push-based fan-out vs a queue-based fan-out for reliability (compare)
- Pitfall: a `Notification` class that formats itself differently per channel via if/else (pitfall)
- Follow-ups: how you'd add delivery-status tracking and retry-on-failure per channel (interview)

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
A gentle first case study: modeling a catalog, its copies, members, and borrowing rules.
- The library management prompt and why it's the standard "gentle first" LLD case study (overview)
- Requirements: books, members, borrowing rules, fines — scoping v1 (concept)
- Core entities: Book, BookItem (copy), Member, Loan — why "book" and "copy" differ (concept)
- Diagram: class diagram for the core library entities (diagram)
- Code: `Member.checkout(BookItem)` with availability + limit checks (code)
- Modeling reservations/holds as their own entity, not a boolean flag (concept)
- Compare: a single `Book` class vs `Book` + `BookItem` — catalog vs inventory concerns (compare)
- Pitfall: fine calculation living inside `Member` instead of a dedicated policy object (pitfall) — cross-link: srp-single-responsibility
- Where a Strategy pattern helps for different fine/loan policies per member type (concept) — cross-link: strategy-pattern
- Follow-ups: how you'd extend this to multi-branch libraries with inter-branch transfers (interview)

### Topic: Splitwise (Expense Sharing) (splitwise-expense-sharing, advanced)
A ledger-modeling case study built around split strategies and a debt-simplification algorithm.
- The Splitwise prompt and why it's a favorite ledger-modeling case study (overview)
- Requirements: groups, expenses, split types (equal/exact/percentage), settle-up (concept)
- Core entities: User, Group, Expense, Split, Balance Sheet (concept)
- Diagram: class diagram for expenses and their splits (diagram)
- Strategy pattern for split types — equal vs exact vs percentage (concept) — cross-link: strategy-pattern
- The debt-simplification problem: minimizing the number of settling transactions (concept)
- Diagram: a debt graph before and after simplification (diagram)
- Code: a greedy debt-simplification algorithm over net balances (code)
- Compare: storing pairwise balances vs net balances per user — why net wins (compare)
- Pitfall: floating-point rounding across splits that never quite sums to the original amount (pitfall)
- Follow-ups: how you'd extend this to multi-currency groups or partial settle-ups (interview)

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

## Boundary notes

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
