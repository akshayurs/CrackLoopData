# HLD Case Studies — expanded (replaces `hld-case-studies`)

Restructures the single 10-topic `hld-case-studies` group into 5 domain-split groups covering
~40 end-to-end "design system X" case studies. The 10 original topics are preserved verbatim
(same slugs, same outlines unless noted) and redistributed into the group that fits them best.
Each case study cross-links the building-block groups it leans on instead of re-deriving them.

---

## Group: Core Systems (hld-cases-core)
*The fundamentals bank — small, self-contained systems that each isolate one hard distributed-systems problem.*

### Topic: Design a URL Shortener (design-url-shortener, beginner)
The classic first system design problem — encoding, redirection, and a cache in front of a hot mapping table.
- Clarifying requirements: read/write ratio, custom aliases, expiry (concept)
- Back-of-envelope: estimating QPS and storage for billions of URLs (concept)
- Diagram: high-level architecture — API, encoder, DB, cache, redirect path (diagram)
- Encoding strategy: base62 counter vs hash-based short codes (concept)
- Compare: counter-based vs hash-based ID generation — collisions, predictability (compare)
- Database choice and schema for the mapping table (concept)
- Caching the hot redirects (concept)
- Handling custom aliases and collision retries (concept)
- Diagram: full request flow for create + redirect, with cache (diagram)
- Pitfall: using an auto-increment ID directly as the short code (pitfall)
- Interview: the follow-ups — analytics, expiry, abuse prevention (interview)

### Topic: Design a Pastebin (design-pastebin, beginner)
Storing and serving arbitrary-size text blobs cheaply, including the read stampede when one paste goes viral.
- The prompt: paste text, get a shareable link, set expiry/visibility (overview)
- Functional & non-functional requirements: size limits, retention, public vs unlisted (concept)
- Back-of-envelope: paste sizes, read:write ratio, storage growth over a year (concept)
- The API surface: create paste, fetch paste, delete/expire (concept)
- Data model: blob storage for content vs a small metadata row per paste (compare)
- Diagram: high-level architecture — API, object store, metadata DB, cache (diagram)
- Why this isn't just a URL shortener: variable-size payloads change the storage answer (concept)
- Handling a viral paste: read stampede on one hot key (concept)
- Diagram: cache-aside in front of the hot paste, with request coalescing (diagram)
- Expiry at scale: TTL sweep vs lazy deletion on read (compare)
- Pitfall: storing every paste inline in the DB row, bloating the primary store (pitfall)
- Interview: the follow-ups — syntax highlighting, private pastes, abuse/rate limits (interview)
— cross-link: object-and-blob-storage, cache-penetration-and-negative-caching

### Topic: Design a Unique ID Generator (design-unique-id-generator, intermediate)
Generating unique, roughly-sortable IDs across many machines without a central bottleneck.
- Why auto-increment IDs break down in a distributed system (concept)
- UUID: simplicity vs its cost (index locality, size) (compare)
- Snowflake-style IDs: timestamp + machine ID + sequence (concept)
- Diagram: anatomy of a 64-bit Snowflake ID (diagram)
- Clock drift and the coordination problem across machines (concept)
- Compare: centralized ID service vs decentralized generation (compare)
- Code: a simplified Snowflake ID generator (code)
- Pitfall: two machines assigned the same machine ID, generating collisions (pitfall)
- Interview: "Design a service that generates unique IDs at scale" (interview)

### Topic: Design a Key-Value Store (design-key-value-store, advanced)
Building a Dynamo-style KV store itself — partitioning, replication, and tunable consistency, not just using one.
- The prompt: put(key, value)/get(key) at massive scale with high availability (overview)
- Functional & non-functional requirements: durability, availability vs consistency target (concept)
- Back-of-envelope: keyspace size, request rate, replication factor and its storage multiplier (concept)
- The API surface: put/get/delete, and what a versioned value looks like (concept)
- Data model: consistent hashing ring for partitioning keys across nodes (concept)
- Diagram: the hash ring with virtual nodes and key ownership (diagram)
- Replication: writing to N replicas and reading from R with quorum (concept)
- Diagram: a write's path across the ring — coordinator, replicas, acks (diagram)
- Tunable consistency: read-your-writes vs eventual, and the R/W/N knobs (compare)
- Conflict resolution when replicas diverge: vector clocks vs last-write-wins (compare)
- The bottleneck: hot partitions from skewed key access (concept)
- Pitfall: rebalancing the ring naively, causing a mass key migration (pitfall)
- Interview: "Design a distributed key-value store like DynamoDB" (interview)
— cross-link: partitioning-and-sharding, quorum-systems, consensus-basics

### Topic: Design a Distributed Cache (design-distributed-cache, advanced)
A cache that is itself a distributed system — sharding, invalidation propagation, and the hot-key problem at cluster scale.
- The prompt: a shared cache tier in front of a database, serving many services (overview)
- Functional & non-functional requirements: hit ratio target, staleness tolerance, eviction policy (concept)
- Back-of-envelope: working-set size vs node memory, number of shards needed (concept)
- The API surface: get/set/delete plus TTL and versioned invalidation (concept)
- Sharding keys across cache nodes with consistent hashing (concept)
- Diagram: client routing to the right shard, with a hash ring (diagram)
- Cache invalidation across nodes: TTL vs explicit invalidation broadcast (compare)
- The hot-key problem: one key exceeding a single node's capacity (concept)
- Diagram: hot-key mitigation — local caching plus key-splitting in front of the shard (diagram)
- Node failure and rebalancing without a stampede on the database (concept)
- Pitfall: a full cache-cluster restart causing a thundering herd on the DB (pitfall)
- Interview: "Design Memcached/Redis Cluster from scratch" (interview)
— cross-link: distributed-caching, cache-invalidation, eviction-policies

### Topic: Design a Rate Limiter Service (design-rate-limiter-service, advanced)
Rate limiting as a shared, low-latency service every other system calls — the distributed service around the algorithm, not the algorithm itself.
- The prompt: a central service any microservice can ask "is this allowed?" (overview)
- Functional & non-functional requirements: per-user/per-API limits, latency budget, config changes without redeploy (concept)
- Back-of-envelope: check QPS across all callers vs the limiter's own capacity (concept)
- The API surface: checkAndIncrement(key, limit, window) (concept)
- Data model: where counters live — in-memory per node vs a shared store (compare)
- Diagram: architecture — client SDK, limiter service, shared counter store (diagram)
- Sharing counters across limiter instances without a single point of contention (concept)
- Propagating limit-config changes globally with low delay (concept)
- Diagram: request path through the limiter under normal and overload conditions (diagram)
- The bottleneck: the shared counter store becoming hotter than the service it protects (concept)
- Trade-off: strict global accuracy vs relaxed per-node approximate limits (compare)
- Pitfall: the limiter itself becoming a single point of failure for every downstream call (pitfall)
- Interview: "Design a rate limiter usable by every service in the company" (interview)
— cross-link: distributed-rate-limiting, rate-limiting-algorithms

