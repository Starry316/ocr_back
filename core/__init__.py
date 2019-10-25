#-*- coding:utf-8 -*-
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import *
from core.orc.api import OrcApi,FileApi
import globalval

import uuid

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
#CORS(app, supports_credentials=True)
#db = SQLAlchemy(app)





api = Api(app)
api.add_resource(OrcApi, '/orc', endpoint='rewrite')
api.add_resource(FileApi, '/upload', endpoint='uploadfiles')



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

