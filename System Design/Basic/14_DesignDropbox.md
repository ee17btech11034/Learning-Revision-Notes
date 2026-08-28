# Design Dropbox / Cloud

    - We can have different clients. 
    - We upload files on cloud and all clients can access this.

    - Advantages:
        - Availability:
            - Data is available everywhere with internet connection
        - Reliability & Durability:
            - Data is secured and remains on the cloud
        - Scalibility:
            - Your needs can expand and reduce as you desire
    
## Requirements and considerations
    - User can upload and download from all of the configured clients.
    - Users can share the files with others
    - Offline editing of files
    - Synchronize files on different clients

## Good to have features:
    - Versoning:
        - Restore previous versions.
    - Premium subscription

- Very heavy on bandwidth, high upload and download.

## Back of the envelope:
    - assume otal users = 500 million; 100 million active Users (20%)
    - Each client has average of 3 devices
    - Each user has average 200 files 
        - total files = 200 * 500 million = 100 Billion
    - avg file size = 100 KB
        - storage = 100 billion * 100 Kb = 10 PB

## High Level Design:
    - We need a block server for servr work like authentication, Rate limiter, etc.
    - We need a Backend data to store the data
    - We need one more database "Matadata Storage". It is useful to fetch the data faster. For this we need Metadata Server.
    - For multiple clients we need a Synchronization Server.

    - When we use any file storage like S3 bucket. We upload the file on our server first and then our server upload that file to S3. Technically here we are uploading file twice. Waste of resoures.
    - Here "Sync Server" helps us in "Presigned URL". Here S3 provide a temporary link with temporary access to private storage to us. We provide that and client directly upload it on S3.
    S3 will provide the response to our server that file is uploaded and this is the metadata.

    - this way only client can download the file.

    - if few files are getting accessed frequently then put a CDN b/w user and S3. store the cache.


    - We can add uses in metadata of file and maintain a list for users as well what files they can access.


    - to synchronize the live changes, we need a queue that will storethe files user is changing.
    - Synchronization server takes those changes and update Metadat storage.
    - If we have n clients we create n different Response queues, Synchronization server sends same update to all these queues and each client is configured to listen this queues.

    - Laptop is connected to internet most of the time so we can implement this with Poll service.
    - But Mobile devices and all we need push services.



- What if file is too big, then upload the file in chunks. Just upload the diff.
- parallel upload-download.
- Speed for premium users.