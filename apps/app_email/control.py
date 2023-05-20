import logging

from flask_mail import Message
from site_start import mail


def send_message(message: str, body: str, recipients=['1906317758@qq.com']) -> bool:
    status = False
    try:
        msg = Message(message, sender='hyp19990919@163.com', recipients=recipients)
        msg.body = body
        mail.send(msg)
        status = True
    except Exception as e:
        logging.error(msg=f'sent email error :{e}')
    finally:
        return status
