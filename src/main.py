import datetime
from twilio.rest import Client
from secrets import *

def main():
    # Create Message
    NOW = datetime.datetime.now()
    TARGET_DATE = datetime.datetime.strptime('Jul 14 2023  6:30PM', '%b %d %Y %I:%M%p')
    DATE_DIFF = TARGET_DATE - NOW

    DAYS_TO_TARGET = DATE_DIFF.days
    HOURS_TO_TARGET = round(DATE_DIFF.seconds/60/60)
    MINUTE_TO_TARGET = round((DATE_DIFF.seconds/60/60))*60) - round((DATE_DIFF.seconds/60)

    MSG = f"Hello! There are {DAYS_TO_TARGET} days, {HOURS_TO_TARGET} hours, and {MINUTE_TO_TARGET} minutes until your Taylor Swift Concert"

    # Send Message
    PHONE_NUMBER = '+15415880215'

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG7615276652668de036f743f60301a698',
        body=MSG,
        to=PHONE_NUMBER
    )

    return client
