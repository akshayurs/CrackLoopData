# Area: Cloud, DevOps & SRE (cloud-devops-sre)

## Group: Cloud Computing Fundamentals (cloud-fundamentals)

### Topic: Cloud Service Models: IaaS, PaaS, SaaS & FaaS (cloud-service-models, beginner)
The abstraction spectrum from raw VMs to fully managed apps, and who manages what at each layer.
- The abstraction ladder: on-prem to IaaS to PaaS to SaaS to FaaS (concept)
- What "as a service" actually removes from your plate (concept)
- IaaS in practice: raw compute you provision and patch (concept)
- PaaS in practice: a managed runtime you just push code to (concept)
- SaaS in practice: consuming a finished product (concept)
- Where FaaS/serverless fits on the ladder (concept)
- The shared responsibility model: what the provider secures vs what you secure (diagram)
- Picking a model: control vs speed trade-off, worked scenario (compare)
- Pitfall: "serverless means no ops" and other layer-blurring myths (pitfall)
- Interview framing: structuring an "IaaS vs PaaS vs SaaS" answer with examples (concept)

### Topic: Regions, Availability Zones & Global Infrastructure (regions-zones-global-infra, beginner)
The physical/logical geography of a cloud provider and how it shapes latency, durability, and failure domains.
- Regions vs Availability Zones vs edge locations, defined (concept)
- Why AZs exist: independent power, network, and cooling failure domains (concept)
- Diagram: a region's AZ layout and inter-AZ links (diagram)
- Latency vs durability: same-AZ, cross-AZ, cross-region trade-offs (compare)
- Choosing a region: data residency, user latency, service availability (concept)
- Multi-AZ vs multi-region: what each actually buys you (compare)
- Worked example: placing a 3-tier app across AZs (concept)
- Pitfall: assuming multi-AZ protects against a region-wide outage (pitfall)
- How CDNs and edge locations differ from a "real" region (concept)

### Topic: Core Primitives: Compute & Storage (cloud-compute-storage-primitives, beginner)
The building-block resource types every cloud service is composed from, independent of any one provider's product names.
- Virtual machines: instance families and what vCPU-to-memory ratio tells you (concept)
- On-demand vs reserved vs spot/preemptible instances, the intuition (compare)
- Object storage vs block storage vs file storage: what each is for (compare)
- Durability vs availability: why "11 nines" and "99.99% uptime" measure different things (concept)
- Storage classes and tiering: hot, cool, cold/archive (concept)
- Worked example: picking storage for a photo-sharing app's three data types (concept)
- Pitfall: using block storage where object storage belongs, and vice versa (pitfall)
- Diagram: a request's path from VM to attached disk vs to object storage (diagram)

### Topic: Cloud Networking Primitives (cloud-networking-primitives, intermediate)
How a cloud provider's virtual network is built and secured, distinct from general TCP/IP networking theory (Area 4).
- VPC and subnets: your private slice of the cloud (concept)
- Public vs private subnets, and why NAT gateways exist (concept)
- Security groups vs network ACLs: stateful vs stateless filtering (compare)
- Diagram: packet path through a VPC with public/private subnets and a NAT gateway (diagram)
- Cloud load balancer types: L4 vs L7, internal vs internet-facing (concept)
- VPC peering vs transit gateway: connecting networks at scale (compare)
- Worked example: locking down a database subnet from the internet (concept)
- Pitfall: an overly permissive security group open on all ports (pitfall)
- Interview framing: designing the network for a 3-tier app (concept)

### Topic: Cloud-Native Design Principles (cloud-native-design-principles, intermediate)
The mindset shift needed to build software that benefits from cloud elasticity — the bridge into containers, Kubernetes, and IaC.
- What "cloud-native" means beyond the buzzword (concept)
- The 12-factor app: the parts that matter most in interviews (concept)
- Statelessness: why it enables horizontal scaling and fast recovery (concept)
- Immutable infrastructure: replace, don't patch (concept)
- Designing for failure: assume any component can die at any time (concept)
- Horizontal vs vertical scaling, revisited for cloud elasticity (compare)
- Worked example: turning a stateful monolith into a cloud-native service (concept)
- Pitfall: lifting-and-shifting a legacy app and calling it "cloud-native" (pitfall)
- How this connects to containers and orchestration (concept)

---

## Group: Containers & Docker (containers)

### Topic: Container Fundamentals: Why & How Isolation Works (container-fundamentals, beginner)
What a container actually is at the OS level, and why it is not "a lightweight VM."
- Containers vs VMs: what's shared (the kernel) vs what's virtualized (diagram)
- Linux namespaces: the isolation primitive — PID, net, mount, UTS, IPC, user (concept)
- cgroups: the resource-limiting primitive for CPU, memory, and I/O (concept)
- Union/layered filesystems: how an image becomes a running filesystem (concept)
- Putting it together: what "container" means underneath the word (concept)
- Worked example: a syscall-level view of what `docker run` actually does (code)
- Pitfall: "containers are more secure than VMs by default" (pitfall)
- Interview framing: how a container differs from a VM (concept)

### Topic: Docker Images & Layers (docker-images-layers, beginner)
The anatomy of a Docker image and how layer caching works.
- What's inside an image: layers, manifest, config (concept)
- The union filesystem: how layers stack into one view (diagram)
- Dockerfile instructions and the layer each one creates (concept)
- Build cache: why instruction order changes build speed (concept)
- Image tags vs digests: mutable pointer vs content hash (compare)
- Worked example: reading `docker history` on a real image (code)
- Pitfall: tagging everything `:latest` and losing reproducibility (pitfall)
- Image registries: the push/pull flow, public vs private (concept)

