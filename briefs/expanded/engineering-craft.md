# Area: Software Engineering & Craft (engineering-craft)

Reference outline — schema v3 (`area → group → topic → slide`; MCQs and interview questions attach at topic level, not listed here). Groups are taken verbatim from `briefs/area-group-map.md` § Area 9. For human review and approval before any slide content is written.

---

## Group: Version Control & Git (git)

### Topic: Git's Mental Model (git-fundamentals-mental-model, beginner)
The conceptual model of git as a content-addressable snapshot DAG — commits, staging, HEAD — that everything else builds on.
- **Concept:** Git is snapshots, not diffs — why this differs from CVS/SVN
- **Diagram:** the commit DAG — commits, parents, branches and tags as pointers
- **Concept:** the three trees — working directory, staging area (index), HEAD/repo
- **Diagram:** file lifecycle — untracked → staged → committed
- **Concept:** what a commit actually contains (tree + parent + author + message, hashed)
- **Concept:** HEAD, detached HEAD, and what "checking out a commit" means
- **Code:** everyday commands — status, add, commit, log, diff — reading the output
- **Compare:** `git diff` vs `git diff --staged` vs `git show`
- **Pitfall:** committing large binaries or secrets — why history makes them permanent

### Topic: Branching & Merging (branching-merging, beginner)
Creating and switching branches and combining them safely, including conflict resolution.
- **Concept:** a branch is just a movable pointer, not a copy of files
- **Code:** create/switch/delete branches (`branch`, `switch`, `checkout -b`)
- **Diagram:** fast-forward merge vs true three-way merge
- **Concept:** how git finds the merge base (common ancestor) and computes the merge
- **Code:** a merge conflict end to end — markers, resolving, completing the merge
- **Concept:** merge commits vs squash merge vs fast-forward-only — what history each leaves
- **Compare:** long-lived branches vs short-lived feature branches — integration pain
- **Pitfall:** merging the wrong direction or a stale base, producing a "phantom" diff in a PR

### Topic: Rebase vs Merge (rebase-vs-merge, intermediate)
Rewriting commit history with rebase, interactive rebase workflows, and the rules for when rebasing is safe.
- **Concept:** what rebase actually does — replay commits onto a new base, new hashes
- **Diagram:** the same two branches merged vs rebased — resulting history shapes
- **Code:** interactive rebase — pick/reword/squash/fixup/drop
- **Concept:** the golden rule — never rebase commits others have already pulled
- **Concept:** resolving conflicts mid-rebase — `--continue` / `--skip` / `--abort`
- **Compare:** rebase vs merge — linear readable history vs preserved true history
- **Concept:** `rebase --onto` for moving a branch to a different base
- **Pitfall:** force-pushing a rebased shared branch and clobbering teammates' work
- **Concept:** `git pull --rebase` vs a default pull — why teams standardize on one

### Topic: Git Workflows & Collaboration (git-workflows-collaboration, intermediate)
Team branching models and how PR-based collaboration is structured in practice.
- **Concept:** why teams need a branching convention at all — coordination cost
- **Compare:** trunk-based development vs GitFlow vs GitHub Flow
- **Diagram:** GitFlow's branch topology (main/develop/feature/release/hotfix)
- **Concept:** trunk-based development plus feature flags as the modern default at scale
- **Concept:** the pull/merge request lifecycle — draft, review, CI gate, merge
- **Compare:** merge commit vs squash-and-merge vs rebase-and-merge on a PR
- **Concept:** release branches and hotfixes — patching production without shipping main
- **Concept:** monorepo vs polyrepo — how branching and ownership change with repo shape
- **Pitfall:** long-lived feature branches causing integration hell ("merge debt")

### Topic: Undoing Changes & Recovery (undoing-changes-recovery, intermediate)
Safely undoing work at every stage — unstaged, staged, committed, pushed — and recovering from mistakes.
- **Concept:** matching the undo tool to the stage — working tree vs index vs history
- **Compare:** `git restore` vs `git checkout --` vs `git reset` for unstaged/staged changes
- **Diagram:** reset soft vs mixed vs hard — what moves (HEAD, index, working tree)
- **Concept:** `git revert` — undoing via a new commit, safe on shared history
- **Compare:** reset vs revert — local cleanup vs public-history-safe undo
- **Concept:** `git stash` — shelving work in progress, pop/apply/drop
- **Concept:** the reflog — git's safety net for "unreachable" commits
- **Code:** recovering a deleted branch or a lost commit via reflog
- **Pitfall:** `reset --hard` discarding uncommitted work with no safety net

### Topic: Advanced Git Internals (advanced-git-internals, advanced)
The object model, storage internals, and power tools that separate git fluency from git literacy.
- **Concept:** the four object types — blob, tree, commit, tag — content-addressed by hash
- **Diagram:** how a commit's tree points to blobs/trees, and identical content is deduplicated
- **Concept:** loose objects vs packfiles — how git compresses history
- **Concept:** garbage collection — when unreferenced objects actually get pruned
- **Code:** `git bisect` — binary-searching history to find a regression's commit
- **Concept:** `git cherry-pick` — applying a specific commit elsewhere, and its conflict risk
- **Compare:** submodules vs subtree vs monorepo — trade-offs for embedding external code
- **Concept:** tags — lightweight vs annotated, and why releases use annotated tags
- **Pitfall:** rewriting history that a submodule or downstream fork already depends on

### Topic: Git at Scale (git-at-scale, advanced)
Operating git in large codebases and teams — performance, ownership, and auditability.
- **Concept:** why cloning and checkout get slow at scale — full history, full tree
- **Compare:** shallow clone vs partial clone vs sparse checkout
- **Concept:** git hooks (pre-commit, pre-push, commit-msg) for local automation and quality gates
- **Concept:** CODEOWNERS and required reviewers — routing review by path
- **Concept:** `git blame` and log archaeology (`-L`, `--follow`, pickaxe) for tracing intent
- **Concept:** signed commits and tags — why supply-chain trust cares about provenance
- **Compare:** monorepo tooling (sparse checkout, virtual filesystems) vs many small repos
- **Pitfall:** one accidental large-file commit bloating clone size for everyone, forever

---

## Group: Testing & Quality (testing)

### Topic: Testing Fundamentals & the Test Pyramid (testing-fundamentals-pyramid, beginner)
Why automated testing exists and how to allocate effort across test types.
- **Concept:** what automated tests buy you — regression safety, executable documentation, design feedback
- **Diagram:** the test pyramid — unit (many, fast, cheap) → integration → e2e (few, slow, expensive)
- **Concept:** the cost/speed/confidence trade-off at each layer
- **Compare:** test pyramid vs "testing trophy" — when each shape fits
- **Concept:** what "unit," "integration," and "e2e" actually mean (boundary of the system under test)
- **Pitfall:** the ice-cream-cone anti-pattern — mostly manual/e2e tests, almost no unit tests
- **Concept:** test-induced design damage vs tests that genuinely catch bugs

