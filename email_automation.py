import smtplib
import ssl
import sys
from email.message import EmailMessage
import yaml
from pathlib import Path
import argparse

ROOT_PATH = Path(__file__).parent.resolve()
# PATH_RECIPIENTS = ROOT_PATH / "recipients.yaml"
EMAIL_SENDER = 'fika.script@gmail.com'
EMAIL_PASSWORD = 'erjdqvdmkswbyksc'
SUBJECT = 'Fika reminder'


def send_email(recipient, message):
    em = EmailMessage()
    em['From'] = EMAIL_SENDER
    em['To'] = recipient["email"]
    em['Subject'] = message["subject"]

    content = message["content"].format(name=recipient["name"])
    em.set_content(content)

    context = ssl.create_default_context()
    port = 465
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, recipient["email"], em.as_string())


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


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="COMMAND", help="select which command you want to run")
    send_parser = subparsers.add_parser("send")
    send_parser.set_defaults(command="send")
    rotate_parser = subparsers.add_parser("rotate")
    rotate_parser.set_defaults(command="rotate")
    # parser.add_argument("COMMAND", help="Select command to run", choices=["send", "rotate"])
    send_parser.add_argument("recipients", help="path to recipients file")
    send_parser.add_argument("message", help="path to message file")
    rotate_parser.add_argument("recipients", help="path to recipients file")
    return parser.parse_args()


def get_message(path_message):
    with open(path_message, 'r', encoding='utf8') as stream:
        message = yaml.safe_load(stream)
    return message


if __name__ == '__main__':
    args = parse_args()

    if args.command == "send":
        recipient = get_first_recipient(args.recipients)
        message = get_message(args.message)
        send_email(recipient, message)
    elif args.command == "rotate":
        rotate_recipients(args.recipients)
    print("hej")
