# Linux User and Group Management

## 🧑‍💻 User Identification Commands

* `whoami`: Displays the username of the currently logged-in shell user.
* `echo $USER`: Outputs the current user environment variable.
* `id [username]`: Displays the unique User ID (UID), primary Group ID (GID), and all secondary groups for a specific user.

---

## ⚙️ User Account Management

### Adding a User
* **Command**: `sudo adduser <username>`
* **System Actions**:
  * Allocates a UID and GID greater than `1000` (the standard range for human users).
  * Automatically creates a primary group matching the username.
  * Creates a dedicated home directory under `/home/<username>`.
  * Copies hidden configuration profile templates from the skeleton directory (`/etc/skel`).
  * Prompts for a secure password, full name, and optional contact details.

### Modifying User Attributes (`usermod`)
* **Assign Secondary Group**: `sudo usermod -aG <group_name> <username>`
  * *Important*: The `-a` (append) flag is critical to prevent overwriting existing secondary groups.
* **Lock a User Account**: `sudo usermod -L <username>` (Disables password authentication).
* **Unlock a User Account**: `sudo usermod -U <username>` (Re-enables password access).

### Deleting a User
* **Standard Safe Delete**: `sudo deluser <username>` (Removes user from system databases but leaves their files intact).
* **Complete Purge**: `sudo deluser --remove-home <username>` (Deletes the account along with their entire home directory structure).

---

## 🔒 Group Account Management

### Key Concepts
* **Primary Group**: The main group associated with a user. Every file or folder created by the user is automatically assigned to this group ownership. A user can only have **one** primary group because whenever user creates a file/dir then it assign to primary group so this must be one.
* **Secondary Group**: Supplemental groups assigned to provide extended file access permissions. A user can belong to **multiple** secondary groups.

### Group Administration Commands
* **Create a Group**: `sudo addgroup <group_name>`
* **Delete a Group**: `sudo delgroup <group_name>`
* **Check User's Groups**: `groups <username>`
* **Add User to Group**: `sudo gpasswd -a <username> <group_name>` (Alternative, direct approach).
* **Remove User from Group**: `sudo gpasswd -d <username> <group_name>` (Safely detaches a user from secondary permissions).

---

## 🛡️ Administrative and Security Operations

### Granting Privileges (`sudo`)
* **Ubuntu / Debian**: `sudo usermod -aG sudo <username>`
* **CentOS / RHEL / Fedora**: `sudo usermod -aG wheel <username>`

### Password Aging policies (`chage`)
* **Force Password Change**: `sudo chage -d 0 <username>` (Triggers a mandatory password update on their next login session).
* **Set Expiration Window**: `sudo chage -M 90 <username>` (Sets maximum password lifetime validity to 90 days).
* **Audit Expiry Metrics**: `sudo chage -l <username>` (Prints comprehensive credential security lifespans).

### Switching User Environments
* **Full Shell Switch**: `su - <username>` (Switches to target user while completely loading their profile, pathing, and configuration environment).
* **Target Execution**: `sudo -u <username> <command>` (Runs a single discrete action mapping as the specified target user context).

---

## 📂 System Configuration Files

Linux tracks all user identity properties inside plain text files under the root `/etc` directory:

| Configuration File | System Purpose | Format Description |
| :--- | :--- | :--- |
| `/etc/passwd` | Contains general human-readable user account registry information. | `username:password_placeholder(x):UID:GID:User_Info:Home_Directory:Default_Shell` |
| `/etc/shadow` | Securely stores encrypted password hashes, salting strings, and account expiration properties. Only readable by root. | `username:salted_hash_value:last_change:min_days:max_days:warn_days` |
| `/etc/group` | Defines system security groups and explicitly maps secondary member lists. | `group_name:password_placeholder:GID:secondary_user_list` |
| `/etc/login.defs` | Establishes shadow suite system-wide parameters (e.g., Min/Max UID limits, password age alerts). | Key-value mapping for dynamic configurations. |
| `/etc/skel` | Holds template hidden dotfiles (`.bashrc`, `.profile`) used to provision freshly built home directories. | Hidden structural profile shell scripts. |

---

