# Area: Data Engineering & Big Data (data-engineering)

Reference outline for human review — expands each Group from `briefs/area-group-map.md` two levels: Topics (L2), then a slide outline (L3) per Topic. Groups and names are taken verbatim from `## Area 11 — Data Engineering & Big Data`. Nothing here is final; trim/merge before this goes to `AUTHORING.md`-driven generation.

---

## Group: Data Engineering Fundamentals (de-fundamentals)
*Scope: pipelines, OLTP vs OLAP, formats.*

### Topic: The Data Engineer's Job (data-engineering-role, beginner)
What a data engineer actually owns end-to-end, and how the role differs from adjacent ones.
- Concept: What a data engineer actually builds and owns
- Compare: Data Engineer vs Data Scientist vs Analytics Engineer
- Diagram: The modern data stack, source to dashboard
- Concept: The data engineering lifecycle (generate → ingest → store → transform → serve)
- Concept: Reliability, not just pipelines — SLAs, on-call, data as a product
- Pitfall: "More tools" is not the same as "more value"
- Concept: Undercurrents — security, DataOps, orchestration, software-engineering discipline
- Compare: Batch-oriented vs product-embedded data engineering roles

### Topic: OLTP vs OLAP (oltp-vs-olap, beginner)
Why transactional and analytical systems are built differently, and what breaks when you conflate them.
- Concept: Transactional workloads — many small reads/writes, row-at-a-time
- Concept: Analytical workloads — few large scans, column-at-a-time
- Diagram: Row store vs column store layout on disk
- Compare: OLTP vs OLAP — schema shape, query shape, latency, hardware profile
- Concept: Why running analytics on a production OLTP DB causes outages
- Concept: HTAP — the attempt to blend both, and its real limits
- Pitfall: Normalizing an OLAP warehouse "because that's correct" and paying for it in joins
- Code: The same business question, an OLTP-shaped query vs an OLAP-shaped query

### Topic: Pipeline Architecture Patterns (pipeline-architecture, beginner)
The reference shape of a data pipeline and where each stage's responsibilities begin and end.
- Diagram: Source → Ingestion → Storage → Transform → Serving, end to end
- Concept: Ingestion — pull vs push, batch vs streaming sources
- Concept: Raw / staging / curated layering (medallion-style bronze/silver/gold)
- Concept: Why you keep raw data even after transforming it
- Compare: ETL-first vs ELT-first architecture
- Concept: Push-down compute — doing transforms where the data already lives
- Pitfall: Skipping the staging layer and transforming straight from source
- Diagram: A concrete pipeline — Postgres CDC → object storage → Spark → warehouse → BI
- Concept: Data contracts as the seams between stages

### Topic: File Formats & Storage Layout (file-formats-and-storage, intermediate)
How CSV/JSON/Avro/Parquet/ORC differ and which to pick for a given access pattern.
- Concept: Row-oriented vs column-oriented file formats, at a glance
- Compare: CSV/JSON vs Avro vs Parquet vs ORC — write pattern, splittability, schema support
- Concept: Splittability — why a single gzip-compressed CSV breaks distributed parallel reads
- Concept: Schema-carrying formats (Avro/Parquet) vs schema-less (CSV/JSON)
- Pitfall: Picking JSON for a 500GB analytical dataset because it's "easy to read"
- Concept: When row-oriented (Avro) beats columnar — write-heavy, full-row-read workloads
- Code: Inspecting a Parquet file's footer to confirm schema, codec, and row count
- Concept: Format choice is the first lever, before any warehouse-level tuning (cross-link → Columnar Storage Internals, Warehousing & Lakes group, for the engine-internals deep dive)

### Topic: Schema Evolution & Serialization (schema-evolution, intermediate)
How schemas change safely in a pipeline without breaking downstream consumers.
- Concept: Why schemas change — new fields, renamed fields, type changes
- Concept: Backward, forward, and full compatibility, defined precisely
- Diagram: A schema registry mediating producer/consumer compatibility checks
- Compare: Avro vs Protobuf vs JSON Schema for evolution support
- Concept: Safe changes (add optional field with default) vs breaking changes (remove/rename/retype)
- Pitfall: Adding a required field and breaking every existing consumer at once
- Code: An Avro schema evolving across two versions with a default value
- Concept: Handling schema drift from upstream sources you don't control

### Topic: Batch vs Streaming — Choosing an Approach (batch-vs-stream-tradeoffs, beginner)
A decision framework for when a pipeline should be batch, micro-batch, or streaming.
- Concept: Latency requirement as the first filter — minutes/hours vs seconds
- Compare: Batch vs micro-batch vs continuous streaming
- Concept: Cost and complexity scale with how "real-time" you demand
- Concept: Micro-batch as the pragmatic middle (most "real-time" pipelines are actually this)
- Pitfall: Building a streaming pipeline because it sounds impressive, not because latency requires it
- Concept: A decision checklist — freshness SLA, data volume, downstream consumer needs
- Diagram: The same use case (fraud detection) solved batch vs streaming, and why one wins

