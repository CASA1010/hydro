import sys
sys.path.append('C:\\Users\\Claudia\\Documents\\Informatik-Studium\\temp\\venv')

from backend.config import app
from backend.models import User
from backend.config import db

app.app_context().push()

user = User.query.get(3)
db.session.delete(user)
db.session.commit()