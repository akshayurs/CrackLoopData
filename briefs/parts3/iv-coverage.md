# Interview-question coverage audit — system-design area

Gap-fill for `briefs/expanded/system-design.md` (52 groups / 382 topics) plus the two question
banks (`briefs/parts2/iv-hld.md`, `briefs/parts2/iv-lld.md`). Scope: interview-question categories
a system-design-focused candidate genuinely faces that have **no home anywhere in this area**.
Does not touch `sd-playbook`, `design-in-practice`, any `interview-*` bank group, or case studies.

---

## Group: Talking About Your Own Designs (design-experience-questions)
*The design-specific behavioral layer — questions about a real system you actually built, distinct from the generic STAR/leadership behavioral round (that lives in `behavioral`, Area 9 / `behavioral-interview`, Area 17). Cross-link: `sd-playbook` for the from-scratch design method; this group is "tell me about a design you already shipped," not "design X for me now."*

### Topic: Walk Me Through the Architecture of Something You Built (iv-walk-through-your-architecture, intermediate)
The opening question of nearly every senior+ system-design loop, and why a chronological build-log answer scores worse than a structured one.
- The question, verbatim, and why it's asked before any whiteboard prompt (overview)
- What's really being probed: can you own and explain a real system, not recite a textbook one (concept)
- Why "we used microservices and Kafka" name-dropping scores low without the why (concept)
- Structuring the answer: problem → constraints → key decisions → what changed over time (concept)
- Diagram: the answer shape as problem → decisions → outcome, not a feature timeline (diagram)
- Picking which system to talk about: the one with real trade-offs, not the biggest one (concept)
- Going deep on one decision when the interviewer asks "why" instead of restating the diagram (concept)
- Compare: a resume-recitation answer vs a decisions-and-trade-offs answer to the same prompt (compare)
- Follow-up: "what was the scale, actually?" — having real numbers ready (concept)
- Pitfall: an answer with no numbers, no trade-off, and no owned decision (pitfall)
- Interview: "Walk me through the architecture of the last system you designed" (interview)

### Topic: What's the Hardest Technical Decision You've Made? (iv-hardest-technical-decision, advanced)
Distinguishing a genuinely hard trade-off from a hard *implementation* problem, and why interviewers can tell the difference immediately.
- What "hard" means here: a decision with real costs on both sides, not a bug that took a while (concept)
- Why picking a decision with an obvious right answer undersells you (concept)
- Structuring the answer: the options actually considered, the axis you decided on, the cost you accepted (concept)
- Diagram: two real options with their costs laid out side by side (diagram)
- Concrete example: choosing eventual consistency for a feature and living with the support cost (concept)
- Compare: a technically-hard story vs a trade-off-hard story — which one this question wants (compare)
- Follow-up: "would you make the same call again?" — showing judgment, not defensiveness (concept)
- Pitfall: a decision that was actually made by your manager or the team, retold as yours (pitfall)
- Interview: "Tell me about the hardest technical trade-off you've had to make" (interview)

### Topic: Tell Me About a Design That Failed (iv-a-design-that-failed, advanced)
Why interviewers deliberately ask for a failure, and how a real one — told with an honest cause and a fix — reads stronger than a disguised success.
- Why this question exists: judgment under a failure signal is harder to fake (concept)
- Picking a real failure, not a "worked too hard" non-failure in disguise (concept)
- Structuring the answer: what you designed, what assumption broke, what it cost, what you changed (concept)
- Diagram: the assumption that broke and the blast radius it caused (diagram)
- Concrete example: a schema decision that didn't survive a 10x traffic increase (concept)
- Compare: a defensive retelling vs an owned, specific retelling of the same failure (compare)
- Follow-up: "what would have caught this earlier?" — process, not just the fix (concept)
- Pitfall: blaming the requirements, the team, or "we didn't have time" with no self-reflection (pitfall)
- Interview: "Tell me about a system you designed that didn't hold up" (interview)

### Topic: What Would You Redo, Knowing What You Know Now? (iv-what-would-you-redo, advanced)
The retrospective-judgment question that separates "I'd change nothing" candidates from ones who show real hindsight.
- Why "nothing, it worked out fine" is the answer that costs you the most points (concept)
- Distinguishing a redo you'd make from a redo that's just complaining about constraints (concept)
- Structuring the answer: what you knew then, what you know now, what specifically changes (concept)
- Diagram: then-vs-now decision points on the same system (diagram)
- Concrete example: redoing a synchronous integration as async after seeing it under load (concept)
- Compare: "I'd rewrite everything" (red flag — no judgment) vs one targeted, justified change (compare)
- Follow-up: "why didn't you know that at the time?" — reasoning about what information was actually available (concept)
- Pitfall: a redo that's really just relitigating someone else's decision (pitfall)
- Interview: "If you could redesign that system today, what would you change?" (interview)

