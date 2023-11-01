from config import app, db, Pflanze
from flask import render_template, redirect, url_for, request
import forms

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