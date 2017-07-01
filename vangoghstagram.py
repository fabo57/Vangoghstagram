# -*- coding: utf8 -*-
# Diccionario
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def api_instagram ():
    headers = {
    -F client_id='d2b00994cc8a4995989cfd98bb0004d3';
    -F client_secret='03f128d0ccf3492e91d203d25ddc02bf';
    -F grant_type='1766293168.d2b0099.55f84ffadb784a41acb6ef50ab556ab3';
    -F redirect_uri='1766293168';
    -F code=' cff2fc0dca2c4c468a18bb8656b84615'; 
    }
    reponse = requests.get("https://api.instagram.com/v1/tags/nofilter/media/recent?access_token=1766293168.d2b0099.55f84ffadb784a41acb6ef50ab556ab3")
def hello():
        return requests.get
@app.route("/home")
def home():
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
