# Area: Databases (databases)

Slide tags: `[concept]` `[diagram]` `[code]` `[compare]` `[pitfall]`. MCQs + interview questions attach at topic level (separate files), not listed here.

## Group: Relational Model & Keys (relational-model)

### Topic: The Relational Model (relational-model-basics, beginner)
What a relation actually is and why the model won.
- [concept] Relation, tuple, attribute, domain — the precise vocabulary
- [concept] Schema vs instance; the closed-world assumption
- [diagram] A table mapped to relation/tuple/attribute terms
- [concept] Why sets: no duplicate rows, no inherent order
- [compare] Relational vs the older hierarchical/network models
- [pitfall] Treating row order or physical layout as meaningful

### Topic: Keys — Super, Candidate, Primary, Foreign (keys, beginner)
The four key types and how they enforce identity and links.
- [concept] Superkey → candidate key → primary key, narrowing down
- [concept] Choosing a primary key; natural vs surrogate keys
- [diagram] Foreign key linking two tables (referential arrow)
- [concept] Composite keys and when they're unavoidable
- [compare] Natural vs surrogate key trade-offs
- [pitfall] Nullable columns in a candidate key
- [code] `PRIMARY KEY`, `FOREIGN KEY … REFERENCES`, `UNIQUE`

### Topic: Integrity Constraints (integrity-constraints, beginner)
The guarantees the engine enforces so data stays valid.
- [concept] Entity, referential, and domain integrity
- [concept] `NOT NULL`, `CHECK`, `UNIQUE`, `DEFAULT`
- [concept] Referential actions: CASCADE / SET NULL / RESTRICT
- [diagram] What a cascading delete touches
- [pitfall] Orphan rows from a missing/disabled foreign key
- [code] Declaring constraints inline vs as table constraints

### Topic: Relational Algebra (relational-algebra, intermediate)
The formal operators every query compiles down to.
- [concept] Selection σ and projection π
- [concept] Union, difference, Cartesian product
- [concept] Joins: theta, equi, natural
- [diagram] An SQL query rewritten as an algebra tree
- [concept] Rename ρ and expression composition
- [compare] Algebra (procedural) vs calculus (declarative)
- [pitfall] Projection dropping duplicates in theory vs SQL keeping them

## Group: SQL (sql)

### Topic: SELECT Fundamentals (sql-select, beginner)
Reading data — the statement you write most.
- [concept] Logical clause order vs written order (FROM→…→SELECT)
- [code] `SELECT … FROM … WHERE`
- [concept] `DISTINCT` and column expressions/aliases
- [concept] Three-valued logic: TRUE/FALSE/UNKNOWN
- [pitfall] `WHERE col = NULL` never matches — use `IS NULL`
- [diagram] The clause-evaluation pipeline

### Topic: Filtering, Sorting & Pagination (filtering-sorting, beginner)
Narrowing and ordering result sets.
- [concept] Predicates, `BETWEEN`, `IN`, `LIKE`
- [code] `ORDER BY … LIMIT … OFFSET`
- [compare] OFFSET vs keyset ("seek") pagination
- [pitfall] Large OFFSET scanning and discarding rows
- [concept] Deterministic ordering needs a tiebreaker column
- [pitfall] `LIKE '%x'` can't use a normal index

### Topic: Joins (joins, beginner)
Combining rows across tables — the interview staple.
- [concept] INNER, LEFT/RIGHT/FULL OUTER
- [diagram] Venn-style view of each join type
- [code] Multi-table join with aliases
- [concept] Self-join and non-equi join
- [compare] `WHERE` filter vs `ON` filter on outer joins
- [pitfall] Fan-out row multiplication from a one-to-many join
- [pitfall] Cross join from a forgotten join condition

### Topic: Aggregation & GROUP BY (aggregation, beginner)
Rolling rows up into summaries.
- [concept] `COUNT/SUM/AVG/MIN/MAX` and NULL handling
- [code] `GROUP BY … HAVING`
- [compare] `WHERE` (pre-group) vs `HAVING` (post-group)
- [pitfall] Selecting a non-aggregated column not in GROUP BY
- [concept] `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)`
- [diagram] Rows collapsing into groups

