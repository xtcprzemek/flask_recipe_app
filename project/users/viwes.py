# project/users/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, url_for, flash

from sqlalchemy.exc import IntegrityError

from .models import User
from .forms import RegisterForm
from project import db
################
#### config ####
################

users_blueprint = Blueprint('users', __name__, template_folder='templates')


################
#### routes ####
################

### Login page  TBC ###

@users_blueprint.route('/login')
def login():
    users = User.query.all()
    print(users[0].email)
    return render_template('login.html')


### Registration page ###

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.email.data, form.username.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
    return render_template('register.html', form=form)





