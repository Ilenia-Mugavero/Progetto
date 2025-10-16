from flask import Flask

# Istanzia l'app Flask
app = Flask(__name__)

# Definisci una route
@app.route('/')
def hello_world():
    return 'Hello, World! 👋'

# Esegui il server locale
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
