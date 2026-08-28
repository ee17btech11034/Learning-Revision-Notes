# Design a News feed

    - We have all latest post on homepage.

## Requirements & Conditions:
    - Should be available for mobile and as a web application too.
    - Should be able to publish updates and push to friends
    - Update should be in near realtime.
    - Have the updates in a reverse chronological order (Newest first)

    - What traffic volume is expected
    - What is the maximum number of friends (Consider a person celebrity after x friends, and we mcan change algorith for that)

    - What do posts contain (img, text, video)

## Design
    - Client upload something via Post service, to Post cache and Post DB.
    - "Fanout Service" sends that upload to all your friends from "News feed Cache"
    - Netification Service to put the notifications.


    - graph Db is best for this.