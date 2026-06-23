# 📁 Linux Command Line Basics & Comprehensive Core Utilities

Welcome to the ultimate production-grade revision blueprint for mastering the Linux Command Line Interface (CLI). This module provides a dense, hands-on architectural review of foundational data traversal, pipeline operations, text manipulation, and deep search filters required for standard system administration and DevOps workflows.

---

## 🏗️ 1. The Anatomy of a Linux Command

Every structured interaction within the Linux terminal environment follows a standardized syntactical pattern:
```bash
command [options] [arguments]
```
* **Command:** The base executable binary or shell builtin utility (e.g., `ls`, `find`, `cat`).
* **Options (Flags):** Prefixed with a single hyphen (`-`) for short-form flags or double hyphens (`--`) for long-form configurations. These alter the operational behavior of the command.
* **Arguments:** The target entities or file parameters on which the command executes its tasks (e.g., file paths, directory addresses, text blocks).

### 📖 Accessing Interactive Help Layouts via `man` & `--help`
When unsure which specific options or positional arguments map to a command, utilize the built-in system documentation:
```bash
# Display the explicit core definitions, syntax flags, and descriptions for a command
man ls

# Display a short, concise summary of available options inline
mkdir --help
```
*Manual Navigation Tip:* Press `q` to terminate the manual viewing interface instantly.

---

## 📂 2. Directory Navigation & Absolute vs. Relative Paths

Linux manages file path tracking using two distinct, fundamental addressing methodologies:

### A. Absolute File Paths
* **Core Trait:** Always initiates from the absolute **Root Directory (`/`)**.
* **Operational Constraint:** It provides a fixed, explicit map down the file hierarchy from the top-most layer, regardless of your active terminal position.
```bash
# Navigate to a user profile using an absolute, root-prefixed layout
cd /home/parallels/myd
```

### B. Relative File Paths
* **Core Trait:** Initiates from your **Present Working Directory (PWD)** without using a root slash prefix.
* **Operational Symbols:**
  * `.` (Single Dot): Represents the absolute present directory structure itself.
  * `..` (Double Dot): Represents the precise Parent Directory one layer above.
  * `~` (Tilde Symbol): Represents the underlying Home Directory of the actively logged-in user profile.
  * `-` (Hyphen Symbol): Switches back to the immediate previous working directory state.
```bash
# Shift exactly one directory block up to the parent directory, then branch into a neighbor folder
cd ../john
```

---

## 📚 3. The Master Linux Command Library

To ensure your revision notes are complete, this library expands far beyond the basic video outline to cover all primary categories of everyday system administration utilities.

### 🧭 A. Filesystem Navigation & Information
* **`pwd`** (Print Working Directory): Reveals the complete absolute path location where your shell process is currently operating.
* **`ls`** (List): Prints directories and files inside a targeted folder path.
  * `ls -l` : Long list format displaying sizes, permissions, owners, and modification timestamps.
  * `ls -a` : Displays hidden files (any configuration file prefixed with a `.`).
  * `ls -h` : Combines with `-l` to print file sizes in human-readable formats (KB, MB, GB).
  * `ls -R` : Recursive lookup listing all files inside subfolders.
* **`cd`** (Change Directory): Traverses from your current structural path position to a target directory.
  * *Crucial Distinction:* `cd` is a **Shell Built-in** command, not an external binary. It must run inside the current shell memory space to change your terminal's path.
* **`clear`** (Reset View): Flushes the terminal scrollback history to give you a clean viewport workspace. (Shortcut: `Ctrl + L`).

### 🛠️ B. File & Directory Management
* **`touch`** : Generates an empty 0-byte regular data placeholder file if it doesn't exist, or updates the access/modification timestamps of an existing file.
* **`mkdir`** (Make Directory): Generates a new folder node.
  * `mkdir -p path/to/folder` : Generates parent directories recursively if they do not already exist.
* **`rmdir`** (Remove Directory): Deletes a folder entry safely **only** if it is completely empty.
* **`rm`** (Remove): Wipes file profiles permanently from storage.
  * `rm -r` : Recursive delete, mandatory for wiping folders and their contents.
  * `rm -f` : Forceful execution that suppresses safety warnings and confirmation prompts.
* **`cp`** (Copy): Replicates an existing file or directory layout structure to a fresh target storage location.
  * `cp -r` : Recursive flag required when copying folder blocks.
