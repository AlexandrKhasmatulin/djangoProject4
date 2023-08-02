import os
import smtplib
import sys
from configparser import ConfigParser

from django.contrib import postgres


def send_email(subject, body_text, emails):
    """
    Send an email
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "from_addr")

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % ', '.join(emails),
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, emails, BODY)
    server.quit()

    con = postgres.connect("catalog.postgres")  # подразумеваю, что таблицу ты уже создал
    cur = con.cursor()
    cur.execute("SELECT email FROM users_user")
    emails = [row['email'] for row in cur]
    subject = "Test email from Python"
    body_text = "Python rules them all!"
    send_email(subject, body_text, emails)