### Topic: Writing Production-Grade Dockerfiles (dockerfile-best-practices, intermediate)
The patterns that separate a hobby Dockerfile from a production one.
- Multi-stage builds: compiling in one stage, shipping a slim runtime (code)
- Minimizing image size: distroless vs alpine vs scratch trade-offs (compare)
- Ordering instructions for maximum cache reuse (concept)
- Running as a non-root user (concept)
- `.dockerignore` and why it matters for build speed and secrets (concept)
- Pinning base image versions vs floating tags (compare)
- Worked example: turning a bloated Dockerfile into a multi-stage one (code)
- Pitfall: baking secrets into image layers, where they persist after removal (pitfall)
- Health checks in the Dockerfile vs orchestrator-level checks (concept)

### Topic: Container Runtime, Networking & Storage (container-runtime-networking-storage, intermediate)
How a container gets network access and persistent data, and what runs underneath the `docker` command.
- The OCI spec: image spec vs runtime spec (concept)
- containerd and runc: what Docker actually delegates to (diagram)
- Container networking modes: bridge, host, none, and container-to-container (compare)
- How a bridge network gets containers talking to each other (concept)
- Volumes vs bind mounts vs tmpfs: persistence options compared (compare)
- Worked example: a container losing its data on restart, and the fix (concept)
- Pitfall: writing to a container's writable layer instead of a volume (pitfall)

### Topic: Multi-Container Apps with Compose (docker-compose-multi-container, intermediate)
Orchestrating a handful of related containers on one host, and recognizing when you've outgrown it.
- What docker-compose solves: defining a multi-service app as one file (concept)
- Services, networks, and volumes in a compose file (code)
- Service discovery within a compose network (concept)
- Environment-specific overrides via compose override files (concept)
- Worked example: a web + API + DB stack in one compose file (code)
- Pitfall: using Compose as a production orchestrator (pitfall)
- When you've outgrown Compose: the signals that say "you need Kubernetes" (concept)

### Topic: Container Security Basics (container-security-basics, intermediate)
The hygiene practices specific to containers, ahead of the deeper IAM/cloud security in Area 13.
- Image provenance: why base image choice is a security decision (concept)
- Vulnerability scanning in the build pipeline (concept)
- Least privilege: non-root, read-only filesystems, dropped capabilities (concept)
- Secrets at runtime vs secrets baked into images (compare)
- Signed images and supply-chain trust, briefly (concept)
- Worked example: hardening a container that runs as root by default (code)
- Pitfall: trusting an unscanned public base image in production (pitfall)

---

## Group: Kubernetes & Orchestration (kubernetes)

### Topic: Kubernetes Architecture: Control Plane & Nodes (k8s-architecture, beginner)
The components that make up a cluster and how a `kubectl apply` actually gets executed.
- The control plane: API server, etcd, scheduler, controller manager (diagram)
- Node components: kubelet, kube-proxy, container runtime (concept)
- etcd's role: the cluster's single source of truth (concept)
- The reconciliation loop: desired state vs actual state (concept)
- Following a `kubectl apply`: from CLI to running Pod, step by step (diagram)
- Controllers and the control-loop pattern, generalized (concept)
- Worked example: what happens when a node dies, from the control plane's view (concept)
- Interview framing: walking through what happens when you deploy to Kubernetes (concept)

### Topic: Pods & Workload Controllers (pods-and-workloads, beginner)
The Pod as the atomic scheduling unit, and the controllers built on top of it.
- Why Pods, not containers, are the atomic unit (concept)
- Multi-container Pods: the sidecar pattern (concept)
- Deployments and ReplicaSets: how they relate (diagram)
- StatefulSets: stable identity, ordered rollout, and when you need them (concept)
- DaemonSets: one Pod per node, and typical use cases (concept)
- Jobs and CronJobs: run-to-completion workloads (concept)
- Deployment vs StatefulSet vs DaemonSet vs Job — picking the right one (compare)
- Worked example: choosing a controller for a database, a log collector, and a nightly report (concept)
- Pitfall: running a database as a bare Deployment (pitfall)

### Topic: Services, Ingress & Cluster Networking (services-and-networking, intermediate)
How traffic finds a Pod, from inside and outside the cluster.
- The Pod IP problem: why you can't rely on Pod IPs directly (concept)
- Service types: ClusterIP, NodePort, LoadBalancer, ExternalName (compare)
- kube-proxy modes: iptables vs IPVS, briefly (concept)
- DNS-based service discovery inside the cluster (concept)
- Ingress vs Service: where each sits in the request path (diagram)
- Ingress controllers: what they actually are — a Pod running a proxy (concept)
- NetworkPolicies: default-allow, and locking down east-west traffic (concept)
- Worked example: exposing a service publicly with TLS termination at the Ingress (concept)
- Pitfall: expecting NetworkPolicies to work without a CNI that enforces them (pitfall)

### Topic: ConfigMaps & Secrets (configuration-and-secrets, beginner)
Externalizing configuration from container images, the Kubernetes-native way.
- Why config doesn't belong baked into an image (concept)
- ConfigMaps: creating and consuming them via env vars vs mounted files (code)
- Secrets: how they differ from ConfigMaps, and how they don't by default (concept)
- Mounting vs env-injecting: the live-update trade-off (compare)
- Encryption at rest for Secrets, and why base64 isn't encryption (pitfall)
- Immutable ConfigMaps/Secrets and rollout-on-change patterns (concept)
- Worked example: rotating a database credential without downtime (concept)
- Interview framing: how you manage secrets in Kubernetes (concept)

