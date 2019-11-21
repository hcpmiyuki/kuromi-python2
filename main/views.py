import flask 
from flask import Flask, Response, request, jsonify
from main import app

@app.route('/')
def show_entries():
    return 'Hello, World!'

@app.route('/msg', methods=['POST'])
def get_msg():
    # msg = request.get_data()
    msg = request.form['msg']
    if msg != "":
        print(msg)
        return jsonify({'message':msg})
    else:
        return jsonify({'message':'失敗'})
