# 📖 Linux Shell Scripting: Introduction & Prompt Customization

Detailed study notes and command references.

---

## 1. Understanding the Shell
A **shell** is a command language interpreter that acts as an interface between the user and the Linux kernel. It reads commands typed by the user, translates them for the kernel, and outputs the result.

### Common Types of Shells
### Common Types of Shells
* **Bourne Shell (`sh`)**: The historical standard shell created by Stephen Bourne at AT&T Bell Labs. Standard prompt symbol: `$`.
* **GNU Bourne-Again Shell (`bash`)**: An enhanced, modern evolution of `sh`. It is the default shell for most modern Linux distributions and supports color-coded file tracking.
* **C Shell (`csh` / `tcsh`)**: Uses a syntax that closely resembles the C programming language. Standard prompt symbol: `%`.
* **Korn Shell (`ksh`)**: Combines the best features of both `sh` and `csh`.
* **Z Shell (`zsh`)**: An advanced shell layer featuring advanced auto-completion, native Git configuration integration, and theme engines.

---

## 2. Shell Scripting Fundamentals
A shell script is a plain text file containing a structured sequence of Linux commands executed sequentially, line-by-line, by the shell interpreter.

### Core Structure Elements
* **The Shebang (`#!`)**: Must always occupy the absolute first line of your script. It tells the kernel which explicit interpreter binary to pull to process the file (e.g., `#!/bin/bash`).
* **Comments (`#`)**: Any line starting with a `#` (excluding the shebang line) is treated as a comment and skipped during execution.
* **File Suffix (`.sh`)**: Used as a best-practice convention to let system administrators easily identify script files.

### Creating and Executing a Script

1. **Write the Script**: Create a file named `basic_script.sh` containing valid commands:
   ```bash
   #!/bin/bash
   # Prints the current directory path and lists out files
   pwd
   ls
   ```

2. **Execute via Explicit Interpreter**:
   ```bash
   bash basic_script.sh
   # Or using the older shell binary:
   sh basic_script.sh
   ```

3. **Make it Executable (Standalone Execution)**:
   By default, newly created text files lack executable permissions (`permission denied` error). Use `chmod` to add the execution bit:
   ```bash
   # Add execute permissions
   chmod +x basic_script.sh

   # Execute directly from your current path
   ./basic_script.sh
   ```

---

## 3. Basic Script Commands & Variables
* **`echo`**: Outputs text strings or system variables directly to the standard terminal output window.
* **`read`**: Pauses script execution to grab real-time user input from the keyboard and assigns it to a variable string.
* **`$` (Variable Evaluator)**: Placed before a variable identifier to retrieve or evaluate its stored value.

### Practical Script Example (`script.sh`)
```bash
#!/bin/bash
echo "What is your name?"
read person
echo "Hello, \$person!"
```

---

## 4. Shell Prompt Customization (PS1 & PS2)
Linux allows you to completely customize the text configurations, metadata indicators, and structural formatting of your terminal environment prompts.

### Primary Prompt String (`PS1`)
The environment variable `PS1` governs your primary interactive terminal command line interface string.

* **Temporary Configuration Change** (Resets cleanly back to defaults upon session exit):
  ```bash
  PS1="[Custom Shell Code] \$ "
  ```
* **Persistent Configuration Change**: 
  To make changes permanent, append your custom `PS1` string definitions directly into your home path configuration profile file (`~/.bashrc`) and reload the environment:
  ```bash
  # Open and edit ~/.bashrc with an editor, append the definition, then run:
  source ~/.bashrc
  ```

#### Standard Escape Sequence Flags

| Escape Sequence | Description | Example Live Output |
| :--- | :--- | :--- |
| `\u` | Displays the current logged-in user name | `staragile` |
| `\h` | Displays the default host network name | `linux-node` |
| `\w` | Displays the absolute full current working directory path | `/home/staragile/shell` |
| `\W` | Displays the basename of the current folder context only | `shell` |
| `\t` | Displays the active execution time (HH:MM:SS format) | `15:30:45` |
| `\d` | Displays the static calendar date (Weekday Month Day) | `Mon Jan 28` |
| `\!` | Displays the active incremental position item in system history | `602` |

### Secondary Prompt String (`PS2`)
The environment variable `PS2` configures the multi-line continuum prompt character string. This prompt appears if you press Enter before completing a matching command block constraint structure (e.g., leaving a quotation string open across lines).

```bash
# Customizing the active multi-line input prompt representation
PS2="Waiting for closing quote > "
```

---

## 5. Closely Related Technical Extensions
To help you advance, here are key foundational scripting concepts that build on this lesson:

### One-Line Execution Operators
Instead of building a script file for every sequence, you can join standard operations directly onto a single execution line:
* **Semicolon (`;`)**: Forces linear command execution sequences regardless of whether previous tasks pass or fail.
* **Logical AND (`&&`)**: Executes the trailing command *only* if the preceding command returns a clean exit status of `0`.
* **Logical OR (`||`)**: Executes the trailing task statement sequence *only* if the leading command fails.

### Dynamic Positional Parameters
Instead of forcing interactive scripts to pause for a keyboard response via `read`, you can pass arguments directly into shell modules when invoking them:
* **`$1, $2, ... $N`**: Locational variables string values matched directly to arguments ordered sequentially after the script name.
* **`$#`**: Automatically returns an integer tracking the count of parameters parsed into the module run context.
* **`$?`**: Captures the exact return validation integer flag code of the most recently evaluated execution thread (`0` signals complete operational success).

## More:
```bash
bash # to open a new session check using history
sh # also does same as bash but does not provide PS1, check file vim ~/.bashrc
exit # exit from the session

$`data`
data # both provide the same 

PS1='==>' # we can change PS1 temporary but not in rc file. new shell and its gone.
PS1='[\u@\h \t \w]\$' #username@hostname time workingdir
PS1='[\u@\h \d]\$' # date
PS1='[\u---> \d]\$' # date
# \W -> absolute path to working dir
# \w -> relative path to working dir
# \# -> command number/index
# \$ => if it is root then it will tern as # or $

hiostname -I # provide IP, MAC addresses


# when we make changes in bashrc file 
vim ~/.bashrc
# these changes will reflect if we reboot the machine, create new session. But if we want to refresh current session then
source ~/.bashrc
echo $PS1


## PS2 -> secondary prompt
# echo "sdnfnvl 
# do not close this with " then it will open for secondary prompt, until you type "
```