### Topic: Subqueries (subqueries, intermediate)
Queries inside queries and how they're evaluated.
- [concept] Scalar, row, and table subqueries
- [compare] Correlated vs non-correlated
- [code] `IN`, `EXISTS`, and derived tables
- [pitfall] `NOT IN` with a NULL in the subquery returns nothing
- [compare] `EXISTS` vs `IN` — when each is faster
- [concept] When a subquery is really a join in disguise

### Topic: Data Modification & NULL Semantics (dml-nulls, intermediate)
Writing data and surviving three-valued logic.
- [code] `INSERT`, `UPDATE`, `DELETE`, `UPSERT/MERGE`
- [concept] NULL propagation in arithmetic and comparisons
- [code] `COALESCE`, `NULLIF`, `IS DISTINCT FROM`
- [pitfall] `UPDATE`/`DELETE` with no `WHERE`
- [concept] `RETURNING` to read back what changed
- [pitfall] Aggregates silently skipping NULLs

## Group: Advanced SQL (advanced-sql)

### Topic: Window Functions (window-functions, intermediate)
Per-row calculations over a related window — the senior-SQL signal.
- [concept] `OVER (PARTITION BY … ORDER BY …)`
- [code] `ROW_NUMBER`, `RANK`, `DENSE_RANK`
- [code] `LAG`/`LEAD` for row-to-row deltas
- [concept] Running totals and moving averages via frames
- [compare] Window function vs GROUP BY (keeps every row)
- [pitfall] Frame default (`RANGE`) surprising running sums
- [diagram] A partition with an ordered running calculation

### Topic: Common Table Expressions & Recursion (ctes, intermediate)
Naming subqueries and walking hierarchies.
- [code] `WITH name AS (…)` for readability
- [concept] Recursive CTE anchor + recursive member
- [code] Walking an org tree / graph path
- [diagram] Recursive CTE iterations expanding a tree
- [pitfall] Missing termination → infinite recursion
- [compare] CTE vs subquery vs temp table (materialization)

### Topic: Views & Materialized Views (views, intermediate)
Saved queries and cached results.
- [concept] View as a stored query; updatable-view limits
- [compare] Regular vs materialized view
- [concept] Refresh strategies and staleness
- [pitfall] Nested views hiding a monstrous query plan
- [code] `CREATE VIEW` / `CREATE MATERIALIZED VIEW`

### Topic: Stored Programs & Triggers (stored-programs-triggers, intermediate)
Logic that lives in the database.
- [concept] Stored procedures vs functions
- [code] A procedure with parameters and control flow
- [concept] Triggers: BEFORE/AFTER, row vs statement
- [pitfall] Hidden side effects and trigger cascades
- [compare] Business logic in DB vs application layer
- [pitfall] Triggers that tank write throughput

## Group: Data Modeling & Normalization (data-modeling-normalization)

