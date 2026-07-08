# Linux Services Management with SYSTEMCTL (Notes)

This guide covers service and daemon architecture, full `systemctl` syntax workflows, legacy syntax alternatives, and essential production-grade related topics.

---

## ⚙️ Section 1: Core Concepts of Service Management

Understanding how background programs interface with the operating system kernel is essential for troubleshooting service lifecycles.

### What is a Service and a Daemon?
* **Service**: Any application software running actively on top of the kernel layer is treated as a service. When a service is stopped, its active communication threads to the kernel and hardware resources are severed.
* **Daemon**: A background process that runs continuously to handle recurring system requests. By standard naming convention, daemons are identified by a trailing letter `d` (e.g., `sshd` for Secure Shell Daemon, `crond` for Cron Daemon).
* **Systemd**: The core system and service manager responsible for initializing the OS and controlling background operations. It is the very first process started by the kernel during boot, and it permanently retains **Process ID (PID) 1**. Historically, legacy versions of Linux utilized an architecture called `init`, which modern `systemd` has fully replaced.

### Dynamic vs. Transient Services
* **Persistent Services**: Continuous network apps (e.g., Apache `apache2`, SSH `ssh`) that stay actively loaded in memory to receive external requests.
* **Transient (One-Shot) Services**: Short-lived utilities that activate, perform a single automated task or hardware interaction, and then immediately enter an `exited` state to free system memory. They do not run continuously.

### Volatile In-Memory Tracking (`/run`)
* Linux maps running processes directly into memory space to track active states.
* Active daemons store their active process runtime state inside the volatile path `/run`.
* Stopping and restarting a service wipes its old files out of `/run` and registers a completely new PID entry (e.g., inside `/run/sshd.pid`). This data is lost when power is cut because `/run` resides completely in volatile RAM.

---

## 🛠️ Section 2: Command Reference Workflows (`systemctl`)

The modern utility `systemctl` offers advanced service capabilities and handles infrastructure changes cleanly on the fly.

### 1. Monitoring & Listing Services
* `systemctl list-units --type=service`
  * Displays a full table of all loaded and managed service units currently initialized on the host machine.
* `systemctl status <service_name>`
  * Displays a detailed diagnostic overview of an application.
  * Shows memory footprints, CPU utilization time, current PID, boot integration context (`enabled`/`disabled`), exact timestamps since activation, and short trailing log lines.
* `systemctl is-enabled <service_name>`
  * Directly queries the init system to see if the target service is configured to start automatically when the system boots up.
* `systemctl --failed`
  * Filters and targets broken or failed applications instantly. This helps you scan for underlying application errors without wading through healthy systems table trees.

### 2. Lifecyle Control Operations
* `sudo systemctl start <service_name>`
  * Boots a target service instantly into active memory.
* `sudo systemctl stop <service_name>`
  * Gracefully tears down operational states and detaches the app safely from kernel threads.
* `sudo systemctl restart <service_name>`
  * Directs systemd to fully stop the target process and start it back up again immediately. This updates its running profile and assigns it a new PID.
* `sudo systemctl reload <service_name>`
  * Live updates modified configuration settings on the fly without interrupting user traffic or forcing a full restart. Unlike Windows environments, which often require complete system restarts, Linux updates configurations seamlessly.

### 3. Boot & Access Restrictions
* `sudo systemctl enable <service_name>`
  * Links the application into target system startup stages so it starts automatically during a system boot.
* `sudo systemctl disable <service_name>`
  * Prevents the application from starting automatically at boot. However, the service can still be started manually by other users or applications.
* `sudo systemctl mask <service_name>`
  * Hard-locks an application by mapping its configuration path directly to a dead link (`/dev/null`). This completely prevents users and automated scripts from starting or stopping the service.
* `sudo systemctl unmask <service_name>`
  * Removes structural access restrictions, restoring the service back to regular manual or automated control states.
* `sudo systemctl daemon-reload`
  * Forces systemd to scan the disk for newly added or customized unit files, updating its execution tree cleanly on the fly.
* `journalctl -u <service-name>`
  * view logs of a service
* `man systemctl`
  * manual for systemctl command.

---

## 🔄 Section 3: Legacy Comparison (`service` vs `systemctl`)

