from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from datetime import datetime
import json

app = Flask("__name__")


#Rendern des main.html Templates, für das Anzeigen der main.html Page
@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')

#Hier wird ein neues Json-File generiert
def write_data_to_json(file_name, daten):
    with open(file_name, "w") as open_file:
        json.dump(daten, open_file)

#Hier wird die Datei gelesen/geladen, falls bestehende Daten vorhanden sind.
#Falls keine Daten verhanden sind, gilt except.
def read_data_from_json(file_name):
    try:
        with open(file_name, "r") as open_file:
            mein_eingelesenes_dict = json.load(open_file)
            return mein_eingelesenes_dict
    except Exception:
        return []


#Mit der Funktion result können Datensätze in das Json-File geladen werden.
#Falls in der app.route "/result" POST-Daten vorhanden sind, wird if ausgeführt. Falls keine POST-Daten vorhanden sind, wird das Template student.html gerendert.
#In student.html ist ein Formular vorhanden, welches ausgefüllt wird und die dort erstellten Daten werden mit der POST-Funktion in das json-File "notenrechner.json" gespeichert und im HTML-File result.html wieder ausgegeben.
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        formulardaten = request.form
        print(formulardaten)
        alle_noten = read_data_from_json("notenrechner.json")
        name = formulardaten['Name']
        vorname = formulardaten['Vorname']
        semester = formulardaten['Semester']
        fach = formulardaten['Fach']
        note = formulardaten['Note']
        neue_noten = {
            "name": name,
            "vorname": vorname,
            "semester": semester,
            "fach": fach,
            "note": note
        }

        alle_noten.append(neue_noten)
        write_data_to_json("notenrechner.json", alle_noten)

        return render_template("result.html", result=formulardaten)
    return render_template('student.html')


#Mit der Funktion durchschnitt soll der Durchschnitt eines Semesters eines erfassten Studenten berechnet werden. 
#Falls in der app.route "/durchschnitt" POST-Daten vorhanden sind, wird if ausgeführt. Falls keine POST-Daten vorhanden sind, wird das Template auswahl.html gerendert.
#In auswahl.html befindet sich ein Formular, in welchem der gewünschte Name, Vorname und das Semester angegeben werden soll. Für diese Angaben wird danach der Schnitt aller erfassten Noten für dieses Semester berechnet und auf zwei Stellen gerundet. Das Resultat wird im File durchschnitt.html gerendert.
@app.route('/durchschnitt', methods=['POST', 'GET'])
def durchschnitt():
    if request.method == 'POST':
        durchschnitt = request.form
        print(durchschnitt)
        gesamte_auswahl = read_data_from_json("notenrechner.json")
        name = durchschnitt['Name']
        vorname = durchschnitt['Vorname']
        semester = durchschnitt['Semester']


        summe_noten = 0
        anzahl_noten = 0
        for eintrag in gesamte_auswahl:
            if eintrag["name"] == name and eintrag["vorname"] == vorname and eintrag["semester"] == semester:
                summe_noten += float(eintrag["note"])
                anzahl_noten += 1
                semesterschnitt = summe_noten/anzahl_noten
                semesterschnitt_gerundet = round(semesterschnitt, 2)
                neue_auswahl = {
                "Name": name,
                "Vorname": vorname,
                "Semester": semester,
                "Schnitt": semesterschnitt_gerundet
                }
            else: #Falls die Eingaben nicht mit den Eingaben im Json-File Notenrechner übereinstimmen, wird die untenstehende Fehlermeldung ausgegeben. 
                fehlermeldung = "Zu den folgenden Eingaben: " + name + " " + vorname + " " + semester + " sind leider noch keine Eingaben gemacht. Prüfe die Rechtschreibung oder erfasse einen Datensatz für diese Eingaben."
                return render_template("fehlermeldung.html", fehlermeldung=fehlermeldung)

        return render_template("durchschnitt.html", data=neue_auswahl)
    return render_template('auswahl.html')


#Mit der Funktion gesamtschnitt soll der Durchschnitt des gesamten Studiums eines erfassten Studenten berechnet werden. 
#Falls in der app.route "/gesamtschnitt" POST-Daten vorhanden sind, wird if ausgeführt. Falls keine POST-Daten vorhanden sind, wird das Template auswahl.html gerendert.
#In auswahl2.html befindet sich ein Formular, in welchem der gewünschte Name, Vorname angegeben werden soll. Für diese Angaben wird danach der Schnitt aller erfassten Noten für alle Semester berechnet und auf zwei Stellen gerundet. Das Resultat wird im File gesamtschnitt.html gerendert.
@app.route('/gesamtschnitt', methods=['POST', 'GET'])
def gesamtschnitt():
    if request.method == 'POST':
        gesamtschnitt = request.form
        print(gesamtschnitt)
        gesamte_auswahl = read_data_from_json("notenrechner.json")
        name = gesamtschnitt['Name']
        vorname = gesamtschnitt['Vorname']

        summe_aller_noten = 0
        anzahl_aller_noten = 0
        for eintrag in gesamte_auswahl:
            if eintrag["name"] == name and eintrag["vorname"] == vorname:
                summe_aller_noten += float(eintrag["note"])
                anzahl_aller_noten += 1
                studiumsschnitt = summe_aller_noten/anzahl_aller_noten
                studiumsschnitt_gerundet = round(studiumsschnitt, 2)
                gesamter_schnitt = {
                "Name": name,
                "Vorname": vorname,
                "Schnitt des gesamten Studiums": studiumsschnitt_gerundet
                }
            else: #Falls die Eingaben nicht mit den Eingaben im Json-File Notenrechner übereinstimmen, wird die untenstehende Fehlermeldung ausgegeben.
                fehlermeldung2 = "Zu den folgenden Eingaben: " + name + " " + vorname + " sind leider noch keine Eingaben gemacht. Prüfe die Rechtschreibung oder erfasse einen Datensatz für diese Eingaben."
                return render_template("fehlermeldung2.html", fehlermeldung2=fehlermeldung2)

        return render_template("gesamtschnitt.html", gesamt=gesamter_schnitt)
    return render_template('auswahl2.html')
 
 # Hier sollen alle bereits erfassten Noten eines Studenten dargestellt werden.
@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        uebersicht = request.form
        print(gesamtschnitt)
        uebersicht_voneinem = read_data_from_json("notenrechner.json")
        name = uebersicht['Name']
        vorname = uebersicht['Vorname']
        liste = [ ]

        for eintrag in uebersicht_voneinem:
            if eintrag["name"] == name and eintrag["vorname"] == vorname:
                liste.append(eintrag["semester"])
                liste.append(eintrag["fach"])
                liste.append(eintrag["note"])
            #else: #Falls die Eingaben nicht mit den Eingaben im Json-File Notenrechner übereinstimmen, wird die untenstehende Fehlermeldung ausgegeben.
                #fehlermeldung3 = "Zu den folgenden Eingaben: " + name + " " + vorname + " sind leider noch keine Eingaben gemacht. Prüfe die Rechtschreibung oder erfasse einen Datensatz für diese Eingaben."
                #return render_template("fehlermeldung3.html", fehlermeldung3=fehlermeldung3)

        return render_template("dashboard.html", liste=liste)
    return render_template("auswahl3.html")

if __name__ == '__main__':
    app.run(debug = True, port=5000)