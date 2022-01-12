#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template

app = Flask(__name__)

app.secret_key= "random random RANDOM!"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/")
def index():
    return render_template("hellobasic.html")

# pull in the value of score as an int
@app.route("/challenge")
def show_groups():
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("challenge.html", hosts=groups)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
