from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import daten

app = Flask("__name__")

# Datei in Klammer anpassen, dass hier main.html geladen wird
@app.route('/home')
# @app.route('/home')
def home():
   return render_template('main.html')

@app.route('/upload')
def upload():
    return render_template('student.html')


#Hier soll das Resultat von result.html geladen werden
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      
      print(result['Name'])
      print(result['Vorname'])
      print(result['Fach'])
      print(result['Note'])

      #Speichern des Resultats als json-File
      def speichern(datei, key, value):
        try:
            with open(datei) as open_file:
                datei_inhalt = json.load(open_file)
            except FileNotFoundError:
                datei_inhalt = {}

            print(datei_inhalt)

            with open(datei, "w") as open_file:
                json.dump(datei_inhalt, open_file)

      def resultat_speichern(resultat):
        datei_name = "resultat.json"
        zeitpunkt = datetime.now()
        speichern(date_name, zeitpunkt, resultat)
        return zeitpunkt, resultat

      def resultat_laden():
          datei_name = "resultat.json"

          try: 
            with open(datei_name) as open_file:
                datei_inhalt = json.load(open_file)
          except FileNotFoundError:
            datei_inhalt = {}

            return datei_inhalt




      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True, port=5000)
