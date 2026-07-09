# Linux Network Troubleshooting & Essentials

Network troubleshooting in a Linux environment involves verifying connectivity, diagnosing domain name resolution (DNS), checking socket/port availability, and tracking network interfaces. These core practices allow administrators to identify bottlenecks, dead gateways, or misconfigured addresses.

---

## 🌐 1. Connectivity & Web Diagnostics

### Ping (`ping`)
Verifies basic connectivity to a remote host using ICMP echo requests. It helps confirm if a server frontend is active and reachable.
```bash
# Ping a host using IPv4
ping -4 google.com

# Flood ping a target (Requires root/sudo privileges)
sudo ping -f google.com
```

### Curl (`curl`)
An advanced utility used to test HTTP/HTTPS processes, view handshake metrics, and inspect TLS certificates.
```bash
# Fetch raw server response details and handshake data
curl -v https://google.com
```

### Web Developer Tools
If standard command-line tools show connectivity but a browser fails, right-click and use **Inspect Element -> Network Tab** to view raw console logs and HTTP response status codes.
* **2xx**: Request succeeded (e.g., `200 OK`).
* **3xx**: Redirection to a new target.
* **4xx**: Client-side errors (e.g., `404 Not Found`, `429 Rate Limited`).
* **5xx**: Server-side failures (e.g., `500 Internal Error`, `504 Gateway Timeout`).

---

## 🔍 2. Interfaces, Routing, & Paths

### Interface Status (`ip a`)
Displays all active network interface cards (NICs), loopbacks, and their currently bound IP addresses.
```bash
ip a
```

### Routing Table (`ip route`)
Maps the current active paths and determines the exact path traffic takes to reach the default gateway or external network networks.
```bash
ip route
```

### Route Tracing (`traceroute`)
Traces the continuous path of hops (routers) that packets jump through to reach a target server up to a maximum of 30 hops.
```bash
traceroute github.com
```
* *Tip:* Asterisks (`* * *`) in the response signal hidden routers or active firewalls dropping tracking packets.

---

## 📂 3. Domain Name Resolution (DNS)

### Resolution Testing Tools
Tools used to map human-readable domain names to underlying target machine IP addresses.
* **`nslookup`**: Simple DNS lookup for quick IP mappings.
* **`host`**: A simplified alternative to `nslookup`.
* **`dig`**: Detailed domain information tool showing authoritative records and configuration blocks.

```bash
nslookup google.com
host google.com
dig google.com
```

### Crucial DNS and Interface Files
* **`/etc/hosts`**: Local configuration file checked first by the system to resolve domain lookups before hitting standard nameservers.
* **`/etc/resolv.conf`**: Defines fallback nameservers for wider Internet lookups.
* **`/etc/netplan/`**: The system configuration file used by `netplan` to permanently bind static or dynamic IP address structures and upstream DNS name servers.

---

## 🔌 4. Sockets, Port Verification, & Traffic

### Telnet (`telnet`)
Verifies if a specific port (like port 80 or 443) on a remote host is active and listening for incoming connection handshakes.
```bash
telnet google.com 443
```

### Netcat (`nc`)
A flexible utility used to verify port connections, transfer files, or run port listening processes.
```bash
# Test connection viability to a specific port
nc -zv google.com 80
```

### Socket and Interface Connections (`netstat` / `ss`)
Monitors current connection sockets, listening services, and stale connections consuming system memory.
```bash
# Show listening TCP/UDP connections along with Process IDs
sudo netstat -tulnp
sudo ss -tulnp
```

### Bandwidth Monitoring via `nload`
Tracks active network interface bandwidth usage in real time, displaying independent graphs for incoming and outgoing data blocks.
```bash
# Run real-time interface monitoring
nload
```

---

## 🛠️ 5. Network Management Commands

When making structural adjustments inside your netplan network manager configurations, execute these commands to safely reload policies:

```bash
# Test a netplan configuration configuration for errors with automatic rollback
sudo netplan try

# Apply netplan network configurations permanently
sudo netplan apply

# Restart the core system network service manager
sudo systemctl restart NetworkManager
```
