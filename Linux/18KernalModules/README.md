# Linux Kernel Modules Notes

Linux Kernel Modules (LKMs) are pieces of code that can be loaded into or unloaded from the kernel on demand. They extend the functionality of the kernel without requiring a system reboot. LKMs are typically used for device drivers, file systems, and networking protocols.

---

## ⚙️ Core Concepts

* **Kernel Role**: The kernel acts as the engine of the operating system, managing hardware, processes, memory, files, and security.
* **Modularity**: Modules allow the kernel to stay updated and compatible with new IT landscapes, such as cloud computing and new hardware.
* **Open Source Contribution**: Since Linux is open-source, developers can write or modify C/C++ based kernel modules to customize system behavior.

---

## 💻 Essential Commands

### 1. Checking Kernel Version
To check the currently running kernel version, use the `uname` command:
```bash
uname -r
```

### 2. Listing Loaded Modules
To see all kernel modules that are currently active and running in your system:
```bash
lsmod
```
* *Tip:* This reads real-time status data directly from the `/proc/modules` file.

### 3. Fetching Module Information
To view details about a specific module (such as its license, author, description, and signature):
```bash
modinfo <module_name>
```

### 4. Dynamic Module Management (`modprobe`)
The standard and preferred tool for adding or removing modules because it handles dependencies automatically:
* **Load a module:**
  ```bash
  sudo modprobe <module_name>
  ```
* **Remove a module:**
  ```bash
  sudo modprobe -r <module_name>
  ```

### 5. Manual Module Insertion
If you have compiled a custom `.ko` (kernel object) file and want to force-insert it via its exact file path:
```bash
sudo insmod /path/to/module.ko
```

### 6. Checking Module Dependencies
To generate a list of module dependencies for the kernel to reference:
```bash
depmod
```

---

## 🔍 Diagnostics & Advanced Management

### Kernel Logging (`dmesg`)
When loading or troubleshooting hardware and modules, checking the kernel ring buffer logs is essential:
```bash
dmesg
```
* *Alternative:* You can also use `journalctl -k` to view filtered kernel-specific outputs.

### Blacklisting Modules
If a module causes software clashes or hardware instability, you can prevent it from loading automatically by adding an entry to the configuration files:
* **Configuration Directory:** `/etc/modprobe.d/`
* **Target File:** `/etc/modprobe.d/blacklist.conf`

To blacklist a module, append the following line to the file:
```text
blacklist <module_name>
```
