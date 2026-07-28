# Phase D — Craft & Interview

New material for the merged Study Area `system-design` (LLD + HLD, beginner → expert). This part supplies:
(a) a new group `design-in-practice` ("for work, not just for the interview"), (b) expert-tier
additions to the existing `sd-playbook` group, and (c) merge notes for assembling the final area.
Format matches `briefs/expanded/system-design.md` lines 1–60. All slugs below were checked against
every `### Topic:` slug already in `briefs/expanded/system-design.md` and `briefs/expanded/object-oriented-design.md` — no collisions.

---

## Group: Design in the Real World (design-in-practice)
*designing on the job, not just in the interview room — docs, migrations, rollouts, review, and org cost*

### Topic: Writing a Design Doc / RFC (writing-a-design-doc, intermediate)
Structuring and writing a design doc that survives review and gets approved — stating the problem before the solution, writing alternatives considered so the rejections teach something, and making non-goals explicit. Boundary: general writing craft and doc templates belong to `engineering-craft`'s `technical-communication`; this Topic covers only the design-doc-specific structure and argument.
- Why design docs exist: forcing a design to survive contact with reviewers (concept)
- The anatomy of an approvable doc: problem, goals, non-goals, alternatives, decision (overview)
- Stating the problem before the solution: the mistake reviewers spot first (concept)
- Alternatives considered: writing them so the rejection reasons teach, not just list (concept)
- Diagram: a design doc as an argument tree, not a report (diagram)
- Explicit non-goals: what you're deliberately not solving, and why that's a feature (concept)
- Compare: a doc written to get sign-off vs a doc written to look thorough (compare)
- Pitfall: the doc that hides the real decision inside implementation detail (pitfall)
- Interview: "Walk me through how you'd get a risky design approved" (interview)

### Topic: Brownfield System Design (brownfield-system-design, advanced)
Designing changes inside a live system that can't be rewritten — mapping blast radius, maintaining backwards compatibility, and the mechanics of dual-writes and backfills without breaking things mid-flight. Boundary: the pattern catalog (strangler fig, etc.) lives in `system-design`'s microservices group; this Topic is the practitioner's playbook for executing a migration safely.
- Greenfield vs brownfield: why "just redesign it" is rarely the real option (concept)
- Mapping the blast radius: who and what depends on the thing you're changing (concept)
- Diagram: an expand-contract migration in stages (diagram)
- Backwards compatibility: versioning the contract while the old caller still exists (concept)
- Dual-writes: keeping two systems consistent during a cutover, and where they drift (concept)
- Backfills: safely rewriting historical data without an outage (concept)
- Compare: big-bang cutover vs incremental migration — when each is actually right (compare)
- Pitfall: the migration with no way to tell if it's actually done (pitfall)
- Interview: "How would you migrate this system's data store with zero downtime?" (interview)

### Topic: Rolling Out a Design (rolling-out-a-design, advanced)
Getting a new design live safely — phased rollout, feature flags, shadow traffic, dark launches — and having a real rollback plan before you ship, not after something breaks. Boundary: pipeline/automation mechanics belong to `engineering-craft`'s `cicd`; this Topic covers the design-time rollout strategy and how to reverse it, not the tooling.
- Why the rollout is part of the design, not an afterthought (concept)
- Phased rollout: percentage ramps and the metrics that gate each step (concept)
- Feature flags as a design tool: decoupling deploy from release (concept)
- Shadow traffic and dark launches: testing the real path without real consequences (concept)
- Diagram: a rollout plan as a decision tree with abort points (diagram)
- Writing a rollback plan before launch, not during the incident (concept)
- Compare: canary release vs blue-green vs shadow traffic — what each actually protects against (compare)
- Pitfall: a rollout with no kill switch because "it should be fine" (pitfall)
- Interview: "How would you roll out a change to a payment path safely?" (interview)

### Topic: Reviewing Someone Else's Design (reviewing-a-design, intermediate)
Giving useful architectural feedback on a design doc — what to look for, how to phrase pushback so it lands, and spotting the assumption the author never wrote down. Boundary: line-by-line code review is `engineering-craft`'s `code-review`; this Topic is review of the design/architecture layer, before code exists.
- What a design review is actually checking: correctness, cost, and blast radius (concept)
- The unstated assumption: finding what the author didn't write down (concept)
- A checklist for reading a design doc critically (overview)
- Giving feedback that changes the design, not just the wording (concept)
- Diagram: separating "must fix" from "consider" comments (diagram)
- Compare: a nitpicking reviewer vs a reviewer who asks the one question that matters (compare)
- Pitfall: approving a design because pushing back feels adversarial (pitfall)
- Interview: "Review this design doc and tell me what concerns you" (interview)

### Topic: Cost- and Org-Aware Design (cost-and-org-aware-design, expert)
Designing with organizational constraints as first-class inputs — build vs buy, the operational burden a design creates, who ends up on call for it, and designing for the team you actually have. Boundary: cross-team org trade-offs at the staff/principal level are covered by the `sd-playbook` addition below; this Topic is the cost/ownership/team-fit lens applied to any single design decision.
- Build vs buy: the real cost of "we could build that ourselves" (concept)
- Operational burden as a design cost, not an implementation detail (concept)
- Who's on call for this: designing with the owning team's reality in mind (concept)
- Diagram: total cost of ownership across build, run, and maintain (diagram)
- Designing for the team you have: skills, headcount, and time horizon as constraints (concept)
- Compare: the "correct" design vs the design this team can actually operate (compare)
- Pitfall: choosing the interesting technology over the boring one that fits (pitfall)
- Interview: "Would you build or buy this, and why?" (interview)

