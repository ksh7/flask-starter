# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length


class MyTaskForm(FlaskForm):
    task = TextAreaField(u'Your Task', [InputRequired(), Length(5, 2048)])
    submit = SubmitField(u'Save Task')
