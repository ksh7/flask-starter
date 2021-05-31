# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Required, Length


class MyTaskForm(FlaskForm):
    task = TextAreaField(u'Your Task', [Required(), Length(5, 2048)])
    submit = SubmitField(u'Save Task')