**Flagged overlap (unavoidable, kept thin):** "operational burden"/"on-call" here necessarily brushes against `engineering-craft`'s `debugging` (incident response) and `clean-architecture`/DDD — this group states the design-time cost/ownership question only, and defers "how you actually debug/operate it" and "how you structure the domain model" to those groups.

---

## Additions to existing group: System Design Interview Playbook (sd-playbook)

The existing group already covers the framework, clarifying requirements, driving the HLD, deep dives,
communication/whiteboarding, common mistakes, and leveling expectations. These three add the tiers above
that, none restated:

### Topic: Designing Under Ambiguity (designing-under-ambiguity, advanced)
Handling the deliberate flavor of interview where the interviewer withholds requirements or context on purpose, and making progress by stating and testing assumptions instead of stalling on a fourth clarifying question.
- Why interviewers withhold information on purpose (concept)
- Stating an assumption out loud instead of asking a fourth clarifying question (concept)
- Diagram: the assumption → decision → checkpoint loop under ambiguity (diagram)
- Making a defensible call with incomplete information (concept)
- Compare: guessing silently vs narrating your reasoning under uncertainty (compare)
- Pitfall: freezing up when the interviewer won't just answer the question (pitfall)
- Interview: "I don't have that number — what would you assume, and why?" (interview)

### Topic: Handling Interviewer Pushback (handling-interviewer-pushback, advanced)
Responding well when the interviewer challenges a choice, disagrees, or introduces a curveball mid-design — defending a decision with reasoning, and knowing when to actually change your mind.
- Why pushback is a deliberate test, not a sign you're wrong (concept)
- Defending a decision with the trade-off you already made, not by repeating it louder (concept)
- Recognizing a genuinely good counterpoint and updating your design (concept)
- Diagram: the pushback exchange as propose → challenge → resolve (diagram)
- Compare: caving immediately vs digging in — the middle path that scores well (compare)
- Pitfall: treating every objection as an attack on your competence (pitfall)
- Interview: "What if I told you that database won't scale to that load?" (interview)

### Topic: The Staff/Principal Signal (staff-level-system-design-signal, expert)
What separates a senior-passing answer from a staff/principal-passing one — org-level thinking: the migration story, cross-team trade-offs, and decisions that outlive a single team's roadmap.
- What "staff signal" actually means beyond a bigger diagram (concept)
- Narrating the migration story: how the org gets from here to there, not just the end state (concept)
- Cross-team trade-offs: whose roadmap absorbs the cost of your design (concept)
- Diagram: a design's blast radius across team boundaries (diagram)
- Compare: a senior answer (one system, right) vs a staff answer (one system, right, and it fits the org) (compare)
- Pitfall: designing an elegant system nobody else's team can adopt (pitfall)
- Interview: "How would this decision play out across three teams over two years?" (interview)

*(Considered and cut: a remote/virtual-whiteboard-mechanics topic — it's tooling/logistics, not design judgment; doesn't clear the value filter as its own Topic. Fold a line on it into `communication-and-whiteboarding` if desired.)*

---

## Merge notes

**Boundary/dedupe decisions for the merged `system-design` area:**
1. **`sd-playbook` (this area) vs `interview-prep`'s `sd-interview-playbook`, and `engineering-craft`'s `behavioral` vs `interview-prep`'s `behavioral-interview`.** Both pairs are flagged in `briefs/area-group-map.md` as the same content under two names. Recommendation: home the full design-interview playbook (including this phase's 3 additions) in `system-design`'s `sd-playbook`, and have `interview-prep` delete `sd-interview-playbook` and point to this group instead; same pattern for `behavioral` — keep it in `engineering-craft`, delete `interview-prep`'s `behavioral-interview` duplicate. `interview-prep` keeps its genuinely distinct groups (`coding-playbook`, `take-home`, `negotiation`).
2. `design-in-practice` (this phase) is new and doesn't duplicate any existing group in either source brief — verified via full slug/group scan above.
3. Every cross-link flagged in this phase's group/Topic scope lines (`technical-communication`, `cicd`, `code-review`, `debugging`, `clean-architecture`, all in `engineering-craft`) should render as an explicit "see also" in the authored content, not get re-explained.

**Suggested group order for the merged area** (group order in the brief file drives app ordering per `tools/regen_v3.py`'s relevance-ordering rule):

1. `sd-fundamentals` → `capacity-estimation` *(Foundations)*
2. `oop-fundamentals` → `design-principles` → `creational-patterns` → `structural-patterns` → `behavioral-patterns` → `uml` → `anti-patterns` → `oo-concurrency` → `lld-framework` → `lld-case-studies` *(LLD)*
3. `load-balancing` → `caching` → `storage-scale` → `consistency-replication` → `messaging-streaming` → `microservices` → `api-design` → `resilience` → `search-indexing` → `observability` → `case-studies` *(HLD)*
4. `design-in-practice` → `sd-playbook` *(Craft & Interview — real-world practice before the interview meta-layer, since the playbook now leans on Phase D's design-doc/rollout/review vocabulary)*