### Topic: The Modern Data Stack — Tool Landscape (data-stack-landscape, intermediate)
How the major tool categories fit together, as a map before going deep on each in later groups.
- Diagram: The modern data stack, layer by layer, with example tools per layer
- Concept: Ingestion tools (managed connectors) vs hand-rolled extraction
- Concept: Orchestrators as the pipeline's control plane
- Concept: Transformation in the warehouse (SQL/dbt-style) vs transformation in a cluster (Spark)
- Concept: Warehouses/lakehouses as the system of record for analytics
- Compare: "Buy" (managed SaaS) vs "build" (self-hosted) at each layer, and the real cost trade-off
- Pitfall: Adopting a big-data tool (Spark/Kafka) at a small-data scale "for the future"
- Concept: Where each later group in this curriculum fits into this map

---

## Group: Batch Processing & ETL (batch-etl)
*Scope: ETL/ELT, orchestration, idempotency.*

### Topic: ETL vs ELT (etl-vs-elt, beginner)
The shift from transform-before-load to transform-after-load, and when each still wins.
- Concept: Classic ETL — transform in a separate engine before loading
- Concept: ELT — load raw first, transform inside the warehouse
- Diagram: ETL pipeline shape vs ELT pipeline shape
- Concept: Why cheap cloud-warehouse compute made ELT the default
- Compare: ETL vs ELT — cost, flexibility, auditability, reprocessing
- Pitfall: Losing the raw data because a legacy ETL job only ever kept the transformed output
- Concept: When ETL still wins — redacting sensitive data before it ever lands, small-system simplicity

### Topic: Extraction Patterns (extraction-patterns, intermediate)
How to pull data out of a source system without breaking it or missing records.
- Concept: Full extraction — simplest, but doesn't scale with source size
- Concept: Incremental extraction by timestamp / high-watermark column
- Pitfall: Watermark extraction silently dropping late-arriving or backdated rows
- Concept: Extracting via API pagination — cursors, rate limits, idempotent retries
- Compare: Query-based extraction vs log-based extraction (preview of CDC)
- Concept: Extracting from scheduled file/exports drops — the naive but common case
- Code: An incremental extraction query using a high-watermark with a safety overlap window
- Concept: Handling deletes — the case incremental-by-timestamp extraction can't see

### Topic: Change Data Capture (change-data-capture, intermediate)
Capturing row-level inserts/updates/deletes from a source database's transaction log.
- Concept: Why query-based extraction can't reliably see deletes or every intermediate update
- Diagram: Log-based CDC — reading the database's write-ahead log/binlog, not its tables
- Concept: How connectors tail the WAL/binlog and emit change events
- Concept: The CDC event shape — before/after image, operation type, transaction metadata
- Compare: Log-based CDC vs trigger-based CDC vs polling
- Concept: CDC's coupling to source-DB internals — replication slots, log retention, failover
- Pitfall: A CDC connector falling behind until the source purges WAL segments it still needs
- Concept: Snapshot + streaming — bootstrapping initial state before tailing live changes
- Concept: Where captured changes go next — streaming into a log for downstream consumers (cross-link → Kafka Deep Dive, Stream Processing group)

### Topic: Transformation Patterns & dbt-Style Modeling (transform-patterns-dbt, intermediate)
Modeling transformations as a version-controlled, tested DAG of SQL inside the warehouse.
- Concept: Transformation as a DAG of SQL models, not ad hoc scripts
- Diagram: A model DAG — sources → staging → intermediate → marts
- Concept: Materializations — view vs table vs incremental vs ephemeral, and the cost/freshness trade-off
- Code: An incremental model with a merge/upsert strategy
- Concept: Testing transformations — not-null, unique, relationships, custom business-rule tests
- Concept: Documentation and lineage as a byproduct of the DAG, not extra work
- Pitfall: An incremental model silently drifting from what a full-refresh would produce
- Compare: Transform-in-warehouse (SQL/dbt) vs transform-in-cluster (Spark) — when each wins

### Topic: Workflow Orchestration (workflow-orchestration, intermediate)
Scheduling, sequencing, and recovering pipeline jobs as a dependency graph.
- Concept: Why cron doesn't scale — no dependency awareness, no retries, no visibility
- Diagram: A pipeline as a DAG of tasks with upstream/downstream dependencies
- Concept: Scheduling models — fixed interval, data-driven/sensor-triggered, event-triggered
- Concept: Retries, timeouts, and alerting as first-class task properties
- Concept: Backfilling — re-running a DAG for a past date range
- Compare: Airflow-style vs Dagster-style vs Prefect-style orchestration — how each models data
- Pitfall: A DAG with a hidden circular dependency or an unbounded retry loop
- Concept: Task idempotency as a precondition for safe retries (cross-link → Idempotency & Backfills, this group)
- Concept: Sensors/deferrable tasks — waiting on an external event without wasting a worker slot

