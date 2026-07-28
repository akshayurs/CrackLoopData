# Area: CS Theory & Math (cs-theory-math)

*`(cross-link: Area N `group-slug`)` parentheticals mean that content's primary home is elsewhere — mentioned here only as a one-line bridge, not duplicated.*

## Group: Discrete Mathematics (discrete-math)

### Topic: Propositional & Predicate Logic (propositional-predicate-logic, beginner)
Truth tables, logical equivalences (De Morgan's), and quantifiers (∀/∃) with their negation rules — the formal language behind correctness proofs, SQL predicates, and specifications.
- Why formal logic matters for engineers (specs, SQL `WHERE` predicates, boolean short-circuiting)
- Propositions and connectives (¬ ∧ ∨ → ↔) — truth tables
- Logical equivalence & De Morgan's laws (diagram)
- Tautologies, contradictions, and contingencies
- Conditional vs biconditional — converse, inverse, contrapositive (compare)
- Predicates and quantifiers (∀, ∃) — reading nested statements correctly
- Negating quantified statements (pitfall: ¬∀x P(x) ≠ ∀x ¬P(x))
- Nested quantifier order matters: ∀x∃y vs ∃y∀x, with a concrete example
- Logic in code: short-circuit evaluation and De Morgan in `if` conditions (code)
- Pitfall: conflating "necessary" and "sufficient" condition language
- Interview: simplify this boolean expression — full walkthrough

### Topic: Proof Techniques (proof-techniques, beginner)
Direct proof, contrapositive, contradiction, induction (weak/strong), and proof by cases — the backbone of algorithm-correctness arguments.
- Why proofs show up in interviews (algorithm correctness, loop invariants)
- Direct proof — structure and a worked example
- Proof by contrapositive — when it beats a direct proof (compare)
- Proof by contradiction — the classic √2-is-irrational example
- Weak induction — base case + inductive step, structure
- Strong induction — when weak induction isn't enough (every integer >1 has a prime factorization)
- Proof by cases — an exhaustive case-split example
- Loop invariants as induction in disguise (diagram/code, ties to algorithm correctness)
- Pitfall: an inductive step that silently assumes what it's proving
- Interview: prove this recursive function is correct — full walkthrough

### Topic: Sets, Functions & Relations (sets-functions-relations, beginner)
Set operations, functions (injective/surjective/bijective), equivalence relations, and partial orders — the vocabulary behind data modeling and dependency scheduling.
- Set operations — union, intersection, difference, complement (diagram: Venn)
- Set identities and proving set equality
- Cartesian product and power set — why |P(S)| = 2^n
- Functions: injective, surjective, bijective (compare, with concrete examples)
- Composition and inverse functions — when an inverse exists
- Relations as sets of pairs; representing one as a matrix or a graph
- Equivalence relations — reflexive/symmetric/transitive and the partitions they induce
- Partial orders & Hasse diagrams (diagram)
- Total vs partial order: topological sort as linearizing a partial order (cross-link Area 1 `graphs`)
- Pitfall: assuming a relation is transitive when it isn't
- Interview: is this relation an equivalence relation? — checklist walkthrough

### Topic: Combinatorics & Counting (combinatorics-counting, intermediate)
Permutations vs combinations, the pigeonhole principle, and inclusion-exclusion — the reasoning toolkit behind "how many ways" interview questions (cross-link: fast nCr-mod-p computation lives in Area 1 `math-number-theory`).
- The product rule and sum rule — the two counting primitives
- Permutations vs combinations — when order matters (compare)
- Counting with repetition
- The pigeonhole principle — statement and the standard proof pattern
- Pigeonhole in interviews: non-obvious applications (collision-style arguments)
- Inclusion-exclusion — the 2-set and 3-set formula (diagram)
- Inclusion-exclusion — a worked counting example
- Binomial coefficients and Pascal's triangle — identities worth knowing
- Stars and bars — counting distributions into bins
- Pitfall: overcounting when order or identical items aren't handled correctly
- Interview: "how many ways can you arrange…" — live walkthrough

### Topic: Graph Theory Foundations (graph-theory-foundations, intermediate)
Graphs as mathematical structures — connectivity, bipartiteness, Euler/Hamiltonian paths, coloring, and planarity (cross-link: traversal/shortest-path/MST algorithms live in Area 1 `graphs` — this topic is structure, not algorithms).
- What separates graph theory from graph algorithms (framing)
- Graph terminology: degree, the handshake lemma, dense vs sparse
- Connectivity — components, strongly vs weakly connected (diagram)
- Bipartite graphs — the 2-coloring test
- Euler paths/circuits — the bridges-of-Königsberg condition
- Hamiltonian paths — why they're hard (NP-completeness preview, cross-link `theory-of-computation`)
- Graph coloring — chromatic number and why map-coloring needs ≤4 colors
- Planarity — Kuratowski's intuition (diagram)
- Trees as a special graph — n−1 edges, unique-path property
- Pitfall: same degree sequence doesn't mean isomorphic
- Interview: is this graph bipartite? — reasoning walkthrough

### Topic: Number Theory for CS (number-theory-for-cs, intermediate)
Modular arithmetic as an algebraic system, Fermat's/Euler's theorems, and why they guarantee RSA correctness — the proof-level "why," not the competitive-programming speed tricks (those live in Area 1 `math-number-theory`).
- Modular arithmetic as an algebraic system — why "clock arithmetic" is well-defined
- Divisibility, gcd, and Bézout's identity (the proof behind Euclid's algorithm)
- The fundamental theorem of arithmetic — unique prime factorization
- Fermat's little theorem — statement and a proof sketch
- Euler's totient function φ(n) and Euler's theorem (generalizing Fermat)
- Why RSA correctness follows directly from Euler's theorem (⭐ cross-link Area 13 `cryptography` for the scheme itself)
- Multiplicative inverses mod n — the gcd(a,n)=1 existence condition
- Pitfall: applying Fermat's little theorem when n isn't prime
- Interview: explain why RSA encryption and decryption are inverses — full walkthrough

