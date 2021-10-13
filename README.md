### FCM push notification service with Python
#### Author: Erick Ogaro, 2021
##### Steps to run:

1.  Download the service key (JSON) for your FCM project in Firebase
2.  Run `pip install firebase-admin` in your project's virtual env
3.  Replace certificate path with the path to your downloaded service key JSON file
4.  Replace the `registration_tokens` list with your own from a server or something
5.  Run `python send_notification.py` to call the `send_push_notification()` function, passing in your custom
    title, body, the list of tokens (can have one) and the screen you want the notification to redirect
    the recipient to.