### Topic: Design a Leaderboard (design-leaderboard, intermediate)
Real-time ranked scores for millions of users — sorted-set structures and rank queries, not a sorted table scan.
- The prompt: show a user's rank and the top N out of millions of scores, updated live (overview)
- Functional & non-functional requirements: update frequency, rank-query latency, tie handling (concept)
- Back-of-envelope: score updates per second vs rank-read QPS (concept)
- The API surface: updateScore(user, delta), getRank(user), getTopN() (concept)
- Data model: sorted set (skip list) vs a B-tree index vs periodic batch ranking (compare)
- Diagram: a sharded sorted-set leaderboard with a merge step for global rank (diagram)
- Getting a user's rank in a sharded leaderboard without a full scan (concept)
- Tie-breaking rules and their effect on rank stability (concept)
- The bottleneck: a single global leaderboard node under write pressure (concept)
- Trade-off: exact real-time rank vs periodically refreshed approximate rank (compare)
- Pitfall: recomputing the full sorted order on every single score update (pitfall)
- Interview: "Design a real-time leaderboard for a game with 100M players" (interview)
— cross-link: nosql-data-models, partitioning-and-sharding

### Topic: Design a Distributed Counter (design-distributed-counter, advanced)
Counting billions of increments (views, likes) without turning one row into the system's hottest lock.
- The prompt: count events (views, likes) at a rate no single DB row can absorb (overview)
- Functional & non-functional requirements: exactness vs approximate-is-fine, read latency for the count (concept)
- Back-of-envelope: increments/sec on a single hot object vs a single row's write ceiling (concept)
- The API surface: increment(key), getCount(key) — and what "get" actually returns (concept)
- Sharded counters: splitting one logical counter into N physical shards (concept)
- Diagram: writes fan out to shards, reads sum across shards (diagram)
- In-memory batching before flushing to durable storage (concept)
- Compare: strongly consistent single-row counter vs eventually-consistent sharded counter (compare)
- The bottleneck: shard count vs read-time aggregation cost (concept)
- Approximate counting (HyperLogLog-style) when exact counts aren't required (concept)
- Pitfall: a "trending" counter read on every page view, redoing the sum each time (pitfall)
- Interview: "Design a view counter for a video that gets 10M views in an hour" (interview)
— cross-link: partitioning-and-sharding, eviction-policies

---

## Group: Social & Messaging Systems (hld-cases-social)
*Feed, chat, and graph systems — the hard problems are fan-out shape, ordering, and graph scale, not any single feature.*

### Topic: Design a News Feed (design-news-feed, advanced)
Fan-out-on-write vs fan-out-on-read, and the hybrid that survives the celebrity problem.
- Clarifying requirements: post, follow, feed read pattern (concept)
- Fan-out-on-write (push): precomputing every follower's feed (concept)
- Fan-out-on-read (pull): assembling the feed at read time (concept)
- Diagram: push vs pull fan-out side by side (diagram)
- The celebrity problem: why pure push breaks for high-follower accounts (concept)
- Hybrid fan-out: push for most, pull for celebrities (concept)
- Compare: push vs pull vs hybrid on latency, storage, write cost (compare)
- Ranking the feed: chronological vs relevance-ranked (concept)
- Diagram: end-to-end architecture — write path and read path (diagram)
- Pitfall: recomputing the entire feed on every read at Twitter scale (pitfall)
- Interview: the follow-ups — feed staleness, pagination, ranking signals (interview)
— cross-link: ml-system-design (ranking model itself lives there; this topic owns the fan-out architecture)

### Topic: Design a Chat System (design-chat-system, advanced)
Real-time delivery, per-conversation ordering, and presence at messaging-app scale.
- Clarifying requirements: 1:1 vs group chat, delivery guarantees, online presence (concept)
- Real-time delivery: WebSockets vs long polling vs push notifications (compare)
- Diagram: connection topology — clients, gateway servers, message store (diagram)
- Message storage and ordering per conversation (concept)
- Delivery and read receipts: tracking per-recipient state (concept)
- Online presence: heartbeat, last-seen, fan-out of status changes (concept)
- Group chat fan-out vs 1:1 delivery (compare)
- Diagram: message send path from sender to all recipients (diagram)
- Offline delivery: queuing for disconnected clients (concept)
- Pitfall: a single connection server becoming a hot spot for popular groups (pitfall)
- Interview: the follow-ups — end-to-end encryption, multi-device sync (interview)

### Topic: Design a Notification System (design-notification-system, intermediate)
Fanning a single event out across channels without spamming or ignoring user preferences.
- Clarifying requirements: channels (push/email/SMS), priority, user preferences (concept)
- Diagram: notification pipeline — trigger, template, channel dispatch (diagram)
- Fan-out for a notification that targets millions of users (concept)
- Deduplication and throttling: avoiding notification spam (concept)
- Respecting user preferences and quiet hours (concept)
- Retry and fallback across channels (push fails → fall back to email) (concept)
- Compare: synchronous send vs queued/async send (compare)
- Pitfall: a retry storm re-sending the same notification to every user (pitfall)
- Interview: "Design a system to notify 10M users of a price drop" (interview)

### Topic: Design a Presence Service (design-presence-service, intermediate)
Fanning "who's online" out to millions of watchers cheaply, when the state changes constantly and matters least when nobody's looking.
- The prompt: show accurate online/last-seen status to anyone watching a user (overview)
- Functional & non-functional requirements: staleness tolerance, watcher fan-out size, mobile battery cost (concept)
- Back-of-envelope: concurrent connections vs status-change rate vs watchers per user (concept)
- The API surface: heartbeat(), subscribe(userId), status-change events (concept)
- Data model: ephemeral state in memory (not the durable DB) with a short TTL (concept)
- Diagram: heartbeat path — client, gateway, presence store, subscriber fan-out (diagram)
- Fan-out of one status change to a large, dynamic watcher set (concept)
- Diagram: publish-subscribe topology for status updates (diagram)
- Handling flapping connections without spamming online/offline toggles (concept)
- Compare: push-based fan-out vs watchers polling on demand (compare)
- Pitfall: writing every heartbeat to durable storage, overwhelming the DB (pitfall)
- Interview: "Design the online-status indicator for a messaging app" (interview)
— cross-link: design-chat-system, messaging-fundamentals

