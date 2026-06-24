# Linux Process Management and Task Scheduling

## 🧵 Process Concepts and Types
* **Foreground Process**: Runs on the front of the shell, takes up active space, and blocks further shell interaction until completion.
* **Background Process**: Runs under the hood (`&`), allowing you to continue executing other tasks simultaneously on the active terminal shell.

---

## ⚙️ Process Control & Monitoring Commands

### 📊 System Monitoring Matrix
* `ps`: Standard tool to view running processes. Use `ps aux` to list all system processes with comprehensive owner details.
* `top`: Real-time legacy text mode process layout showing dynamic CPU and physical usage metrics.
* `htop`: Interactive, modern, colorful process viewer featuring scrolling, custom search layout, column configurations, and hierarchical tree views (`F2`).

### 🛠️ Foreground & Background States
* `Ctrl + Z`: Instantly suspends a running foreground execution, dropping it into a stopped background state.
* `jobs`: Lists the dynamic identification tracking ID and state of all current active or stopped shell processes.
* `bg %<job_id>`: Resumes a stopped job, forcing it to execute directly in the background.
* `fg %<job_id>`: Pulls a background or stopped process back into full foreground terminal shell focus.

### ❌ Terminating Processes
* `kill <PID>`: Transmits a standard software termination signal (`SIGTERM`) requesting the kernel to cleanly stop a process via its unique process ID.
* `kill -9 <PID>`: Transmits an immediate forced shutdown signal (`SIGKILL`) to instantly kill stubborn or unresponsive processes.

---

## 📈 Managing Process Priorities

Linux determines a process’s scheduling importance using **Nice values** (typically ranging across standard operational weights).

* `nice -n <value> <command> &`: Launches a fresh project instance initialized under a specific priority level.
* `renice <value> -p <PID>`: Dynamically adjusts the running execution priority value of an active Process ID on the fly.
* `sudo renice <value> -u <username>`: Modifies execution priority thresholds for all active workloads owned by a specific system user account.
* *Note*: Standard users can only decrease priority. Setting negative nice values to grant higher CPU priority requires root administrator privileges (`sudo`).

---

## ⏰ Automated Task Scheduling

### 🔄 Recurring Tasks: `cron`
The `cron` daemon handles automated background scripts using a specific five-field calendar time grid layout:
```text
┌────────────── minute (0 - 59)
│ ┌──────────── hour (0 - 23)
│ │ ┌────────── day of month (1 - 31)
│ │ │ ┌──────── month (1 - 12)
│ │ │ │ ┌────── day of week (0 - 7, where 0 or 7 is Sunday)
│ │ │ │ │
* * * * * <command_to_execute>
```

* `crontab -l`: Lists all scheduled automation jobs configured for the current session user.
* `crontab -e`: Opens your profile workspace configuration block inside terminal editors (e.g., `vim`) to add or edit tasks.
* `crontab -r`: Purges and deletes all registered recurring jobs for the session user account.
* `sudo crontab -u <username> -e`: Configures automation calendars for a different targeted system user.

#### Practical Cron Examples:
* **Run a Python validation utility every hour at minute zero:**
  ```bash
  0 * * * * /usr/bin/python3 /home/parallels/password_check.py
  ```
* **Append dynamic diagnostic trace statements to a file every minute:**
  ```bash
  * * * * * echo "hi this is staragile" >> /home/parallels/file.txt
  ```

### ⏱️ One-Time Tasks: `at`
Used to execute a command or script exactly once at a specific time in the future, rather than on a recurring schedule.

* `at <time>`: Opens an interactive structural shell (`/bin/sh`) prompt where you enter commands. Press `Ctrl + D` to save the job.
* `echo "<command>" | at now + 2 hours`: Proactively pipelines a one-time job execution window exactly two hours out from the current system time.
* `atq`: Audits the queue to list all pending one-time automated tasks.
* `atrm <job_id>`: Removes a pending task from the one-time scheduling queue.

---

## 🪵 Diagnostics & System Logs
* **System Cron Events**: View system logs by filtering for the cron keyword within the central logging system file:
  ```bash
  sudo grep cron /var/log/syslog
  ```

## More commands:
```bash
sleep 100  (sleep for 100 sec; forground process as we can not use this terminal untill this is completed; 'ctrl+z' to stop (in stop state))

jobs (tells about the process that are running, in stop state, in start state)

fg 1 (again run the process, it brings process on forground on shell, 1 is cmd number/id in 'jobs')


sleep 100 & ('&' tells to run in background)

jobs 

bg  %1 (run job 'id=1' in background)

kill processID (kill processID)

sudo kill -9 ProcessID ('-9' tells to force kill, )
ps aux | grep -i "command" (to find the processID in 2nd col)
pas aux | grep -i "sleep 100" 

man kill

ps (running processes)
ps aux (all processes)
htop (all process live:-> PR-> process priority, Ni-> used to calculate priority, VIRT -> Virtual memory used by process, RES -> Residential memory (physical), SHR -> shared memory, S/R-> R for running/ S for sleeping,  Kernal works)(swap memory -> not a physical RAM but a physical memory)(press f2, we will see category, we can choose options)


nice -n 10 sleep 300 & (setting priority '10' for high priority as default is 0)

renice -n priorityNum -p processID (change the priority for a process)

sudo renice -n priorityNum -u user1 (change the priority for all process run by user1)

jobs
ps aux | grep "sleep 1000"


(only root can assign -ve priority as -ve are top)

top (same as top but layout/options is not that good)
```

```bash
* * * * * /path/to/command (first star tells mins(0-59), 2nd is hour 0-23, 3rd is day 1-31, 4th is month 1-12, 5th day of week 1-7)

crontab -l (list of scheduling task for user)

crontab -e (set a crontab, e tells to choose editor to add details for schedule)(0 * * * * python a.py ==> run py file each hour at 0 min)(0 * * * * python a.py > ~/file.txt 2> /dev/null ==> output in file.txt and error in /dev/null)

crontab -r (remove the cron)

sudo crontab -u user1 (set by/for user1)

time (tells time)
date (tells date)
```

```bash
echo "ls -al" | at 3:30 PM (one time run this command)

atq (check the commands which are set, provide id as well)

at 3:30 (will open a command)(end command like ls /home/parallels  ctrl+d to close enter to add new command)

atrm jobID (remove this single command, use atq for jobID)

echo "Hello" | at now + 2 hours (2 hours later)



grep CRON /var/log/syslog (log file for CRON)
cat /var/spool/at (at logs, can check if location is different)


echo "notify-send ' Meeting at 3PM!'" | at 2:55 PM


```