### Topic: Questions to Ask About Their Architecture and Team (iv-questions-to-ask-about-their-system, intermediate)
The design-specific version of "any questions for me?" — asking about their actual scaling story, on-call reality, and technical debt instead of generic culture questions (which are covered in `behavioral-questions-to-ask`, Area 17).
- Why this moment is still evaluated, and why generic questions waste it (concept)
- Cross-link: `behavioral-questions-to-ask` for the general two-way-signal framing this Topic assumes (concept)
- Questions that read as senior: "what's the part of the system you'd redesign if you could?" (concept)
- Questions that surface real signal: on-call load, biggest recent incident, how architecture decisions get made (concept)
- Diagram: question categories — scale, ownership, debt, decision process (diagram)
- Concrete example: asking about a specific technology mentioned earlier in the loop, not a generic one (concept)
- Compare: a question that signals genuine technical curiosity vs one that signals you didn't listen (compare)
- Pitfall: asking a question the job description already answered (pitfall)
- Interview: "Do you have any questions about how we've built this?" (interview)

---

## Group: Interview Formats Beyond the Standard Loop (design-round-formats)
*Round-specific mechanics that differ from the standard 45-60 minute HLD round already covered end-to-end by `sd-playbook` and `sd-interview-playbook` (Area 17). Each Topic here covers what changes about the *format*, not the design method itself — cross-link back to `sd-playbook` for the method that still applies inside each format.*

### Topic: The Rapid-Fire Trade-off Screen (iv-rapid-fire-tradeoff-screen, intermediate)
The phone-screen format of 8-10 quick trade-off questions in 15-20 minutes, and why rambling through the standard framework fails it.
- What this round looks like: quick-fire questions, no whiteboard, 60-90 seconds each (overview)
- Why the full requirements-gathering framework doesn't fit here (concept)
- The pattern that scores: name the axis, pick a side, give one sentence of why (concept)
- Diagram: a rapid-fire answer shape vs a full deep-dive answer shape, side by side (diagram)
- Concrete example: "SQL or NoSQL for a shopping cart?" answered in three sentences (concept)
- Compare: hedging with "it depends, well, both have trade-offs..." vs committing to a side (compare)
- Cross-link: `sd-tradeoff-articulation` (Area 17) for the underlying trade-off-naming skill this format compresses (concept)
- Pitfall: treating a 90-second question like a 10-minute deep dive and running out the clock (pitfall)
- Pitfall: giving a one-word answer with no reasoning, which reads as a guess (pitfall)
- Interview: "Quick one — would you use a queue or direct call here, and why?" (interview)

### Topic: The Bar-Raiser and Hiring-Manager Design Round (iv-bar-raiser-design-round, advanced)
How a bar-raiser or hiring-manager-led design round differs in intent from a peer round, even when the prompt looks identical.
- What a bar-raiser is actually calibrating: consistency across candidates, not just this one's skill (concept)
- Why the hiring manager's round often probes ownership and judgment over raw technique (concept)
- Diagram: what a peer interviewer scores vs what a bar-raiser scores on the same answer (diagram)
- Why bar-raisers often let you struggle longer before offering a hint (concept)
- Concrete example: the same "why this trade-off" question landing differently depending on who's asking (concept)
- Compare: optimizing an answer for a peer's checklist vs for a bar-raiser's calibration bar (compare)
- Follow-up: a hiring-manager question about how you'd staff or sequence building the system (concept)
- Pitfall: assuming the bar-raiser is hostile because their questions feel less structured (pitfall)
- Interview: "As the hiring manager, I want to know how you'd sequence building this with a team of three" (interview)

### Topic: The Take-Home Architecture Exercise (iv-take-home-architecture-exercise, intermediate)
The async design-doc or architecture-proposal exercise some senior/staff loops use instead of (or alongside) a live whiteboard round.
- What this format asks for: a written design doc or diagram set, not working code (overview)
- Why it's graded on the same axes as a live round, minus the time pressure (concept)
- Cross-link: `writing-a-design-doc` (`design-in-practice`) for the doc structure itself — this Topic covers using it as an interview artifact (concept)
- Structuring the submission: problem, requirements, options considered, chosen design, trade-offs (concept)
- Diagram: an architecture exercise submission outline (diagram)
- Time-boxing the exercise instead of polishing it for days (concept)
- Compare: a live round's ability to probe follow-ups vs a take-home's need to preempt them in writing (compare)
- Pitfall: submitting a diagram with no written rationale, leaving the evaluator to guess your reasoning (pitfall)
- Pitfall: over-scoping the design far beyond what the prompt's constraints call for (pitfall)
- Interview: "Send us a one-page design for this system by Friday" (interview)

