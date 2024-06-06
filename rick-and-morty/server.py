from flask import Flask, redirect, render_template, session
from pprint import pprint
import requests

app = Flask(__name__)
app.secret_key = "5f699dabd4a1fe43e1584a60c0d1234c343f5ab7bd7ef8e6989c3f7345e92749"


@app.route("/")
def index():

    if "url" not in session:
        session["url"] = "https://rickandmortyapi.com/api/character"

    r = requests.get(session["url"])
    results = r.json()["results"]
    info = r.json()["info"]
    session["prev"] = info["prev"]
    session["next"] = info["next"]

    characters = []
    for result in results:
        character = {}
        character["image"] = result["image"]
        character["name"] = result["name"]
        character["species"] = result["species"]
        character["gender"] = result["gender"]
        characters.append(character)

    return render_template("index.html", characters=characters)


@app.get("/prev")
def prev():
    session["url"] = session["prev"]
    return redirect("/")


@app.get("/next")
def next():
    session["url"] = session["next"]
    return redirect("/")


@app.get("/clear")
def clear():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5150)
