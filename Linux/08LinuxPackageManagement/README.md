# Linux Package Management Reference Guide

Packages are softwares. Package management in Linux automates software handling—including installation, updating, uninstallation, configuration, and structural dependency resolution.

---

## 🏗️ 1. Distribution Package Ecosystems
Linux package manager architectures vary depending on your software family and machine hardware layout.

### Package Management
Package management can be done using 3 type of tools `apt`, `yum` and `rpm`.

- **apt:** mainly used for debians like ubuntu.
- **yum:** It has a complete set of tools that are needed to download and install the software.
- **rpm:** rpm is Red Hat Package Manager, that is specificall dedicated for the Red Hat packages becaus Red Hat published those packages, available in rpm repositories (free).

```bash
apt list --installed (provide the list of pkgs installed on the ubuntu machine)
apt list --installed | grep -i vim (provide the vim related pkgs installed on the ubuntu machine)(this command is used to check if pkg is available)

apt-cache policy gimp (version of gimp pkg in repository(ubuntu pkgs OR apt repo))

apt-cache search python* (checks if python pkgs are available in apt cache)

cat /var/log/apt/history.log (seperate file apt history)

sudp apt check
apt search apache2 (search pkg 'apache2' and provide dependencies)


sudo apt install /pkg_name/path (to install available pkg)
sudo apt install pkg_name=2:8.0.1 (to install specific version pkg => not recommended)

sudo apt download pkg (used when pkg is not available in apt repo)


sudo add-apt-repository ppa:deadsnakes/ppa (adding a repository, repo has to be check or verified; useful when pkgs are on github or any other source)

sudo apt update (update pkg manager)

apt list --upgradable (list of upgradable pkgs)

sudo apt install python3.9

sudo apt-mark hold vim (it will not update vim now until will unhold it)
sudo apt-mark unhold vim (unhold vim)

sudo apt install vim --simulate (simulate tells more info in more redable format)
sudo apt reinstall vim --simulate (simulate tells more info in more redable format)

man apt

dpkg -l  (list all available packages, arrow key to up/down)
dpkg -l | grep vim (tells if vim is available)

sudo apt autoremove (remove all unused packages)

sudo apt clean (clean cache pkg file)

sudo apt autoclean (list pkgs that are taking disk spaces, auto clean them)

sudo apt --fix-broken install (fix broken pkgs)

apt show vim (provide information about pkg vim)
apt show bluefish (provide information about pkg bluefish)
```

### Distro Toolchain Breakdown
Different distributions rely on distinct low-level package formats and high-level dependency managers:

| Distribution Family | Package Extension | Low-Level Installer | High-Level Tool (Dependency Resolver) |
| :--- | :--- | :--- | :--- |
| **Debian / Ubuntu** | `.deb` | `dpkg` | `apt` / `apt-get` |
| **Red Hat (RHEL) / CentOS / Fedora** | `.rpm` | `rpm` | `yum` / `dnf` |
| **Arch Linux** | `.pkg.tar.zst` | N/A | `pacman` |

> ⚠️ **Hardware Architecture Safeguard:** Ensure downloaded software packages match your processor type. Running `AMD64` x86 binaries on native Apple Silicon `ARM64` virtualization environments can cause erratic behavior and structural failures.

### The Core Concept: Dependencies
Most software bundles are not single independent files. A parent package requires multiple sub-packages or libraries (dependencies) to work properly. Advanced tools like `apt` and `yum` automate the process of tracking, downloading, and installing these interconnected dependencies cleanly under the hood.

---

## ⚙️ 2. APT (Advanced Package Tool) Command Matrix
*These administrative operations are primarily used on Debian and Ubuntu distributions and require `sudo` system privileges.*

### Querying & System Inspection
*   **List Every Installed Package:**
    ```bash
    apt list --installed
    ```
    *Streams a complete record of every binary tracking on the host configuration.*
*   **Filter Installed Files:**
    ```bash
    apt list --installed | grep -i "vim"
    ```
    *Pipes the live tracking records to filter out specific target package strings.*
*   **Query Package Cache Availability:**
    ```bash
    apt-cache search python3
    ```
    *Scans your indexed system cache to locate matching software and libraries.*
*   **Inspect Remote Repository Versioning:**
    ```bash
    apt-cache policy gimp
    ```
    *Displays the exact package candidate variant available to pull versus the version locally installed.*
*   **Extract Deep Package Metadata:**
    ```bash
    apt show bluefish
    ```
    *Queries detailed information, including maintainer origin, structural dependencies, homepages, and descriptions.*
*   **Find Which Package Owns a Specific File on Disk (Crucial for Revision):**
    ```bash
    dpkg -S /usr/bin/vim
    ```
    *Reverse-searches the package database to identify exactly which package installed a specific command or configuration file.*

### Maintenance, Sync, & Installation
*   **Sync Package Repository Indexes:**
    ```bash
    sudo apt update
    ```
    *Contacts external package warehouses to pull the latest versions of upgradeable software lists.*