### Topic: Scheduling & Autoscaling (scheduling-and-scaling, intermediate)
How the scheduler picks a node, and how workloads grow and shrink automatically.
- Resource requests vs limits: what each actually controls (concept)
- QoS classes — Guaranteed, Burstable, BestEffort — and eviction order (concept)
- Node affinity/anti-affinity and Pod affinity/anti-affinity (concept)
- Taints and tolerations: repelling Pods from nodes (compare)
- Horizontal Pod Autoscaler: metrics, targets, scale-up/down behavior (concept)
- Vertical Pod Autoscaler vs HPA: resizing vs replicating (compare)
- Cluster Autoscaler: adding/removing nodes based on pending Pods (concept)
- Worked example: a Pod stuck Pending — diagnosing scheduler vs autoscaler (concept)
- Pitfall: setting no resource requests and getting unpredictable scheduling (pitfall)

### Topic: Storage in Kubernetes (storage-in-kubernetes, intermediate)
Persistent data in an otherwise ephemeral, Pod-churning system.
- Volumes: tied to the Pod's lifecycle, not the container's (concept)
- PersistentVolume vs PersistentVolumeClaim: the request/supply model (diagram)
- StorageClasses and dynamic provisioning (concept)
- Access modes — RWO, ROX, RWX — and what actually supports each (compare)
- Reclaim policies: Retain vs Delete, and the data-loss trap (pitfall)
- StatefulSets and storage: stable, per-replica volumes (concept)
- Worked example: resizing a PVC without losing data (concept)
- Interview framing: running a stateful database on Kubernetes (concept)

### Topic: Deployment Strategies & Zero-Downtime Rollouts (k8s-deployment-strategies, advanced)
How Kubernetes-native mechanics enable safe rollouts — the implementation layer, not general deployment-strategy theory.
- Rolling updates: maxSurge/maxUnavailable and how they shape the rollout (concept)
- Readiness vs liveness vs startup probes: what each actually gates (compare)
- Pitfall: a missing readiness probe sending traffic to a not-yet-ready Pod (pitfall)
- Blue-green in Kubernetes: swapping Service selectors (concept)
- Canary in Kubernetes: two Deployments and a weighted Service vs mesh-driven (concept)
- PodDisruptionBudgets: protecting availability during voluntary disruptions (concept)
- Rollback: how `kubectl rollout undo` actually works (concept)
- Worked example: a bad rollout caught by readiness probes before users notice (concept)

### Topic: Helm, Kustomize & Package Management (helm-and-k8s-ecosystem, intermediate)
Managing Kubernetes manifests at scale without hand-editing YAML per environment.
- The problem: raw YAML doesn't scale across environments (concept)
- Helm charts: templates, values, and releases (concept)
- Helm's templating engine, briefly, with a real example (code)
- Kustomize: overlay-based customization without templating (concept)
- Helm vs Kustomize: templating vs patching philosophy (compare)
- Chart repositories and versioning a release (concept)
- Worked example: one chart, three environments — dev/stage/prod values (code)
- Pitfall: a Helm release drifting from what's actually applied (pitfall)

### Topic: Kubernetes Troubleshooting (k8s-troubleshooting-and-debugging, advanced)
The systematic diagnosis flow for the failures that come up constantly in real clusters and in interviews.
- The diagnosis flow: describe, then logs, then events, then exec (concept)
- CrashLoopBackOff: reading the signal and the common root causes (concept)
- Pod stuck Pending: scheduler constraints vs resource shortage vs autoscaler lag (compare)
- ImagePullBackOff: registry auth, typos, and network policy causes (concept)
- OOMKilled: how limits trigger it, and how to spot it in `describe` (concept)
- Node pressure and eviction: disk and memory pressure taints (concept)
- Worked example: a service returning 503s — tracing it from Ingress to Pod (concept)
- Debugging with an ephemeral container vs shelling into a running one (concept)
- Interview framing: a Pod won't start — walking through the debugging steps (concept)

---

## Group: Infrastructure as Code (iac)

### Topic: Infrastructure as Code: Why & Core Ideas (iac-fundamentals, beginner)
The problem IaC solves and the vocabulary — declarative, idempotent, drift — shared across every IaC tool.
- The problem: click-ops doesn't scale or reproduce (concept)
- Declarative vs imperative infra definitions (compare)
- Idempotency: why running the same code twice must be safe (concept)
- Configuration drift: when reality diverges from code (concept)
- Version-controlled infra: review, history, and rollback for infra changes (concept)
- Worked example: the same VPC, clicked vs codified (concept)
- Pitfall: "IaC" that's really just scripts full of imperative API calls (pitfall)
- Interview framing: why use IaC instead of the console (concept)

### Topic: Terraform Core Workflow (terraform-core-workflow, beginner)
The init/plan/apply loop and the HCL vocabulary needed to read and write basic Terraform.
- Providers: how Terraform talks to a cloud API (concept)
- Resources vs data sources: declaring vs reading (compare)
- HCL basics: blocks, arguments, expressions (code)
- The core loop: init, then plan, then apply, then destroy (diagram)
- Reading a plan: create, update-in-place, and destroy-and-recreate symbols (concept)
- The dependency graph: how Terraform orders resource creation (concept)
- Worked example: provisioning a VM and a security group together (code)
- Pitfall: misreading "destroy and recreate" and causing unplanned downtime (pitfall)

