# 📖 Linux Shell Scripting: Variables, Arguments & Custom Commands

---

## 1. System & Predefined Shell Variables
The Linux environment provides built-in global variables that store information about your system profile, path mappings, and session context.

### Essential System Variables
* **`$PWD`**: Holds the current active working directory path string.
* **`$RANDOM`**: Generates a pseudo-random integer ranging dynamically from `0` to `32,767` on each call.
* **`$PATH`**: A colon-separated list of system directories where executable files or binaries are located. If a script or file is dropped into one of these standard locations, it will run seamlessly as an independent shell command from anywhere in the system.
* **`$TERM`**: Identifies the currently active terminal emulation configuration (e.g., `xterm-256color`).
* **`$UID`**: Displays the unique Numeric User ID of the currently logged-in account (e.g., `1005`).
* **`$LANG`**: Indicates the active language settings, system keyboard configurations, and character encoding schemes (e.g., `en_US.UTF-8`).
* **`$HOME`**: Holds the absolute path pointing directly to the current user's default home folder space.

---

## 2. Variable Scope & Types
Variables inside Linux shell scripting are categorised into three primary architectural categories depending on their operational visibility and mutability rules.

### Local / Scalar Variables
* **Definition**: Volatile, local parameters that live strictly inside the current terminal session or execution thread where they were initialised.
* **Session Bound**: If you instantiate a scalar variable on one shell terminal, opening a new terminal window or child session completely drops its awareness. Exiting back to the original shell cleanly recovers access.
* **Naming Constraints**: Can safely consist of uppercase or lowercase letters (`A-Z`, `a-z`), digits (`0-9`), and underscores (`_`).
  * *Valid*: `_var1="test"`, `V_1="data"`, `USER_NAME="admin"`
  * *Invalid*: Cannot start with numerical digits or contain symbols like hyphens or exclamation points (`1var`, `var-1`, `var!`). These prompt a `command not found` syntax error from the shell parser.
* **Case Sensitivity**: Variable evaluations are strictly case-sensitive; `$var` and `$VAR` are parsed as entirely separate variables.

### Read-Only Variables
* **Definition**: Behaves like a locked configuration constant. Once declared and flagged as read-only, its assigned string value cannot be modified or updated during that terminal session.
* **Unset Restriction**: Read-only variables are permanently protected—they cannot be wiped out using the `unset` command. The session must be restarted or changed to drop them from local memory.
* **Syntax**:
  ```bash
  my_server="192.168.1.50"
  readonly my_server
  ```

### Environmental Variables
* **Definition**: Variables shared across child execution paths and different terminal execution sub-shells.
* **Export Action**: You use the `export` keyword to push a local variable description up into the active environment space.
* **Syntax**:
  ```bash
  export TEAM_LEAD="Himanshu" # we can access these in any shell in current environment (session created from it.
  ```

---

## 3. Advanced Special Variables Reference
Special variables extract process contexts, count variables, and check command executions on the fly.

| Special Variable | Description / Purpose |
| :--- | :--- |
| **`$0`** | Extracts and prints the actual script file filename being executed. |
| **`$1` to `$9`** | Evaluates specific operational command-line positional parameters sequentially. |
| **`$#`** | Returns the absolute count of arguments passed down to the running script. |
| **`$*`** | Combines all arguments cleanly into a single continuous text string line. |
| **`$@`** | Parses inputs individually, preserving distinct positional elements one by one. |
| **`$?`** | Captures the exit status code of the last completed command execution thread (`0` = Success, `Non-Zero` = Failure or Permission Error). |
```bash
#!/bin/bash
echo "Script Name: $0" # outputs the name of script
echo "First Arg: $1" # outputs the first argument
echo "Sec argument: $2" # outputs the second argument
echo "last argument: $n" # outputs the last argument
echo "Script Name: $#" # outputs the number of arguments.
echo "Exit status: $?" # prints the exit status of the last command. 0-> successful execution else failed

if [ $? -eq 0 ]; then
   echo "Successful"
else
   echo "Failed"
fi
```
```bash
./abc.sh arg1 arg2 arg3 arg4
```
---

## 4. Unsetting Variables
To explicitly drop a regular local variable and free up its allocated space from memory, use the `unset` command tool.

```bash
# Define a test variable
db_user="root"
echo $db_user

# Wipe the configuration variable from active tracking
unset db_user # not readonly vars
```

---

## 5. Creating Your Own Custom Shell Commands
You can write custom workflows or map complex administrative scripts to run as standalone system commands alongside native tools like `ls` or `pwd`.

### Step-by-Step Implementation Guide
1. **Write the core logic file** (e.g., creating a shorthand module called `mycmd` to automatically trigger detailed file audits):
   ```bash
   #!/bin/bash
   ls -al
   ```
2. **Apply global executable operational permissions**:
   ```bash
   chmod +x mycmd
   ```
3. **Move the operational file into a directory tracked by your `$PATH` mapping** (requires `sudo` administrative rights):
   ```bash
   sudo cp mycmd /usr/bin/
   ```
4. **Run your new tool directly** from any active directory path context:
   ```bash
   mycmd
   ```

---
