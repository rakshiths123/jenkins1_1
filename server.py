from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
    return "Rakshith S - 1BM20IS117"

if _name_ == "_main_":
    app.run(host='0.0.0.0')
