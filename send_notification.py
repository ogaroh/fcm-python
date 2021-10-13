import fcm_manager as fcm


# These fcm tokens are generated from the client side FCM SDKs
# In our case we'll get them from the Flutter app then associate them with a user account by
# updating the user details and adding the device token, and the generation timestamp
# to their account everytime they launch the app
# Then we'll query the token(s) from our database any time we want to send a push notification

fcm_tokens = [
    "ea4OEUB1SvadeJaO7qWVXK:APA91bFIFCs2XgzvVyEw3xaBqslRB3YrpUbhtNtzSgPQnZ5fvhwM0zDjn4NfmuyjhtDOhaLjEgfHcBhWP2hgILXiQi_5eK__tnKpqDJHBveasCSyA-B4ul5qErx6uQ53wDRAkWvh21cw"]


# request for input from the console to send a custom string
title = input("Enter notification title: ")
body = input("Enter notification body: ")
screen = input("Enter notification screen: ")

fcm.send_push_notification(title, body, screen, fcm_tokens)
