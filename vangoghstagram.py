# -*- coding: utf8 -*-
# Diccionario
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
    def hola_mundo():
        return "Hola a todos"
