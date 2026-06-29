# Linux Web Server Deployment, Virtual Hosting & Security Management

A comprehensive operational manual and quick-recap guide for installing, configuring, troubleshooting, and securing Apache2 and Nginx web services, alongside multi-site Virtual Host orchestration.

---

## 💻 Part 1: Web Server Engine Installation & Core Management

### 🌐 1. Protocols & Core Architectural Ports
*   **HTTP (Hypertext Transfer Protocol):** Runs unencrypted by default on **Port 80** (or testing ports like 8080). It transmits data in cleartext, making it vulnerable to packet sniffing and interception.
*   **HTTPS (Hypertext Transfer Protocol Secure):** An encrypted application layer running on **Port 443**. It employs cryptographic SSL/TLS public certificates signed by an authoritative Certificate Authority (CA) to establish host legitimacy and maintain absolute data encryption and integrity.

### 🌐 2. Apache2 HTTP Server Deployment
Apache2 is a robust, full-featured, and highly extensible web server engine capable of handling complex multi-module configurations and enterprise-scale application stacks.

*   **Operational Paths & Repositories:**
    *   **Default Web Document Root:** `/var/www/html/`
    *   **Default Landing Content Configuration:** `/var/www/html/index.html`
    *   **Available Configuration Architecture Repository:** `/etc/apache2/sites-available/`
*   **Install the Core Package:** (Downloads and installs the Apache2 server binary stack from default repositories)
    ```bash
    sudo apt update && sudo apt install apache2 -y
    ```
*   **Verify Service Operational Uptime:** (Queries systemd to ensure the web server service engine is active and listening)
    ```bash
    systemctl status apache2
    ```
*   **Service Lifecycle Management Commands:**
    ```bash
    sudo systemctl start apache2    # Spawns the web server runtime process engine
    sudo systemctl stop apache2     # Kills the active server background daemon
    sudo systemctl enable apache2   # Configures service to auto-start on system boot
    sudo systemctl reload apache2   # Hot-reloads configuration edits without dropping active connections
    ```
*   **Verify Web Content Delivery via CLI:** (Uses curl as a command-line interface browser to validate HTTP responses locally)
    ```bash
    # "localhost:80": Targets the local machine interface on standard HTTP communication Port 80
    curl http://localhost:80
    ```

### ⚡ 3. Nginx High-Performance Light Web Server
Nginx (Engine X) is an asynchronous, event-driven, highly optimized, lightweight web server and reverse proxy/load balancer engine engineered for extreme speed and low hardware resource consumption.

*   **Install the Lightweight Engine:** (Deploys the alternative Nginx web service framework)
    ```bash
    sudo apt install nginx -y
    ```
*   **Manage Port Conflicts & Swap Engines:** (Stops Apache2 to free up Port 80 before spinning up the Nginx process. Only **one** service framework can occupy public socket Port 80 concurrently; failure to do so yields critical bind errors.)
    ```bash
    sudo systemctl stop apache2 && sudo systemctl start nginx
    ```

---

## 📂 Part 2: Virtual Hosting & Multi-Site Directory Orchestration

Virtual Hosting allows a single Linux physical machine node or server instance to host hundreds of distinct websites concurrently by routing distinct traffic streams based on the incoming domain name or header metadata.

### 📐 1. Directory Tree & Permission Foundations
*   **Provision Custom Site Directories:** (Creates isolated web document root paths for separate domains)
    ```bash
    sudo mkdir -p /var/www/staragile
    sudo mkdir -p /var/www/mywebsite
    sudo mkdir -p /var/www/othersite
    ```
*   **Structure Minimal HTML Target Layout Files:** (Injects barebones content to verify dynamic domain routing later)
    ```bash
    echo "<h1>This is a virtual hosting test for My Website</h1>" | sudo tee /var/www/mywebsite/index.html
    echo "<h1>Welcome to StarAgile Training</h1>" | sudo tee /var/www/staragile/index.html
    ```
*   **Enforce Web User Ownership Structures:** (Grabs directory blocks recursively and updates permissions so the non-privileged system web process can read files safely while preventing unauthorized tampering)
    ```bash
    # "-R": Recursively impacts all nested child folders and indices
    # "www-data:www-data": Modifies owner and group to match the standard Linux web execution account
    sudo chown -R www-data:www-data /var/www/staragile
    sudo chown -R www-data:www-data /var/www/mywebsite
    sudo chown -R www-data:www-data /var/www/othersite
    
    # Enforce safe read-execution configurations (755 for directories, 644 for files)
    sudo chmod -R 755 /var/www/staragile
    sudo chmod -R 755 /var/www/mywebsite
    sudo chmod -R 755 /var/www/othersite
    ```

### 📝 2. Virtual Host Site Configuration
Site configuration files are explicitly handled within the system available directory repository path: `/etc/apache2/sites-available/`

*   **Create a Virtual Host Blueprint Configuration:** (Defines domain bindings, target document paths, and directory privileges)
    ```bash
    sudo nano /etc/apache2/sites-available/staragile.conf
    ```
