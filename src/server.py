from flask import Flask

app = Flask(__name__)


@app.route('/mem', methods = ['POST'])
def index():
    return {"HOLA" : "TEST"}

if __name__ == "__main__":
    app.run(debug=True)