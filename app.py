# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 17:58:15 2021

@author: Srinu
"""

from flask import Flask , render_template , request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods = ["POST","GET"])
def predict():
    if request.method == "POST":
        ms = request.form["ms"]
        ad = request.form["as"]
        rd = request.form["rd"]
        s = request.form["s"]
        data = [[ms,ad,rd,s]]
        #model.predict(sc.transform(ct.transform([[]])))
    return render_template("index.html",value = str(data))
        
if __name__ == "__main__":
    
    app.run(debug = True)
