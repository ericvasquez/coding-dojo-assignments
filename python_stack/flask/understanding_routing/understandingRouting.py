from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def say_hi(name):
    return "Hi " + name + "!"

@app.route("/repeat/<int:number>/<message>")
def repeat(number, message):
    messages = ""
    for i in range(0, number, 1):
        messages+=message + " "
    return messages

if __name__=="__main__":
    app.run(debug=True)