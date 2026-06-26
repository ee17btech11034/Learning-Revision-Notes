# Linux Networking Fundamentals Notes

### Core Networking Concepts
* **IP Address Definitions**: Machines use `IPv4` (4 octets -> a.b.c.d) or `IPv6` to identify and communicate with other nodes over the internet. `IPv6` was introduced to handle the eventual exhaustion of public `IPv4` addresses.
* **MAC Address**: Unique hardware address embedded in a Network Interface Card (NIC).
* **Default Gateway**: The routing node used to send network traffic outside of the local subnet.
* **Loopback Address**: Localhost address (`127.0.0.1`) common to all computers.
* **CIDR (Classless Inter-Domain Routing)**: Format representing an IP address and its associated network prefix (e.g., `/24` means the first 24 bits define the network portion and the remaining 8 bits define individual hosts).

```text
10.0.0.0 -> 10.255.255.255 (range for a network)
10.211.55.12/24 ('/24' means first 24 bits are used for network address, remaining 8 bits for Host Address)

converted in binary:
10  -> 00001010 ( 8 bits each)
211 -> 11010011
55  -> 00110111
12  -> 00001100

'/24' is the subnet mask means 
10.211.55.0   -> will be the network address
10.211.55.1 -- 10.211.55.254   -> can be used in machines
10.211.55.255   -> will be the broadcast address

```

* **NAT (Network Address Translation)**: Translates local private IP addresses to public IPs for outbound traffic. If traffic is going from private network to public network then it requires NAT to translate private addresses to public address.

### Predefined Private IP Ranges
* `10.0.0.0/8 range(10.0.0.0  -- 10.255.255.255)`
* `172.16.0.0/12 range(172.16.0.0  -- 172.31.255.255)`
* `192.168.0.0/16 range(192.168.0.0  -- 192.168.255.255)`

---

### Core Protocols
* **DNS (Domain Name System)**: Resolves human-readable domain names into IP addresses. Follows a structural hierarchy starting from root (`.`), going to Top-Level Domains (`.com`, `.org`), down to domains and subdomains.

```text
Assume We have a machine 10.0.0.27 and trying to connect `www.google.com`. 
Steps
- 1. First our machine will check the 'local DNS' ('/etc/hosts' and '/etc/resolve.conf` file) for entry for google IP address '8.8.4.4'.
- 2. If not resolved, then it check the DNS server of Internet Provider (router). It has 'Top Level Domain (TLD)' table like or may be in Graph table 
 | TLD | Domain name | Domain Address |
 | com | google.com  | 8.8.4.4 |
 | com | facebook.com | a.b.c.d |
 | org | bharatpetrolium | a.b.c.d |
 | in | xyz | a.b.c.d |
 | gov | xyz | a.b.c.d |
 | edu | xyz | a.b.c.d |
 Google can also have multiple sub services like mail.google.com, doc.google.com, drive.google.com and each can be hosted on different IPs. 
 DNS resolve this and provide the IP.
```

* **DHCP (Dynamic Host Configuration Protocol)**: Dynamically assigns IP configurations to clients, involving a 4-step allocation process: Discover, Offer, Request, and Acknowledge (DORA).
* **TCP (Transmission Control Protocol)**: A connection-oriented protocol that establishes a reliable communication session using a three-way handshake (`SYN` -> `SYN-ACK` -> `ACK`).
'SYN' -> Sending a signal packet 'SYN' to server
'SYN-ACK' -> Server send 'Acknowledge with SYN (it got)' to client
'ACK' -> Client send this top server that it acknowledged it.

---

### Linux Networking Commands Cheat Sheet

#### Interface Configuration & Status
```bash
# View active IP addresses and interface configurations in CIDR format
ip addr show

# Alternative legacy syntax to list active interfaces (Requires net-tools)
ifconfig

# Show device connection status handled via NetworkManager
nmcli device status

# Set a network interface state to active or inactive
sudo ip link set dev <interface_name> up/down

# Provision a temporary virtual secondary IP configuration
sudo ifconfig <interface_name>:1 <ip_address> netmask <subnet_mask> up

# Commit configurations modified inside netplan YAML configuration directories
sudo netplan apply
```

#### Diagnostic & Routing Checks
```bash
# Display the kernel routing tables and current default gateway exits
ip route

# Send ICMP echo requests indefinitely to check connectivity
ping google.com

# Restrict ICMP tracking to exactly 4 packet transfers
ping -c 4 8.8.8.8
```

#### Port Auditing & Open Connections
```bash
# Check all current listening TCP ports
ss -tuln

# Trace the packet delivery path across various routers (hops) to a destination
traceroute ubuntu.com

# Live interface inspection showing real-time network loss and latency statistics
mtr google.com

# Print statistics summaries for all active socket types
ss -s
```

#### Name Resolution & Protocol Inspection
```bash
# Fetch domain records, queries, and IP addresses via DNS
dig ubuntu.com

# Retrieve a short structural summary of domain name records
nslookup ubuntu.com

# Fast single-line resolution of standard network hostnames
host google.com
```

#### Traffic Capture & Low-Level Audits
```bash
# Actively monitor raw TCP packets traversing a specific interface
sudo tcpdump -i <interface_name> tcp