*   **List Upgradeable Packages (Crucial for Revision):**
    ```bash
    apt list --upgradable
    ```
    *Shows the names and version disparities of packages that have newer versions available in remote repositories.*
*   **Upgrade All Outdated Software Safely (Crucial for Revision):**
    ```bash
    sudo apt upgrade -y
    ```
    *Installs available upgrades for all packages currently installed on the system without deleting existing packages.*
*   **Install/Upgrade a Specific Package:**
    ```bash
    sudo apt install python3.9
    ```
    *Downloads the core target application package alongside all necessary operational dependencies.*
*   **Install From a Specific Manual Path:**
    ```bash
    sudo apt install ./package-name.deb
    ```
    *Installs local packages while utilizing APT to automatically fetch missing components over the network.*
*   **Pin Exact Version Alignments:**
    ```bash
    sudo apt install vim=2:9.1.*
    ```
    *Forces the system to install a precise software version instead of defaulting to the newest package release.*
*   **Reinstall a Package Buffer:**
    ```bash
    sudo apt install --reinstall vim
    ```
    *Overwrites active package configuration scripts to quickly fix corrupted software files.*
*   **Dry-Run / Installation Simulation:**
    ```bash
    sudo apt install vim --simulate
    ```
    *Simulates file footprints and changes cleanly without actually downloading files or altering disk storage.*

### Housekeeping, Safes, & Removals
*   **Uninstall Packages Safely:**
    ```bash
    sudo apt remove bluefish
    ```
    *Deletes the core application binaries but keeps user configuration profiles safe on disk.*
*   **Purge Software Footprints:**
    ```bash
    sudo apt purge bluefish
    ```
    *Wipes out configuration scripts, persistent data pools, and binaries completely.*
*   **Automatically Evict Abandoned Dependencies:**
    ```bash
    sudo apt autoremove
    ```
    *Scans your environment to safely purge unused, orphaned packages left behind by uninstalled software.*
*   **Clean Out Local Download Archives:**
    ```bash
    sudo apt clean
    sudo apt autoclean
    ```
    *`clean` clears cached `.deb` installer packages from local storage. `autoclean` removes outdated, redundant packages that can no longer be downloaded.*
*   **Force Fix Interrupted Environment States:**
    ```bash
    sudo apt install --fix-broken
    ```
    *Instructs the package manager to automatically repair broken dependency paths after failed installation runs.*

### Custom Repository Controls & Package Version Locking
*   **Pin/Hold a Package Version:**
    ```bash
    sudo apt-mark hold vim
    ```
    *Locks a package's current version, preventing global updates (`apt upgrade`) from changing it.*
*   **Release Version Update Locks:**
    ```bash
    sudo apt-mark unhold vim
    ```
    *Removes the version lock, allowing the software to safely upgrade during future system updates.*
*   **Register Secure Third-Party Developer PPAs:**
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    ```
    *Adds custom, verified external software repositories to your system package lists.*
*   **Remove an Unwanted PPA Repository (Crucial for Revision):**
    ```bash
    sudo add-apt-repository --remove ppa:deadsnakes/ppa
    ```
    *Cleans out an abandoned or broken PPA from your system configuration targets.*

---

## 📦 3. Low-Level Tracking Utilities (Using `dpkg`)
When working with standalone `.deb` package archives without relying on upstream remote connections, use the `dpkg` tool directly.

*   **List Every Local Package Record:**
    ```bash
    dpkg -l
    ```
    *Queries system inventory and prints out status maps, versions, and descriptions of all local packages.*
*   **Check a Specific Application Presence:**
    ```bash
    dpkg -l gedit
    ```
    *Verifies if a specific application package is actively tracking on your machine.*
*   **List Files Inside a Package Archive (Crucial for Revision):**
    ```bash
    dpkg -L vim
    ```
    *Lists every directory path and configuration file dropped onto your file system by that package.*

---

## ⚠️ 4. Essential Troubleshooting & Safety (Crucial for Revision)
*Commands to run when package management encounters errors or breaks down.*

### Resolving Stuck Lock Files
If an update process crashes or another installer is running in the background, you will see a `Could not get lock` error. Use these to find and resolve it:
*   **Find which process is locking APT:**
    ```bash
    sudo lsof /var/lib/dpkg/lock-frontend
    ```
*   **Kill the stuck process safely:**
    ```bash
    sudo kill -9 <PID_NUMBER>
    ```

### Reconfiguring a Broken Dpkg Database
If an installation gets cut off mid-way and crashes `dpkg`, reset the configuration state:
```bash
sudo dpkg --configure -a
```

---

## 🗂️ 5. Package Audit Trails & Logs
The package manager records system changes, updates, and uninstallation history inside specialized log files.

*   **Core History Log Path:** `/var/log/apt/history.log`
*   **Audit Command:**
    ```bash
    less /var/log/apt/history.log
    ```
    *Allows you to check historical timelines, identifying exact execution timestamps, tracking requested sub-packages, and identifying the User IDs that triggered changes.*
