# Linux Text Editors & File Inspection Guide

A comprehensive technical reference manual for mastering terminal-based editing tools (Vim, Nano), graphical workspaces (Gedit), and low-level stream inspection utilities in Linux systems.

---

## 🏗️ 1. Core Operating Modes in Vim (Vi Improved)
Vim is a highly capable modal editor. Unlike standard text processors, keys have completely different functionalities depending on your active operating state.

*   **Command Mode**: The universal baseline state. Every keystroke is interpreted as a structural navigation shortcut, text-deletion directive, or internal macro. This is the default mode when a file loads.
*   **Insert Mode**: The raw text entry canvas. Keystrokes map directly to standard character insertions inside the file stream.
*   **Execution Mode (Last-line Mode)**: The system interface panel. Activated by typing a colon (`:`) from Command Mode, it drops your cursor to the lower-left terminal window frame to accept environments, search filters, and file-writing protocols.

```text
There are 3 types of mode:
1. Insert
2. Execution
3. Command

Whenever we open a file it is in command mode. 
To insert something we need to change mode to "insert" by pressing 
    (i, 
    a[capital A to go to last of line with going to insert mode],
    o[put the cursor on a new line created by it.]). 

Presss "esc" to go from insert to command mode.
Arrow keys to move cursor.
Shortcut for commnd mode (h (left), l(right), j(down), k(up), 0(zero for beginning of line), $(for end of line), w(jump to first character of next word), b(jump to first character of previous word), G(capital G -> to go last line of file), gg(2 times small g -> go to start of file))

undo changes (go to command mode, press 'u')
Search (press '/' and then type the word) in command mode.
copy-paste (press 'yy' to yanking the line, 'p' to paste in nxt line cursor is present) in cmd mode.
Word matches (press '/' and add pattern then enter; 'n' to go to next patter, shift+n to go to previous pattern)
last matching pattern (press '?' and then word)
'DD' to delete one line in cmd mode
'3DD'to delete 3 lines from cursor
'shift + Z' 2 times will save the file in cmd mode.
'10 then yy' to copy 10 lines (below cursor) 


press (:) to go to execution mode.
Now we can type commands we want to execute like 
':set nu' -> show the numbers of lines for the file 
':6' -> jump cursor to line number 6
':%s/word/word2/g' -> '%s' will select all the occurences of pattern 'word' and replace then with 'word2'
up & down key shows the previous commands in execution mode.
':%s/word/word2/gc' -> '%s' will select all the occurences of pattern 'word' and ask for confirmation 'c' and if press 'yes' then replace with 'word2'

':wq!' -> writing, saving and quit the file.
':q!' ->  quit the file without saving.
':e file2.txt' (to open file2 from vim of file1)
':w file3.txt' (to save the content of file1 to file3, ctrl+w to jump btw files).

':split file3.txt' (open file in split window format horizontally)
':vsplit file3.txt' (open file in split window format vertically)
'shft +z +q' to close this split file without saving changes.

':3,5s/^/#/' (line [3, 5], search (s), ^ tells to go to start of the line, replace with '#')
':3,5s/^He/#/' (line [3, 5], search (s), ^ tells to go to start of the line with 'He' as start character, replace with '#')

'3,5s/^/#/ | :1,2s/^#//' (multiple execution in single command)

+-----------------------------------------------------------+
|                    Command Mode                           |
+-----------------------------------------------------------+
        |            /|\         |         |         /|\    |
        |             |          |         |          |     |
Press i,a,o      Press Escape    |     Press :      ':wq'   |
       \|/            |          |        \|/         |     |
+--------------------------------+ | +----------------------+
|           Insert Mode          | | |    Execution Mode    |
+--------------------------------+ | +----------------------+
|
+--- Press v/V/Ctrl+V ---> [Visual/Block Mode]
```

---

## 📊 2. Vim Command Reference Matrix

