# Secure Shell (SSH) & Security Hardening Guide (Part 2)

This reference document outlines the implementation, execution parameters, and security profiles for establishing secure remote connections via SSH.

---

## 🔑 Secure Shell (SSH) & Remote Login

Secure Shell (SSH) provides an encrypted cryptographic network channel for administering remote systems, operating natively over destination **Port 22**. SSH provides a facility to users to connect to remote via secure way/tunnel.
```bash
sudo apt install openssh-server (install ssh)
```

### 🔒 Server Hardening (`/etc/ssh/sshd_config`)
To secure enterprise environments against malicious automated discovery attacks, open `/etc/ssh/sshd_config` and adjust the configuration parameters as follows:

```ini
# Disable direct administrative root logins
# (Forces administrators to log in using an unprivileged user profile before running higher commands)
PermitRootLogin no

# Enable cryptographic public key authentication
# (Permits authentication checking via matching public/private digital key configurations)
PubkeyAuthentication yes

# Optional: Disable fallback password authentication
# (Blocks brute-force attempts by rejecting basic standard string passkeys globally)
PasswordAuthentication no
```
*Note: You must restart the runtime daemon module engine to read and enforce configuration profile adjustments.*

### 🎮 Managing the SSH Service
* **Check SSH Status:** (Queries systemd to verify the remote access daemon is actively running and watching for user connection hits)
  ```bash
  systemctl status ssh (can use sudo)
  ```
* **Restart SSH Daemon Process:** (Triggers a quick shutdown and reboot sequence of the server listener to safely apply newly modified configuration values)
  ```bash
  sudo systemctl start ssh
  sudo systemctl restart ssh
  ```
* **Persistent Boot Enable:** (Configures a symlink mapping in systemd to ensure the SSH service automatically launches following an uncontrolled machine reboot cycle)
  ```bash
  sudo systemctl enable ssh
  # if not enabled then setting will vanish as we reboot
  ```

### 🗝️ Key-Based Authentication Deployment
Eliminate vulnerable cleartext password handling routines entirely by setting up asymmetrical cryptographic key pairs.

1. **Generate Cryptographic RSA Key-Pair:** (Creates a complex mathematical validation token pair)
   ```bash
   # "-t rsa": Specifies the Rivest–Shamir–Adleman data encryption algorithm
   # "-b 4096": Explicitly defines a heavy 4096-bit key length matrix for high computational safety
   # "-C": Injects an identifiable descriptive text metadata comment tag string onto the tail of the key
   ssh-keygen -t rsa -b 4096 -C "admin@company.com"
   ```
   * *Private Key Path:* `~/.ssh/id_rsa` *(Your absolute digital identification token—never share this or transfer it from your local laptop!)*
   * *Public Key Path:* `~/.ssh/id_rsa.pub` *(The public anchor file deployed cleanly onto all external servers)*

2. **Deploy Public Key to Target Server:** (Automates logging into a target remote point and safely inserting your authentication token string)
   ```bash
   # "-i": Target flag pointing explicitly to your local system public verification file path
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote_host_ip
   ```
   *This appends your raw key string into the remote system's master file template path at `~/.ssh/authorized_keys`.*

### 🛰️ Remote Execution & Session Monitoring
* **Establish Remote Terminal Shell:** (Authenticates your identity and drops you into a remote, secure interactive bash subsystem)
  ```bash
  ssh user@remote_host_ip
  ```
* **One-Off Command Execution:** (Runs a process on a remote asset node and relays output data streams locally without spawning a persistent terminal console)
  ```bash
  # 'ls -la /var/www/html': The isolated terminal instruction processed remotely
  ssh user@remote_host_ip 'ls -la /var/www/html'
  ```
* **Monitor Active Shell Sessions:** (Prints connected tty console IDs, background processing runtimes, and incoming telemetry source locations for tracking users)
  ```bash
  w ('w' is used by itself, it is self-contained builtin linux binary)
  w <username> (shows the user)
  ```

### More commands:

- **SSH into the Remote Machine:** Steps to connect to remote machines

 ```bash
 # Step 1. Find Ip address of remote machine
 # Go to monitor we want to connect to and run
 ip a


 # Step 2. Login from different machine
 # Use ssh commands to log in.
 ssh <userName>@<Ip> (remote username and ip)
 ssh raj@192.168.1.10

 # Step 3. Accept the Key Fingerprint
 # On the first login, SSh will ask to verify the remote machine's fingerprint. Type 'yes' to proceed.

 # Step 4. Enter a Password
 # You will be prompted for the password of the user  account on the remote machine.
 ```

- **Using SSH Keys:**
 ```bash
 # Step 1. Generate an SSH KEY pair
 ssh-keygen -t ras -b 4096 -C "<emailaddress>"
 #save the key (default loc is ~/.ssh/id_rsa); if ext is .pub means it is public key

 # Step 2. Copy yhe pubic key to the remote machine
 # Use the ssh-copy-id command to copy the public key
 ssh-copy-id <username>@<IP>

 # Step 3. Login without password
 # After copying the key, we can login without password 
 ssh <username>@<IP>
 ``` 

 - **Common SSh Commands:** 
 ```bash
 #Execute command remotely
 ssh <username>@<ip> "ls -al"

 # Copying file between machines (local and remote)
 scp /path/to/localfile <username>@<ip>:/path/to/destination
 scp <username>@<ip>:/path/to/file /path/to/destination


 # Forward Ports 
 ssh -L 8080:localhost:80 <username>@<ip> #(forward local port 8080 to a remote web service)

 # Press Exit or (ctrl + D) to terminate SSH session.
 exit
 ```
 - **More Commands:**
 ```bash
 sudo system 

 sudo vim /etc/ssh/sshd_config (default file for ssh configuration, read this file and its all parts.)
 sudo vim ~/.ssh/authorized_keys (public key)

 sudo ufw allow ssh (for firewall)
 ```