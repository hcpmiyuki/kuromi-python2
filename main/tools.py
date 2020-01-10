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
    if ("マイメロ" in base_list) or ("お願い" in base_list) or ("おねがい" in base_list):
        if ("バカ" in base_list) or ("ばか" in base_list) or ("馬鹿" in base_list) or ("アホ" in base_list) or ("あほ" in base_list) or ("嫌い" in base_list) or ("嫌う" in base_list) or ("きらい" in base_list) or ("キライ" in base_list) or ("キモイ" in base_list) or ("きもい" in base_list) or ("キモい" in base_list):
            sound("そんな、嬉しいー.mp3", 3)
            kuromi_status = "heart"
            print("そんな、嬉しいー")
        else:
            kuromi_status = "angry"
            sound("アタイが一番嫌いな言葉を使いやがって.mp3", 4)
            print("アタイが一番嫌いな言葉を使いやがって")
    elif ("バカ" in base_list) or ("ばか" in base_list) or ("馬鹿" in base_list) or ("アホ" in base_list) or ("あほ" in base_list) or ("嫌い" in base_list) or ("嫌う" in base_list) or ("きらい" in base_list) or ("キライ" in base_list) or ("キモイ" in base_list) or ("きもい" in base_list) or ("キモい" in base_list):
        num = random.randint(0, 1)
        kuromi_status = "angry"
        if num == 0:
            sound("なに冗談言ってんのさ.mp3", 3)
            print("なに冗談言ってんのさ")
        else:
            sound("とぼけんな、すべての原因はお前にあるんだ.mp3", 4)
            print("とぼけんな、すべての原因はお前にあるんだ")
 
    elif ("かわいい" in base_list) or ("可愛い" in base_list) or ("カワイイ" in base_list) or\
            ("すごい" in base_list) or ("大好き" in base_list) or ("だいすき" in base_list) or ("最高" in base_list):
        num = random.randint(0, 4)
        if num == 0 or num == 1:
            sound("ありがとう.mp3", 3)
            print("ありがとう")
        elif num == 2:
            sound("なに冗談言ってんのさ.mp3", 3)
            kuromi_status = "angry"
            print("なに冗談言ってんのさ")
        elif num == 3:
            sound("やっぱりこうじゃなきゃ、クロミちゃんじゃないもんね.mp3", 4)
            kuromi_status = "good"
            print("やっぱりこうじゃなきゃ、クロミちゃんじゃないもんね")
        else:
            sound("そんな、嬉しいー.mp3", 3)
            print("そんな、嬉しいー")
            kuromi_status = "heart"
    elif ("ただいま" in base_list):
        sound("遊びに来てくれたな、嬉しいな、今紅茶を入れるね.mp3", 4)
        print("おかえり")
    elif ("疲れる" in base_list) or ("つかれる" in base_list):
        sound("こういう時は甘くしちゃえば大丈夫だろう.mp3", 4)
        print("おつかれさま♪")
    elif ("遊ぶ" in base_list) or ("あそぶ" in base_list):
        sound("チュロランチュロランてへー.mp3", 3)
        print("いっしょにあそぼ〜♪")
    elif ("おやすみ" in base_list) or ("お休み" in base_list):
        sound("うん.mp3", 3)
        print("うん")
        kuromi_status = "goodnight"
    elif ("会う" in base_list) or ("会える" in base_list):
        sound("遊びに来てくれたな、嬉しいな、今紅茶を入れるね.mp3", 4)
        print("嬉しいな")
    elif ("頑張る" in base_list) or ("がんばる" in base_list) or ("できる" in base_list):
        sound("わー！かっこいい！.mp3", 3)
        kuromi_status = "heart"
    elif ("歌" in base_list) or ("うた" in base_list) or ("歌う" in base_list):
        num = random.randint(1, 3)
        sound("歌" + str(num) + ".mp3", 20)
        # ランダムで歌わせる
        print("歌ってあげる")
    else:
        num = random.randint(0,1)
        if num == 0:
            sound("うふふ.mp3", 3)
            print("うふふ")
        else:
            sound("わ、なんか言ったかい.mp3", 3)
            print("わ、なんか言ったかい")
    return kuromi_status


def sound(voice_name, voice_time):
    pygame.mixer.init() #初期化

    pygame.mixer.music.load('./voices/' + voice_name) #読み込み
    pygame.mixer.music.play(1) #再生

    time.sleep(voice_time)

    pygame.mixer.music.stop() #終了