### Topic: Unit Testing Principles (unit-testing-principles, beginner)
What makes an individual unit test correct, isolated, and worth keeping.
- **Concept:** a unit test's job — one behavior, one reason to fail
- **Concept:** the AAA structure — Arrange, Act, Assert
- **Concept:** FIRST principles — Fast, Isolated, Repeatable, Self-checking, Timely
- **Concept:** test isolation — no shared mutable state, no order dependence
- **Compare:** testing behavior/outputs vs testing implementation details
- **Concept:** naming tests so failures are self-explanatory
- **Pitfall:** brittle tests that break on every refactor despite unchanged behavior
- **Pitfall:** assertion roulette — one test asserting five unrelated things

### Topic: Test Doubles & Mocking (test-doubles-mocking, intermediate)
The taxonomy of test doubles and choosing the right one to isolate a unit from its dependencies.
- **Concept:** why isolate — dependencies that are slow, non-deterministic, or unbuilt yet
- **Compare:** dummy vs stub vs spy vs mock vs fake — what each actually does
- **Diagram:** a test double sitting between the unit under test and its real dependency
- **Code:** mocking a dependency and asserting an interaction (mockist style)
- **Code:** using a fake in-memory implementation instead of a mock (classical style)
- **Compare:** mockist (London school) vs classicist (Detroit school) testing philosophy
- **Pitfall:** over-mocking — tests that pass while the real integration is broken
- **Pitfall:** mocking types you don't own — coupling tests to a library's internals
- **Concept:** verifying behavior vs verifying state — when interaction testing is actually warranted

### Topic: TDD — Red, Green, Refactor (tdd-red-green-refactor, intermediate)
The test-driven development cycle as a design technique, not just a testing technique.
- **Concept:** the TDD loop — red (failing test) → green (minimal code) → refactor
- **Concept:** TDD as a design tool — tests force a usable API before the implementation exists
- **Compare:** outside-in (acceptance-driven) vs inside-out (unit-first) TDD
- **Code:** a short TDD kata walkthrough across a few red-green-refactor cycles
- **Concept:** "write the minimum code to pass" and why that constraint matters
- **Compare:** TDD vs test-after — when writing tests first actually changes the design
- **Pitfall:** over-specifying implementation in tests, making the refactor step impossible
- **Concept:** when TDD isn't worth it — throwaway spikes, exploratory UI work

### Topic: Integration Testing (integration-testing, intermediate)
Testing the seams between a unit and its real collaborators — database, filesystem, other services.
- **Concept:** what integration tests verify that unit tests structurally cannot
- **Concept:** narrow integration tests (one boundary) vs broad integration tests (many components)
- **Code:** spinning up a real dependency for tests via containers (e.g. a real Postgres in CI)
- **Concept:** contract testing — verifying a consumer and provider agree without a live call
- **Diagram:** consumer-driven contract testing flow (consumer publishes expectations, provider verifies)
- **Compare:** testing against a real dependency vs an in-memory/lightweight substitute
- **Pitfall:** integration tests sharing mutable state, becoming order-dependent
- **Concept:** test data setup/teardown strategies — transactional rollback, fixtures, builders

### Topic: E2E & UI Testing (e2e-and-ui-testing, intermediate)
Exercising the whole system through its real interface, and managing the flakiness that comes with it.
- **Concept:** what e2e tests cover that lower layers can't — real wiring, real user paths
- **Concept:** choosing critical user journeys — e2e tests are expensive, so scope is deliberate
- **Code:** a browser automation test for a login flow
- **Concept:** the Page Object pattern — decoupling test logic from UI selectors
- **Concept:** why e2e tests flake — timing, network, shared environments, animations
- **Compare:** explicit waits/retries vs fixed sleeps for async UI state
- **Concept:** test environments — staging vs ephemeral per-PR environments vs prod smoke tests
- **Pitfall:** a flaky e2e suite that gets muted, silently losing its safety value

### Topic: Code Coverage & Test Quality (code-coverage-and-test-quality, intermediate)
Measuring how well tests exercise the code, and why coverage numbers can mislead.
- **Concept:** what coverage measures — line, branch, and path coverage, in increasing strictness
- **Concept:** 100% coverage still allows bugs — coverage proves code ran, not that it was checked
- **Diagram:** a covered line with a missing assertion — the false-confidence case
- **Concept:** mutation testing — deliberately injecting bugs to check whether tests catch them
- **Compare:** coverage percentage as a target vs coverage as a diagnostic signal
- **Pitfall:** a team gaming a coverage gate with assertion-free tests
- **Concept:** setting sensible coverage policy — e.g. gating on diff coverage, not a global average

### Topic: Test Strategy at Scale (test-strategy-at-scale, advanced)
Keeping a large test suite fast, reliable, and trustworthy as a codebase and team grow.
- **Concept:** the tax of a slow test suite — feedback loop length shapes developer behavior
- **Concept:** parallelizing and sharding test suites in CI
- **Concept:** flaky test triage — quarantine, auto-retry, tracking flake rate per test
- **Compare:** quarantining flaky tests vs deleting them vs blocking merges until fixed
- **Concept:** test data management at scale — synthetic data, anonymized snapshots, seed builders
- **Concept:** consumer-driven contract testing across many microservices
- **Diagram:** a CI pipeline's test stages — fast unit gate first, slower suites later or parallel
- **Pitfall:** a quarantine list that only ever grows, becoming a graveyard of ignored failures

### Topic: Property-Based & Specialized Testing (property-based-and-specialized-testing, advanced)
Testing techniques beyond example-based tests — generating inputs, fuzzing, and snapshotting.
- **Concept:** example-based tests check specific cases; property-based tests check invariants across generated inputs
- **Code:** a property-based test (e.g. "sorting is idempotent") over a generated input set
- **Concept:** shrinking — reducing a failing generated case to a minimal repro
- **Concept:** fuzz testing — feeding malformed or random input to find crashes and security bugs
- **Concept:** snapshot/golden-file testing — capturing output and diffing against a stored baseline
- **Compare:** property-based vs example-based vs snapshot testing — what each catches well
- **Pitfall:** snapshot tests that get blindly re-approved, ceasing to test anything

---

## Group: CI/CD & Release Engineering (cicd)

*Boundary: this group is the software-delivery practice (pipelines, deploy strategy, release process, flags). Infra automation for provisioning environments (Terraform, GitOps) is `iac` / `cicd-infra` in Area 10 — flagged as a likely near-duplicate to reconcile with that area.*