While administrators should prioritize the modern `systemctl` command structure, legacy commands remain useful when interacting with older enterprise machines.
* **systemctl** is more powerful and provides additional functionality (eg enabling/disabling services, viewing logs, and masking services).
* **service** is simple but lacks advanced options and is considered deprecated.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        SYNTAX COMMAND COMPARISON                       │
├───────────────────────────────────┬────────────────────────────────────┤
│ Modern Systemd (`systemctl`)      │ Legacy SysVinit (`service`)        │
├───────────────────────────────────┼────────────────────────────────────┤
│ systemctl start apache2           │ service apache2 start              │
│ systemctl stop ssh                │ service ssh stop                   │
│ systemctl status cron             │ service cron status                │
│ systemctl reload nginx            │ service nginx reload               │
│ systemctl list-units --type=service│ service --status-all               │
└───────────────────────────────────┴────────────────────────────────────┘
```

* **Argument Ordering**: `systemctl` places the desired action first and the target application second. The legacy `service` tool places the application name first and the action command at the end.
* **Deprecation Warnings**: Under the hood, modern machines transparently redirect legacy `service` requests through systemd compatibility layers. However, relying on old commands is a bad habit; they are slowly being deprecated across modern Linux distributions.

```bash
# Using Service
  
  ## check service status
  sudo service <service-name> status
  sudo service apache2 status

  ## Start a service
  sudo service <service-name> start
  
  ## Stop a service
  sudo service <service-name> stop
  
  ## Restart a service
  sudo service <service-name> restart
  
  ## Reload a service
  sudo service <service-name> reload
  
  ## list all services
  service --status-all
```

---

## 💡 Section 4: Other Related Topics 

To round out your production knowledge, ensure you understand these additional concepts commonly used in enterprise scale-out architectures:

### 1. Anatomy of a Custom Systemd Service File
You can inspect or build custom configuration profiles at `/etc/systemd/system/`. A standard configuration follows this architecture:

```ini
[Unit]
Description=My Custom Production Python API
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /opt/myapp/api.py
Restart=on-failure
User=www-data

[Install]
WantedBy=multi-user.target
```
* **After**: Specifies dependencies, ensuring this app waits to initialize until network services are completely active.
* **Restart=on-failure**: Automatically revives the process if it crashes unexpectedly, providing resilient self-healing.
* **WantedBy**: Maps the program to standard terminal operation levels (multi-user target matches standard boot states).

### 2. Systemd Targets (Runlevels)
Legacy Linux machines relied on numbered Runlevels (`0-6`) to determine system states. Systemd uses `.target` profiles to group dependencies and configure server boot targets cleanly:
* `multi-user.target`: Boots the machine into a standard, secure text console terminal workspace (common for remote cloud instances).
* `graphical.target`: Loads full graphical user interfaces and desktop managers on top of background services.
* To shift modes instantly without forcing a reboot, use: `sudo systemctl isolate multi-user.target`.

### 3. File Metadata Analysis via `stat`
Briefly touched on in the lecture, the `stat` command provides deep metadata context for files:
* Run `stat /etc/systemd/system/` to display exact inode configurations, file block allocations, and strict access permission profiles.
* It logs three distinct system timestamps: **Access** (last read time), **Modify** (last content update), and **Change** (last metadata or permission adjustment).

## More Commands
```bash
man systemctl

# data or entries related to service are also kept in a files
cd /run/systemd # systemd is service manager to manage serives.
ls system # .service file are also files
sudocat system/netplan---.service

cat /run/sshd.pid # provide the process id => pid may change everytime we stop and start the service
ps aux | grep -i ssh

systemctl stop ssh # stopped
systemctl start ssh # start
cat /run/sshd.pid # now id is different

# /run is th dir where all the volatile files like PID are present.


systemctl status apache2
systemctl status cron # can read more on CGroup

sysemctl reload ssh # just reload to apply changes but does not restart


sudo systemctl enable ssh #provide the dir path with that it is synchronised
cat /usr/lib/systemd/systemd-sysv-install # got this path from above enable command
stat /usr/lib/systemd/systemd-sysv-install # stat command is to see the meta data of a file.


# mask => prevent any service to start
sudo systemctl mask ssh # service is masked and it will create a symlink
systemctl restart ssh # show failed to restart as it is masked
systemctl status ssh # show ssh as inactive

sudo systemctl unmask ssh # loaded but inactive
sudo systemctl start ssh # start the service
systemctl status ssh # service is masked and active -> only admin can start it now, other users can only stop it.
systemctl list-units --type=service # can see ssh in yellow 


systemctl daemon-reload # under the hood daemon is the one managing systemctl and service. Both use same dir.

# INIT is in the previous version of Linux but now it is systemd. It runs on PID 1 (one) as first process.
htop # can check here as well
```