### Topic: Recurrence Relations (recurrence-relations, intermediate)
Setting up and solving recurrences by substitution, recursion trees, and the characteristic-equation method (cross-link: applying Master theorem to divide-and-conquer complexity lives in Area 1 `complexity`).
- What a recurrence relation is — Fibonacci as the running example
- Solving by unrolling / substitution
- The recursion-tree method (diagram)
- Linear homogeneous recurrences — the characteristic-equation method
- Worked example: Fibonacci's closed form (Binet's formula)
- Linear non-homogeneous recurrences — particular + homogeneous solution
- Generating functions — the 60-second intuition
- Bridging recurrences to complexity: where Master theorem picks up (cross-link, not a repeat)
- Pitfall: guessing a closed form without verifying the base case
- Interview: what's the closed form of this recursive function? — walkthrough

---

## Group: Probability & Statistics (probability-stats)

### Topic: Foundations of Probability (probability-foundations, beginner)
Sample spaces, axioms of probability, conditional probability, and independence — the base vocabulary every later topic in this group depends on.
- Sample space, events, and the axioms of probability
- Conditional probability — definition and intuition (diagram: probability tree)
- Independence vs mutual exclusivity (pitfall: routinely confused)
- The multiplication rule and the chain rule for probability
- The law of total probability (diagram: partition)
- Combinatorial probability — counting-based problems (cross-link `combinatorics-counting`)
- Pitfall: the gambler's fallacy and other independence misconceptions
- Interview: classic dice/cards probability question — full walkthrough

### Topic: Bayes' Theorem & Bayesian Reasoning (bayes-theorem, intermediate)
Deriving and applying Bayes' theorem, the base-rate fallacy, and prior/likelihood/posterior framing — the single most-asked probability topic in interviews.
- Deriving Bayes' theorem from conditional probability
- Prior, likelihood, posterior — the vocabulary (diagram)
- The classic medical-test example, worked in full
- The base-rate fallacy — why intuition gets this wrong
- Bayesian updating with multiple pieces of evidence
- Naive Bayes intuition — the "naive" independence assumption (cross-link Area 12 `supervised-learning`)
- Frequentist vs Bayesian interpretation of probability (compare)
- Pitfall: confusing P(A|B) with P(B|A) — the prosecutor's fallacy
- Interview (⭐ most-asked): you test positive for a rare disease — what's the real probability?

