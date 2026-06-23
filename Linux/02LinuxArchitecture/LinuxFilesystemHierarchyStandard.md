# Linux Filesystem Hierarchy Standard (FHS) & Modern Tooling Reference Guide

A structured overview and modern reference manual for the Linux Filesystem Hierarchy Standard (FHS). This document serves as a guide for system administrators, developers, and DevOps engineers to understand file placement, core sub-hierarchies, modern architectural changes, and next-generation command-line alternatives.

---

## 📌 Core Concepts

The FHS categorizes all system files into a 2 × 2 matrix based on two independent traits:

| | Shareable | Unshareable |
| :--- | :--- | :--- |
| **Static** | `/usr/bin`, `/opt` | `/etc`, `/boot` |
| **Variable** | `/var/mail`, `/var/spool` | `/var/run`, `/var/log` |

*   **Shareable:** Files that can be stored on one host and used by other machines (e.g., via NFS).
*   **Unshareable:** Machine-specific files that cannot be shared without breaking functionality.
*   **Static:** Read-only data that remains unchanged unless modified by a system administrator.
*   **Variable:** Volatile data that changes dynamically during system runtime.

---

## 📁 Modern Root Directory Layout (`/`) & UsrMerge

Modern Linux distributions (Ubuntu, Fedora, Arch) implement **UsrMerge**. Legacy directories (`/bin`, `/sbin`, `/lib`) are now **symbolic links** to their equivalents inside `/usr` to simplify package management, snapshots, and replication.

```text
/ (Root)
├── bin ──► usr/bin       # Essential user binaries (Merged)
├── sbin ─► usr/sbin      # System administration binaries (Merged)
├── lib ──► usr/lib       # Shared libraries & kernel modules (Merged)
├── boot                  # Bootloader files, kernel images, and initramfs
├── dev                   # Device nodes (hardware mappings)
├── etc                   # Host-specific system configuration files
├── home                  # User home directories
├── media                 # Mount points for removable media (USB, CD-ROM)
├── mnt                   # Temporary mount points for filesystems (USB drive, etc)
├── opt                   # Optional, standalone third-party software
├── proc                  # Virtual filesystem for kernel & process info
├── root                  # Home directory for the root superuser
├── run                   # Ephemeral runtime data (PIDs, sockets)
├── srv                   # Site-specific data served by this system (web servers)
├── sys                   # Hardware & driver subsystem info
├── tmp                   # Temporary files (wiped on reboot)
├── usr                   # User applications (The true software core)
└── var                   # Variable data (logs, caches, spools)
```

> ⚙️ **Immutable OS Note:** On modern atomic or immutable distributions (Fedora Silverblue, openSUSE MicroOS), `/usr` is mounted as **read-only**, while configurations persist dynamically in `/etc` and user data lives in `/var`.

---

## 🔍 Key Sub-Hierarchies

### 📦 The `/usr` Hierarchy (User Utilities)
Contains read-only, shareable data used after the core system boots. This is the largest directory on a typical system.
*   `/usr/bin`: Primary user commands and application binaries (e.g., `git`, `python`).
*   `/usr/sbin`: Non-essential system administration binaries used by the root user.
*   `/usr/local`: Host-specific programs compiled from source (ensures custom software doesn't mix with system packages).
*   `/usr/share`: Architecture-independent data (man pages, icons, time zones, application themes).

### 🪵 The `/var` Hierarchy (Variable Data)
Handles files that grow, shrink, or are continuously modified during operations. Isolating `/var` prevents runtime data from consuming the entire storage partition.
*   `/var/log`: System and application event logs (critical for troubleshooting).
*   `/var/cache`: Cached application data to save download or heavy processing time.
*   `/var/spool`: Task queues waiting for execution (e.g., print queues, outbound mail, cron jobs).
*   `/var/tmp`: Temporary files meant to survive system reboots (unlike `/tmp`).

### 🧠 Virtual Filesystems
These do not exist on physical storage; they are generated dynamically by the Linux kernel in RAM.
*   `/proc`: Exposes kernel variables, system hardware, and real-time process status tracking.
*   `/sys`: Highly-structured view of device drivers, kernel subsystems, and hardware settings.

---

## 🛠️ Next-Generation CLI Tooling

Modern system administration has shifted from legacy Unix tools to high-performance, safer, and feature-rich alternatives (mostly written in **Rust** or **Go**).

### 1. File & Directory Navigation
*   **`eza`** (Replaces `ls`): A modern drop-in replacement featuring color-coded file types, integrated Git status tracking, and built-in tree views.
*   **`zoxide`** (Replaces `cd`): A smarter, learning directory jumper that tracks your most frequently used paths for instant navigation.

### 2. Search & Text Processing
*   **`ripgrep (rg)`** (Replaces `grep`): A blazing-fast recursive search utility that naturally respects `.gitignore` rules and hidden files.
*   **`fd`** (Replaces `find`): A simple, fast, and user-friendly alternative to the `find` command that uses sensible color-coded defaults.

### 3. File Inspection & Editing
*   **`bat`** (Replaces `cat`): A `cat` clone that features automatic Git integration, syntax highlighting for multiple languages, and paging capabilities.
*   **`helix` / `neovim`** (Replaces `vi` / `nano`): Modern terminal editors featuring out-of-the-box LSP support, syntax trees, and smart selections.

### 4. System Monitoring & Storage
*   **`btop`** (Replaces `top` / `htop`): A visually striking terminal dashboard displaying real-time CPU usage, memory processes, disk I/O, and network activity.
*   **`ncdu` / `dust`** (Replaces `du`): Interactive, multi-threaded disk usage analyzers that easily track down large storage hogs.
*   **`procs`** (Replaces `ps`): A modern process viewer featuring color-coded output, keyword search, and docker container ID mappings.

### 5. Network Utilities
*   **`doggo` / `dig`** (Replaces `nslookup`): Modern DNS clients featuring human-readable outputs and JSON export capabilities.
*   **`httpie` / `curlie`** (Replaces `curl`): User-friendly CLI HTTP clients built for interacting with APIs, featuring formatted JSON outputs.

---

## 🎯 Best Practices

1.  **Isolate Custom Binaries:** Install standalone tools to `/usr/local/bin` or `/opt` to prevent system updates from altering them.
2.  **Keep `/etc` Version Controlled:** Track changes to your primary system configuration directory using tools like `etckeeper` and Git.
3.  **Prevent Disk Exhaustion:** Always configure structured log rotation (`logrotate`) under `/var/log` to stop services from consuming the entire partition.

