# Linux Network Configuration & SSH Administration

A comprehensive guide and reference documentation for configuring network interfaces using Netplan/Network Manager, establishing secure remote connections via SSH, and managing data transmissions on modern Linux systems (Ubuntu 18.04+).

---

## 🛠️ Network Interface Configuration

Modern Linux systems (such as Ubuntu 18.04 and newer) utilize **Netplan** as the default network configuration utility, while desktop or alternative server setups rely on **Network Manager**.

> [!WARNING]
> Choose **either** Netplan or Network Manager exclusively. Running both concurrently to manage the same physical network interface card (NIC) will cause configuration conflicts and drop your internet connection.

### 📂 Configuration Files
System configurations are stored as text profiles using the structured YAML (Yet Another Markup Language) layout inside the system configuration directory:
* **Netplan Interface Profile:** `/etc/netplan/50-cloud-init.yaml` *(The default file containing base cloud initialization network settings)*
* **Network Manager Generated Entry:** `/etc/netplan/90-nm.yaml` *(The dynamically created backup entry generated when Network Manager takes control)*

### ⌨️ Key Netplan Commands
* **Apply Network Changes:** (Instantly commits current YAML edits to the running system kernels)
  ```bash
  sudo netplan apply
  ```
* **Safe-Test Network Changes:** (Applies settings with a 120-second countdown; automatically rolls back changes if your ssh connectivity breaks)
  ```bash
  sudo netplan try
  ```
* **Verify Physical Interface Link:** (Displays all connected network adapters along with their current link state, such as UP or DOWN)
  ```bash
  ip link show
  ```
* **Display IP Address Allocations:** (Lists all assigned layer-3 IPv4 and IPv6 addresses paired to specific hardware interfaces)
  ```bash
  ip addr show
  # OR
  ip a
  ```
* **Manually Allocate Temporary IP:** (Forces an immediate static IP binding onto an interface; resets automatically on system reboot)
  ```bash
  # 'add 192.168.1.100/24': The IP address and subnet mask being bound
  # 'dev enp0s3': The target network interface card name
  sudo ip addr add 192.168.1.100/24 dev enp0s3
  ```
* **Manually Deallocate Temporary IP:** (Clears an explicitly configured static IP address from a live hardware controller)
  ```bash
  sudo ip addr del 192.168.1.100/24 dev enp0s3
  ```

### ⚙️ Managing Network Services via Systemd
* **Check Service Status:** (Queries the system manager to verify if the networking engine daemon is currently active, disabled, or failing)
  ```bash
  systemctl status NetworkManager
  ```
* **Stop Network Service:** (Kills the active network background daemon, cutting off dynamic link management handles)
  ```bash
  sudo systemctl stop NetworkManager
  ```
* **Start Network Service:** (Spawns a fresh network daemon listener to continuously monitor and connect interface nodes)
  ```bash
  sudo systemctl start NetworkManager
  ```

### 🎛️ Network Manager CLI (`nmcli`) Operations
* **List Active Device Connections:** (Prints a clean layout mapping managed profiles to their respective hardware controller UUIDs)
  ```bash
  nmcli connection show
  ```
* **Assign Static IP Address:** (Modifies a named connection template profile to inject a hardcoded IPv4 address parameter)
  ```bash
  # "enp0s3": The name of your saved network profile connection
  # "ipv4.addresses": The parameter field setting the system identity IP
  nmcli connection modify "enp0s3" ipv4.addresses 192.168.1.50/24
  ```
* **Assign Default Gateway:** (Defines the master router hop endpoint for exiting traffic destined outside the local network)
  ```bash
  # "ipv4.gateway": The target address routing all external traffic packets
  nmcli connection modify "enp0s3" ipv4.gateway 192.168.1.1
  ```
* **Assign DNS Servers:** (Configures domain name resolution systems to map web host strings directly to numerical IP entries)
  ```bash
  # "ipv4.dns": The IP endpoints for upstream public resolver arrays (Google DNS / Cloudflare DNS)
  nmcli connection modify "enp0s3" ipv4.dns "8.8.8.8,1.1.1.1"
  ```
