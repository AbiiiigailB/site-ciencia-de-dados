from flask import Flask

app = flask(__name__, template_folder ="sitenciencia/templates", static_folder = "sistencia/static")

def index():
    return "bom dia, professor."

@app.route("/home")
def index ():
    return "<h1>bom dia, professor!<h1>"
