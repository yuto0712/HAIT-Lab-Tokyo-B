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
    a = 'carrot'
    b = 'meat'
    c = 'onion'
    d = 'potato'
    e = 'tomato'
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
