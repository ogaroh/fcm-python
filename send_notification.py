import fcm_manager as fcm


# These fcm tokens are generated from the client side FCM SDKs
# In our case we'll get them from the Flutter app then associate them with a user account by
# updating the user details and adding the device token, and the generation timestamp
# to their account everytime they launch the app
# Then we'll query the token(s) from our database any time we want to send a push notification

fcm_tokens = [
    "f5c5ZdvfTZa9K5zc_BkTCY:APA91bFeEM8YySUhTGRsAm5yEuXbJTjZr_TXfEOlMGrgOsMqt1K1bcz2sj2fg_bOhtQMuRh45Qi9v-aZV-Uakx4SjZI0DYScBKIPl1yh88BmuBjDgDrOniFx34hyg_FwRuv4j6TWMFyr"]

# request for input from the console to send a custom string
title = input("Enter notification title: ")
body = input("Enter notification body: ")
screen = input("Enter notification screen: ")

fcm.send_push_notification(title, body, screen, fcm_tokens)
