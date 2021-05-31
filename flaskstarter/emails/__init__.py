# -*- coding: utf-8 -*-

from flask_mail import Message

from ..extensions import mail


async def send_async_email(subject, html, send_to):
    """ send mail in async mode"""

    message = Message(subject=subject, html=html, recipients=[send_to])
    await mail.send(message)
