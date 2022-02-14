# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import (InputRequired, Length, EqualTo, Email)
from flask_login import current_user

from ..user import Users
from ..utils import PASSWORD_LEN_MIN, PASSWORD_LEN_MAX


class ProfileForm(FlaskForm):
    multipart = True
    name = StringField(u'Name', [Length(max=50)])
    email = EmailField(u'Email', [InputRequired(), Email()])
    submit = SubmitField(u'Update')


class PasswordForm(FlaskForm):
    password = PasswordField('Current password', [InputRequired()])
    new_password = PasswordField('New password', [InputRequired(), Length(PASSWORD_LEN_MIN, PASSWORD_LEN_MAX)])
    password_again = PasswordField('Password again', [InputRequired(), Length(PASSWORD_LEN_MIN, PASSWORD_LEN_MAX), EqualTo('new_password')])
    submit = SubmitField(u'Update')

    def validate_password(form, field):
        user = Users.get_by_id(current_user.id)
        if not user.check_password(field.data):
            raise ValidationError("Password is wrong")
