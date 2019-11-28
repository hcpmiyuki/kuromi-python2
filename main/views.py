import flask 
from flask import Flask, Response, request, jsonify
from main import app
from janome.tokenizer import Tokenizer

t = Tokenizer()

@app.route('/')
def show_entries():
    return 'Hello, World!'

@app.route('/msg', methods=['POST'])
def get_msg():
    # msg = request.get_data()
    msg = request.form['msg']
    if msg != "":
        print(msg)
        base_list = [token.base_form for token in t.tokenize(msg)]
        if "かわいい" in base_list:
            print("ありがとう")
        elif "疲れ" in base_list:
            print("おつかれさま♪")
        else:
            print("うふふ")

        return jsonify({'message':msg})
    else:
        return jsonify({'message':'失敗'})
