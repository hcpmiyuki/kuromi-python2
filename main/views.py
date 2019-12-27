#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from flask import Flask, Response, request, jsonify
from main import app
from main.tools import *

@app.route('/hello')
def show_entries():
    return 'Hello, World!'

@app.route('/msg', methods=['POST'])
def get_msg():
    # msg = request.get_data()
    msg = request.form['msg']
    if msg != "":
        kuromi_status = talk(msg)
        return jsonify({'kuromi_status':kuromi_status})
    else:
        return jsonify({'kuromi_status':'失敗'})
