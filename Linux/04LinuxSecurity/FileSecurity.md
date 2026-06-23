# 🔒 Linux File Permissions, Security & Privilege Escalation (Ep 04)

Welcome to the production-grade master revision manual for managing system flags, security boundaries, and user accounts in Linux. This module breaks down standard file notations, ownership structures, special operational properties (SUID/SGID/Sticky Bits), granular Access Control Lists (ACLs), and advanced access control loops using the `sudo` architecture.

---

## 🏗️ 1. Understanding the Linux Permission String

When you evaluate a directory item layout using the standard long listing command `ls -l`, the kernel returns a 10-character string reflecting its structural security settings:

```bash

r  w x r   w - r   - - 1 parallels parallels  4096 Jun 23 11:15 file1.txt
│ └──┬──┘ └──┬──┘ └──┬──┘
│    │       │       └─ Others Permissions (Users outside the Owner or Group)
│    │       └─ Group Permissions (Members belonging to the Primary Group)
│    └─ Owner/User Permissions (The individual account that created/owns the file)
└─ File Type Indicator (e.g., '-' = Regular File, 'd' = Directory)

```

### 🔹 The Core Permission Tiers & Operational Traits
* **`r` (Read):** Value = **4**. For files, permits reading data contents. For directories, allows listing item names inside the folder via `ls`.
* **`w` (Write):** Value = **2**. For files, permits altering or saving data modifications. For directories, allows creating, renaming, or deleting nested file entries.
* **`x` (Execute):** Value = **1**. For files, allows binary programs or scripts to run as system tasks. For directories, allows the user to change into the path (`cd`) and open files inside it.

---

## 🛠️ 2. Resource Management Command Matrix

| Utility Command | Core Operational Target | Key Production Options & Syntax Pass Patterns |
| :--- | :--- | :--- |
| **`chmod`** | **Change Mode:** Alters access flags using either symbolic letters or numerical octal groups. | `u` (User), `g` (Group), `o` (Others), `a` (All).<br>`chmod 644 file.txt` : Forces precise octal mask.<br>`chmod o+w folder` : Appends write flags to others safely. |
| **`chown`** | **Change Owner:** Re-allocates the underlying account owner or group alignment of an active file. | Requires root privilege level context.<br>`chown john file.txt` : Shifts user target mapping.<br>`chown user:group file` : Shifts user/group in one pass. |
| **`chgrp`** | **Change Group:** Exclusively alters the primary group alignment mapping tracking identifier. | `chgrp marketing data_share` |

### 🔄 Recursive Modification Enforcement
To push permission or ownership modifications all the way down through deep multi-layered directories and structural subfolder groupings in a single command, apply the **Recursive (`-R`)** switch:
```bash
# Shift both user owner and group alignment across all nested configurations simultaneously
sudo chown -R himansu1:himansu1 /home/parallels/myd/
```

---

## 🔏 3. Beyond Standard Permissions: Access Control Lists (ACLs)

Standard Linux permissions limit you to configuring only **one owner, one group, and others**. If you need to give a *second* specific user account access to a file without rewriting the entire group configuration, standard bits fail. This requires **Access Control Lists (ACLs)**.

### How to Identify an ACL-Protected File
When an ACL is applied to a file, the `ls -l` permission string appends a **plus sign (`+`)** onto the end of the permissions array:
```text
-rw-rwxr--+ 1 admin engineering 1024 Jun 23 11:15 corporate_plan.xlsx
          ▲
          └─ This plus sign alerts you that extended ACL entries are active!
```

### Essential ACL Administration Commands:
```bash
# 1. Inspect extended permissions using getfacl
getfacl corporate_plan.xlsx

# 2. Grant read/write access to an individual outside user account (e.g., 'alice') using setfacl
setfacl -m u:alice:rw corporate_plan.xlsx

# 3. Strip all custom configurations and return to standard permissions
setfacl -b corporate_plan.xlsx
```

---

## 🔒 4. Deep Dive: Special Linux Security Permissions

Beyond standard user/group rings, the kernel uses specialized bits to handle complex file execution behaviors and secure team shared workspaces:

