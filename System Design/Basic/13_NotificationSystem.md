# Design a Notification System
    - We can have sms, email, apps notification system

## Requirements for a Notification System:
    - What type of notifications do you want to send?
        - All 3 (Email, SMS, Push notification)
    - Are these notification real-time
        - Yes, we want them in near real-time. A small delay is fine in busy hours.
    - What kind of devices do you want to send the notification to?
        - All devices (laptop, Mobile, IOS, Android)
    - How are these notifications triggered?
        - Can be automatic / scheduled / manual

## High Level Design:
    - Provider ==service==> client
    - Push notification for IOS, we need "Apple Push Notification Service".
    - Push notification for Android, we need "Firebase Cloud Messaging".

    - We need user's info to send the notification.
    - We can store the user's user_id, user_device, Device_token, last_used etc in a different db/schema.

    - All services put the notifications in "Notification System" and third party services pull from that and send to clients.
    - Notification System can generate different body fro same message for different clients.Like I want to send email and sms for order confirmation.

## Improvements:
    - "Notification System" can become single point of failure.
    - no mechanism if any service is not able to send the message. 

    - we put a Queue b/w system and third party.
    - A worker pull the req and add entry in "Notification Log" and then provide that to third party.
    - worker can put the failed msg in queue again.

    - To create message body we will need details like email or device_id and all there we will need to do some processing
    - We can use cache, DB, and a small machine.


    - What if a service gets corrupted and it puts so many notifications. 
    - we need rate limiter in this type of scenario.
    - We can restrict like max 10 message per client.
    - Device authentication before sending. Like sending message for authentic user.
    - User can choose time like send all notifications at this time.


## Event Tracking
    start --> pending --> sent --> deliver --> click
                    |      |            |
                    |      |            |
                    V      V            V
                      Error             spam

    - Did user click or sent that to spam.

