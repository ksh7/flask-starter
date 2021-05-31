# -*- coding: utf-8 -*-

from sqlalchemy import Column

from ..extensions import db
from ..utils import get_current_time

from flask_login import current_user
from flask_admin.contrib import sqla


class MyTaskModel(db.Model):

    __tablename__ = 'mytask_model'

    id = Column(db.Integer, primary_key=True)

    task = Column(db.String(2048))

    added_time = Column(db.DateTime, default=get_current_time)

    users_id = Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("Users", uselist=False, backref="mytask_model")

    def __unicode__(self):
        _str = 'ID: %s, Post: %s' % (self.id, self.task)
        return str(_str)


# Customized MyTask model admin
class MyTaskModelAdmin(sqla.ModelView):
    column_sortable_list = ('id', 'users_id', 'added_time')

    column_filters = ('id', 'users_id', 'added_time')

    def __init__(self, session):
        super(MyTaskModelAdmin, self).__init__(MyTaskModel, session)

    def is_accessible(self):
        if current_user.role == 'admin':
            return current_user.is_authenticated()
