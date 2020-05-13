from app import app
from flask import render_template
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


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