### A. SUID (Set User ID) — Symbolic Indicator: `s` (User Tier)
* **Operational Rules:** When an executable file with an active SUID flag is run, the executing process assumes the authority and privilege level of the **file owner** rather than the account currently clicking enter.
* **Real-World Case Study:** The **`passwd`** tool (`/usr/bin/passwd`). Standard users need to edit `/etc/shadow` to update their password, but that file is locked down to root access only. The `passwd` binary has SUID active and is owned by `root`. When a standard account runs it, the task escalates to root authority temporarily to patch the shadow file successfully.
```bash
# Enforce SUID symbolically on an executable script component
chmod u+s processing_binary
```
*⚠️ Production Security Warning:* SUID binaries are high-value targets for attackers. If an administrator leaves a root-owned file like a Python runner or a text editor with SUID active, an unprivileged user can use that file to drop into a root system shell, resulting in a severe privilege escalation breach.

### B. SGID (Set Group ID) — Symbolic Indicator: `s` (Group Tier)
* **Operational Rules:** Applied mainly to directories. Any subfolder or file created inside an SGID directory automatically inherits the **parent directory's group owner**, ignoring the primary group of the user account that made it.
* **Real-World Case Study:** Collaborative engineering folders where multi-tier groups drop documentation assets, ensuring group read/write operations stay unbroken.
```bash
# Force group inheritance rules on a team repository folder
sudo chmod g+s /tmp/shared_repository/
```

### C. The Sticky Bit — Symbolic Indicator: `t` (Others Tier)
* **Operational Rules:** Restricts file deletion within a directory. Even if a directory has wide-open write rights (`777`), an account **cannot delete or rename** files inside it unless they are the explicit file owner or the system root administrator.
* **Real-World Case Study:** The system public temp directory (`/tmp`). It lets anyone drop operational metrics, but blocks malicious or broken accounts from accidentally purging critical background task temp blocks belonging to other active workloads.
```bash
# Protect directory assets from accidental third-party purges
sudo chmod +t /tmp/shared_repository/
```

---

## ⚡ 5. The Sudo Architecture & Sudoers Hardening

The **`sudo` (Superuser Do)** command lets authorized system users scale their privilege rings temporarily to run commands as the root superuser or another protected service profile.

### 🔒 Operational Advantages over Root Account Login
1. **User Accountability:** Avoids sharing absolute root credentials across operations teams.
2. **Detailed Auditing Trails:** Every execution line passed through `sudo` logs back to internal monitoring facility chains (`/var/log/auth.log` or `/var/log/secure`), showing exactly who performed an administrative change.
3. **Granular Control Boundaries:** Admins can configure rules down to the individual command level, locking an account into a single restricted management task.

### ⚙️ Configuring the `/etc/sudoers` Policy Index
Never modify the `/etc/sudoers` data array using raw text editors directly. If you break a single syntax character, you risk locking every user completely out of administrative privilege control blocks. Always invoke the safe verification configuration utility **`visudo`**, which scans for structural formatting errors before saving changes:
```bash
# Safely open up the sudoers policy configuration tracking array
sudo visudo
```

#### Production Entry Directives Syntax Rule Checklist:
To authorize an infrastructure account (e.g., `himansu1`) to invoke an editor tool on a specific root file path without prompting for a user account password challenge, configure the rule exactly like this:

```text
himansu1    ALL=(ALL:ALL) NOPASSWD: /usr/bin/vim /etc/sudoers
# └──┬──┘   └─┬─┘ └───┬───┘   └───┬────┘ └───────────┬────────────┘
#    │        │       │           │                  └─ Absolute path to the allowed command binary
#    │        │       │           └─ Suppress the authentication password challenge prompt
#    │        │       └─ Rule maps to all users and all group execution rings
#    │        └─ Rule applies across all network host connections
#    └─ Target system user profile account
```

### 🎛️ Advanced Privilege Identification Options
* **`sudo -l` (List):** Scans the active configuration rules and prints exactly what command limits are allocated to your current terminal profile.
* **`sudo -u username command`:** Runs a task acting under the specific authorization mask of a separate user profile instead of root.
* **`sudo -k` (Kill Cache):** Clears your active cached validation tokens instantly. This forces the shell to require your password on the very next `sudo` call rather than relying on standard 15-minute time-out windows.
* **`sudo -i` vs `sudo su`:**
  * `sudo -i` opens a clean, authentic **Root Login Shell**, changing your workspace path straight to the root home profile (`/root`) while sourcing all administrative environment profile attributes.
  * `sudo su` escalates privileges to the root user but preserves your current user account's environmental shell variables and path locations intact.

---
