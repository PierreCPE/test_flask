from flask import Flask, render_template, request
import serial
import time

# Configuration de la liaison série
ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

# Initialisation de l'application Flask
app = Flask(__name__)

# Définition de la route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Définition de la route pour envoyer le message "avance"
@app.route('/send_avance')
def send_avance():
    message = "avance\n"
    ser.write(message.encode('utf-8'))
    time.sleep(1)
    return "Message envoyé : avance"

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True, host='172.20.10.2')