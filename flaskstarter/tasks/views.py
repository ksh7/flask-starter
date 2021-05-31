# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from ..extensions import db

from .forms import MyTaskForm
from .models import MyTaskModel


tasks = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks.route('/my_tasks', methods=['GET', 'POST'])
@login_required
def my_tasks():

    _all_tasks = MyTaskModel.query.filter_by(users_id=current_user.id).all()

    return render_template('tasks/my_tasks.html',
                           all_tasks=_all_tasks,
                           _active_tasks=True)


@tasks.route('/view_task/<id>', methods=['GET', 'POST'])
@login_required
def view_task(id):
    _task = MyTaskModel.query.filter_by(id=id, users_id=current_user.id).first()

    if not _task:
        flash('Oops! Something went wrong!.', 'danger')
        return redirect(url_for("tasks.my_tasks"))

    return render_template('tasks/view_task.html',
                           task=_task)


@tasks.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():

    _task = MyTaskModel()

    _form = MyTaskForm()

    if _form.validate_on_submit():

        _task.users_id = current_user.id

        _form.populate_obj(_task)

        db.session.add(_task)
        db.session.commit()

        db.session.refresh(_task)
        flash('Your task is added successfully!', 'success')
        return redirect(url_for("tasks.my_tasks"))

    return render_template('tasks/add_task.html', form=_form, _active_tasks=True)


@tasks.route('/delete_task/<id>', methods=['GET', 'POST'])
@login_required
def delete_task(id):
    _task = MyTaskModel.query.filter_by(id=id, users_id=current_user.id).first()

    if not _task:
        flash('Oops! Something went wrong!.', 'danger')
        return redirect(url_for("tasks.my_tasks"))

    db.session.delete(_task)
    db.session.commit()

    flash('Your task is deleted successfully!', 'success')
    return redirect(url_for('tasks.my_tasks'))


@tasks.route('/edit_task/<id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    _task = MyTaskModel.query.filter_by(id=id, users_id=current_user.id).first()

    if not _task:
        flash('Oops! Something went wrong!.', 'danger')
        return redirect(url_for("tasks.my_tasks"))

    _form = MyTaskForm(obj=_task)

    if _form.validate_on_submit():

        _task.users_id = current_user.id
        _form.populate_obj(_task)

        db.session.add(_task)
        db.session.commit()

        flash('Your task updated successfully!', 'success')
        return redirect(url_for("tasks.my_tasks"))

    return render_template('tasks/edit_task.html', form=_form, task=_task, _active_tasks=True)
