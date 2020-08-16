# python structure ::
# library/framework/python.framework/versions/3.8/bin/python3 
#   >> base python which I'll use
# library/framework/python.framework/versions/3.8/bin/pip
#   >> base pip place, where I'll set pkg from pip
# usr/local/bin/python3
#   >> call recent python location through librarys,
#   >> call python3 +pip + frameworks


from flask import Flask
import pandas as pd
import datetime
#for regular expression
import re


# developement server call : python3 -m flask run , basically call 'app.py', 
# can add --host=0.0.0.0 --port=80.
app = Flask(__name__)
@app.route("/")
def home():
    print("logging 1")
    return "Hellow, finally"



@app.route("/hellow/<name>")
def hello(name):
    now = datetime.datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)


    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content =  "Hello there, " + clean_name + "! It's " + formatted_now
    

    return content