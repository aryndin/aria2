from app import db
from . import lm
from werkzeug.security import generate_password_hash, check_password_hash

@lm.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(120))
	password_hash2 = db.Column(db.String(120))
	tasks_to_do = db.relationship("Tasks", backref="worker", lazy="dynamic", foreign_keys='[Tasks.assigned_to]')
	assigned_tasks = db.relationship("Tasks", backref="manager", lazy="dynamic", foreign_keys='[Tasks.assigned_by]')

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3

	def __repr__(self):
		return '<User {}>'.format(self.nickname)


class Tasks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	assigned_by = db.Column(db.Integer, db.ForeignKey(User.id))
	assigned_to = db.Column(db.Integer, db.ForeignKey(User.id))
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	state = db.Column(db.Boolean)

	def __repr__(self):
		return '<Task %r>' % (self.body)