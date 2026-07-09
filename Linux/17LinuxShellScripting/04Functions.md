# 📖 Linux Shell Scripting: Functions and Practical SysAdmin Use Cases

Detailed study notes and script templates based on https://www.youtube.com/watch?v=_N8w7bIAcrc&list=PLMyATy-xvDAiP5EbC1KluG1sFNuroLsXR&index=6.

---

## 1. Introduction to Functions in Shell Scripting
A **function** is a block of reusable code designed to perform a specific task. Instead of writing identical sequences of commands multiple times throughout a script, you encapsulate the logic inside a function block and call it whenever needed. This makes scripts modular, clean, efficient, and easier to debug.

### Basic Structure and Syntax
A function is defined by its name followed by open/close parentheses `()` and curly braces `{}` which wrap the code block.

```bash
#!/bin/bash
# 1. Define the function
function_name() {
    # Commands to execute
    echo "Hello $1, Executing function logic"
}

# 2. Call the function by its name
function_name "world"
```

---

## 2. Core Function Types and Demos

### A. Basic Functions with Arguments
Functions inside scripts accept input values via **positional arguments**. Within the function block, these inputs are referenced sequentially using `$1`, `$2`, `$3`, etc.

```bash
#!/bin/bash
# Definition of a greeting helper
greet() {
    # \$1 captures the first argument passed specifically to this function
    echo "Hello, \$1"
}

# Invoking the module with distinct string properties
greet "World"    # Output: Hello, World
greet "Himanshu" # Output: Hello, Himanshu
```

### B. Functions with Return Values & Exit Codes
In Bash scripting, the `return` keyword passes an **exit status integer** (ranging from `0` to `255`) back to the parent execution thread. To retrieve the outcome of the immediate last executed statement, evaluate the special variable `$?`.

```bash
#!/bin/bash
add_numbers() {
    # Arithmetic evaluation context inside double brackets
    result=\$(( \$1 + \$2 ))
    return \$result
}

# Triggering the calculation block
add_numbers 5 3

# Capture and print the returned evaluation state code (\$?)
echo "The sum is: \$?"
echo "The sum is: $result?"
echo (add_numbers(5 3))
```
*Note: If your numeric output naturally scales past `255`, assign the logic to local parameters or echo the data stream inside a variable expansion subshell instead.*

### C. Function Tracking Scope (Local Variables)
Variables declared normally inside a function default to global visibility across the entire script context. To prevent a function from overwriting outside variables, restrict its scope using the `local` flag keyword.

```bash
#!/bin/bash
multiply() {
    # Explicitly declared internal local scoping constraint
    local product=\$(( \$1 * \$2 ))
    echo "Multiplication Result: \$product"
}

system_info() {
    echo "Hostname: $(hostname)"
    echo "Uptime: $(uptime)"
    echo "Free Memory: $(free -h)"
}
multiply 5 6
system_info
```

### D. Advanced Recursive Mechanics (Factorial Script)
Functions can iteratively loop back or invoke themselves to evaluate branching or cascading algorithms, such as mathematical factorials.

```bash
#!/bin/bash
# Recursive algorithm pattern mapping
factorial() {
    local num=\$1
    if [ \$num -le 1 ]; then
        echo 1
    else
        # Self-referencing subshell calculation branch
        local local_prev=\$(( num - 1 ))
        local prev_fact=(factorial local_prev)
        echo \$(( num * prev_fact ))
    fi
}

# Combined runtime prompt parameter validation logic
read -p "Enter a number to calculate its factorial: " target_num

if [ \$target_num -lt 0 ]; then
    echo "Factorial is undefined for negative values."
else
    res=(factorial target_num)
    echo "Factorial of \(target_num is:\)res"
fi
```

### E. Structuring Functions with Error Handling
You can build error verification mechanisms inside functions to cleanly validate system state paths before running risky modifications.

```bash
#!/bin/bash
check_file() {
    local target_path=\$1
    # Check if the target object exists inside the file system space
    if [ -e "\$target_path" ]; then
        echo "Success: File [\$target_path] exists."
    else
        echo "Error: File [\$target_path] cannot be located."
    fi
}

# Validation testing sweeps
check_file "/etc/passwd"
check_file "/etc/non_existing_file"
```

---

## 3. Real-World Practical Automation Use Cases
These practical tools are used by DevOps engineers and System Administrators to eliminate repetitive daily maintenance workflows.

