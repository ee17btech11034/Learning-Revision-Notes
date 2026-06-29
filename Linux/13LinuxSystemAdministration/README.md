# Linux Disk Management, Partitioning & File Systems (Notes)

Comprehensive technical notes based on the Linux System Administration tutorial, complete with command explanations, practical workflows, and crucial production-grade storage management concepts.

---

## 💾 Core Concepts of Partitioning

### Traditional MBR Partition Limits
* **Maximum Partitions**: Overall partitions in standard Master Boot Record (MBR) systems are limited to a maximum of **four**.
* **Primary Partitions**: You can create up to 4 primary partitions. However, if you allocate all space to 4 primary partitions, any left-out space cannot be used later. So, if we have 500GB and we create 4 Primary Partitions then remaining 100GB will be of no use. Better to create atleast one Extended partion in this case
* **Extended & Logical Partitions**: Best practice is to create **3 primary partitions and 1 extended partition**. The extended partition acts as a container inside which you can create up to **60 logical partitions**.
* **Total Partitions**: This method allows for a maximum total of 63 partitions on a single disk.

### Sector Offsets & Alignment
* **Reserved Sectors**: The initial **2048 sectors** of a disk are blocked and kept reserved for metadata, inode tracking, and boot loader compatibility (e.g., GRUB/GRUB2). 
* **Optimization**: Leaving these sectors unallocated ensures proper alignment for 4KB physical sector devices, optimizing overall operating system performance.
* **Size Calculation Formula**: Disk size is measured via sectors, where `1 sector = 512 bytes`.
  $$\text{Size (in Bytes)} = \text{Number of Sectors} \times 512$$

---

## 🛠️ Essential Monitoring & Navigation Commands

* `lsblk`
  * Displays block devices in a visual **tree structure**.
  * Shows major/minor numbers, disk/partition types, size, and active mount points.
* `sudo fdisk -l`
  * View detailed information about partitions
* `df`
  * Displays **File System usage** and available space across storage paths.
* `df -h`
  * Shows disk storage allocations in a **human-readable format** (Gigabytes `G`, Megabytes `M`, Kilobytes `K`).
* `du -sh <directory>`
  * Displays the specific **disk usage of a directory** rather than the entire filesystem.
* `blkid`
  * Displays the attributes of block devices, crucially revealing their **UUIDs (Universally Unique Identifiers)** and filesystem format type.

---

## 🔀 Mounting and the `/etc/fstab` File

### Mount vs Unmount
Storage partitions must be linked into an existing operating directory to be readable. Ejecting or disconnecting a device requires safely decoupling it from the directory path.

* `sudo mount <device> <directory>`
  * Mounts a hardware partition onto a target folder directory.
* `sudo umount <device_or_directory>`
  * Unmounts/detaches the storage partition safely using either the device location or directory node name.

### Persistent Configurations via `/etc/fstab`
Linux refers to the `/etc/fstab` configuration file during the system boot cycle to automate mounting arrays. Entries follow this layout structure:

```text
# <device/UUID/Label>       <mount_point>       <filesystem>    <options>   <dump>  <fsck_pass>
UUID=xxxx-xxxx-xxxx         /mnt/star_agile     ext4            defaults    0       2
LABEL=star_agile            /mnt/star_agile     ext4            defaults    0       2
```

* **Dump (Column 5)**: Explicitly designated as `0` to skip filesystem data backups.
* **FSCK Pass Priority (Column 6)**: Priority checking logic where `0` disables checks, `1` targets high-priority root paths first, and `2` checks additional storage sectors consecutively after the root sequence completes.
* `sudo mount -a`
  * Forces the operating system to reread `/etc/fstab` and safely remount all listed storage arrays instantly.

---

## 🏗️ Step-by-Step Disk Partition Management

### 1. Creating a Standard Partition
```bash
# Enter fdisk workspace for your targeted drive
sudo fdisk /dev/sdc
```
* Press `p` to output existing partition table data to console safely.
* Press `n` to create a brand new slice registry.
* Pick `p` for Primary or `e` for Extended.
* Set the starting sector array offset value (Leave default to secure the 2048 metadata offset).
* Use size identifiers to define boundaries (e.g., `+500M` or `+2G`).
* Press `w` to finalize changes, save configuration tables, and exit cleanly.
* `sudo partprobe`
  * Forces the underlying OS Kernel block engine to refresh and register structural shifts instantly without forcing a complete machine reboot.

### 2. Formatting File Systems
Operating targets cannot interact with raw partitions until a file architecture framework is stamped.
* `sudo mkfs.ext4 /dev/sdc1` -> Formats using the robust EXT4 journaling standard.
* `sudo mkfs.xfs -f /dev/sdc1` -> Imprints an enterprise high-scale XFS environment (`-f` forces write).
* `sudo mkfs.vfat /dev/sdc1` -> Formats into multi-OS readable FAT32 storage structures.

### 3. Labeling Slices
* `sudo e2label /dev/sdc1 star_agile`
  * Applies an easier string name tag descriptor alias strictly on EXT filesystem variants.

---

