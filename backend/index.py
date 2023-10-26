from config import app, db, Pflanze
from flask import Flask, render_template, redirect, url_for, request
import forms


@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def start_page():
    
    #wenn wir uns im Eingabe-Formular für die Pflanzen befinden und alle Daten-Validierungen
    #dieses Formulars erfolgreich waren
    if forms.PflanzeForm().validate_on_submit():
        if request.form.get('post_header') == 'update pflanze':
            pflanze_form = forms.PflanzeForm()
            Pflanze.query.filter_by(id =      
                request.form.get('pflanze_to_update')).update({
                         'name' : pflanze_form.name.data,
                         'wissenschaft_name' : pflanze_form.wissenschaft_name.data,
                         'familie' : pflanze_form.familie.data,
                         'vegetationszone' : pflanze_form.vegetationszone.data,
                        'will_sonne' : pflanze_form.will_sonne.data,
                         'gefahr' : pflanze_form.gefahr.data,})
            
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
                        pflanze_form = forms.PflanzeForm()
                        )


if __name__ == "__main__": # Ausführen
    app.run(debug=True) # Starten