### Topic: CI Fundamentals (ci-fundamentals, beginner)
The core practice of continuously integrating and validating code changes automatically.
- **Concept:** what Continuous Integration means — merge often, build and test automatically on every change
- **Concept:** the pre-CI world — integration hell, "it works on my machine"
- **Diagram:** a basic CI flow — push → build → test → report status back to the PR
- **Concept:** the CI feedback loop and why speed matters — fast fail beats slow fail
- **Concept:** build status as a merge gate — required checks, branch protection
- **Code:** a minimal CI config — install, build, test, lint stages
- **Concept:** keeping the main branch always green and deployable
- **Pitfall:** a red main branch that's tolerated, teaching the team to ignore CI

### Topic: CD & Deployment Strategies (cd-and-deployment-strategies, intermediate)
Automating the path from a green build to production, and the deployment patterns that reduce risk.
- **Concept:** continuous delivery (always releasable) vs continuous deployment (auto-released)
- **Diagram:** rolling deployment — replacing instances gradually
- **Diagram:** blue-green deployment — two full environments, instant traffic switch
- **Diagram:** canary deployment — shifting a small percentage of traffic first
- **Compare:** rolling vs blue-green vs canary — risk, cost, and rollback-speed trade-offs
- **Concept:** deployment vs release — decoupling "code is live" from "feature is visible"
- **Concept:** health checks and automated promotion or abort based on error rate/latency
- **Pitfall:** deploying without a fast, tested rollback path

### Topic: Pipeline Design (pipeline-design, intermediate)
Structuring a CI/CD pipeline itself — stages, artifacts, caching, and pipeline-as-code.
- **Concept:** pipeline stages — build, test, package, deploy — and their dependencies
- **Concept:** pipeline-as-code — versioned, reviewable pipeline definitions
- **Concept:** build artifacts — building once, promoting the same artifact through environments
- **Concept:** caching dependencies and build layers to cut pipeline time
- **Diagram:** a multi-stage pipeline with fan-out (parallel test shards) and fan-in (deploy gate)
- **Concept:** build matrices — testing across OS/language-version combinations
- **Compare:** building a fresh artifact per environment vs "build once, promote everywhere"
- **Pitfall:** an environment-specific build masking a bug that only appears in production

### Topic: Feature Flags & Progressive Delivery (feature-flags-progressive-delivery, intermediate)
Decoupling deployment from release using flags, and rolling out changes progressively.
- **Concept:** why decouple deploy from release — ship dark code, turn it on independently
- **Compare:** release flags vs experiment flags vs ops/kill-switch flags vs permission flags
- **Diagram:** progressive rollout — 1% → 10% → 50% → 100% with monitoring gates between
- **Concept:** kill switches — the fastest rollback there is, no redeploy needed
- **Code:** a feature-flag check gating a code path, with a default-safe fallback
- **Concept:** targeting and segmentation — rolling out by user cohort, region, or account
- **Pitfall:** flag debt — stale flags left in code long after the decision is made
- **Concept:** testing both flag states, and cleaning up flags after full rollout

### Topic: Release Management & Versioning (release-management-versioning, intermediate)
Naming, tracking, and shipping releases in a way consumers can depend on.
- **Concept:** semantic versioning — major.minor.patch and what each bump promises
- **Concept:** changelogs generated from commit conventions (e.g. Conventional Commits)
- **Compare:** release trains (fixed cadence) vs continuous release (ship when ready)
- **Concept:** release branches — cutting a branch to stabilize while main keeps moving
- **Concept:** hotfix flow — patching a released version without shipping unreleased main work
- **Compare:** calendar-based releases vs feature-based releases
- **Concept:** deprecation policy — versioning breaking changes so consumers can migrate
- **Pitfall:** breaking semver by shipping a breaking change as a minor or patch bump

### Topic: Rollback & Safe Deploys (rollback-and-safe-deploys, intermediate)
Making deploys reversible and detecting problems fast enough to act.
- **Concept:** the deploy-risk equation — blast radius × detection time × rollback time
- **Concept:** health checks and readiness/liveness probes gating traffic
- **Concept:** automated rollback triggers — error-rate or latency thresholds post-deploy
- **Diagram:** a deploy pipeline with an automatic abort-and-rollback step
- **Concept:** database migrations as the hard part — backward-compatible schema changes
- **Concept:** expand/contract (parallel change) pattern for zero-downtime schema migration
- **Compare:** forward-fix vs rollback — when rolling back isn't actually safe (data already written)
- **Pitfall:** a schema migration that breaks the previous app version during a rolling deploy

### Topic: Build & Dependency Management (build-and-dependency-management, intermediate)
Making builds reproducible and dependencies trustworthy and pinned.
- **Concept:** reproducible builds — same input, same output, every time
- **Concept:** lockfiles — pinning transitive dependency versions
- **Concept:** artifact repositories (package/container registries) as the source of truth for built code
- **Compare:** floating versions vs pinned versions vs pinned-with-scheduled-updates
- **Concept:** build provenance and supply-chain basics — SBOMs, signed artifacts
- **Pitfall:** an unpinned dependency silently changing behavior between builds
- **Concept:** dependency-update automation and the review burden it creates

### Topic: CI/CD Infrastructure at Scale (infra-for-cicd-at-scale, advanced)
Keeping CI/CD fast and correct as the codebase, team, and traffic grow.
- **Concept:** why naive "test everything, every time" stops scaling
- **Concept:** affected-only builds and tests in a monorepo — only run what changed impacts
- **Diagram:** a dependency graph used to compute the affected build/test set
- **Compare:** self-hosted runners vs managed/hosted CI runners — cost, control, scaling
- **Concept:** distributed build caching across the team and CI fleet
- **Concept:** deployment orchestration across many services — ordering, dependency-aware rollout
- **Concept:** progressive-delivery infrastructure — mesh-based canary, automated analysis
- **Pitfall:** CI infra becoming a second production system with no one owning its reliability

---

## Group: Debugging & Incident Response (debugging)

### Topic: Systematic Debugging Method (systematic-debugging-method, beginner)
A repeatable, disciplined process for finding the cause of a bug instead of guessing.
- **Concept:** debugging as the scientific method — observe, hypothesize, test, refine
- **Concept:** reproduce first — a bug you can't reproduce, you can't verify you fixed
- **Concept:** isolating the smallest failing case (minimal repro)
- **Concept:** binary search over the problem space — narrowing where the bug lives
- **Concept:** forming a specific, falsifiable hypothesis before changing code
- **Pitfall:** shotgun debugging — changing many things at once and losing signal
- **Concept:** verifying the fix addresses the root cause, not a symptom
- **Concept:** rubber duck debugging — explaining the problem out loud surfaces assumptions

