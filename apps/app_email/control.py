import logging

from flask_mail import Message
from site_start import mail

from backgroup import concurrent_decorator


@concurrent_decorator
def send_message(message: str, body: str, recipients=['1906317758@qq.com']) -> bool:
    try:
        msg = Message(message, sender='hyp19990919@163.com', recipients=recipients)
        msg.body = body
        mail.send(msg)
    except Exception as e:
        logging.error(msg=f'sent email error :{e}')
