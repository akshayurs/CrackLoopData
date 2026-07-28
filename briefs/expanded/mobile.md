# Area: Mobile (mobile)

*Building and reasoning about native, cross-platform, and system-level mobile clients — the app (not the backend) side of the interview.*

---

## Group: Mobile Fundamentals (mobile-fundamentals)

### Topic: Mobile App Lifecycle & Process Model (app-lifecycle-process-model, beginner)
The cross-platform mental model of app states and why memory-constrained OSes kill processes without warning; platform-specific callbacks belong to the Android/iOS groups.
- The four app states every mobile OS models: active, background, suspended, killed
- Why phones kill processes without asking
- Diagram: state transitions and what triggers each
- Foreground vs background execution budgets
- Rebuilding UI after a process death: state restoration
- Cold start vs warm start vs hot start
- What actually persists across a kill vs what doesn't
- Pitfall: assuming "backgrounded" means "paused in place, safe to keep working"
- Pitfall: never testing restoration because it rarely happens on a dev device

### Topic: Local Storage Options on Mobile (local-storage-options, beginner)
The decision framework across preferences, embedded databases, files, and secure storage; Room/Core Data-specific APIs belong to the Android/iOS groups.
- The four storage tiers: preferences, database, files, secure storage
- What belongs in key-value prefs vs a real database
- Embedded SQL databases on device: why SQLite won
- When a document/NoSQL store beats relational on-device
- Diagram: choosing a storage layer by data shape and size
- Encrypting data at rest: what the OS gives you for free
- Secure storage for tokens and secrets
- Migrating an on-device schema without losing user data
- Pitfall: storing sensitive data in plain preferences
- Pitfall: an unbounded local cache that fills the device's disk

### Topic: Mobile Networking Essentials (mobile-networking-essentials, intermediate)
Constraints unique to a mobile radio and API-style trade-offs for a mobile client; HTTP/TCP fundamentals themselves live in Computer Networks.
- Why mobile networking isn't just "HTTP but on a phone"
- The radio state machine: why a network call has a cost beyond bytes
- Diagram: request batching and coalescing to save radio wakeups
- REST vs GraphQL vs gRPC for a mobile client
- Client-side caching layers: memory, disk, HTTP cache headers
- Retry, backoff, and idempotency on flaky connections
- Detecting and reacting to connectivity changes
- Certificate pinning: what it buys you and what it breaks
- Pitfall: firing one network call per list item instead of batching
- Pitfall: retrying a non-idempotent request and double-charging a user

### Topic: Battery, Power & Background Execution Limits (battery-power-background-limits, intermediate)
Why every mobile OS throttles background work and the cross-platform vocabulary for reasoning about power; WorkManager/Background Tasks specifics live in Android/iOS.
- Where battery actually goes: radio, screen, CPU
- Why every OS aggressively limits background work
- Wakelocks and why holding one wrong drains a battery overnight
- Diagram: a generic doze/app-standby-style power state model
- Deferring, batching, and coalescing background jobs
- User-facing work vs deferrable maintenance work
- Measuring battery impact: what to profile before optimizing
- Pitfall: polling a server on a tight timer "just to be safe"
- Pitfall: holding a wakelock across a network call with no timeout

