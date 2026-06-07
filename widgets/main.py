from flask import Flask, render_template, request, jsonify
import logging
import json
import pathlib

import random

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/timer")
# def chat():
#     if request.is_json:
#         lines = dict()
#         for i in range(10):
#             lines[str(i)] = str(time())
#         logging.debug(lines)
#         return jsonify({"lines": lines})
#
#     return render_template("chat.html")

@app.route("/chat")
def chat():
    if request.is_json:
        if pathlib.Path("../common/chat_history.json").exists():
            with open("../common/chat_history.json", "r", encoding="utf8") as f:
                lines = json.load(f)
        else:
            lines = []

        return jsonify({"lines": lines})

    return render_template("chat.html")

@app.route("/follow")
def follow():
    if request.is_json:
        if pathlib.Path("../common/follow_history.json").exists():
            with open("../common/follow_history.json", "r", encoding="utf8") as f:
                followers = json.load(f)
        else:
            followers = []

        return jsonify({"followers": followers})

    return render_template("follow.html")

@app.route("/todo")
def todo():
    if request.is_json:
        if pathlib.Path("../common/objetivos.json").exists():
            with open("../common/objetivos.json", "r", encoding="utf8") as f:
                todo = json.load(f)
        else:
            todo = {}

        return jsonify({"todo": todo})

    return render_template("todo.html")

@app.route("/followme")
def followme():
    if request.is_json:
        messages = [
            "Siga-me!",
            "Lives de Programação todas as noites!",
            "💖"
        ]
        msg = random.choice(messages)
        return jsonify({"text": msg})
    return render_template("followme.html")


app.run()