### Use Case 1: Automated Old Log Archiving
Finds and packs log tracking streams that are older than 30 days into compact `.tar.gz` packages to prevent disk space consumption.

```bash
#!/bin/bash
# Archiving automated maintenance routine
SRC_LOG_DIR="/var/log"
ARCHIVE_DEST="/var/log/archive"

# Find targets matching extensions older than 30 days and pass to tar
find "\$SRC_LOG_DIR" -type f -name "*.log" -mtime +30 -exec tar -cvzf "\(ARCHIVE_DEST/log_backup_\)(date +%F).tar.gz" {} +
```

### Use Case 2: Auto-Cleaning Temporary File Dumps
Maintains host stability by clearing old files out of public workspace partitions.

```bash
#!/bin/bash
# Deletes files inside the /tmp directory that haven't been modified in over 7 days
find /tmp -type f -mtime +7 -exec rm -f {} \;
```

### Use Case 3: Storage Monitoring Threshold & Mail Alerts
Continuously checks server storage space allocations and sends a warning if usage passes a configured limit.

```bash
#!/bin/bash
# Disk allocation reporting monitor script
THRESHOLD=90
# Extract the active percentage of the root directory partition space
CURRENT_USAGE=\$(df / | awk 'NR==2 {print \$5}' | sed 's/%//')

if [ "\(CURRENT_USAGE" -gt "\)THRESHOLD" ]; then
    echo "Warning: Disk usage has exceeded the safe limit. Active space use: \$CURRENT_USAGE%" | mail -s "Disk Space Alert!" admin@company.com
else
    echo "Storage check complete. Disk space is at nominal levels (\$CURRENT_USAGE%)."
fi
```

### Use Case 4: Bulk User Multi-Account Provisioning
Automates onboarding by reading user names from an external text file and setting up their accounts instantly.

```bash
#!/bin/bash
# Mass account provisioner script module
USER_DATA_FILE="users.txt"

if [ ! -f "\$USER_DATA_FILE" ]; then
    echo "Data file \$USER_DATA_FILE missing."
    exit 1
fi

while read -r username; do
    if [ -n "\$username" ]; then
        useradd -m "\$username"
        echo "User [\$username] configured successfully."
    fi
done < "\$USER_DATA_FILE"
```

---

## 4. Converting Local Scripts into System-Wide Binaries
To run any of your custom automated scripts seamlessly from any working path (like native system binaries such as `pwd` or `ls`), add them to the system binary directory.

```bash
# 1. Give the automated logic script file global execution bits
chmod +x factorial.sh

# 2. Copy the file into the primary system binary execution path location
sudo cp factorial.sh /usr/bin/factorial

# 3. Test execution instantly from anywhere on the host environment
factorial
```

## Scripts for Automation
### 1. File and Directory Management
* **Archiving and compressing old log files** 
```bash
#!/bin/bash
#Archive logs older than 7 days
find /var/log/myapp -type f -mtime +7 -exec tar -rvf old_logs.tar {} \;
gzip old_logs.tar
echo "Archived old logs"
```

* **Automatically clean up temporary files** 
```bash
#!/bin/bash
# Remove temporary files older than 2 days
find /tmp -type f -mtime +2 -exec -f {} \;
echo "Temporary files cleaned up"
```

### 2. System Monitoring & Reporting
* **Disk space usage monitoring**
```bash
#!/bin/bash
# check disk usage & send email alert if usage exceeds 80%
THRESOLD=80
df -h | awk '$5 > THRESOLD {print $1 " is above " THRESOLD "%" }'
```

* **Automating server uptime checks**
```bash
#!/bin/bash
# Ping server and log uptime
SERVER="example.com"
if ping -c l $SERVER &> /dev/null; then
    echo "$(date): $SERVER is up" >> uptime.log
else
    echo "$(date): $SERVER is down" >> uptime.log
fi
```

### 3. User Management & Security
* **Creating multiple user accounts from a file**
```bash
#!/bin/bash
# Add users from a text file
while IFS=, read -r username password; do
    useradd $username
    echo $password | passwd --stdin $username
done < users.csv
echo "Users added"
```

* **Automating Backups**
```bash
#!/bin/bash
# backup important files to a remote server
rsync -avz /home/user/data user@backupserver:/backup/data
echo "Backup Completed"
```