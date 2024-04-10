from twilio.rest import Client
from constants import *


# para mas informacion acerca de la API ver https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
class NotificationManager:

    def __init__(self):
        
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
