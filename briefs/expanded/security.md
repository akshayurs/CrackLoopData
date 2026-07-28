# Area: Security (security)

Reference outline — 2 levels below the group (Topics + slide headings) for human review and approval.
Groups are taken exactly from `briefs/area-group-map.md` § Area 13 — Security, same names and slugs, same order.
Slide headings are the real pages a Topic will contain (concept / diagram / code / compare / pitfall), matching
schema v3 (`area → group → topic → slide`). MCQs and Interview Questions are separate topic-level arrays and are
intentionally **not** listed here — this outline covers Topics (L2) and the slide outline (L3) only.

---

## Group: Security Fundamentals (`security-fundamentals`)
*Scope (area-group-map): CIA triad, threat modeling, defense-in-depth.*

### Topic: CIA Triad & Security Goals (`cia-triad`, beginner)
The confidentiality/integrity/availability model as the shared vocabulary for reasoning about any security decision, plus the accountability ideas that sit alongside it.
- What "security" protects: assets, not just secrets
- Confidentiality: encryption, access control, least privilege
- Integrity: hashing, checksums, tamper detection
- Availability: redundancy, graceful degradation, DoS resistance
- The CIA trade-off: more logging helps integrity but can hurt confidentiality
- Non-repudiation and accountability: the ideas CIA leaves out
- Diagram — CIA triad mapped to concrete controls on a real system
- Pitfall — treating "security" as synonymous with "encrypt everything"

### Topic: Security Design Principles (`security-design-principles`, beginner)
The classic engineering principles (Saltzer & Schroeder–style) that make a system's design inherently harder to get wrong, independent of any specific control.
- Kerckhoffs's principle: assume the algorithm/design is public
- Why "security through obscurity" fails as a sole control
- Economy of mechanism: simplicity as a security property
- Complete mediation: check every access, every time — no cached "yes"
- Fail-safe defaults baked into the design, not bolted on
- Separation of privilege and duty
- Psychological acceptability: security people won't route around
- Pitfall — confusing "nobody knows how it works" with "it's secure"

### Topic: Social Engineering & the Human Factor (`social-engineering`, beginner)
Attacks that target people rather than systems, and why security awareness is itself a control.
- Why humans are the most-targeted layer of any security stack
- Phishing: the anatomy of a convincing email
- Spear phishing and whaling: targeted variants
- Vishing and smishing: phone- and SMS-based social engineering
- Pretexting and impersonation
- Business email compromise: social engineering with a wire transfer at the end
- Diagram — a phishing attack chain from email to credential theft to account takeover
- Compare — technical controls (MFA, allowlists) vs awareness training — why you need both
- Pitfall — assuming technical staff are immune to social engineering

### Topic: Defense in Depth & Security Architecture (`defense-in-depth`, intermediate)
Layering independent controls so no single failure is catastrophic, plus the design defaults that make layers effective.
- The layered-castle model: why one control is never enough
- Least privilege and need-to-know as default posture
- Fail-secure vs fail-open: choosing the safe default on error
- Security by design vs bolted-on security
- Attack surface reduction: turning off what you don't need
- Compare — perimeter security vs defense-in-depth vs zero trust (full zero trust in Network & Infra Security)
- Diagram — layered controls wrapping a sensitive asset
- Pitfall — a single control treated as "the whole defense" (one firewall, one WAF rule)

### Topic: Threat Modeling (`threat-modeling`, intermediate)
Structured methods for finding a system's weaknesses before an attacker does, and scoring which ones matter.
- Why you threat model before (not after) you build
- Data flow diagrams and trust boundaries
- STRIDE: the six threat categories
- Attack trees: decomposing an attacker's goal into paths
- Risk scoring: likelihood × impact
- Compare — STRIDE vs DREAD vs PASTA
- Worked example — threat-modeling a login flow end to end
- Diagram — a DFD with trust boundaries for a web app
- Pitfall — threat-modeling once at launch and never revisiting

### Topic: Risk, Vulnerabilities & Security Frameworks (`risk-frameworks`, intermediate)
The precise vocabulary and the frameworks an engineer is expected to recognize, at interview depth rather than compliance depth.
- Vulnerability vs threat vs risk vs exploit — precise definitions
- CVSS: how a vulnerability gets a severity score
- NIST Cybersecurity Framework at a glance: identify/protect/detect/respond/recover
- Where compliance (SOC2, ISO 27001, PCI-DSS) fits vs engineering security work
- Security as a continuous process, not a one-time project
- Compare — a high-CVSS bug with no real exposure vs a medium-CVSS bug that's trivially exploitable
- Pitfall — chasing a CVSS number instead of actual exploitability in context

