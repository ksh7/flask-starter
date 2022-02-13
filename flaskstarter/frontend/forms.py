# -*- coding: utf-8 -*-

from flask import Markup

from flask_wtf import FlaskForm
from wtforms import (ValidationError, HiddenField, BooleanField, StringField,
                     PasswordField, SubmitField, TextAreaField, EmailField)
from wtforms.validators import InputRequired, Length, EqualTo, Email

from ..utils import (NAME_LEN_MIN, NAME_LEN_MAX, PASSWORD_LEN_MIN,
                     PASSWORD_LEN_MAX)

from ..user import Users

terms_html = Markup('<a target="blank" href="/terms">Terms of Service</a>')


class LoginForm(FlaskForm):
    next = HiddenField()
    login = StringField(u'Email', [InputRequired()])
    password = PasswordField('Password', [InputRequired(),
                                          Length(PASSWORD_LEN_MIN,
                                                 PASSWORD_LEN_MAX)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class SignupForm(FlaskForm):
    next = HiddenField()
    name = StringField(u'Name', [InputRequired(), Length(NAME_LEN_MIN, NAME_LEN_MAX)])
    email = EmailField(u'Email', [InputRequired(), Email()])
    password = PasswordField(u'Password',
                             [InputRequired(), Length(PASSWORD_LEN_MIN, PASSWORD_LEN_MAX)],
                             description=u' 6 or more characters.')
    agree = BooleanField(u'Agree to the ' + terms_html, [InputRequired()])
    submit = SubmitField('Sign up')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first() is not None:
            raise ValidationError(u'This email is taken')


class RecoverPasswordForm(FlaskForm):
    email = EmailField(u'Your email', [Email()])
    submit = SubmitField('Send instructions')


class ChangePasswordForm(FlaskForm):
    email_activation_key = HiddenField()
    email = HiddenField()
    password = PasswordField(u'Password', [InputRequired()])
    password_again = PasswordField(u'Password again', [EqualTo('password', message="Passwords don't match")])
    submit = SubmitField('Save')


class ContactUsForm(FlaskForm):
    name = StringField(u'Name', [InputRequired(), Length(max=64)])
    email = EmailField(u'Your Email', [InputRequired(), Email(), Length(max=64)])
    subject = StringField(u'Subject', [InputRequired(), Length(5, 128)])
    message = TextAreaField(u'Your Message', [InputRequired(), Length(10, 1024)])
    submit = SubmitField('Submit')