## 📉 Resizing Partitions (Shrink & Extend Workflows)

### Structural Room Metaphor
Think of your partition space like a standard room containing furniture. You cannot build a new wall directly down the center while chairs sit scattered in the path. You must clean, organize, and consolidate items down into one safe corner before moving structural boundaries.

### Workflow A: Shrinking Safely (High Risk)
> ⚠️ **Warning**: Shrinking presents potential data corruption risks; **always generate a comprehensive backup beforehand**.

1. **Unmount target partition**: `sudo umount /dev/sdc1`
2. **Execute consistency scan**: `sudo e2fsck -f /dev/sdc1`
3. **Downscale internal filesystem first**: `sudo resize2fs /dev/sdc1 100M`
4. **Reduce real structural layout bounds**: `sudo parted /dev/sdc resizepart 1 100M`
5. **Remount framework**: `sudo mount -a`

### Workflow B: Extending Safely (Low Risk)
1. **Unmount target partition**: `sudo umount /dev/sdc1`
2. **Expand the partition container profile**: `sudo parted /dev/sdc resizepart 1 300M`
3. **Grow the tracking file engine space internally**: `sudo resize2fs /dev/sdc1`
4. **Scan and clear errors**: `sudo fsck -f /dev/sdc1`
5. **Remount system dynamically**: `sudo mount -a`

---

## 🎛️ LVM (Logical Volume Manager) Deep Dive

LVM pools varying physical sector groups together dynamically, abstracting architecture so sysadmins can expand or shrink storage footprints fluidly on demand.

```text
  [ Physical Disk: /dev/sdb ]     [ Physical Disk: /dev/sdc ]
               │                               │
       (PV Creation)                   (PV Creation)
               ▼                               ▼
       [ Physical Vol 1 ]              [ Physical Vol 2 ]
               │                               │
               └───────────────┬───────────────┘
                               │
                        (VG Formulation)
                               ▼
                    [ Volume Group (VG) ]
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
       [ Logical Vol (LV1) ]     [ Logical Vol (LV2) ]
                  │                         │
            (mkfs.ext4)                (mkfs.xfs)
                  ▼                         ▼
         Ready to Mount /          Ready to Mount /
```

### The Three-Tier Architecture
1. **Physical Volume (PV)**: Standard raw unorganized disks or primary partitions. Broken internally into microscopic **Physical Extents (PE)**, commonly sized at 4MB data chunks.
2. **Volume Group (VG)**: Combined abstract pool generated out of several active primary Physical Volumes.
3. **Logical Volume (LV)**: Real virtual operational storage slices cleanly cut from Volume Groups. These host actual standard operational filesystems.

### Practical Operational Setup Commands
* `sudo pvcreate /dev/sdc2` -> Swipes disk metadata away, registering block space as a clean **Physical Volume**.
* `sudo pvdisplay` -> Outputs metadata properties of active underlying PV installations.
* `sudo vgcreate star_agile_vg /dev/sdc2` -> Bundles specified PV components together tightly under one unified **Volume Group** structural moniker name.
* `sudo vgdisplay` -> Visualizes configuration size parameters, allocated extents, and structural bindings for active VGs.
* `sudo lvcreate -L 500M -n star_agile_lv star_agile_vg` -> Dynamically carves out a new target **Logical Volume** from our active storage group allocation asset pool.
* `sudo lvdisplay` -> Provides an overview of active storage paths, properties, and usage stats across current operational LVs.

Once your LV is generated, treat it like a regular standard partition device by formatting it (`sudo mkfs.ext4 /dev/star_agile_vg/star_agile_lv`) and mapping its node paths to directories to begin usage.

---

## 💡 Other Related Topics

### 1. MBR vs. GPT Partitioning Schemes
Production architecture relies heavily on GPT over legacy MBR layers.

| Feature | MBR (Master Boot Record) | GPT (GUID Partition Table) |
| :--- | :--- | :--- |
| **Max Disk Size** | Limited to 2 Terabytes (TB) | Up to 9.4 Zettabytes (ZB) |
| **Max Partition Count**| 4 Primary Partitions | 128 Primary Partitions natively |
| **Redundancy** | Single point of failure (sector 0) | Stores duplicate tables at the end of the disk |
| **Command Tool** | `fdisk` | `gdisk` or `parted` |

### 2. Inodes Deep Dive
* **Definition**: An Inode (index node) is a data structure on a Linux filesystem that stores everything about a file *except* its actual contents and its name. 
* **Metadata Stored**: File size, owner user ID, group ID, read/write permissions, timestamps, and direct data block location pointers.
* **The "No Space Left on Device" Error:** If a filesystem runs out of its fixed allocation of available Inodes, you cannot create new files, even if the disk has free physical space remaining. Check inode metrics using `df -i`.

### 3. Swap Space Management
Swap space acts as overflow memory. When system RAM is fully saturated, inactive memory pages are dumped temporarily onto disk storage to maintain system stability.
* **Creating a Swap Partition:**  
```bash 
sudo mkswap /dev/sdc3    # Standardize a partition to host system swap pages 
sudo swapon /dev/sdc3    # Activate the target partition space into service layout 
```
* **Persistent Configuration Entry (/etc/fstab):**
```text /dev/sdc3 none swap defaults 0 0 
```

