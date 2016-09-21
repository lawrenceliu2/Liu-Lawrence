from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso"

@app.route("/gorillas")
def foo():
    return "Harambe"

@app.route("/ostrich")
def juice():
    return "Ostrich juice"

if __name__=="__main__":
    app.run()
