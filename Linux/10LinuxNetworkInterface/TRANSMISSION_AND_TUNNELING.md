# Secure Data Transmission & Network Tunneling Guide (Part 3)

This reference document outlines the implementation, execution parameters, and architectural definitions for safely moving file sets and establishing secure network communication tunnels.

---

## 📦 Data Transmission & Tunneling

### ✈️ Secure Copy Protocol (SCP)
Safely transfer structural files and source directories between distinct network endpoints over an authenticated SSH container framework.

* **Upload Local File to Remote Host:** (Copies local files up onto a remote infrastructure node directory destination)
  ```bash
  # "local_document.txt": The origin path item residing on your local workstation
  # "user@remote_host_ip...": The target host network identifier address and target directory path
  scp local_document.txt user@remote_host_ip:/home/user/target_directory/
  ```
* **Download Remote File to Local Working Path:** (Grabs files hosted on distant remote points and pulls them into your current local active window)
  ```bash
  # "./": The target location mapping directly to your current active local directory path
  scp user@remote_host_ip:/home/user/remote_document.txt ./
  ```

### 🚇 Local Port Forwarding (SSH Tunneling)
Securely route web, testing, or internal database access streams originating locally on your computer through an encrypted secure gateway over to an unreachable network node target:

```bash
# "-L": Signals Local Port Forwarding routine structures
# "[local_binding_port]": The port number you map on your physical machine
# "localhost:[remote_application_port]": The true internal port listening at the remote end
ssh -L [local_binding_port]:localhost:[remote_application_port] user@remote_host_ip
```

#### Example Usage
Map a custom local desktop web tracking port (`8081`) to handle internal production traffic listening explicitly on remote asset port `80` across your firewall perimeter:
```bash
ssh -L 8081:localhost:80 system_user@10.211.55.12
```
Now, navigating directly to `http://localhost:8081` within your local browser safely wraps and decrypts all network requests straight through to the production network framework endpoint.

---

## 💡 Extra Production Administration Tools

### 🌐 Advanced Socket & Troubleshooting Diagnostics
* **Discover Actively Listening Network Sockets:** (Returns tracking summaries for all open system ports along with application process execution tags)
  ```bash
  # "-t": Shows TCP sockets / "-u": Shows UDP sockets
  # "-l": Limits tracking onto active listening state items
  # "-n": Displays precise numeric metrics rather than tracking resolved service string text
  # "-p": Unveils the explicit operational system Process ID (PID) owning the channel
  ss -tulnp
  ```
* **Follow Real-Time Authentication System Failure Streams:** (Pipes a continuous live log stream tracking security access trends and authentication validations to catch intrusions)
  ```bash
  # "-u ssh": Limits logging profiles to the tracking daemon service engine
  # "-f": Forces the console to follow the file logs in real-time as events land
  journalctl -u ssh -f
  ```
* **Trace Layer 3 Routing Network Hops:** (Maps out intermediate layer-3 system route points and delay metrics to target endpoints for uncovering routing failure blocks)
  ```bash
  traceroute google.com
  ```

### 📝 Complete Blueprint Netplan Static Profile Template
To explicitly enforce predictable static network connections via custom manual scripts, modify your tracking file profile located at `/etc/netplan/50-cloud-init.yaml` using this layout template structure:

```yaml
network:
  version: 2
  renderer: networkd      # Specifies 'networkd' as the backend infrastructure core engine driver
  ethernets:
    enp0s3:               # Your targeted physical hardware network interface device name identifier
      dhcp4: no           # Explicitly shuts off automatic structural dynamic IP address assignments
      addresses:
        - 192.168.1.50/24 # Assigns the static IPv4 node identifier along with its Classless Inter-Domain Routing (CIDR) netmask
      routes:
        - to: default
          via: 192.168.1.1 # Directs system traffic destined outside the local network out through the gateway router
      nameservers:
        addresses:
          - 8.8.8.8       # Google Primary Public Name Resolution server engine target IP
          - 1.1.1.1       # Cloudflare Secondary Public Name Resolution server engine target IP
```
