from flask import Flask, request

from AWS import Rekognition

app = Flask(__name__)


@app.route('/tarea3-201603047', methods = ['POST'])
def index():
    #Importante para que nuestro servidor entienda peticiones JSON
    request_data = request.get_json()
    Rekognition.DetectLabels(request_data['Imagen64'])
    
    return {"HOLA" : "TEST"}

if __name__ == "__main__":
    app.run(debug=True)
