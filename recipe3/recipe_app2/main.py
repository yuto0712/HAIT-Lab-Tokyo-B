from keras.models import model_from_json
import numpy as np
import os, random
from keras.preprocessing.image import img_to_array, load_img
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from django.core.files.storage import default_storage
from django.conf import settings
import tensorflow as tf



def recipe(text_path):
    f = open(text_path)
    f2 = f.readlines()
    f3 = []
    for i in range(len(f2)):
        f3.append(f2[i].rstrip("\n"))
    print(f3)
    a = '人参'
    b = '肉'
    c = '玉ねぎ'
    d = 'じゃがいも'
    e = 'トマト'
    """
    a in listが真(listの中にaの要素が含まれている)ならifが実行されて、偽ならelseが実行される。
    a not in listとも書けてlistの中にaが含まれていない場合が真になる。
    """

    if a in f3 and b in f3 and d in f3:
        return "カレー"
    elif b in f3 and d in f3:
        return "肉じゃが"
    elif a in f3 and c in f3 and e in f3:
        return "サラダ"
    else:
        return "作れるものはありません"

def recipe2(text_path):
    import numpy as np
    import os
    import cv2
    import matplotlib.pyplot as plt
    import re
    import sys


    f = open(text_path)
    f2 = f.readlines()
    search_words = []
    for i in range(len(f2)):
        search_words.append(f2[i].rstrip("\n"))

    # 食材リストと照らし合わせてリストに照合するものがレシートのデータに存在すれば
    # その食材をsearch_wordsに加える
    print(search_words)
    search_words.sort(key=len, reverse=True)
    search_words = search_words[:3]
    print("search_words is ....", search_words, "\n")
    url = "https://cookpad.com/search/{:s}%E3%80%80{:s}%E3%80%80{:s}".format(search_words[0],
                                                         search_words[1],search_words[2])
    # ここからスクレイピング
    import requests
    import lxml.html
    import os
    import cv2
    import matplotlib.pyplot as plt


    def save_image(filename, image):
        with open(filename, "wb") as fout:
            fout.write(image)

    # 3つの検索ワードで検索する場合、このようなURLになる。
    url = "https://cookpad.com/search/{:s}%E3%80%80{:s}%E3%80%80{:s}".format(search_words[0],
                                                         search_words[1],search_words[2])
    # レシピ検索のhtmlを取得
    response = requests.get(url)
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    url_list = []
    # 検索の上位にあるレシピのurlを獲得する
    for a in root.cssselect('a.recipe-title'):
        url = a.get('href')
        url_list.append(url)

    path_w = settings.BASE_DIR + r'/save_data/text2.txt'
    with open(path_w, mode='a') as f:

        response = requests.get(url_list[0])
        root = lxml.html.fromstring(response.content)
        recipe_title = root.cssselect("title")[0].text_content()
        f.write(recipe_title + "\n")
        ingridient_name = root.cssselect("span.name")
        ingridient_amount = root.cssselect("div.ingredient_quantity")
        step = root.cssselect("p.step_text")

    ## os.system("wget {:s} -o picture.jpg".format(src))

        f.write('必要な材料\n')
        for i in range(len(ingridient_name)):
            f.write(ingridient_name[i].text_content() + "\t" + ingridient_amount[i].text_content() + "\n")
        for i in range(len(step)):
            f.write(str(i+1) + ",\t" + step[i].text_content() + "\n")

        # 画像ファイルの読み込みと表示
        src = root.cssselect("#main-photo > img")[0].get('src')
        src = re.findall(r'https://.+\.jpg', src)[0]
        img_response = requests.get(src, timeout=10, stream=False)
        name_search = re.findall(r'\/([a-zA-Z0-9:.=_-]*jpg|jpeg|JPG|JPEG)', src)
        img_name = name_search[0]
        save_image('./pictures/' + img_name, img_response.content)
        recipe_image = cv2.imread("./pictures/"+img_name)
    f2 = open(path_w)
    data = f2.read()
    #lines = data.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
    return data