### Topic: Design a Comment & Like System (design-comment-like-system, intermediate)
Aggregating a huge number of small writes onto one hot object (a viral post's like count) without that object becoming a bottleneck.
- The prompt: attach likes and threaded comments to any post, at any scale (overview)
- Functional & non-functional requirements: like-count accuracy, comment ordering, edit/delete (concept)
- Back-of-envelope: likes/sec on a single viral post vs a single row's write ceiling (concept)
- The API surface: like(postId, userId), comment(postId, text), getCounts(postId) (concept)
- Data model: comments as a tree/adjacency list vs a flat list with parentId (compare)
- Diagram: write path for a like — dedup by user, async counter increment (diagram)
- Deduplicating repeated likes from the same user without a full scan (concept)
- The hot object: a single post absorbing millions of likes in minutes (concept)
- Sharded counters and async aggregation for the visible like count (concept)
- Diagram: comment thread rendering — pagination and reply nesting (diagram)
- Pitfall: incrementing a single like_count column directly on the posts table (pitfall)
- Interview: "Design the like/comment system for a viral post" (interview)
— cross-link: design-distributed-counter, partitioning-and-sharding

### Topic: Design a Follow Graph Service (design-follow-graph-service, advanced)
Storing and querying a directed graph with hundreds of millions of edges — follower lists and mutuals are graph-traversal problems, not row lookups.
- The prompt: follow/unfollow, list followers, list following, check mutual (overview)
- Functional & non-functional requirements: read-heavy skew, celebrity fan-out of edges, count consistency (concept)
- Back-of-envelope: edges for a billion-user graph, and read QPS for follower lists (concept)
- The API surface: follow(a,b), unfollow(a,b), getFollowers(a), isFollowing(a,b) (concept)
- Data model: adjacency-list tables vs a native graph store (compare)
- Diagram: sharding the edge table by follower vs by followee, and why it matters (diagram)
- The celebrity problem again, from the graph side: a followee with 100M follower-edges (concept)
- Precomputed follower-count vs counting edges live (compare)
- Diagram: fan-out of a new post using this graph — where it hands off to news feed (diagram)
- The bottleneck: fetching "who follows both A and B" without a full graph engine (concept)
- Pitfall: storing follows only as forward edges, making "who follows me" an expensive scan (pitfall)
- Interview: "Design the follow/follower system behind a social network" (interview)
— cross-link: design-news-feed, nosql-data-models, ml-system-design (who-to-follow ranking)

### Topic: Design a Content Moderation Pipeline (design-content-moderation-pipeline, advanced)
An async, multi-stage pipeline that screens user content before and after it's live — the pipeline and feedback loop are the hard part, not the classifier.
- The prompt: screen every post/comment/image for policy violations, at platform scale (overview)
- Functional & non-functional requirements: pre-publish vs post-publish screening, latency budget, appeal flow (concept)
- Back-of-envelope: content volume vs review-queue throughput vs human reviewer capacity (concept)
- The API surface: submitForReview(content), reportContent(id), reviewDecision(id, verdict) (concept)
- Pipeline design: automated classifier pass, then a human-review queue for borderline cases (concept)
- Diagram: content flow — ingest, automated filters, priority queue, human review, action (diagram)
- Prioritizing the review queue: virality risk vs first-come-first-served (concept)
- Compare: block-before-publish vs publish-then-remove, and their different risk profiles (compare)
- Feedback loop: reviewer decisions retraining/tuning the automated filters (concept)
- Diagram: appeal flow when a user disputes a takedown (diagram)
- Pitfall: a synchronous moderation check on the publish path, adding latency to every post (pitfall)
- Interview: "Design a system to detect and act on abusive content in real time" (interview)
— cross-link: ml-system-design, event-driven-architecture, abuse-and-antifraud-in-design

### Topic: Design an Ephemeral Stories System (design-ephemeral-stories-system, intermediate)
Content that must vanish after 24 hours at massive scale, plus per-viewer view-tracking — expiry and read-receipts are the hard parts, not the media itself.
- The prompt: post a photo/video that disappears after 24h, and see who viewed it (overview)
- Functional & non-functional requirements: exact vs approximate expiry timing, viewer-list size (concept)
- Back-of-envelope: stories created/day, views/story, total ephemeral storage in flight (concept)
- The API surface: postStory(media, ttl), viewStory(id, viewerId), getViewers(id) (concept)
- Data model: TTL-indexed storage vs a background expiry sweep (compare)
- Diagram: expiry path — lazy deletion on read plus a low-priority background reaper (diagram)
- Tracking viewers per story without a hot write on every single view (concept)
- Diagram: story ring fan-out to followers, similar to but simpler than a full feed (diagram)
- The bottleneck: expiring millions of stories at the same wall-clock moment (concept)
- Compare: deleting the media immediately vs soft-deleting and reaping later (compare)
- Pitfall: a cron job scanning the entire stories table every minute to find expired rows (pitfall)
- Interview: "Design Instagram/Snapchat Stories" (interview)
— cross-link: design-comment-like-system, object-and-blob-storage

*Considered and cut:* a standalone Twitter-timeline case study (same fan-out lesson as News Feed with a
different logo); a generic Instagram photo-feed case study (same lesson again); a poll/voting case study
(same hot-object-counter lesson as Comment & Like); a standalone direct-messaging case study (Chat System
already owns 1:1 delivery).

---

## Group: Media & Streaming Systems (hld-cases-media)
*Video, audio, image, and file delivery — each system has a different storage shape (huge-few-files vs tiny-many-files) and a different latency contract (live vs on-demand).*

### Topic: Design a Video Streaming Platform (design-video-streaming-platform, advanced)
Upload, transcode, and adaptive-bitrate delivery of video at global scale.
- Clarifying requirements: upload, transcode, playback, live vs VOD (concept)
- Diagram: upload → transcode pipeline → storage → CDN → playback (diagram)
- Transcoding into multiple resolutions/bitrates (concept)
- Adaptive bitrate streaming: how the player picks a quality in real time (concept)
- Chunked delivery (HLS/DASH) instead of one giant file (concept)
- CDN placement for global low-latency playback (concept)
- Compare: on-the-fly transcoding vs precomputed renditions (compare)
- Storage architecture: object storage for video, DB for metadata (concept)
- Pitfall: serving video directly from origin without a CDN (pitfall)
- Interview: the follow-ups — recommendations, view-count accuracy, live streaming (interview)

### Topic: Design a Global Video Delivery Network (design-video-delivery-network, expert)
Netflix-scale delivery — deciding which titles live on which edge caches and failing over across CDNs, not how a single video gets transcoded.
- The prompt: serve a catalog of millions of titles to a global audience with minimal buffering (overview)
- Functional & non-functional requirements: startup latency target, rebuffer rate, regional demand skew (concept)
- Back-of-envelope: catalog size vs edge cache capacity vs origin egress if every request missed (concept)
- The API surface: a playback manifest request resolving to the nearest healthy edge (concept)
- Cache placement: which titles get pre-positioned at which edge locations (concept)
- Diagram: origin, regional caches, edge caches, and the request path for a play (diagram)
- Predictive pre-positioning: pushing new/trending titles to edges before demand hits (concept)
- Compare: single-CDN vs multi-CDN with real-time routing by health and cost (compare)
- Diagram: multi-CDN failover when one CDN degrades in a region (diagram)
- The bottleneck: origin overload when a cache-miss storm hits an under-cached title (concept)
- Trade-off: cache hit ratio vs storage cost of over-provisioning every edge (compare)
- Pitfall: routing purely by geography, ignoring real-time CDN health/cost signals (pitfall)
- Interview: "Design the CDN strategy behind a global video streaming service" (interview)
— cross-link: design-video-streaming-platform, cdn-and-edge-caching, multi-region-topologies

### Topic: Design an Audio Streaming Service (design-audio-streaming-service, advanced)
A catalog of hundreds of millions of small files with high-QPS random access and offline sync — the opposite storage shape from video's few-huge-files problem.
- The prompt: stream any of hundreds of millions of songs instantly, plus offline downloads (overview)
- Functional & non-functional requirements: startup latency, offline license expiry, gapless playback (concept)
- Back-of-envelope: catalog size, concurrent streams, per-track storage vs video's per-title storage (compare)
- The API surface: getStreamUrl(trackId), download(trackId), cross-device playlist sync (concept)
- Data model: small immutable audio objects plus a metadata/catalog service (concept)
- Diagram: storage and delivery architecture — object store, CDN, metadata DB (diagram)
- Offline downloads: syncing licensed content to a device and expiring it without connectivity (concept)
- Diagram: cross-device playlist and playback-position sync (diagram)
- The bottleneck: metadata/catalog lookups at far higher QPS than video's per-title lookups (concept)
- Compare: pre-computing personalized playlists vs computing them on read (compare)
- Pitfall: treating audio like small video — over-engineering ABR for files that fit in a phone's cache (pitfall)
- Interview: "Design the backend for a music streaming app with offline mode" (interview)
— cross-link: design-video-streaming-platform, object-and-blob-storage, ml-system-design (playlist ranking)

### Topic: Design an Image Hosting Service (design-image-hosting-service, intermediate)
Content-addressable storage for billions of small immutable blobs — dedup and on-the-fly derivatives are the hard parts, not the upload form.
- The prompt: upload an image, get a URL, serve it fast at many sizes (overview)
- Functional & non-functional requirements: upload volume, read:write ratio, supported sizes/formats (concept)
- Back-of-envelope: images/day, storage growth, derivative-size multiplier per original (concept)
- The API surface: upload(image), getUrl(id, size), delete(id) (concept)
- Content-addressable storage: hashing image bytes to dedup identical uploads (concept)
- Diagram: upload path — hash, dedup check, store original, enqueue derivative generation (diagram)
- On-the-fly resizing vs precomputing common sizes at upload time (compare)
- Diagram: read path — CDN, cache, on-the-fly resize fallback (diagram)
- The bottleneck: a burst of resize requests for sizes that weren't precomputed (concept)
- Serving via CDN with cache keys that include the requested size/format (concept)
- Pitfall: hashing only the file name for dedup instead of the content, missing true duplicates (pitfall)
- Interview: "Design an image hosting service like Imgur" (interview)
— cross-link: object-and-blob-storage, cdn-and-edge-caching

### Topic: Design a File Sync Service (design-file-sync-service, advanced)
Delta sync of files across devices that go offline — chunking and conflict resolution are the hard parts, not storing a file.
- The prompt: keep a folder in sync across a laptop, phone, and the cloud, even offline (overview)
- Functional & non-functional requirements: max file size, offline edit window, conflict frequency (concept)
- Back-of-envelope: files per user, change frequency, bandwidth if every edit re-uploaded the whole file (concept)
- The API surface: uploadChunk(fileId, chunk), getChanges(since), resolveConflict(fileId) (concept)
- Chunking files into fixed or content-defined blocks for delta sync (concept)
- Diagram: block-level diff — only changed chunks travel over the wire (diagram)
- Metadata service (file tree, versions) separate from block storage (concept)
- Diagram: sync architecture — client watchers, metadata service, block store (diagram)
- Conflict resolution when two devices edit the same file offline (concept)
- Compare: this delta-sync/offline model vs the collaborative editor's live-merge model (compare)
- The bottleneck: the metadata service under a large folder with frequent small changes (concept)
- Pitfall: re-uploading the entire file on every save instead of just the changed blocks (pitfall)
- Interview: "Design Dropbox — file sync across devices" (interview)
— cross-link: design-collaborative-editor, object-and-blob-storage, conflict-resolution

### Topic: Design a Live Streaming Platform (design-live-streaming-platform, expert)
Sub-second-latency ingest-to-viewer pipeline for content that doesn't exist until the moment it's watched — the opposite of VOD's precompute-then-serve model.
- The prompt: a streamer broadcasts live, thousands watch with minimal delay (overview)
- Functional & non-functional requirements: end-to-end latency budget, concurrent viewer spikes, live chat (concept)
- Back-of-envelope: ingest bitrate, fan-out viewers per stream, total egress during a spike (concept)
- The API surface: startStream(), ingest endpoint, a playback manifest that updates as segments arrive (concept)
- Live transcoding: producing renditions in real time instead of precomputing them (concept)
- Diagram: ingest → real-time transcode → low-latency CDN distribution → viewers (diagram)
- Chunked low-latency delivery: small segment windows vs VOD's larger chunks (compare)
- Diagram: viewer fan-out during a spike — one popular stream, huge simultaneous join (diagram)
- The bottleneck: transcoding falling behind ingest under load, causing latency to climb (concept)
- Live chat at stream scale, fanning out to viewers without lagging the video (concept)
- Trade-off: lower latency vs playback stability (larger buffers smooth network jitter) (compare)
- Pitfall: applying the VOD precompute-then-cache model to live, adding minutes of delay (pitfall)
- Interview: "Design a live streaming platform like Twitch" (interview)
— cross-link: design-video-streaming-platform, design-chat-system, load-balancing-fundamentals

### Topic: Design a Media Transcode Pipeline (design-transcode-pipeline, intermediate)
The general async job system behind "process every uploaded photo/video into derivatives" — orchestration and idempotent retries are the lesson, not any one codec.
- The prompt: any uploaded media file needs one or more derivative jobs run on it (overview)
- Functional & non-functional requirements: job types, priority (user-facing vs batch), retry budget (concept)
- Back-of-envelope: uploads/sec vs worker throughput per job type (concept)
- The API surface: submitJob(mediaId, jobType), job status callback/webhook (concept)
- Data model: a job queue plus a job-state table keyed by mediaId + jobType (concept)
- Diagram: pipeline — upload triggers job, queue, worker pool, output storage, status update (diagram)
- Idempotent retries: a worker crashing mid-job must not corrupt or duplicate output (concept)
- Prioritization: a user waiting on a thumbnail vs a batch re-encode running overnight (compare)
- Diagram: worker pool autoscaling against queue depth (diagram)
- The bottleneck: one job type (e.g. 4K transcode) starving the queue for cheap jobs (thumbnails) (concept)
- Pitfall: no idempotency key, so a retried job double-charges storage or emits duplicate output (pitfall)
- Interview: "Design the system that processes every file a user uploads" (interview)
— cross-link: design-distributed-job-scheduler, messaging-fundamentals, backpressure-and-dead-letter-handling

---

## Group: Marketplace & Transactional Systems (hld-cases-marketplace)
*Two- and three-sided marketplaces plus money-movement systems — correctness under contention (double-booking, double-charging, unfair matching) is the shared hard problem, expressed differently each time.*

### Topic: Design a Ticket Booking System (design-ticket-booking-system, advanced)
Preventing double-booking under heavy contention for a fixed, scarce inventory of seats.
- Clarifying requirements: seat selection, holds, high-contention drops (concept)
- The core problem: preventing double-booking under concurrent requests (concept)
- Pessimistic locking vs optimistic concurrency for seat reservation (compare)
- Diagram: two users racing for the same seat, and how the lock resolves it (diagram)
- Temporary holds: reserving a seat during checkout without a permanent lock (concept)
- Handling a high-demand on-sale moment (queueing users, waiting rooms) (concept)
- Compare: database-level locking vs a distributed lock service (compare)
- Diagram: end-to-end booking flow — search, hold, pay, confirm (diagram)
- Pitfall: releasing a seat hold only on success, leaking seats on abandoned checkouts (pitfall)
- Interview: "Design a movie ticket booking system for a popular release" (interview)

### Topic: Design a Ride-Hailing System (design-ride-hailing-system, expert)
Real-time matching, dispatch, and surge pricing on top of a live location feed — the matching/pricing loop is the hard part, not finding nearby drivers.
- The prompt: rider requests a ride, gets matched to a nearby driver in seconds (overview)
- Functional & non-functional requirements: match latency target, cancellation handling, surge fairness (concept)
- Back-of-envelope: concurrent rides, location pings/sec per driver, matches/sec in a dense city (concept)
- The API surface: requestRide(), driverLocationUpdate(), acceptMatch() (concept)
- Data model: live driver locations (ephemeral, high-write) vs ride/trip records (durable) (compare)
- Diagram: architecture — location service, matching engine, trip service, pricing service (diagram)
- The matching algorithm: nearest-available driver vs balancing marketplace-wide efficiency (concept)
- Diagram: match loop — candidate drivers from the location index, scored, offered, accepted (diagram)
- Dynamic/surge pricing: computing a price multiplier from live supply/demand per zone (concept)
- Compare: greedy nearest-match vs batched matching for better marketplace efficiency (compare)
- The bottleneck: the matching engine during a demand spike (a concert letting out) (concept)
- Pitfall: matching purely by distance, ignoring driver heading/ETA and causing bad matches (pitfall)
- Interview: "Design the rider-driver matching system behind Uber" (interview)
— cross-link: design-proximity-service, quorum-systems, geo-routing-and-failover

### Topic: Design a Food Delivery System (design-food-delivery-system, advanced)
A three-sided marketplace (customer, restaurant, courier) with a real-time order state machine and batching — different from ride-hailing's point-to-point match.
- The prompt: order from a restaurant, a courier picks up and delivers it, all parties see live status (overview)
- Functional & non-functional requirements: prep-time estimates, courier assignment latency, order accuracy (concept)
- Back-of-envelope: concurrent orders, couriers online, orders/courier during a batching window (concept)
- The API surface: placeOrder(), updateOrderStatus(), assignCourier() (concept)
- Data model: an order state machine (placed → accepted → preparing → picked up → delivered) (concept)
- Diagram: three-sided data flow — customer app, restaurant app, courier app synced off one order record (diagram)
- Courier assignment: assign per order vs batch multiple orders into one courier's route (compare)
- Diagram: batching two nearby orders onto one courier trip (diagram)
- ETA prediction feeding both the customer app and the assignment decision (concept)
- The bottleneck: restaurant-side order acceptance lag during a lunch-hour spike (concept)
- Pitfall: syncing order status via client polling instead of push, causing stale statuses (pitfall)
- Interview: "Design a food delivery system connecting customers, restaurants, and couriers" (interview)
— cross-link: design-ride-hailing-system, event-driven-architecture, design-notification-system

### Topic: Design a Hotel Booking System (design-hotel-booking-system, intermediate)
Date-range inventory (room-nights, not single seats) searched across thousands of properties — a range-overlap problem, not a single-item lock.
- The prompt: search "rooms in city X, these dates", book one, avoid overselling (overview)
- Functional & non-functional requirements: search latency across many properties, overbooking policy (concept)
- Back-of-envelope: properties, room-nights of inventory, search QPS vs booking QPS (concept)
- The API surface: searchAvailability(city, dates), holdRoom(), confirmBooking() (concept)
- Data model: per-room-per-night availability rows vs a date-range calendar structure (compare)
- Diagram: search fan-out across properties, filtered by date-range availability (diagram)
- Preventing overselling a room for overlapping date ranges under concurrent bookings (concept)
- Compare: strict no-overbooking vs deliberate overbooking with a cancellation buffer (compare)
- Diagram: booking flow — hold, payment, confirm, release-on-timeout (diagram)
- The bottleneck: search fan-out latency across a large city with thousands of properties (concept)
- Pitfall: modeling inventory as a single "rooms available" counter instead of per-date rows (pitfall)
- Interview: "Design a hotel booking system like Booking.com" (interview)
— cross-link: design-ticket-booking-system, partitioning-and-sharding

### Topic: Design an E-Commerce Checkout System (design-ecommerce-checkout-system, advanced)
A distributed transaction across inventory, payment, and shipping that must be idempotent under retries — the saga is the hard part, not the shopping cart UI.
- The prompt: cart → checkout → confirmed order, touching inventory, payment, and shipping (overview)
- Functional & non-functional requirements: no double-charge, no oversell, checkout latency under flash-sale load (concept)
- Back-of-envelope: checkouts/sec in steady state vs a flash-sale spike (concept)
- The API surface: checkout(cartId), and the idempotency key that makes retries safe (concept)
- Data model: order as a saga of steps, each with its own compensating action (concept)
- Diagram: the saga — reserve inventory, charge payment, create shipment, or compensate on failure (diagram)
- Idempotency: a client retry after a timeout must not create a second order or a second charge (concept)
- Compare: two-phase-commit-style locking vs a saga with compensation (compare)
- Diagram: flash-sale path — inventory reservation under heavy contention (diagram)
- The bottleneck: the inventory-decrement step during a flash sale on a limited-stock item (concept)
- Pitfall: charging payment before confirming inventory, leading to refund storms on oversells (pitfall)
- Interview: "Design the checkout flow for an e-commerce site during a flash sale" (interview)
— cross-link: distributed-transactions-and-sagas, design-payment-system, idempotency-and-exactly-once

### Topic: Design a Payment System (design-payment-system, expert)
Moving money exactly once and being able to prove it — ledger correctness and reconciliation matter more than throughput.
- The prompt: charge a customer, pay out a merchant, and never lose or duplicate money (overview)
- Functional & non-functional requirements: exactly-once guarantees, auditability, regulatory retention (concept)
- Back-of-envelope: transactions/sec vs the far stricter correctness bar than typical read/write systems (concept)
- The API surface: charge(idempotencyKey, amount), refund(), and why idempotency keys are non-negotiable here (concept)
- Data model: a double-entry ledger — every transaction is two balanced entries, not one balance update (concept)
- Diagram: a charge as a ledger entry pair, not a single account-balance mutation (diagram)
- Idempotency keys preventing a network retry from double-charging a card (concept)
- Reconciliation: matching your ledger against the external payment processor's records (concept)
- Diagram: end-to-end flow — client, payment service, processor, ledger, async reconciliation job (diagram)
- The bottleneck: synchronous calls to an external processor on the critical checkout path (concept)
- Compare: strong consistency on the ledger vs eventual consistency on account-balance views (compare)
- Pitfall: updating a single balance column instead of an immutable ledger, losing the audit trail (pitfall)
- Interview: "Design a payment processing system that never double-charges" (interview)
— cross-link: design-ecommerce-checkout-system, idempotency-and-exactly-once, consensus-basics

### Topic: Design an Ad Click Aggregation System (design-ad-click-aggregation-system, advanced)
Billing-accuracy-critical stream aggregation — exactly-once counting and fraud filtering matter more than raw throughput.
- The prompt: count ad clicks/impressions accurately enough to bill advertisers (overview)
- Functional & non-functional requirements: billing accuracy (no double-count), fraud/click-spam filtering, reporting freshness (concept)
- Back-of-envelope: clicks/sec at platform scale vs the cost of a 1% counting error at that volume (concept)
- The API surface: recordClick(adId, userId, ts), getAggregate(adId, window) (concept)
- Stream processing: windowed aggregation over a click event stream (concept)
- Diagram: pipeline — event ingest, dedup/fraud filter, windowed aggregation, billing store (diagram)
- Exactly-once counting despite at-least-once delivery from the ingest layer (concept)
- Handling late-arriving events: a click that lands after its window already closed (concept)
- Compare: real-time (Lambda-architecture) counts vs an end-of-day authoritative batch recount (compare)
- Diagram: fraud filtering — bot detection and click-spam rules ahead of the aggregator (diagram)
- The bottleneck: the fraud-filter stage becoming the throughput ceiling for the whole pipeline (concept)
- Pitfall: counting clicks at ingest time before fraud filtering, then billing on the inflated number (pitfall)
- Interview: "Design a system to count ad clicks for billing at scale" (interview)
— cross-link: log-based-streaming, ml-system-design (fraud/bot detection), schema-evolution-and-compatibility

### Topic: Design a Stock Exchange Matching Engine (design-stock-exchange-matching-engine, expert)
Deterministic, price-time-priority order matching at microsecond latency — a single-threaded correctness core, the opposite of "scale by adding nodes."
- The prompt: match buy and sell orders fairly and deterministically, at extreme speed (overview)
- Functional & non-functional requirements: fairness (price-time priority), determinism, microsecond-level latency (concept)
- Back-of-envelope: orders/sec per symbol vs the latency budget per match (concept)
- The API surface: submitOrder(symbol, side, price, qty), cancelOrder(), market data feed (concept)
- Data model: the order book — a price-ordered structure per symbol, not a generic DB table (concept)
- Diagram: the order book — bids and asks as two price-ordered queues (diagram)
- Why this core is single-threaded per symbol: any reordering breaks fairness and auditability (concept)
- Compare: horizontally scaling by symbol-sharding vs trying to parallelize one order book (compare)
- Diagram: the matching loop — incoming order, price-time priority match, trade emitted (diagram)
- Sequencing and audit logging every order/match for regulatory replay (concept)
- The bottleneck: a single hot symbol's order book exceeding one core's throughput (concept)
- Pitfall: introducing any nondeterminism (e.g. multi-threaded matching) that breaks trade replay (pitfall)
- Interview: "Design a simplified stock exchange matching engine" (interview)
— cross-link: consensus-basics, time-and-ordering, physical-and-cost-constraints

---

## Group: Infrastructure & Platform Systems (hld-cases-infra)
*Systems that other systems are built on — search, telemetry, scheduling, and the storage/queue/gateway primitives themselves. The lesson here is building the primitive, where the building-block groups teach using one.*

### Topic: Design a Web Crawler (design-web-crawler, advanced)
Crawling at scale politely, without duplicating work or getting blocked.
- Clarifying requirements: scale, freshness, politeness constraints (concept)
- The crawl frontier: a queue of URLs to visit, prioritized (concept)
- Diagram: crawler architecture — frontier, fetchers, parser, dedup store (diagram)
- Politeness: rate-limiting per domain, respecting robots.txt (concept)
- URL deduplication at scale (Bloom filters) (concept)
- Distributing the crawl across many workers without duplicate work (concept)
- Compare: breadth-first vs priority-based crawl ordering (compare)
- Handling traps: infinite URL spaces, duplicate content (concept)
- Pitfall: no per-domain rate limit, hammering one site and getting blocked (pitfall)
- Interview: "Design a crawler that indexes a billion pages" (interview)

### Topic: Design a Proximity Service (design-proximity-service, intermediate)
Answering "what's nearby" fast, using a spatial index instead of scanning every location.
- Clarifying requirements: "find nearby X" query shape and update frequency (concept)
- Naive approach and why scanning all locations doesn't scale (concept)
- Geohashing: encoding location into a sortable string prefix (concept)
- Diagram: geohash grid cells around a query point (diagram)
- Quadtrees as an alternative spatial index (concept)
- Compare: geohash vs quadtree vs simple grid (compare)
- Handling moving objects: frequent location updates at scale (concept)
- Diagram: end-to-end architecture for a "nearby drivers" query (diagram)
- Pitfall: a geohash boundary splitting nearby points into different cells (pitfall)
- Interview: "Design 'find nearby drivers' for a ride-hailing app" (interview)

### Topic: Design a Collaborative Editor (design-collaborative-editor, advanced)
Merging concurrent real-time edits from multiple users without clobbering anyone's changes.
- Clarifying requirements: real-time multi-user editing, offline edits (concept)
- The core problem: merging concurrent edits without clobbering each other (concept)
- Operational Transformation (OT): the classic approach (concept)
- CRDTs as a newer alternative to OT (concept)
- Diagram: two concurrent edits transformed/merged into a consistent result (diagram)
- Compare: OT vs CRDTs on complexity and correctness guarantees (compare)
- Real-time sync transport: WebSockets and presence (concept)
- Diagram: end-to-end architecture — client, sync server, document store (diagram)
- Pitfall: naive last-write-wins on a shared document, silently dropping edits (pitfall)
- Interview: "Design Google Docs-style collaborative editing" (interview)

### Topic: Design a Search Typeahead System (design-search-typeahead-system, advanced)
Sub-100ms prefix suggestions ranked by popularity — a specialized prefix data structure and freshness problem, distinct from full-text search ranking.
- The prompt: as a user types, show ranked query suggestions in under 100ms (overview)
- Functional & non-functional requirements: latency budget, personalization, trending-query freshness (concept)
- Back-of-envelope: keystrokes/sec platform-wide vs suggestions-per-keystroke fan-out (concept)
- The API surface: getSuggestions(prefix, userId) (concept)
- Data model: a trie/FST of prefixes to top-K completions vs a generic inverted index (compare)
- Diagram: trie structure with precomputed top-K suggestions cached at each node (diagram)
- Ranking suggestions by historical popularity, recency, and personalization signals (concept)
- Keeping trending queries fresh without rebuilding the whole trie (concept)
- Diagram: offline aggregation job periodically refreshing the trie from query logs (diagram)
- The bottleneck: serving latency if the trie doesn't fit in memory on one node (concept)
- Compare: precomputed trie vs querying the full-text search index live for suggestions (compare)
- Pitfall: ranking suggestions by raw frequency only, surfacing stale/abandoned queries (pitfall)
- Interview: "Design the autocomplete behind a search bar" (interview)
— cross-link: autocomplete-and-typeahead, inverted-index, relevance-ranking

### Topic: Design a Logging & Metrics Pipeline (design-logging-metrics-pipeline, advanced)
Ingesting and querying telemetry at a volume far exceeding the systems it monitors — the pipeline's own scale is the design problem.
- The prompt: every service emits logs and metrics; make them queryable and alertable (overview)
- Functional & non-functional requirements: ingest volume, query latency, retention/cost tiers (concept)
- Back-of-envelope: log lines/sec and metric points/sec at fleet scale, vs storage cost (concept)
- The API surface: emit(log/metric), query(timeRange, filter), alert rule evaluation (concept)
- Data model: time-series storage for metrics vs a search index for logs (compare)
- Diagram: pipeline — agents, ingest buffer, stream processor, hot store, cold store (diagram)
- Sampling and aggregation: not every log line survives to long-term storage (concept)
- Downsampling metrics over time (raw → 1min → 1hr rollups) to control storage cost (concept)
- Diagram: hot (recent, full-resolution) vs cold (old, downsampled) storage tiers (diagram)
- The bottleneck: a logging spike from a misbehaving service drowning out everyone else's signal (concept)
- Pitfall: no per-tenant ingest limit, so one noisy service can take down the whole pipeline (pitfall)
- Interview: "Design the logging/metrics backend behind an observability platform" (interview)
— cross-link: logging-at-scale, metrics-and-slis-slos, cost-aware-telemetry-at-scale

### Topic: Design a Distributed Job Scheduler (design-distributed-job-scheduler, expert)
A distributed cron that guarantees every job runs, reliably, even as workers and leaders fail — the scheduling guarantee is the whole problem.
- The prompt: run millions of scheduled/recurring jobs across a fleet of workers, reliably (overview)
- Functional & non-functional requirements: at-least-once vs exactly-once execution, missed-job handling, priority (concept)
- Back-of-envelope: jobs scheduled/min, worker fleet size, jobs-in-flight at peak (concept)
- The API surface: scheduleJob(cronSpec/runAt), cancelJob(), job status/heartbeat (concept)
- Data model: a job table with next-run-time, lease/lock state, and retry count (concept)
- Diagram: architecture — scheduler leader, job store, worker pool, lease-based dispatch (diagram)
- Leader election for the component that decides "which jobs are due now" (concept)
- Leasing a job to a worker so a crashed worker's job gets picked up by another (concept)
- Diagram: a worker crash mid-job — lease expiry and safe re-dispatch (diagram)
- The bottleneck: the job store under a scheduling stampede (many jobs due at the same minute) (concept)
- Compare: at-least-once execution with idempotent jobs vs trying to guarantee exactly-once (compare)
- Pitfall: no lease/lock on dispatched jobs, so a slow worker's job gets run twice by two workers (pitfall)
- Interview: "Design a distributed cron system like a lightweight Airflow" (interview)
— cross-link: design-transcode-pipeline, idempotency-and-exactly-once, distributed-coordination

### Topic: Design a Blob / Object Store (design-blob-object-store, expert)
Building the durable object store itself (S3-like) — erasure coding, metadata scaling, and multi-part upload, not using one.
- The prompt: store and serve arbitrarily large immutable objects, durably, at exabyte scale (overview)
- Functional & non-functional requirements: durability target (many nines), availability, upload size limits (concept)
- Back-of-envelope: objects stored, average size, storage overhead of your durability scheme (concept)
- The API surface: putObject(key, bytes), getObject(key), multi-part upload for large objects (concept)
- Data model: metadata service (key → location) fully decoupled from the data-storage nodes (concept)
- Diagram: architecture — metadata service, storage nodes, and how a GET resolves through both (diagram)
- Durability via replication vs erasure coding, and the storage-overhead trade-off (compare)
- Diagram: erasure coding — splitting an object into data + parity shards across nodes (diagram)
- Multi-part upload: large objects uploaded as independent chunks, assembled on commit (concept)
- The bottleneck: metadata service throughput at billions of objects (concept)
- Compare: strong consistency on writes (read-after-write) vs eventual consistency on list operations (compare)
- Pitfall: colocating metadata and data on the same nodes, so a data-node failure loses lookups too (pitfall)
- Interview: "Design a durable object store like S3 from first principles" (interview)
— cross-link: object-and-blob-storage, replication-strategies, storage-engine-choice-as-a-design-decision

### Topic: Design a Distributed Message Queue (design-distributed-message-queue, expert)
Building the broker itself (Kafka/SQS-like) — the partitioned log and delivery-semantics internals, not how to use a queue.
- The prompt: a durable, ordered, at-least-once message broker that producers and consumers share (overview)
- Functional & non-functional requirements: throughput, ordering scope, delivery guarantee, retention window (concept)
- Back-of-envelope: messages/sec, average message size, retention-window storage (concept)
- The API surface: produce(topic, key, value), consume(topic, partition, offset) (concept)
- Data model: the partitioned append-only log as the core storage structure (concept)
- Diagram: topic split into partitions, each an ordered, append-only log with an offset (diagram)
- Consumer offset tracking: how a consumer resumes exactly where it left off (concept)
- Diagram: producer → partition (by key) → replicated log → consumer group offsets (diagram)
- Delivery semantics internals: how at-least-once, at-most-once, and exactly-once actually differ here (compare)
- Replication within the broker for durability if a partition leader fails (concept)
- The bottleneck: a single hot partition (skewed key) capping one topic's throughput (concept)
- Pitfall: growing partition count after the fact, silently breaking key-based ordering guarantees (pitfall)
- Interview: "Design a distributed message queue like Kafka from scratch" (interview)
— cross-link: log-based-streaming, message-delivery-semantics, replication-strategies

### Topic: Design a Feature Flag Service (design-feature-flag-service, intermediate)
Millisecond flag evaluation on every request, globally consistent rollout percentages, and instant propagation — without a central bottleneck in every request path.
- The prompt: turn features on/off, or roll out to X% of users, without a redeploy (overview)
- Functional & non-functional requirements: evaluation latency (must not slow the request), propagation delay, targeting rules (concept)
- Back-of-envelope: flag evaluations/sec across the whole fleet vs a central service's capacity (concept)
- The API surface: isEnabled(flagKey, userContext), updateFlag(config) (concept)
- Stable bucketing: hashing userId + flagKey so the same user always lands in the same bucket (concept)
- Diagram: consistent-hash bucketing deciding in/out of a percentage rollout (diagram)
- Local evaluation via an SDK with a cached config, instead of a network call per request (concept)
- Diagram: config propagation — control plane pushes updates to SDKs via streaming/polling (diagram)
- The bottleneck: the control plane during a global config push to every service instance (concept)
- Compare: server-side evaluation (central call) vs client-side SDK evaluation (local, cached) (compare)
- Pitfall: evaluating flags with a synchronous network call on the hot request path (pitfall)
- Interview: "Design a feature flag system used by every service at the company" (interview)
— cross-link: strangler-fig-and-migration-patterns, consistency-models

### Topic: Design an API Gateway (design-api-gateway-system, advanced)
The gateway as its own system with its own failure modes — routing, auth, and rate limiting at the edge, distinct from the API-design and resilience concepts it enforces.
- The prompt: one edge layer in front of many backend services, handling cross-cutting concerns (overview)
- Functional & non-functional requirements: added-latency budget, availability (it fronts everything), config agility (concept)
- Back-of-envelope: fleet-wide QPS through the gateway vs a single backend service's QPS (concept)
- The API surface: route config (path → service), plus the cross-cutting policies attached to a route (concept)
- Data model: a routing table plus per-route policy config (auth, rate limit, timeout) (concept)
- Diagram: request path — TLS termination, auth, rate limit, routing, backend, response (diagram)
- Request aggregation: composing one client-facing response from multiple backend calls (concept)
- Compare: a single monolithic gateway vs sidecar-based per-service gateways (service mesh) (compare)
- Diagram: gateway cluster behind a load balancer, stateless and horizontally scaled (diagram)
- The bottleneck: the gateway itself, since every request in the system passes through it (concept)
- Failure isolation: one slow backend must not exhaust the gateway's connection pool for everyone (concept)
- Pitfall: putting business logic in the gateway, coupling it to backends it should stay agnostic of (pitfall)
- Interview: "Design an API gateway for a company with dozens of backend services" (interview)
— cross-link: api-gateway-patterns, service-mesh, bulkheads-and-isolation

---

## Boundary notes

- **`ml-system-design` (in the separate `ai-ml` area) owns the ranking/recommendation models.**
  Several case studies here touch a ranking or scoring signal but should stop at "here's the
  slot in the architecture where a model plugs in" and cross-link out rather than re-teach it:
  `design-news-feed` (feed ranking), `design-follow-graph-service` (who-to-follow suggestions),
  `design-audio-streaming-service` (playlist ranking), `design-content-moderation-pipeline`
  (the classifier itself), `design-ad-click-aggregation-system` (fraud/bot-detection model).
- **LLD case studies vs this group's service-scale case studies share a name, not a lesson.**
  `lld-case-studies` has `rate-limiter` (an in-process class/algorithm) and `notification-system`
  (an OOP class design); this brief's `design-rate-limiter-service` and `design-notification-system`
  are the distributed *service* versions — different hard part (shared state, fan-out, config
  propagation) at a different altitude. No slug collision; keep the framing distinct in both places.
- **Building-block groups teach the concept; the matching infra case study teaches building the
  primitive.** `design-blob-object-store` builds what `object-and-blob-storage` teaches you to use;
  `design-distributed-message-queue` builds what `messaging-fundamentals`/`queues-vs-pubsub` teach
  you to use; `design-distributed-cache` builds what `caching`/`distributed-caching` teach you to
  use. Each case study's cross-links point at the *usage*-level group so slides don't re-derive it.
- **Resilience group overlap.** `design-rate-limiter-service` cross-links `distributed-rate-limiting`
  for the algorithms; the original `hld-case-studies` brief explicitly skipped a rate-limiter case
  study "to avoid duplicating" that group. Per this task's brief (more depth/coverage), it's added
  back here but scoped strictly to the service-architecture problem, not the token-bucket/sliding-
  window mechanics, which stay owned by `resilience`.
- **Merged/cut, with reasoning inline near each group above:** Twitter timeline, generic Instagram
  photo-feed, poll/voting, and standalone direct-messaging case studies — each would have re-taught
  an existing topic's lesson with a different product name attached.