### Topic: Terraform State Management (terraform-state-management, intermediate)
What the state file is for, why it's dangerous to hand-edit, and how teams share it safely.
- What the state file stores, and why Terraform needs it (concept)
- Local state vs remote backends, S3-and-lock-table style or Terraform Cloud (compare)
- State locking: preventing concurrent applies from corrupting state (concept)
- Diagram: a team applying through a shared remote backend with locking (diagram)
- `terraform import`: bringing existing resources under management (concept)
- Manual state surgery — `state rm`/`state mv` — when it's unavoidable (concept)
- Worked example: recovering from a state file out of sync with reality (concept)
- Pitfall: committing a local state file to git, secrets and all (pitfall)

### Topic: Terraform Modules & Multi-Environment Structure (terraform-modules-and-reuse, intermediate)
Structuring Terraform so dev, stage, and prod don't mean copy-pasted code.
- Modules: inputs, outputs, and composition (concept)
- Root modules vs reusable child modules (concept)
- Workspaces vs separate state files per environment (compare)
- Worked example: one module, three environments, different variable values (code)
- Versioning and pinning modules from a registry or git ref (concept)
- Pitfall: one giant root module for every environment, one giant blast radius (pitfall)
- Interview framing: structuring Terraform for multiple environments (concept)

### Topic: Testing IaC & Managing Drift (iac-testing-and-drift, advanced)
Guarding infra changes the way you'd guard application code — review, policy, and drift detection.
- Plan review in CI: gating applies on a human-reviewed plan (concept)
- Policy-as-code: OPA/Sentinel-style guardrails on what a plan may do (concept)
- Automated drift detection: scheduled plans that should show "no changes" (concept)
- Testing approaches: static validation vs provisioning in a real sandbox (compare)
- Worked example: a policy that blocks a plan opening a database to the internet (concept)
- Pitfall: applying from a laptop with untracked local changes (pitfall)

### Topic: IaC Tool Landscape: Terraform, CloudFormation, Pulumi, Ansible (iac-tool-landscape, intermediate)
Comparing the major IaC approaches, including the provisioning-vs-configuration-management split that trips people up.
- Provisioning vs configuration management: Terraform/CloudFormation vs Ansible/Chef/Puppet (compare)
- Terraform vs cloud-native CloudFormation/ARM/Deployment Manager (compare)
- Pulumi: general-purpose languages instead of a DSL, and the trade-off (concept)
- Ansible in an IaC pipeline: configuring what Terraform just provisioned (concept)
- Worked example: Terraform provisions the VM, Ansible configures what's on it (concept)
- Interview framing: choosing Terraform vs Ansible for a given job (concept)

---

## Group: CI/CD Pipelines (infra) (cicd-infra)

### Topic: The Deploy-Side Pipeline: Build to Release (cicd-infra-pipeline-anatomy, beginner)
The infra-facing stages of a pipeline, from a built artifact to a running environment; test-gate and branching-strategy CI theory is Area 9's `cicd`.
- Where this picks up: artifact already built and tested, now what (concept)
- Pipeline-as-code: defining stages in a file the repo owns (concept)
- Build, then containerize, then push, then deploy, as one flow (diagram)
- Artifact repositories: what they store and why immutability matters (concept)
- Environment promotion: the same artifact moving dev to staging to prod (concept)
- Worked example: one pipeline file from commit to a running staging Pod (code)
- Pitfall: rebuilding the artifact per environment instead of promoting one build (pitfall)

### Topic: Container Image Build Pipelines (container-image-build-pipelines, intermediate)
The CI-side mechanics of turning source into a trustworthy, cacheable image.
- Building images in CI: layer caching across pipeline runs (concept)
- Tagging strategy: commit SHA vs semantic version vs `latest` (compare)
- Pushing to a registry: auth, retries, and multi-arch builds (concept)
- Vulnerability scanning as a pipeline gate (concept)
- Worked example: a CI job that builds, scans, and only pushes on a clean scan (code)
- Pitfall: a slow, uncached image build that makes every pipeline run crawl (pitfall)

### Topic: Automating Deployment Strategies (deployment-strategies-automation, intermediate)
How a pipeline actually executes progressive delivery, not just the theory of blue-green or canary.
- Automating a rolling update from a pipeline step (concept)
- Progressive delivery tools: what Argo Rollouts/Flagger add over a plain rollout (concept)
- Automated canary analysis: promoting or aborting based on live metrics (concept)
- Automated rollback triggers: error-rate and latency thresholds that self-heal (concept)
- Worked example: a canary that auto-rolls-back on an error-rate spike (diagram)
- Pitfall: a canary step with no automated gate, so nobody actually watches it (pitfall)

### Topic: GitOps Fundamentals (gitops-fundamentals, intermediate)
Pull-based, git-as-source-of-truth deployment, and how it differs from a pipeline pushing changes out.
- Push-based CD vs pull-based GitOps: who initiates the change (compare)
- Git as the single source of truth for desired cluster state (concept)
- The reconciliation loop: an agent continuously converging state (diagram)
- Drift detection and self-healing: auto-reverting manual cluster changes (concept)
- Worked example: a merged PR flowing to a running change with no separate deploy step (concept)
- Pitfall: giving the pipeline cluster-admin credentials instead of using a pull agent (pitfall)
- Interview framing: what GitOps is and how it differs from a CI/CD pipeline (concept)

### Topic: Secrets & Config in Pipelines (secrets-and-config-in-pipelines, intermediate)
Keeping credentials and per-environment config out of pipeline code while still deploying automatically.
- Why secrets in pipeline YAML or env files are a recurring breach cause (concept)
- Secrets managers integrated into a pipeline (concept)
- Short-lived, scoped credentials vs long-lived pipeline secrets (compare)
- Config promotion across environments without copy-pasting values (concept)
- Worked example: a pipeline fetching a short-lived token instead of a stored secret (code)
- Pitfall: a secret leaked in build logs because it was echoed for "debugging" (pitfall)