## ⚠️ Core Differences: `adduser` vs `useradd`

* **`adduser` (Recommended)**: A high-level, interactive Perl script wrapper. It configures the home workspace directory, prompts for a password, and copies custom environmental skeletons automatically.
* **`useradd` (Legacy/Low-Level)**: A raw system binary utilities execution file. It will **not** create a home directory or configure terminal profile dynamics by default unless complex manual flags (`-m -s /bin/bash`) are provided explicitly.

---

## 🛠️ Advanced Operations Filter Example

To quickly review real human users on a system without opening complete configuration files, use the `awk` command to print names alongside UIDs and GIDs:

```bash
awk -F: '\$3 >= 1000 && \$3 <= 60000 {print \$1 ", UID: " \$3 " - GID: " \$4}' /etc/passwd
```

## More Commands:
```bash
whoami 
echo $USER (same as whoami)

sudo adduser user4 (create new user 'user4'-> check the cmd output  UID/GID are important)(whenever we create user then group also gets created with same name as user can not exist with group)('/etc/skel' has skeleton for files)

vim /etc/passwd (can be used to check the user lists)
sudo vim /etc/shadow (can be used to check user-> It is seperated with '$', like salt, and password hash value, validation year, warning for days, etc)

vim password_check.sh (We can create this file or python file to check the password by providing the salf, hash, etc.)
./password_check.sh (can execute if 'x' is there in the end)

echo $SHELL (can find the shell for current user)

cat .bash_logout (run when user logsout)
cat .profile ('Path' is binary files path)
echo $PATH (can see all paths)
cat .bashrc (it has alias, with colors; need to edit here for permanent else it will temp, reboot and gone; PS1 is the cmd's left cmd portion 'user@...' we can edit this as well)

exit (log out user)
su - user4 (log in)

cat .bash_history (show history)
history
history -c (to clean the history but does not clean from .bash_history)

ls -al /etc/skel/ (it has template for 3 files, .bash_logout, .bashrc, .profile)

sudo deluser user4 (delete user)(check passws, shadow file)(explore options for this command using 'man deluser'; home dir does not remove)

sudo deluser --remove-home user4 (home dir removed now)

```

```text
UID/GID (User/group ID):
ID: 0            ==> always assigned to root user
ID: 1 -> 999     ==> alloted to system user like DNS masq, apache servers, etc.
ID: 1001 ->  (16k to 60k)   ==> Normal user (max depend on system 32/64 bit 'vim /etc/login.defs')
ID: (16k to 6k) -> ==> Manually we can assign.
```

```bash
vim /etc/login.defs

awk -F: '$3 >=1000 && $3 < 65534 {print $1}' /etc/passwd ('-F' is used to set the delimeter, to fetch the data)(read /etc/passwd file, print the first col but only if 3rd col is in the range, ':' is delimeter which is defined in file to seperate entries in a single row -> find the col)

awk -F: '$3 >=1000 && $3 < 65534 {print $1", "$3"-"$4}' /etc/passwd (print col 1, 3, 4)

vim /etc/group (this file contains groups)

group user1 (to check the users)
sudo usermod -aG user3 user1 
vim /etc/group (user3: x: GID: user1)(user1 is added in the list )(user3 is the secondary gp for user1)

sudo addgroup random (adding group named 'random')

sudo usermod -L user1 (This lock the user and user has 7 days, else it will delete the user.)

sudo usermod -U user1 (to unlock the user)

sudo delgroup random (delete group named 'random')

id user1 (tells the uid, GID)

sudo passwd -S user1 (password details like limit)

man passwd (type '/' to search in manual)

sudo useradd test1 (it is older command which does not create home dir)(not a good idea)
sudo su - test1 (can switch the user but no home dir so no use.)
whoami (tell test1)
ls -al (to check the files like skeleton files)
sudo cp -r /etc/skel/.* /home/test1 (need to add if we use above command)
sudo useradd -m -s /bin/bash test1 (need to add this also if using above command)

sudo adduser user4 (it is new and better command to add user)


sudo adduser --ingroup usergp1 user3 (creating user as 'user3' but primary group is existing gp 'usergp1')
groups user3 (to check all the gps)
```