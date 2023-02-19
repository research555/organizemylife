from simplegmail import Gmail
from simplegmail.query import construct_query
from datetime import datetime
import regex as re
from sql import SQL
"""

I need a function that will automatically update the sql table with new emails.

Function that checks which order messages are in thread

Function that checks if the email is a reply to a previous email



"""

sql = SQL()
cursor = sql.cursor
mydb = sql.mydb


# Thread ID is unique for all convos in your inbox while message ID is unique for each message in a convo
# This means that if you have a convo with 5 messages, the thread ID will be the same for all 5 messages
# but the message ID will be different for each message.

# Create a Gmail object with your Gmail email address and password
gmail = Gmail()
query_params = {"newer_than": (2, "day")}
messages = gmail.get_messages(query=construct_query(query_params))

for message in messages:
    head, sep, tail = message.date.partition('+')
    message_id = message.id
    thread_id = message.thread_id
    sender = get_email(message.sender)
    subject = message.subject
    message_received = head
    content = message.plain
    labels = [label.name for label in message.label_ids]
    recipient = get_email(message.recipient)

    # Convert the labels to inte


    # Insert the data into the MySQL database
    cmd = "INSERT INTO emails (sender, recipient, message_received, message_id, thread_id, content, subject, label_unread, label_important, label_job_applications, label_accepted, label_rejected, label_first_interview, label_second_interview, label_offer, label_inbox) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
    sender, recipient, message_received, message_id, thread_id, content, subject, label_unread, label_important,
    label_job_applications, label_accepted, label_rejected, label_first_interview, label_second_interview, label_offer,
    label_inbox
    )
    #cursor.execute(cmd, values)
    #mydb.commit()


class Email:
    def __init__(self, gmail, SQL):
        self.gmail = gmail
        self.sql = SQL
        self.cursor = self.sql.cursor
        self.mydb = self.sql.mydb

    def _get_email(self, str):
        email = re.findall(r'[\w\.-]+@[\w\.-]+', str)
        if email:
            return ','.join(email)
        else:
            return None

    def _get_labels(self, labels):
        labels = [label.name for label in labels]
        label_unread = int('UNREAD' in labels)
        label_important = int('IMPORTANT' in labels)
        label_job_applications = int('Job Applications' in labels)
        label_accepted = int('Accepted' in labels)
        label_rejected = int('Rejected' in labels)
        label_first_interview = int('First Interview' in labels)
        label_second_interview = int('Second Interview' in labels)
        label_offer = int('Offer' in labels)
        label_inbox = int('INBOX' in labels)
        return label_unread, label_important, label_job_applications, label_accepted, label_rejected, label_first_interview, label_second_interview, label_offer, label_inbox

    def _get_date(self, date):
        head, sep, tail = date.partition('+')
        return head

    def _get_query(self, query_params):
        return construct_query(query_params)

    def _get_messages(self, query_params=None):
        if query_params is None:
            query_params = {"newer_than": (2, "day")}
        return self.gmail.get_messages(query=construct_query(query_params))

    def



