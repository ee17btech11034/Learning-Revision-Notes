# Linux File Transfer and Security Notes

## 📁 File Transfer Mechanisms

### 1. SCP (Secure Copy Protocol)
* **Definition**: Non-interactive command-line utility that copies files securely over an SSH connection.
* **Enterprise Use Case**: Safely pushing configurations or scripts tested locally onto an internet-facing production server without breaking existing settings.
* **Limitation**: It requires you to know the exact path beforehand since it lacks an interactive navigation prompt.

```bash
# Upload a file from client to remote server home directory
scp file1.txt <remoteUser>@10.211.55.12:~/

# Download a configuration file from remote server to the present local directory
scp <remoteUser>@10.211.55.12:~/config.yml .

# Recursive Directory
scp -r folder/ user@host:/path/
```
> 💡 *Note: Ensure your targeted destination directory permissions match your logged-in username, otherwise you will hit a `Permission denied` error.*

---

### 2. SFTP (Secure File Transfer Protocol)
* **Definition**: An interactive shell environment that uses SSH under the hood to manage remote storage repositories safely.
* **Key Advantage**: Allows interactive terminal command executions like `ls` or `pwd` directly within the connection layout.

```bash
# to check configuration for sftp on remote
sudo cat /etc/group | grep -i sftp 

# group is not creatd  on remote machine then
sudo groupadd sftpusers (add group)
sudo useradd -m -G sftpusers -s /bin/bash sftpuser (to create user)
sudo passwd sftpuser (to set password)
sudo chown root:root /home/sftpuser
sudo chmod 755 /home/sftpuser
ls /home/sftpuser/ (must have a upload dir)
sudo chown sftpuser:sftpusers /home/sftpuser/uploads/
ls -al /home/sftpuser/uploads/
sudo systemctl restart ssh



# Connect to the remote SFTP Server
sftp <remoteUser>@10.211.55.12

# --- Inside the SFTP Interactive Shell Prompts ---
ls                          # View remote directory contents
lpwd # Prints the current active working directory directory path on your **local** workstation machine.
pwd  #Prints the current active structural folder directory location on the **remote** server node.
lls  #Lists all files and nested folder profiles residing inside your active **local** workstation window.
cd uploads                  # Change remote directories
get test.txt /home/user/dest                # Download file to your local machine
put /home/user/local_file.txt uploads/          # Upload file to your remote server
pwd
bye                         # Terminate the interactive session (or use 'exit')
```
> ⚠️ *Warning: SFTP locks files to the immediate directory permissions of the authenticating user context. If files with duplicate names already exist without write overrides, you must first rename them locally before running `put`.*

---

### 3. Rsync (Remote Sync)
* **Definition**: An advanced tool optimized for synchronizing both files and entire multi-level directories across local and remote paths.
* **Key Advantage**: Uses incremental lists to send only modified blocks or files, making it perfect for cloud updates or EC2 bulk storage uploads/downloads.

```bash
# Sync a single text file to a remote server
rsync another.txt <remoteUser>@10.211.55.12:~/

# Sync an entire directory with compression (-z), details (-v), and recursive archiving (-r)
rsync -rvis ./my_folder/ <remoteUser>@10.211.55.12:/home/star_agile/

# Sync/download a directory from a remote path to your current local layout
rsync <remoteUser>@10.211.55.12:/home/username/remote_dir/ .

# Sync local to remote
rsync -avz /local/dir/ user@host:/remote/dir/

# Mirror (Delete Source Extras)
rsync -avz --delete /local/dir/ user@host:/remote/dir/
```

---

## 🛡️ Linux Network Firewalls

### 1. UFW (Uncomplicated Firewall)
* **Definition**: A user-friendly front-end wrapper application designed to simplify basic Netfilter `iptables` rules management.

```bash
# Install the UFW package on Debian/Ubuntu systems
sudo apt install ufw

# Enable the firewall and ensure it persists on system reboots
sudo ufw enable

# Check firewall rules layout in highly descriptive/detailed mode
sudo ufw status
sudo ufw status verbose

# Block all incoming access connections trying to hit SSH port 22 globally
sudo ufw deny 22

# Allow structural web traffic targeting specific ecosystem service groups
sudo ufw allow "Apache Full" (We can accesse apache from anywhere)
sudo ufw allow ssh (check status before and after this command using 'utf ststus')

# Restrictively allow complete server entry solely to a single trusted IP target
sudo ufw allow from 192.168.1.50

# Allow a specific IP address access strictly to Port 80
sudo ufw allow from 192.168.1.100 to any port 80

# Enable built-in connection rate limiting on SSH to disrupt automated Brute Force attacks
sudo ufw limit ssh

# Delete specific existing rules easily by tracking their numerical list indexing
sudo ufw status numbered
sudo ufw delete 1

# Erase custom user variations and reset firewall defaults back to an inactive fallback state
sudo ufw reset
sudo ufw disable
```
> 💡 *Note: Always back up rule sets prior to issuing global resets in corporate network setups.*

---

### 2. IP Tables
* **Definition**: A complex, granular table system utilized to configure system-level network packet filtration, targets, and network rules.

```bash
# List all active rule chains mapped across current target systems
sudo iptables -L

# List all active configurations including verbose metric statistics and specific data ranges
sudo iptables -L -v

# Append an absolute incoming packet rule to reject all incoming TCP transactions hitting Port 23
sudo iptables -A INPUT -p tcp --dport 23 -j REJECT
sudo iptables -L -v -n | grep -i 22 (just to check the above commands working)

# Open default incoming access routes for public Web server Traffic on HTTP Port 80
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Accept connections dynamically that are already marked as RELATED or ESTABLISHED
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Droping all the connections
sudo iptables -P INPUT DROP (Do not do it, else how will you connect with this machine)

# Review current NAT (Network Address Translation) structural maps and rules
sudo iptables -t nat -L

# Redirect all traffic hitting Port 80 over to an alternative localized path (Port Forwarding)
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080

# Export running configurations directly out into a persistent local backup text block
sudo iptables-save > /tmp/firewall_rules.txt

# Restore system tables using a saved configuration rule file
sudo iptables-restore < /tmp/firewall_rules.txt

# show all the commands
sudo iptables

```

---

## ⚖️ Architectural Comparisons

| Attribute / Tool | **SCP** | **SFTP** | **Rsync** |
| :--- | :--- | :--- | :--- |
| **Interface Style** | Raw Command Line | Interactive Shell Prompt | Raw Command Line |
| **Primary Scope** | Static single file transfers | Interactive remote file/repo navigation | Syncing directories & changes |
| **Data Efficiency** | Standard linear block streaming | Standard interactive stream actions | Incremental delta block sync |

| Attribute / Tool | **UFW (Uncomplicated Firewall)** | **IP Tables** |
| :--- | :--- | :--- |
| **Operational Role** | High-level front-end application | Core low-level backend filter layout |
| **Rule Complexity** | Simple macro definitions (Service names/Ports) | Deep network manipulation (Mangle/NAT/States) |
| **Best Used For** | Quick system setups and simple server security | Complex routing and detailed enterprise network logic |
