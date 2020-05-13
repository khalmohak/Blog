from app import app
from flask import render_template,redirect,flash, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')


def index():
	user = {'username':'Mohak'}
	posts = [{
		'author':{'username':'John'},
		'body':'Hello this is John'
	},
	{

		'author':{'username':'Lida'},
		'body':'Im a Linda'
	}



	]
	return render_template('index.html',  user=user, posts=posts)


@app.route('/login', methods=['GET','POST'])

def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, rememberme={}'.format(
			form.username.data, form.rememberme.data))
		return redirect(url_for('index'))
	return render_template('login.html', form=form)
