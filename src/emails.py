from __future__ import annotations

import datetime
import os

import mailparser
from dotenv import find_dotenv
from dotenv import load_dotenv
from imapclient import IMAPClient

_ = load_dotenv(find_dotenv())

IMAP_HOST = "imap-mail.outlook.com"
IMAP_PORT = 993
EMAIL_IMAP_USERNAME = os.getenv("EMAIL_IMAP_USERNAME")
EMAIL_IMAP_PASSWORD = os.getenv("EMAIL_IMAP_PASSWORD")

with IMAPClient(host=IMAP_HOST, port=IMAP_PORT) as client:
    try:
        client.login(EMAIL_IMAP_USERNAME, EMAIL_IMAP_PASSWORD)
        client.select_folder("Inbox", readonly=True)

        # search criteria are passed in a straightforward way
        # (nesting is supported)
        print("Searching for emails since", datetime.date.today())
        messages = client.search(criteria=["SINCE", datetime.date.today()])

        # fetch selectors are passed as a simple list of strings.
        response = client.fetch(messages, ["FLAGS", "RFC822", "RFC822.SIZE"])

        # `response` is keyed by message id and contains parsed,
        # converted response items.
        for message_id, data in response.items():
            email_message = mailparser.parse_from_bytes(data[b"RFC822"])
            print(email_message)
    except Exception as e:
        print("An error occurred:", e)
