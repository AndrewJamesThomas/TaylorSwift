import os
from twilio.rest import Client
from secrets import *

client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG7615276652668de036f743f60301a698',
    body='Hi',
    to='+5415880215'
)