---

## Group: Cryptography (`cryptography`)
*Scope (area-group-map): symmetric/asymmetric, hashing, signatures.*

### Topic: Cryptography Foundations (`crypto-foundations`, beginner)
The vocabulary and guarantees of cryptography, and the ground rule that governs every other topic in this group.
- What cryptography actually promises — and what it doesn't ("unbreakable" is not a property)
- Plaintext, ciphertext, key, algorithm: the vocabulary
- Compare — symmetric vs asymmetric at a glance (full depth in their own topics)
- Key length and brute-force resistance: why AES-128 is "enough"
- Kerckhoffs's principle in practice: security lives in the key, not the algorithm's secrecy
- Diagram — the general encrypt/decrypt pipeline
- Pitfall — inventing a "custom" or proprietary encryption scheme

### Topic: Hashing & Message Integrity (`hashing-integrity`, beginner)
What makes a hash function cryptographically useful, where hashing is (and isn't) the right tool, and HMAC for authenticated integrity.
- The three properties of a cryptographic hash: pre-image, second pre-image, collision resistance
- Why MD5 and SHA-1 are considered broken today
- Hashing for integrity: checksums and file verification
- HMAC: keyed hashing for authenticated messages
- Hashing vs encryption — the confusion interviewers love to probe
- Diagram — HMAC construction (key + message → tag)
- Compare — general-purpose hashing (SHA-256) vs password hashing (bcrypt/argon2) — different jobs (full treatment in Authentication & Authorization)
- Pitfall — assuming a hash can be "decrypted" back to the input

### Topic: Symmetric Encryption (`symmetric-encryption`, intermediate)
Block and stream ciphers, AES at a conceptual level, and the modes of operation that determine whether an encryption scheme actually holds up.
- Block ciphers vs stream ciphers
- AES at a glance: block size, key sizes, rounds (conceptual, not bit-level)
- Modes of operation: why the mode matters as much as the cipher
- ECB mode: why identical plaintext blocks leak a pattern
- CBC mode: chaining, IVs, and the padding-oracle risk
- CTR mode: turning a block cipher into a stream cipher
- GCM: authenticated encryption in a single pass
- Diagram — the "ECB penguin": visual proof that ECB leaks structure
- Compare — ECB vs CBC vs CTR vs GCM: when to use which
- Pitfall — reusing an IV/nonce with the same key

### Topic: Asymmetric (Public-Key) Cryptography (`asymmetric-encryption`, intermediate)
Public/private key pairs, the two dominant algorithm families, and why real systems combine asymmetric with symmetric crypto.
- Public/private key pairs: the mental model, made rigorous
- RSA at a glance: a trapdoor function built on factoring
- Elliptic curve cryptography: same guarantee, much smaller keys
- Why asymmetric operations are computationally expensive
- Hybrid encryption: use asymmetric crypto only to exchange a symmetric key
- Diagram — hybrid encryption flow (this is how TLS and PGP actually work)
- Compare — RSA vs ECC: key size, performance, adoption
- Pitfall — encrypting a large payload directly with RSA instead of hybrid encryption

### Topic: Digital Signatures & PKI (`signatures-pki`, advanced)
Signing and verifying with key pairs, and the certificate infrastructure that binds a public key to a real-world identity.
- Digital signatures: sign with the private key, verify with the public key
- What a signature actually proves: integrity + authenticity + non-repudiation
- Certificates: binding a public key to an identity
- Certificate Authorities and the chain of trust
- X.509 fields an engineer should recognize
- Certificate validation: expiry, revocation (CRL vs OCSP)
- Diagram — a certificate chain from leaf certificate to root CA
- Compare — CA-signed vs self-signed certificates: what you gain and lose
- Pitfall — disabling certificate validation to silence an error

### Topic: Key Management & Key Exchange (`key-management`, advanced)
The operational lifecycle of cryptographic keys and the protocol that lets two parties agree on a secret over a public channel.
- The key lifecycle: generation, distribution, rotation, revocation, destruction
- Where keys should live: HSMs and KMS vs environment variables (full treatment in Cloud Security)
- Diffie-Hellman key exchange: agreeing on a secret in plain sight
- Forward secrecy: why today's compromised key shouldn't decrypt yesterday's traffic
- Diagram — a Diffie-Hellman exchange step by step
- Compare — rotating a symmetric key vs rotating an asymmetric key pair — why one is harder
- Pitfall — a hardcoded key or secret committed to source control

---

## Group: Application Security (`appsec`)
*Scope (area-group-map): OWASP Top 10, injection, XSS/CSRF.*

### Topic: OWASP Top 10 Overview (`owasp-top-10`, beginner)
What the OWASP Top 10 is, how it's compiled, and how to use it as a floor for review — the map the rest of this group fills in.
- What the OWASP Top 10 is and how it's compiled (real incident data, not opinion)
- The current categories at a glance: access control, crypto failures, injection, and the rest
- Diagram — OWASP categories mapped onto a request's lifecycle (client → network → app → data)
- Compare — OWASP Top 10 as a floor vs a complete security program
- How this group and Authentication & Authorization split the categories between them
- Pitfall — treating "not in the Top 10" as "safe"

### Topic: Security Misconfiguration & Logging Failures (`security-misconfig-logging`, beginner)
The failures that come from defaults and visibility rather than a specific exploit.
- Security misconfiguration: default credentials, verbose stack traces, open admin panels
- The "disable what you don't use" principle
- Logging and monitoring failures: what good security logging looks like
- What must never be logged: passwords, tokens, full card numbers, PII
- Diagram — a misconfigured stack (debug mode on, defaults unchanged) as an attack surface map
- Compare — enough logging to detect abuse vs logging that becomes a liability
- Pitfall — logging a password or token "temporarily, for debugging"

### Topic: Injection Attacks (`injection-attacks`, intermediate)
How untrusted input becomes executed code or commands across SQL, OS commands, and NoSQL — and the one fix that actually closes the class.
- What injection is: untrusted data treated as code
- SQL injection: the classic `' OR '1'='1` example
- Blind SQL injection: extracting data with no visible output
- Command injection: shelling out with user-controlled input
- NoSQL injection: the operator-injection variant
- Code — a vulnerable string-built query next to its parameterized fix
- Diagram — an injection attack path from input field to database
- Compare — parameterized queries vs escaping vs blocklists
- Pitfall — "sanitizing" input with ad hoc string replacement

### Topic: Cross-Site Scripting (XSS) (`xss`, intermediate)
The three XSS variants, why they happen, and encoding/CSP as the two real defenses — the server-side and conceptual half of XSS (browser-specific mechanics live in Web & Frontend).
- What XSS is: injected script running in someone else's browser session
- Reflected XSS
- Stored XSS
- DOM-based XSS
- Output encoding by context: HTML body vs attribute vs JavaScript vs URL
- Content Security Policy as a defense-in-depth layer (frontend mechanics in Web & Frontend)
- Code — a template that escapes output vs one that doesn't
- Diagram — a stored-XSS attack chain: attacker → stored comment → victim's browser
- Compare — stored vs reflected vs DOM-based — where the payload lives
- Pitfall — relying on a blocklist of "dangerous" characters

### Topic: CSRF & Request Forgery (`csrf`, intermediate)
How ambient cookie authority lets one site forge requests to another on a victim's behalf, and the token/attribute defenses that close it.
- What CSRF is: tricking a browser into sending a request it's already authenticated for
- Why cookies alone are "ambient authority" — no proof of intent
- The synchronizer token pattern
- The double-submit cookie pattern
- The SameSite cookie attribute as a modern mitigation
- Diagram — a CSRF attack: malicious page triggers a request using the victim's session
- Compare — CSRF vs XSS: different problem, often confused
- Pitfall — assuming HTTPS alone prevents CSRF

### Topic: Broken Access Control (`broken-access-control`, intermediate)
The application-layer bugs that let one user reach another's data or functions — the OWASP #1 category, distinct from the authorization *design* patterns in Authentication & Authorization.
- Why broken access control tops the OWASP list
- IDOR: Insecure Direct Object Reference (`/orders/1234` → `/orders/1235`)
- Missing function-level authorization: hidden admin routes that aren't actually protected
- Horizontal vs vertical privilege escalation
- Why a client-side check is not an access control
- Code — adding the missing server-side ownership check
- Diagram — an IDOR request walking through a system with no ownership check
- Pitfall — hiding a feature in the UI and calling it "access controlled"

### Topic: Insecure Deserialization & SSRF (`deserialization-ssrf`, advanced)
Two "trusting the input's shape" failure classes: deserialization gadget chains leading to code execution, and SSRF tricking a server into requesting internal resources.
- Why deserialization can escalate straight to remote code execution
- Gadget chains: the classic Java/Python pickle-style example
- Safer alternatives: schema-validated formats with strict parsing
- Server-Side Request Forgery: making the server fetch what the attacker wants
- Diagram — SSRF reaching a cloud metadata endpoint (cross-link Cloud Security IAM)
- Compare — deserialization risk vs plain JSON parsing risk
- Pitfall — deserializing untrusted data with a general-purpose/"native" deserializer

---

## Group: Authentication & Authorization (`authn-authz`)
*Scope (area-group-map): OAuth2/OIDC, JWT, sessions, RBAC.*

### Topic: Authentication Fundamentals (`authn-fundamentals`, beginner)
The factor model behind every login mechanism, and why combining factors (MFA) changes the security guarantee qualitatively, not just additively.
- Authentication vs authorization — the distinction interviewers always check first
- The three factors: something you know, have, are
- Why MFA stops most credential-stuffing attacks
- TOTP: how a 6-digit code rotates every 30 seconds
- Passwordless approaches: magic links and WebAuthn/passkeys at a glance
- Diagram — an MFA login flow: password + second factor
- Compare — SMS OTP vs authenticator app vs hardware key: why they're not equally strong
- Pitfall — treating "has a password" as "is securely authenticated"

### Topic: Sessions & Cookies (`sessions-cookies`, beginner)
How server-side session auth actually works end to end, and the cookie attributes that determine whether a session can be stolen.
- How session-based auth works: session ID plus server-side store
- Cookie attributes: HttpOnly, Secure, SameSite — what each one actually blocks
- Session fixation vs session hijacking
- Session expiry, idle timeout, and invalidation on logout
- Where sessions live at scale: sticky sessions vs a shared store
- Diagram — the cookie round-trip between browser and server
- Pitfall — storing sensitive data directly and unsigned in a cookie

### Topic: Password Storage & Credential Security (`password-storage`, intermediate)
How passwords should be stored so a database breach doesn't hand over usable credentials, and the runtime defenses against guessing attacks.
- Why plaintext and reversibly-encrypted password storage are both wrong
- Salting: defeating precomputed rainbow tables
- Why bcrypt/scrypt/argon2 beat SHA-256 for passwords: deliberately slow, memory-hard
- Peppering: an extra server-side secret beyond the salt
- Credential stuffing and brute force: why rate limiting and lockout matter
- Code — hashing and verifying a password with bcrypt
- Compare — bcrypt vs scrypt vs argon2
- Pitfall — rolling a custom password-hashing scheme

### Topic: Token-Based Auth & JWT (`jwt-tokens`, intermediate)
The structure and trade-offs of JSON Web Tokens as a stateless alternative to server-side sessions, including the revocation problem that trade-off creates.
- JWT structure: header, payload, signature
- Signing (JWS) vs encrypting (JWE) a token
- Stateless auth: why JWT skips the server-side session lookup
- Access tokens vs refresh tokens
- The revocation problem: you can't "delete" a stateless token early
- Where to store a JWT client-side, and why localStorage is risky
- Diagram — a JWT-based request flow from login to an authenticated API call
- Compare — session cookies vs JWT: real trade-offs, not "JWT is strictly better"
- Pitfall — accepting `alg: none` or skipping signature verification

### Topic: Authorization Models: RBAC, ABAC & Beyond (`authorization-models`, intermediate)
The major patterns for deciding who can do what, and when a role-based model stops being granular enough.
- Authorization models overview: the problem each one solves
- RBAC: roles as a bundle of permissions
- ABAC: attribute-based rules (time, location, resource sensitivity)
- ACLs: per-resource permission lists
- Relationship/policy-based authorization at a glance (Zanzibar-style, for breadth)
- Diagram — an RBAC role–permission–user mapping
- Compare — RBAC vs ABAC: when roles alone aren't granular enough
- Pitfall — role explosion: a role per user defeats the point of RBAC

### Topic: OAuth 2.0 (`oauth2`, advanced)
The delegated-authorization problem OAuth solves, its four roles, and the authorization-code-plus-PKCE flow that is the modern default.
- The problem OAuth solves: delegated access without sharing a password
- The four roles: resource owner, client, authorization server, resource server
- The Authorization Code grant, step by step
- PKCE: why even public clients need it now
- Scopes: limiting exactly what a token can do
- Why the implicit and password grants are now deprecated
- Diagram — the full authorization-code-plus-PKCE flow
- Pitfall — a public client storing a client secret

### Topic: OpenID Connect & SSO (`oidc-sso`, advanced)
The identity layer OIDC adds on top of OAuth2, and how single sign-on lets one login serve many applications.
- OAuth2 is authorization, not authentication — why OIDC exists
- ID token vs access token: different purpose, different audience
- The `/userinfo` endpoint and standard claims
- Single sign-on: one login, many applications
- SAML at a glance: the enterprise SSO context you'll still meet
- Diagram — an OIDC login handing back an ID token alongside an access token
- Compare — OIDC vs SAML: modern web vs enterprise identity
- Pitfall — using an OAuth2 access token to "authenticate" a user

---

## Group: Network & Infra Security (`netsec`)
*Scope (area-group-map): firewalls, TLS, zero-trust.*

### Topic: Firewalls & Network Segmentation (`firewalls-segmentation`, beginner)
What a firewall actually filters, and how segmentation limits how far an attacker can move after one host is compromised.
- What a firewall filters: packets, ports, protocols, connection state
- Stateless vs stateful packet filtering
- Next-gen firewalls: application-aware filtering
- Network segmentation and VLANs: limiting blast radius
- The DMZ pattern: isolating public-facing services from the internal network
- Diagram — a DMZ network layout
- Pitfall — treating the firewall as the only control (see Defense in Depth)

### Topic: VPNs & Secure Remote Access (`vpn-remote-access`, beginner)
How traditional VPNs grant network-level trust, and why that model is being displaced by zero trust.
- What a VPN actually does: an encrypted tunnel plus network membership
- Site-to-site vs remote-access VPN
- IPSec vs SSL/TLS VPN
- The VPN trust problem: once connected, broad network access
- Diagram — a remote-access VPN tunnel into a corporate network
- Pitfall — treating "connected to VPN" as "trusted device"

### Topic: TLS in Practice (`tls-in-practice`, intermediate)
What TLS guarantees and how it's actually deployed in a security architecture — cipher suite policy, pinning, and mutual TLS (the handshake byte-by-byte lives in Computer Networks).
- What TLS guarantees: confidentiality, integrity, and server (optionally client) authentication
- TLS versions: why 1.0/1.1 are deprecated and what 1.3 improved
- Cipher suites: what gets negotiated (handshake mechanics live in Computer Networks)
- Certificate pinning: trusting a specific cert/key, not any valid CA
- Mutual TLS (mTLS): both sides present certificates
- Diagram — mTLS between two internal services
- Compare — TLS terminated at the load balancer vs end-to-end TLS
- Pitfall — disabling certificate validation to silence an error

### Topic: Intrusion Detection, Prevention & DDoS Defense (`ids-ips-ddos`, intermediate)
Detecting and blocking active attacks on the network, from single-host intrusions to volumetric floods.
- IDS vs IPS: detect-and-alert vs detect-and-block
- Signature-based vs anomaly-based detection
- DDoS attack types: volumetric, protocol, application-layer (L7)
- DDoS mitigation: scrubbing centers, rate limiting, anycast
- Diagram — DDoS traffic routed through a scrubbing center
- Compare — network-layer DDoS defenses vs application-layer (L7) defenses
- Pitfall — mistaking an IDS alert for an actual blocked attack

### Topic: Zero Trust Architecture (`zero-trust`, advanced)
The "never trust, always verify" model that replaces network location with continuous, per-request identity and posture checks.
- The perimeter model's core assumption — and why insider threats and lateral movement break it
- Zero trust principles: never trust always verify, least privilege, assume breach
- Identity-aware access: verifying user, device, and context per request
- Microsegmentation: shrinking blast radius to a single workload
- Continuous verification vs a one-time login
- Diagram — a zero-trust access decision: identity + device posture + policy engine
- Compare — perimeter/VPN model vs zero trust
- Pitfall — calling a product "zero trust" without changing the underlying trust model

---

## Group: Cloud Security (`cloud-security`)
*Scope (area-group-map): IAM, secrets, shared responsibility.*

### Topic: Shared Responsibility Model (`shared-responsibility`, beginner)
Where the cloud provider's security obligation ends and the customer's begins, and how that line moves across service models.
- The shared responsibility model: "security of the cloud" vs "security in the cloud"
- How the responsibility line shifts across IaaS, PaaS, and SaaS
- Common customer-side failures mistakenly blamed on "the cloud"
- Diagram — the responsibility split drawn across IaaS/PaaS/SaaS
- Compare — an IaaS VM breach vs a SaaS misconfiguration: whose failure is it
- Pitfall — assuming the provider secures your data by default

### Topic: Cloud IAM (`cloud-iam`, intermediate)
How cloud platforms model identity and permissions, and the workload-identity patterns that avoid long-lived credentials.
- Cloud IAM building blocks: identities, roles, policies
- Policy evaluation logic: allow/deny, and why explicit deny wins
- Roles vs users: why workloads should assume roles, not hold long-lived keys
- Service accounts and instance roles: how a VM or function gets permissions
- Cross-account access patterns
- Diagram — a service assuming a role to reach another resource
- Pitfall — attaching a wildcard admin policy "to unblock" development

### Topic: Secrets Management (`secrets-management`, intermediate)
Where secrets should live instead of source code or config files, and how rotation limits the damage when one leaks anyway.
- Why secrets don't belong in source code, checked-in config, or container images
- Secrets managers and vaults: centralized, access-controlled retrieval
- Static long-lived secrets vs short-lived/dynamic secrets
- Injecting secrets at runtime instead of build time
- Diagram — an app fetching a secret from a vault at startup
- Compare — rotation on a schedule vs rotation on suspected compromise
- Pitfall — rotating a leaked secret without revoking the old one (or leaving that gap the other way round)

### Topic: Cloud Network & Data Security (`cloud-network-data-security`, intermediate)
The network isolation and encryption controls specific to a cloud environment, and matching control strength to data sensitivity.
- Security groups vs NACLs: stateful instance-level vs stateless subnet-level
- VPC isolation and private subnets
- Encryption at rest: provider-managed vs customer-managed keys
- Encryption in transit inside the cloud, not just at the edge
- Data classification: knowing what needs the strongest controls
- Diagram — a VPC with public and private subnets behind security groups
- Pitfall — a security group open to `0.0.0.0/0` on a database port

### Topic: Container & Kubernetes Security (`container-k8s-security`, advanced)
The security concerns layered on top of container and Kubernetes mechanics — image trust, runtime hardening, and cluster-level access control (operational mechanics live in Cloud, DevOps & SRE).
- Image security: scanning for known CVEs, minimal base images
- Running containers as non-root with a read-only filesystem
- Kubernetes RBAC: service accounts, roles, role bindings
- Network policies: default-deny between pods
- Why a base64 Kubernetes Secret is not encryption
- Diagram — a namespace with a network-policy boundary around it
- Pitfall — mounting the Docker socket into a container (a container-breakout path)

---

## Group: Secure Coding (`secure-coding`)
*Scope (area-group-map): input validation, safe defaults.*

### Topic: Input Validation & Sanitization (`input-validation`, beginner)
The discipline of validating untrusted input at every trust boundary, and why allowlisting beats blocklisting as a default technique.
- Validate at every trust boundary, not just the UI
- Allowlist (positive) validation vs blocklist (negative) validation
- Type, length, format, and range checks
- Validation vs sanitization vs encoding — three different jobs, often confused
- Client-side validation is UX, not security
- Code — allowlist validation for a username field
- Pitfall — validating once at the API gateway and trusting it everywhere downstream

### Topic: Error Handling & Information Leakage (`error-handling-leakage`, beginner)
How error messages and timing behavior can hand an attacker a map of the system, and what a safe error response looks like instead.
- Why detailed error messages help an attacker map your system
- Stack traces and debug pages left on in production
- Generic user-facing errors vs detailed internal logs
- Timing attacks: when "how long it took" leaks information
- Diagram — a safe error response next to a leaky one, side by side
- Pitfall — returning a full stack trace in an API's JSON error body

### Topic: Secure Defaults & Fail-Safe Design (`secure-defaults`, intermediate)
Designing APIs and configuration so the safest option is also the default one, and deciding what a failed security check should do.
- Secure by default: the safest option should require the least effort
- Fail-safe vs fail-open: what should happen when a check itself errors
- Opt-out security features are a smell — security should be opt-in to disable
- Why "batteries-included" framework defaults remove whole vulnerability classes
- Diagram — a fail-open vs fail-closed branch inside an authorization check
- Pitfall — a try/catch around a permission check that defaults to "allow" on error

### Topic: Dependency & Supply Chain Hygiene (`dependency-hygiene`, intermediate)
Treating the dependency tree as part of the attack surface, from lockfiles to automated vulnerability scanning in CI.
- Your dependency tree is part of your attack surface
- Lockfiles and pinned versions: reproducibility as a security property
- Automated vulnerability scanning (SCA) in CI
- Evaluating a new dependency before adding it: maintenance, popularity, permissions
- Diagram — a vulnerable dependency three levels deep in the tree
- Compare — a known-CVE direct dependency vs the same CVE in a transitive one
- Pitfall — force-updating every dependency right before a release

### Topic: Secure Code Review (`secure-code-review`, intermediate)
The security-specific lens a reviewer adds on top of a normal code review, focused on catching missing checks rather than style.
- What a security-focused review adds beyond a normal code review
- Checklist: authorization on new endpoints, input validation, secrets, error handling
- Spotting a missing authorization check in a diff
- When a change needs a threat-model note vs when that's overkill
- Diagram — a PR diff with a highlighted missing-authz-check line
- Pitfall — reviewing only the changed lines and missing that a new path bypasses an old check

### Topic: Security Testing: SAST, DAST & Fuzzing (`security-testing`, advanced)
The automated techniques for finding vulnerabilities before an attacker does, and where each fits in a CI/CD pipeline.
- SAST: scanning source code for known-bad patterns
- DAST: attacking a running instance like a black box
- Fuzzing: throwing malformed or random input to find crashes
- Where each technique fits in the CI/CD pipeline
- Penetration testing vs automated scanning — different guarantees
- Diagram — SAST/DAST/fuzzing mapped onto CI/CD pipeline stages
- Pitfall — treating a clean SAST scan as proof the code is secure

---

## Cross-Area & Cross-Group Notes

- **`netsec` (A13) vs `network-security` (A4, Computer Networks):** A4 owns TLS handshake mechanics and the general attack survey; A13's `tls-in-practice` owns the security-architecture usage (cipher-suite policy, pinning, mTLS) plus firewalls/VPN/zero-trust/IDS-IPS/DDoS, which A4 doesn't cover. Cross-linked inline in `tls-in-practice`.
- **`xss` (A13, `appsec`) vs `web-security` (A14, Web & Frontend):** A13 owns vulnerability mechanics + server-side/conceptual defenses (encoding, CSP as a concept); A14 owns browser/JS-specific mechanics (CSP header wiring, SOP, DOM APIs). Cross-linked inline.
- **`broken-access-control` (`appsec`) vs `authorization-models` (`authn-authz`):** deliberately split as bug-class (what goes wrong in application code) vs design pattern (how authorization is modeled). No content overlap; each references the other's home group.
- **`hashing-integrity` (`cryptography`) vs `password-storage` (`authn-authz`):** generic hash properties/HMAC live in Cryptography; password-specific slow-hash algorithms (bcrypt/scrypt/argon2) live in Authn & Authz. Cross-linked inline both directions.
- **`container-k8s-security` (`cloud-security`) vs `kubernetes` (A10, Cloud/DevOps/SRE):** A10 owns operational mechanics (pods/deployments/scheduling); A13 owns the security lens (RBAC, network policy, image scanning, breakout risks). Cross-linked inline.
- **Gaps intentionally left out:** privacy law/compliance depth (GDPR/CCPA specifics) — out of engineering-interview value filter beyond the one-line mention in `risk-frameworks`; wireless/Wi-Fi security — homed in A4's `Wireless & Mobile` group, not duplicated here.