* **Set Connection Method to Manual:** (Disables dynamic DHCP network discovery routines, forcing the link profile to respect static inputs)
  ```bash
  # "manual": Switches off automatic network configuration requests
  nmcli connection modify "enp0s3" ipv4.method manual
  ```
* **Activate Network Profile Changes:** (Brings down the old connection states and spins up the newly configured interface profile instantly)
  ```bash
  nmcli connection up "enp0s3"
  ```

---

## 🔑 Secure Shell (SSH) & Remote Login

Secure Shell (SSH) provides an encrypted cryptographic network channel for administering remote systems, operating natively over destination **Port 22**.

### 🔒 Server Hardening (`/etc/ssh/sshd_config`)
To secure enterprise environments against malicious automated discovery attacks, open `/etc/ssh/sshd_config` and adjust the configuration parameters as follows:

```ini
# Disable direct administrative root logins
# (Forces administrators to log in using an unprivileged user profile before running higher commands)
PermitRootLogin no

# Enable cryptographic public key authentication
# (Permits authentication checking via matching public/private digital key configurations)
PubkeyAuthentication yes

# Optional: Disable fallback password authentication
# (Blocks brute-force attempts by rejecting basic standard string passkeys globally)
PasswordAuthentication no
```
*Note: You must restart the runtime daemon module engine to read and enforce configuration profile adjustments.*

### 🎮 Managing the SSH Service
* **Check SSH Status:** (Queries systemd to verify the remote access daemon is actively running and watching for user connection hits)
  ```bash
  systemctl status ssh
  ```
* **Restart SSH Daemon Process:** (Triggers a quick shutdown and reboot sequence of the server listener to safely apply newly modified configuration values)
  ```bash
  sudo systemctl restart ssh
  ```
* **Persistent Boot Enable:** (Configures a symlink mapping in systemd to ensure the SSH service automatically launches following an uncontrolled machine reboot cycle)
  ```bash
  sudo systemctl enable ssh
  ```

### 🗝️ Key-Based Authentication Deployment
Eliminate vulnerable cleartext password handling routines entirely by setting up asymmetrical cryptographic key pairs.

1. **Generate Cryptographic RSA Key-Pair:** (Creates a complex mathematical validation token pair)
   ```bash
   # "-t rsa": Specifies the Rivest–Shamir–Adleman data encryption algorithm
   # "-b 4096": Explicitly defines a heavy 4096-bit key length matrix for high computational safety
   # "-C": Injects an identifiable descriptive text metadata comment tag string onto the tail of the key
   ssh-keygen -t rsa -b 4096 -C "admin@company.com"
   ```
   * *Private Key Path:* `~/.ssh/id_rsa` *(Your absolute digital identification token—never share this or transfer it from your local laptop!)*
   * *Public Key Path:* `~/.ssh/id_rsa.pub` *(The public anchor file deployed cleanly onto all external servers)*

2. **Deploy Public Key to Target Server:** (Automates logging into a target remote point and safely inserting your authentication token string)
   ```bash
   # "-i": Target flag pointing explicitly to your local system public verification file path
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote_host_ip
   ```
   *This appends your raw key string into the remote system's master file template path at `~/.ssh/authorized_keys`.*

### 🛰️ Remote Execution & Session Monitoring
* **Establish Remote Terminal Shell:** (Authenticates your identity and drops you into a remote, secure interactive bash subsystem)
  ```bash
  ssh user@remote_host_ip
  ```
* **One-Off Command Execution:** (Runs a process on a remote asset node and relays output data streams locally without spawning a persistent terminal console)
  ```bash
  # 'ls -la /var/www/html': The isolated terminal instruction processed remotely
  ssh user@remote_host_ip 'ls -la /var/www/html'
  ```
* **Monitor Active Shell Sessions:** (Prints connected tty console IDs, background processing runtimes, and incoming telemetry source locations for tracking users)
  ```bash
  w
  ```

---

## 📦 Data Transmission & Tunneling

### ✈️ Secure Copy Protocol (SCP)
Safely transfer structural files and source directories between distinct network endpoints over an authenticated SSH container framework.

* **Upload Local File to Remote Host:** (Copies local files up onto a remote infrastructure node directory destination)
  ```bash
  # "local_document.txt": The origin path item residing on your local workstation
