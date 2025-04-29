from azure.communication.email import EmailClient
from dotenv import load_dotenv
import os

#Utilizando la misma logica de azure communication
class Send_email:
    def __init__(self, message, recipient, subject_line = "2FA Code"):
        self.message = message
        self.recipient = recipient
        self.subject_line = subject_line

    def send_the_email(self):
        response = False
        load_dotenv()
        try:
            connection_string = os.getenv('connection_string')
            client = EmailClient.from_connection_string(connection_string)

            message = {
                "senderAddress":os.getenv('email_sender'), 
                "recipients": {
                    "to": [{"address": self.recipient}],
                },
                "content": {
                    "subject": self.subject_line,
                    "plainText": self.message,
                }
            }

            poller = client.begin_send(message)
            result = poller.result()  
            response = True

        except Exception as ex:
            print(ex)

        return response
    
    
    def send_the_reset_link(self):
        response = False
        load_dotenv()
        try:
            connection_string = os.getenv('connection_string')
            client = EmailClient.from_connection_string(connection_string)
            message = {
                "senderAddress": os.getenv('email_sender'), 
                "recipients": {
                    "to": [{"address": self.recipient}],
                },
                "content": {
                    "subject": self.subject_line,
                    "html": f"<a href='{self.message}'>{self.message} Click para resetear la contraseña</a>",
                }
            }
            poller = client.begin_send(message)
            result = poller.result()  
            response = True
        except Exception as ex:
            print(ex)
        return response
    

    def send_the_payment_info(self):
        response = False
        load_dotenv()
        try:
            connection_string = os.getenv('connection_string')
            client = EmailClient.from_connection_string(connection_string)

            message = {
                "senderAddress": os.getenv('email_sender'),
                "recipients": {
                    "to": [{"address": self.recipient}],
                },
                "content": {
                    "subject": self.subject_line,
                    "plainText": self.message,
                }
            }

            poller = client.begin_send(message)
            result = poller.result()
            response = True

        except Exception as ex:
            print(ex)

        return response


    