### Topic: Idempotency & Backfills (idempotency-and-backfills, advanced)
Designing batch jobs so re-running them is always safe, including for historical ranges.
- Concept: Idempotent vs non-idempotent operations — append vs overwrite-partition vs upsert
- Pitfall: A retried job double-inserting rows because it only ever appended
- Concept: Partition overwrite as the standard idempotent pattern for batch jobs
- Code: An upsert (MERGE) that makes re-running a load safe
- Concept: Backfilling a date-partitioned table after a logic change
- Concept: The "reprocessing blast radius" — what downstream breaks when you backfill upstream
- Pitfall: Backfilling directly into a table that live dashboards are querying mid-run
- Concept: Exactly-once vs effectively-once in batch — why it's really about idempotent writes, not magic delivery
- Concept: Designing a job to be safely re-runnable for any historical date, not just "today"

### Topic: Pipeline Reliability & Testing (pipeline-reliability-testing, advanced)
Catching bad data and broken jobs before they reach a dashboard or a downstream team.
- Concept: What can fail in a pipeline — late data, schema drift, silent data loss, logic bugs
- Concept: Data quality checks as tests — freshness, volume, null-rate, distribution checks
- Diagram: Where checks sit in the DAG — after extraction, after each transform, before serving
- Concept: SLAs and alerting — what to page on vs what to just log
- Pitfall: A pipeline that "succeeds" (no errors) while silently loading zero rows
- Concept: Circuit-breaking a pipeline — halting downstream stages when an upstream check fails
- Compare: Testing a SQL/dbt model vs testing a Spark job vs testing an orchestrator DAG
- Concept: Observability as a cross-cutting concern (cross-link → Observability for Data Pipelines, Data Quality & Governance group)

---

## Group: Stream Processing (stream-processing)
*Scope: event time, windowing, exactly-once.*

### Topic: Streaming Fundamentals (streaming-fundamentals, beginner)
What makes unbounded data different, and the vocabulary the rest of the group builds on.
- Concept: Bounded (batch) vs unbounded (streaming) data
- Concept: Event time vs processing time vs ingestion time
- Diagram: An event's journey — produced, transported, processed, with time gaps at each hop
- Concept: Delivery guarantees — at-most-once, at-least-once, exactly-once, defined precisely
- Concept: Throughput vs latency as the core streaming trade-off
- Pitfall: Assuming events arrive in the order they were produced
- Concept: Why "streaming" doesn't mean "instant" — there's always some latency budget
- Concept: The stream-processing building blocks — source, processing, sink, state

### Topic: Event Time, Watermarks & Late Data (event-time-watermarks, intermediate)
How streaming systems reason about "done" when events arrive out of order.
- Concept: Why processing-time-only logic gives wrong answers for out-of-order data
- Concept: Watermarks — the system's estimate of "no earlier event-time data is coming"
- Diagram: A watermark advancing through a stream of out-of-order events
- Concept: Trade-off — a tighter watermark is faster but drops more late data
- Concept: Handling late-arriving events — allowed lateness, side outputs, updating results
- Pitfall: A slow upstream partition stalling the watermark for the entire pipeline
- Code: Configuring allowed lateness and a late-data side output in a windowed aggregation
- Concept: Idle sources and watermark stalls — the partition that never sends anything

### Topic: Windowing Strategies (windowing-strategies, intermediate)
Grouping unbounded events into finite chunks for aggregation.
- Concept: Why you must window an unbounded stream before aggregating it
- Diagram: Tumbling vs sliding vs session windows, drawn on a timeline
- Concept: Tumbling windows — fixed, non-overlapping intervals
- Concept: Sliding windows — overlapping intervals, and the cost of overlap
- Concept: Session windows — gap-based, activity-driven boundaries
- Code: A sessionization query grouping clicks into user sessions with a gap timeout
- Compare: Choosing a window type for a concrete metric (5-min QPS vs per-session revenue)
- Pitfall: A sliding window's output volume exploding because the slide interval is too small

### Topic: Stateful Stream Processing (stateful-stream-processing, advanced)
How streaming engines maintain and recover state across unbounded runtime.
- Concept: Why aggregations, joins, and dedup all require state, not just per-event logic
- Diagram: A state store backing a running aggregation, checkpointed periodically
- Concept: Checkpointing — snapshotting state so a crashed job resumes instead of restarting
- Concept: State backends — in-memory vs disk-backed, and the size trade-off
- Concept: Stream-stream joins needing state on both sides within a time bound
- Pitfall: Unbounded state growth from a join or dedup window with no expiry
- Concept: Recovery — replaying from the last checkpoint plus the source's committed offset
- Concept: State TTL/retention as a required design decision, not an afterthought

### Topic: Exactly-Once Semantics (exactly-once-semantics, advanced)
What "exactly-once" really guarantees end-to-end, and how it's actually implemented.
- Concept: Why true exactly-once delivery across a network is effectively impossible — it's really "effectively-once"
- Concept: Idempotent producers — deduplicating retried writes at the source
- Concept: Transactional writes — atomically committing processed offsets together with output
- Diagram: A read-process-write cycle wrapped in a transaction spanning source offset and sink
- Compare: At-least-once + idempotent sink vs true transactional exactly-once
- Pitfall: Calling a pipeline "exactly-once" when the sink itself isn't idempotent or transactional
- Concept: The cost of exactly-once — throughput and latency overhead of transactions
- Concept: When at-least-once is actually the right (cheaper) choice

