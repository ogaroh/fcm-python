import fcm_manager as fcm


# These registration tokens comes from the client side FCM SDKs.
# In our case we'll get them from the Flutter app associate them with a user account
registration_tokens = [
    "ea4OEUB1SvadeJaO7qWVXK:APA91bFIFCs2XgzvVyEw3xaBqslRB3YrpUbhtNtzSgPQnZ5fvhwM0zDjn4NfmuyjhtDOhaLjEgfHcBhWP2hgILXiQi_5eK__tnKpqDJHBveasCSyA-B4ul5qErx6uQ53wDRAkWvh21cw"]


# request for input from the console to send a custom string
title = input("Enter notification title: ")
body = input("Enter notification body: ")
screen = input("Enter notification screen: ")

fcm.send_push_notification(title, body, screen, registration_tokens)
