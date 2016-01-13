import os
import threading
import imaplib
import email.parser


def read(username, password):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')

    # Use search(), not status()
    status, response = imap.search(None, ("unseen"))
    unread_msg_nums = response[0].split()

    # Print the count of all unread messages
    print len(unread_msg_nums)

    # Print all unread messages from a certain sender of interest
    result, cnt = imap.search(None, ("unseen"))
    unread_msg_nums = cnt[0].split()
    da = []
    if unread_msg_nums > 0:
        for e_id in unread_msg_nums:
            print e_id
            result, data = imap.fetch(e_id, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
            extract = data[0][1]

            print extract
            new = "new_mail"
            os.system('notify-send ' + new)

    imap.close()
    imap.logout()


def check():
    username = "optimistisu@gmail.com"
    password = "XXXXXXXXxx"
    read(username, password)
    threading.Timer(60.0, check).start()


check()
