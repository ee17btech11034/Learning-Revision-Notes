# 🧮 Linux Permissions Math: Binary, Octal & Umask Deep Dive

Welcome to the architectural reference sheet for Linux permission calculations. This document strips away the symbolic abstractions (`rwx`) to break down the underlying mathematical equations, bitmask conversions, and umask filtering logic utilized by the Linux Kernel.

---

## 🔢 1. The Core Binary-to-Octal Translation

At the lowest architectural layer, the Linux kernel reads permission bits as a series of electronic on/off switches (**Binary values `1` and `0`**). These bits are grouped into triplets representing three distinct user domains: **User/Owner**, **Group**, and **Others**.

Each bit inside a triplet has a fixed, positional mathematical weight:

* **First Position (Read):** Binary 2^2 = Weight of **4**
* **Second Position (Write):** Binary 2^1 = Weight of **2**
* **Third Position (Execute):** Binary 2^0 = Weight of **1**

### 📐 The Mathematical Summation Rule

To convert any symbolic string into an octal integer, you calculate the absolute sum of the enabled weights within that specific 3-bit block:

```bash
Symbolic String Layout:         ( r   w   x )
Binary Bit Field Mask:            1   1   1
Positional Value Weight:          4 + 2 + 1  =  7 (Full Access)

Symbolic String Layout:         ( r   w   - )
Binary Bit Field Mask:            1   1   0
Positional Value Weight:          4 + 2 + 0  =  6 (Read & Write)

Symbolic String Layout:         ( r   -   x )
Binary Bit Field Mask:            1   0   1
Positional Value Weight:          4 + 0 + 1  =  5 (Read & Execute)

Symbolic String Layout:         ( r   -   - )
Binary Bit Field Mask:            1   0   0
Positional Value Weight:          4 + 0 + 0  =  4 (Read-Only)

```

### 📋 Full Octal-to-Symbolic Reference Matrix

| Octal Value | Binary Bitmask | Symbolic String | Absolute System Privilege Level |
| :---: | :---: | :---: | :--- |
| **`7`** | `111` | `rwx` | **Full Read, Write, and Execute:** Complete control over the resource. |
| **`6`** | `110` | `rw-` | **Read and Write:** Can modify data contents but cannot execute binaries. |
| **`5`** | `101` | `r-x` | **Read and Execute:** Standard configuration for scripts and navigatable directories. |
| **`4`** | `100` | `r--` | **Read-Only:** Safe viewing access; blocks all file modifications. |
| **`3`** | `011` | `-wx` | **Write and Execute:** Highly irregular state; write access without read capabilities. |
| **`2`** | `010` | `-w-` | **Write-Only:** Rare state; useful for drop-only logging files. |
| **`1`** | `001` | `--x` | **Execute-Only:** Can run a binary but cannot read its underlying code. |
| **`0`** | `000` | `---` | **No Permissions:** Access completely denied for that specific user ring. |

---

## 🎭 2. The Mechanics of the Umask (User Mask)

When an application or user accounts generate a fresh resource, they do not assign permissions arbitrarily. The operating system utilizes a base default system template and passes it through an elimination filter called the **User Mask (`umask`)**.

The `umask` dictates which permissions **must be stripped away** during the creation process for security hardening.

### 🛑 Maximum Structural Boundaries (The Starting Point)
Before the umask filter drops, the kernel assigns a maximum theoretical ceiling value based on resource type:
* **Maximum Directory Base = `777` (`rwxrwxrwx`)** — Paths need execute rights by default so users can cross into them (`cd`).
* **Maximum File Base = `666` (`rw-rw-rw-`)** — Files block execute rights at creation to prevent rogue or uploaded files from executing automatically.

### 🧮 The Umask Subtraction Formula
The finalized octal permission string is resolved using simple positional subtraction:
Maximum Base Ceiling - System Umask = Final Creation Permissions

#### Practice Scenario A: Standard User Configuration (`umask 022`)