### Topic: Reading Stack Traces & Logs (reading-stack-traces-and-logs, beginner)
Extracting the actual signal from exceptions, stack traces, and application logs.
- **Concept:** anatomy of a stack trace — frames, the throw site vs the root cause
- **Concept:** reading bottom-up vs top-down, and finding "your code" among library frames
- **Concept:** exception chaining — the wrapped "caused by" trail
- **Concept:** log levels (debug/info/warn/error) and using them to filter signal from noise
- **Concept:** structured logging — key-value fields vs free-text messages, and why it matters at scale
- **Concept:** correlation/request IDs — tracing one request across logs and services
- **Diagram:** a request's correlation ID threading through multiple services' logs
- **Pitfall:** logging sensitive data (PII, secrets) by default in error messages

### Topic: Debugging Tools & Techniques (debugging-tools-techniques, intermediate)
The practical toolkit for finding bugs beyond just reading code.
- **Concept:** interactive debuggers — breakpoints, stepping, watch expressions, call-stack inspection
- **Compare:** print/log debugging vs interactive debugger vs static analysis — when each wins
- **Concept:** conditional and logpoint breakpoints for bugs that only trigger under specific state
- **Code:** `git bisect` to find the commit that introduced a regression
- **Concept:** record-replay/time-travel debugging for inspecting past program state
- **Concept:** memory and allocation debugging tools (sanitizers, leak detectors) for native code
- **Compare:** debugging in dev (full tooling) vs staging vs production (limited, higher stakes)
- **Pitfall:** leaving debug logging or debug-only code paths in a shipped commit

### Topic: Production Debugging & Observability (production-debugging-observability, intermediate)
Diagnosing issues in live systems you cannot attach a local debugger to. *(Cross-link: the full observability stack — logs/metrics/traces tooling — is covered in depth by System Design's `observability` group and Cloud/DevOps's `observability-ops`; this topic is the debugging workflow that consumes them.)*
- **Concept:** why production debugging is different — no debugger, real traffic, real cost of downtime
- **Concept:** the three pillars — logs, metrics, traces — and what each answers
- **Diagram:** a distributed trace across services showing where latency or errors concentrate
- **Concept:** dashboards and alerting as the first signal something's wrong
- **Concept:** correlating an error/latency spike with a deploy, config change, or traffic shift
- **Concept:** safe read-only investigation techniques before touching any state
- **Compare:** debugging a monolith vs a distributed system — where complexity moves
- **Pitfall:** making a live change to "test a theory" in production without a rollback plan

### Topic: Concurrency Bugs & Heisenbugs (concurrency-bugs-and-heisenbugs, advanced)
Diagnosing the hardest class of bugs — ones that depend on timing and vanish under observation.
- **Concept:** what makes a bug a "Heisenbug" — behavior changes when you try to observe it
- **Concept:** race conditions — two threads touching shared state without ordering guarantees
- **Diagram:** an interleaving diagram showing how thread scheduling produces a race
- **Concept:** deadlocks and livelocks — recognizing the symptom and the resource-ordering cause
- **Concept:** the probe effect — why adding a log statement can hide a timing bug
- **Concept:** tools for concurrency bugs — thread sanitizers, deterministic replay, stress testing
- **Concept:** memory corruption bugs (use-after-free, buffer overrun) — why they're non-deterministic
- **Pitfall:** "fixing" a race by adding a sleep instead of proper synchronization

### Topic: On-Call & Incident Response (on-call-and-incident-response, intermediate)
How teams detect, triage, and respond to live incidents in real time.
- **Concept:** what on-call is for — being the first responder to production alerts
- **Concept:** severity levels and how severity drives response urgency
- **Concept:** incident roles — commander, communicator, responders — and why role separation matters at scale
- **Diagram:** an incident timeline — detect → triage → mitigate → resolve → follow-up
- **Concept:** mitigate first, root-cause later — stopping the bleeding beats a perfect fix
- **Concept:** communication during an incident — status pages, stakeholder updates, avoiding silence
- **Compare:** escalation policies and paging — reducing alert fatigue vs missing real incidents
- **Pitfall:** an on-call engineer diagnosing root cause for an hour while the outage continues

### Topic: Postmortems & Incident Learning (postmortems-and-incident-learning, intermediate)
Turning an incident into durable organizational learning without blame.
- **Concept:** blameless postmortems — why blame suppresses the honest detail you need
- **Concept:** the postmortem document — timeline, impact, root cause(s), action items
- **Concept:** the "5 whys" technique for digging past the first proximate cause
- **Concept:** distinguishing root cause from contributing factors — incidents are rarely one cause
- **Concept:** action items — assigning owners and due dates, tracking them to completion
- **Compare:** a single-root-cause narrative vs a systems view where multiple factors aligned
- **Concept:** sharing postmortems org-wide — normalizing failure as a learning input
- **Pitfall:** a postmortem with great analysis but action items that never get done

---

## Group: Code Review & Collaboration (code-review)

### Topic: Why Code Review & What to Look For (why-code-review-and-what-to-look-for, beginner)
The purpose of code review and the checklist of what a reviewer should actually evaluate.
- **Concept:** what code review is actually for — correctness, design, knowledge-sharing, shared ownership
- **Concept:** the review checklist — correctness, tests, readability, design fit, security, performance
- **Compare:** reviewing for bugs vs reviewing for style — why style should mostly be automated away
- **Concept:** reading a diff in context — pulling up the surrounding file, not just red/green lines
- **Concept:** what reviewers are not responsible for — re-deriving the whole design from scratch
- **Concept:** review as a second author's confidence, not a gate to satisfy
- **Pitfall:** rubber-stamp approvals — approving without actually reading the change

### Topic: Giving Effective Feedback (giving-effective-feedback, intermediate)
Writing review comments that improve the code without damaging the relationship.
- **Concept:** comment on the code, not the person
- **Concept:** distinguishing blocking issues from nits so authors know what's optional
- **Concept:** asking questions instead of issuing commands
- **Concept:** explaining the "why" behind a requested change, not just the "what"
- **Concept:** praising good decisions in the diff, not only flagging problems
- **Compare:** a harsh, terse comment vs the same feedback reframed constructively
- **Pitfall:** bikeshedding — spending review effort on trivial, low-stakes details
- **Concept:** calibrating review depth to the change's risk

### Topic: Receiving Feedback & Disagreement (receiving-feedback-and-disagreement, intermediate)
Responding to review feedback professionally, including when you disagree with it.
- **Concept:** default posture — assume good intent, respond to substance not tone
- **Concept:** separating "I disagree with the suggestion" from "I feel criticized"
- **Concept:** when to push back — reasoning with evidence, not just asserting
- **Concept:** disagree-and-commit — moving forward once a decision is made
- **Concept:** escalation paths — bringing in a third opinion when reviewer and author are stuck
- **Compare:** async back-and-forth in comments vs a quick call to resolve disagreement faster
- **Pitfall:** silently resenting feedback instead of raising the disagreement directly