### Topic: Kafka Deep Dive (kafka-deep-dive, intermediate)
The log-based architecture underneath most streaming pipelines, and its operational model.
- Concept: The log abstraction — an append-only, ordered, partitioned commit log
- Diagram: Topics, partitions, and how producers/consumers map onto them
- Concept: Partitioning strategy and why key choice determines ordering guarantees
- Concept: Consumer groups — how partitions split across consumers for parallelism
- Concept: Offsets and offset commits — at-least-once by default, exactly-once with transactions
- Concept: Replication — leader/follower partitions, in-sync replicas, durability guarantees
- Pitfall: Too few partitions capping consumer parallelism; too many hurting broker performance
- Code: A consumer-group rebalance triggered by a new consumer joining
- Concept: Retention — time/size-based expiry, and log compaction as an alternative to deletion

### Topic: Stream Processing Engines Compared (stream-processing-engines-compare, intermediate)
Choosing between the major engines for a given latency and complexity target.
- Compare: Micro-batch vs true per-event engines — execution model
- Concept: Micro-batch processing — batches of the stream on a fixed interval
- Concept: Continuous/per-event processing — lower latency floor, different fault-tolerance cost
- Concept: Library-embedded stream processing vs a dedicated cluster
- Compare: Latency floors and throughput ceilings across the approaches
- Pitfall: Reaching for the lowest-latency engine for a job a scheduled batch model would have solved more simply
- Concept: Ecosystem fit — shared batch+stream code, lowest latency, or embedding in a service (cross-link → Spark Architecture, Big Data Frameworks group)

### Topic: Streaming Architecture Patterns — Lambda & Kappa (streaming-architecture-patterns, advanced)
The two dominant ways teams combine batch and streaming for correctness plus speed.
- Diagram: Lambda architecture — parallel batch and speed layers merged at serving
- Concept: Why Lambda exists — batch for correctness, streaming for freshness, before streaming engines matured
- Pitfall: Maintaining the same business logic twice (batch job + streaming job) and having them drift
- Diagram: Kappa architecture — a single streaming pipeline reprocesses history by replay
- Concept: Kappa's precondition — a log with enough retention to replay from, and a fast-enough engine
- Compare: Lambda vs Kappa — operational cost, consistency, when each is still justified
- Concept: Modern middle ground — one engine running the same code in batch and streaming mode

---

## Group: Data Warehousing & Lakes (warehousing-lakes)
*Scope: warehouse/lake/lakehouse, columnar.*

### Topic: Data Warehouse Fundamentals (warehouse-fundamentals, beginner)
What makes a warehouse architecturally different from an application database.
- Concept: MPP (massively parallel processing) — spreading a query across many nodes
- Diagram: A query fanning out across worker nodes and re-aggregating
- Concept: Columnar storage as the warehouse default, and why (cross-link → Columnar Storage Internals, this group)
- Concept: Separation of storage and compute in modern cloud warehouses
- Concept: Why warehouses scale and charge differently from OLTP databases
- Pitfall: Expecting warehouse queries to have OLTP-like point-lookup latency
- Concept: The warehouse's role as the single source of truth for analytics

### Topic: Columnar Storage Internals (columnar-storage-internals, intermediate)
The on-disk techniques that make analytical scans fast and cheap.
- Concept: Column-per-chunk layout vs row-per-record layout
- Diagram: A columnar file's row groups, column chunks, and per-column stats
- Concept: Compression — dictionary encoding, run-length encoding, delta encoding
- Concept: Predicate pushdown using min/max stats to skip entire row groups
- Concept: Column pruning — reading only the columns a query touches
- Code: Why `SELECT col FROM t` reads a fraction of the bytes `SELECT *` does
- Pitfall: A wide table with hundreds of rarely-used columns quietly bloating storage and scan cost
- Concept: Late materialization — filtering before reconstructing full rows

### Topic: Data Lakes (data-lakes, beginner)
Storing raw data cheaply at scale before deciding how it'll be modeled.
- Concept: Object storage as the substrate — cheap, durable, schema-less
- Concept: Schema-on-read vs schema-on-write
- Diagram: A data-lake layout — raw/bronze, cleaned/silver, curated/gold zones
- Compare: Data lake vs data warehouse — cost, flexibility, query performance, governance
- Pitfall: The "data swamp" — a lake with no lineage, ownership, or quality controls
- Concept: Why lakes historically lacked the ACID guarantees warehouses took for granted
- Concept: What a lake is good at that a warehouse isn't — unstructured data, ML training sets

