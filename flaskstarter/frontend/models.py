# -*- coding: utf-8 -*-

from sqlalchemy import Column

from ..extensions import db
from ..utils import get_current_time

from flask_login import current_user
from flask_admin.contrib import sqla


class ContactUs(db.Model):

    __tablename__ = 'contactus'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), nullable=False)
    email = Column(db.String(64), nullable=False)
    subject = Column(db.String(128), nullable=False)
    message = Column(db.String(2048), nullable=False)

    received_time = Column(db.DateTime, default=get_current_time)

    def __unicode__(self):
        _str = '%s. %s %s' % (self.id, self.name, self.email)
        return str(_str)


# Customized ContactUs model admin
class ContactUsAdmin(sqla.ModelView):
    column_sortable_list = ('id', 'name', 'email', 'received_time')
    column_filters = ('id', 'name', 'email', 'received_time')

    def __init__(self, session):
        super(ContactUsAdmin, self).__init__(ContactUs, session)

    def is_accessible(self):
        if current_user.role == 'admin':
            return current_user.is_authenticated()
