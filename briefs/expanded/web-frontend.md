# Area: Web & Frontend (web-frontend)

Reference outline (draft, pending human review) — expands each Group from `briefs/area-group-map.md` Area 14
two levels: Topics, then a slide-heading outline per Topic. Groups and slugs are taken exactly from the map;
nothing invented or pulled from other areas.

**Cross-area boundaries (see map's "Overlap flags"):**
- `web-security` (this area) covers only browser-enforced, client-side mechanisms (XSS, CSRF from the client,
  CSP, clickjacking, token storage, third-party script risk). Server-side input validation/OWASP Top 10 lives
  in Area 13 (`appsec`); TLS handshake mechanics and network-layer attacks live in Area 4 (`network-security`)
  / Area 13 (`netsec`). Flagged in the map as needing a granularity decision — this outline resolves it as above.
- Deep DNS/TCP/TLS mechanics are Area 4 (`computer-networks`); this area only covers them at the depth a
  frontend engineer needs (e.g. inside `url-to-page-lifecycle`).
- Deep GC/interpreter internals stay language-general in this area's own `javascript` group; `browser-performance`
  only covers the browser-observable, SPA-specific symptoms (see `long-session-spa-perf`'s cross-link note).

---

## Group: Web Fundamentals (web-fundamentals)

*Tier 🔵 — HTTP, browser, DOM, rendering path.*

### Topic: How Browsers Work (how-browsers-work, beginner)
How a browser is put together — engines, multi-process architecture, and why that shapes everything else in this area.
- What a browser actually is: engine + rendering engine + JS engine + UI shell
- Multi-process architecture: browser process, renderer process, GPU process, network process
- Why tabs get their own process: crash isolation and site isolation
- Renderer internals: main thread vs compositor thread
- The JavaScript engine's role: parsing, bytecode, JIT compilation
- Sandboxing: why renderer processes are untrusted by design
- Same browser, different engines: Blink vs Gecko vs WebKit — what actually differs
- Pitfall: assuming one page = one process always (site isolation exceptions)
- Interview angle: "walk me through what a browser is doing right now"

### Topic: URL-to-Page Lifecycle (url-to-page-lifecycle, beginner)
The full "type a URL, hit Enter" journey from the browser's point of view, from parsing to first bytes rendered.
- The classic interview question: what happens when you type a URL and press Enter
- Step 1: URL parsing — scheme, host, path, query
- Step 2: DNS resolution at a glance (cross-link: full mechanics in `computer-networks`)
- Step 3: connection setup — TCP handshake + TLS negotiation, briefly
- Step 4: sending the HTTP request — headers a browser adds automatically
- Step 5: server response — the browser starts parsing HTML immediately (streaming parse)
- Step 6: fetching subresources — preload scanner, request priority
- Diagram: full navigation timeline from keypress to first paint
- Redirects, HSTS, and cached navigations — what changes
- Pitfall: assuming the whole page loads before anything renders
- Interview angle: answering this question at the right depth for the level asked

### Topic: The DOM and CSSOM (dom-and-cssom, beginner)
How HTML and CSS parsing produce the DOM and CSSOM trees the rest of rendering builds on.
- What the DOM really is: a live tree, not "the HTML"
- HTML parsing: tokenizing, tree construction, error recovery
- Why the DOM parser never truly "fails" — malformed HTML handling
- CSSOM construction: cascade, specificity, inheritance tied to parsing
- Diagram: HTML + CSS producing a DOM tree and a CSSOM tree
- The `<script>` tag problem: why scripts block parsing
- `defer` vs `async` vs plain `<script>` — parsing impact compared
- Code: minimal DOM traversal and manipulation via the DOM APIs
- Pitfall: mutating the DOM in a loop and forcing synchronous layout

### Topic: The Critical Rendering Path (critical-rendering-path, intermediate)
How DOM + CSSOM become pixels — render tree, layout, paint, composite — and what blocks it.
- From DOM + CSSOM to pixels: building the render tree
- Layout (reflow): computing geometry
- Paint: filling in pixels layer by layer
- Compositing: why layers exist and how the GPU helps
- Diagram: the full critical rendering path pipeline
- Render-blocking resources: CSS in `<head>`, synchronous JS
- Techniques to shorten the path: critical CSS, deferring non-critical JS
- Compare: render-blocking vs parser-blocking vs non-blocking resource loading
- Pitfall: a `<link>` in body, or late-injected CSS-in-JS, silently re-triggering layout
- Interview angle: "how would you speed up first paint on this page"

### Topic: HTTP for Frontend Engineers (http-for-frontend, intermediate)
The HTTP surface a frontend engineer actually touches — methods, status codes, headers, and browser caching semantics.
- HTTP request/response anatomy from the frontend's seat
- Methods that matter for frontend devs: GET/POST/PUT/PATCH/DELETE, idempotency
- Status codes you'll actually handle in fetch/XHR error paths
- Headers frontend code reads and sets: Content-Type, Authorization, Accept
- Caching headers: Cache-Control, ETag, Last-Modified — fresh vs revalidate vs miss
- Diagram: browser cache decision flow
- Compare: cache-first vs network-first patterns and when each fits
- Code: `fetch` with cache-control-aware options and abort/timeout handling
- Pitfall: treating a 200 served from cache as "fresh data" when it's stale

### Topic: Cookies and Web Storage (cookies-and-web-storage, intermediate)
Cookies, localStorage, sessionStorage, and IndexedDB — lifetime, scope, and which to reach for.
- The four browser storage options and what each is actually for
- Cookies: attributes that matter — `HttpOnly`, `Secure`, `SameSite`, expiry
- localStorage vs sessionStorage: lifetime, scope, synchronous API cost
- IndexedDB: when you outgrow key-value storage
- Diagram: storage lifetime and scope side by side
- Why cookies (not storage) are the only thing sent automatically with requests
- Code: reading/writing each storage type safely, handling quota errors
- Pitfall: storing JWTs in localStorage vs cookies — the XSS/CSRF trade-off (cross-link: `secure-storage-and-tokens`)
- Interview angle: "where would you store an auth token, and why"

### Topic: Same-Origin Policy and CORS (same-origin-policy-and-cors, intermediate)
Why origins are isolated by default and how CORS deliberately punches a hole in that isolation.
- What "origin" actually means: scheme + host + port
- Why the Same-Origin Policy exists: the threat it stops
- Simple requests vs preflighted requests
- Diagram: the CORS handshake — `Origin`, `Access-Control-Allow-Origin`, preflight `OPTIONS`
- Credentialed requests: cookies + CORS, `Access-Control-Allow-Credentials`
- Code: reading a real CORS error in devtools and fixing it
- Compare: CORS vs a proxy vs JSONP (legacy) as workarounds
- Pitfall: `Access-Control-Allow-Origin: *` with credentials — why browsers reject it
- Cross-link: deeper XSS/CSRF implications live in the `web-security` group

### Topic: Service Workers and Offline (service-workers-and-offline, advanced)
The service worker as a network proxy in the browser, caching strategies, and building offline-capable pages.
- What a service worker is: a programmable network proxy in the browser
- Diagram: lifecycle — install, activate, fetch — and why updates are tricky
- Caching strategies: cache-first, network-first, stale-while-revalidate
- Code: a minimal service worker implementing stale-while-revalidate
- The Cache API vs the HTTP cache — who's in control
- Building a basic PWA: manifest, install prompts, offline fallback page
- Pitfall: a stale service worker holding back new deploys (the "zombie" SW)
- Interview angle: "make this app work offline" — the design conversation

---

## Group: HTML/CSS & Layout (html-css)

*Tier 🟡 — box model, flex/grid, responsive.*

### Topic: Box Model and Layout Basics (box-model-and-layout-basics, beginner)
Content/padding/border/margin, box-sizing, and how block/inline/inline-block participate in normal flow.
- Diagram: the box model — content, padding, border, margin
- `box-sizing: content-box` vs `border-box` — why border-box is the sane default
- Block vs inline vs inline-block: how each participates in layout
- Margin collapsing: when adjacent margins merge and why it surprises people
- Code: resetting box-sizing globally, and why teams do it
- The normal flow: how elements lay out with no positioning/flex/grid applied
- Interview angle: "why isn't my width doing what I expect" — box-model debugging

### Topic: Positioning and Stacking Contexts (positioning-and-stacking, beginner)
The position property, what it removes from flow, and how stacking contexts actually govern z-index.
- The five `position` values and what each removes from flow
- `relative` as a double-duty tool: nudging and anchoring absolute children
- `sticky` positioning: the scroll-container gotchas
- Pitfall: stacking contexts — what creates one and why z-index "doesn't work"
- Diagram: a stacking-context tree with nested z-index examples
- Code: a sticky header and dropdown fighting over z-index, and the fix
- Compare: `fixed` vs `sticky` vs `absolute` for common UI patterns

### Topic: Flexbox (flexbox, beginner)
The one-dimensional flex model — axes, growth/shrink/basis — for the layouts it's built for.
- The flex model: container, items, main axis vs cross axis
- `justify-content` vs `align-items` vs `align-content` — which axis each controls
- `flex-grow`/`flex-shrink`/`flex-basis` — how items share extra or missing space
- Diagram: a row of items with different flex values and their resulting sizes
- Code: perfectly centering something with flexbox
- Code: equal-height columns / sticky footer pattern
- Pitfall: flex items not shrinking because of the default `min-width: auto`
- Interview angle: build a responsive navbar live with flexbox

### Topic: CSS Grid (css-grid, intermediate)
The two-dimensional grid model — tracks, areas, gaps — and when it beats flexbox.
- The grid model: tracks, lines, areas, gaps
- Defining tracks: `fr` units, `repeat()`, `minmax()`
- Code: `grid-template-areas` for naming layout regions
- Diagram: a dashboard layout defined with named grid areas
- Implicit vs explicit grid: what happens when content overflows defined tracks
- Compare: flexbox vs grid — one-dimensional vs two-dimensional, when to reach for which
- Code: a responsive card grid using `auto-fill`/`auto-fit` with `minmax`
- Pitfall: mixing grid and flex unnecessarily where one would do

### Topic: Responsive Design (responsive-design, intermediate)
Building layouts that adapt across viewports — media queries, fluid units, and container queries.
- Mobile-first vs desktop-first media queries
- Common breakpoint strategy: content-based, not device-based
- Compare: `%`, `vw`/`vh`, `rem` vs `px` — when each unit is right
- Container queries: styling by parent size, not viewport size
- Diagram: the same component at three breakpoints via container queries
- Code: responsive images with `srcset`, `sizes`, and `<picture>` for art direction
- Code: `clamp()` for fluid typography
- Pitfall: using viewport units for font-size without clamping min/max
- Interview angle: "make this card component responsive" live exercise

### Topic: The Cascade and Specificity (css-cascade-and-specificity, intermediate)
How the cascade resolves competing styles, and taming it with layers instead of `!important`.
- The cascade: origin, importance, specificity, source order — in that priority
- Calculating specificity: ID vs class vs element, the tuple mental model
- Pitfall: `!important` as an escape hatch, not a tool
- Cascade layers (`@layer`): taming specificity wars in large codebases
- Diagram: specificity-tuple comparison for a tricky selector clash
- Inheritance: which properties inherit by default, and forcing it with `inherit`/`initial`/`unset`
- Code: debugging "why is this style not applying" using computed styles

### Topic: CSS Architecture at Scale (css-architecture-at-scale, advanced)
Scoping strategies (BEM, CSS Modules, CSS-in-JS, utility-first) for CSS in a large, multi-team codebase.
- The scoping problem: global CSS doesn't survive past a few pages
- BEM: naming convention as a scoping discipline
- CSS Modules: build-time scoping via generated class names
- CSS-in-JS: runtime/build-time styling tied to components
- Utility-first (Tailwind-style): trading semantic classes for composition speed
- Compare: BEM vs CSS Modules vs CSS-in-JS vs utility-first — bundle size, DX, runtime cost
- Diagram: where each approach resolves styles — build time vs runtime
- Interview angle: "how would you structure CSS for a 200-component design system"

### Topic: Forms and Validation (forms-and-validation, intermediate)
Semantic form markup, native validation, and the client/server validation split.
- Semantic form elements, and why `<div onclick>` isn't a button
- Native HTML validation: `required`, `pattern`, `min`/`max`, `:invalid` styling
- Code: custom validation with the Constraint Validation API
- Accessible error messaging: associating errors with fields (cross-link: `accessible-forms-and-errors`)
- Controlled vs uncontrolled form inputs (framework version: `component-model-basics`)
- Diagram: form submission lifecycle — client validation, network, server validation
- Pitfall: relying on client-side validation alone (security and UX both break)

---

## Group: JavaScript & TypeScript (javascript)

*Tier 🔵 — event loop, closures, async, types.*

### Topic: Execution Context and Scope (execution-context-and-scope, beginner)
Execution contexts, the scope chain, hoisting, and the `var`/`let`/`const` + TDZ distinctions.
- What an execution context is: global vs function vs eval
- The scope chain: how variable lookup resolves through outer scopes
- Hoisting: what actually moves up — declarations, not assignments
- Compare: `var` vs `let`/`const` — function scope vs block scope
- Pitfall: the Temporal Dead Zone — why `let`/`const` throw before hoisting completes
- Diagram: creation phase vs execution phase of a context
- Code: a hoisting trap in a loop, `var` vs `let`
- Global scope pollution: why it matters in browsers (`window`)
- Interview angle: predict-the-output questions on hoisting and TDZ

### Topic: Closures (closures, beginner)
What a closure captures and why, with the practical patterns (private state, memoization) it enables.
- What a closure actually is: a function plus its lexically captured scope
- Diagram: a closure retaining a reference to an outer variable after the outer function returns
- Code: private state without classes (the module pattern)
- Code: memoization via a closure-held cache
- Pitfall: the classic loop-with-`var`-and-`setTimeout` interview trap
- Code: fixing it with `let`, an IIFE, or explicit parameter binding
- Pitfall: closures keeping large objects alive longer than expected
- Interview angle: "write a counter/debounce function using closures"

### Topic: `this` and Function Context (this-and-function-context, beginner)
The four `this`-binding rules and how arrow functions opt out of them.
- How `this` is determined: call-site binding, not definition-site
- The four binding rules: default, implicit, explicit, `new`
- Code: `call`/`apply`/`bind` — borrowing functions and fixing `this`
- Arrow functions: lexical `this`, and why they can't be rebound
- Diagram: a `this`-resolution decision tree for a given call site
- Pitfall: losing `this` when passing a method as a callback
- Code: fixing a detached event handler's `this` with `bind` vs an arrow function
- Interview angle: predict `this` across nested objects and callbacks

### Topic: Prototypes and Inheritance (prototypes-and-inheritance, intermediate)
The prototype chain, what `class` desugars to, and prototypal vs classical inheritance mental models.
- The prototype chain: how property lookup falls through to `Object.prototype`
- `__proto__` vs `prototype` vs `Object.getPrototypeOf` — the naming confusion
- Diagram: the prototype chain for an instance created via a constructor function
- `class` syntax as sugar over prototypes — what it desugars to
- Code: `Object.create` for direct prototypal inheritance without classes
- Overriding and shadowing: own properties vs inherited ones
- Compare: classical (class-based) vs prototypal mental models
- Pitfall: mutating a shared prototype method's object argument

### Topic: The Event Loop and Async Execution (event-loop-and-async, intermediate)
The call stack, Web APIs, microtask vs macrotask queues, and why microtasks always run first.
- The call stack: synchronous execution, one frame at a time
- Where async work actually runs: Web APIs / Node APIs, not the JS engine
- Task queue (macrotasks) vs microtask queue — and why microtasks always win
- Diagram: the full event loop — call stack, Web APIs, microtask queue, macrotask queue
- Code: predict-the-output with mixed `setTimeout`, `Promise.then`, and sync code
- `requestAnimationFrame` and where it fits relative to micro/macrotasks
- Pitfall: an infinite microtask queue starving rendering
- Compare: Node's event loop phases vs the browser's, at a high level
- Interview angle: the canonical "order of execution" whiteboard question

### Topic: Promises and Async/Await (promises-and-async-await, intermediate)
The Promise contract, combinators (`all`/`race`/`allSettled`/`any`), and async/await's error-handling patterns.
- The Promise contract: pending to fulfilled/rejected, exactly once
- Chaining `.then`: return values, thrown errors, and flattening nested promises
- Compare: `Promise.all` vs `allSettled` vs `race` vs `any` — failure semantics
- Diagram: `Promise.all` short-circuiting on first rejection vs `allSettled` waiting for all
- `async`/`await` as sugar over promises — what the transpiled version looks like
- Code: `try/catch` around `await` vs `.catch` chains
- Pitfall: sequential `await` in a loop when parallel would do
- Pitfall: an unhandled promise rejection silently swallowing an error
- Code: implementing a simple `Promise.all` from scratch

### Topic: The JS Runtime and Memory (js-runtime-and-memory, advanced)
Stack vs heap, garbage collection, and the common ways frontend code leaks memory.
- Stack vs heap: primitives vs reference types
- Garbage collection basics: mark-and-sweep, reachability
- Diagram: a reference graph with an unreachable cycle getting collected
- Pitfall: common leak sources — detached DOM nodes, forgotten timers/listeners, growing closures
- `WeakMap`/`WeakSet`: letting the GC collect keys you don't own
- Code: fixing a listener-based memory leak in a component teardown
- Profiling: reading a heap snapshot at a high level
- Interview angle: "this page's memory grows over time — how do you find why"

### Topic: Modules and Bundling Basics (modules-and-bundling-basics, intermediate)
CommonJS vs ESM, static vs dynamic imports, and how module structure enables tree-shaking.
- Compare: CommonJS (`require`/`module.exports`) vs ES Modules (`import`/`export`)
- Static vs dynamic module resolution — why ESM enables tree-shaking
- Code: `import()` dynamic import for code-splitting
- Diagram: a dependency graph and which branches get tree-shaken
- Pitfall: circular dependencies — what happens and how each module system handles it
- Compare: named vs default exports — API design trade-offs for a library
- Interview angle: "how does tree-shaking actually eliminate code"

### Topic: The TypeScript Type System (typescript-type-system, intermediate)
Structural typing, interfaces vs type aliases, generics, and unions/intersections.
- Structural typing ("duck typing") vs nominal typing — TS's core model
- Compare: `interface` vs `type` alias — where they differ, where they don't
- Union and intersection types: modeling "or" and "and"
- Code: generics in a reusable typed function or component
- Diagram: type-narrowing flow through a series of guards
- Type inference: when to let TS infer vs when to annotate
- Pitfall: over-using `any` and losing the point of TypeScript
- Interview angle: type a generic `useState`-like function or a typed API client

### Topic: Advanced TypeScript Types (typescript-advanced-types, advanced)
Utility types, conditional and mapped types, and narrowing with `unknown`/discriminated unions.
- Utility types: `Partial`, `Pick`, `Omit`, `Record` — what each solves
- Conditional types: `T extends U ? X : Y` and distributive conditionals
- Code: mapped types building new object types from existing ones
- Compare: `unknown` vs `any` vs `never` — safety trade-offs
- Type narrowing: `typeof`, `instanceof`, discriminated unions
- Diagram: a discriminated union narrowed inside a `switch`
- Pitfall: type assertions (`as`) hiding a real runtime mismatch
- Code: a type-safe event emitter using mapped and conditional types

---

## Group: Frontend Frameworks (frameworks)

*Tier 🟡 — component model, state, reactivity.*

### Topic: Component Model Basics (component-model-basics, beginner)
What a component is, props vs state ownership, composition, and unidirectional data flow.
- What a component is: a function of data (props/state) to UI
- Compare: props vs state — who owns the data, who can change it
- Composition over inheritance: building complex UI from small components
- Diagram: unidirectional data flow — data down, events up
- Code: a parent-child component passing props and a callback
- Controlled vs presentational vs container components
- Pitfall: mutating props directly instead of lifting state
- Interview angle: "design the component tree for this UI mockup"

### Topic: State Management Fundamentals (state-management-fundamentals, beginner)
Local vs lifted state and deciding where a given piece of state should live.
- Local state: when a component's own state is enough
- Lifting state up: sharing state between siblings via a common parent
- Diagram: state lifted from two sibling components into a shared parent
- Derived state: computing values instead of storing redundant state
- Pitfall: syncing two sources of truth with an effect instead of deriving
- Code: lifting form state up to validate across two fields
- Interview angle: "where should this piece of state live" — the decision process

### Topic: Reactivity Models (reactivity-models, intermediate)
Virtual-DOM diffing vs fine-grained (signal-based) reactivity — how each detects and applies changes.
- Virtual DOM: render a full tree in memory, diff, patch the real DOM
- Fine-grained reactivity (signals): tracking exactly which values changed
- Diagram: virtual-DOM diffing vs signal-based dependency tracking, side by side
- Compare: React's re-render-then-diff vs Vue/Svelte's compiled reactivity
- Why fine-grained reactivity can skip the diffing step entirely
- Compare: developer mental-model simplicity vs raw update performance
- Interview angle: "why does React re-render a whole subtree by default"

### Topic: Rendering and Reconciliation (rendering-and-reconciliation, intermediate)
How a framework turns a new element tree into minimal DOM operations, and why `key` matters.
- Reconciliation: turning a new element tree into minimal DOM operations
- The diffing heuristics: same type updates in place, different type replaces
- Why `key` matters in lists: stable identity across re-renders
- Diagram: reordering a keyed list vs an unkeyed list — DOM operations compared
- Pitfall: using array index as `key`, and the subtle bugs it causes
- Code: a list re-render bug caused by missing/wrong keys, and the fix
- Interview angle: "why did my component's internal state end up on the wrong row"

### Topic: Hooks and Lifecycle (hooks-and-lifecycle, intermediate)
Mapping mount/update/unmount to hooks, dependency arrays, cleanup, and the Rules of Hooks.
- Mapping class lifecycle (mount/update/unmount) to hooks
- `useEffect` dependency arrays: what "reactive" really means here
- Diagram: effect timing relative to render and paint
- Code: cleanup functions preventing leaks from subscriptions/timers
- The Rules of Hooks: why hooks can't be conditional, and what breaks if they are
- Code: custom hooks extracting reusable stateful logic
- Pitfall: a missing dependency causing a stale closure inside an effect
- Interview angle: "why does this effect re-run every render" debugging exercise

### Topic: State Management at Scale (state-management-at-scale, advanced)
Context, external stores, and normalized state shape once prop drilling stops scaling.
- When local/lifted state stops being enough: prop-drilling pain
- Context: solving prop drilling, and its re-render cost
- External stores (Redux/Zustand-style): single source of truth, actions/reducers
- Diagram: data flow through a store — dispatch, reducer, subscribers
- Normalizing state shape: avoiding nested/duplicated data
- Compare: Context vs a dedicated store — when each is the right call
- Pitfall: putting everything in global state "just in case"
- Interview angle: "design the state layer for a Trello-like board"

### Topic: Performance in Frameworks (performance-in-frameworks, advanced)
Memoization, list virtualization, and diagnosing unnecessary re-renders with the profiler.
- Why components re-render: parent re-renders, state/prop changes
- `React.memo`/`useMemo`/`useCallback` — what each actually memoizes
- Diagram: a re-render cascade before and after memoization
- List virtualization: rendering only visible rows for long lists
- Code: windowing a 10,000-row list with a virtualization pattern
- Pitfall: memoizing everything with no measured gain, at a readability cost
- Profiling: using the framework devtools profiler to find the actual bottleneck
- Interview angle: "this list is janky when scrolling — diagnose and fix"

### Topic: Routing and Data Fetching (routing-and-data-fetching, intermediate)
Client-side routing and the fetch-on-render vs render-as-you-fetch data-loading spectrum.
- Client-side routing: intercepting navigation, history API basics
- Nested routes and layouts: matching URL segments to component trees
- Compare: fetch-on-render vs fetch-then-render vs render-as-you-fetch
- Diagram: a request waterfall from fetch-on-render vs a parallelized loader pattern
- Suspense-style loading states: coordinating multiple async boundaries
- Code: a route loader that fetches data before rendering the page
- Pitfall: waterfalled requests because a child fetches only after its parent finishes

### Topic: Framework Comparison (framework-comparison, intermediate)
React vs Vue vs Svelte's differing mental models for reactivity and rendering, compared fairly.
- Mental-model differences: React (re-render + VDOM) vs Vue (reactive refs) vs Svelte (compiled, no VDOM)
- Compare: bundle size and runtime cost trade-offs across the three
- Template syntax vs JSX vs compiled templates — authoring experience
- Diagram: where each framework's "reactivity work" happens — runtime vs compile time
- State management conventions: idiomatic patterns per framework
- When the choice actually matters vs when it's a team-preference call
- Interview angle: "you know React — explain how Svelte's approach differs"

---

## Group: Frontend System Design (frontend-system-design)

*Tier 🔵 — design a large SPA, perf budgets.*

### Topic: The Frontend System Design Framework (frontend-system-design-framework, intermediate)
The interview method for frontend HLD — requirements, component breakdown, data flow, API contract, non-functionals.
- Why frontend system design interviews differ from backend HLD
- Step 1: clarify requirements — devices, scale, offline needs, real-time-ness
- Diagram: step 2 — sketching the component/UI tree before any code
- Step 3: data flow — where state lives, what's server truth vs client truth
- Step 4: API contract — shaping requests around UI needs
- Step 5: non-functional concerns — performance, accessibility, offline, i18n
- Interview angle: a worked mini-example — framing "design a notifications widget" in four steps
- Pitfall: diving into component code before agreeing on data flow

### Topic: Component Architecture at Scale (component-architecture-at-scale, advanced)
Structuring a large codebase — feature-based organization, design systems, and monorepos.
- Structuring a codebase by feature vs by type
- Design systems: a shared component library as a product, not a folder
- Diagram: dependency direction between app code, feature modules, and the design system
- Monorepos: shared code across multiple frontend apps, tooling trade-offs
- Versioning a component library consumed by multiple teams
- Compare: monorepo vs polyrepo for a multi-team frontend org
- Pitfall: a "shared" component accumulating one-off props per consumer

### Topic: State and Data Layer Design (state-and-data-layer-design, advanced)
Splitting UI state from client cache from server cache, normalization, and optimistic updates.
- Splitting state into UI state, client cache, and server cache
- Diagram: a three-layer state model for a typical SPA
- Normalizing fetched data: entities by ID vs deeply nested API responses
- Compare: time-based, event-based, and tag-based cache-invalidation strategies
- Optimistic updates: updating the UI before the server confirms, then rolling back
- Code: an optimistic-update pattern with rollback on failure
- Pitfall: two components silently disagreeing because the cache wasn't the single source of truth
- Interview angle: "design the data layer for a Twitter-like feed with likes and replies"

### Topic: Micro-Frontends (micro-frontends, advanced)
Splitting a large app across teams — integration approaches, shared dependencies, and the trade-offs.
- What a micro-frontend is and the problem it solves: independent team deploys
- Compare: build-time, run-time (module federation), and server-side composition
- Diagram: a shell app composing three independently-deployed micro-frontends
- Shared dependencies: avoiding duplicate framework bundles across micro-frontends
- Cross-app communication: events, shared state, URL as contract
- Compare: team autonomy vs consistency, bundle duplication, operational complexity
- Pitfall: micro-frontends adopted for org reasons on a codebase too small to need them

### Topic: Performance Budgets (performance-budgets, intermediate)
Defining and enforcing hard limits (bundle size, LCP, TTI) tied to user-facing metrics.
- What a performance budget is: a hard limit tied to a user-facing metric
- Common budget targets: bundle size, TTI, LCP, request count
- Diagram: a budget dashboard tracking bundle-size trend per PR
- Code: enforcing budgets in CI, failing a build that exceeds the budget
- Code-splitting as the primary lever for staying under budget
- Compare: route-based vs component-based code splitting
- Pitfall: setting a budget once and never revisiting it as the app grows
- Interview angle: "this app's bundle doubled in six months — what do you do"

### Topic: Build and Deployment Pipeline (build-and-deployment-pipeline, intermediate)
Bundling, code-splitting strategy, cache-busting, and feature-flagged frontend rollouts.
- The bundler's job: resolve, transform, split, minify
- Code-splitting strategies: per-route, per-component, vendor chunk
- Diagram: a build pipeline from source to CDN-served chunks
- Cache-busting: content hashes in filenames and long-lived CDN caching
- Feature flags for frontend rollouts: shipping dark code safely
- Compare: client-side rendering vs SSR vs static generation — deploy implications
- Pitfall: a cached `index.html` serving stale asset references after a deploy

### Topic: Case Study — Design a News Feed (case-study-design-a-news-feed, advanced)
Worked example — infinite-scroll feed architecture: pagination, virtualization, live updates.
- Requirements: infinite scroll, mixed content types, real-time-ish updates
- Diagram: component breakdown — feed container, item renderer, loader sentinel
- Data fetching: cursor-based pagination from the client's perspective
- Virtualizing the feed: rendering only visible posts for long sessions
- Handling new posts arriving while the user is scrolled down
- Diagram: full data flow from scroll event to a rendered page of posts
- Pitfall: re-fetching page one and losing scroll position when a new post arrives
- Interview angle: the full worked answer, step by step, as in the room

### Topic: Case Study — Design a Collaborative Editor (case-study-design-a-collaborative-editor, advanced)
Worked example — a real-time collaborative editor's client architecture and conflict handling.
- Requirements: multiple cursors, low-latency edits, eventual consistency across clients
- Why last-write-wins breaks for concurrent text edits
- Compare: Operational Transformation vs CRDTs — conceptual difference, not the math
- Diagram: two clients editing concurrently and converging to the same document
- Local-first editing: applying edits locally before server confirmation
- Presence: showing other users' cursors and selections
- Cross-link: consensus/replication depth lives in System Design's `consistency-replication` group
- Interview angle: framing this design at the right depth for a frontend (not distributed-systems) interview

---

## Group: Browser Internals & Performance (browser-performance)

*Tier 🟡 — reflow/repaint, Core Web Vitals.*

### Topic: Layout, Reflow, and Repaint (layout-reflow-and-repaint, intermediate)
What triggers reflow vs repaint vs compositing, and which CSS properties are "expensive."
- Reflow (layout): when the browser recomputes geometry
- Repaint: when only pixels change, not geometry
- Compositing: when the GPU can skip both
- Diagram: the pipeline decision tree — which properties trigger which stage
- Properties that always cause reflow: `width`, `top`, `display`, etc.
- Properties that are "free": `transform`, `opacity`
- Code: swapping a `top`/`left` animation for `transform`
- Interview angle: "why is this animation janky, and this other one smooth"

### Topic: Layout Thrashing (layout-thrashing, advanced)
Forced synchronous layout from interleaved reads/writes, and the batch-reads-then-writes fix.
- Forced synchronous layout: reading a layout property right after writing one
- Diagram: a read-write-read-write loop forcing repeated layout per frame
- Code: a thrashing loop (`offsetHeight` read inside a style-writing loop)
- Code: the fix — batch all reads, then all writes
- `requestAnimationFrame` for scheduling layout-safe work
- Tools: spotting stacked "Layout" entries in the Performance panel
- Pitfall: a well-intentioned "measure each item" loop tanking a long list's render
- Interview angle: diagnose a jank report from a real trace

### Topic: Compositing and GPU Layers (compositing-and-gpu-layers, advanced)
How layers let the GPU move pixels without re-layout, and the cost of over-promoting elements.
- Why layers exist: letting the GPU move pixels without re-layout or re-paint
- What promotes an element to its own layer (`will-change`, 3D transforms, video, canvas)
- Diagram: the layer tree for a page with a few promoted elements
- Pitfall: too many layers causing memory pressure ("layer explosion")
- `will-change` as a hint, not a magic switch — using it sparingly
- Code: promoting a sidebar for a smooth slide-in animation
- Interview angle: "how would you make this drawer animation buttery smooth"

### Topic: Core Web Vitals (core-web-vitals, intermediate)
LCP, INP, and CLS — what each measures, common culprits, and how to fix them.
- Why Google standardized on these three metrics
- LCP (Largest Contentful Paint): what it measures, common culprits
- INP (Interaction to Next Paint): responsiveness, replacing FID
- CLS (Cumulative Layout Shift): unexpected layout movement, how it's scored
- Diagram: a page-load timeline marking when each vital is measured
- Code: fixing LCP — preloading the hero image/font, removing render blockers
- Code: fixing CLS — reserving space for images/ads/fonts before they load
- Pitfall: optimizing lab scores (Lighthouse) while field data stays bad
- Interview angle: "this page has a bad LCP score — walk me through debugging it"

### Topic: Measuring Performance (measuring-performance, intermediate)
Lab vs field data, reading a DevTools trace, and instrumenting Web Vitals in production.
- Compare: lab data (synthetic runs) vs field data (Real User Monitoring)
- The DevTools Performance panel: reading a trace — main thread, frames, long tasks
- Lighthouse: what it measures and its scoring model's limits
- Diagram: a flame chart with a long task highlighted
- Code: the `PerformanceObserver` API capturing Web Vitals in production
- Synthetic monitoring services vs RUM — when you need both
- Pitfall: trusting a single Lighthouse run instead of a distribution across real devices
- Interview angle: "how would you know if a regression shipped to real users"

### Topic: Loading Performance Patterns (loading-performance-patterns, intermediate)
Resource hints, lazy loading, image/font optimization, and shortening the loading waterfall.
- The loading waterfall: what blocks first paint vs what can wait
- Compare: `preload`, `prefetch`, `preconnect`, `dns-prefetch` — what each actually does
- Diagram: a waterfall before and after adding a `preload` for the hero image
- Code: lazy loading images (`loading="lazy"`), routes, and below-the-fold components
- Image optimization: responsive formats, modern codecs (AVIF/WebP), correct sizing
- Font loading strategies: `font-display`, avoiding invisible/flashing text
- Pitfall: prefetching everything and competing with the resources that actually matter
- Interview angle: "the homepage is slow on 3G — where do you start"

### Topic: JavaScript Performance Patterns (javascript-performance-patterns, advanced)
Debounce/throttle, Web Workers, and keeping the main thread free of long tasks.
- Long tasks: anything over 50ms blocking the main thread
- Compare: debounce vs throttle — reducing how often expensive work runs
- Diagram: debounce vs throttle timing on a stream of scroll events
- Code: implementing debounce and throttle from scratch
- Web Workers: moving heavy computation off the main thread
- Code: a worker computing something expensive while the UI stays responsive
- Breaking up long tasks with `requestIdleCallback` or manual yielding
- Pitfall: debouncing something that needed throttling (or vice versa)

### Topic: Long-Session SPA Performance (long-session-spa-perf, advanced)
Why SPAs uniquely degrade over a long session, and the cleanup discipline that prevents it.
- Why SPAs uniquely degrade over time: no full navigation to reset state
- Common accumulators: event listeners never removed, timers/intervals left running
- Detached DOM nodes: still referenced by JS after removal from the page
- Diagram: a memory graph climbing across route changes in a memory profiler
- Code: a router-based cleanup pattern (unsubscribe on unmount/navigation)
- Cross-link: GC mechanics and closures are covered in `javascript`'s `js-runtime-and-memory`
- Pitfall: a "temporary" polling interval from an old feature nobody removed
- Interview angle: "users report the app slows down after using it for an hour"

---

## Group: Accessibility (accessibility)

*Tier ⚪ — ARIA, semantic HTML, WCAG.*

### Topic: Why Accessibility Matters (why-accessibility-matters, beginner)
Who accessibility serves, the assistive tech landscape, and the business/legal case for investing in it.
- Who accessibility is for: permanent, temporary, and situational disabilities
- Assistive technology overview: screen readers, switch devices, screen magnifiers
- The business/legal case: lawsuits, market reach, SEO overlap
- Diagram: the spectrum of disability types mapped to the tech that helps
- The "curb-cut effect": accessible design helping everyone
- Pitfall: the myth that accessibility is only about screen readers
- Interview angle: "why should the team invest time in accessibility"

### Topic: Semantic HTML for Accessibility (semantic-html-for-a11y, beginner)
The accessibility tree, native element behavior, and landmark/heading structure for screen-reader navigation.
- The accessibility tree: how the browser exposes the DOM to assistive tech
- Diagram: DOM tree vs accessibility tree for a small component
- Native elements come with behavior for free: `<button>` vs `<div onclick>`
- Landmark regions: `<nav>`, `<main>`, `<header>` and screen-reader navigation
- Heading structure: why skipping levels breaks navigation-by-heading
- Code: fixing a div-soup component into semantic elements
- Pitfall: a clickable `<div>` invisible to keyboard and screen-reader users

### Topic: ARIA Roles, States, and Properties (aria-roles-states-properties, intermediate)
When ARIA is appropriate, the roles/states/properties model, and keeping attributes in sync with UI.
- The first rule of ARIA: don't use it if a native element already does the job
- Roles vs states vs properties — what each ARIA attribute category does
- Common roles: `dialog`, `tablist`/`tab`/`tabpanel`, `alert`
- `aria-expanded`, `aria-hidden`, `aria-live` — state that must stay in sync with the UI
- Diagram: a custom dropdown's ARIA attributes mapped to its visual states
- Code: a minimal accessible custom checkbox with the right ARIA
- Pitfall: ARIA attributes going stale when JS updates the UI but forgets the attribute
- Interview angle: "make this custom dropdown accessible"

### Topic: Keyboard Navigation and Focus (keyboard-navigation-and-focus, intermediate)
Tab order, focus management/traps, skip links, and `:focus-visible`.
- Tab order: how `tabindex` values (0, -1, positive) actually behave
- Focus management on route/view changes in an SPA
- Code: a focus trap keeping keyboard focus inside an open modal
- Skip links: letting keyboard users bypass repeated navigation
- Compare: `:focus-visible` vs `:focus` — showing focus rings only when useful
- Diagram: tab order through a page with a modal open
- Pitfall: a modal that opens but leaves keyboard focus behind it in the page
- Interview angle: "build a modal that's fully keyboard-operable"

### Topic: Accessible Forms and Errors (accessible-forms-and-errors, intermediate)
Labeling strategies, associating errors with fields, and live regions for dynamic feedback.
- Compare: `<label for>` vs `aria-label` vs `aria-labelledby` — when each fits
- Associating error text with its field via `aria-describedby`
- Live regions: announcing dynamic errors/status without moving focus unexpectedly
- Diagram: a form submission with a validation error announced to a screen reader
- Code: an accessible error-summary pattern for multi-field forms
- Cross-link: native validation mechanics are covered in `html-css`'s `forms-and-validation`
- Pitfall: color-only error indication with no text or icon

### Topic: WCAG and Accessibility Testing (wcag-and-testing, intermediate)
WCAG's POUR principles, conformance levels, and the automated-vs-manual testing split.
- WCAG's POUR principles: Perceivable, Operable, Understandable, Robust
- Conformance levels: A, AA, AAA — what most companies target and why
- Automated testing: what tools like axe can and can't catch
- Diagram: the split between issues automated tools catch vs need manual review
- Manual testing: a basic keyboard-only and screen-reader pass
- Code: wiring an automated a11y check into CI
- Pitfall: treating a 100% automated-tool score as "fully accessible"
- Interview angle: "how would you audit this page for accessibility"

### Topic: Accessible Component Patterns (accessible-components-patterns, advanced)
Building accessible custom widgets (modal, combobox, tabs) per established ARIA patterns.
- Why custom widgets need explicit accessibility work — no free native behavior
- The ARIA Authoring Practices Guide as the reference for common patterns
- Code: an accessible modal — focus trap, `aria-modal`, labeled by its heading
- Code: an accessible combobox — roles, `aria-activedescendant`, keyboard interaction
- Diagram: the keyboard interaction map for a combobox (arrow keys, Enter, Escape)
- Building accessible tabs: the roving-tabindex pattern
- Pitfall: reinventing a widget pattern instead of following the established one
- Interview angle: "implement an accessible tab component"

---

## Group: Client-Side Security (web-security)

*Tier 🟡 — XSS/CSRF/CSP from the frontend.*

### Topic: XSS Fundamentals (xss-fundamentals, intermediate)
What XSS is, the stored/reflected/DOM-based varieties, and why it runs with the victim's full privileges.
- What XSS is: attacker script running in another user's browser session
- Compare: stored vs reflected vs DOM-based XSS — where the payload lives and travels
- Diagram: a stored-XSS payload's path from comment field to victim's browser
- Why XSS is devastating: it runs with the victim's full session privileges
- Code: a minimal vulnerable snippet (`innerHTML` from user input) and the exploit
- DOM-based XSS: when the vulnerability never touches the server at all
- Pitfall: assuming "we don't have a database, so we can't have stored XSS"
- Interview angle: "find the XSS vulnerability in this code snippet"

### Topic: Preventing XSS (preventing-xss, intermediate)
Context-aware output encoding, framework auto-escaping, and sanitizing the escape hatches that reopen the hole.
- Output encoding: escaping data for the context it's rendered into (HTML/attribute/JS/URL)
- Why escaping for the wrong context still leaves you vulnerable
- Framework auto-escaping: how React/Vue/Angular protect you by default
- Diagram: the same untrusted string escaped differently per rendering context
- Pitfall: the escape hatches that reopen the hole — `dangerouslySetInnerHTML`, `v-html`, `innerHTML`
- Code: sanitizing user-generated HTML with a library (e.g. DOMPurify) before rendering
- Interview angle: "the product needs rich-text comments — how do you render them safely"

### Topic: CSRF from the Frontend (csrf-from-the-frontend, intermediate)
Why ambient cookies enable forged requests, and how SameSite cookies plus tokens defend against it.
- What CSRF is: a forged request riding the victim's ambient cookies
- Why CSRF only threatens cookie-based auth, not token-in-header auth
- Diagram: a malicious site triggering a state-changing request using the victim's session cookie
- `SameSite` cookies (`Strict`/`Lax`/`None`) as the modern first line of defense
- Code: reading and attaching an anti-CSRF token from the frontend
- Compare: SameSite cookies vs CSRF tokens vs both together
- Pitfall: `SameSite=None`, required for a legitimate cross-site use case, reopening the risk
- Interview angle: "why doesn't this login form need a CSRF token but this one does"

### Topic: Content Security Policy (content-security-policy, advanced)
CSP as an execution/load allowlist — key directives, nonces/hashes, and safe rollout via report-only mode.
- What CSP is: an allowlist telling the browser what's allowed to execute or load
- Key directives: `script-src`, `style-src`, `connect-src`, `default-src`
- Code: nonces and hashes — allowing specific inline scripts without `unsafe-inline`
- Diagram: a request blocked by CSP and what the console error tells you
- Report-only mode: rolling out CSP without breaking production first
- Compare: allowlist-by-domain vs nonce/hash-based — why the latter is more robust
- Pitfall: `unsafe-inline` or `unsafe-eval` added "temporarily" and never removed
- Interview angle: "design a CSP for this app" given its script/style sources

### Topic: Clickjacking and Framing (clickjacking-and-framing, intermediate)
UI-redress attacks via invisible framing, and blocking them with `frame-ancestors`/`X-Frame-Options`.
- What clickjacking is: tricking a user into clicking something they can't see
- Diagram: the classic attack — an invisible iframe of a real page layered under bait UI
- Compare: `X-Frame-Options` vs CSP's `frame-ancestors` — the legacy vs modern header
- Code: setting `frame-ancestors` to block being framed by other origins
- When framing is legitimate: widgets/embeds needing an allowlist, not a blanket block
- Pitfall: relying only on JS "frame-busting" scripts, which attackers can neutralize
- Interview angle: "how would you stop this page from being embedded elsewhere"

### Topic: Secure Storage and Tokens (secure-storage-and-tokens, intermediate)
The cookie-vs-localStorage token trade-off through a security lens, and refresh-token patterns.
- Restating the trade-off: cookies (CSRF-exposed, XSS-resistant if HttpOnly) vs localStorage (XSS-exposed, CSRF-immune)
- Diagram: attack-surface comparison — token in an HttpOnly cookie vs token in localStorage
- Refresh-token patterns: short-lived access token plus an HttpOnly refresh cookie
- Why `HttpOnly` blocks JS from ever reading the cookie, closing the XSS-exfiltration path
- Code: an auth flow keeping the access token in memory, not persistent storage
- Pitfall: a "temporary" localStorage token that becomes permanent because it was convenient
- Interview angle: "where do you store the JWT, and defend the choice"

### Topic: Third-Party Scripts and Supply Chain (third-party-scripts-and-supply-chain, advanced)
Why third-party JS shares your privileges, and containing it with SRI, CSP, and iframe sandboxing.
- The risk: any third-party script has the same privileges as your own code
- Code: Subresource Integrity (SRI) — pinning a script to an expected hash
- Diagram: a compromised CDN serving altered JS, and SRI rejecting it
- Sandboxing third-party content with `<iframe sandbox>`
- Vetting and limiting third-party tags: analytics/ads/chat widgets as attack surface
- Compare: SRI vs CSP allowlisting vs iframe sandboxing — layered defenses
- Pitfall: adding a third-party script tag with no integrity check "because marketing needs it"
- Interview angle: "a third-party analytics script got compromised — what limited the blast radius"