### Topic: Lakehouse Table Formats (lakehouse-table-formats, advanced)
How Iceberg/Delta/Hudi-style table formats bring warehouse-grade guarantees to lake storage.
- Concept: The lakehouse pitch — warehouse features (ACID, schema enforcement) directly on lake files
- Diagram: A table format's metadata layer sitting above plain columnar files
- Concept: ACID transactions on object storage via atomic metadata-pointer swaps
- Concept: Time travel — querying a table as of a past snapshot or version
- Concept: Schema evolution and enforcement at the table-format layer
- Compare: The major open table formats — metadata model and ecosystem fit
- Concept: Compaction — merging small files produced by frequent streaming writes
- Pitfall: Small-file explosion from high-frequency micro-batch writes, and its query-time cost
- Concept: Concurrent writers and optimistic concurrency control at the metadata layer

### Topic: Warehouse Platforms Compared (warehouse-platforms-compare, intermediate)
The architectural choices behind the major cloud warehouses and what they mean in practice.
- Compare: The major cloud warehouses — storage/compute separation model
- Concept: Independently scalable compute clusters on shared storage
- Concept: Serverless query models — no cluster sizing, pay per query/storage
- Concept: Fixed-cluster models and their closer kinship to traditional MPP
- Concept: Concurrency scaling — how platforms handle bursts of simultaneous queries
- Pitfall: Porting a schema designed for one platform's cost model straight into another's
- Concept: Choosing a platform based on workload shape, not benchmark headlines

### Topic: Partitioning & Clustering for Query Performance (partitioning-clustering, intermediate)
Physically organizing warehouse tables so common queries scan less data.
- Concept: Partitioning — splitting a table by a column (commonly date) into separate physical units
- Diagram: A date-partitioned table and a query that prunes to one partition
- Concept: Clustering/sort keys — ordering data within partitions for range-filter efficiency
- Code: A query whose WHERE clause does or doesn't align with the partition key, and the cost difference
- Pitfall: Over-partitioning — thousands of tiny partitions hurting metadata overhead more than they help
- Concept: Choosing a partition key — cardinality, query patterns, data skew
- Concept: Storage-layer partitioning vs compute-layer shuffle partitioning — same word, different layer (cross-link → Partitioning & Shuffle in Distributed Compute, Big Data Frameworks group)

### Topic: Warehouse Cost & Performance Optimization (warehouse-cost-performance, advanced)
The levers for making warehouse workloads faster and cheaper in production.
- Concept: Where warehouse cost actually comes from — bytes scanned, compute time, storage
- Concept: Materialized views — precomputing expensive aggregates
- Concept: Caching layers — result cache vs data cache, and their invalidation triggers
- Pitfall: A `SELECT *` in a dashboard query scanning terabytes to render three columns
- Concept: Query pruning via partitioning/clustering as the highest-leverage cost lever
- Concept: Right-sizing compute — auto-suspend/auto-scale vs always-on clusters
- Concept: Monitoring cost — attributing spend to teams/queries for accountability

---

## Group: Analytics Data Modeling (analytics-modeling)
*Scope: star/snowflake, slowly-changing dims.*

### Topic: Dimensional Modeling Basics (dimensional-modeling-basics, beginner)
The fact/dimension vocabulary that all analytics modeling builds on.
- Concept: Facts (measurements/events) vs dimensions (descriptive context)
- Concept: Grain — the single most important decision in a fact table's design
- Diagram: A simple sales fact surrounded by product/customer/date dimensions
- Concept: Why analytics modeling denormalizes on purpose — the deliberate opposite of OLTP normalization (cross-link → Area 2 Databases, Data Modeling & Normalization group)
- Pitfall: Mixing two grains in one fact table (e.g. order-level and line-item-level rows together)
- Concept: Conformed dimensions — one shared customer/date dimension reused across many fact tables

### Topic: Star Schema vs Snowflake Schema (star-vs-snowflake-schema, intermediate)
The two classic dimensional layouts and the real trade-off between them.
- Diagram: Star schema — one fact table, denormalized dimensions radiating out
- Diagram: Snowflake schema — dimensions further normalized into sub-dimensions
- Compare: Star vs snowflake — query simplicity/speed vs storage and update efficiency
- Concept: Why columnar warehouses mostly favor star — joins are cheap, repeated text storage is cheap
- Pitfall: Snowflaking a dimension "for normalization purity" and adding avoidable joins to every query
- Concept: When snowflaking still earns its keep — huge, slowly-changing sub-dimensions reused widely
- Code: The same report query written against a star vs a snowflake layout

### Topic: Slowly Changing Dimensions (slowly-changing-dimensions, intermediate)
How dimension attributes are tracked as they change over time.
- Concept: The problem — a customer's address/tier changes, but old facts should still see the old value
- Concept: SCD Type 1 — overwrite, no history kept
- Concept: SCD Type 2 — new row per change, with effective-date ranges and a current-flag
- Diagram: A Type 2 dimension table showing the same customer across three historical rows
- Code: A merge statement implementing Type 2 history tracking
- Concept: SCD Type 3 — limited history via "previous value" columns
- Compare: Type 1 vs 2 vs 3 — when each is the right, cheapest choice
- Pitfall: Joining facts to the *current* dimension row instead of the *effective-at-the-time* row, rewriting history by accident

