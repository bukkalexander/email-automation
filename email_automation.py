import smtplib
import ssl
import sys
from email.message import EmailMessage
import yaml
from pathlib import Path

ROOT_PATH = Path(__file__).parent.resolve()
PATH_RECIPIENTS = ROOT_PATH / "recipients.yaml"
EMAIL_SENDER = 'fika.script@gmail.com'
EMAIL_PASSWORD = 'erjdqvdmkswbyksc'
SUBJECT = 'Fika reminder'


def send_email(name_receiver, email_receiver):
    em = EmailMessage()
    em['From'] = EMAIL_SENDER
    em['To'] = email_receiver
    em['Subject'] = SUBJECT

    body = """
        Congratulations {name}!

        Your are the fika provider of the week

        // Fika Script
        """.format(name=name_receiver)
    em.set_content(body)

    context = ssl.create_default_context()
    port = 465
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, email_receiver, em.as_string())


def get_first_recipient(path_recipients):
    with open(path_recipients, 'r', encoding='utf8') as stream:
        recipients = yaml.safe_load(stream)
        return recipients[0]


def rotate_recipients(path_recipients):
    with open(path_recipients, 'r', encoding='utf8') as stream:
        recipients = yaml.safe_load(stream)
        recipients = recipients[1:] + recipients[:1]
    with open(path_recipients, 'w', encoding='utf8') as stream:
        yaml.safe_dump(recipients, stream, allow_unicode=True)


if __name__ == '__main__':
    if sys.argv[1] == "send":
        recipient = get_first_recipient(PATH_RECIPIENTS)
        send_email(recipient["name"], recipient["email"])
    elif sys.argv[1] == "rotate":
        rotate_recipients(PATH_RECIPIENTS)
