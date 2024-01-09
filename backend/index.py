from config import app, db, Pflanze, User
from flask import render_template, redirect, url_for, request, flash
import forms
from flask_login import current_user, login_user


#Registrierungs-Seite
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(message='Glückwunsch, Sie haben sich erfolgreich registriert!', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#Login-Seite
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('start_page'))
    return render_template('login.html', title='Sign In', form=form)

#TODO: Logging Users Out
#TODO: Requiring Users To Login
#TODO: Showing The Logged In User in Templates


#Upload-Seite
@app.route('/pflanze/<id>/upload', methods = ['GET', 'POST'])
def upload_file(id):
    pflanze_form = forms.PflanzeForm()
    if request.method == 'POST':
        f = request.files['bild']
        str = app.config['UPLOAD_FOLDER'] + '/Pflanze_' + id + '.jpg'
        f.save(str)
        return redirect(url_for('start_page'))
    else:
        return render_template('file_upload.html',
                               pflanze_form = pflanze_form,
                               id = id)

#Seite mit der Detailsicht einer Pflanze
@app.route('/Pflanze/<id>', methods = ['GET', 'POST'])
def form_pflanze_details(id):
    pflanze_form = forms.PflanzeForm()
    pflanzen = db.session.query(Pflanze).filter(Pflanze.id == id)
    if 'aendern' in request.form:
        for pflanze in pflanzen:
            pflanze.name = pflanze_form.name.data
            pflanze.wissenschaft_name = pflanze_form.wissenschaft_name.data
            pflanze.familie = pflanze_form.familie.data
            pflanze.vegetationszone = pflanze_form.vegetationszone.data
            pflanze.will_sonne = pflanze_form.will_sonne.data
            pflanze.gefahr = pflanze_form.gefahr.data
            
            db.session.commit()
            
            return redirect(url_for('start_page'))
    elif 'abbrechen' in request.form:
            return redirect(url_for('start_page'))
    elif 'loeschen' in request.form:
        
            db.session.query(Pflanze).filter_by(id = id).delete()
            db.session.commit()
        
            return redirect(url_for('start_page'))
    elif 'bild_hochladen' in request.form:
        return redirect(url_for('upload_file', id=id))
    else:
        for pflanze in pflanzen:
            pflanze_form.name.data = pflanze.name
            pflanze_form.wissenschaft_name.data = pflanze.wissenschaft_name
            pflanze_form.familie.data = pflanze.familie
            pflanze_form.vegetationszone.data = pflanze.vegetationszone
            pflanze_form.will_sonne.data = pflanze.will_sonne
            pflanze_form.gefahr.data = pflanze.gefahr
            return render_template('pflanze.html',
                            pflanzen = pflanzen,
                            pflanze_form = pflanze_form
                        )
        

#Übersichts-Seite
@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def start_page():
    
    #wenn wir uns im Eingabe-Formular für die Pflanzen befinden und alle Daten-Validierungen
    #dieses Formulars erfolgreich waren
    pflanze_form = forms.PflanzeForm()
    if pflanze_form.validate_on_submit():
        if request.form.get('post_header') == 'update pflanze':
            #pflanze_form = forms.PflanzeForm()
            pflanze = Pflanze.query.filter_by(id = request.form.get('pflanze_to_update')).first()
            
            #Pflanze.query.filter_by(id =      
                #request.form.get('pflanze_to_update')).first() 
            pflanze_form= forms.PflanzeForm(pflanze)
            pflanze.name= pflanze_form.name.data
            pflanze.wissenschaft_name =pflanze_form.wissenschaft_name.data
            pflanze.familie = pflanze_form.familie.data
            pflanze.vegetationszone = pflanze_form.c.data
            pflanze.will_sonne = pflanze_form.will_sonne.data
            pflanze.gefahr = pflanze_form.gefahr.data

                        
            db.session.commit()
            

            #Seiten-Refresh
            return redirect(url_for('start_page'))
        
        else:
        
            
            #Instanz der Pflanze-Klasse anlegen
             pflanze_form = forms.PflanzeForm()
             pflanze = Pflanze(  name = pflanze_form.name.data,
                                wissenschaft_name = pflanze_form.wissenschaft_name.data,
                                familie = pflanze_form.familie.data,
                                vegetationszone = pflanze_form.vegetationszone.data,
                                will_sonne = pflanze_form.will_sonne.data,
                                gefahr = pflanze_form.gefahr.data)

            #Instanz der Pflanze-Klasse in die Datenbank inserten
        db.session.add(pflanze)
        db.session.commit()
        
        
            #Seiten-Refresh
        return redirect(url_for('start_page'))
    
    pflanzen = Pflanze.query.all()

    return render_template('index.html',
                        pflanzen = pflanzen,
                        pflanze_form = pflanze_form
                        )


if __name__ == "__main__": # Ausführen
    app.run(debug=True) # Starten