#!/usr/bin/python

import util.testmod

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "No hablo queso"

@app.route("/occupations")
def jobs():
    joblist = util.testmod.randjob().items()
    return render_template("Occupations.html", jobs = "Occupations", diction = joblist, rand = util.testmod.weightedrand(util.testmod.randjob()))

@app.route("/test")
def testing():
    return util.testmod.goo()


if __name__=="__main__":
    app.debug = True
    app.run()