* **`mv`** (Move): Cuts and relocates a target resource from a source path to a destination path. Also acts as the default system tool to **rename** files.
* **`ln`** (Link): Formats structural shortcuts on your drive.
  * `ln -s source target` : Creates a soft/symbolic link pointer.

### 📝 C. Text Viewing & Content Manipulation
* **`cat`** (Concatenate): Reads and prints plaintext file content streams directly into the active standard output terminal window.
* **`echo`** : Outputs a plaintext string or variable block directly to the screen or to data streams.
* **`less`** : Opens large text files or logs in a paginated, scrollable viewport interface. Prevents your terminal memory from choking on massive data readouts.
* **`head`** : Outputs the top lines of a target file. Default is the first 10 lines.
  * `head -n 20 file.txt` : Displays exactly the first 20 lines.
* **`tail`** : Outputs the trailing lines of a target file. Default is the last 10 lines.
  * `tail -f file.log` : Active tracking mode. Keeps the file stream open and prints new log entries in real-time as they are written.
* **`nano` / `vim`** : Built-in command-line text editors used to write scripts and edit system configuration text blocks natively in the shell.

### 🔍 D. Searching, Filtering & Aggregation
* **`grep`** (Global Regular Expression Print): Functions like a command-line `Ctrl + F`. Scans plaintext data streams or target files to extract only lines matching a specific pattern.
  * `grep -i` : Case-insensitive matching filter.
  * `grep -v` : Inverted match; filters out and hides lines matching the target pattern.
  * `grep -r` : Recursively searches for text strings within all files in a directory tree.
* **`find`** : Searches the physical directory hierarchy for files matching conditional properties (names, sizes, types, permissions).
  * `find . -type f -name "*.sh"` : Finds all regular script files ending in `.sh` under your current directory.
* **`wc`** (Word Count): Calculates the bounds of a text file stream.
  * `wc -l` : Outputs the exact line count.
  * `wc -w` : Outputs the exact word count.
  * `wc -c` : Outputs the exact character byte count.

### ⚙️ E. System Performance, Processes & Disks
* **`ps`** (Process Status): Captures a static snapshot of actively running background and foreground processes.
  * `ps aux` : Displays all running processes across all users on the host system.
* **`top` / `htop`** : Dynamic real-time task manager frameworks displaying current CPU core usage, RAM absorption, uptime matrices, and resource-heavy PIDs.
* **`kill`** : Terminates an active process using its distinct Process ID (PID).
  * `kill -9 PID` : Sends the `SIGKILL` kernel instruction to forcefully terminate a non-responsive background task.
* **`df`** (Disk Free): Reports structural storage statistics, displaying available and used disk space across mounted filesystems.
  * `df -h` : Human-readable size strings.
* **`du`** (Disk Usage): Calculates space consumed by specific files or directory trees.
  * `du -sh *` : Prints a summary screen showing the total file space occupied by each item in your active path.
* **`free`** : Prints active system memory parameters, detailing total, used, free, and cached physical RAM/Swap boundaries.
  * `free -h` : Human-readable display format.

### 🌐 F. Network Diagnostics & Connectivity
* **`ping`** : Sends ICMP Echo Requests to network hosts to check baseline external network connectivity and response latency.
* **`curl` / `wget`** : Command-line network engines used to download files or interact with remote API web endpoints over protocols like HTTP, HTTPS, and FTP.
* **`ip a` / `ifconfig`** : Displays system network interface hardware mappings, active local IP configurations, and hardware MAC routing values.

### 👥 G. Ownership, Permissions & History
* **`chmod`** (Change Mode): Modifies the read (`r`), write (`w`), and execute (`x`) permissions flags of target resources.
* **`chown`** (Change Owner): Assigns a new user or group owner to files and directories.
* **`sudo`** (Superuser Do): Escales privilege boundaries to execute commands with root administrative authority.
* **`history`** : Prints an indexed log listing previous terminal commands executed by the active user profile.
  * `!#` (e.g., `!957`) : Reruns that indexed command code block instantly.
* **`alias`** : Generates customized shorthand labels to map long, complex command strings into a simple single-word trigger.

---

## 🛠️ 4. Advanced Stream Redirection & Pipelines

Linux excels at linking commands together to create sophisticated data processing workflows. This section covers output redirection, error management, and pipeline orchestration.

---

## A. Output Redirection Operators (`>` and `>>`)

Redirection operators alter where standard command output is sent, routing data away from the terminal screen and directly into storage configurations.