### Topic: ER & EER Modeling (er-modeling, beginner)
Turning requirements into an entity model.
- [concept] Entities, attributes, relationships
- [concept] Cardinality and participation constraints
- [diagram] A small ER diagram (crow's-foot)
- [concept] Weak entities and identifying relationships
- [concept] EER: generalization/specialization, inheritance
- [diagram] Mapping ER to relational tables
- [pitfall] Many-to-many without a junction table

### Topic: Functional Dependencies (functional-dependencies, intermediate)
The theory that drives normalization.
- [concept] X → Y meaning; trivial vs non-trivial
- [concept] Armstrong's axioms
- [concept] Attribute closure X⁺
- [code] Computing a candidate key from FDs
- [concept] Minimal cover
- [pitfall] Confusing correlation in data with a true FD

### Topic: Normalization 1NF → BCNF (normalization, intermediate)
Removing anomalies step by step.
- [concept] Insertion/update/deletion anomalies (the "why")
- [concept] 1NF, 2NF, 3NF definitions
- [diagram] A table decomposed through the normal forms
- [concept] BCNF and where 3NF isn't enough
- [compare] 3NF vs BCNF (dependency preservation trade-off)
- [pitfall] Lossy decomposition; the lossless-join test
- [concept] Brief note: 4NF/multivalued dependencies

### Topic: Denormalization & Trade-offs (denormalization, intermediate)
When to deliberately break the rules.
- [concept] Read performance vs write complexity
- [concept] Redundancy, precomputed aggregates, duplicated columns
- [compare] Normalized OLTP vs denormalized analytics/read models
- [pitfall] Update anomalies you now own manually
- [concept] Materialized views as controlled denormalization

## Group: Transactions & Concurrency (transactions-concurrency)

### Topic: ACID & Transaction Lifecycle (acid-lifecycle, beginner)
What a transaction guarantees.
- [concept] Atomicity, Consistency, Isolation, Durability
- [diagram] Transaction states: active→committed/aborted
- [code] `BEGIN … COMMIT / ROLLBACK`, savepoints
- [concept] Why "consistency" is partly the app's job
- [pitfall] Long-running transactions holding resources
- [compare] Autocommit vs explicit transactions

### Topic: Isolation Levels & Anomalies (isolation-levels, intermediate)
The dial between correctness and concurrency.
- [concept] Dirty read, non-repeatable read, phantom
- [compare] Read Uncommitted / Committed / Repeatable Read / Serializable
- [diagram] Which anomaly each level permits (matrix)
- [concept] Write skew (the anomaly SERIALIZABLE-but-snapshot misses)
- [pitfall] Assuming the default level is SERIALIZABLE
- [code] `SET TRANSACTION ISOLATION LEVEL …`

### Topic: Locking & Two-Phase Locking (locking, advanced)
The pessimistic path to isolation.
- [concept] Shared vs exclusive locks; lock granularity
- [concept] 2PL and strict 2PL
- [diagram] Growing and shrinking lock phases
- [concept] Intention locks and lock escalation
- [pitfall] Lock contention and reduced throughput
- [compare] Row vs page vs table locks

### Topic: MVCC & Deadlocks (mvcc-deadlocks, advanced)
The optimistic path, plus the classic failure mode.
- [concept] Multi-version reads without blocking writers
- [diagram] Version chain per row; snapshot visibility
- [concept] Deadlock conditions and the wait-for graph
- [diagram] A two-transaction deadlock cycle
- [concept] Detection vs prevention vs timeout
- [pitfall] Inconsistent lock ordering causing deadlocks
- [compare] MVCC vs pure locking

### Topic: Serializability & Recoverability (serializability, advanced)
The formal correctness targets for schedules.
- [concept] Serial vs serializable schedules
- [concept] Conflict serializability + precedence graph
- [diagram] Precedence graph with/without a cycle
- [concept] Recoverable, cascadeless, strict schedules
- [pitfall] Cascading aborts from reading uncommitted data

## Group: Storage & Indexing (storage-indexing)

### Topic: Storage & File Organization (storage-file-organization, intermediate)
How rows physically live on disk.
- [concept] Pages/blocks, rows, and the buffer pool
- [compare] Heap vs sorted vs hashed file organization
- [concept] Row-oriented vs column-oriented storage
- [diagram] A page with a slotted-row layout
- [concept] TOAST / overflow for large values
- [pitfall] Random I/O vs sequential I/O cost

### Topic: B-Tree & B+Tree Indexes (btree-indexes, intermediate)
The default index and why it's everywhere.
- [concept] Balanced multi-way tree; height vs fanout
- [diagram] A B+Tree with leaf-level linked list
- [concept] Range scans via leaf traversal
- [compare] B-Tree vs B+Tree (where data lives)
- [pitfall] Index on a low-selectivity column
- [concept] Composite index and left-prefix rule

### Topic: Hash & LSM Indexes (hash-lsm-indexes, advanced)
The write-optimized and point-lookup alternatives.
- [concept] Hash index: O(1) equality, no ranges
- [concept] LSM tree: memtable → SSTables → compaction
- [diagram] LSM write path and compaction levels
- [compare] B-Tree (read-optimized) vs LSM (write-optimized)
- [concept] Bloom filters cutting disk reads
- [pitfall] LSM read/space amplification

### Topic: Index Design & Selectivity (index-design, intermediate)
Choosing indexes like an engineer, not by reflex.
- [concept] Selectivity and cardinality
- [concept] Covering indexes and index-only scans
- [compare] Clustered vs non-clustered indexes
- [pitfall] Over-indexing punishing writes
- [pitfall] Functions on a column disabling the index
- [code] `CREATE INDEX`, composite + partial indexes

## Group: Query Processing & Optimization (query-optimization)

### Topic: Query Execution Pipeline (query-execution, intermediate)
From SQL text to a running plan.
- [diagram] Parse → rewrite → optimize → execute
- [concept] Logical vs physical plan
- [concept] The iterator/volcano execution model
- [concept] Pipelining vs materialization of intermediate results
- [pitfall] Reading a plan bottom-up, not top-down

### Topic: Join Algorithms (join-algorithms, advanced)
The three ways engines actually join.
- [concept] Nested-loop join (and indexed variant)
- [concept] Hash join
- [concept] Sort-merge join
- [compare] Cost profile of each vs input size/sortedness
- [diagram] Hash join build/probe phases
- [pitfall] Nested loops on two large unindexed tables

### Topic: Optimizer, Statistics & EXPLAIN (optimizer-explain, advanced)
Why the planner picks what it picks — and how to read it.
- [concept] Cost-based optimization and the search space
- [concept] Statistics, histograms, cardinality estimation
- [code] Reading `EXPLAIN ANALYZE` output
- [pitfall] Stale statistics → catastrophic plan
- [pitfall] Parameter sniffing / plan caching surprises
- [concept] Estimated vs actual rows as the debugging signal

## Group: NoSQL & Modern Databases (nosql)

### Topic: Why NoSQL (nosql-intro, intermediate)
The motivation and the taxonomy.
- [concept] Drivers: scale, flexible schema, developer velocity
- [compare] The four families (KV, document, column, graph)
- [concept] Aggregate-oriented modeling
- [pitfall] "NoSQL = no schema" (it's schema-on-read)
- [pitfall] Choosing NoSQL to avoid learning SQL
- [diagram] Data-model shapes side by side

### Topic: Key-Value & Document Stores (kv-document, intermediate)
The two most common families.
- [concept] KV: access by key only; Redis/DynamoDB shape
- [concept] Document: nested JSON, secondary indexes
- [code] A document query + partial update
- [compare] Embedding vs referencing documents
- [pitfall] Unbounded document growth
- [concept] Single-table design for access patterns

### Topic: Wide-Column & Graph Databases (column-graph, advanced)
The specialized families and their sweet spots.
- [concept] Wide-column: partition + clustering keys (Cassandra)
- [diagram] Wide-column physical layout
- [concept] Query-first modeling in wide-column
- [concept] Graph DBs: nodes, edges, traversals
- [compare] Graph DB vs relational join for deep relationships
- [pitfall] Modeling a highly-relational domain in KV

## Group: Distributed Databases (distributed-databases)

### Topic: Replication (replication, intermediate)
Copying data for availability and read scale.
- [concept] Single-leader, multi-leader, leaderless
- [diagram] Leader/follower replication flow
- [compare] Synchronous vs asynchronous replication
- [concept] Replication lag and read-your-writes
- [pitfall] Reading stale data from a lagging follower
- [concept] Failover and split-brain risk

### Topic: Partitioning & Sharding (sharding, advanced)
Splitting data to scale writes and storage.
- [concept] Range vs hash partitioning
- [diagram] Rows distributed across shards
- [concept] Consistent hashing and rebalancing
- [concept] Hot partitions and shard keys
- [pitfall] Cross-shard joins and transactions
- [pitfall] A shard key you can't change later

### Topic: CAP, PACELC & Consistency Models (cap-consistency, intermediate)
The theory that frames every distributed trade-off.
- [concept] CAP: consistency, availability, partition tolerance
- [diagram] The choice during a partition (CP vs AP)
- [concept] PACELC: the else-latency half people forget
- [compare] Strong vs eventual vs causal consistency
- [concept] Tunable consistency (quorum reads/writes)
- [pitfall] Treating CAP as "pick 2 freely"

### Topic: Consensus & Distributed Transactions (consensus-transactions, advanced)
Agreeing and committing across nodes.
- [concept] Quorums: R + W > N
- [concept] Consensus (Paxos/Raft) at a high level
- [diagram] Raft leader election + log replication
- [concept] Two-phase commit and its blocking problem
- [compare] 2PC vs saga for cross-service transactions
- [pitfall] Coordinator failure stalling 2PC

## Group: Database Ops (database-ops)

### Topic: Durability, WAL & Crash Recovery (wal-recovery, advanced)
How committed data survives a crash.
- [concept] Write-ahead logging; redo/undo
- [diagram] WAL then page flush ordering
- [concept] Checkpoints and the ARIES idea
- [concept] Recovery: analysis → redo → undo
- [pitfall] `fsync` disabled → silent durability loss

### Topic: Backup & High Availability (backup-ha, intermediate)
Keeping data safe and the service up.
- [compare] Full / incremental / differential backups
- [concept] RPO vs RTO
- [concept] Point-in-time recovery via WAL archiving
- [concept] Failover, standby replicas, and health checks
- [pitfall] Backups that were never test-restored

### Topic: Database Security & Tuning (security-tuning, intermediate)
Access control and day-to-day performance.
- [concept] AuthN/Z, roles, row-level security
- [concept] Encryption at rest and in transit
- [concept] SQL injection and parameterized queries
- [concept] Connection pooling; N+1 query problem
- [pitfall] Over-privileged application DB accounts
- [code] Parameterized query vs string concatenation

## Group: Data Warehousing & OLAP (data-warehousing)

### Topic: OLTP vs OLAP (oltp-vs-olap, beginner)
Two workloads that pull design in opposite directions.
- [compare] Transactional vs analytical access patterns
- [concept] Why row-store suits OLTP, column-store suits OLAP
- [diagram] The path from OLTP sources into a warehouse
- [concept] Data warehouse vs data lake vs lakehouse
- [pitfall] Running heavy analytics on the OLTP primary

### Topic: Dimensional Modeling (dimensional-modeling, intermediate)
The warehouse modeling technique interviewers ask about.
- [concept] Facts vs dimensions; grain
- [diagram] Star schema vs snowflake schema
- [concept] Slowly changing dimensions (Type 1/2/3)
- [compare] Star (denormalized) vs snowflake (normalized)
- [pitfall] Wrong/ambiguous fact-table grain

### Topic: Columnar Storage & OLAP Operations (columnar-olap, advanced)
Why analytics engines are fast.
- [concept] Columnar layout, compression, vectorized scans
- [diagram] Row-store vs column-store on disk
- [concept] OLAP cube ops: roll-up, drill-down, slice/dice
- [concept] Partition pruning and predicate pushdown
- [pitfall] Point lookups/updates on a column store
- [concept] Note: ETL/ELT pipelines — see Area 11 (data-engineering)

---

## Cross-links & overlap notes
- **CAP/consistency/replication/sharding** here cover the *DB-internal* view; the *architecture* view (choosing them in a design) lives in Area 7 System Design (`consistency-replication`, `storage-scale`). Cross-link, don't duplicate.
- **ETL/ELT, stream ingestion, big-data frameworks** belong to Area 11 (`data-engineering`); this area only touches ETL as a one-slide bridge under Data Warehousing.
- **SQL injection / DB encryption** overlap Area 13 Security — kept here as the DB-practitioner view; deep appsec stays in Security.
- **Concurrency/locking/deadlocks** parallel OS concepts (Area 3) but are taught here in the transaction context; reference, don't re-teach.

**TOTALS: 11 groups, 48 topics, 366 slides.**
