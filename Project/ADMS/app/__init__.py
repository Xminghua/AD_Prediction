#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 1:18
# @Author  : HuaCode
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import redis


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:638436@127.0.0.1:3306/adms?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 设置session密钥
app.config['SECRET_KEY'] = 'secret_key'
# # 设置连接的redis数据库 默认连接到本地6379
app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_PERMANENT'] = True
# # 设置远程
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

db = SQLAlchemy(app)

from app import models,views
