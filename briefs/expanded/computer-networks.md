# Area: Computer Networks (computer-networks)

## Group: Network Fundamentals & Models (network-fundamentals)

### Topic: OSI vs TCP/IP Reference Models (layered-network-models, beginner)
Why networks are layered, the OSI 7-layer model vs the TCP/IP 4-layer model, and how to translate between them.
- Why layering: separating concerns so each layer solves one problem — *concept*
- The OSI 7 layers, one by one, with what each is responsible for — *diagram*
- The TCP/IP 4-layer model and why the real internet uses it, not OSI — *diagram*
- Mapping OSI layers onto TCP/IP layers — *compare*
- Protocol Data Units per layer: bits, frames, packets, segments, data — *concept*
- Encapsulation: an HTTP request wrapped down to bits, layer by layer — *diagram*
- De-encapsulation: unwrapping on the receiving host — *concept*
- Pitfall: treating OSI as something literally implemented rather than a mental model — *pitfall*

### Topic: Circuit, Packet Switching & Network Delay (switching-techniques-latency, beginner)
How data actually moves through a network — switching techniques and the delay components engineers reason about.
- Circuit switching: a dedicated path, the telephone network example — *concept*
- Packet switching: store-and-forward and statistical multiplexing — *concept*
- Compare: circuit vs packet switching — efficiency, latency, failure handling — *compare*
- The four delay components: propagation, transmission, queuing, processing — *concept*
- Diagram: a packet's delay breakdown hop by hop across three routers — *diagram*
- Bandwidth-delay product and why it matters for throughput — *concept*
- Pitfall: confusing bandwidth (capacity) with latency (delay) — *pitfall*

### Topic: Network Devices & Topologies (network-hardware-topologies, beginner)
What hubs, switches, routers, and gateways do at each layer, and the basic physical/logical topologies.
- Hub vs switch vs router: which OSI layer each operates at — *compare*
- How a switch learns MAC addresses and forwards frames — *concept*
- How a router forwards packets between networks — *concept*
- Common topologies: bus, star, ring, mesh, hybrid — *diagram*
- LAN vs WAN vs MAN: scope and typical technologies — *concept*
- Broadcast domain vs collision domain — what a switch changes vs a hub — *concept*
- Diagram: a home/office network with a default gateway — *diagram*
- Pitfall: confusing a "router" with any device that just forwards traffic ("gateway") — *pitfall*

### Topic: Anatomy of a Network Request — URL to Response (client-server-request-lifecycle, intermediate)
Trace one HTTP request end-to-end across every layer, tying DNS, routing, TCP, TLS, and HTTP into a single mental model.
- Overview: the six phases from typing a URL to a rendered page — *concept*
- DNS resolution: hostname to IP address — *diagram* → application-layer/dns-resolution
- Route lookup: the packet's hop-by-hop path to the server — *diagram* → routing/routing-fundamentals
- TCP three-way handshake before any data moves — *diagram* → transport-layer/tcp-connection-management
- TLS handshake establishing the encrypted channel — *diagram* → network-security/tls-handshake-deep-dive
- Sending the HTTP request and receiving the response — *concept* → application-layer/http-fundamentals
- Where a CDN edge or browser cache can short-circuit the whole chain — *concept* → network-infra/cdn-edge-caching
- Connection reuse: keep-alive and why new connections are expensive — *concept*
- Compare: a cold connection vs a warm/reused connection — timing breakdown — *compare*
- Pitfall: assuming DNS/TCP/TLS overhead is negligible — where real-world latency actually hides — *pitfall*

## Group: Physical & Data Link Layer (link-layer)

### Topic: Framing & Error Control (data-link-framing-error-control, beginner)
How the data link layer packages bits into frames and detects errors before handing data up the stack.
- Why framing: delimiting a raw bitstream into discrete units — *concept*
- Framing methods: byte counting, byte stuffing, bit stuffing — *concept*
- Error detection: parity bits, checksums, CRC — *concept*
- Diagram: a CRC division worked through on a small example — *diagram*
- Detection vs correction: why the link layer usually detects and retransmits rather than corrects — *concept*
- Flow control basics: stop-and-wait vs sliding window — *concept*
- Compare: retransmission vs forward error correction — when each wins — *compare*
- Pitfall: assuming a passing checksum means the data is correct — burst errors CRC can miss — *pitfall*