### Topic: Fact Table Design (fact-table-design, intermediate)
Choosing grain and measure types so a fact table aggregates correctly.
- Concept: Additive measures — safely summable across any dimension (e.g. revenue)
- Concept: Semi-additive measures — summable across some dimensions, not others (e.g. account balance across time)
- Concept: Non-additive measures — ratios/percentages that must be recomputed, never summed
- Pitfall: Summing a semi-additive balance across time periods and getting a meaningless number
- Concept: Factless fact tables — recording that an event happened with no numeric measure
- Concept: Transaction, periodic-snapshot, and accumulating-snapshot fact table types
- Diagram: An accumulating-snapshot fact table updated as an order moves through its lifecycle

### Topic: One Big Table vs Star Schema (obt-vs-star-schema, advanced)
The modern debate between wide denormalized tables and classic dimensional modeling.
- Concept: The "One Big Table" (OBT) pattern — pre-joining everything into a single wide table
- Concept: Why cheap columnar storage and compute made OBT viable at scale
- Compare: OBT vs star schema — query simplicity vs update cost and storage duplication
- Pitfall: An OBT that must be fully rebuilt whenever any one upstream source changes
- Concept: Where OBT wins — BI-tool simplicity, ML feature tables, avoiding join mistakes by non-experts
- Concept: Where star schema still wins — many fact tables sharing dimensions, update efficiency
- Concept: Hybrid reality — star schema in the warehouse, OBT materialized for specific consumers

### Topic: Semantic & Metrics Layer (semantic-metrics-layer, advanced)
Defining a metric once so every tool and team computes it the same way.
- Concept: The problem — five dashboards, five slightly different definitions of "active user"
- Concept: A metrics layer as a single, version-controlled definition of each metric
- Diagram: BI tools and notebooks all querying through one semantic layer instead of raw tables
- Concept: Metric primitives — measure, dimension, grain, and how they compose
- Compare: A headless BI/metrics layer vs each BI tool defining its own metrics
- Pitfall: A metric redefined slightly differently in a new dashboard, silently disagreeing with the "official" number

---

## Group: Big Data Frameworks (big-data-frameworks)
*Scope: MapReduce, Spark, partitioning.*

### Topic: MapReduce & the Hadoop Legacy (mapreduce-hadoop, beginner)
The model that started distributed batch processing, and why it was superseded.
- Concept: The MapReduce model — map, shuffle, reduce, expressed simply
- Diagram: A word-count job traced through map, shuffle, and reduce stages
- Concept: HDFS — blocks, replication, and its NameNode/DataNode roles
- Concept: Data locality — moving compute to the data, not the reverse
- Pitfall: Every MapReduce stage round-tripping through disk, making iterative jobs painfully slow
- Concept: Why an in-memory execution model displaced MapReduce for most new work
- Concept: Where Hadoop/HDFS-era ideas still show up today

### Topic: Spark Architecture (spark-architecture, intermediate)
How a Spark job is planned and executed across a cluster.
- Diagram: Driver, cluster manager, and executors, with tasks distributed across executors
- Concept: RDDs — the original distributed, partitioned, fault-tolerant abstraction
- Concept: Lazy evaluation — transformations build a plan, actions trigger execution
- Diagram: A job broken into stages at each shuffle boundary, and stages into tasks per partition
- Concept: In-memory caching between stages as the core speed advantage over disk-bound MapReduce
- Concept: Fault tolerance via lineage — recomputing lost partitions instead of replicating everything
- Pitfall: Calling a full-collect action on a huge dataset and blowing up the driver's memory
- Code: A transformation chain and the physical plan it triggers on an action

### Topic: Spark DataFrames & the Catalyst Optimizer (spark-dataframes-catalyst, intermediate)
The structured API layer that lets Spark optimize your job before running it.
- Concept: DataFrames/Datasets as structured, schema-aware RDDs
- Concept: Why the DataFrame API lets Spark optimize in ways raw RDD code can't
- Diagram: The optimizer's phases — logical plan, optimized logical plan, physical plan
- Concept: Predicate and projection pushdown into the optimized plan
- Concept: Off-heap memory management and whole-stage code generation
- Code: Reading a query's physical plan (`.explain()`) to see pushdown in action
- Compare: RDD API vs DataFrame API — when you still drop down to RDDs
- Pitfall: A user-defined function silently disabling the optimizer's rewrites

### Topic: Partitioning & Shuffle in Distributed Compute (partitioning-and-shuffle, advanced)
Why data movement across the network, not computation, is usually the real bottleneck.
- Concept: What a shuffle is — redistributing data across the cluster by key
- Diagram: A groupBy triggering a shuffle — map-side write, network transfer, reduce-side read
- Concept: Why shuffles are expensive — disk I/O, network, and serialization all at once
- Concept: Data skew — one key holding far more data than the rest, stalling one task
- Concept: Salting — splitting a hot key into sub-keys to spread skewed load
- Pitfall: A single straggler task from a skewed key making the whole stage look "stuck"
- Code: Detecting skew from a job UI's per-task duration distribution
- Concept: Partition-count tuning — too few underutilizes the cluster, too many adds overhead