* **`>` (Overwrite)**: Routes standard command outputs straight into a target file, wiping out any data that was previously inside that file.
* **`>>` (Append)**: Appends new data rows to the absolute bottom of the target file without destroying its existing contents.

### Interactive Code Examples:
```bash
# Overwrite a log file with a new string entry
echo "Hi this is Himanshu your DevOps trainer at StarAgile" > server_logs.txt

# Append a secondary line safely onto the bottom of the same log file
echo "Appending a backup timestamp reference row" >> server_logs.txt

# Check your work by reading the final file contents
cat server_logs.txt
```

---

## B. Standard Error Redirection (`2> /dev/null`)

Every command line process tracks separate output streams: **Standard Output (1 / stdout)** and **Standard Error (2 / stderr)**. 

When running large system lookup passes, unauthorized directories cause a flood of "Permission Denied" errors that clutter your viewport. You can isolate pure success logs by routing the Standard Error channel (`2>`) into the system's virtual black hole device node (`/dev/null`):

### Interactive Code Example:
```bash
# Find files globally by name, but silently discard all access permission errors
find / -name "config.yml" 2> /dev/null
```

---

## C. The Pipe Operator (`│`)

The pipe symbol channels the textual output of a preceding tool and maps it directly as the input vector for a trailing utility. This memory-efficient design processes streams dynamically, avoiding the overhead of temporary file read/write operations.

### Interactive Code Examples:
```bash
# Example A: Extract process tracking metrics, filter down to root tasks, and print the active line count
ps aux │ grep "root" │ wc -l

# Example B: Look up network socket data, filter out an active port, and inspect the tracking node
ss -tulpn │ grep ":80"
```

### More examples:
```bash
cat < file.txt (read the file and present the outout)
cat > file.txt (will open the cmd for input, this will be overwrite if > else append if >>)(ctrl + D to push/close)

man ls (open manual for ls command)

clear (ctrl + l) -> to clear the screen

cp /src/dir/file dest/folder (copy file)
mv /src/dir/file dest/folder (move file)
mv /src/dir/file.txt /src/dir/file2.txt (rename file)
cp -R /src/dir/. dest/folder (copy folder files recursively)

rm filename (remove file)
rm -rf dir (forcefully recursively remove dir)
rm -rf dir/prefix* (forcefully recursively remove files)
rmdir dir (remove only empty dir)
man rm (manual for rm command)

date (tells date)


find /path/to/search -name "file1.txt"
find . -name "file1.txt" (search in current dir, here some error like permission denied will come)
find . -name "file1.txt" 2> /dev/null (clean output, error will go to /dev/null)
file /home -mtime 7 2> /dev/null (file which got modified in last 7 days)

touch .file2.txt (create hidden file)
ls (does not show hidden files)
ls -al (show all files)

history (history for all commands in terminal -> Here we can see number before that command)
!CommandNumber (it will automatically re-run that command)
(ctrl + R => will open the terminal for reverse search, just type few characters from previous commands and it will show the latest one)

find /home -type f mtime +30 exec rm {}\; (find the file more than 30 days older with f type; once found then execute 'rm' command with prev's output as input here.) 


wc -l file.txt (word count but here -l shows count lines)
cat < file.txt | wc -l  (same as above, here pipe character (|) can be used for input-output bridge)
wc -c file.txt (word count but here -l shows count characters)


echo "msg1" (print the same output)
echo "msg1" > file.txt (dump in file)


ls -al image.png (check the size right after name)
(lets compress)
find ~/Desktop/ -type f -name "*.png" | xargs -n 1 -P 4 -I {} convert "{}" --size 100X100 "{}"
(Here -n 1 tells that take one file from pipe)
{-P 4 tells that 4 processors will run parallely}
du -sh file.png (provide the proper size)

(grep command is like ctrl + f in pdf/file search)
cat file.txt | grep "word" (will print the lines with exact match "word" -> case sensitive)
cat file.txt | grep -i "word" (will print the lines with exact match "word" -> ignore case sensitive)

ls | grep "mydir" (used to search the dir named "mydir")


ps aux (provide processes that are running on our system)
ps aux | head ("head' will provide the top 10 lines)
ps aux | awk '{print $2}' (will print the 2nd column)
ps aux | awk '{print $2}' | sort (will print the 2nd column in sorted way)

sudo su (make user root, to run 'cd /home/user1' while being in '/home/user2')
```
---
