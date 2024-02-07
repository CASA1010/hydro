from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from config import db, login

#Zuordnung User zu User-Rollen
class UserRole(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), primary_key=True)

#Definition der User-Rollen
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    desc = db.Column(db.String(40), nullable=False)

    users = db.relationship("User", secondary="user_role", back_populates="roles")

#Definition der Model-Klassen
#-User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    roles = db.relationship('Role', secondary='user_role', back_populates='users')
    pflanzen = db.relationship('Pflanze', backref='publisher', lazy='dynamic')
    
    @hybrid_property
    def is_admin(self):
        return self.has_role('admin')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def has_role(self, role):
        return bool(
            Role.query
            .join(Role.users)
            .filter(User.id == self.id)
            .filter(Role.name == role)
            .count() == 1
        )

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#-Pflanze
class Pflanze(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=True)
    wissenschaft_name = db.Column(db.String(40), nullable=True)
    familie = db.Column(db.String(40), nullable=True)
    vegetationszone = db.Column(db.String(40), nullable=True)
    will_sonne = db.Column(db.String(40), nullable=True)
    gefahr = db.Column(db.String(40), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))