### Topic: Distributed Joins at Scale (distributed-joins-at-scale, advanced)
How a join executes across a cluster, and which strategy to force when the planner guesses wrong.
- Concept: Shuffle (sort-merge) join — both sides shuffled by join key, then merged
- Concept: Broadcast hash join — the small side sent whole to every executor, no shuffle needed
- Diagram: Broadcast join vs shuffle join, side by side
- Concept: How the optimizer chooses — size thresholds and table statistics
- Pitfall: A stale table statistic causing the optimizer to shuffle-join when it should have broadcast
- Concept: Skewed join keys and the salting/isolated-key techniques to handle them
- Code: Forcing a broadcast hint on a join the optimizer mis-sized
- Concept: Joining many small dimension tables — why order and broadcast choice compound

### Topic: Spark Performance Tuning (spark-performance-tuning, advanced)
The concrete levers for diagnosing and fixing a slow Spark job.
- Concept: Reading a job's execution UI — stages, tasks, and where time actually goes
- Concept: Caching/persisting a dataset reused across multiple actions
- Concept: Adaptive query execution — runtime replanning based on actual data sizes
- Concept: Spill — when data exceeds executor memory and lands on disk mid-shuffle
- Pitfall: Over-partitioning "just in case" and drowning the cluster in scheduling overhead
- Concept: Executor sizing — cores/memory per executor vs number of executors
- Compare: Wide vs narrow transformations and why only wide ones force a shuffle
- Concept: Common wins — filter/project early, avoid UDFs where a built-in exists, broadcast small tables

### Topic: Cluster Resource Management (cluster-resource-management, intermediate)
How a Spark job actually gets machines, and what changes across cluster managers.
- Concept: The cluster manager's job — allocating executors to a submitted application
- Compare: Standalone vs YARN vs Kubernetes as a Spark cluster manager
- Concept: Static vs dynamic allocation — fixed executor count vs scaling with workload
- Diagram: A Spark job requesting executors from Kubernetes as pods
- Pitfall: Dynamic allocation fighting a shared cluster's other tenants for resources
- Concept: Resource requests/limits and why under-provisioning causes OOM-killed executors (cross-link → Area 10 Cloud, DevOps & SRE, Kubernetes & Orchestration group, for the general k8s model)
- Concept: Queueing and fair-share scheduling across multiple concurrent jobs

---

## Group: Data Quality & Governance (data-governance)
*Scope: lineage, contracts, quality checks.*

### Topic: Data Quality Fundamentals (data-quality-fundamentals, beginner)
The dimensions of "bad data" and how to turn them into automated checks.
- Concept: The core dimensions — accuracy, completeness, timeliness, uniqueness, consistency
- Concept: Turning each dimension into a concrete, automatable check
- Diagram: Quality checks placed at pipeline boundaries — on ingest, after transform, before serving
- Code: A not-null / uniqueness / referential-integrity test on a warehouse table
- Pitfall: A pipeline that "ran successfully" while silently loading half the expected rows
- Concept: Statistical checks — row-count and distribution anomalies vs hard rule violations
- Concept: Deciding severity — what fails the pipeline vs what just gets flagged

### Topic: Data Contracts (data-contracts, intermediate)
Formal agreements between data producers and consumers so upstream changes don't silently break downstream.
- Concept: The problem — a producer changes a field and every downstream pipeline breaks with no warning
- Concept: A data contract as a schema-plus-semantics agreement, enforced like an API contract
- Diagram: A producer's CI pipeline validating a schema change against the contract before it ships
- Concept: What a contract specifies — schema, nullability, semantic meaning, SLAs (freshness, volume)
- Compare: Data contracts vs "monitor it and fix it after it breaks"
- Pitfall: A contract that only checks schema shape and misses a semantic change (e.g. currency units silently switching)
- Concept: Contracts as the mechanism that makes decentralized, team-owned data viable

### Topic: Data Lineage (data-lineage, intermediate)
Tracing where a piece of data came from and everywhere it went.
- Concept: Table-level lineage vs column-level lineage — what each answers
- Diagram: A lineage graph from a source table through transforms to a dashboard field
- Concept: Why lineage matters for impact analysis — "what breaks if I change this column?"
- Concept: Why lineage matters for incident debugging — "where did this bad number originate?"
- Concept: How lineage gets captured — static SQL parsing vs runtime execution tracking
- Pitfall: Manually documented lineage that goes stale the first time a pipeline changes
- Concept: Lineage as a prerequisite for trustworthy impact analysis before a breaking schema change

### Topic: Data Catalogs & Metadata Management (data-catalogs-metadata, intermediate)
Making data discoverable, owned, and understandable across a growing organization.
- Concept: The discovery problem — nobody can find, or trust, a dataset that isn't cataloged
- Concept: What a catalog holds — schema, owner, description, tags, usage stats, lineage
- Diagram: A catalog indexing the warehouse, lake, and BI tool side by side
- Concept: Ownership as metadata — who to ask, who gets paged when it breaks
- Pitfall: A catalog populated once at launch and never kept current, becoming actively misleading
- Concept: Automated metadata harvesting vs manually curated documentation
- Concept: Business glossaries — tying a technical column to the term the business actually uses