### Topic: Ethernet & MAC Addressing (ethernet-mac-addressing, beginner)
The Ethernet frame format, MAC address structure, and how shared-medium contention historically worked.
- Ethernet frame format and MTU — *diagram*
- MAC address structure: OUI plus NIC identifier, reading one — *concept*
- CSMA/CD: how legacy shared Ethernet avoided collisions — *concept*
- Why switched full-duplex Ethernet made CSMA/CD mostly obsolete — *concept*
- Unicast, broadcast, and multicast at layer 2 — *concept*
- VLAN tagging (802.1Q) and why VLANs isolate broadcast domains — *diagram*
- Compare: MAC address vs IP address — which layer, which changes hop-to-hop — *compare*
- Jumbo frames and MTU mismatches causing silent drops — *concept*
- Pitfall: assuming MAC addresses are routable across the internet — *pitfall*

### Topic: Switch Forwarding & Spanning Tree (switching-forwarding-stp, intermediate)
How switches learn and forward frames, and how Spanning Tree Protocol prevents loops in redundant topologies.
- How a switch builds its MAC address table: learning, flooding, forwarding — *concept*
- Diagram: a frame flooded then learned across three switches — *diagram*
- Why redundant links create broadcast storms and loops — *concept*
- Spanning Tree Protocol: root bridge election and blocking redundant ports — *diagram*
- STP convergence time as a real production pain point — *concept*
- RSTP and why modern data-center fabrics move away from STP — *concept*
- Compare: switch (layer 2 MAC table) vs router (layer 3 routing table) forwarding — *compare*
- Pitfall: adding a "safety" redundant cable without STP and taking down the LAN — *pitfall*

### Topic: ARP & Address Resolution (arp-address-resolution, beginner)
How a host maps an IP address to a MAC address on the local network, and the trust weakness that creates.
- Why IP-to-MAC resolution is needed at all — *concept*
- ARP request/reply walkthrough on a LAN — *diagram*
- The ARP cache: what's stored, TTL — *concept* → network-tools/diagnostic-tools-ping-traceroute
- Gratuitous ARP and its legitimate uses (failover, conflict detection) — *concept*
- ARP spoofing/poisoning: exploiting trust-by-default ARP — *concept* → network-security/common-network-attacks
- Diagram: an attacker poisoning two hosts' ARP caches to sit in the middle — *diagram*
- Defenses: static entries, dynamic ARP inspection — *concept*
- Pitfall: confusing ARP (local, layer 2/3) with DNS (global, layer 7) — both resolve names, nothing else alike — *pitfall*

## Group: IP & Addressing (ip-addressing)

### Topic: IPv4 Addressing Fundamentals (ipv4-addressing-basics, beginner)
IPv4 address structure, historical classful addressing, and public vs private ranges.
- IPv4 address format: 32 bits, dotted-decimal, binary conversion — *concept*
- Network portion vs host portion of an address — *diagram*
- Classful addressing (A/B/C) — historical context — *concept*
- Why classful addressing failed: address exhaustion — *concept*
- Private ranges (RFC 1918) vs public addresses — *concept*
- Special addresses: loopback, link-local, broadcast, 0.0.0.0 — *concept*
- Diagram: converting an IP address to binary octet by octet — *diagram*
- Pitfall: assuming an address alone tells you the network — you need the mask — *pitfall*

### Topic: Subnetting, CIDR & VLSM (subnetting-cidr-vlsm, intermediate)
The core whiteboard skill — carving a network into subnets with CIDR notation and variable-length masks.
- Why subnet: splitting one network into smaller broadcast domains — *concept*
- Subnet mask mechanics: AND-ing an address against the mask — *diagram*
- CIDR notation and what the slash number means — *concept*
- Worked example: carve a /24 into 4 equal subnets — *code*
- Finding network address, broadcast address, and usable host range from a CIDR block — *concept*
- VLSM: subnets of different sizes from one block — *concept*
- Worked example: a VLSM plan for subnets needing 100, 50, 20, and 10 hosts — *code*
- Route summarization / supernetting: combining CIDR blocks upward — *concept* → routing/routing-fundamentals
- Diagram: a VLSM tree splitting a /24 into uneven pieces — *diagram*
- Fast subnetting tricks: powers of two, the magic-number method — *concept*
- Compare: fixed-length subnetting vs VLSM — when each is used — *compare*
- Pitfall: off-by-one errors — forgetting network/broadcast addresses aren't usable hosts — *pitfall*

### Topic: IPv6 Addressing (ipv6-addressing, intermediate)
Why IPv6 exists, its address structure, and the practical differences from IPv4 interviews probe.
- Why IPv6: IPv4 exhaustion and what 128 bits buys you — *concept*
- Address format: hextets, colon-hex notation, zero compression — *concept*
- Address types: unicast, multicast, anycast — no more broadcast — *concept*
- Global unicast, link-local, and unique local addresses — *concept*
- Address autoconfiguration: SLAAC vs DHCPv6 — *concept*
- Why IPv6 reduces NAT-by-necessity — a different addressing model — *concept* → ip-addressing/nat-address-translation
- Diagram: IPv6 header vs IPv4 header — what got simpler — *diagram*
- Dual-stack and transition mechanisms (tunneling, NAT64) — *concept*
- Pitfall: assuming IPv6 adoption removes the need for IPv4 fluency in interviews — *pitfall*

