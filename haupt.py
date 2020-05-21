from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from datetime import datetime
import json

app = Flask("__name__")


#Remdern des main.html Templates
@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')

# write modus "w"
def write_data_to_json(file_name, daten):
    with open(file_name, "w") as open_file:
        json.dump(daten, open_file)


def read_data_from_json(file_name):
    try:
        with open(file_name, "r") as open_file:
            mein_eingelesenes_dict = json.load(open_file)
            return mein_eingelesenes_dict
    except Exception:
        return []


# Hier soll das Resultat von result.html geladen werden
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


#Hier soll der Durchschnitt von einem Studenten für ein Semester berechnet.
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
                neue_auswahl = {
                "Name": name,
                "Vorname": vorname,
                "Semester": semester,
                "Schnitt": semesterschnitt
                }

        return render_template("durchschnitt.html", data=neue_auswahl)
    return render_template('auswahl.html')

#Hier soll der Durchschnitt von einem Studenten für das gesamte Studium berechnet.
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
                gesamter_schnitt = {
                "Name": name,
                "Vorname": vorname,
                "Schnitt des gesamten Studiums": studiumsschnitt
                }

        return render_template("gesamtschnitt.html", gesamt=gesamter_schnitt)
    return render_template('auswahl2.html')
 
 # Hier sollen alle bereits erfassten Noten eines Studenten dargestellt werden.
@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        uebersicht = request.form
        print(uebersicht)
        uebersicht_voneinem = read_data_from_json("notenrechner.json")
        name = uebersicht['Name']
        vorname = uebersicht['Vorname']

        for eintrag in uebersicht_voneinem:
            if eintrag["name"] == name and eintrag["vorname"] == vorname:
                alle_dicts = {
                "name": name,
                "vorname": vorname,
                "semester": semester,
                "fach": fach,
                "note": note
                }

        return render_template("dashboard.html", alle_voneinem=alle_dicts)
    return render_template("auswahl3.html")

if __name__ == '__main__':
    app.run(debug = True, port=5000)