### Topic: Release Orchestration Across Many Services (release-orchestration-multi-service, advanced)
Coordinating deploys once you have more than a handful of independently-deployed services.
- The problem: N services, each with its own pipeline, needing a coherent release (concept)
- Dependency ordering: deploying a schema change before the service that needs it (concept)
- Feature-flag-gated infra rollouts: decoupling deploy from release (concept)
- Blast radius control: staged rollout by percentage, region, or tenant (concept)
- Worked example: a backwards-incompatible API change rolled out safely across services (concept)
- Pitfall: a "deploy everything at once" release that cascades into an outage (pitfall)

---

## Group: Observability & Monitoring (observability-ops)

### Topic: Observability Fundamentals (observability-fundamentals, beginner)
The ops-implementation view of observability — building and running the stack; the HLD-level framing for a design answer is Area 7's `observability`.
- Monitoring vs observability: knowing something's wrong vs asking why (concept)
- The three pillars: metrics, logs, traces (concept)
- Why the pillars alone aren't enough — correlation is the real value (concept)
- Diagram: one request's data footprint across all three pillars (diagram)
- Instrumentation: where metrics, logs, and traces actually get emitted from (concept)
- Worked example: using all three pillars together to find one bug (concept)
- Pitfall: dashboards for everything, but no way to answer "why" (pitfall)

### Topic: Metrics & Time-Series Data (metrics-and-time-series, intermediate)
What makes a metric useful, and the data model underneath tools like Prometheus.
- Counters, gauges, and histograms: what each measures (compare)
- The Prometheus data model: metric name plus labels, briefly (concept)
- Push vs pull metric collection: the trade-offs (compare)
- Cardinality: why an unbounded label value can take down your monitoring (pitfall)
- Aggregation and percentiles: why averages hide the pain — p50/p95/p99 (concept)
- Worked example: a p50 that looks fine while p99 is on fire (concept)
- Interview framing: why p99 latency matters, not just the average (concept)

### Topic: Logging Pipelines at Scale (logging-pipelines, intermediate)
How logs get from a running process to a searchable, affordable store.
- Structured logging vs free-text logs (compare)
- The pipeline: agent, then buffer/queue, then processing, then storage, then query (diagram)
- Log levels and when each is appropriate (concept)
- Sampling and filtering: you can't keep everything at scale (concept)
- The cost of logs: cardinality and volume drive the bill (concept)
- Worked example: tracing one request across services using a correlation ID in logs (concept)
- Pitfall: logging PII or secrets by accident (pitfall)

### Topic: Distributed Tracing (distributed-tracing, intermediate)
The span/trace model and how context survives a hop across services.
- Trace, span, and parent-child relationships (concept)
- Context propagation: how a trace ID survives a network hop (concept)
- Diagram: a trace waterfall across four services showing where time went (diagram)
- Sampling strategies: head-based vs tail-based (compare)
- Instrumentation: automatic agent-based vs manual code-level spans (concept)
- Worked example: finding the slow downstream call in a waterfall view (concept)
- Pitfall: 100% sampling in production drowning the tracing backend (pitfall)

### Topic: Dashboards That Actually Get Used (dashboards-and-visualization, beginner)
Designing dashboards people check during an incident, not vanity walls.
- The RED method — Rate, Errors, Duration — for request-driven services (concept)
- The USE method — Utilization, Saturation, Errors — for resources (concept)
- RED vs USE: when each framework fits (compare)
- Designing for the 3am on-call reader, not the exec review (concept)
- Worked example: a service dashboard built around RED (code)
- Pitfall: a dashboard with 40 panels and no clear "is it broken" signal (pitfall)

### Topic: Alerting Design (alerting-design, intermediate)
Writing alerts that page the right person for the right reason — the bridge into SRE's on-call practice.
- Symptom-based vs cause-based alerting: alert on what users feel (compare)
- Actionable alerts: every page should have a next step (concept)
- Alert fatigue: how too many low-value pages erode response quality (concept)
- Paging vs ticket vs chat: matching urgency to channel (concept)
- Runbooks: linking an alert to the steps that resolve it (concept)
- Worked example: rewriting a noisy CPU-threshold alert into a symptom-based one (concept)
- Interview framing: what makes a good alert (concept)

---

## Group: Site Reliability Engineering (sre)

### Topic: SRE Fundamentals (sre-fundamentals, beginner)
What SRE actually is as a discipline, and how it differs from traditional ops and from "DevOps" as a buzzword.
- SRE's original framing: what happens when a software engineer runs production (concept)
- SRE vs traditional sysadmin ops: engineering the fix vs manually applying it (compare)
- SRE vs DevOps: overlapping but not the same thing (compare)
- Toil, defined: manual, repetitive, automatable, no lasting value (concept)
- Why reducing toil is the core SRE lever (concept)
- Worked example: a manual restart-the-service runbook turned into self-healing (concept)
- Interview framing: what SRE is and how it differs from DevOps (concept)

### Topic: SLIs, SLOs & SLAs (sli-slo-sla, intermediate)
The measurement hierarchy that makes "reliable" a number instead of a feeling.
- SLI: the metric that represents user-perceived health (concept)
- Choosing a good SLI: user-facing, measurable, meaningful (concept)
- SLO: the internal target built on an SLI (concept)
- SLA: the external, often contractual promise, and why it's usually looser than the SLO (compare)
- Diagram: SLI feeds SLO feeds SLA, with the safety margin between them (diagram)
- Worked example: defining an SLI/SLO for a checkout API (concept)
- Pitfall: setting an SLO of 100%, which is impossible and kills your ability to ship (pitfall)
- Interview framing: walking through defining an SLO for a service (concept)