```bash
        DIRECTORY CREATION                             FILE CREATION
Max Directory Base:     7 7 7                  Max File Base:          6 6 6
Deduct System Umask:  - 0 2 2                  Deduct System Umask:  - 0 2 2

────────────────────────────
Final Perm State:       7 5 5                  Final Perm State:       6 4 4
Symbolic Output:     (rwxr-xr-x)               Symbolic Output:      (rw-r--r--)
```

#### Practice Scenario B: Shared Team Workspace Configuration (`umask 002`)

```bash
        DIRECTORY CREATION                             FILE CREATION
Max Directory Base:     7 7 7                  Max File Base:          6 6 6
Deduct System Umask:  - 0 0 2                  Deduct System Umask:  - 0 0 2

────────────────────────────
Final Perm State:       7 7 5                  Final Perm State:       6 6 4
Symbolic Output:     (rwxrwxr-x)               Symbolic Output:      (rw-rw-r--)
```

#### Practice Scenario C: Hardened Production System Configuration (`umask 077`)

```bash
        DIRECTORY CREATION                             FILE CREATION
Max Directory Base:     7 7 7                  Max File Base:          6 6 6
Deduct System Umask:  - 0 7 7                  Deduct System Umask:  - 0 7 7

────────────────────────────
Final Perm State:       7 0 0                  Final Perm State:       6 0 0
Symbolic Output:     (rwx------)               Symbolic Output:      (rw-------)
```

---

## ⚡ 3. The Special Bit Offset Math (SUID / SGID / Sticky)

Standard file systems use a **3-digit** octal mask (`644`). However, the complete system permission string contains a hidden **4th leading digit** used to track specialized system operational properties:

```text
Special Bit Digit 👇
7 5 5 5
│ │ │ │
│ │ │ └─ Others Permissions (Standard)
│ │ └─ Group Permissions (Standard)
│ └─ Owner/User Permissions (Standard)
└─ Special Security Permissions Mask
```

### 🔢 Special Bit Positional Weights
* **SUID (Set User ID):** Weight value = **4**. Prepend this to elevate processes to file owner privileges.
* **SGID (Set Group ID):** Weight value = **2**. Prepend this to force group folder asset inheritance.
* **Sticky Bit:** Weight value = **1**. Prepend this to create deletion protection zones inside directories.

### 📐 Comprehensive 4-Digit Examples
```bash
# Example 1: Enforce the Sticky Bit (1) on a wide-open directory (777)
chmod 1777 /var/shared_scratch/
# Output String Result: drwxrwxrwt (Note the trailing 't')

# Example 2: Enforce both SUID (4) and SGID (2) on an administrative tool path
# Mathematical calculation: 4 + 2 = 6 (Leading Special Digit)
chmod 6755 /usr/local/bin/custom_admin_tool
# Output String Result: -rwsr-sr-x (Note both user and group show 's')
```

---

## 🚀 Speed-Run Revision Practice Guide

Test your conversion processing speeds against these common production configurations:

1. **`chmod 755`** -> `rwxr-xr-x` : Standard script file (Full user control, read/execute for everyone else).
2. **`chmod 600`** -> `rw-------` : Highly secure data file (Only the owner can read or write; everyone else is blocked).
3. **`chmod 444`** -> `r--r--r--` : System-wide immutable file configuration (Read-only for all accounts).
4. **`chmod 2770`** -> `rwxrws---` : Collaborative secure group directory (No outside access, forces group alignment inheritance automatically).