# Verify remote target port availability (e.g., test if port 80 is reachable)
nc -zv <ip_address> 80

# Fetch target webpage body outputs and diagnostic HTTP transaction headers 
curl -v http://localhost:8080
```

---

### Key Local Networking Files
* `/etc/hosts`: Static table lookup file for system hostname configurations.
* `/etc/resolv.conf`: Contains definitions specifying targeted system nameservers.
* `/etc/netplan/*.yaml`: Configuration scripts managed by Ubuntu's netplan system.
* `/var/lib/dhcp/dhclient.leases`: Local file documenting active DHCP address leases.

---

### Common Well-Known Network Ports
* **FTP**: `21` / `22`
* **SSH**: `22`
* **DNS**: `53`
* **HTTP**: `80`
* **HTTPS**: `443`
* **MySQL**: `3306`


### Netmask (Subnet Mask) Architecture
* **Purpose**: A 32-bit masking sequence used to divide an IP address into its corresponding Network ID and Host ID components.
* **Mechanism**: Binary `1`s designate the immutable network prefix, while binary `0`s indicate the range of dynamic addresses available for local host allocation.
* **CIDR Equivalence**: Shorthand notation (e.g., `/24`) corresponds exactly to a physical netmask representation (e.g., `255.255.255.0`).
* **Broadcast Bounds**: The very first address in a masked block identifies the network wire itself, while the absolute last address serves as the local subnet broadcast lane.

### DNS Resolution Order & Local Configs
* **Resolution Pipeline**: When a lookup is triggered, Linux queries local static mapping files before sending outbound requests to external upstream nameservers.
* `/etc/resolv.conf`: The active runtime configuration file containing system nameserver records used to resolve external host domains.
* `systemd-resolved`: The modern default background stub listener daemon on modern distributions that dynamically intercepts, caches, and forwards standard system DNS queries.

### Additional DNS Query Commands
```bash
# Query a specific DNS server directly, bypassing the system local cache
dig @8.8.8.8 ubuntu.com

# Request only the short, absolute IP address string answer for a domain
dig +short ubuntu.com

# Trace the entire recursive resolution journey from root servers downward
dig ubuntu.com +trace
```

### More commands:
```bash
ip a (provide  ip addresses (2) of physical cards like enp0s5, )

nmcli device status (Only connected network address with ip configuration, like Ethernet)

ping google.com ( ICMp packet transfer to get the response from server; it wil continously run until we interupt )

ping -c 4 8.8.8.8 (ping for 4 time request send)


dig ubuntu.com (command to check DNS)(each service has multiple ip address for always available and in each region)

nslookup ubuntu.com ( only tells IPs for ubuntu, not detailed as 'dig')
nslookup 34.107.243.93 ( to do reverse search)

ip route (route to connect to any server)

sudo ifconfig enp0s5:1 10.0.0.50 netmask 255.0.0.0 up (creating virtual interface 'enp0s5:1' () for enp0s5:1 (ip 10.0.0.50))

sudo ip link set enp0s5 down (will set it as DOWN, check output)
sudo ip link set enp0s5 up (will set it UP, check output)

sudo ip addr add 192.168.1.50/24 dev enp0s5

ifconfig ( only shows Primary IP addresses not secondary IP addresses)

ip a (show all addresses)

apt install net-tools (sometimes we are not able to use 'ifconfig', we neet this too to use that)


ss -t (open local connection)


ss -tl (TCP ports that are in listening mode)

sudo tcpdump -i <enp0s5> tcp (now it is listening, search a new query in chrom/firefox, it will listen that)(wireshark is the tool GUI used to capture the traffic)(tcpdump is linux utility to dump output in icap file, once dump is done then we need wireshark to read this file)

nc -VZ <192.168.1.1> 80 (net cat command to check the remote/local connection, 80 is port where it is listening)

telnet <192.168.1.50> 80 (can be used to check the connection for remote network; check the created socket type file for this)

curl -v http://localhost:8080 (Get the reponse if we do not have Web Browser)

netstat -st (all stats of TCP)
ss -s (all stats of Sockets)

host google.com (short summary of google.com)

cat /etc/resolv.conf

sudo vim /etc/netplan/*.yaml (setting custom DNS)
sudo netplan apply (to apply above done changes)

```

```bash
# DHCP Servers are used to automatically assign ip addresses to machines which are needed in the network network. 
# It does the discovery of client ip addresses after this it offers it to client. Client send the req of the offered ip addresses. That's how it acknowledge the client req.

cat /var/lib/dhcp/dhcpd6.leases (contains the entries about DHCP things, dhcp requires pkg 'isc-dhcp...')(To setup DHCP Server we need this)

sudo dhclient -r (renew the lease)

resolvectl status (will show service not found as it require 'system resolve' to run if we are using DNS mask)
sudo systemctl start systemd-resolved.service (start the service)
resolvectl status (Now we can run)
sudo systemctl disable systemd-resolved.service (stop the service)

sudo tcpdump -i enp0s5 -n (to check full traffic including local interface ip)

sudo tcpdump -i enp0s5 host google.com 

mtr google.com (check be used to see pings, loss etc, useful to back trace)

traceroute www.google.com (useful to see flow of traffic to google.com, hops -> routers, * means firewall are there else real ip will show)

```