### Topic: Error Budgets (error-budgets, intermediate)
Turning an SLO into a spendable budget that governs release velocity.
- Error budget: 100% minus the SLO, as a spendable allowance (concept)
- Burn rate: how fast you're consuming the budget, and why speed matters more than the raw number (concept)
- Fast-burn vs slow-burn alerts on the same budget (compare)
- Error budget policy: what happens when the budget's exhausted (concept)
- The velocity vs reliability tension the budget is designed to resolve (concept)
- Worked example: a team freezing feature launches after a bad week burns the budget (concept)
- Pitfall: tracking the budget but having no policy for when it's gone (pitfall)

### Topic: On-Call & Incident Response (on-call-and-incident-response, intermediate)
The operational process and roles for handling an active incident, plus the blameless postmortem that follows; general debugging technique is Area 9's `debugging`.
- On-call rotation design: primary/secondary, follow-the-sun, escalation paths (concept)
- Severity levels: what SEV1 vs SEV2 actually changes about the response (compare)
- The incident commander role: coordinating without doing the fixing yourself (concept)
- Communication during an incident: status page, internal channel, stakeholder updates (concept)
- Diagram: an incident's timeline from page to resolution to postmortem (diagram)
- Blameless postmortems: why "blameless" is a mechanism, not just a nice idea (concept)
- Writing a postmortem: timeline, impact, root cause(s), action items (concept)
- Worked example: a postmortem action item that actually prevents recurrence vs one that doesn't (compare)
- Pitfall: a postmortem that ends at "human error" instead of the systemic cause (pitfall)

### Topic: Redundancy & Failover Patterns (redundancy-and-failover-patterns, advanced)
Infra-level high-availability design — multi-AZ/region, failover automation, graceful degradation; app-level circuit breakers and retries are Area 7's `resilience`.
- Active-active vs active-passive: what each costs and what each buys (compare)
- Multi-AZ vs multi-region failover, and the RTO/RPO each realistically achieves (concept)
- DR tiers: backup-restore, pilot light, warm standby, multi-site (compare)
- Health-check-driven failover: how the system decides "this is down" (concept)
- DNS failover: what it's good at, and its inherent lag from propagation and caching (pitfall)
- Graceful degradation: shedding non-critical features before failing completely (concept)
- Worked example: designing failover for a payment service with a 5-minute RTO (concept)
- Interview framing: designing a system for 99.99% availability (concept)

### Topic: Toil Reduction & Automation (toil-and-automation, intermediate)
Turning the "reduce toil" principle into a concrete, ongoing practice.
- Identifying toil: manual, repetitive, automatable, tactical, no enduring value (concept)
- The automation ladder: manual, then documented runbook, then scripted, then self-service, then eliminated (diagram)
- Google's roughly-50% rule: capping ops work so engineering time survives (concept)
- Worked example: a recurring "restart and clear cache" ticket automated away (concept)
- Measuring toil: is it actually going down over time (concept)
- Pitfall: automating a bad process instead of fixing or removing it first (pitfall)

### Topic: Chaos Engineering (chaos-engineering, advanced)
Deliberately injecting failure to verify reliability assumptions before an incident does it for you.
- The core idea: build confidence by breaking things on purpose (concept)
- Steady-state hypothesis: what "normal" looks like before you break anything (concept)
- Blast radius control: starting small, in staging, with an abort switch (concept)
- Common fault injections: kill a Pod, add latency, drop a dependency (concept)
- Game days: scheduled, team-wide chaos exercises (concept)
- Worked example: a chaos test that reveals a missing retry/timeout (concept)
- Pitfall: running chaos experiments in production with no rollback plan (pitfall)
- Interview framing: what chaos engineering is and why you'd do it (concept)

---

## Group: API Gateways & Service Mesh (api-gateway-mesh)

### Topic: API Gateway Fundamentals (api-gateway-fundamentals, beginner)
What a gateway does at the edge of your system, distinct from a plain load balancer.
- What an API gateway does: routing, auth termination, rate limiting, transformation (concept)
- Gateway vs plain load balancer: one more layer of "what," not just "where" (compare)
- North-south traffic: the gateway's job is at the system's edge (concept)
- Common products, conceptually: Kong/NGINX/cloud-managed gateways (concept)
- Diagram: a request's path through a gateway to a backend service (diagram)
- Worked example: a gateway centralizing auth so backend services don't each reimplement it (concept)
- Pitfall: putting business logic in the gateway layer (pitfall)
- Interview framing: what a gateway does that a load balancer doesn't (concept)

### Topic: Service Mesh Fundamentals (service-mesh-fundamentals, intermediate)
Why east-west traffic between services gets its own infrastructure layer.
- East-west traffic: the problem a mesh solves that a gateway doesn't (concept)
- The sidecar pattern: a proxy next to every service instance (concept)
- Data plane vs control plane: proxies that move traffic vs the brain that configures them (diagram)
- What a mesh buys you without app code changes: mTLS, retries, observability, traffic control (concept)
- Mesh vs handling the same concerns in a shared library (compare)
- Worked example: adding mTLS between 20 services without touching their code (concept)
- Pitfall: adopting a mesh for 3 services that didn't need one (pitfall)

### Topic: Envoy & Sidecar Proxy Mechanics (envoy-and-proxy-mechanics, intermediate)
What the proxy in "sidecar proxy" is actually doing, using Envoy as the reference implementation.
- Envoy's role: the proxy most meshes are built on (concept)
- Listeners, routes, and clusters: Envoy's core configuration model (concept)
- How traffic actually gets redirected into the sidecar via iptables or eBPF (diagram)
- xDS: how Envoy gets its configuration dynamically from a control plane (concept)
- Worked example: tracing a request through a sidecar's listener, route, and cluster (concept)
- Pitfall: forgetting the sidecar adds a real latency hop, not a free one (pitfall)

