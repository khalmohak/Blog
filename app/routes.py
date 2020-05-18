from werkzeug.urls import url_parse
from app import app, db
from flask import render_template,redirect,flash, url_for, request
from app.forms import LoginForm, RegisterForm, EditForm
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from app.models import User

app.config['SECRET_KEY']='somepassword'

@app.route('/')
@app.route('/index')


def index():
	user = {'username':'Mohak'}
	posts = [{
		'author':{'username':'John'},
		'body':'Hello this is John',
		'title':'Post 1'
	},
	{

		'author':{'username':'Lida'},
		'body':'Im a Linda',
		'title':'Post 2'
	}



	]
	return render_template('index.html',  user=user, posts=posts)


@app.route('/login', methods=['GET','POST'])

def login():
	form = LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash(f'Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.rememberme.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout', methods=['GET','POST'])

def logout():
	logout_user()
	return redirect(url_for('index'))



@app.route('/register', methods=['GET','POST'])

def register():
	form=RegisterForm()
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created sucessfuly for {form.username.data}', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/user/<username>')
@login_required

def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	posts=[
		{'author':user, 'body':'test post 1'},
		{'author':user, 'body':'test post 2'}
	]

	return render_template('user.html', title = 'Profile', user=user , posts=posts)

@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@app.route('/edit_profile', methods=['GET','POST'])
def edit_profile():
	form = EditForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about = form.about_me.data
		db.session.commit()
		flash('Your changes have been saved')
		return redirect(url_for('edit_profile'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.about_me.data = current_user.about
	return render_template('edit_profile.html', title='Edit Form', form=form)
