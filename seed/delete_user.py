import sys
sys.path.append('C:\\Users\\Claudia\\Documents\\Informatik-Studium\\temp\\venv\\backend')

from config import app
from models import User
from config import db

app.app_context().push()

user = User.query.get(7)
db.session.delete(user)
db.session.commit()