### Topic: Istio Traffic Management (istio-traffic-management, advanced)
Configuring mesh-driven traffic behavior — the mechanics behind mesh-based canary and testing.
- VirtualService: routing rules independent of the underlying deployments (concept)
- DestinationRule: subsets and load-balancing policy per subset (concept)
- Traffic splitting for canary releases: mesh-driven vs manual Kubernetes Service weighting (compare)
- Fault injection: testing timeouts and retries by injecting delay or errors deliberately (concept)
- Worked example: shifting 5% of traffic to a new version and watching error rate (diagram)
- Pitfall: a VirtualService/DestinationRule mismatch silently routing traffic wrong (pitfall)

### Topic: mTLS & Zero-Trust Networking in a Mesh (mtls-and-zero-trust-networking, advanced)
How a mesh enforces service identity and encryption at the infra layer; broader authn/zero-trust theory is Area 13's security track.
- Zero-trust in one line: never trust the network, always verify the caller (concept)
- mTLS: both sides prove identity, not just the server (concept)
- Service identity: how a mesh assigns and verifies who is calling (concept)
- Diagram: a mesh-enforced mTLS handshake between two sidecars (diagram)
- Permissive vs strict mTLS modes during migration (compare)
- Worked example: locking down a mesh from permissive to strict without an outage (concept)
- Pitfall: assuming mTLS alone means authorization is handled too (pitfall)

### Topic: Gateway vs Mesh: Making the Call (gateway-vs-mesh-decision, intermediate)
The decision framework interviewers actually probe — when you need one, the other, or both.
- North-south (gateway) vs east-west (mesh): the traffic-direction framing (concept)
- Team size and service count: the threshold where a mesh starts paying for itself (concept)
- Using both together: gateway at the edge, mesh internally (diagram)
- What each layer solves that the other structurally can't (compare)
- Worked example: a 5-service startup (gateway only) vs a 200-service org (gateway plus mesh) (concept)
- Interview framing: structuring a "would you recommend a service mesh here" answer (concept)

---

## Group: Cost & Capacity Engineering (cost-capacity)

### Topic: Cloud Cost Fundamentals (cloud-cost-fundamentals, beginner)
The pricing vocabulary and visibility practices every cost conversation starts from.
- Pricing models: on-demand, reserved/committed use, spot/preemptible, savings plans (compare)
- Why cloud bills spike: idle resources, data egress, over-provisioning (concept)
- Cost visibility: tagging resources so spend maps to a team or product (concept)
- Showback vs chargeback: making cost visible vs making it billed (compare)
- Worked example: reading a cost breakdown and spotting the dominant line item (concept)
- Pitfall: no tagging strategy, so nobody can explain the bill (pitfall)
- Interview framing: investigating a sudden cloud cost spike (concept)

### Topic: Rightsizing & Waste Reduction (rightsizing-and-waste-reduction, intermediate)
Matching provisioned resources to actual usage, and finding the waste that accumulates by default.
- Rightsizing compute: matching instance type to actual CPU/memory usage (concept)
- Rightsizing storage: tiering cold data instead of leaving it on hot storage (concept)
- Idle and orphaned resources: unattached disks, idle load balancers, forgotten snapshots (concept)
- Choosing instance types by workload shape — CPU-bound, memory-bound, I/O-bound (compare)
- Worked example: a rightsizing pass that cuts fleet cost with no performance loss (concept)
- Pitfall: rightsizing once and never revisiting as traffic patterns change (pitfall)

### Topic: Autoscaling Economics (autoscaling-economics, intermediate)
The cost side of scaling decisions, distinct from the mechanics covered in the Kubernetes group.
- The trade-off autoscaling manages: headroom cost vs the risk of underprovisioning (concept)
- Reactive vs predictive autoscaling: scaling on current load vs forecasted load (compare)
- Scale-to-zero: when it saves real money and when cold starts make it a bad trade (concept)
- Spot/preemptible strategies: diversifying instance types to reduce interruption impact (concept)
- Worked example: a workload split across on-demand baseline plus spot burst capacity (concept)
- Pitfall: autoscaling on a laggy metric, so scale-up always arrives late (pitfall)

### Topic: Capacity Planning (capacity-planning, intermediate)
Forecasting demand and deciding how much headroom to carry — where cost and reliability trade off explicitly.
- Forecasting demand: trend, seasonality, and known future events (concept)
- Headroom strategy: how much spare capacity is "enough" (concept)
- Load testing to find the actual breaking point, not the assumed one (concept)
- The cost-reliability trade-off, made concrete with an error-budget lens (concept)
- Worked example: capacity planning for a predictable, Black-Friday-style traffic spike (concept)
- Pitfall: planning capacity from average load instead of peak (pitfall)

---

## Group: Serverless & Edge (serverless)

### Topic: Serverless & FaaS Fundamentals (serverless-fundamentals, beginner)
What "serverless" actually means and the event-driven execution model underneath it.
- Serverless, defined: servers still exist, you just don't manage them (concept)
- FaaS: functions as the unit of deployment and billing (concept)
- Event-driven execution: a function runs in response to a trigger, not a running process (concept)
- Pay-per-invocation: how billing differs from an always-on VM (concept)
- Statelessness requirement: why a function can't rely on local memory between calls (concept)
- Worked example: an image-resize function triggered by a file upload (concept)
- Pitfall: "serverless means no infrastructure to think about" (pitfall)
- Interview framing: what serverless actually means (concept)

