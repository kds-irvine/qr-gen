#!/usr/bin/env python

import os
import qrcode
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, render_template, request, Response, session
from io import BytesIO

import requests 
import json
import traceback
import image
import base64

app = Flask(__name__)

@app.route('/')
def showForm():
    return render_template("form.html"), 200, {'Content-Type': 'text/html'}

@app.route('/qr', methods=['POST'])
def qr():
    data = request.form
    qrstr = 'lic:%s;vin:%s;unit:%s;mfg:%s;model:%s;hp:%s;year:%s;dia:%s;kit:%s' % \
        (data['lic'],data['vin'],data['unit'],data['engMauf'],data['engModel'],
        data['engHP'],data['engYear'],data['exhDia'],data['exhKit'])
    img = qrcode.make(qrstr,
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    buf = BytesIO()
    img.save(buf)
    qrval = base64.b64encode(buf.getvalue()).decode('ascii')
    print(request.form)
    
    return render_template("qr.html",qr=qrval), 200, {'Content-Type': 'text/html'}

@app.route('/qrstr', methods=['POST'])
def qrstr():
    data = request.form
    qrstr = 'lic:%s;vin:%s;unit:%s;mfg:%s;model:%s;hp:%s;year:%s;dia:%s;kit:%s' % \
        (data['lic'],data['vin'],data['unit'],data['engMauf'],data['engModel'],
        data['engHP'],data['engYear'],data['exhDia'],data['exhKit'])
    img = qrcode.make(qrstr,
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    buf = BytesIO()
    img.save(buf)
    qrval = base64.b64encode(buf.getvalue()).decode('ascii')
    
    return qrval

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9100,debug=False)