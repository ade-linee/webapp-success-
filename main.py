from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
  return render_template("home.html")

@app.route("/results", methods=["POST", "GET"]) 
def marks():
  mark = request.form["mye"]
  desired = request.form["desired"]
  promomark = (int(desired) - (0.2*(int(mark))))/0.8
  return render_template("results.html", results=promomark)

if __name__ == "__main__":
  app.run() 
