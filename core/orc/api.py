
#-*- coding:utf-8 -*-
'''
@author: Zilin Hsu
@file: api.py
@time: 2019/10/25 11:05
@desc:
'''
from flask_restful import Resource, reqparse
from core.output import Output
from PIL import Image
from glob import glob
from werkzeug.datastructures import FileStorage


import os
import ocr
import time
import shutil
import numpy as np
import uuid


class OrcApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
       # self.reqparse.add_argument('text', type=str, location='json')
        super(OrcApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        image_url = args['image_url']
        image_file = glob(image_url)
        image = np.array(Image.open(image_file).convert('RGB'))
        t = time.time()
        result, image_framed = ocr.model(image)
        print("Mission complete, it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")

        data = []
        for key in result:
            print(result[key][1])
            data.append(result[key][1])
        # val.val()
        return Output.success(data)

class FileApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('file', type=FileStorage, location='files')

    def post(self):
        args = self.reqparse.parse_args()
        f = args['file']
        uid = str(uuid.uuid4())
        suid = ''.join(uid.split('-'))
        type = f.filename.split('.')[-1]

        url = './upload/' + suid + "." + type
        f.save(os.path.join('./upload', suid + "." + type))
        return Output.success(url)