### Topic: Review Process & Tooling (review-process-and-tooling, intermediate)
Structuring the review process itself — PR size, ownership, SLAs, and automation.
- **Concept:** why small PRs get reviewed better — cognitive limits on diff size
- **Concept:** splitting a large change into reviewable, independently-mergeable pieces
- **Concept:** required reviewers and CODEOWNERS — routing review to the right expertise
- **Concept:** review SLAs — why slow turnaround compounds into slow delivery
- **Concept:** automating away style/format/lint nits so humans review substance
- **Diagram:** a PR lifecycle — draft → automated checks → human review → approval → merge
- **Compare:** single required approver vs multiple approvers — speed vs safety
- **Pitfall:** a PR sitting for days because no reviewer felt assigned to it

### Topic: Code Review Anti-Patterns (code-review-anti-patterns, advanced)
Recognizable failure modes in review culture and how to counter them.
- **Concept:** rubber-stamping — approving without engaging, and why it happens
- **Concept:** nitpicking overload — burying one real issue under twenty trivial comments
- **Concept:** the drive-by reviewer who blocks a PR then disappears
- **Concept:** gatekeeping — using review power to relitigate settled design decisions
- **Concept:** review as a bottleneck — one senior engineer required on every PR
- **Compare:** healthy review friction (catches real issues) vs unhealthy friction (slows delivery for no gain)
- **Pitfall:** a team that stops trusting review because it never catches anything real

### Topic: Pair & Mob Programming (pair-and-mob-programming, intermediate)
Real-time collaborative coding as an alternative or complement to async review.
- **Concept:** pair programming — driver/navigator roles and the tight feedback loop
- **Concept:** mob programming — a whole team working on one problem at one keyboard
- **Compare:** pairing vs async code review — when live collaboration catches more, costs more
- **Concept:** remote pairing tooling and etiquette — screen share, shared cursors, turn-taking
- **Concept:** pairing for onboarding — transferring codebase knowledge faster than docs alone
- **Pitfall:** pairing seniors with seniors while juniors are left to review-only feedback
- **Concept:** when pairing is overkill vs high-value (tricky bugs, onboarding, design-in-progress)

### Topic: Async Collaboration for Distributed Teams (async-collaboration-for-distributed-teams, intermediate)
How collaboration mechanics change across timezones and remote teams. *(Boundary: the writing itself — design docs, RFCs — belongs to Technical Communication; this topic is the collaboration process around timezones and decisions.)*
- **Concept:** synchronous vs asynchronous collaboration — what each requires
- **Concept:** designing handoffs across timezones so work continues without waiting for a reply
- **Concept:** decision-making without a shared meeting — written proposals plus a comment deadline
- **Compare:** a quick sync call vs a long async thread — when the meeting is actually faster
- **Concept:** overlap-hours strategy — using the few shared hours deliberately
- **Concept:** making silence safe — default-approve or lazy consensus after a stated review window
- **Pitfall:** a decision stalling for weeks because it required a meeting nobody could schedule

---

## Group: Clean Architecture & DDD (clean-architecture)

### Topic: Layered Architecture Fundamentals (layered-architecture-fundamentals, beginner)
Why software separates into layers and how dependency direction between them is chosen.
- **Concept:** why we layer software — separating concerns that change for different reasons
- **Diagram:** classic three-layer architecture — presentation, business/domain, data access
- **Concept:** dependency direction — layers depending downward, never upward
- **Concept:** what belongs in each layer, and the smell of logic leaking into the wrong one
- **Compare:** a layered architecture vs a script with everything in one file or function
- **Pitfall:** fat controllers — business logic living in the presentation layer
- **Pitfall:** the data layer leaking into business logic (ORM entities used as domain objects)
- **Concept:** layering applies inside a single deployable too, not just across services

### Topic: Dependency Inversion & Boundaries (dependency-inversion-and-boundaries, intermediate)
Using the Dependency Inversion Principle to make architectural boundaries enforceable, not just conventional.
- **Concept:** the Dependency Inversion Principle — depend on abstractions, not concretions
- **Diagram:** a domain layer defining an interface that an outer infrastructure layer implements
- **Concept:** why this inverts the "natural" dependency direction
- **Concept:** ports (interfaces owned by the core) vs adapters (implementations in the outer layer)
- **Code:** a repository interface defined in the domain, implemented by a concrete DB adapter
- **Concept:** what this buys you — swappable infrastructure, testable domain logic without a real DB
- **Compare:** dependency inversion vs plain layering — layering alone still lets the wrong direction slip in
- **Pitfall:** an interface that leaks implementation details (e.g. SQL-shaped methods)

### Topic: Hexagonal & Clean Architecture (hexagonal-and-clean-architecture, intermediate)
Named architectural styles that formalize boundary-and-dependency-direction rules.
- **Concept:** the shared idea across these styles — a core with no outward dependencies, surrounded by adapters
- **Diagram:** hexagonal architecture — ports and adapters around an application core
- **Diagram:** Clean Architecture's concentric circles — entities, use cases, interface adapters, frameworks
- **Concept:** the Dependency Rule — source code dependencies point only inward
- **Compare:** hexagonal vs onion vs Clean Architecture — same core idea, different vocabulary
- **Concept:** use cases/application services as the layer that orchestrates domain logic
- **Concept:** what lives at the outermost ring — frameworks, DB drivers, UI, the "details"
- **Pitfall:** over-applying Clean Architecture's ceremony to a small CRUD app

### Topic: Domain-Driven Design Fundamentals (domain-driven-design-fundamentals, intermediate)
The core DDD mindset — modeling software around the business domain and a shared language.
- **Concept:** why DDD exists — software that mirrors the business is easier to change as the business changes
- **Concept:** ubiquitous language — one vocabulary shared by domain experts and code
- **Concept:** entities — objects with identity that persists across state changes
- **Concept:** value objects — defined by their attributes, immutable, no identity
- **Compare:** entity vs value object with a concrete example
- **Concept:** the domain model as executable knowledge, not just data structures
- **Pitfall:** an anemic domain model — objects that are just data bags with logic living elsewhere
- **Concept:** domain experts and engineers modeling together as a collaboration practice

### Topic: Tactical DDD Patterns (tactical-ddd-patterns, intermediate)
The concrete building blocks DDD uses to implement a domain model in code.
- **Concept:** aggregates — a cluster of objects treated as one consistency boundary
- **Concept:** the aggregate root — the single entry point that guards the aggregate's invariants
- **Diagram:** an aggregate boundary example with the root controlling access
- **Concept:** repositories — an abstraction for loading and saving whole aggregates
- **Concept:** domain services — logic that doesn't naturally belong to one entity or value object
- **Concept:** domain events — recording "something happened" for other parts of the system to react to
- **Compare:** transaction-per-aggregate vs spanning a transaction across multiple aggregates
- **Pitfall:** an aggregate so large that every operation contends on the same lock or row