### Topic: Mobile Security Fundamentals (mobile-security-fundamentals, intermediate)
Applying crypto/auth theory (Area 13) specifically to a mobile client: secure storage, transport security, tampering resistance, and deep-link validation.
- The mobile attack surface: device, network, backend, supply chain
- Where tokens and secrets should (and shouldn't) live on-device
- Diagram: a login token's path from server to secure storage to API calls
- Certificate pinning and man-in-the-middle defense
- Biometric authentication: what "unlocks the app" actually verifies
- Code: validating and sanitizing an incoming deep link
- Obfuscation and tampering: why client-side checks aren't trustworthy alone
- Client-side vs server-side enforcement of business rules
- Pitfall: trusting a client-side "isPremiumUser" flag
- Pitfall: logging tokens or PII to on-device crash logs

### Topic: Push Notifications & Deep Linking (push-notifications-deep-linking, intermediate)
The cross-platform delivery model and permission/routing concerns; APNs/FCM SDK wiring specifics live in the Android/iOS groups.
- How a push notification actually travels: server, push service, device
- Diagram: the push delivery pipeline end to end
- Notification push vs silent/data push: different jobs
- Why delivery is best-effort, not guaranteed
- Permission prompts: asking at the right moment
- Deep links and universal/app links: routing a tap into app state
- Code: parsing a deep link into a navigation target
- Pitfall: treating push as a reliable message queue
- Pitfall: deep-linking into a screen that assumes prior app state exists

### Topic: App Distribution, Releases & Compatibility (app-distribution-releases-compatibility, beginner)
Why you can't force-update every install and what that forces onto release process and API design; CI/CD pipeline mechanics live in Engineering Craft/Cloud & DevOps.
- Why mobile releases aren't like deploying a web server
- The app store review pipeline and what it means for release timing
- Staged rollouts and kill switches for a bad release
- Diagram: a rollout with a canary percentage and rollback
- Feature flags and remote config on mobile
- Designing APIs that tolerate years of old client versions in the field
- What can be fixed remotely vs what requires a new binary
- Pitfall: shipping a breaking API change assuming everyone updates fast
- Pitfall: relying on a forced-update prompt as the only compatibility strategy

### Topic: Mobile UX Constraints & Accessibility (mobile-ux-constraints-accessibility, beginner)
Interaction constraints unique to touch/small screens; general web accessibility (ARIA/WCAG) lives in Web & Frontend — this covers TalkBack/VoiceOver and touch ergonomics.
- Designing for thumbs: touch target size and reachability
- Gestures vs buttons: discoverability trade-offs
- Adapting layout across phones, tablets, and foldables
- Diagram: safe areas and responsive breakpoints on a device screen
- Screen readers on mobile: TalkBack and VoiceOver basics
- Asking for permissions at the moment they're needed, not at launch
- Pitfall: a tap target that's visually bigger than its actual hit area
- Pitfall: an accessibility label that reads a decorative icon instead of its action

---

## Group: Android Development (android)

### Topic: Activity & Fragment Lifecycle (activity-fragment-lifecycle, beginner)
The concrete callback sequence for Activities and Fragments, configuration changes, and where to keep state across them.
- The Activity lifecycle callbacks in order
- Diagram: the Activity lifecycle state machine with callback names
- Why a configuration change (rotation) recreates your Activity
- Fragment lifecycle layered on top of its host Activity
- onSaveInstanceState vs ViewModel for surviving rotation
- Code: restoring UI state in onCreate from a saved Bundle
- Fragment transactions and the back stack
- Pitfall: leaking an Activity by holding its Context in a static field
- Pitfall: doing heavy work in onCreate and slowing cold start

### Topic: Jetpack Compose Fundamentals (jetpack-compose-fundamentals, intermediate)
Compose's declarative rendering model — composables, recomposition, and state hoisting; cross-platform declarative-UI framing lives in the Cross-Platform group.
- Composable functions: UI as a function of state
- Diagram: how recomposition re-runs only the affected composables
- State hoisting: lifting state up to make composables reusable
- remember vs rememberSaveable
- Code: a stateful counter refactored into a stateless composable
- Side effects: LaunchedEffect and DisposableEffect, and when to use each
- Jetpack Compose vs the classic View/XML system
- Pitfall: reading mutable state in a way that skips recomposition
- Pitfall: doing expensive work directly inside a composable body

### Topic: Android Architecture Components — MVVM in Practice (android-architecture-components, intermediate)
ViewModel, LiveData/StateFlow, and the Repository pattern as Android's concrete implementation of MVVM; general pattern theory lives in Object-Oriented Design.
- Why Android needed ViewModel: surviving configuration changes
- Diagram: the MVVM data flow — View, ViewModel, Repository, data source
- LiveData vs StateFlow for exposing UI state
- The Repository pattern: hiding data sources behind one API
- Code: a ViewModel exposing StateFlow consumed by Compose
- Single source of truth and unidirectional data flow
- MVVM vs MVI on Android
- Pitfall: holding a View reference inside a ViewModel
- Pitfall: a ViewModel that calls a network client directly instead of a repository

### Topic: Kotlin Coroutines & Flow (kotlin-coroutines-flow, intermediate)
Structured concurrency, suspend functions, dispatchers, and Flow as Kotlin's concrete async model; general async-model theory lives in Languages & Compilers.
- Suspend functions: pausable code without callback hell
- Diagram: a coroutine suspending and resuming on a dispatcher
- Structured concurrency: why every coroutine needs a scope
- viewModelScope and lifecycleScope: scopes tied to Android lifecycles
- Dispatchers.Main vs IO vs Default
- Flow vs a single suspend function: streams vs one-shot results
- Code: collecting a Flow safely with repeatOnLifecycle
- Pitfall: launching a coroutine in GlobalScope and leaking work
- Pitfall: blocking the main dispatcher with a synchronous call inside a coroutine

### Topic: Dependency Injection with Hilt (dependency-injection-hilt, intermediate)
Why Android's framework classes make manual DI awkward and how Hilt's component hierarchy maps to lifecycles; DI as a general principle lives in Object-Oriented Design.
- Why Android's framework classes make manual DI awkward
- Diagram: Hilt's component hierarchy mapped to Android lifecycles
- @Inject, @Module, and @Provides: the core annotations
- Scoping objects to Application, Activity, or ViewModel lifetime
- Code: injecting a repository into a ViewModel with Hilt
- Manual DI vs Dagger vs Hilt
- Pitfall: injecting an Activity-scoped dependency into a longer-lived singleton
- Pitfall: a circular dependency graph Hilt can't resolve

### Topic: RecyclerView & Efficient Lists (recyclerview-efficient-lists, intermediate)
The ViewHolder pattern, view recycling, and DiffUtil for performant lists in the View system.
- The ViewHolder pattern: why recycling views beats inflating them
- Diagram: how a RecyclerView reuses view holders while scrolling
- Code: a RecyclerView.Adapter with view holder binding
- DiffUtil: updating a list without a full rebind
- RecyclerView with DiffUtil vs Compose's LazyColumn
- Pagination: loading more items before the user hits the bottom
- Pitfall: calling notifyDataSetChanged() for every small update
- Pitfall: decoding images on the main thread inside onBindViewHolder

### Topic: Background Work — Services & WorkManager (background-work-services-workmanager, intermediate)
Android's concrete tools for background work and when to pick which; the cross-platform "why background work is throttled" lives in Mobile Fundamentals.
- Services, foreground Services, and WorkManager: three tools, three jobs
- Diagram: deciding which background tool fits a given task
- Code: scheduling a deferrable upload with WorkManager constraints
- Foreground Services and the user-visible notification they require
- Broadcast Receivers: reacting to system-wide events
- WorkManager's guarantees: what survives a reboot or process death
- Pitfall: using a bare Service for work that should be a WorkManager job
- Pitfall: an unconstrained periodic worker that runs more than intended

### Topic: Memory Management & ANRs on Android (memory-management-anrs-android, advanced)
Context leak patterns and the main-thread ANR watchdog; general JVM GC mechanics live in Languages & Compilers.
- What actually causes an ANR: the 5-second main-thread rule
- Diagram: the main thread's message queue and where it gets stuck
- Common Context leak patterns: static references and inner classes
- Code: a listener leak fixed with a WeakReference or lifecycle-aware scope
- Detecting leaks: heap dumps and LeakCanary's approach
- A memory leak vs a legitimate long-lived cache
- Pitfall: an anonymous inner class silently holding its outer Activity
- Pitfall: registering a listener in onCreate and never unregistering it

### Topic: Kotlin Language Patterns for Android (kotlin-language-patterns, beginner)
Idiomatic Kotlin used throughout Android code — null safety, data/sealed classes, scope and extension functions; coroutines/Flow are their own Topic.
- Null safety: ?, !!, and why Kotlin kills a class of NPEs
- Data classes: equals/hashCode/copy for free
- Sealed classes for modeling UI state: Loading, Success, Error
- Code: a screen's UI state modeled as a sealed class
- Extension functions: adding behavior without inheritance
- Scope functions: let, apply, run, also, and with
- Sealed class vs enum for representing a fixed set of states
- Pitfall: overusing !! and reintroducing the NPEs Kotlin was meant to prevent
- Pitfall: an extension function that shadows a member and confuses readers

---

## Group: iOS Development (ios)

### Topic: App & Scene Lifecycle on iOS (app-scene-lifecycle-ios, beginner)
UIKit's concrete app-state delegate callbacks and multi-scene/multi-window handling; the cross-platform state model lives in Mobile Fundamentals.
- App states: not running, inactive, active, background, suspended
- Diagram: the app lifecycle state machine and its delegate callbacks
- AppDelegate vs SceneDelegate: who owns what since multi-window
- Code: handling entering background to save state in time
- Background execution time: the seconds you get before suspension
- State restoration across a termination
- Pitfall: assuming applicationWillTerminate always runs
- Pitfall: starting a long task in applicationDidEnterBackground with no time limit

### Topic: UIViewController Lifecycle & View Hierarchy (uiviewcontroller-lifecycle, beginner)
The concrete UIKit view-controller callback sequence and containment; SwiftUI's equivalent lives in its own Topic.
- The UIViewController lifecycle methods in order
- Diagram: view controller lifecycle vs view hierarchy loading
- viewDidLoad vs viewWillAppear: what belongs in each
- Container view controllers: navigation, tab bar, and child VCs
- Code: passing data forward and back between view controllers
- Pitfall: doing layout-dependent work in viewDidLoad before frames are set
- Pitfall: a strong parent-child view controller reference cycle

### Topic: SwiftUI Fundamentals (swiftui-fundamentals, intermediate)
The declarative rendering model — View as a function of state, and view identity; UIKit interop and state ownership are their own Topics.
- Views as a function of state: SwiftUI's declarative model
- Diagram: a state change flowing through the view tree to a re-render
- @State, @Binding, and who owns the source of truth
- View identity: how SwiftUI decides to update vs recreate a view
- Code: a stateful counter view using @State and a binding
- SwiftUI vs UIKit for a new feature
- Pitfall: mutating state off the main actor and missing updates
- Pitfall: an overly large body causing expensive diffing on every change

### Topic: State Management — Combine & Observation (state-management-combine-observation, intermediate)
ObservableObject/@Published, Combine pipelines, and the newer Observation framework; Android's parallel (coroutines/Flow) is its own Topic in that group.
- ObservableObject and @Published: pushing state changes to views
- Diagram: a Combine pipeline from a publisher to a subscribed view
- Combine operators: map, filter, debounce, combineLatest
- Code: debouncing a search field with Combine
- The Observation framework: what changed vs ObservableObject
- Combine vs async/await for a one-shot network call
- Pitfall: a memory leak from a Combine subscription with no stored cancellable
- Pitfall: overusing @Published and triggering redraws for irrelevant state

### Topic: Memory Management — ARC, Retain Cycles & Closures (memory-management-arc-retain-cycles, advanced)
How ARC counts references and the concrete patterns that create and break retain cycles in Swift.
- ARC: how Swift counts references without a tracing garbage collector
- Diagram: a strong reference cycle between two objects
- Strong vs weak vs unowned: choosing the right reference
- Code: a closure retain cycle fixed with [weak self]
- Delegate patterns and why delegates are almost always weak
- Detecting leaks with Instruments' memory graph
- Pitfall: using unowned when the referenced object can legitimately outlive it
- Pitfall: capturing self strongly in a long-lived escaping closure

### Topic: Concurrency — GCD & Swift Structured Concurrency (concurrency-gcd-structured-concurrency, intermediate)
Dispatch queues, async/await, actors, and Task as Swift's concrete concurrency model; general async-model theory lives in Languages & Compilers.
- GCD queues: serial vs concurrent, and the main queue's special role
- Diagram: dispatching work off the main queue and back
- async/await: replacing nested completion handlers
- Code: an async function calling a network client and updating UI
- Actors: how Swift protects mutable state from data races
- GCD vs structured concurrency for a new codebase
- Task and task groups: structured child work with cancellation
- Pitfall: calling an async function and forgetting it needs a Task context
- Pitfall: updating UI from a background queue without hopping to main

### Topic: Auto Layout & Adaptive UI (auto-layout-adaptive-ui, intermediate)
UIKit's constraint-based layout system and adapting across screen sizes; the cross-platform responsive-layout concept lives in Mobile Fundamentals.
- Auto Layout's model: constraints as a system of equations
- Diagram: a constraint conflict and how the layout engine resolves priority
- Stack Views vs raw constraints: when each is simpler
- Code: pinning a view to the safe area with layout anchors
- Size classes: adapting layout across iPhone and iPad
- Pitfall: ambiguous layout from under-constrained views
- Pitfall: hardcoding pixel offsets that break across screen sizes

### Topic: iOS Persistence — Core Data & SwiftData (core-data-swiftdata-persistence, intermediate)
Core Data's object-graph model and SwiftData as its modern replacement; the cross-platform storage decision framework lives in Mobile Fundamentals.
- Core Data's model: managed objects, contexts, and the persistent store
- Diagram: the Core Data stack from model to SQLite file
- Code: fetching and saving objects with a managed object context
- SwiftData: the same ideas with a Swift-native, macro-based API
- Core Data vs SwiftData vs a plain SQLite wrapper
- Lightweight vs custom migrations when the model changes
- Pitfall: accessing a managed object across threads without its own context
- Pitfall: an unbatched fetch request that loads an entire table

---

## Group: Cross-Platform (cross-platform)

### Topic: Cross-Platform Rendering Models (cross-platform-rendering-models, intermediate)
How Flutter and React Native actually get pixels on screen, and the native/hybrid/self-rendered framing behind every cross-platform trade-off.
- Three strategies: fully native, hybrid-native, and self-rendered
- Diagram: Flutter's widget-to-Skia pipeline vs React Native's native-view bridge
- Why Flutter looks pixel-identical across platforms and native apps don't
- Flutter's Skia/Impeller rendering vs React Native's native components
- The bridge/JS-to-native boundary and where it costs performance
- React Native's New Architecture: JSI replacing the async bridge
- Pitfall: assuming "cross-platform" means zero platform-specific code
- Pitfall: judging a framework's performance from one janky demo instead of the real bottleneck

### Topic: Flutter & Dart Fundamentals (flutter-dart-fundamentals, intermediate)
The widget tree, build method, and state-management landscape in Flutter.
- Everything is a widget: composing UI from small pieces
- Diagram: the widget tree, element tree, and render tree
- StatelessWidget vs StatefulWidget
- Code: a StatefulWidget counter using setState
- The build method and why it must stay fast and pure
- State management options at a glance: setState, Provider, Riverpod, Bloc
- Pitfall: calling setState on a widget that's already disposed
- Pitfall: rebuilding an expensive subtree because state lives too high up

### Topic: React Native Fundamentals (react-native-fundamentals, intermediate)
React's component model applied to native primitives, and how JavaScript reaches native code.
- React Native's component model: React's rules, native primitives
- Diagram: the JavaScript thread, the native thread, and the bridge between them
- Code: a functional component with hooks driving native views
- Native modules: calling platform APIs from JavaScript
- Hermes vs JavaScriptCore as the JS engine
- Styling with Flexbox: React Native's layout model
- Pitfall: blocking the JS thread with heavy synchronous work
- Pitfall: passing a new function/object prop every render and defeating memoization

### Topic: Choosing Native vs Cross-Platform (choosing-native-vs-cross-platform, intermediate)
The decision framework a team should actually reason through — not framework hype, but constraints.
- The real trade-off: engineering velocity vs platform fidelity
- Diagram: a decision tree from product requirements to a framework choice
- When native wins: heavy graphics, deep platform integration, camera/AR-first apps
- When cross-platform wins: content-driven apps, small teams, fast iteration
- Total cost of ownership: two native codebases vs one shared codebase plus patches
- Sharing business logic without a shared UI framework, via a shared core module
- Pitfall: picking a framework by hype instead of the team's actual constraints
- Pitfall: underestimating the platform-specific code cross-platform apps still need

### Topic: Cross-Platform Performance & Native Interop (cross-platform-performance-native-interop, advanced)
Diagnosing jank in a cross-platform app and writing native modules/platform channels when the framework falls short.
- Where cross-platform performance actually breaks down
- Diagram: a platform-channel call from Flutter/React Native into native code and back
- Code: a native module exposing a platform API to JavaScript
- Profiling a cross-platform app: framework tools vs native profilers
- Falling back to a native module vs waiting on a framework feature
- Pitfall: crossing the bridge/channel per-frame for something that should be batched
- Pitfall: shipping a native module that works on one platform and crashes on the other

---

## Group: Mobile System Design (mobile-system-design)

### Topic: Mobile Client Architecture Patterns (mobile-client-architecture-patterns, intermediate)
Layering a whole app — presentation/domain/data — and module boundaries, one level above any single screen's MVVM.
- Layering a mobile app: presentation, domain, data
- Diagram: a clean-architecture-style dependency flow on mobile
- MVVM vs MVI vs Clean Architecture at the whole-app level
- Feature modularization: why large apps split into independent modules
- The data layer's job: one source of truth behind repositories
- Single-module vs multi-module app trade-offs
- Pitfall: a "God" repository every feature depends on directly
- Pitfall: business logic leaking into the UI layer because it was the fastest path

### Topic: Offline-First Design (offline-first-design, intermediate)
Designing so the app is fully usable with no network, local database as source of truth, optimistic UI; storage tech choice itself lives in Mobile Fundamentals.
- Offline-first vs "offline-tolerant": a real distinction
- Diagram: local database as the single source of truth, server as sync target
- Optimistic UI: showing a change before the server confirms it
- Code: an optimistic update with a rollback path on failure
- Queuing writes made while offline for later sync
- Offline-first vs cache-then-network vs network-only
- Pitfall: showing stale data with no visible "syncing" or "stale" indicator
- Pitfall: an optimistic update with no rollback when the server rejects it

### Topic: Data Synchronization & Conflict Resolution (data-sync-conflict-resolution, advanced)
Sync protocols and conflict strategies applied to a mobile client; general consistency/replication theory lives in System Design (HLD).
- Full sync vs delta/incremental sync
- Diagram: two devices syncing deltas through a server
- Detecting changes: timestamps, version numbers, and vector clocks
- Conflict resolution strategies: last-write-wins, field-level merge, manual resolution
- CRDTs at a glance: conflict-free structures for collaborative data
- Code: a sync loop that pushes local changes then pulls remote ones
- Server-authoritative vs peer-to-peer sync models
- Pitfall: a naive last-write-wins that silently discards a user's edit
- Pitfall: a sync loop with no idempotency key that double-applies a change on retry

### Topic: Mobile API Design & Backend-for-Frontend (mobile-api-design-bff, intermediate)
Shaping APIs for mobile constraints and a BFF aggregation layer; general API-design theory lives in System Design (HLD).
- Why a mobile client needs a different API shape than a web dashboard
- Diagram: a Backend-for-Frontend aggregating multiple services for one screen
- Payload shaping: sending only what the screen needs
- Pagination and prefetching for infinite-scroll screens
- BFF-per-platform vs one general-purpose API for everyone
- Versioning an API that old, un-updatable clients still call
- Code: a paginated endpoint response shape with a next-page cursor
- Pitfall: a chatty screen making five sequential calls a BFF could collapse to one
- Pitfall: an API version bump that silently breaks the last 10% of installs

### Topic: Caching & Prefetching Strategy for Mobile Clients (caching-prefetching-mobile-clients, intermediate)
Multi-layer client caching and predictive prefetch; general caching theory lives in System Design (HLD) — this is the client-side application.
- The client-side cache hierarchy: memory, disk, CDN, origin
- Diagram: a request's path through each cache layer
- Cache invalidation strategies a mobile client can actually use
- Time-based expiry vs server-driven cache headers vs push-invalidation
- Prefetching: loading the next likely screen before the user asks
- Code: an image loader with memory and disk cache tiers
- Pitfall: an unbounded disk cache that slowly fills the user's storage
- Pitfall: prefetching aggressively on a metered connection and burning user data

### Topic: Designing a Mobile Client — Chat/Messaging App (design-mobile-client-chat-app, advanced)
A worked case study synthesizing the group: message send/receive, offline queue, delivery receipts, real-time updates.
- Framing the problem: what "design a chat client" is really asking
- Diagram: the chat client's architecture — local DB, sync engine, real-time channel
- Sending a message: optimistic insert, queue, server ack
- Receiving messages: a persistent connection vs push-triggered fetch
- Delivery and read receipts: modeling per-message state
- Handling offline: queuing outgoing messages and replaying on reconnect
- Code: a message's local states from pending to sent to delivered
- Pitfall: showing a message as "sent" before the server has actually accepted it
- Pitfall: no de-duplication, so a retried send shows the message twice

### Topic: Designing a Mobile Client — Feed/Content App (design-mobile-client-feed-app, advanced)
A second worked case study focused on pagination, prefetch, and offline reading rather than real-time messaging.
- Framing the problem: what "design a feed client" is really asking
- Diagram: the feed client's architecture — paged cache, prefetcher, action queue
- Paginating and caching a feed for smooth infinite scroll
- Code: merging a freshly fetched page with an already-cached feed without duplicates
- Optimistic likes/comments and reconciling with the server's real count
- Offline reading: what to prefetch so the feed works on a subway
- Pull-to-refresh vs background-refreshed feeds
- Pitfall: a like button that flickers from a race between optimistic and server state
- Pitfall: re-fetching page 1 on every app open and losing scroll position

---

## Cross-links & Overlap Notes

- **Mobile Security Fundamentals** (mobile-fundamentals) applies crypto/auth/OWASP theory from Area 13 Security (`cryptography`, `authn-authz`, `appsec`) to a mobile client; it does not re-teach the theory.
- **Battery & Background Limits** and **Push Notifications** (mobile-fundamentals) give the cross-platform concept; concrete APIs (WorkManager, Background Tasks framework, APNs/FCM SDKs) live in Android/iOS.
- **Local Storage Options** (mobile-fundamentals) gives the decision framework; Room usage lives in Android's architecture/DI topics, Core Data/SwiftData is its own iOS Topic.
- **Data Sync, Mobile API Design/BFF, and Caching** (mobile-system-design) apply Area 7 System Design theory (`consistency-replication`, `api-design`, `caching`) to a mobile client rather than re-deriving it.
- **Mobile UX Constraints & Accessibility** (mobile-fundamentals) is the mobile-native counterpart to Area 14 Web & Frontend's `accessibility` (ARIA/WCAG is web-specific; TalkBack/VoiceOver here).
- **Cross-Platform Rendering Models** references Compose/SwiftUI's declarative model (taught fully in Android/iOS) only for comparison, not re-teaching.
- **Kotlin Coroutines & Flow** (Android) and **GCD & Structured Concurrency** (iOS) are parallel, platform-specific topics — not overlapping each other; general async-model theory lives in Area 6 Languages & Compilers (`concurrency-models`).
- **Dependency Injection with Hilt** (Android) references DI as a general principle from Area 8 Object-Oriented Design (`design-principles`) but is scoped to Hilt's concrete mechanics.
- No gaps against the group scopes in the map: mobile-fundamentals covers lifecycle/storage/networking/battery (plus security/notifications/distribution/UX as adjacent must-haves for a complete fundamentals track); mobile-system-design covers offline-first/sync/"design a mobile client" (plus API design and caching as the supporting must-haves) with two worked case studies (chat, feed) so the pattern isn't taught in the abstract only.