### Topic: NAT & Address Translation (nat-address-translation, intermediate)
How NAT lets many private hosts share public addresses, the NAT variants, and what it breaks.
- Why NAT exists: address conservation for private networks — *concept*
- Static NAT vs dynamic NAT vs PAT (NAT overload) — *compare*
- Diagram: a PAT translation table — one public IP serving many hosts via ports — *diagram*
- Problems NAT causes: broken end-to-end connectivity, hairpinning — *concept*
- NAT traversal: why peer-to-peer/VoIP needs STUN/TURN/hole punching — *concept*
- Port forwarding: manually opening a hole in NAT — *concept*
- Compare: NAT vs a firewall — related but distinct jobs — *compare* → network-security/vpns-network-security-tools
- NAT and the shift toward IPv6 — *concept*
- Pitfall: treating NAT as a security feature rather than address translation — *pitfall*

## Group: Routing (routing)

### Topic: Routing Fundamentals & Routing Tables (routing-fundamentals, beginner)
How a router picks a next hop, what a routing table contains, and static vs dynamic routing.
- What a routing table contains: destination, next hop, metric, interface — *diagram*
- Longest prefix match: choosing among overlapping routes — *concept*
- Static vs dynamic routing — trade-offs — *compare*
- Route precedence: directly connected, static, dynamic — *concept*
- Diagram: a packet's next-hop decision walked through two routers — *diagram*
- Default routes and the "gateway of last resort" — *concept*
- Administrative distance: choosing between routing protocols — *concept*
- Pitfall: confusing routing (path selection) with switching (in-network forwarding) — *pitfall*

