import fcm_manager as fcm


# These fcm tokens are generated from the client side FCM SDKs
# In our case we'll get them from the Flutter app then associate them with a user account by
# updating the user details and adding the device token, and the generation timestamp
# to their account everytime they launch the app
# Then we'll query the token(s) from our database any time we want to send a push notification

fcm_tokens = [
    "czwlbWjTSwu150CWf4H6P4:APA91bGHuegUfZM68R3zOJHYFpLvlKtR96JyC27cV-T5pkevyfoUhZlzqZ6WnsICcgf95a7_XTgVyVIomvLN_pakeSNCwxgLW2xhF2_AxmPQQN0IAq6XSxdUVi5aaAoADNZ76aWtcbhl"]

# request for input from the console to send a custom string
title = input("Enter notification title: ")
body = input("Enter notification body: ")
screen = input("Enter notification screen: ")

fcm.send_push_notification(title, body, screen, fcm_tokens)