| Operational Axis | Context / Mode | Syntax Key | Definitive Technical Outcome |
| :--- | :--- | :--- | :--- |
| **State Transitions** | Command → Insert | `i` | Drops into insert mode exactly at the current cursor position. |
| | Command → Insert | `a` | Enters insert mode one space right, appending text after the cursor. |
| | Command → Insert | `o` | Drops down, spawns a clean row below the cursor, and enters insert mode. |
| | Command → Insert | `I` | Instantly moves the cursor to the absolute start of the row and inserts. |
| | Command → Insert | `A` | Instantly moves the cursor to the absolute end of the row and appends. |
| | Command → Insert | `O` | Spawns a clean row directly above the cursor and enters insert mode. |
| | Any State → Command| `Escape` | Aborts current operational state and safely locks into Command Mode. |
| | Command → Execution| `:` | Drops line focal point down to parse administrative configuration scripts. |
| **Grid Navigation** | Command Mode | `h` / `j` / `k` / `l`| Standard directional mapping: Left (`h`), Down (`j`), Up (`k`), Right (`l`). |
| | Command Mode | `0` (Zero) | Snaps focus directly back to the absolute index 0 character of the line. |
| | Command Mode | `^` | Snaps focus to the first non-whitespace character on the current row. |
| | Command Mode | `$` | Snaps focus directly onto the terminating character of the active line. |
| | Command Mode | `w` | Advances cursor index forward to the first character of the next word. |
| | Command Mode | `b` | Shifts cursor index backward to the first character of the previous word. |
| | Command Mode | `gg` | Snaps line focal index to line 1 at the absolute top of the document. |
| | Command Mode | `G` | Snaps line focal index to the trailing terminal row of the entire file. |
| | Execution Mode | `:X` | Directly shifts terminal line cursor registry down to explicit row `X`. |
| **Text Modification**| Command Mode | `yy` | Yanks (copies) the structural layout of the active row into system cache.|
| | Command Mode | `p` | Pastes the contents of the yanked cache directory below the active row. |
| | Command Mode | `u` | Executes a linear state recovery, rolling back the last recorded edit action. |
| | Command Mode | `dd` | Completely excises (cuts) the active row out of the system document. |
| | Command Mode | `Xdd` | Excises `X` count of rows downwards from the active index (e.g., `3dd`). |
| **Find & Replace** | Command Mode | `/pattern` | Searches forward through the active directory file for a specific query. |
| | Command Mode | `?pattern` | Searches backward through the active directory file for a specific query. |
| | Command Mode | `n` | Traverses forward to locate the next chronological match entry. |
| | Command Mode | `N` | Traverses backward to locate the previous chronological match entry. |
| | Execution Mode | `:%s/A/B/g` | Scans structural canvas globally; changes every occurrence of `A` to `B`. |
| | Execution Mode | `:%s/A/B/gc`| Scans globally; initiates an individual interactive verification prompt (`y/n`).|
| | Execution Mode | `:X,Ys/A/B/g`| Constrains the scope of search and replace exclusively between rows `X` and `Y`.|
| **Buffer Maintenance**| Execution Mode | `:set number` | Forces Vim wrapper to paint literal sequence indices on the left track.|
| | Execution Mode | `:e filename` | Suspends active buffer layout and reads a secondary text document inline. |
| | Execution Mode | `:w filename` | Clones or outputs active working text block into an isolated target file.|
| | Execution Mode | `:wq!` | Forces raw compilation write to hardware disk architecture and exits. |
| | Execution Mode | `:q!` | Halts background buffer instantly, completely discarding unsaved edits. |
| | Command Mode | `ZZ` | Direct micro-shortcut sequence to write modified file and exit buffer. |
| | Command Mode | `ZQ` | Direct micro-shortcut sequence to abandon mutations and kill editor. |
| **Workspace Splits** | Execution Mode | `:split file` | Splits editor view horizontally to handle secondary data streams concurrently.|
| | Execution Mode | `:vsplit file`| Splits editor view vertically to manage files side-by-side. |
| | Command Mode | `Ctrl+w+w` | Toggles interface keyboard control focus between active window panels. |

---

