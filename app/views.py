from flask import render_template, flash, redirect, abort, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm
from .models import User


@app.route('/')
@app.route('/index')
def index():
	user = g.user
	tasks = [  # fake array of posts
		{
			'state': 1,
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'state': 0,
			'author': {'nickname': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html",
						   title='Home',
						   user=user,
						   tasks=tasks)


@app.route('/login', methods=['GET', 'POST'])
def login():
#?    if g.user is not None and g.user.is_authenticated:
#?        return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.login.data).first()


		if user is not None and user.verify_password(form.password.data):
			print(user.nickname)
			print(type(user.nickname))
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or/and password')
	return render_template('login.html',
						   title='Sign In',
						   form=form,
						   providers=app.config['OPENID_PROVIDERS'])


@app.route('/user/<nickname>')
@login_required
def user(nickname):
	user = User.query.filter_by(nickname=nickname).first()
# TODO: 404 instead if redirect
	if user is None:
		flash('User %s not found.' % nickname)
		abort(404)
		return redirect(url_for('index'))
	tasks = [
		{'author': user, 'body': 'Test post #1'},
		{'author': user, 'body': 'Test post #2'}
	]
	return render_template('user.html',
						   user=user,
						   tasks=tasks)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.route('/logout')
def logout():
	if current_user.is_authenticated:
		logout_user()
		flash('You have been logged out')
	return redirect(url_for('index'))


@app.before_request
def before_request():
	g.user = current_user


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))