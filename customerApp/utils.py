import africastalking
import environ
from dotenv import load_dotenv
load_dotenv()

env = environ.Env()
class SMS:
  def __init__(self):
    self.username = env.str('USERNAME')
    self.api_key = env.str('API_KEY')
    self.sender_id = env.str('SHORT_CODE')
    africastalking.initialize(self.username, self.api_key)

    self.sms = africastalking.SMS

  def send_message(self, phone_number):
    recipients = ['+254' + phone_number[1:]]
    message = "Your order has been placed successfully";
    print(self.sender_id, recipients, message)
    try:
      response = self.sms.send(message, recipients, self.sender_id)
      print (response)
    except Exception as e:
      print (f"Encountered an error while sending: {e}")
      

