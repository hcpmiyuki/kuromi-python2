from flask import Flask
from janome.tokenizer import Tokenizer
import pygame.mixer
import time
import random

t = Tokenizer()

def talk(msg):
    base_list = [token.base_form for token in t.tokenize(msg)]
    kuromi_status = "smile"
    print(base_list)
    if ("かわいい" in base_list) or ("可愛い" in base_list) in ("カワイイ" in base_list):
        num = random.randint(0, 3)
        if num == 0:
            sound("ありがとう.mp3")
            print("ありがとう")
        else:
            sound("バカ言ってんじゃないよ.mp3")
            kuromi_status = "angry"
            print("バカ言ってんじゃないよ")
    elif ("ただいま" in base_list):
        sound("遊びに来てくれたな、嬉しいな、今紅茶を入れるね.mp3")
        print("おかえり")
    elif ("疲れる" in base_list) or ("つかれる" in base_list):
        sound("こういう時は甘くしちゃえば大丈夫だろう.mp3")
        print("おつかれさま♪")
    elif ("遊ぶ" in base_list) or ("あそぶ" in base_list):
        sound("チュロランチュロランてへー.mp3")
        print("いっしょにあそぼ〜♪")
    elif ("おやすみ" in base_list) or ("お休み" in base_list):
        num = random.randint(0, 1)
        if num == 0:
            sound("うん.mp3")
            print("うん")
        else:
            sound("バイバイ.mp3")
            print("バイバイ")
        kuromi_status = "goodnight"
    elif ("会う" in base_list):
        # 会いにきてない
        print("会いたくない")
    elif ("歌" in base_list) or ("うた" in base_list):
        # ランダムで歌わせる
        print("歌ってあげる")
    else:
        sound("うふふ.mp3")
        print("うふふ")
    return kuromi_status


def sound(voice_name):
    pygame.mixer.init() #初期化

    pygame.mixer.music.load('./voices/' + voice_name) #読み込み
    pygame.mixer.music.play(1) #再生

    time.sleep(3)

    pygame.mixer.music.stop() #終了
