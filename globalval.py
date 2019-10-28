#-*- coding:utf-8 -*-

'''
@author: Zilin Hsu
@file: globalval.py
@time: 2019/10/25 11:05
@desc: load global values
'''
import tensorflow as tf
import os
from imp import reload
from keras.layers import Input
from keras.models import Model
# import keras.backend as K

from densenet import keys
from densenet import densenet

global basemodel,graph,nclass


graph = graph = tf.get_default_graph()

reload(densenet)

characters = keys.alphabet[:]
characters = characters[1:] + u'卍'
nclass = len(characters)

input = Input(shape=(32, None, 1), name='the_input')
y_pred= densenet.dense_cnn(input, nclass)
basemodel = Model(inputs=input, outputs=y_pred)

modelPath = os.path.join(os.getcwd(), './densenet/models/weights_densenet.h5')
if os.path.exists(modelPath):
    basemodel.load_weights(modelPath)