---

## Audit notes

**Already covered — nothing added:**
- Level-specific expectations (SDE-1 → staff, same question graded differently): `leveling-expectations` +
  `staff-level-system-design-signal` (`sd-playbook`), plus `sd-calibrating-seniority` and
  `behavioral-calibrating-level` (Area 17, interview-prep).
- Live-collaboration mechanics (managing the clock, thinking out loud, redirecting, "what would you do with
  more time"): `the-interview-framework`, `communication-and-whiteboarding`, `deep-dives-and-trade-off-discussions`
  (`sd-playbook`), plus `sd-driving-conversation` and `sd-interview-framework` (Area 17).
- Handling hints / interviewer pushback / curveballs: `handling-interviewer-pushback`,
  `designing-under-ambiguity` (`sd-playbook`), `sd-deep-dive-followups` (Area 17).
- Standard round-length and who's-in-the-room basics (45 vs 60 min, peer vs bar-raiser vs hiring manager):
  `sd-interview-format` (Area 17) — thin (one bullet on bar-raiser/HM), which is why this audit deepened it
  into its own Topic above rather than duplicating the whole group.
- Generic reverse questions ("any questions for me?"): `behavioral-questions-to-ask` (Area 17,
  `behavioral-interview`) — general career/culture framing; this audit added the design-specific version
  (asking about their architecture/team) since that angle wasn't covered there.
- LLD / machine-coding round with real implementation: `lld-interview-process` (method + a worked code
  example) plus `lld-case-studies` (each case study includes implementation-level content).
- Take-home and pair-programming formats (coding-flavored): full `take-home` group (Area 17,
  `take-home-strategy`, `pair-programming-format`, etc.) — this audit added only the architecture-specific
  take-home variant, which that group doesn't cover (it's written for coding submissions).
- Generic behavioral question archetypes (conflict, failure, ambiguity, feedback): `behavioral-question-archetypes`
  (Area 17) — distinct from this area's new `design-experience-questions`, which is architecture-specific,
  not generic-behavioral.

**Added — genuinely had no home:**
- `design-experience-questions` (5 topics): resume/experience-in-a-design-context questions
  ("walk me through your architecture," "hardest decision," "a design that failed," "what would you
  redo") plus the design-specific reverse question. These are asked in nearly every senior+ loop but
  are neither generic behavioral (Area 9/17, which teaches STAR/conflict/leadership) nor a from-scratch
  design prompt (`sd-playbook`) — no existing Topic addresses talking about a system you already built.
- `design-round-formats` (3 topics): the rapid-fire phone-screen format, the bar-raiser/hiring-manager
  round's distinct calibration intent, and the take-home architecture exercise. All three are real,
  distinct formats with no Topic anywhere in the area or in Area 17's interview-prep coverage, which
  assumes the standard live 45-60 minute round throughout.

**Considered and cut (value filter):**
- Pair-design (interviewer actively co-designs alongside the candidate) — rare enough, and mechanically
  the standard round with more interviewer participation; already addressed by `sd-driving-conversation`
  and `handling-interviewer-pushback`. Not worth a dedicated Topic.
- A generic "screening call" format Topic beyond the rapid-fire trade-off angle — the only
  system-design-specific mechanic a screen adds is the rapid-fire compression, which is covered above;
  the rest (scheduling, recruiter chat) isn't design content.

**Cross-area recommendations (not authored here — outside this file's scope):**
- Domain-flavored design rounds already have a *technical* home: `frontend-system-design` (web-frontend),
  `mobile-system-design` (mobile), `ml-system-design` (ai-ml) each carry a framework Topic + case studies.
  `data-engineering` has no equivalent system-design group at all — worth flagging to that area's owner
  as a gap (a data-pipeline/warehouse design framework + case study), separate from this audit's scope.
  None of these areas currently frame their content as "how the interview round differs for this role"
  (vs. backend) beyond one bullet in `sd-interview-format` — if that distinction is wanted, it belongs
  in each domain area (interview framing) or as a single cross-referencing note in `sd-interview-format`,
  not duplicated across five areas.
