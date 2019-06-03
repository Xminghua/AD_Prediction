#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 11:47
# @Author  : HuaCode
# @File    : views.py
# @Software: PyCharm

# from app import app
# from .admin import admin
# from .user import user
#
from flask import Blueprint, redirect, render_template, request, url_for, session
from app.models import User, Admin, Expert, MRI, DApplication, EAchievement, Resu, Pred, JApply
import pymysql
import json
import traceback


# 连接数据库,此前在数据库中创建数据库adms
db = pymysql.connect("127.0.0.1", "root", "638436", "adms")

def get_mri(username):
    cursor = db.cursor()
    mri = "select * from mri where m_uid='" + username + "'order by m_id desc "
    try:
        # 执行sql语句
        cursor.execute(mri)
        results = cursor.fetchall()
        if results:
            if results[0]:
                if results[0][0]:
                    data = {'flag':1,'MRI_Name':results[0][2]}
                    data = json.dumps(data)
                    print(data)
                    return data
                else:
                    data = {'flag':0, 'MRI_Name':0}
                    data = json.dumps(data)
                    return data
        else:
            data = {'flag': 0, 'MRI_Name': 0}
            data = json.dumps(data)
            return data
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        data = {'flag':2, 'MRI_Name':2}
        data = json.dumps(data)
        return data
    # 关闭数据库连接
    db.close()

# 用户重复注册验证
def verify_user(username):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "select * from user where u_id='" + username + "'"
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        print(len(results))
        if len(results) == 1:
            data = {'flag':1}
            data = json.dumps(data)
            return data
        else:
            data = {'flag':0}
            data = json.dumps(data)
            return data
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()

# 注册验证
def regist(UserID, PWD1, UserName, Sex, Age, Phone):
    cursor = db.cursor()
    sql = "INSERT INTO user(u_id, u_pwd, u_name, u_sex, u_birth, u_phone) VALUES " \
          "('" + UserID + "','" + PWD1 + "','" + UserName + "','" + Sex + "','" + Age + "','" + Phone + "')"
    data = verify_user(UserID)
    data = json.loads(data)
    if data['flag'] == 1:#该用户已经被注册
        data1 = {'flag':0}#用户已经被注册，则返回状态码0
        data1 = json.dumps(data1)
        return data1
    elif data['flag'] == 0:#该用户未被注册
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            data1 = {'flag':1}#该用户未被注册则返回状态码1
            data1 = json.dumps(data1)
            return data1
            # 注册成功之后跳转到登录页面
        except:
            # 抛出错误信息
            traceback.print_exc()
            # 如果发生错误则回滚
            db.rollback()
            data1 = {'flag':2}#出现服务器错误，则返回状态码2
            data1 = json.dumps(data1)
            return data1
        # 关闭数据库连接
    db.close()

# if __name__ == '__main__':
    # data = get_mri();
    # data = json.loads(data)
    # print(data['flag'])
    # print(data['MRI_Name'])


