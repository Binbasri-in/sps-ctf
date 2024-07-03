from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/secret")
def secret_page():
    return render_template("secret.html")

if __name__ == "__main__":
    app.run(debug=True)

