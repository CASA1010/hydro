from main import app,db,Pflanze

app.app_context().push()
db.drop_all()
db.create_all()