### Topic: Distance-Vector vs Link-State Routing (distance-vector-vs-link-state, intermediate)
The two classic intra-domain routing algorithm families, how routes are built, and their failure modes.
- Distance-vector idea: routers share their whole table with neighbors — *concept*
- RIP as a distance-vector example, hop count metric, its limits — *concept*
- Count-to-infinity and the split-horizon/poison-reverse fixes — *diagram*
- Link-state idea: every router floods link info to build a full topology map — *concept*
- Shortest-path computation over the link-state database (Dijkstra's algorithm) — *concept*
- OSPF as a link-state example: areas, faster convergence — *concept*
- Diagram: link-state flooding vs distance-vector table exchange, side by side — *diagram*
- Compare: distance-vector vs link-state — convergence speed, overhead, scalability — *compare*
- Convergence: what it means and why it matters operationally — *concept*
- Pitfall: assuming a routing protocol picks the geographically shortest path rather than its configured metric — *pitfall*

### Topic: Inter-Domain Routing & BGP Basics (interdomain-routing-bgp, advanced)
How autonomous systems exchange routes on the internet, BGP's path-vector model, and why BGP incidents happen.
- Autonomous Systems: what they are, ASNs, the internet as a network of networks — *concept*
- Intra-domain (IGP) vs inter-domain (EGP) routing — where BGP fits — *compare*
- BGP as a path-vector protocol: AS-path instead of a single metric — *concept*
- eBGP vs iBGP: peering between vs within ASes — *diagram*
- How BGP picks a best path — a simplified decision process — *concept*
- Route advertisement and propagation across the internet — *diagram*
- BGP policy: why ISPs prefer/filter routes for business reasons, not shortest path — *concept*
- Real-world BGP incidents: route hijacks and major outages — *concept* → network-security/common-network-attacks
- Compare: BGP vs OSPF — trust model, scale, metric philosophy — *compare*
- Anycast and how BGP enables it — *concept* → network-infra/cdn-edge-caching
- Pitfall: assuming internet routing is symmetric — the return path can differ — *pitfall*

## Group: Transport Layer (transport-layer)

### Topic: Transport Layer Role & Ports (transport-layer-overview-ports, beginner)
What the transport layer adds over IP, the port/socket model, and the TCP-vs-UDP choice framing.
- What transport adds over the network layer: process-to-process delivery — *concept*
- Ports: well-known, registered, and dynamic ranges — *concept*
- The socket: IP + port + protocol as a connection's identity — *diagram*
- Diagram: client ephemeral port and server well-known port forming a 4-tuple — *diagram*
- Connection-oriented vs connectionless transport — framing the TCP/UDP choice — *concept*
- Multiplexing and demultiplexing across simultaneous connections — *concept*
- Common ports interviews expect: 80, 443, 53, 22, 25 — *concept*
- Pitfall: assuming a port number implies a protocol — *pitfall*

### Topic: TCP Connection Setup & Teardown (tcp-connection-management, intermediate)
The three-way handshake, TCP's connection states, and graceful vs abrupt termination.
- The three-way handshake: SYN, SYN-ACK, ACK — *diagram*
- Sequence numbers and the initial sequence number — why randomized — *concept*
- TCP connection states: the state machine overview — *diagram*
- Four-way termination (FIN/ACK) vs an abrupt RST — *concept*
- TIME_WAIT: why it exists and how it can exhaust ports on busy servers — *concept* → network-tools/diagnostic-tools-ping-traceroute
- Half-close connections — *concept*
- Diagram: full handshake-to-teardown sequence for one HTTP request — *diagram*
- SYN flood as a handshake-level denial-of-service attack — *concept* → network-security/common-network-attacks
- Compare: graceful close (FIN) vs abrupt reset (RST) — *compare*
- Pitfall: assuming a closed connection frees resources instantly — lingering TIME_WAIT sockets — *pitfall*

### Topic: TCP Reliability & Flow Control (tcp-reliability-flow-control, intermediate)
How TCP guarantees ordered, lossless delivery and paces a fast sender against a slow receiver.
- Sequence numbers and acknowledgments: how TCP tracks delivered bytes — *concept*
- Retransmission: timeout-based vs fast retransmit on duplicate ACKs — *concept*
- Sliding window: multiple unacked segments in flight — *diagram*
- Flow control: the receive window advertised by the receiver — *concept*
- Diagram: the sliding window advancing as ACKs arrive — *diagram*
- Selective acknowledgment (SACK) vs cumulative ACK — *concept*
- Nagle's algorithm and delayed ACK — and how they can interact badly — *concept*
- Out-of-order delivery: buffering and reassembly — *concept*
- Compare: flow control (protecting the receiver) vs congestion control (protecting the network) — *compare* → transport-layer/tcp-congestion-control
- Pitfall: assuming TCP guarantees low latency — it guarantees order and reliability, not speed — *pitfall*

### Topic: TCP Congestion Control (tcp-congestion-control, advanced)
How TCP infers and reacts to network congestion — slow start, avoidance, and modern algorithms.
- Why congestion control exists: shared capacity, avoiding collapse — *concept*
- Slow start: exponential growth of the congestion window — *diagram*
- Congestion avoidance: additive increase past the slow-start threshold — *concept*
- Multiplicative decrease on loss — *concept*
- Diagram: the sawtooth congestion-window graph over time — *diagram*
- Fast retransmit and fast recovery — *concept*
- Classic Reno/Tahoe vs modern CUBIC — what changed — *compare*
- BBR: measuring bandwidth and RTT instead of reacting to loss — *concept*
- Bufferbloat: why oversized buffers make latency worse under congestion — *concept* → network-tools/packet-capture-tcpdump-wireshark
- Compare: loss-based (Reno/CUBIC) vs model-based (BBR) congestion control — *compare*
- Pitfall: confusing the congestion window (network-limited) with the receive window (receiver-limited) — *pitfall*

### Topic: UDP & Choosing TCP vs UDP (udp-and-tcp-vs-udp, beginner)
UDP's minimal connectionless model and the concrete engineering trade-off of picking it over TCP.
- The UDP header and its minimalism: no handshake, no ordering, no retransmission — *diagram*
- What "best-effort, unreliable" means in practice — *concept*
- Why some applications want unreliability: voice, video, DNS, gaming — *concept*
- Building reliability on top of UDP when you need it — *concept* → modern-protocols/quic-http3
- Compare: TCP vs UDP head-to-head — ordering, reliability, overhead, use cases — *compare*
- The UDP checksum: optional in IPv4, mandatory in IPv6 — *concept*
- Multicast/broadcast use cases that only make sense over UDP — *concept*
- Diagram: a lost UDP packet (silently gone) vs a lost TCP segment (retransmitted) — *diagram*
- Pitfall: picking UDP "for speed" without designing for loss, reordering, and duplication — *pitfall*

## Group: Application Layer (application-layer)

### Topic: DNS: Domain Name Resolution (dns-resolution, beginner)
How a hostname becomes an IP address, the DNS hierarchy, and the record types interviewers probe.
- What DNS solves: human names to machine addresses — *concept*
- The DNS hierarchy: root, TLD, authoritative servers — *diagram*
- Recursive resolver vs authoritative server — who does the work — *diagram*
- Full resolution walkthrough: browser cache to OS to resolver to root to TLD to authoritative — *diagram*
- Common record types: A, AAAA, CNAME, MX, TXT, NS — *concept*
- Iterative vs recursive queries — *concept*
- Caching and TTL: why DNS changes take time to propagate — *concept*
- DNS over UDP and when it falls back to TCP — *concept* → transport-layer/udp-and-tcp-vs-udp
- DNS-based load balancing and round-robin DNS — *concept* → network-infra/load-balancing-layers-algorithms
- DNS as an attack surface: cache poisoning and spoofing — *concept* → network-security/common-network-attacks
- Pitfall: assuming DNS changes are instant — TTL and caching layers delay propagation — *pitfall*

### Topic: HTTP Fundamentals (http-fundamentals, beginner)
HTTP's request/response model, methods, status codes, and headers — the vocabulary every other web topic assumes.
- The request/response model: what a client sends, what a server returns — *diagram*
- Anatomy of an HTTP request: method, path, headers, body — *diagram*
- Anatomy of an HTTP response: status line, headers, body — *concept*
- HTTP methods and idempotency: GET, POST, PUT, PATCH, DELETE — *compare*
- Status code families: 2xx/3xx/4xx/5xx and what each signals — *concept*
- Statelessness and why cookies/sessions exist to work around it — *concept*
- Headers that matter: Content-Type, Cache-Control, ETag, Authorization — *concept*
- HTTP/1.0 vs HTTP/1.1: persistent connections, chunked transfer — *compare*
- Diagram: a full request/response cycle over an established TCP connection — *diagram*
- Pitfall: returning 200 with an error body, or confusing 401 with 403 — *pitfall*

### Topic: HTTPS — HTTP over TLS (https-tls-in-http, intermediate)
What HTTPS adds at the application boundary, and the limits of what it actually guarantees.
- What HTTPS is: HTTP layered over a TLS-encrypted transport — *concept* → network-security/tls-handshake-deep-dive
- What HTTPS guarantees: confidentiality, integrity, server authenticity — *concept*
- What HTTPS does NOT guarantee: application trust, phishing safety — *pitfall*
- Mixed content: why loading HTTP resources on an HTTPS page gets blocked — *concept*
- HSTS: forcing HTTPS and preventing downgrade attacks — *concept*
- What a browser checks before trusting a site's certificate — *concept* → network-security/certificates-pki
- Compare: HTTP vs HTTPS overhead — and why it's now negligible — *compare*
- Pitfall: treating the padlock icon as "this site is safe" rather than "this connection is encrypted" — *pitfall*

### Topic: REST & API Design Basics (rest-api-design-basics, intermediate)
REST's constraints and conventions as commonly interviewed, distinct from full system-design API content.
- What REST means: resources, representations, a uniform interface — *concept*
- Resource-oriented URLs: nouns not verbs, nesting conventions — *concept*
- Mapping CRUD to HTTP methods correctly — *concept* → application-layer/http-fundamentals
- Statelessness in REST vs a stateful RPC session — *concept*
- Choosing the right status code for the right failure — *concept*
- Versioning approaches: URL, header, query param — *compare*
- Pagination, filtering, and sorting conventions — *concept*
- HATEOAS: what it promises and why most real APIs skip it — *concept*
- Compare: REST vs RPC-style APIs vs GraphQL, one mental model each — *compare* (see also: system-design/api-design)
- Pitfall: calling any JSON-over-HTTP API "RESTful" without resource semantics — *pitfall*

### Topic: WebSockets & Real-Time Communication (websockets-realtime, intermediate)
How a persistent full-duplex channel differs from request/response HTTP, and when to reach for it.
- The limits of request/response HTTP for real-time updates — *concept*
- Polling vs long polling vs WebSockets — the evolution — *compare*
- The WebSocket handshake: upgrading an HTTP connection — *diagram* → application-layer/http-fundamentals
- Full-duplex framing after the upgrade — *concept*
- Keeping connections alive: ping/pong frames, timeouts — *concept*
- Scaling WebSockets: sticky sessions and connection state across servers — *concept* → network-infra/load-balancing-layers-algorithms
- Server-Sent Events as a simpler one-way alternative — *compare*
- Diagram: HTTP handshake into a persistent bidirectional connection — *diagram*
- Pitfall: reaching for WebSockets when polling or SSE would be simpler and more resilient — *pitfall*

## Group: TLS & Network Security (network-security)

### Topic: The TLS Handshake (tls-handshake-deep-dive, advanced)
Exactly how a TLS session is established, key exchange mechanics, and what changed in TLS 1.3.
- What TLS provides: confidentiality, integrity, authentication — *concept* → application-layer/https-tls-in-http
- Symmetric vs asymmetric crypto — why TLS uses both — *concept*
- The TLS 1.2 handshake step by step: ClientHello to Finished — *diagram*
- Certificates and the chain of trust: CA, intermediate, leaf — *diagram* → network-security/certificates-pki
- Key exchange: RSA vs Diffie-Hellman — *concept*
- Perfect forward secrecy: why ephemeral DH matters — *concept*
- Symmetric session keys: why bulk traffic uses fast symmetric ciphers — *concept*
- TLS 1.3: the 1-RTT handshake and removed legacy ciphers — *compare*
- 0-RTT resumption and its replay-attack trade-off — *concept*
- SNI: how a server picks a certificate before decryption — *concept* → network-infra/reverse-proxies-gateways
- Diagram: TLS 1.2 vs TLS 1.3 handshake round-trip comparison — *diagram*
- Pitfall: treating handshake latency as free — why resumption and TLS 1.3 matter for performance — *pitfall*

### Topic: Certificates & Public Key Infrastructure (certificates-pki, intermediate)
How the CA trust model actually works, separate from the handshake mechanics.
- What's inside an X.509 certificate — *concept*
- Certificate Authorities and the chain of trust — *diagram*
- Root vs intermediate vs leaf certificates, and why intermediates exist — *concept*
- How a browser validates a certificate chain — *concept*
- Self-signed certificates: when they're fine, when they're a red flag — *concept*
- Certificate revocation: CRL vs OCSP — *concept*
- Certificate pinning: what it defends against — *concept*
- Pitfall: confusing "certificate expired" with "connection insecure" — different failures, different responses — *pitfall*

### Topic: Common Network Attacks (common-network-attacks, intermediate)
The attack patterns interviewers ask you to name and explain at the network/transport level.
- Man-in-the-middle: the general pattern, why encryption alone isn't enough without authentication — *diagram*
- ARP spoofing as a MITM vector — *concept* → link-layer/arp-address-resolution
- DNS spoofing and cache poisoning — *concept* → application-layer/dns-resolution
- SYN flood: exhausting half-open connections — *concept* → transport-layer/tcp-connection-management
- DoS vs DDoS: single-source vs distributed — *compare*
- Amplification/reflection attacks (DNS/NTP amplification) — *concept*
- Packet sniffing on unencrypted traffic — why HTTPS-everywhere matters — *concept*
- IP spoofing: forging source addresses — *concept*
- Diagram: a reflection/amplification attack flow — *diagram*
- Compare: where each attack sits in the stack — link, network, transport — *compare*
- Pitfall: assuming a firewall alone stops DDoS — volumetric attacks need capacity/scrubbing — *pitfall*

### Topic: VPNs & Perimeter Security Basics (vpns-network-security-tools, beginner)
How VPNs and firewalls fit into a secure network conceptually (deep firewall/zero-trust design lives in the Security area).
- What a VPN does: an encrypted tunnel over an untrusted network — *diagram*
- Site-to-site vs remote-access VPN — *concept*
- IPsec vs TLS-based VPNs, one paragraph each — *concept*
- Firewalls: packet-filtering vs stateful vs application-layer, one layer each — *concept* → network-fundamentals/network-hardware-topologies
- Diagram: a remote worker's traffic through a VPN tunnel into a corporate network — *diagram*
- Compare: VPN (encrypts a path) vs firewall (filters traffic) — *compare*
- Pitfall: treating "we have a VPN" as equivalent to "our network is secure" — *pitfall*

## Group: Modern Protocols (modern-protocols)

### Topic: HTTP/2 — Multiplexing & Binary Framing (http2-multiplexing, intermediate)
What HTTP/2 fixed about HTTP/1.1 and how it works, as the bridge to HTTP/3.
- HTTP/1.1's problem: head-of-line blocking at the application layer — *concept* → application-layer/http-fundamentals
- A binary framing layer instead of plain text — *concept*
- Multiplexed streams over one TCP connection — *diagram*
- Header compression with HPACK — *concept*
- Server push: the idea, and why it's largely deprecated in practice — *concept*
- Stream prioritization — *concept*
- Diagram: several HTTP/1.1 connections vs one multiplexed HTTP/2 connection — *diagram*
- Compare: HTTP/1.1 vs HTTP/2 — connections, blocking, overhead — *compare*
- Pitfall: HTTP/2 fixes app-layer head-of-line blocking but not transport-layer blocking — *pitfall*

### Topic: QUIC & HTTP/3 (quic-http3, advanced)
Why the web moved its transport onto UDP, and what QUIC and HTTP/3 actually change.
- The transport-layer head-of-line blocking problem TCP still has under HTTP/2 — *concept* → transport-layer/tcp-reliability-flow-control
- QUIC's core idea: reimplementing reliability and congestion control over UDP — *concept*
- Independent streams: one lost packet no longer stalls the others — *diagram*
- Built-in TLS 1.3: encryption as integral, not bolted on — *concept* → network-security/tls-handshake-deep-dive
- 0-RTT/1-RTT connection establishment — faster than TCP+TLS — *compare*
- Connection migration: surviving an IP change, e.g. Wi-Fi to cellular — *concept* → wireless/cellular-mobile-networking
- HTTP/3: HTTP semantics carried over QUIC instead of TCP — *concept*
- Diagram: TCP+TLS+HTTP/2 handshake vs QUIC+HTTP/3 handshake, round-trips compared — *diagram*
- Compare: HTTP/2 vs HTTP/3 — what changed vs what stayed the same — *compare*
- Pitfall: assuming QUIC is "just HTTP/2 on UDP" — it also changes congestion control and loss recovery — *pitfall*

## Group: Load Balancing & CDNs (network-infra)

### Topic: Load Balancing — Layers & Algorithms (load-balancing-layers-algorithms, intermediate)
L4 vs L7 load balancing and the concrete algorithms used to pick a backend.
- What a load balancer does and where it sits — *diagram*
- Layer 4 load balancing: routing on IP/port, connection-level — *concept*
- Layer 7 load balancing: routing on HTTP content (host, path, header) — *concept*
- Compare: L4 vs L7 — speed vs flexibility — *compare*
- Algorithms: round robin, weighted round robin, least connections, IP hash — *concept*
- Consistent hashing for sticky routing without a central map — *concept*
- Health checks: active vs passive detection of a dead backend — *concept*
- Diagram: an L7 load balancer routing by path prefix — *diagram*
- Session persistence and why it complicates scaling — *concept* → application-layer/websockets-realtime
- Pitfall: picking least-connections blindly when backends have unequal capacity — *pitfall*

### Topic: Reverse Proxies & API Gateways (reverse-proxies-gateways, beginner)
The reverse-proxy pattern underlying load balancers, CDNs, and API gateways alike.
- Forward proxy vs reverse proxy — who it hides, from whom — *compare*
- What a reverse proxy adds: TLS termination, compression, caching, routing — *concept*
- Diagram: client to reverse proxy to a pool of backends — *diagram*
- TLS termination at the proxy vs end-to-end encryption — *concept* → network-security/tls-handshake-deep-dive
- API gateway as a specialized reverse proxy: auth, rate limiting, routing — *concept* (see also: system-design/api-design)
- Compare: reverse proxy vs load balancer — overlapping but distinct roles — *compare*
- Pitfall: conflating a proxy with a VPN — different trust and routing purpose — *pitfall*

### Topic: CDNs & Edge Caching (cdn-edge-caching, intermediate)
How a CDN gets content physically close to users and the caching rules that keep it correct.
- Why a CDN: physical distance is latency, so replicate content at the edge — *concept*
- Diagram: origin server vs edge points of presence serving nearby users — *diagram*
- Routing a client to the nearest edge: DNS-based and anycast routing — *concept* → routing/interdomain-routing-bgp
- Cache hit vs miss at the edge, and origin pull — *concept*
- Cache-Control, ETag, and how a CDN decides what and how long to cache — *concept* → application-layer/http-fundamentals
- Cache invalidation and purging — the classic hard problem — *pitfall*
- Static vs dynamic content caching strategies — *concept*
- Compare: CDN edge caching vs application-level caching (e.g. Redis) — *compare* (see also: system-design/caching)
- Diagram: full request path with a cache hit vs a miss falling through to origin — *diagram*
- Pitfall: caching a personalized or authenticated response at a shared edge node — *pitfall*

## Group: Wireless & Mobile (wireless)

### Topic: Wi-Fi Fundamentals (802.11) (wifi-fundamentals, beginner)
How Wi-Fi shares the airwaves, and the practical model behind "why is my Wi-Fi slow."
- Wi-Fi as shared-medium wireless Ethernet — the 802.11 family — *concept*
- CSMA/CA: why wireless can't detect collisions the way wired Ethernet does — *concept* → link-layer/ethernet-mac-addressing
- Access points, BSSID/SSID, and the association process — *diagram*
- 2.4GHz vs 5GHz vs 6GHz — range, speed, and interference trade-offs — *compare*
- Channels and channel overlap/interference — *concept*
- Signal degradation: distance, walls, interference — *concept*
- WPA2 vs WPA3 security basics — *concept*
- Diagram: multiple devices contending for airtime on one access point — *diagram*
- Pitfall: assuming more signal bars means more available bandwidth — *pitfall*

### Topic: Cellular Networks & Mobile Data (cellular-mobile-networking, beginner)
The high-level architecture of cellular data networks an interviewer expects for mobile-context questions.
- Cellular architecture: cell towers and handoff between cells — *diagram*
- Generations at a glance: what changed 3G to 4G/LTE to 5G — *concept*
- Keeping a session alive across tower handoffs — *concept* → modern-protocols/quic-http3
- 5G's three pillars: enhanced speed, IoT density, low latency — *concept*
- Diagram: a handoff between two cell towers mid-session — *diagram*
- Compare: Wi-Fi vs cellular — who controls the network, typical latency and cost — *compare*
- Pitfall: assuming cellular loss/jitter behaves like a wired link — *pitfall*

## Group: Network Tools & Troubleshooting (network-tools)

### Topic: Ping, Traceroute & Basic Diagnostics (diagnostic-tools-ping-traceroute, beginner)
The first two tools reached for, what they actually measure, and how to read their output.
- Ping: ICMP echo request/reply, what round-trip time tells you — *diagram*
- Reading ping output: loss, latency, jitter — *concept*
- Traceroute: how TTL expiry reveals each hop — *diagram*
- Why traceroute hops can show timeouts or vary between runs — *concept*
- ICMP's role, and why some networks block it — *pitfall*
- MTR as ping and traceroute combined over time — *concept*
- Diagram: a five-hop traceroute annotated with per-hop latency — *diagram*
- Compare: ping vs traceroute — "is it reachable" vs "where does it break" — *compare*
- Pitfall: concluding "the network is down" from one blocked ICMP probe — *pitfall*

### Topic: Packet Capture — tcpdump & Wireshark (packet-capture-tcpdump-wireshark, intermediate)
Capturing and reading raw traffic to debug what's actually happening on the wire.
- Why capture packets: ground truth vs trusting application logs — *concept*
- tcpdump basics: interfaces and filters (host/port/protocol) — *code*
- Reading a captured TCP handshake in tcpdump output — *code* → transport-layer/tcp-connection-management
- Wireshark: following a TCP or HTTP stream visually — *concept*
- Common filter patterns for isolating one conversation — *code*
- Diagram: a capture point (client, server, or midpoint) and what it can and can't see — *diagram*
- Spotting retransmissions, resets, and duplicate ACKs in a capture — *concept* → transport-layer/tcp-reliability-flow-control
- Compare: tcpdump (scriptable CLI) vs Wireshark (deep GUI inspection) — *compare*
- Pitfall: capturing on the wrong interface or host and concluding "no traffic" — *pitfall*

### Topic: DNS & HTTP Debugging Tools (dns-http-debugging-tools, beginner)
The application-layer counterparts to ping/traceroute — dig, curl, and browser developer tools.
- dig/nslookup: querying DNS directly and reading the answer section — *code* → application-layer/dns-resolution
- Diagnosing DNS propagation with dig +trace — *code*
- curl for manual HTTP requests: headers, verbose mode, timing — *code* → application-layer/http-fundamentals
- Reading response headers to debug caching, CORS, and redirects — *concept*
- Browser DevTools Network tab: the request waterfall — *diagram*
- Diagram: a waterfall annotated with DNS, connect, TLS, TTFB, and download phases — *diagram* → network-fundamentals/client-server-request-lifecycle
- Compare: curl vs DevTools — scriptable/headless vs visual/interactive — *compare*
- Pitfall: calling an API "slow" without separating DNS, connect, TLS, and server time in the waterfall — *pitfall*

### Topic: Systematic Network Troubleshooting (network-troubleshooting-methodology, intermediate)
How to structure a "the connection is broken, find out why" investigation across every layer.
- The layered troubleshooting mental model: bottom-up, top-down, divide-and-conquer — *concept*
- A checklist from physical/link to IP to DNS to TCP to TLS to HTTP — *concept* → network-fundamentals/client-server-request-lifecycle
- Mapping common tools to each layer of the checklist — *concept*
- Diagram: a decision tree from "can't reach the site" to a root cause — *diagram*
- Distinguishing client-side, network-path, and server-side failures — *concept*
- Reading connection errors: timeout vs refused vs reset — what each implies — *pitfall*
- Intermittent vs consistent failures — different diagnostic strategies — *concept*
- Compare: "works on my machine" — the network-specific reasons this happens (DNS cache, proxy, VPN) — *compare*
- Pitfall: changing multiple variables at once while debugging and losing the signal — *pitfall*
