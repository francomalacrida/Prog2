from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from datetime import datetime
import json

app = Flask("__name__")

# Rendern der versch. Templates, für url_for
@app.route('/')
@app.route('/home')
def home():
   return render_template('main.html')

@app.route('/upload')
def upload():
    return render_template('student.html')

@app.route('/durchschnitt')
def auswahl():
    return render_template('auswahl.html')

#write modus "w"
def write_data_to_json(file_name, daten):
  with open(file_name, "w") as open_file:
    json.dump(daten,open_file)

def read_data_from_json(file_name):
  try: 
    with open(file_name, "r") as open_file:
      mein_eingelesenes_dict = json.load(open_file)
      return mein_eingelesenes_dict
  except Exception:
    return []   

#Hier soll das Resultat von result.html geladen werden
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      alle_noten = read_data_from_json("notenrechner.json")
      name = result['Name']
      vorname = result['Vorname']
      semester = result['Semester']
      fach = result['Fach']
      note = result['Note']
      neue_noten = {
        "name": name,
        "vorname": vorname,
        "semester": semester,
        "fach": fach,
        "note": note,
      }

      alle_noten.append(neue_noten)
      write_data_to_json("notenrechner.json", alle_noten)

      return render_template("result.html",result = result)

#Hier soll das Resultat von durchschnitt.html geladen werden
@app.route('/durchschnitt',methods = ['POST', 'GET'])
def durchschnitt():
   if request.method == 'POST':
      durchschnitt = request.form
      print(durchschnitt)
      #alle_noten = read_data_from_json("notenrechner.json")
      name = durchschnitt['Name']
      vorname = durchschnitt['Vorname']
      semester = durchschnitt['Semester']
      neue_auswahl = {
        "name": name,
        "vorname": vorname,
        "semester": semester
      }

      return render_template("durchschnitt.html",result = neue_auswahl)   

if __name__ == '__main__':
   app.run(debug = True, port=5000)
