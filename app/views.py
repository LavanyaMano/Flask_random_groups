from flask import render_template
from app import app
from os import path
from app.lib.random_groups import RandomGroups

@app.route("/")
@app.route("/index")

def index():

    #random_group=run()
    random_group =RandomGroups()
    random_g = random_group.teamed_groups


    return render_template("index.html",random_group=random_g)