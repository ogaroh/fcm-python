# Author: Erick Ogaro, 2021
# Steps to run:
#   1. Download the service key (JSON) for your FCM project in Firebase
#   2. Run `pip install firebase-admin` in your project's virtual env
#   3. Replace certificate path with the path to your downloaded service key JSON file
#   4. Replace the `registration_tokens` list with your own from a server or something
#   5. Run `python send_notification.py` to call the `send_push_notification()` function, passing in your custom
#       title, body, the list of tokens (can have one) and the screen you want the notification to redirect
#       the recipient to.
#

import firebase_admin
from firebase_admin import credentials, messaging

# replace this path with your own
cred = credentials.Certificate(
    "/Users/sibasi/dev-tools/firebase-admin/service-keys/service-account-key.json"
)
firebase_admin.initialize_app(cred)


# function to send a multicast message with custom data
def send_push_notification(title, body, screen, tokens):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        data={
            "screen": screen
        },
        tokens=tokens,
    )

    # Send a message to the devices corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
