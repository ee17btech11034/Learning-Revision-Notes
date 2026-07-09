# Linux Performance Tuning & Monitoring Notes

Performance tuning in Linux involves monitoring, analyzing, and adjusting system parameters across critical hardware resources—CPU, Memory, Storage I/O, and Network. The goal is to optimize stability, eliminate bottlenecks, and ensure applications run under ideal conditions.

---

## 🚀 1. CPU Monitoring & Optimization

### Core Real-Time Tools
* **`top`**: Displays an interactive, real-time summary of the system's resource state. It tracks active processes, CPU percentage per state (user vs. system), memory usage, and load averages.
* **`htop`**: A visually enhanced, color-coded alternative to `top` offering advanced filtering, process searching, and thread tracking.
  * *Signal Management*: Within `htop`, hitting **F9** exposes 64 standard system signals. Selecting a process and sending `SIGKILL` (`kill -9`) triggers an immediate, unyielding kernel-level termination.

### Deciphering System Load Averages
The load average values display system queues over 1, 5, and 15-minute periods.
* **Understanding Core Capacity**: On a 4-core machine, a load rating of `4.00` indicates a precise 100% capacity balance across all cores.
* **Identifying a Bottleneck**: Spikes on the short-term 1-minute load are safe to ignore if long-term trends remain low. However, sustained values doubling capacity (e.g., `8.00` on a 4-core machine) over the 5 and 15-minute marks warn of stacked backlogs requiring swift resolution.

### Dynamic CPU Priority Tuning
* **`renice`**: Alters the execution priority of already active processes using their Process ID (PID).
  * Nice values span an aggressive `-20` (highest priority, high CPU preference) to `19` (lowest priority).
  ```bash
  # Shift an active process to an aggressive, high-priority state
  sudo renice -n -5 -p <PID>
  ps aux # to know the priority 
  ```

### More
```bash
ps # to list all process
ps aux # will list all running process
```

---

## 🧠 2. Memory Utilization & Tuning

### Memory Diagnostics
* **`free -h`**: Provides a human-readable layout of physical RAM allocation and Swap usage. Production nodes typically flag administrative warnings when physical allocations consistently breach 90%.
* **`vmstat`**: Tracks virtual memory statistics, page-swapping operations, and CPU idle fractions. A high `id` (ideal/idle) value around 95% indicates an unburdened processor.

### Kernel Swappiness Management
Swappiness defines the kernel's balance profile between freeing active RAM pages and leveraging the backup disk storage (Swap space).
* Values range from `0` to `100`.
* **Lower Values (`0`–`10`)**: Forces the kernel to favor local physical RAM retention, avoiding slow disk swapping. This setup is ideal for low-latency systems like gaming machines or production desktop boxes.
* **Higher Values (`60`–`100`)**: Aggressively offloads inactive process memories over to the backup disk partition.

```bash
# Check current system swappiness value
cat /proc/sys/vm/swappiness

# Modify swappiness temporarily on the fly
sudo sysctl vm.swappiness=10

sudo sysctl -p # to save these changes
man sysctl


/sbin/sysctl -n kernel.hostname # same as below command
hostname
cat /etc/lsb-release # both above commands use this file to get the data
```

### More
```bash
free #to check currently available memory in bytes
free -h #to check currently available memory in a better way
# We must make sure that if free memory is below 10% then alert user because it may create issue.

vmstat #
man vmstat # manual


## For disk I/O tunning
vim /etc/fstab

man fstab
man mount
```
---

## 💾 3. Storage Input/Output (I/O) Tuning

### I/O Monitoring
* **`iostat -x <interval>`**: Generates extended storage device and partition input/output metrics. High `iowait` states flag storage constraints where processing layers are waiting on slow physical disk reads/writes. High-throughput platforms like Apache Kafka require persistent disk monitoring to prevent data processing delays.
  ```bash
  # Check extended device I/O statistics refreshed every 5 seconds
  iostat -x 5
  iostat -x sda sdb 2 5 # provide data about sda every 2 sec, for sdb every 5 sec.
  ```

### File System Adjustments
* **`noatime` Option**: Adjusting storage behavior inside `/etc/fstab` can speed up intensive I/O operations. Appending the `noatime` flag to a file system block stops the kernel from writing timestamp updates every single time a file is accessed.
* **Disk Quotas**: Running `quotaon` lets system admins implement hard storage ceilings, preventing individual profiles or groups from completely filling up disk arrays.

```bash
apt install quota
man quota # quata is restrictions like upper limit or lower limit.
```

---

## 🌐 4. Network Performance & Tuning

### Traffic Analysis via `iftop`
The `iftop` command tracks network socket traffic across active interfaces in real time.
* **Directional Vectors**: On-screen arrows map clear transactional pathways, displaying whether data is transmitting outwards to external targets or pulling down inwards.
* **DNS Resolution Toggle**: Stripping domain mapping by pressing **n** speeds up terminal rendering by displaying raw IP addresses.

```bash
sudo iftop # not good way to look


# Bind network inspection to a single targeted active interface
sudo iftop -i enp0s5

# Start monitoring with domain name resolution disabled automatically
sudo iftop -n
```

### Optimizing Network Windows & Buffers
For vast cloud environments or high-bandwidth transactions, adjusting core TCP socket sizing allows for significantly increased network data throughput.

```bash
# Push max core receive network socket memory parameters outwards
sudo sysctl -w net.core.rmem_max=16777216

# Push max core write network socket memory parameters outwards
sudo sysctl -w net.core.wmem_max=16777216

# Reload and commit runtime parameter states directly from sysctl configuration
sudo sysctl -p
```