### Topic: The FaaS Execution Model: Cold Starts & Concurrency (faas-execution-model, intermediate)
The mechanics that make serverless performance characteristics different from a warm server.
- Cold start vs warm start: what actually happens during each (diagram)
- Why cold starts happen: init phase, runtime choice, package/dependency size (concept)
- What shrinks a cold start: smaller packages, lighter runtimes, provisioned concurrency (concept)
- Concurrency model: how many invocations run in parallel, and the limits (concept)
- Execution time limits and why long-running work doesn't fit FaaS (concept)
- Worked example: comparing cold-start latency across two runtime choices (compare)
- Pitfall: benchmarking only warm invocations and missing the cold-start tail (pitfall)

### Topic: Serverless Architecture Patterns (serverless-architecture-patterns, intermediate)
How real serverless systems are composed from triggers and functions.
- Event sources: HTTP, queue, schedule, and storage triggers (concept)
- Function composition: chaining functions vs a step-function-style orchestrator (compare)
- Fan-out/fan-in patterns: one event triggering many parallel functions (diagram)
- Synchronous vs asynchronous invocation, and what changes about error handling (compare)
- Worked example: an order pipeline as a chain of triggered functions (diagram)
- Pitfall: a deep synchronous function-calling-function chain that's slow and fragile (pitfall)

### Topic: State & Storage in a Stateless World (serverless-state-and-storage, intermediate)
Where data actually lives when the compute layer can't remember anything between invocations.
- Statelessness in practice: nothing survives reliably between invocations (concept)
- Where state moves instead: managed databases, caches, object storage (concept)
- The connection pooling problem: many concurrent functions vs a fixed DB connection limit (pitfall)
- Patterns that help: connection poolers/proxies, serverless-native databases (concept)
- Worked example: a function fleet exhausting a relational database's connection limit under load (concept)
- Interview framing: what breaks when a serverless fleet sits in front of a relational database at scale (concept)

### Topic: Serverless Trade-offs: When Not to Use It (serverless-tradeoffs-and-pitfalls, advanced)
The honest cost, latency, and lock-in trade-offs that decide whether serverless fits a given workload.
- The cost crossover: cheap at low/spiky volume, expensive at steady high volume (compare)
- Long-running or steady high-throughput workloads: where containers/VMs win (concept)
- Vendor lock-in: how tightly a FaaS platform couples you to one provider's ecosystem (concept)
- Observability challenges: debugging a system with no long-lived process to attach to (concept)
- Worked example: modeling the cost crossover point for a steady-traffic service (concept)
- Pitfall: choosing serverless for a workload that never idles, and paying more than a VM would (pitfall)
- Interview framing: when you would NOT use serverless (concept)

### Topic: Edge Computing Fundamentals (edge-computing-fundamentals, intermediate)
Pushing compute to the network edge, and how it differs from a CDN or a regular cloud region.
- Edge vs cloud region vs CDN: three different things people conflate (compare)
- Edge functions/workers: the constrained runtime model at the edge (concept)
- Why edge wins on latency: physical proximity to the user (diagram)
- What edge compute is constrained at: execution time, memory, limited APIs (concept)
- Common use cases: personalization, A/B testing, auth checks, request rewriting at the edge (concept)
- Worked example: moving an auth check from origin to the edge to cut latency (concept)
- Pitfall: putting stateful, heavy logic at the edge where it doesn't belong (pitfall)

---

## Notes: overlaps deliberately resolved (not duplicated)

- **`observability-ops` (this area) vs `observability` (Area 7).** This area owns the ops-implementation view — instrumenting, running Prometheus/Grafana-style stacks, alert design. Area 7 owns the HLD-answer framing (what to mention when observability comes up inside a system design interview). No topic here re-teaches SLI/SLO theory from scratch (owned by `sre` group's `sli-slo-sla`).
- **`cicd-infra` (this area) vs `cicd` (Area 9).** Area 9 owns test-gate/branching-strategy/feature-flag CI theory as a general engineering practice. This area's group owns the deploy-side infra mechanics: containerizing, pushing, GitOps, release orchestration across services. Cross-linked explicitly in `cicd-infra-pipeline-anatomy` and `release-orchestration-multi-service`.
- **`api-gateway-mesh` (this area) vs `microservices`/`api-design`/`resilience` (Area 7).** Area 7 covers decomposition, sagas, API contract design, and resilience patterns (circuit breaker, retries) conceptually. This area's group covers the infra mechanics that implement mesh/gateway behavior (Envoy, Istio CRDs, mTLS). `gateway-vs-mesh-decision` is the explicit decision-framework bridge.
- **`redundancy-and-failover-patterns` (`sre`) vs `resilience` (Area 7).** This topic is infra-level HA (multi-AZ/region, DNS/health-check failover, DR tiers); Area 7's `resilience` is app-level (rate limiters, circuit breakers, retries).
- **`on-call-and-incident-response` (`sre`) vs `debugging` (Area 9).** Area 9 owns the general skill of systematic debugging; this topic owns the operational process (rotations, severities, incident commander, postmortem mechanics).
- **`autoscaling-economics`/`capacity-planning` (`cost-capacity`) vs scheduling/HPA mechanics (`kubernetes`).** The Kubernetes group teaches how HPA/Cluster Autoscaler work; this group teaches the cost/forecasting decisions layered on top — mechanics vs economics, not a repeat.
- **No gaps identified** against the group's stated scope (IaaS/PaaS/SaaS, containers, K8s, IaC, CI/CD, observability, SRE, gateway/mesh, cost, serverless) — all ten groups from the map are covered with no group skipped or merged.
