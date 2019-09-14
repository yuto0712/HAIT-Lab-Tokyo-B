from keras.models import model_from_json
import numpy as np
import os, random
from keras.preprocessing.image import img_to_array, load_img
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from django.core.files.storage import default_storage
from django.conf import settings
import tensorflow as tf

graph = tf.get_default_graph()
def pred(img_path):
    global get_default_graph
    with graph.as_default():
        batch_size = 32
        file_name = 'vgg16_veg_file'


        # trainディレクトリのフォルダ名の順序通り並べます
        label = ['人参', '肉', '玉ねぎ', 'じゃがいも', 'トマト']
        json_string = default_storage.open('./weight_dir/' + file_name + '.json').read()
        model = model_from_json(json_string)
        model.load_weights(settings.BASE_DIR + r'/media/weight_dir/' + file_name + '.h5')



        #score = model.evaluate_generator(test_generator)
        #print('\n test loss:', score[0])
        #print('\n test acc :', score[1])

        img = load_img(img_path, grayscale=False, target_size=(224,224))


        temp_img_array = img_to_array(img)
        temp_img_array = temp_img_array.astype('float32') / 255.0
        temp_img_array = temp_img_array.reshape((1,224,224,3))

        img_pred = model.predict(temp_img_array)

        path_w = settings.BASE_DIR + r'/save_data/text.txt'
        with open(path_w, mode='a') as f:
            f.write('\n' + label[np.argmax(img_pred)])
        return label[np.argmax(img_pred)]

def delete():
    path = settings.BASE_DIR + r'/save_data/text.txt'
    if os.path.exists(path) ==True:
        os.remove(path)