### Topic: Strategic DDD & Bounded Contexts (strategic-ddd-bounded-contexts, advanced)
Applying DDD across a whole system — where one model ends and another begins, and how models relate.
- **Concept:** bounded context — the boundary within which a model and its language stay consistent
- **Concept:** the same word meaning different things in different contexts
- **Diagram:** a context map showing two bounded contexts and their relationship
- **Concept:** upstream/downstream relationships between contexts — who adapts to whom
- **Concept:** anti-corruption layer — translating a foreign model at the boundary instead of absorbing it
- **Concept:** shared kernel — a small shared model between tightly-coupled contexts, and its cost
- **Compare:** conformist vs anti-corruption-layer relationship
- **Concept:** bounded contexts as a natural seam for microservice boundaries
- **Pitfall:** one "God model" spanning multiple bounded contexts, becoming a shared bottleneck

### Topic: Architectural Boundaries in Practice (architectural-boundaries-in-practice, advanced)
Enforcing architectural rules in a real, evolving codebase, and knowing when the ceremony isn't worth it.
- **Concept:** enforcing boundaries with modules and visibility, not just convention
- **Concept:** architecture tests/fitness functions — automated checks that a boundary rule holds
- **Concept:** how boundaries erode over time without enforcement
- **Compare:** a strictly-enforced boundary vs a documented-but-unenforced one
- **Concept:** right-sizing architecture to the project — a CRUD admin tool doesn't need four layers
- **Concept:** refactoring toward better boundaries incrementally via the strangler pattern
- **Pitfall:** introducing full Clean Architecture on day one of a startup MVP

---

## Group: Performance Engineering (performance-engineering)

### Topic: Performance Mindset & Measurement (performance-mindset-and-measurement, beginner)
The discipline of measuring before optimizing, and the core vocabulary of latency, throughput, and bottlenecks.
- **Concept:** measure, don't guess — why intuition about bottlenecks is usually wrong
- **Concept:** latency vs throughput — optimizing one can hurt the other
- **Concept:** Amdahl's Law — the speedup ceiling imposed by the part you didn't optimize
- **Diagram:** a request's time budget broken into parts, showing which part dominates
- **Concept:** finding the bottleneck first — the biggest single win beats broad micro-tuning
- **Concept:** setting a performance budget or goal before optimizing
- **Pitfall:** premature optimization — tuning code that was never the bottleneck
- **Pitfall:** optimizing a benchmark that doesn't represent real production traffic

### Topic: Profiling Techniques (profiling-techniques, intermediate)
Using profilers to locate where time and memory actually go, instead of guessing.
- **Concept:** sampling profilers vs instrumenting profilers — overhead vs precision
- **Diagram:** reading a flame graph — width is time, stacks show call hierarchy
- **Code:** profiling a slow function and reading the hot path from the output
- **Concept:** CPU vs memory vs I/O/wait-time profiling — different bottlenecks, different tools
- **Concept:** profiling in production safely — low-overhead sampling, continuous profiling
- **Compare:** profiling locally (reproducible, limited) vs profiling in production (real, harder to control)
- **Pitfall:** profiling a debug build or a cold cache and drawing production conclusions

### Topic: Benchmarking Methodology (benchmarking-methodology, intermediate)
Measuring performance rigorously enough to trust the number and act on it.
- **Concept:** what a benchmark must control for — warm-up, environment noise, input realism
- **Concept:** microbenchmarks vs system-level benchmarks — what each can and can't tell you
- **Concept:** JIT warm-up and why the first N iterations of a benchmark lie
- **Concept:** statistical rigor — reporting percentiles/distributions, not a single run's average
- **Pitfall:** the compiler or runtime eliminating "dead" benchmark code, measuring nothing
- **Compare:** benchmarking in isolation vs benchmarking under realistic concurrent load
- **Concept:** regression benchmarking — tracking a metric over time in CI to catch slow creep

