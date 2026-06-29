# Linux Network Configuration Guide (Part 1)

A comprehensive guide and reference documentation for configuring network interfaces using Netplan/Network Manager on modern Linux systems (Ubuntu 18.04+).

---

## 🛠️ Network Interface Configuration

Modern Linux systems (such as Ubuntu 18.04 and newer) utilize **Netplan** as the default network configuration utility, while desktop or alternative server setups rely on **Network Manager**.

> [!WARNING]
> Choose **either** Netplan or Network Manager exclusively. Running both concurrently to manage the same physical network interface card (NIC) will cause configuration conflicts and drop your internet connection.

### 📂 Configuration Files
System configurations are stored as text profiles using the structured YAML (Yet Another Markup Language) layout inside the system configuration directory `sudo ls /etc/netplan/`:
* **Netplan Interface Profile:** `/etc/netplan/50-cloud-init.yaml` *(The default file containing base cloud initialization network settings)*
* **Network Manager Generated Entry:** `/etc/netplan/90-nm.yaml` *(The dynamically created backup entry generated when Network Manager takes control)*

```bash

```

### ⌨️ Key Netplan Commands
* **Open Network Changes:** (Open YAML file to edits to the running system kernels)
  ```bash
  sudo vim /etc/netplan/*.yaml
  ```
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
  systemctl status NetworkManager (systemctl is a utility that helps us get the status of tool running on Linux machine)
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
  nmcli connection show (network manager cli command to check the connect with network manager)
  ```
* **Assign Static IP Address:** (Modifies a named connection template profile to inject a hardcoded IPv4 address parameter)
  ```bash
  # "enp0s3": The name of your saved network profile connection or 'netplan-enp0s5' etc.
  # "ipv4.addresses": The parameter field setting the system identity IP
  nmcli connection modify "enp0s3" ipv4.addresses 192.168.1.50/24
  nmcli con mod "enp0s3" ipv4.addresses 192.168.1.50/24
  ```
* **Assign Default Gateway:** (Defines the master router hop endpoint for exiting traffic destined outside the local network)
  ```bash
  # "ipv4.gateway": The target address routing all external traffic packets
  nmcli connection modify "enp0s3" ipv4.gateway 192.168.1.1
  nmcli con mod "enp0s3" ipv4.gateway 192.168.1.1
  ```
* **Assign DNS Servers:** (Configures domain name resolution systems to map web host strings directly to numerical IP entries)
  ```bash
  # "ipv4.dns": The IP endpoints for upstream public resolver arrays (Google DNS / Cloudflare DNS)
  nmcli connection modify "enp0s3" ipv4.dns "8.8.8.8,1.1.1.1"
  nmcli con mod "enp0s3" ipv4.dns "8.8.8.8,1.1.1.1"
  ```
* **Set Connection Method to Manual:** (Disables dynamic DHCP network discovery routines, forcing the link profile to respect static inputs)
  ```bash
  # "manual": Switches off automatic network configuration requests
  nmcli connection modify "enp0s3" ipv4.method manual
  nmcli con mod "enp0s3" ipv4.method manual
  ```
* **Activate Network Profile Changes:** (Brings down the old connection states and spins up the newly configured interface profile instantly)
  ```bash
  nmcli connection up "enp0s3"
  nmcli con up "enp0s3"
  ip a (to check changes)
  ```
