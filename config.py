import os


DEBUG = True
WTF_CSRF_ENABLED = True
SECRET_KEY = 'qwerty'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:951793@localhost/mainflask'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

BOOTSTRAP_SERVE_LOCAL = True