### Topic: Random Variables & Distributions (random-variables-distributions, intermediate)
Discrete vs continuous random variables, PMF/PDF/CDF, and the handful of named distributions that actually come up in interviews.
- Random variables — discrete vs continuous (framing)
- PMF, PDF, and CDF — what each one tells you (diagram)
- Bernoulli and Binomial — coin-flip-style problems
- Poisson distribution — modeling rare events, and its link to Binomial
- Uniform distribution — discrete and continuous
- The Normal (Gaussian) distribution — why it's everywhere (CLT preview)
- Exponential distribution — modeling wait times (pitfall: memorylessness is counter-intuitive)
- Choosing the right distribution for a real scenario (compare table)
- Interview: model this real-world process — which distribution, and why?

### Topic: Expectation, Variance & Moments (expectation-variance, intermediate)
Expected value, variance, and linearity of expectation — the calculation toolkit, with linearity as the single highest-leverage interview trick.
- Expected value — definition and intuition
- Linearity of expectation — why it holds even for dependent variables (⭐ the key trick)
- Worked example: expected collisions/fixed points via linearity (classic interview problem)
- Variance and standard deviation — definition
- Var(X+Y) and the covariance term — when variances simply add
- Covariance and correlation (pitfall: correlation isn't causation)
- Law of large numbers — intuition
- Central limit theorem — why sample means look Normal (diagram)
- Interview: "expected number of X" problem solved via linearity, step by step

### Topic: Statistical Inference & Hypothesis Testing (statistical-inference, advanced)
Confidence intervals, hypothesis testing, p-values, and Type I/II errors — the toolkit behind "is this difference real" questions.
- Population vs sample; point estimation
- Confidence intervals — what "95% confidence" actually means (pitfall: the common misreading)
- Hypothesis testing framework — null vs alternative hypothesis
- p-values — what they do and don't mean (⭐ frequently misunderstood)
- Type I vs Type II error — the trade-off (compare, diagram)
- Statistical significance vs practical significance
- t-test vs z-test — when each applies
- The multiple-testing problem — why testing many hypotheses inflates false positives
- Interview: how would you tell if this change made a real difference?

### Topic: A/B Testing & Experimentation (ab-testing, advanced)
Designing a controlled experiment, sample size/power, and the classic pitfalls (peeking, novelty effect, Simpson's paradox) that turn a clean test into a wrong conclusion.
- Anatomy of an A/B test — control, treatment, randomization unit
- Choosing a metric and a minimum detectable effect
- Sample size and statistical power — why underpowered tests mislead
- The peeking problem — why checking results early inflates false positives (pitfall)
- Novelty and primacy effects — why early results can mislead
- Simpson's paradox — a segment-level reversal example (diagram)
- Interference between control and treatment (network effects)
- Reading a results dashboard — what to trust, what to question (compare)
- Interview: design an A/B test for this feature — full walkthrough

---

## Group: Linear Algebra for CS (linear-algebra)

### Topic: Vectors & Vector Spaces (vectors-vector-spaces, beginner)
Vectors as data, norms, dot product, and linear independence — the foundation for embeddings and feature vectors.
- Vectors as data — the feature-vector / embedding framing (overview)
- Vector addition and scalar multiplication — the geometric picture (diagram)
- Dot product — algebraic and geometric meaning
- Norms (L1, L2, L∞) — what each one measures (compare)
- Cosine similarity vs Euclidean distance (⭐ common interview question — when to use which)
- Linear independence — the intuition
- Basis and dimension — spanning a space
- Orthogonality and orthonormal bases
- Pitfall: geometric intuition breaks down in high dimensions (curse-of-dimensionality preview)
- Interview: cosine similarity vs dot product for a recommender — walkthrough

### Topic: Matrices & Matrix Operations (matrices-operations, beginner)
Matrix multiplication, transpose, inverse, and matrices as linear transformations — the mechanical toolkit everything else builds on.
- A matrix as a table of numbers vs a linear transformation (two views, overview)
- Matrix multiplication — mechanics and dimension rules (diagram)
- Why matrix multiplication isn't commutative — a concrete example
- Transpose and symmetric matrices
- Identity matrix and inverse — when an inverse exists
- Determinant — what it measures geometrically (area/volume scaling)
- Singular matrices — what "no inverse" means practically
- Matrices as linear transformations — a rotation/scaling example (diagram)
- Cost of matrix multiplication (cross-link Area 1 `complexity`; Strassen mention)
- Interview: multiply these matrices — what's the complexity?

### Topic: Systems of Linear Equations (linear-systems, intermediate)
Solving Ax=b, Gaussian elimination, and rank — connects straight to least squares and graphics transforms.
- Ax = b as the central problem (framing)
- Gaussian elimination — the mechanics (code/diagram)
- Row echelon form and rank
- No solution, one solution, or infinitely many — reading it off the matrix (compare, diagram)
- Overdetermined systems and least squares — the practical case
- Least squares intuition — minimizing squared error (cross-link Area 12 `supervised-learning`)
- Pitfall: ill-conditioned systems — small input changes, big output changes
- Interview: fit a line through these points — least squares walkthrough

### Topic: Eigenvalues, Eigenvectors & Diagonalization (eigenvalues-eigenvectors, advanced)
What eigenvectors mean geometrically, diagonalization, and why they power PageRank, Markov chains, and PCA — the most-tested "why do I care" linear-algebra topic.
- Eigenvectors as directions a transformation doesn't rotate (diagram)
- Eigenvalues — computing via the characteristic polynomial
- Worked example: a 2×2 matrix eigen-decomposition
- Diagonalization — when a matrix decomposes as PDP⁻¹
- Symmetric matrices — real eigenvalues, orthogonal eigenvectors, and why that matters
- Computing powers of a matrix efficiently via diagonalization
- PageRank as an eigenvector problem (⭐ classic interview tie-in, diagram)
- Markov chains and stationary distributions as eigenvectors (cross-link `probability-stats`)
- Pitfall: not every matrix is diagonalizable (repeated eigenvalues)
- Interview: why do eigenvectors matter for PCA/PageRank?

### Topic: Singular Value Decomposition & Dimensionality Reduction (svd-dimensionality-reduction, advanced)
SVD as the general matrix factorization and PCA as its headline application — the machinery behind embedding compression and recommenders (cross-link: PCA as an ML technique lives in Area 12 `unsupervised-learning`; this topic owns the factorization mechanics).
- Why SVD — factorizing any matrix, not just square ones (overview)
- The U-Σ-Vᵀ decomposition — what each factor means (diagram)
- SVD vs eigen-decomposition — how they relate
- Low-rank approximation — keeping the top-k singular values
- PCA derived from SVD — the variance-maximization intuition
- Application: recommender systems via matrix factorization
- Application: image compression via low-rank approximation
- Pitfall: dimensionality reduction can lose interpretability, not just information
- Interview: how would you compress this embedding matrix?

### Topic: Matrix Calculus for Gradients (matrix-calculus-gradients, advanced)
Gradients and Jacobians of vector/matrix functions — exactly enough to read a backprop derivation without re-deriving deep learning itself (cross-link: training mechanics live in Area 12 `deep-learning`).
- Why gradients w.r.t. vectors matter (one step beyond scalar calculus)
- The gradient of a scalar function w.r.t. a vector — shape conventions
- Common gradient identities (∇(Ax), ∇(xᵀAx)) — a cheat-sheet slide
- The Jacobian matrix — gradients of vector-valued functions
- Chain rule in matrix form — composing layers (cross-link `deep-learning` backprop)
- Worked example: gradient of squared error loss w.r.t. weights
- Pitfall: shape mismatches — the #1 debugging issue in gradient code
- Interview: derive the gradient of this loss function

---

## Group: Theory of Computation (theory-of-computation)

### Topic: Finite Automata & Regular Languages (finite-automata-regular-languages, intermediate)
DFAs, NFAs, their equivalence, and regular expressions — grounds why regex can't match balanced parentheses.
- What a formal language is — alphabets, strings, languages (framing)
- Deterministic finite automata (DFA) — states and transitions (diagram)
- Nondeterministic finite automata (NFA) — the intuition of "guessing"
- NFA-to-DFA equivalence (subset construction) — why NFAs add no power
- Regular expressions ↔ finite automata (Kleene's theorem)
- Building a DFA for a concrete pattern (code/diagram worked example)
- The pumping lemma — proving a language is NOT regular
- Pitfall: balanced parentheses isn't regular — why regex can't fully match nesting
- Regular languages in practice — lexers, input validation (cross-link Area 6 `compilers`)
- Interview: design a DFA that accepts strings matching X

### Topic: Context-Free Grammars & Pushdown Automata (context-free-grammars, intermediate)
Grammars, derivations, and pushdown automata as the machine model — the theory behind parsers.
- Context-free grammars — productions and derivations (diagram)
- Parse trees and ambiguity in grammars
- Pushdown automata — a stack-augmented finite automaton (diagram)
- CFG ↔ PDA equivalence (framing, no deep proof)
- The Chomsky hierarchy — regular ⊂ context-free ⊂ context-sensitive ⊂ recursively enumerable (compare/diagram)
- Parsing strategies at a glance — top-down vs bottom-up (cross-link Area 6 `compilers`)
- Where context-free breaks down — aⁿbⁿcⁿ-style languages
- Pitfall: assuming every language a parser needs is context-free
- Interview: is this language context-free? — reasoning walkthrough

### Topic: Turing Machines & Computability (turing-machines-computability, intermediate)
The Turing machine model, decidability, and the halting problem — the line between what's computable at all and what isn't.
- The Turing machine model — tape, head, states (diagram)
- Why Turing machines are the reference model (Church-Turing thesis)
- Decidable vs undecidable languages and problems
- The halting problem — the statement (⭐ most-cited theory result)
- Proving the halting problem undecidable — the diagonalization argument, at a walkthrough level
- Reductions — proving a new problem undecidable via the halting problem
- Real-world undecidability: why no tool perfectly detects infinite loops or dead code in general
- Pitfall: undecidable in general doesn't mean unsolvable in every practical case
- Interview: why can't we write a program that detects infinite loops in general?

### Topic: Computational Complexity: P, NP & Reductions (complexity-classes-p-np, advanced)
Complexity classes, polynomial-time reductions, and how to argue NP-completeness — the single most interview-relevant theory-of-computation topic.
- Complexity classes framing — decision problems, P vs NP (overview, diagram)
- P — problems solvable in polynomial time, with examples
- NP — verifiable in polynomial time (pitfall: NP does not mean "not polynomial")
- NP-complete vs NP-hard — the distinction (compare)
- Polynomial-time reductions — the core proof technique
- The Cook-Levin theorem — SAT is NP-complete (framing, not the full proof)
- Classic NP-complete tour: 3-SAT, vertex cover, TSP, knapsack, clique
- How to argue a problem is NP-hard in an interview — the reduction recipe (⭐)
- P vs NP — why it's unsolved and why it matters practically
- Living with NP-hardness: approximation and heuristics (cross-link Area 1 `greedy`, `dynamic-programming`)
- Interview: prove this problem is NP-complete

### Topic: Space Complexity & Advanced Complexity Classes (space-complexity-advanced-classes, advanced)
Space complexity (L, NL, PSPACE) and a light touch on randomized complexity — rounding out the complexity landscape beyond P/NP for theory-flavored interviews.
- Space complexity — measuring memory instead of time
- Classes L and NL — logarithmic space, and why it's a useful bound
- PSPACE — polynomial space, and its relationship to NP (diagram)
- Savitch's theorem — the surprising space-vs-nondeterminism result (framing only)
- Randomized complexity — BPP and probabilistic algorithms (cross-link Area 1 for concrete randomized algorithms)
- The known containments L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE — "what we actually know" (compare/diagram)
- Why so many of these containments are still open questions
- Interview: what's the difference between P, NP, and PSPACE — a crisp answer

---

## Group: Information Theory (information-theory)

### Topic: Entropy & Information Content (entropy-information-content, intermediate)
Self-information, Shannon entropy, and mutual information/KL divergence — the formal measures of uncertainty and "distance" between distributions.
- Information content of an event — why rarer events carry more information
- Shannon entropy — the formula and its intuition (diagram)
- Entropy of a fair vs biased coin — a worked example
- Joint entropy and conditional entropy
- Mutual information — how much one variable tells you about another
- Cross-entropy — defining it and how it relates to entropy (bridges to ML applications)
- KL divergence — measuring distance between distributions (pitfall: it isn't symmetric)
- Entropy as a lower bound on average code length (bridges to source coding)
- Interview: what does entropy actually measure — explain it without the formula first

### Topic: Source Coding & Data Compression (source-coding-compression, intermediate)
Huffman coding, the Kraft inequality, and lossless-compression intuition — turning entropy theory into actual bits saved.
- The source coding problem — encoding symbols in fewer average bits (framing)
- Shannon's source coding theorem — entropy as the compression limit
- Prefix codes — why "no code is a prefix of another" matters (diagram)
- Huffman coding — the greedy construction algorithm (code, cross-link Area 1 `greedy`/`heaps`)
- Huffman coding — a worked example building the tree
- The Kraft inequality — when a prefix code is achievable
- Run-length and dictionary-based compression (LZ77/LZ78 intuition) — when each wins
- Lossless vs lossy compression — where each is used (compare: text/code vs image/audio/video)
- Pitfall: compressing already-compressed or high-entropy data buys nothing
- Interview: design a compression scheme for this data

### Topic: Channel Coding & Error Detection/Correction (channel-coding-error-correction, advanced)
Noisy channels, channel capacity, and the codes actually used in practice (parity, checksums, Hamming codes) — how data survives a lossy link.
- The noisy channel model — why error correction is necessary (overview, diagram)
- Channel capacity — Shannon's noisy-channel coding theorem (intuition level)
- Parity bits — the simplest error detection, and its blind spot
- Checksums and CRC — how real systems detect corruption (cross-link Area 4 `link-layer`)
- Hamming distance — the concept underlying error correction
- Hamming codes — a single-error-correction worked example (diagram)
- Error correction vs error detection — the redundancy trade-off (compare)
- Where this shows up: RAID, network packets, QR codes, ECC memory (concrete tie-ins)
- Pitfall: more redundancy isn't free — the bandwidth/reliability trade-off
- Interview: how would you detect a corrupted message cheaply?

### Topic: Information Theory in Machine Learning (information-theory-machine-learning, advanced)
Applying entropy, cross-entropy, and KL divergence to real ML problems — loss functions, distillation, and perplexity — where classical information theory shows up in day-to-day ML interviews (cross-link: model architectures/training live in Area 12 `deep-learning`).
- Why cross-entropy loss is the natural choice for classification (derivation from likelihood, ⭐)
- Worked example: computing cross-entropy loss for a 3-class prediction
- KL divergence as "extra bits wasted" — connecting back to source coding
- KL divergence in practice: knowledge distillation (teacher-student models)
- KL divergence in VAEs — the regularization term, light touch (cross-link `deep-learning`)
- Mutual information for feature selection — picking informative features
- Perplexity in language models — entropy in disguise (⭐ common LLM-era interview question)
- Pitfall: minimizing cross-entropy vs accuracy — why they can diverge
- Interview: why use cross-entropy instead of MSE for classification?
