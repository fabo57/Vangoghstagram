# -*- coding: utf8 -*-
# Diccionario
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
#def api_instagram ():
#    headers = {
#curl-F 'client_id=d2b00994cc8a4995989cfd98bb0004d3' \
#    -F 'client_secret=03f128d0ccf3492e91d203d25ddc02bf ' \
#    -F 'grant_type=authorization_code' \
#    -F 'redirect_uri=http://127.0.0.1' \
#    -F 'code=cff2fc0dca2c4c468a18bb8656b84615' \
#    }
#    reponse = requests.get("https://api.instagram.com/v1/tags/nofilter/media/recent?access_token=ACCESS_TOKEN")
def hello():
        return "Hola a todos"
@app.route("/home")
def home():
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