* **Check current metrics** 
```bash
via swapon --show or free -m
```

### 4. RAID (Redundant Array of Independent Disks)
Production storage nodes combine several physical independent hard disks into single logical setups via software commands (mdadm) to prevent data loss or maximize performance speeds.
* **RAID 0 (Striping):** Splits data evenly across multiple drives. Speeds up read/write performance but offers zero backup safety. If one drive fails, all data is lost.
* **RAID 1 (Mirroring):** Duplicates exact data matches identically across paired mirror drives. High read speed safety protection; if one drive dies, the system stays online.
* **RAID 5 (Distributed Parity):** Requires a minimum of 3 drives. Strips data and balances tracking checksum calculations safely across disks. Survives a single drive failure without data loss.
* **RAID 10 (1+0):** Combines mirror protection and speed advantages concurrently. Requires at least 4 drives.

## More commands
```bash
## Step 1 Check current Disk & Partition information
lsblk # list all disk & partitions
sudo fdisk -l # view detailed info about partitions
df -h # check disk usage
df -h /home # check file system usage
du -sh /home/user1 # check disk system usage

## Step 2 Partitioning a Disk using fdisk

# Launch fdisk for a disk: Replace /dev/sdX with the disk (eg /dev/sdb)
sudo fdisk /dev/sdX

# Common fdisk commands (can be check when we run above fdisk command)
n # create a new partition
d # delete a partition
p # print the current partition table
w # write changes to disk & exit
q # Quit without saving changes

# Create a Partition
# Press n to create a new partition
# choose the partition type(primary or extended)
# specify the partition size (eg +20G for 20GB)
# press w to save changes.

## 
# Refresh Kernal Partition table
sudo partprobe


#parted command is used for GPT type partition tables that are larger disk like PetaBytes, ZetaBytes etc

sudo mkfs.ext4 /dev/sdX #better to use => (format this disk) (formated in windows with fat 32 or any will not work in linux or Mac. Like they won't even detect disk because of different format structure like INode, etc)
mkfs.ntfs /dev/sdX #(another way to format)
mkfs.xf /dev/sdX #(another way to format)
mkfs.vfat /dev/sdX #(another way to format like fat 32)

mkfs.xf -f /dev/sdX # if formateed with any 


# Label the device
sudo e2lable /dev/sdX NewLabel



# mount a dir
sudo mkdir /mnt/<folder>
sudo mount /dev/sdb3 /mnt/<folder? #(mount partition '/dev/sdb3' to a directory '/mnt')
sudo unmount /mnt #(unmount)

sudo vim /etc/fstab # (this file is used to check the mount part by system when reboot, add once we mount)
sudo mount -a #(Read fstab file and remount according to file)


# Scan file system -> 
sudo fsck /dev/sdb1 # need when we want to shrink or expand 
sudo fsck -y /dev/sbd1 # forfully check partitions


blkid /dev/sdk # to check the Unique Identifier for this disk



# To reduce/shrink the partion, first reduce the file system as it scatter its datat in that available disk
sudo e2fsck -f /dev/sdc1 # forcefully check
sudo unmount /dev/sdc1
sudo e2fsck -f /dev/sdc1 # forcefully check

sudo resize2fs /dev/sdc1 100M #(reduce the file system)

sudo parted /dev/sdc resizepart 1 100MB #(partition number 1 to 100MB shrink)(sometimes data gets corrupted specially sectors, so we need to go to recovery mode na dhandle that)

sudo /dev/sdc print 

sudo mount -a #(if gets error then below commmands run)

sudo resixe2fs /dev/sdc1 # (just to resize again)
sudo fsck -d /dev/sdc1 # clean
sudo fsck -f /dev/sdc1 # clean
# Now can run mount -a
df -h



# To expand partition
sudo unmount /dev/sdc1 # unmount
sudo e2fsck -f /dev/sdc1 # scan this

sudo parted /dev/sdc resizepart 1  300 MB

sudo resize2fs /dev/sdc1

sudo parted /dev/sdc print

sudo fsck -f /dev/sdc1

sudo mount -a



#### 
#lvM (LOGICAL VOLUME MANAGER) -> 
    # fIRST WE CREATE pv (pHYSICAL vOLUME) => THEN WE CREATE vg(vOLUME GROUP) => then we can create Logical Volume (LV).
pvdisplay # display physical volumes

sudo apt install lvm2 # software to create lv

sudo /dev/sdc

sudo pvcreate /dev/sdc2 # to create a new 

pvdisplay


sudo vgc
sudo vgcreate <gp_name> /dev/sdc2

sudo vgdisplay

sudo lvcreate -L 500M -n <name> <vg-name>

sudo lvdisplay

sudo mkfs.ext4 /dev/<gpname>/<lvName>

sudo mkdir /mnt/<lv_name>
mount /dev/<vgName>/<lvName> /mnt/<name>

df -h 
```