import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from flask import current_app as app

def mail(text, message):
    ret = True
    try:
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(["cmdb",  app.config['MAIL_SENDER']])
        msg['To'] = formataddr(["quxiaotong", app.config['MAIL_RECEIVER']])
        msg['Subject'] = message
        server = smtplib.SMTP_SSL("smtp.163.com", 465)
        server.login(app.config['MAIL_SENDER'], app.config['MAIL_PASSWORD'])
        server.sendmail(app.config['MAIL_SENDER'], [app.config['MAIL_RECEIVER']], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret
