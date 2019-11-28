import flask 
from flask import Flask, Response, request, jsonify
from main import app
from janome.tokenizer import Tokenizer
import pygame.mixer
import time

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
        print(base_list)
        if "かわいい" in base_list:
            sound("ありがとう.mp3")
            print("ありがとう")
        elif "疲れる" in base_list or "つかれる" in base_list:
            sound("こういう時は甘くしちゃえば大丈夫だろう.mp3")
            print("おつかれさま♪")
        else:
            sound("うふふ.mp3")
            print("うふふ")

        return jsonify({'message':msg})
    else:
        return jsonify({'message':'失敗'})

def sound(voice_name):
    pygame.mixer.init() #初期化

    pygame.mixer.music.load('./voices/' + voice_name) #読み込み
    pygame.mixer.music.play(1) #再生

    time.sleep(3)

    pygame.mixer.music.stop() #終了

