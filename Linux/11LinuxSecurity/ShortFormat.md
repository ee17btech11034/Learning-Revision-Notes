# Linux File Transmission & Firewall Security Management

A reference guide for securely transferring data (SCP, SFTP, rsync) and managing firewalls (UFW, iptables) on Linux.

## 📦 Part 1: Secure File Transfer
*   **SCP (Secure Copy):** Fast, non-interactive secure file transfer.
    *   *Upload:* `scp local_file user@host:/path/`
    *   *Download:* `scp user@host:/path/file ./`
    *   *Recursive Directory:* `scp -r folder/ user@host:/path/`
*   **SFTP:** Interactive session for remote file management.
    *   *Connect:* `sftp user@host`
    *   *Commands:* `ls`, `cd`, `pwd`, `get` (download), `put` (upload), `exit`
*   **rsync:** Optimized, delta-transfer synchronization.
    *   *Sync Local to Remote:* `rsync -avz /local/dir/ user@host:/remote/dir/`
    *   *Mirror (Delete Source Extras):* `rsync -avz --delete /local/dir/ user@host:/remote/dir/`

## 🛡️ Part 2: Firewall Security
*   **UFW (Uncomplicated Firewall):** User-friendly front-end for iptables.
    *   *Status:* `sudo ufw status numbered`
    *   *Control:* `sudo ufw enable` / `disable`
    *   *Allow:* `sudo ufw allow 22` / `80/tcp`
    *   *Block IP:* `sudo ufw allow from 192.168.1.50`
    *   *Delete:* `sudo ufw delete [rule_number]`
*   **iptables:** Advanced, kernel-level packet filtering.
    *   *View:* `sudo iptables -L -vn`
    *   *Allow Port:* `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT`
    *   *Drop IP:* `sudo iptables -A INPUT -s 203.0.113.50 -j DROP`
    *   *Flush All:* `sudo iptables -F`

## Table:

| Firewall Layer | **UFW (Uncomplicated Firewall)** | **IP Tables** |
| :--- | :--- | :--- |
| **Abstraction Level** | User-friendly, high-level command-line tool | Low-level system engine directly editing netfilter tables |
| **Rule Specification** | Simplified macro parsing (e.g., application profiles) | Deep bitwise evaluation (Protocols, interfaces, states, flags) |
| **Deployment Context** | Ideal for standard servers and localized host protection | Engineered for complex corporate routing, NAT, edge security |