## More examples:
```bash
ls -al file.txt (we can see the permissions)
umask (to check the umask value for user)
ls -al dir1 (we can see the permissions)

chmod o+w dir1 (it will add the 'write permission' for other ('o') users)
chmod u-w dir1 (it will remove the 'write permission' for user ('u') users)
chmod g-x dir1 (it will remove the 'execute/open permission' for group ('g') users)
chmod ug+rw,o+r file.txt (user, group will get read & write both but other will get read)
chmod 444 file.txt (user will get first 4, group will get 2nd 4, other will get last 4.)


sudo chown user2 file.txt (change the owner to user2)
sudo chown user2:user2 file.txt (change the owner&group to user2)
sudo chown -Ruser2:user2 dir (change the owner&group to user2 for dir and its all files)

sudo chgrp user3 dir (group permission to user3, only dir)


# to check the command binary location 
which ls (bin dir location for 'ls' command)
which passwd (bin dir location for 'passwd' command)

ls -al /usr/bin/passwd (here we will see 'rws...' for user. Here 's' is Set UID, means set on the user ownership. Means whoseever will run this command, this command will run with the power of user/owner of command) (that's why companies do not give root permission to user. As they can run and change or delete things, like serer setup, etc.)

chmod u+s file.txt (this will set 'rwS' 'capital S' as it is set by a user not by root. if 's' is there then it is set by root user.)

su - user3 (to switch user)
exit (logout the user)

ctrl + dot (.) (puts the argument from above command in here curr cmd)

(if a user1 creates a dir in tmp then group owner will be 'user1'. If user2 create files in that dir then group owner will be same 'user1')



# Sticky bit:-> user can add the data or files in a dir but can not delete it.
chmod +t dir (other user can not delete files inside dir even if others have write permission on dir)
chmod -t dir (other user can delete files inside dir only if others have write permission on dir)

```

## Sudo Command:
`SUDO` is a lightweight, secure command-line utility that allows authorized users to execute individual commands with elevated administrative privileges (as a superuser or root). It functions similarly to the classic Unix `sudo` but is optimized for custom environment restrictions and modern configuration parsing. Whenever we need admin/root permission to execute something. 

### Features
- **Privilege Elevation:** Execute specific workflows as `root` without switching user contexts completely. Grants temporary administrative rights to execute commands.
- **Granular Access Control:** Define explicitly which users can run which commands via a custom configuration file called `sudoers`. 
- **Activity Logging:** Log every executed command, timestamp, and invoking user to `/var/log/sudo_activity.log` for audit trails.
- **Cache Timeout:** Cache credentials safely for a configurable window (default: 15 minutes) to avoid repeated password prompts.
- **Enhanced Security:** Reduces the need to log in as the root user directly, minimizing security risks.

### Use Cases:
- **Installing Software:**
```bash
sudo apt install package_name
``` 
- **Managing Services:**
```bash
sudo systemctl restart service_name
``` 
- **Editing System Files:**
```bash
sudo nano /etc/fstab
``` 
- **Changing File Ownerships/Permissions:**
```bash
sudo chmod 644 file.txt
sudo chown user:group /path/to/file
``` 

### Command Options

| Flag | Long Flag | Description |
| :--- | :--- | :--- |
| `-h` | `--help` | Displays the help text menu and exits. |
| `-v` | `--validate` | Updates the user's cached credentials timeout window. |
| `-k` | `--kill` | Revokes the current cached credentials immediately. |
| `-l` | `--list` | Lists the allowed and forbidden commands for the invoking user. |

other: 

```bash
sudo -l
sudo -u username command (Run a command as a specific user -> default is root)
sudo -k
sudo -s (start a shell with root priviledges)
sudo -i (Start a root login shell, directory also changes to root)
sudo su (start as root, but directory does not change)

sudo -u user2 ls /home/user2 (while being user1, we can access the data from user2)
```

### Password Behaviour
- **Authentication:** by default, `sudo` prompts for the user's password to verify permissions.
- **Caching:** After successful authentication, `sudo` caches credentials for a short period (default 15 mins).
- **Password Bypass:** Usinf `NOPASSWD` in the `sudoers` file can allow specific commands to run without a password prompt.

```bash
sudo vim /etc/sudoers [open the file in vim and can add 
(user1 ALL=(ALL) NOPASSWD: /usr/bin/vim /etc/sudoers)(if user1 tries to open sudoers file with sudo command then it won't ask for password)]

vim /etc/hosts (read only file -> contains DNS informations)
sudo vim /etc/hosts (writable file)

sudo apt install pkg-1 (install packages)
which apt
ls -al /pth/apt (others has permission to execute this file but internal files are locaked so we need sudo)
```