### Topic: Data Governance & Access Control (data-governance-access-control, advanced)
Controlling who can see and use which data, and staying compliant while doing it.
- Concept: Why governance is a data-engineering concern, not just a legal/compliance one
- Concept: PII classification — identifying sensitive columns systematically, not by memory
- Concept: Row-level and column-level security — the same table, different visible rows/columns per role
- Diagram: A masking policy applied at query time based on the querying user's role
- Concept: Data minimization and retention policies — deleting what you no longer have a reason to keep
- Compare: Anonymization vs pseudonymization vs tokenization for sensitive fields
- Pitfall: A "de-identified" dataset that's re-identifiable by joining it against a public dataset
- Concept: Compliance basics that shape pipeline design — right-to-deletion in an append-only warehouse

### Topic: Observability for Data Pipelines (data-pipeline-observability, advanced)
Knowing a pipeline is broken before a stakeholder says the dashboard looks wrong.
- Concept: The data-specific observability pillars — freshness, volume, schema, distribution
- Diagram: Monitors sitting on top of every table in the pipeline, not just infra metrics
- Concept: Freshness monitoring — alerting when a table hasn't updated within its expected cadence
- Concept: Volume anomaly detection — row counts that spike or drop outside a normal band
- Compare: Data observability (table-level signals) vs infra observability (cross-link → Area 10 Cloud, DevOps & SRE, Observability & Monitoring group — CPU/latency/logs; complementary, not duplicative)
- Pitfall: An infra dashboard showing all-green while a silent upstream logic bug corrupts every row
- Concept: Alert routing and ownership — who actually gets paged when a table goes stale
- Concept: Closing the loop — observability findings feeding back into data contracts and quality checks

---

## Cross-links & overlap notes

- **CDC ↔ Kafka.** *Change Data Capture* (Batch & ETL) produces events that typically stream through a log; the log's own mechanics (partitions, consumer groups, offsets) are owned once by *Kafka Deep Dive* (Stream Processing) and referenced, not repeated.
- **Idempotency ↔ Exactly-once.** *Idempotency & Backfills* (Batch & ETL) covers safe batch job re-runs (upserts, partition overwrite); *Exactly-Once Semantics* (Stream Processing) covers continuous-delivery guarantees (idempotent producers, transactional writes). Same word, deliberately distinct mechanisms — kept as separate Topics.
- **File formats ↔ columnar internals.** *File Formats & Storage Layout* (Fundamentals) stops at "which format to pick and why"; *Columnar Storage Internals* (Warehousing & Lakes) owns the engine-level depth (encodings, predicate pushdown, column pruning). No content duplicated between them.
- **Partitioning, two meanings.** *Partitioning & Clustering* (Warehousing & Lakes) is storage-layer (physical table layout for query pruning). *Partitioning & Shuffle* (Big Data Frameworks) is compute-layer (in-flight shuffle partitioning during a distributed job). Same term, different layer — both legitimate, cross-referenced so a reviewer doesn't mistake one for a duplicate of the other.
- **Spark internals ↔ engine comparison.** *Stream Processing Engines Compared* (Stream Processing) only compares engines at a summary level; the deep Spark-specific internals (architecture, Catalyst, shuffle, joins, tuning) live entirely in Big Data Frameworks and are cross-linked rather than restated.
- **Cluster resource management vs general infra.** *Cluster Resource Management* (Big Data Frameworks) is scoped strictly to Spark's executor/resource model; general Kubernetes/cloud-infra mechanics belong to Area 10 (Cloud, DevOps & SRE) and are not repeated here.
- **Data-pipeline observability vs infra observability.** *Observability for Data Pipelines* (Data Quality & Governance) is scoped to data-specific signals (freshness/volume/schema/distribution), distinct from and complementary to Area 10's infra observability and Area 7's system-design observability — same naming pattern flagged in `area-group-map.md`, resolved here for Area 11's angle.
- **Dimensional modeling vs relational normalization.** *Dimensional Modeling Basics* (Analytics Data Modeling) is the deliberate denormalized counterpart to Area 2 (Databases) → *Data Modeling & Normalization*. Different purpose (OLAP read-optimized vs OLTP integrity-optimized), not overlapping, but a natural compare-and-contrast for a reviewer or a learner moving between the two areas.

## Totals
7 Groups · 48 Topics · 368 slides.

| Group | Topics | Slides |
|---|---|---|
| Data Engineering Fundamentals | 7 | 57 |
| Batch Processing & ETL | 7 | 58 |
| Stream Processing | 8 | 63 |
| Data Warehousing & Lakes | 7 | 52 |
| Analytics Data Modeling | 6 | 41 |
| Big Data Frameworks | 7 | 54 |
| Data Quality & Governance | 6 | 43 |
