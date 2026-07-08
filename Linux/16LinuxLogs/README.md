# Linux Log Monitoring

Linux logs track system activity, application behavior, and security events. Effectively reading and managing these logs is a core responsibility for system administrators troubleshooting system issues.

---

## Log Management: `journalctl` vs. `syslog`

Modern Linux distributions use two primary logging architectures: **systemd-journald** (`journalctl`) and **traditional syslog**.

| Feature | `journalctl` (`systemd-journald`) | `syslog` / `rsyslog` |
| :--- | :--- | :--- |
| **Storage Format** | Binary files | Plain text files (`/var/log/*`) |
| **Search Speed** | Exceptionally fast and optimized | Slower (requires text parsing tools) |
| **Storage Efficiency** | Highly compressed binary data | High storage footprint |
| **Real-time Tail** | Supported natively via flags | Requires external commands (`tail -f`) |

---

## Mastering `journalctl` (Systemd Journal)

`journalctl` queries the binary logs populated by the `systemd-journald` service and then provide to us in readable format.

### Basic Navigation & Views
* **View all logs since boot**: 
  ```bash
  journalctl # provide full logs
  journalctl --output=short # provide logs in a shorter format
  journalctl --output=json # provide logs in json format, we can use this json file to create report or meaningful analytics using tools like ElasticSearch, splunk.
  ```
  *(Launches a scrollable  `less` style interface. Press `q` to exit, or search with `/`)*.
* **View logs from current boot**:
  ```bash
  journalctl -b
  ```

### Filtering Logs
* **Filter by a specific service unit** (`-u`):
  ```bash
  journalctl -u <service-name>
  journalctl -u ssh # use to debug service
  ```
* **Filter by log priority level** (`-p`):
  ```bash
  journalctl -p <priority>
  journalctl -p 3
  journalctl -p err
  ```
  *Common Priority Levels:* `3` (Error), `4` (Warning), `5` (Notice), `6` (Informational), `7` (Debug).
* **Filter exclusively for Kernel logs** (`-k`):
  ```bash
  journalctl -k
  ```
* **Filter for current user logs**:
  ```bash
  journalctl --user
  ```

### Time-Based Filtering
* **Filter logs since a specific date/time**:
  ```bash
  journalctl --since "2025-01-18 00:00:00"
  ```
* **Filter logs within a specific time window**:
  ```bash
  journalctl --since "10:00" --until "10:30"
  journalctl --since "2025-01-18" --until "2025-01-19"
  ```

### Real-Time Monitoring & Output Formatting
* **Follow live log updates (Real-time tracking)**:
  ```bash
  journalctl -f
  ```
* **Follow live updates for a single service**:
  ```bash
  journalctl -u apache2 -f
  ```
* **Limit output to a specific number of lines**:
  ```bash
  journalctl -n 100
  ```
* **Format output as structured JSON data**:
  ```bash
  journalctl -o json
  ```
  *(Highly useful when piping logs into modern analysis tools like `JQ`, Splunk, or ElasticSearch)*.

### Maintenance & Vacuuming
Binary log files can grow large. Use vacuum rules to clear old archival records. Always ensure data backups exist before trimming logs in production environments.
* **Trim logs to a fixed storage limit**:
  ```bash
  sudo journalctl --vacuum-size=100M
  ```
* **Purge logs older than a specific timeframe**:
  ```bash
  sudo journalctl --vacuum-time=10d
  ```

---

## Reading Traditional Text Logs (`syslog`)

Traditional log mechanisms output events in human-readable plain text inside the `/var/log` directory.

### Essential Log File Locations
* **`/var/log/syslog`** (or `/var/log/messages`): Global system activity log.
* **`/var/log/auth.log`** (or `/var/log/secure`): Authentication and authorization events (user logins, `sudo` access).
* **`/var/log/kern.log`**: Raw kernel messages and hardware events.
* **`/var/log/apache2/`** (or `/var/log/nginx/`): Web server records containing `access.log` and `error.log`.

### Monitoring Plain-Text Logs
* **Real-time live monitoring of text logs**:
  ```bash
  sudo tail -f /var/log/syslog # system logs
  cat /var/log/syslog # system logs
  ls /var/log # other logs

  sudo tail -f /var/log/kern.log # kernal logs
  sudo tail -f /var/log/auth.log # authentication logs -> monitor SSH authentication attempts
  ```
* **Track web server traffic logs live**:
  ```bash
  sudo tail -f /var/log/apache2/access.log
  sudo tail -f /var/log/apache2/error.log
  ```

---

## Log Manipulation & Troubleshooting Tools

### Advanced Log Filtering (`grep` & Pipeline Mechanics)
Combine logs with text filter pipes to isolate data sequences efficiently.
* **Search logs for exact keyword instances**:
  ```bash
  journalctl | grep "<keyword>"
  journalctl | grep "SSH"
  ```
* **Count the total occurrences of an event line**:
  ```bash
  journalctl --since "today" | grep "ssh" | wc -l
  ```

### Creating Custom Logs (`logger`)
You can inject a custom string directly into the system log subsystem for testing pipeline configurations.
```bash
logger "Test Log Entry: Checking pipeline functionality"
```

### Output Redirection
Export a log window directly into a localized text file for troubleshooting analysis using single (`>`) or double (`>>`) operators.
* **Overwrite export to a file**:
  ```bash
  journalctl > logs.txt
  journalctl -u ssh -n 100 > ssh_diagnostic.log
  ```
* **Append export to a file**:
  ```bash
  journalctl -u apache2 -n 100 >> ssh_diagnostic.log
  ```

---

## Other Topics

### Log Rotation (`logrotate`)
Plain text logs grow infinitely if left unchecked. Linux uses the `logrotate` utility to systematically compress, rename, or delete old logs based on rules configured in `/etc/logrotate.conf` and `/etc/logrotate.d/`.

### Kernel Rings (`dmesg`)
Before logging services launch during early system boot phases, kernel events print to a localized ring buffer memory block. Use `dmesg` to inspect these early initialization sequences:
```bash
# View human-readable boot hardware logs
dmesg -T
```

## More commands
```bash
# Generate a Test log 
logger "This is a test log entry"

journalctl | grep "test log entry" # view the test log


## stop a service to generate an error
sudo systemctl stop apache2
journalctl -u apache -p err # check logs


## Forward logs to Remote server

# Edit rsyslog configuration:
sudo nano /etc/rsyslog.conf
Add:
*.* @remote-server:514

#Restart rsyslog
sudo systemctl restart rsyslog
#verify logs on the remote server

man journalctl




## Analytics
journalctl --output=json
journalctl -u apache2 --output=json 
#jq refers to json query, query performed on json.
journalctl -u apache2 --output=json | jq '{message: .MESSAGE, hostname: .hostname}'


which systemctl # dir for any command
```