## 📝 3. Nano & Gedit Workspace Overview

### Nano Text Editor
An explicit, terminal-bound utility optimized for quick runtime configuration updates without modal management context.

*   **Operation Summary**: Commands are issued using the static control wrapper layout mapped permanently to the bottom margin of the workspace interface.
*   **Primary System Operations**:
    *   `Ctrl + O` (WriteOut): Forces compilation of runtime data layout onto disk architecture.
    *   `Ctrl + X` (Exit): Terminates active editing frame session to slide back to shell terminal.

### Gedit Workspace utility
A text editing wrapper utility designed explicitly for graphical subsystem interfaces (GUI), behaving similarly to traditional desktop notepad environments.

*   **Operation Summary**: Designed natively for direct pointer interactions, desktop highlight schemas, and predictable global shortcuts like `Ctrl + S` for save actions. 
*   **Target Application**: Ideal toolset for engineers validating configurations through GUI environments while making a gradual transition over to native headless Linux CLI environments.

---

## 🔍 4. Advanced Stream Inspection & File Traversal

When operating within professional Linux architectures, evaluating massive runtime data logs using text editors can exhaust local system memory. Use specialized stream manipulation tools to isolate target rows directly inside the shell terminal.

### Vertical Slice Boundaries (`head` & `tail`)
*   **`head -n X [target_path]`**: Pulls down and reviews strictly the first `X` metadata entries starting directly from line index 1.
*   **`tail -n X [target_path]`**: Pulls down and reviews strictly the concluding `X` records up to the exact end of file marker.
*   **Piped Slicing Segments**: Pipe operator processing patterns can link utilities together to inspect precise rows hidden deep within text blocks:
    ```bash
    tail -n 30 trace_system.log | head -n 5
    ```
    *Isolates the final 30 rows generated within the structural tracking log, then passes that stream payload directly into head to print out the first 5 records of that slice.*

### Paged Screen Navigation (`less` & `more`)
*   **`more [target_path]`**: Loads and delivers static file arrays using percentage-based rendering blocks. It drops down in quick screen-sized blocks as you progress through the document.
*   **`less [target_path]`**: A highly efficient paging reader utility that loads content on-demand without buffering the entire document into system memory. Supports standard search keys (`/`) and explicit row traversal using navigation buttons.
*   **`less +X [target_path]`**: Bypasses the default introductory file tracks to initialize view perspective precisely on line integer position `X`.
*   **`less -p "error_string" [target_path]`**: Automatically parsing optimization flag that instructs the reader wrapper to skip matching records and lock viewing focus right onto the initial highlighted index matching your keyword patterns.

### Dynamic Real-Time Stream Tracking
*   **`tail -f [target_path]`**: Binds standard terminal system outputs tightly to live hardware file write requests. This operational command allows engineers to monitor active application servers as they log real-time diagnostics.
    ```bash
    tail -f /var/log/apache2/access.log
    ```
    *Tracks real-time web server activity, enabling immediate validation of client request formats, tracking HTTP operational response codes, and diagnosing ongoing configuration issues. Terminate continuous stream tracking by passing an interrupt signal via `Ctrl + C` to clear the operational workspace prompt.*

### More Commands:

```text
cmd > nano file.txt (to open file in nano editor)
```

```bash
less file.txt (first 10 lines of file, then use arrow keys to scroll line by line)
less +22 file.txt (start printing from line number 22)

man less (for manual)

head -n 10 file.txt (provide only top 10 lines)
tail -10 file.txt (provide only bottom 10 lines)

tail -30 file.txt | head -5 (choose last 30 lines then out of those choose top 5)

more file.txt (shows the % of file showed with currently visiblt, arrow key takes to chunks)

less -p "word' file.txt (open the file with pattern 'word' highlighted)

(tail command just shows output and closes, but I want that to capture real time like if updated then update the output as well)
tail -f log_file.txt (this will do the work)

tail -f /var/log/apache2/access.log (search something in firefox, see; ctrl+c to exit)

grep 'word' file.txt | less
```
