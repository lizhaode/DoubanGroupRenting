import smtplib

from email.mime.text import MIMEText
from email.header import Header


class SendEmail:

    def __init__(self):
        smtp_host = 'smtp.qq.com'
        self._login_user = ''
        login_password = ''

        self.qq_smtp = smtplib.SMTP_SSL(host=smtp_host)
        self.qq_smtp.login(user=self._login_user, password=login_password)

    def send_email(self, send_addr, email_message):
        mime_body = MIMEText(email_message, _charset='UTF-8')
        mime_body['Subject'] = Header(s='发现新的租房信息', charset='UTF-8')
        mime_body['from'] = 'lizhaohenry@qq.com'
        mime_body['to'] = send_addr

        self.qq_smtp.sendmail(from_addr=self._login_user, to_addrs=send_addr, msg=mime_body.as_string())
