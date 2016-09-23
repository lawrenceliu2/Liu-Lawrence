#!/usr/bin/python

import random

from flask import Flask, render_template
app = Flask(__name__)

def randjob():
    #store the data from the csv into a list, s
    a = open ('occupations.csv', 'r')
    s = a.read()
    s = s.split('\n')
    #remove the titles and blank data
    s = s[1:len(s)-2]

    #make a dictionary
    dict = {}
    for job in s:
        #the Occupation is the string job up to the last comma, the percent is whats after the last comma
        if (job[0] == '"'):
            dict[job[1:job.rfind('"')]] = float(job[job.rfind(',')+1:])
        else:
            dict[job[:job.rfind(',')]] = float(job[job.rfind(',')+1:])
    return dict

def weightedrand(dict):
    r = random.random() * 99.8
    start = 0.0
    for job in dict:
        stop = start + dict[job]
        if (start <= r < stop):
            return job
        else:
            start = stop

@app.route("/")
def hello_world():
    return "No hablo queso"

@app.route("/occupations")
def jobs():
    joblist = (randjob()).items()
    return render_template("Occupations.html", jobs = "Occupations", diction = joblist, rand = weightedrand(randjob()))


if __name__=="__main__":
    app.run()