*   **Insert the Core Site Profile Code Block:** (Ensure `ServerName` maps clean domain names without protocol prefixes like `http://` or `://`)
    ```apache
    <VirtualHost *:80>
        ServerName staragile.com
        ServerAlias ://staragile.com
        DocumentRoot /var/www/staragile

        <Directory /var/www/staragile>
            AllowOverride All
            Require all granted
        </Directory>
    </VirtualHost>
    ```

### 🚀 3. Activating Site Profiles & Local DNS Spoofing
*   **Enable the Virtual Host Profile:** (Generates symlinks linking the available profile into the live active site database array)
    ```bash
    sudo a2ensite staragile.conf
    sudo a2ensite mywebsite.conf
    sudo a2ensite othersite.conf
    ```
*   **Hot-Reload Web Service Configurations:** (Forces the runtime server to parse newly added profiles without restarting the service entirely, avoiding operational downtime)
    ```bash
    sudo systemctl reload apache2
    ```
*   **Map Domain Layout Strings in the Hosts Profile:** (Intercepts public internet DNS lookups to force custom domain strings to resolve directly to your local server node IP, bypassing global DNS propagation delays)
    ```bash
    sudo nano /etc/hosts
    ```
    *Append these resolution entry rule lines directly inside the file:*
    ```text
    127.0.0.1       ://mywebsite.com
    127.0.0.1       ://othersite.com
    10.211.55.12    staragile.com ://staragile.com
    ```

---

## 🛡️ Part 3: Layer-4 Netfilter Firewall Intercept Controls

- Read from chapter 11.

---

## ⚖️ Architectural System Matrix

| Architectural Vector | **Apache2 Server** | **Nginx Web Server** |
| :--- | :--- | :--- |
| **Process Model** | Multi-Processing Modules (Prefork, Worker, Event) | Asynchronous, Non-blocking, Event-Driven loop |
| **Performance Profile** | Higher memory footprint under heavy traffic loads | Stable, low memory consumption; extreme concurrency capacity |
| **Best-Use Application** | Complex dynamic sites with granular rewrite directories | High-speed static assets, reverse-proxying, load-balancing |


## More commands:

```bash
# In remote machine
curl -v localhost:80 (command line utility to fetch the http)
curl -v <ip>:80 (command line utility to fetch the http)
iptables -L (to check if firewall is available to block)
sudo -D INPUT 2 (Delete  rule no 2 which was blocking http req from anywhere -> it must be allowed)

# In client machine browser:
http://<remoteIp>:80 (to check the connection)
```

## Setting Up a Basic Server
```bash
## Step 1: Install Web Server Software on remote machine
# Remote machine
sudo apt update
sudo apt install apache2 (install pkg)
sudo systemctl start apache2 (to start apache service)
sudo systemctl enable apache2 (to enable apache service)

vim /var/www/html/index.html (readonly -> this is the file that has content of webservice)
sudo vim /var/www/html/index.html (this is the file that has content of webservice)

http://<web_server_ip> (type this in browser of client machine to check; if not visible then check more command section)


## Step 2 Configure the firewall -> allow HTTP & HTTPS traffic through the firewall
sudo ufw allow 'Apache Full'
sudo ufw status


## Step 3: Save and Restore Rules
 # Save Rules
 sudo iptables-save > /etc/iptables/rules.v4

 # Resore Rules
 sudo iptables-restore < /etc/iptables/rules.v4

 # Persist Rules Across Reboots: insta;; the persistent package
 sudo apt install iptables-persistent
```

## Nginx Web Server
It is lightweight and high performace web server. it can e used as load balancer as well.
```bash
### Step 1 Install Nginx
sudo apt install nginx

sudo systemctl start nginx
sudo systemctl enable nginx

http://<server_ip> (search this in browser in any client to verify)


## Step 2 Configure the firewall -> allow HTTP & HTTPS traffic through the firewall
sudo ufw allow 'Nginx Full'
sudo ufw status

## Step 3 Serve Web content
# 1. Default Web Directory:
    # - For Apache=> /var/www/html
    # - For Nginx=> /usr/share/nginx/html

# 2. Create a test page
echo "<h1>Welcome....</h1>" | sudo tee /var/www/html/index.html

# Verify in Browser usinf http://<ip>

## Step 4 Host a custom website
# 1. Upload website files
    # - Replace the default index.html with your website's content

# 2. Set Permissions
    # - Ensure the web server has the correct permissions
    sudo chown -R www-data:www-data /var/www/html
    sudo chmod -R 755 /var/www/html

## Step 5 Multiple website host
    # We can host multiple websites on a single machine. 
    # Create folder at `/var/www/<myWebsite> ' with 755 permissions sung 'sudo mkdir -p /var/www/mywebsite'. 
    # inside this we can create index.html. And inside SSH Configuration file '/etc/apache2/sites-available/<mywebsite.conf>' we can give reference for this new page

    # Once done then enable it
    sudo a2ensite <mywebsite.conf>
    sudo systemctl reload apache2.servce #(restart not recommended)
    cat /etc/hosts #(can check the domain with respective ip)


    # *************************** On client as well whenever we try to access a website it comes to '/etc/hosts' file for resolve if not entry then will go to DNS Server. Better to add there as well if our website is not hosted yet.

## Step 6 Stop services 
    sudo systemctl stop apache2.service
```