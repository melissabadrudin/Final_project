#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:11:13 2020

@author: melissabadrudin
"""

#import Flask magic
from flask import Flask

#Flask logic section
#we are creating an object which is a flask app
app = Flask(__name__)

#create routes which is a possible door that our app can expect to be opened
# to do this we need to use decorators -> basicamente é usar um @
#@ calls a python inbuilt function without having to import anything

@app.route('/')

def index():
    #the python logic that will be ran when the route is called
    return "Out of Scope"


#running our Flask app defined above   
if __name__ == "__main__":
    app.run(debug = True)
    
