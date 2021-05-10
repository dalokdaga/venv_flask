from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'mensaje':"Hola mundo", 'success': True}

@app.route('/api')
def checkapi():
    return {'mensaje':"API LISTA", 'success': True}

@app.route('/api/saludo')
def checkapisaludo():
    return {'mensaje':"Api, Hola mundo", 'success': True}

if __name__ == '__main__':
    app.run(debug=True)