### Topic: Algorithmic & Data Structure Optimization (algorithmic-and-data-structure-optimization, intermediate)
Applying complexity and data-layout knowledge to make a real hot path faster. *(Assumes Big-O fundamentals from Data Structures & Algorithms' `complexity` group — this topic is about applying them, not re-deriving them.)*
- **Concept:** Big-O tells you scaling, not speed — a "worse" algorithm can win at small N
- **Concept:** picking the right data structure for the access pattern
- **Concept:** cache locality — why array-of-structs vs struct-of-arrays changes real-world speed
- **Diagram:** cache-friendly sequential access vs cache-unfriendly pointer-chasing
- **Concept:** reducing allocations on a hot path — reuse and pooling vs allocate-per-call
- **Compare:** a theoretically-optimal algorithm vs a simpler one that wins in practice on real inputs
- **Pitfall:** swapping in an asymptotically better algorithm that's slower at your actual input size

### Topic: Latency Optimization (latency-optimization, intermediate)
Reducing end-to-end and tail latency in request-driven systems.
- **Concept:** average latency hides the real user experience — why p50 isn't the number that matters
- **Concept:** tail latency — p99/p999 and why it compounds across a fan-out of calls
- **Diagram:** a request fanning out to ten dependencies — why overall p99 is worse than any single call's
- **Concept:** identifying the critical path — what's actually blocking the response
- **Concept:** reducing latency via caching, parallelizing independent calls, and precomputation
- **Concept:** queueing basics — how latency explodes as utilization approaches 100%
- **Compare:** adding capacity vs reducing work per request — two different levers for latency
- **Pitfall:** chasing average-latency improvements that make the tail worse

### Topic: Memory & GC Performance (memory-and-gc-performance, advanced)
Performance issues rooted in memory allocation and garbage collection.
- **Concept:** allocation cost — why "just allocate an object" isn't free at scale
- **Concept:** garbage collection basics — generational GC, stop-the-world pauses
- **Diagram:** a GC pause showing up as a latency spike on a timeline
- **Concept:** tuning GC — heap sizing, generation thresholds — trading throughput for pause time
- **Concept:** memory leaks in managed languages — retained references, not "no GC"
- **Code:** diagnosing a leak via heap snapshots and diffing over time
- **Concept:** object pooling and reuse to reduce allocation and GC pressure on hot paths
- **Pitfall:** "fixing" GC pauses by disabling GC instead of reducing allocation rate

### Topic: Concurrency Performance (concurrency-performance, advanced)
Using concurrency and parallelism to improve throughput, and the contention costs that limit it.
- **Concept:** concurrency (structure) vs parallelism (execution) — why both matter for performance
- **Concept:** Amdahl's Law revisited — the serial fraction caps parallel speedup
- **Concept:** lock contention — how a shared lock becomes the new bottleneck under parallel load
- **Diagram:** throughput vs number of threads, plateauing or dropping past a contention point
- **Concept:** reducing contention — finer-grained locks, sharding, lock-free structures, immutability
- **Compare:** thread-per-request vs event-loop/async — different concurrency models, different limits
- **Concept:** false sharing — cache-line contention between "independent" variables
- **Pitfall:** adding more threads to a lock-bound workload and making throughput worse

### Topic: Capacity Planning & Load Testing (capacity-planning-and-load-testing, intermediate)
Proving — not estimating — how much load a real system can take, and finding the bottleneck under load. *(Boundary: back-of-envelope capacity estimation for systems that don't exist yet is System Design's `capacity-estimation` group; this topic measures an existing system.)*
- **Concept:** load testing vs stress testing vs soak testing — different questions, different test shapes
- **Concept:** ramping load and watching for the knee — where latency/error rate breaks down
- **Diagram:** a load-test curve — throughput rising linearly, then latency spiking near saturation
- **Concept:** identifying the actual bottleneck resource — CPU, DB connections, thread pool, dependency
- **Concept:** realistic load generation — traffic shape, think time, concurrent users vs requests/sec
- **Concept:** soak testing for slow leaks or degradation that only appear over hours
- **Compare:** testing in staging vs shadow/replay testing against production-like traffic
- **Pitfall:** load testing with unrealistic traffic (all cache hits, no think time) and missing the real bottleneck

---

## Group: Technical Communication (technical-communication)

### Topic: Technical Writing Fundamentals (technical-writing-fundamentals, beginner)
The core skills of writing clearly for a technical audience.
- **Concept:** writing for the reader's time — lead with the conclusion, not the journey
- **Concept:** the inverted pyramid — most important information first, details after
- **Concept:** knowing your audience — what they already know, what they need from this doc
- **Concept:** concrete over vague — numbers, named examples, specific claims
- **Concept:** editing ruthlessly — cutting words that don't change the meaning
- **Compare:** a paragraph before and after a ruthless edit pass
- **Pitfall:** burying the actual ask or decision three paragraphs into a doc
- **Concept:** using structure — headings, bullets, tables — so a skimming reader still gets the point

### Topic: Writing Design Docs (writing-design-docs, intermediate)
Writing a document that proposes and gets agreement on a technical design before building it.
- **Concept:** why write a design doc — cheap to change on paper, expensive to change in code
- **Concept:** the standard shape — problem/context, goals and non-goals, proposed design, alternatives
- **Concept:** goals vs non-goals — scoping out of the debate what this design isn't trying to solve
- **Concept:** alternatives considered — showing the road not taken and why
- **Concept:** calling out trade-offs and risks explicitly instead of hiding them
- **Diagram:** a system diagram inside a design doc — the right level of detail for the audience
- **Compare:** a design doc written to inform vs one written to defend a decision already made
- **Pitfall:** a design doc with no clear decision or ask, so reviewers don't know what they're approving

### Topic: RFCs & Technical Decision Records (rfcs-and-technical-decision-records, advanced)
Formal processes for proposing, debating, and recording technical decisions in writing.
- **Concept:** the RFC process — proposal, open comment period, resolution
- **Concept:** building written consensus — comment threads, explicit sign-off from stakeholders
- **Concept:** architecture decision records (ADRs) — a lightweight record of what was decided, why, and when
- **Diagram:** an RFC lifecycle — draft → review window → decision → archived record
- **Compare:** an RFC (proposing a future decision) vs an ADR (recording one already made)
- **Concept:** why decisions need a durable record — avoiding re-litigating the same debate later
- **Concept:** who has decision authority vs who has input
- **Pitfall:** an RFC thread that goes in circles because no one owns the final call

### Topic: Documentation for Engineers (documentation-for-engineers, intermediate)
The practical, ongoing documentation engineers maintain, and keeping it alive.
- **Concept:** documentation as a product with users — write for the reader trying to get unblocked at 2am
- **Concept:** a good README's anatomy — what it is, how to run it, how to contribute
- **Concept:** API documentation — describing behavior and contracts, not just parameter types
- **Concept:** runbooks — step-by-step operational instructions for known failure modes
- **Concept:** docs-as-code — versioning docs alongside the code they describe
- **Compare:** docs that live next to the code vs a separate wiki — the staleness-risk trade-off
- **Pitfall:** a runbook that's never been tested and fails during the actual incident it was written for
- **Concept:** signaling doc freshness — last-reviewed dates, owners — so readers can trust or distrust it

### Topic: Presenting Technical Work (presenting-technical-work, intermediate)
Communicating technical work verbally and visually to different audiences — reviews, demos, leadership updates.
- **Concept:** adjusting altitude to the audience — engineers want mechanism, leadership wants impact and risk
- **Concept:** structuring a technical presentation — problem, options, recommendation, ask
- **Concept:** demos — showing the real thing beats describing it, with a fallback if it breaks
- **Concept:** handling pushback and hard questions live without getting defensive
- **Compare:** a status update to your team vs the same update to a skip-level manager
- **Concept:** using a diagram instead of a paragraph when explaining architecture live
- **Pitfall:** a demo or presentation that drowns the one key decision needed in unnecessary detail

---

## Group: Behavioral & Staff+ Competencies (behavioral)

*Note: overlaps with `behavioral-interview` in Area 17 (Interview Prep & Career) per the map's own overlap flag — this group is the intended home; Area 17, if built, should link here rather than duplicate.*

### Topic: Behavioral Interview Fundamentals (behavioral-interview-fundamentals, beginner)
What behavioral interviews measure and the STAR structure used to answer them.
- **Concept:** what behavioral interviews actually score — past behavior as a predictor of future behavior
- **Concept:** the STAR format — Situation, Task, Action, Result
- **Diagram:** a STAR answer's time allocation — brief S/T, most time on Action, crisp Result
- **Concept:** why interviewers probe with follow-ups — testing whether the story is real and yours
- **Concept:** "I" vs "we" — clearly owning your specific contribution in a team story
- **Compare:** a vague, generic answer vs a specific, evidence-rich answer to the same question
- **Pitfall:** a rambling answer with no clear result or takeaway
- **Concept:** preparing a story bank in advance vs improvising live

### Topic: Crafting STAR Stories (crafting-star-stories, intermediate)
Turning real work experience into sharp, reusable STAR stories.
- **Concept:** picking stories with real stakes and a clear before-vs-after
- **Concept:** one story, many questions — mapping a single strong story to multiple prompts
- **Concept:** quantifying results — numbers, scale, business impact, not just "it went well"
- **Concept:** the Action section is the interview — depth on decisions and trade-offs you personally made
- **Concept:** a worked example — turning a vague memory into a tight STAR story
- **Concept:** anticipating follow-up questions and pre-loading the details they'll ask for
- **Pitfall:** a story where your role is unclear and it sounds like the team's success, not yours
- **Concept:** building a story matrix — mapping your stories against common question categories

### Topic: Common Behavioral Questions (common-behavioral-questions, beginner)
The canonical bank of behavioral prompts and what each is actually trying to assess.
- **Concept:** question categories — conflict, failure, leadership, ambiguity, prioritization, influence
- **Concept:** "tell me about a conflict with a coworker" — what's really being tested
- **Concept:** "tell me about a time you failed" — testing accountability, not perfection
- **Concept:** "tell me about a time you disagreed with your manager" — testing judgment under disagreement
- **Concept:** "tell me about a decision with incomplete information" — testing judgment under ambiguity
- **Concept:** "tell me about a time you influenced without authority" — testing leadership signal at any level
- **Concept:** "tell me about your proudest achievement" — testing what you value and how you measure impact
- **Compare:** the same question asked of an IC vs a staff+ candidate — what "good" looks like at each level

### Topic: Leadership & Influence Without Authority (leadership-and-influence-without-authority, intermediate)
Demonstrating leadership and cross-team influence when you didn't have formal authority over the people involved.
- **Concept:** leadership is not management — driving outcomes through others without a reporting line
- **Concept:** influence tactics — data and evidence, alliance-building, framing around shared goals
- **Concept:** identifying and winning over a skeptical stakeholder
- **Concept:** leading through ambiguity — setting direction when no one assigned you the problem
- **Compare:** influence via authority (as a manager) vs influence via credibility (as an IC)
- **Concept:** the "informal tech lead" story arc — noticing a gap, taking it on, bringing others along
- **Pitfall:** a leadership story that's actually just solo work, with no one else involved

### Topic: Conflict & Difficult Conversations (conflict-and-difficult-conversations, intermediate)
Handling interpersonal friction — disagreement, hard feedback, underperformance — and telling that story well.
- **Concept:** task conflict (healthy) vs relationship conflict (unhealthy) — naming which one your story shows
- **Concept:** structuring a hard-feedback conversation — specific behavior, impact, desired change
- **Concept:** disagreeing with a manager or senior stakeholder respectfully and effectively
- **Concept:** de-escalating a heated technical disagreement in a meeting
- **Concept:** addressing underperformance on your team — clarity, support, and follow-through
- **Compare:** a conflict story that ends in resentment vs one that ends in a stronger working relationship
- **Pitfall:** a conflict story where you "won" but damaged trust

### Topic: Ownership & Scope of Impact (ownership-and-scope-of-impact, intermediate)
Showing a track record of increasing scope and impact — what interviewers use to calibrate level.
- **Concept:** scope as the unit interviewers use to calibrate level — team, project, org, company
- **Concept:** ownership — taking a problem from ambiguous to shipped without being told each step
- **Concept:** going beyond your ticket — noticing and fixing a problem nobody assigned you
- **Diagram:** a scope ladder — IC task → project → cross-team initiative → org-wide impact
- **Concept:** measuring impact in business terms — cost saved, risk removed, velocity gained
- **Compare:** a story about effort ("I worked really hard") vs a story about impact ("here's what changed")
- **Pitfall:** describing a big project's impact without being able to say your specific contribution

### Topic: Failure & Growth Stories (failure-and-growth-stories, intermediate)
Talking about mistakes and setbacks in a way that builds credibility instead of undermining it.
- **Concept:** why interviewers ask about failure — testing honesty, accountability, and real learning
- **Concept:** picking a real failure with real stakes, not a disguised humblebrag
- **Concept:** owning your part specifically — not deflecting blame to the team or process
- **Concept:** the "what changed after" — a credible failure story ends with a concrete behavior change
- **Compare:** a failure story that reads as blame-shifting vs one that reads as ownership
- **Concept:** calibrating severity to the question — real stakes without sounding catastrophic
- **Pitfall:** a "failure" story where nothing bad actually happened — reads as evasive

### Topic: Staff+ Competencies (staff-plus-competencies, advanced)
The signals that distinguish senior-IC and staff+ candidates — technical vision, org-level impact, force-multiplying others.
- **Concept:** what changes at staff+ — impact through others and systems, not just your own output
- **Concept:** the multiplier effect — mentorship, tooling, and process changes that scale a team's output
- **Concept:** staff engineer archetypes — tech lead, architect, solver, right-hand
- **Concept:** technical vision — setting direction for a domain across multiple teams or quarters
- **Concept:** operating with organizational ambiguity — influencing roadmap and priorities, not just execution
- **Compare:** a senior-IC story (deep, bounded technical ownership) vs a staff story (breadth, org-level leverage)
- **Concept:** mentorship and growing other engineers as a demonstrable body of work
- **Pitfall:** a "staff-level" story that's actually still scoped to one person's individual contribution

### Topic: Closing the Interview Strong (closing-the-interview-strong, beginner)
The final minutes of an interview — questions to ask, and leaving a strong last impression.
- **Concept:** "any questions for us?" is still part of the evaluation, not a formality
- **Concept:** good questions signal genuine interest and research, not perks-shopping
- **Concept:** questions that reveal what you'd actually want to know before joining
- **Compare:** a generic question ("what's the culture like?") vs a sharp one tailored to the role
- **Concept:** reading the room — adjusting follow-up questions based on the interviewer's answers
- **Concept:** a closing statement that restates genuine interest and fit without sounding rehearsed
- **Pitfall:** asking only about compensation and perks in a technical round, or asking nothing at all

---

## Totals
9 groups · 67 topics · 524 slides.

## Overlaps / gaps flagged
- **`behavioral` (A9) = `behavioral-interview` (A17)** — pre-flagged in the map. This group is built as the full, owned version; Area 17 (not yet built) should cross-link rather than duplicate.
- **`cicd` (A9) vs `iac`/`cicd-infra` (A10, Cloud/DevOps/SRE)** — not previously flagged in the map, but a real risk: A9's `cicd` is the software-delivery practice (pipelines, deploy strategy, release process, feature flags); A10's groups are infra provisioning/automation (Terraform, GitOps). Boundary noted inline in the group; worth confirming when A10 is expanded.
- **`production-debugging-observability` (A9/debugging) vs `observability` (A7) / `observability-ops` (A10)** — consistent with the map's existing A7/A10 flag; this topic is scoped to the debugging workflow, not the tooling stack itself.
- **`algorithmic-and-data-structure-optimization` (A9/performance-engineering)** cross-links `complexity` (A1) — assumes, doesn't re-teach, Big-O.
- **`capacity-planning-and-load-testing` (A9/performance-engineering)** cross-links `capacity-estimation` (A7) — this topic measures existing systems; A7's is back-of-envelope estimation for new ones.
- **`async-collaboration-for-distributed-teams` (A9/code-review)** boundary drawn against `technical-communication`'s doc-writing topics (same group, no cross-area risk) — collaboration mechanics vs the writing itself.
- No design-patterns content duplicated here — confirmed patterns stay in Area 8 per the map's flag; `clean-architecture` here covers layering/DDD only, a genuinely distinct concern.
- No gaps found in the group list itself — all 9 groups from the map are represented with no invented or borrowed groups.
