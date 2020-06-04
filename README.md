# Projektidee:

## Ausgangslage: 
Ich studiere DBM an der FHGR. Leider ist das Rechnen des Notendruchschnitts relativ mühesam, sehr viele Module anstehen und demnach die Übersicht über den Durchschnitt aller Noten sehr schwer zu behalten ist. Die Noten zählen alle 100% und sollten somit gleich gewichtet werden.

## Funktion / Projektidee: 
Der Notenrechner soll es erlauben für verschiedene Studenten die Noten für Fächern in verschiedenen Semestern zu erfassen. Es soll schlussendlich eine Übersicht aller bereits erfassten Noten eines Studenten vorhanden sein. Zusätzlich soll für einen erfassten Studenten der Durchschnitt eines Semesters berechnet werden. Des Weiteren soll es auch möglich sein, den Durchschnitt des gesamten bisherigen Studiums, also aller bisher erfassten Noten, zu berechnen.

## Workflow: 
Im Register Upload können die benötigten Daten erfasst werden. Im Register Dashboard kann der Namen und Vornamen eines bereits erfassten Studenten eingegeben werden und es werden sämtliche bereits erfassten Noten ausgegeben. Im Register Semesterschnitt kann der Schnitt für ein Semester eines Studenten berechnet werden. Im Register Studiumsschnitt kann der Durchschnitt aller bisher erfassten Noten eines Studenten berechnet werden.

## Test-Cases / Funktionsbeschrieb: 
### Startseite: 
- Durch das Anwählen des Buttons "START UPLOADING!" soll der User auf die Upload-Page (Register Upload) weitergeleitet werden. 
- Durch das Anwählen des Buttons "Dashboard" soll der User auf die Dashboard-Page (Register Dashboard) weitergeleitet werden.
- Durch das Anwählen des Buttons "Semesterschnitt" soll der User auf die Semesterschnitt-Page (Register Semesterschnitt) weitergeleitet werden. 
- Durch das Anwählen des Buttons "Studiumsschnitt" soll der User auf die Studiumsschnitt-Page (Register Studiumsschnitt) weitergeleitet werden.

### Upload-Page: 
- Das Formular soll mit beliebigen Zeichen ausgefüllt werden können. 
- Falls ein Feld nicht ausgefüllt wird, soll beim Drücken auf den Upload-Button eine Fehlermeldung aufkommen, da sämtliche Felder für einen Upload ausgefüllt werden sollen. 
- Wenn das Formular komplett ausgefüllt wurde und der Upload durch den Upload-Button bestätigt wurde, werden die soeben erfassten Daten nochmals angezeigt. 
    - Auf der Page der soeben erfassten Daten soll der User durch das Anwählen des Buttons "Erneuter-Upload!" wieder auf die Upload-Page weitergeleitet werden. 

### Dashboard-Page: 
- Das Formular soll mit beliebigen Zeichen ausgefüllt werden können. 
- Falls ein Feld nicht ausgefüllt wird, soll beim Drücken auf den Anzeigen-Button eine Fehlermeldung aufkommen, da sämtliche Felder ausgefüllt werden müssen.
- Sollten die eingegebenen Daten nicht erfasst sein oder nicht mit den erfassten Daten übereinstimmen, soll eine Fehlermeldung aufkommen. 
    - Mit dem Button "Zurück" auf der Page der Fehlermeldung soll der User wieder zurück auf die Dashboard-Page geleitet werden. 

### Semesterschnitt-Page: 
- Das Formular soll mit beliebigen Zeichen ausgefüllt werden können. 
- Falls ein Feld nicht ausgefüllt wird, soll beim Drücken auf den Berechnen-Button eine Fehlermeldung aufkommen, da sämtliche Felder ausgefüllt werden müssen.
- Wenn das Formular komplett ausgefüllt wurde und der die erfassten Daten durch den Berechnen-Button bestätigt wurde und die Daten mit den erfassten Daten übereinstimmen, wird der Schnitt dieses Studenten für dieses Semester auf zwei Stellen nach dem Komma gerundet angezeigt. 
- Sollten die eingegebenen Daten nicht erfasst sein oder nicht mit den erfassten Daten übereinstimmen, soll eine Fehlermeldung aufkommen. 
    - Mit dem Button "Zurück" auf der Page der Fehlermeldung soll der User wieder zurück auf die Semesterschnitt-Page geleitet werden. 

### Studiumsschnitt-Page:
- Das Formular soll mit beliebigen Zeichen ausgefüllt werden können. 
- Falls ein Feld nicht ausgefüllt wird, soll beim Drücken auf den Berechnen-Button eine Fehlermeldung aufkommen, da sämtliche Felder ausgefüllt werden müssen.
- Wenn das Formular komplett ausgefüllt wurde und der die erfassten Daten durch den Berechnen-Button bestätigt wurde und die Daten mit den erfassten Daten übereinstimmen, wird der Schnitt dieses Studenten für sämtliche bisher erfassten Noten auf zwei Stellen nach dem Komma gerundet angezeigt. 
- Sollten die eingegebenen Daten nicht erfasst sein oder nicht mit den erfassten Daten übereinstimmen, soll eine Fehlermeldung aufkommen. 
    - Mit dem Button "Zurück" auf der Page der Fehlermeldung soll der User wieder zurück auf die Studiumsschnitt-Page geleitet werden.

## Ablaufdiagramm:
![alt text](https://github.com/francomalacrida/Prog2/blob/master/Ablaufdiagramm.jpg)