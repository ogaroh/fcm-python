import firebase_admin
from firebase_admin import credentials, messaging

# replace this path with your own
cred = credentials.Certificate(
    "/Users/sibasi/dev-tools/firebase-admin/service-keys/service-account-key.json"
)
firebase_admin.initialize_app(cred)


# function to send a push notification with custom data
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
