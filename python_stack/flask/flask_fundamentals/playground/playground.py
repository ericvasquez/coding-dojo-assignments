from flask import Flask, render_template
app = Flask(__name__)
@app.route("/play")
def index():
    return render_template("index.html", times=3, color="rgb(165, 197, 244)")

@app.route("/play/<int:x>")
def more_boxes(x):
    return render_template("index.html", times=x, color="rgb(165, 197, 244)")

@app.route("/play/<int:x>/<color>")
def color_boxes(x, color):
    return render_template("index.html", times=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)


 