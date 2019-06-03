# -*-coding:utf-8 -*-
from flask import Flask, redirect, request, flash, url_for, render_template, jsonify, session
from flask_login import UserMixin, LoginManager, login_required, login_user
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from app.models import User, Admin, Expert, MRI, DApplication, EAchievement, Resu, Pred, JApply
from app.views import regist, get_mri
from app.ExpertPush import get_expertexcel
from datetime import timedelta
from flask.helpers import url_for
from flask import Response
from Pred.SinglePrediction import Prediction
from Pred.HipvoluSum import get_hipvlousum, get_PredHipvlouSum
import redis
import pymysql
import psutil
import datetime
import urllib
import json
from flask import make_response
import os
import traceback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:638436@127.0.0.1:3306/adms?charset=utf8'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# 设置session密钥
app.config['SECRET_KEY'] = 'secret_key'
# # 设置连接的redis数据库 默认连接到本地6379
app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_PERMANENT'] = True
# # 设置远程
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
# db = SQLAlchemy(app)
# db.init_app(app=app)


'''
登录界面的路由设置，包括页面内的登录，注册，以及忘记密码的页面跳转.
'''
# 默认登录页面
@app.route('/', methods=['GET'])
def login_1():
    msg = ''
    return render_template('login.html', msg=msg)

# 登录验证
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        type = request.form['radioname']
        # db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        # if type == "普通用户":
        #     user = User.query.filter(User.u_id == username, User.u_pwd == password).first()
        #     if user:
        #         user.save()
        #         session['username'] = username
        #         return render_template('user/UserIndex.html', username=username)
        #     else:
        #         msg = '密码或用户名错误，请重新登录！'
        #         return render_template('login.html', msg=msg)
        # elif type == "专家用户":
        #     expert = Expert.query.filter(Expert.e_id == username, Expert.e_pwd == password).first()
        #     if expert:
        #         expert.save()
        #         session['username'] = username
        #         return render_template('expert/ExpertIndex.html', username=username)
        #     else:
        #         msg = '密码或用户名错误，请重新登录！'
        #         return render_template('login.html', msg=msg)
        # elif type == "管理员":
        #     admin = Admin.query.filter(Admin.a_id == username, Admin.a_pwd == password).first()
        #     if admin:
        #         admin.save()
        #         session['username'] = username
        #         return render_template('admin/AdminIndex.html', username=username)
        #     else:
        #         msg = '密码或用户名错误，请重新登录！'
        #         return render_template('login.html', msg=msg)

        print(username)
        print(password)
        print(type)
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        if type == "普通用户":
            cursor = db.cursor()
            sql = "select * from user where u_id='" + username + "' and u_pwd='" + password + "'"
            try:
                # 执行sql语句
                cursor.execute(sql)
                results = cursor.fetchall()
                print(len(results))
                if len(results) == 1:
                    session['username'] = username
                    return render_template('user/UserIndex.html', username=username)
                else:
                    msg = '密码或用户名错误，请重新登录！'
                    return render_template('login.html', msg=msg)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                traceback.print_exc()
                db.rollback()
            # 关闭数据库连接
            db.close()
        elif type == "专家用户":
            cursor = db.cursor()
            sql = "select * from expert where e_id='" + username + "' and e_pwd='" + password + "'"
            try:
                # 执行sql语句
                cursor.execute(sql)
                results = cursor.fetchall()
                print(len(results))
                if len(results) == 1:
                    session['username'] = username
                    return render_template('expert/ExpertIndex.html', username=username)
                else:
                    msg = '密码或用户名错误，请重新登录！'
                    return render_template('login.html', msg=msg)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                traceback.print_exc()
                db.rollback()
            # 关闭数据库连接
            db.close()
        elif type == "管理员":
            cursor = db.cursor()
            sql = "select * from admin where a_id='" + username + "' and a_pwd='" + password + "'"
            try:
                # 执行sql语句
                cursor.execute(sql)
                results = cursor.fetchall()
                print(len(results))
                if len(results) == 1:
                    session['username'] = username
                    return render_template('admin/AdminIndex.html', username=username)
                else:
                    msg = '密码或用户名错误，请重新登录！'
                    return render_template('login.html', msg=msg)
                # 提交到数据库执行
                db.commit()
            except:
                # 如果发生错误则回滚
                traceback.print_exc()
                db.rollback()
            # 关闭数据库连接
            db.close()


"""
普通用户：操作如下
"""
# 普通用户注册验证
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    if request.method == 'POST':
        UserID = request.form['UserID']
        PWD1 = request.form['PWD1']
        UserName = request.form['UserName']
        Sex = request.form['Sex']
        Age = request.form['Birth']
        Phone = request.form['Phone']
        data = regist(UserID, PWD1, UserName, Sex, Age, Phone)
        data = json.loads(data)
        print(data)
        if data['flag'] == 0:#获得状态码0则说明该用户已经被注册
            msg = "该用户已经被注册，请重新注册！"
            return render_template('registration.html', msg=msg)
        elif data['flag'] == 1:#返回状态码1则说明该用户未被注册
            msg = "注册成功，请登录！"
            return render_template('user/regist_success.html', msg=msg)
        elif data['flag'] == 2:#返回状态码2则说明服务器错误
            msg = '服务器错误，请重新注册！'
            return render_template('registration.html', msg=msg)

# UserIndex
@app.route('/UserIndex')
def UserIndex():
    if 'username' in session:
        return render_template('user/UserIndex.html', username=session['username'])
    else:
        return render_template('user/UserIlleagl.html')

# UserInfo
@app.route('/UserInfo')
def UserInfo():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        sql = "select * from user where u_id='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1:
                if results[0][3] == "男":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" checked="checked">'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="">'
                    return render_template('user/UserInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1])
                elif results[0][3] == "女":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" >'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="" checked="checked">'
                    return render_template('user/UserInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1])
            else:
                return render_template('user/UserInfo.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('user/UserInfo.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('user/UserIlleagl.html')

# UserInfoPushMessage普通用户提交信息成功与否返回提示信息
@app.route('/UserInfoPushMessage/?<string:msg>')
def UserInfoPushMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        sql = "select * from user where u_id='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1:
                if results[0][3] == "男":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" checked="checked">'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="">'
                    return render_template('user/UserInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1], msg=msg)
                elif results[0][3] == "女":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" >'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="" checked="checked">'
                    return render_template('user/UserInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1], msg=msg)
            else:
                return render_template('user/UserInfo.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('user/UserInfo.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('user/UserIlleagl.html')

# UserInfoPush普通用户个人信息修改提交页面
@app.route('/UserInfoPush', methods=['GET', 'POST'])
def UserInfoPush():
    if request.method == 'GET':
        return render_template('user/UserInfo.html', username=session['username'])
    if request.method == 'POST':
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        userid = session['username']
        pwd1 = request.form['pwd1']
        pwd2 = request.form['pwd2']
        name = request.form['name']
        sex = request.form['radios']
        birth = request.form['Birth']
        phone = request.form['phone']
        print(pwd1)
        if pwd1 != pwd2:
            msg = '两次密码不一致，请重新提交！'
            return redirect(url_for('UserInfoPushMessage', msg=msg))
        else:
            # 修改多个列的值应该用逗号，来进行连接，而不是and
            user = "UPDATE user set u_pwd='" + pwd1 + "', u_name='" + name + "', u_sex='" + sex + \
                   "', u_birth='" + birth + "', u_phone='" + phone + "'where u_id='" + userid +"'"
            try:
                # 执行sql语句
                cursor.execute(user)
                # 提交到数据库执行
                db.commit()
                msg = '提交修改成功！'
                return redirect(url_for('UserInfoPushMessage', msg=msg))
                # 注册成功之后跳转到登录页面
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = '服务器错误，提交修改失败，请重新提交！'
                return redirect(url_for('UserInfoPushMessage', msg=msg))
            # 关闭数据库连接
            db.close()

# UserContact普通用户联系我们页面
@app.route('/UserContact')
def UserContact():
    if 'username' in session:
        return render_template('user/UserContact.html', username=session['username'])
    else:
        return render_template('user/UserIlleagl.html')

# UserDApply进入用户诊断申请提交页面
@app.route('/UserDApply')
def UserDApply():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        # 将查询到的MRI影像按MRI影像ID递减排列，则获得最新上传的MRI影，再判断该MRI是否为空来进行是否申请诊断
        mri = "select * from mri where m_uid='" + username + "'order by m_id desc "
        dapply = "select * from dapplication where da_uid='" + username + "'"#获得诊断申请列表查询语句
        try:
            # 执行sql语句
            cursor.execute(mri)
            mri_re = cursor.fetchall()
            if mri_re:#首先判断该查询获得结果是否为空
                if mri_re[0]:#如果结果不为空的话，就获得第一条数据
                    if mri_re[0][0]:#如果第一条数据不为空的话，就获得元组中的第一个值
                        # 查询诊断申请列表
                        cursor.execute(dapply)
                        da_re = cursor.fetchall()
                        db.commit()
                        return render_template('user/UserDApply.html', username=session['username'],
                                               MRI_Name=mri_re[0][2], dapply=da_re)
                    else:
                        # 查询诊断申请列表
                        cursor.execute(dapply)
                        da_re = cursor.fetchall()
                        db.commit()
                        return render_template('user/UserDApply.html', username=session['username'],
                                               MRI_Name="未获得MRI影像名称", dapply=da_re)
            else:#如果查询到的结果为空，就直接返回
                return render_template('user/UserDApply.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('user/UserDApply.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('user/UserIlleagl.html')

# UserGetMRI进入用户上传MRI页面
@app.route('/UserGetMRI')
def UserGetMRI():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        mri = "select * from mri where m_uid='" + username + "'"#获得MRI影像列表的sql查询语句
        try:
            # 执行sql语句
            cursor.execute(mri)
            results = cursor.fetchall()
            # 如果查询到的结果不为空的话，就直接返回到前端
            if results:
                return render_template('user/UserGetMRI.html', username=session['username'], mri=results)
            else:
                return render_template('user/UserGetMRI.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            return render_template('user/UserGetMRI.html', username=session['username'])
        # 关闭数据库连接
        db.close()
    else:
        return render_template('user/UserIlleagl.html')

# UserHistoryInfo进入用户历史信息对比页面
@app.route('/UserHistoryInfo')
def UserHistoryInfo():
    if 'username' in session:
        return render_template('user/UserHistoryInfo.html', username=session['username'])
    else:
        return render_template('user/UserIlleagl.html')

# 返回请求头
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# 将获得海马体历史信息返回到前端并绘制折线图、柱状图
@app.route('/Echarts')
def Echarts():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        resu = "select * from resu where r_uid='" + username + "'"#获得MRI影像列表的sql查询语句
        try:
            # 执行sql语句
            cursor.execute(resu)
            rhipvlou_r = cursor.fetchall()
            # 如果查询到的结果不为空的话，就添加到data
            print(rhipvlou_r)
            data = []
            if rhipvlou_r:
                for i in rhipvlou_r:
                    x_data = "海马体" + "-" + i[4].strftime('%Y.%m.%d')
                    y_data = int(i[6])
                    print(x_data)
                    print(y_data)
                    data_dict = {"name": x_data, "num": y_data}
                    data.append(data_dict)
                print(data)
                datas = {"data":data}
                content = json.dumps(datas)
                resp = Response_headers(content)
                return resp
            else:
                datas = {"data":"暂未获得历史数据"}
                content = json.dumps(datas)
                resp = Response_headers(content)
                return resp
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            datas = {"data": "服务器错误"}
            content = json.dumps(datas)
            resp = Response_headers(content)
            return resp
        # 关闭数据库连接
        db.close()

    # datas = {
	# 	"data":[
	# 		{"name":"allpe","num":100},
	# 		{"name":"peach","num":123},
	# 		{"name":"Pear","num":234},
	# 		{"name":"avocado","num":20},
	# 		{"name":"cantaloupe","num":1},
	# 		{"name":"Banana","num":77},
	# 		{"name":"Grape","num":43},
	# 		{"name":"apricot","num":0}
	# 	]
	# }
    # content = json.dumps(datas)
    # resp = Response_headers(content)
    # return resp

# UserIlleagl进入非法用户页面
@app.route('/UserIlleagl')
def UserIlleagl():
    return render_template('user/UserIlleagl.html')

# UserLogout进入普通用户登出页面
@app.route('/UserLogout')
def UserLogout():
    session.pop('username', None)
    session.clear()
    return render_template('user/UserLogout.html')

# UserResu进入用户诊断结果页面
@app.route('/UserResu')
def UserResu():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        resu = "select * from resu where r_uid='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(resu)
            results = cursor.fetchall()
            if results:
                print(results)
                msg = "(诊断结果信息如下：)"
                return render_template('user/UserResu.html', username=session['username'], resu=results, msg1=msg)
            else:
                msg = "(未获取到诊断结果信息)"
                return render_template('user/UserResu.html', username=session['username'], msg1=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg1 = "(服务器错误！)"
            return render_template('user/UserResu.html', username=session['username'], msg1=msg1)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('user/UserIlleagl.html')

# UserSetting进入用户设置页面
@app.route('/UserSetting')
def UserSetting():
    if 'username' in session:
        return render_template('user/UserSetting.html', username=session['username'])
    else:
        return render_template('user/UserIlleagl.html')



"""
管理员：管理员页面及操作如下
"""
# AdminIndex管理员登录首页
@app.route('/AdminIndex')
def AdminIndex():
    if 'username' in session:
        return render_template('admin/AdminIndex.html', username=session['username'])
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminDApply进入管理员诊断申请批准页面
@app.route('/AdminDApply')
def AdminDApply():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        dapply = "select * from dapplication"  # 获得诊断申请列表查询语句 where da_uid='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(dapply)
            da_re = cursor.fetchall()
            print(da_re)
            status_apply = ()
            if da_re:
                for i in da_re:
                    if i[4] == "申请中":
                        # 这一步是将后续要进行预测的URL提前传递过去
                        action = "/" +i[2] + "/1"#这一步是获得该用户的用户ID和对应的MRI影像名称
                        i = i + (action, 'btn-success', 'submit', '批准')
                    elif i[4] == "申请完毕，请预测":
                        action1 = "/" + i[1] + "/" + i[2]#这里是将预测路径传入
                        pred = '<form method="post" action='+ action1 +'>' \
                               '<!--批准：btn btn-success；完成批准：btn btn-inverse-->' \
                               '<input id="allow1" name="allow1" class="btn-success" type="submit" value="开始预测">' \
                               '</form>'
                        i = i + ("#", 'btn-inverse', 'button', '已批准', pred)
                    elif i[4] == "预测完毕":
                        i = i + ("#", 'btn-inverse', 'button', '已预测')
                    elif i[4] == "已诊断，请反馈结果":
                        i = i + ("#", 'btn-inverse', 'button', '已预测')
                    elif i[4] == "诊断完毕":
                        i = i + ("#", 'btn-inverse', 'button', '已诊断')
                    status_apply += ((i),)
                print(status_apply)
                return render_template('admin/AdminDApply.html', username=session['username'], dapply=status_apply)
            else:
                return render_template('admin/AdminDApply.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('admin/AdminDApply.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminJApply进入管理员入职申请批准页面
@app.route('/AdminJApply')
def AdminJApply():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        japply = "select * from japply"  # 获得诊断申请列表查询语句 where da_uid='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(japply)
            ja_re = cursor.fetchall()
            print(ja_re)
            status_apply = ()
            if ja_re:
                for i in ja_re:
                    print(i)
                    if i[6] == "申请中":
                        # 这一步是将后续要进行预测的URL提前传递过去
                        action = "/" + i[1] + "/3"   # 这一步是获得该用户的用户ID和对应的MRI影像名称
                        action_1 = "/" + i[1] + "/4" #这一步是获得查看专家个人履历的URL
                        i = i + (action, 'btn-success', 'submit', '批准', action_1, 'btn-success', 'submit', '查看')
                    elif i[6] == "申请完毕":
                        action_1 = "/" + i[1] + "/4"  # 这一步是获得查看专家个人履历的URL
                        i = i + ("/JApplyAllow", 'btn-inverse', 'button', '已批准', action_1, 'btn-success', 'submit', '查看')
                    status_apply += ((i),)
                print(status_apply)
                return render_template('admin/AdminJApply.html', username=session['username'], japply=status_apply)
            else:
                return render_template('admin/AdminJApply.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('admin/AdminJApply.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminUserManage管理员用户管理页面
@app.route('/AdminUserManage')
def AdminUserManage():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        user = "select * from user"
        try:
            # 执行sql语句
            cursor.execute(user)
            results = cursor.fetchall()
            if results:
                db.commit()
                return render_template('admin/AdminUserManage.html', username=username, user=results)
            else:
                db.commit()
                return render_template('admin/AdminUserManage.html', username=username)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('admin/AdminUserManage.html', username=username, msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminExpertManage管理员专家管理页面
@app.route('/AdminExpertManage')
def AdminExpertManage():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        user = "select * from expert"
        try:
            # 执行sql语句
            cursor.execute(user)
            results = cursor.fetchall()
            if results:
                db.commit()
                return render_template('admin/AdminExpertManage.html', username=username, user=results)
            else:
                db.commit()
                return render_template('admin/AdminExpertManage.html', username=username)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('admin/AdminExpertManage.html', username=username, msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminExpertPush管理员专家用户导入
@app.route('/AdminExpertPush')
def AdminExpertPush():
    if 'username' in session:
        return render_template('admin/AdminExpertPush.html', username=session['username'])
    else:
        return render_template('admin/AdminIlleagl.html')

# ExpertPush管理员导入专家用户
@app.route('/ExpertPush', methods=['POST'])
def ExpertPush():
    db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
    cursor = db.cursor()
    xlsx = request.files.to_dict().get('file_data')
    filename = xlsx.filename
    data = get_expertexcel(filename)
    print(data)
    msg = ''
    if request.method == 'POST':
        try:
            for i in data:
                e_id = i[0]
                e_pwd = i[1]
                e_name = i[2]
                e_sex = i[3]
                e_birth = i[4]
                e_phone = i[5]
                e_phone = json.dumps(e_phone)
                expert_insert = "INSERT INTO expert(e_id, e_pwd, e_name, e_sex, e_birth, e_phone) VALUES " \
                       "('" + e_id + "','" + e_pwd + "','" + e_name + "','" + e_sex + "','" + e_birth + "','" + e_phone + "')"
                try:
                    # 执行sql语句
                    cursor.execute(expert_insert)
                    # 提交到数据库执行
                    db.commit()
                    # print("成功导入专家信息！")
                    msg = "成功导入专家信息!"
                except:
                    # 如果发生错误则回滚
                    traceback.print_exc()
                    db.rollback()
                    # print("服务器错误")
                    msg = "服务器错误!"
            data = {'msg':msg}
            print(data['msg'])
            data = json.dumps(data)
            return data
        except Exception as e:
            raise e
    # 关闭数据库连接
    db.close()
    return "false"

# AdminInfo管理员个人信息页面
@app.route('/AdminInfo')
def AdminInfo():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        sql = "select * from admin where a_id='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1:
                if results[0][3] == "男":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" checked="checked">'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="">'
                    return render_template('admin/AdminInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1])
                elif results[0][3] == "女":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" >'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="" checked="checked">'
                    return render_template('admin/AdminInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1])
            else:
                return render_template('admin/AdminInfo.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('admin/AdminInfo.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminInfoPushMessage管理员提交信息成功与否返回提示信息
@app.route('/AdminInfoPushMessage/?<string:msg>')
def AdminInfoPushMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        sql = "select * from admin where a_id='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1:
                if results[0][3] == "男":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" checked="checked">'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="">'
                    return render_template('admin/AdminInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1], msg=msg)
                elif results[0][3] == "女":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" >'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="" checked="checked">'
                    return render_template('admin/AdminInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1], msg=msg)
            else:
                return render_template('admin/AdminInfo.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('admin/AdminInfo.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminInfoPush管理员提交个人修改信息
@app.route('/AdminInfoPush', methods=['GET', 'POST'])
def AdminInfoPush():
    if request.method == 'GET':
        return render_template('admin/AdminInfo.html', username=session['username'])
    if request.method == 'POST':
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        userid = session['username']
        pwd1 = request.form['pwd1']
        pwd2 = request.form['pwd2']
        name = request.form['name']
        sex = request.form['radios']
        birth = request.form['Birth']
        phone = request.form['phone']
        if pwd1 != pwd2:
            msg = '两次密码不一致，请重新填写！'
            return redirect(url_for('AdminInfoPushMessage', msg=msg))
        else:
            # 修改多个列的值应该用逗号，来进行连接，而不是and
            admin = "UPDATE admin set a_pwd='" + pwd1 + "', a_name='" + name + "', a_sex='" + sex + \
                   "', a_birth='" + birth + "', a_phone='" + phone + "'where a_id='" + userid +"'"
            try:
                # 执行sql语句
                cursor.execute(admin)
                # 提交到数据库执行
                db.commit()
                msg = '提交修改成功！'
                return redirect(url_for('AdminInfoPushMessage', msg=msg))
                # 注册成功之后跳转到登录页面
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = '服务器错误，提交修改失败，请重新提交！'
                return redirect(url_for('AdminInfoPushMessage', msg=msg))
            # 关闭数据库连接
            db.close()

# AdminContact管理员联系我们页面
@app.route('/AdminContact')
def AdminContact():
    if 'username' in session:
        return render_template('admin/AdminContact.html', username=session['username'])
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminSetting管理员设置页面
@app.route('/AdminSetting')
def AdminSetting():
    if 'username' in session:
        return render_template('admin/AdminSetting.html', username=session['username'])
    else:
        return render_template('admin/AdminIlleagl.html')

# AdminIlleagl管理员非法用户页面
@app.route('/AdminIlleagl')
def AdminIlleagl():
    return render_template('admin/AdminIlleagl.html')

# AdminLogout管理员登出页面
@app.route('/AdminLogout')
def AdminLogout():
    session.pop('username', None)
    session.clear()
    return render_template('admin/AdminLogout.html')

# AdminExpertResume管理员查看专家用户个人履历页面
@app.route('/AdminExpertResume')
def AdminExpertResume():
    if 'username' in session:
        return render_template('admin/AdminExpertResume.html', username=session['username'])
    else:
        return render_template('admin/AdminIlleagl.html')


"""
专家用户：操作如下
"""
# ExpertIndex专家用户登录首页
@app.route('/ExpertIndex')
def ExpertIndex():
    if 'username' in session:
        return render_template('expert/ExpertIndex.html', username=session['username'])
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertDApply专家用户诊断批准页面
@app.route('/ExpertDApply')
def ExpertDApply():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        dapply = "select * from dapplication"#获得诊断申请列表查询语句
        try:
            cursor.execute(dapply)
            da_re = cursor.fetchall()
            print(da_re)
            status_diagnose = ()
            if da_re:
                for i in da_re:
                    if i[4] == "申请中":
                        i = i + ("#", 'btn-danger', 'button', '未批准')
                    elif i[4] == "申请完毕，请预测":
                        i = i + ("#", 'btn-danger', 'button', '未预测')
                    elif i[4] == "预测完毕":
                        action = "/" + i[2] + "/2"#action传递的是含有MRI影像的URL，共后续调用
                        i = i + (action, 'btn-success', 'submit', '诊断')
                    elif i[4] == "已诊断，请反馈结果":
                        # action1 = "/" + i[2] + "/22"
                        # a = "<a href="../../static/requiredimages/admin/Pred/ADNI_002_S_0295_MR_HarP_135_final_release_2015_Br_20150226095012465_S13408_I474728.nii" download="ADNI_002_S_0295_MR_HarP_135_final_release_2015_Br_20150226095012465_S13408_I474728.nii">点击下载</a>"
                        url = "../../static/requiredimages/admin/Pred/" + i[2] + ""
                        file = i[2]
                        pred = '<button class="btn-success" > <a href=' + url +'  download=' + file + '>' \
                                                                                '下载预测文件</a></button>'
                        i = i + ("#", 'btn-inverse', 'button', '诊断中', pred)
                    elif i[4] == "诊断完毕":
                        i = i + ("#", 'btn-inverse', 'button', '已诊断')
                    status_diagnose += ((i),)
                print(status_diagnose)
                return render_template('expert/ExpertDApply.html', username=username, dapply=status_diagnose)
            else:
                return render_template('expert/ExpertDApply.html', username=username)
            #提交到数据库执行
            db.commit()
        except:
        # 如果繁盛错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误"
            return render_template('expert/ExpertDApply.html', username=username, msg=msg)
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertGetMRI专家用户上传诊断结果页面
@app.route('/ExpertGetMRI')
def ExpertGetMRI():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        resu = "select * from resu where r_eid='" + username + "'"
        results_r = ()
        try:
            # 执行sql语句
            cursor.execute(resu)
            results = cursor.fetchall()
            if results:
                for i in results:
                    r_diag = i[7][:15] + '***'# 截取指定部分的个人履历进行显示
                    i = i + (r_diag,)
                    results_r += ((i),)
                print(results)
                msg = "(诊断结果信息如下：)"
                return render_template('expert/ExpertGetMRI.html', username=session['username'], resu=results_r, msg1=msg)
            else:
                msg = "(未获取到诊断结果信息)"
                return render_template('expert/ExpertGetMRI.html', username=session['username'], msg1=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg1 = "(服务器错误！)"
            return render_template('expert/ExpertGetMRI.html', username=session['username'], msg1=msg1)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertJApply专家用户入职申请页面
@app.route('/ExpertJApply')
def ExpertJApply():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        japply = "select * from japply where j_eid='" + username + "'"  # 获得入职申请列表
        japply_r1 = ()
        try:
            # 执行sql语句
            cursor.execute(japply)
            japply_r = cursor.fetchall()
            if japply_r:
                db.commit()
                resume = japply_r[0][5][:30] + '***'  # 截取指定部分的个人履历进行显示
                for i in japply_r:
                    i = i + (resume,)
                    japply_r1 += ((i),)
                print(japply_r1)
                return render_template('expert/ExpertJApply.html', username=session['username'],japply=japply_r1)
            else:  # 如果查询到的结果为空，就直接返回
                db.commit()
                msg = "(暂无入职申请)"
                return render_template('expert/ExpertJApply.html', username=session['username'], msg_ja=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('expert/ExpertJApply.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

#ExpertJApplyPush专家用户入职申请提交
@app.route('/ExpertJApplyPush', methods=['GET','POST'])
def ExpertJApplyPush():
    if request.method == 'GET':
        return render_template('expert/ExpertJApply.html')
    if request.method == 'POST':
        j_eid = session['username']
        j_atime = request.form['japply_time']
        j_aidentity = request.form['japply_identity']
        j_asalary = request.form['japply_salary']
        j_resume = request.form['resume']
        j_astatus = "申请中"
        if len(j_resume) < 10:#这里规定为100字，目前测试为10个字
            msg = "个人履历字数未达到要求，请重新申请！"
            return redirect(url_for('JApplyPushMessage', msg=msg))
        else:
        # print(j_resume)
        # return j_resume
            db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
            cursor = db.cursor()
            japply = "select * from japply where j_eid='" + j_eid + "'"  # 获得入职申请列表
            cursor.execute(japply)
            japply_r = cursor.fetchall()
            print(japply_r)
            if japply_r:
                if japply_r[0][1] == j_eid:
                    db.commit()
                    msg = "你已提交入职申请，请勿重新提交！"
                    return redirect(url_for('JApplyPushMessage', msg=msg))
                else:
                    ja_insert = "INSERT INTO japply(j_eid, j_atime, j_aidentity, j_asalary, j_resume, j_astatus) VALUES " \
                          "('" + j_eid + "','" + j_atime + "','" + j_aidentity + "','" + j_asalary + "','" + j_resume + "','" \
                                + j_astatus + "')"
                    try:
                        # 执行sql语句
                        cursor.execute(ja_insert)
                        db.commit()
                        msg = "申请成功！"
                        return redirect(url_for('JApplyPushMessage', msg=msg))
                    except:
                        # 如果发生错误则回滚
                        traceback.print_exc()
                        db.rollback()
                        msg = '服务器错误！'
                        return redirect(url_for('JApplyPushMessage', msg=msg))
                        # 关闭数据库连接
                    db.close()
            else:
                ja_insert = "INSERT INTO japply(j_eid, j_atime, j_aidentity, j_asalary, j_resume, j_astatus) VALUES " \
                            "('" + j_eid + "','" + j_atime + "','" + j_aidentity + "','" + j_asalary + "','" + j_resume + "','" \
                            + j_astatus + "')"
                try:
                    # 执行sql语句
                    cursor.execute(ja_insert)
                    db.commit()
                    msg = "申请成功！"
                    return redirect(url_for('JApplyPushMessage', msg=msg))
                except:
                    # 如果发生错误则回滚
                    traceback.print_exc()
                    db.rollback()
                    msg = '服务器错误！'
                    return redirect(url_for('JApplyPushMessage', msg=msg))
                    # 关闭数据库连接
                db.close()

# JApplyPushMessage专家用户入职申请提交状态反馈
@app.route('/JApplyPushMessage/?<string:msg>')
def JApplyPushMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        japply = "select * from japply where j_eid='" + username + "'"  # 获得入职申请列表
        japply_r1 = ()
        try:
            # 执行sql语句
            cursor.execute(japply)
            japply_r = cursor.fetchall()
            if japply_r:
                db.commit()
                resume = japply_r[0][5][:30] + '***'  # 截取指定部分的个人履历进行显示
                for i in japply_r:
                    i = i + (resume,)
                    japply_r1 += ((i),)
                print(japply_r1)
                return render_template('expert/ExpertJApply.html', username=session['username'],japply=japply_r1, msg=msg)
            else:  # 如果查询到的结果为空，就直接返回
                db.commit()
                return render_template('expert/ExpertJApply.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('expert/ExpertJApply.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertInfo专家用户个人信息页面
@app.route('/ExpertInfo')
def ExpertInfo():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        sql = "select * from expert where e_id='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1:
                if results[0][3] == "男":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" checked="checked">'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="">'
                    return render_template('expert/ExpertInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1])
                elif results[0][3] == "女":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" >'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="" checked="checked">'
                    return render_template('expert/ExpertInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1])
            else:
                return render_template('expert/ExpertInfo.html', username=session['username'])
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('expert/ExpertInfo.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertInfoPushMessage专家用户提交个人信息成功与否返回提示信息
@app.route('/ExpertInfoPushMessage/?<string:msg>')
def ExpertInfoPushMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        sql = "select * from expert where e_id='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1:
                if results[0][3] == "男":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" checked="checked">'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="">'
                    return render_template('expert/ExpertInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1], msg=msg)
                elif results[0][3] == "女":
                    nan = '<input type="radio" value="男" name="radios" id="radio1" required="" >'
                    nv = '<input type="radio" value="女" name="radios" id="radio2" required="" checked="checked">'
                    return render_template('expert/ExpertInfo.html', username=session['username'],
                                           name=results[0][2], phone=results[0][5], nan=nan, nv=nv, birth=results[0][4],
                                           pwd1=results[0][1], pwd2=results[0][1], msg=msg)
            else:
                return render_template('expert/ExpertInfo.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('expert/ExpertInfo.html', username=session['username'], msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertInfoPush专家用户个人信息修改提交
@app.route('/ExpertInfoPush', methods=['GET', 'POST'])
def ExpertInfoPush():
    if request.method == 'GET':
        return render_template('expert/ExpertInfo.html', username=session['username'])
    if request.method == 'POST':
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        userid = session['username']
        pwd1 = request.form['pwd1']
        pwd2 = request.form['pwd2']
        name = request.form['name']
        sex = request.form['radios']
        birth = request.form['Birth']
        phone = request.form['phone']
        if pwd1 != pwd2:
            msg = '两次密码不一致，请重新填写！'
            return redirect(url_for('ExpertInfoPushMessage', msg=msg))
        else:
            # 修改多个列的值应该用逗号，来进行连接，而不是and
            admin = "UPDATE expert set e_pwd='" + pwd1 + "', e_name='" + name + "', e_sex='" + sex + \
                   "', e_birth='" + birth + "', e_phone='" + phone + "'where e_id='" + userid +"'"
            try:
                # 执行sql语句
                cursor.execute(admin)
                # 提交到数据库执行
                db.commit()
                msg = '提交修改成功！'
                return redirect(url_for('ExpertInfoPushMessage', msg=msg))
                # 注册成功之后跳转到登录页面
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = '服务器错误，提交修改失败，请重新提交！'
                return redirect(url_for('ExpertInfoPushMessage', msg=msg))
            # 关闭数据库连接
            db.close()

# ExpertAchievement专家用户个人成就页面
@app.route('/ExpertAchievement')
def ExpertAchievement():
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        japply = "select * from japply where j_eid='" + username + "'"
        achievement = "select * from eachievement where ea_eid='" + username + "'"
        ranks = "select ea_eid, ea_score, (select count(distinct ea_score) from eachievement where ea_score >= s.ea_score) " \
               "as Rank from eachievement as s order by ea_score desc"
        try:
            cursor.execute(japply)
            japply_r = cursor.fetchall()
            if japply_r:
                # db.commit()
                if japply_r[0][6] == "申请完毕":
                    # 执行sql语句
                    cursor.execute(achievement)
                    results = cursor.fetchall()
                    print(results)
                    if results:
                        rank = ""
                        db.commit()
                        cursor.execute(ranks)
                        rank_r = cursor.fetchall()
                        if rank_r:
                            # db.commit()
                            for i in rank_r:
                                if i[0] == username:
                                    rank = i[2]
                            return render_template('expert/ExpertAchievement.html', username=username, achievement=results,
                                                   rank=rank)
                        else:
                            # db.commit()
                            rank = "暂无"
                            return render_template('expert/ExpertAchievement.html', username=username, achievement=results,
                                                   rank=rank)
                        db.commit()
                    else:
                        # db.commit()
                        return render_template('expert/ExpertAchievement.html', username=username)
                    # 提交到数据库执行
                    db.commit()
                else:
                    return render_template('expert/ExpertAchievement.html', username=username)
            else:
                return render_template('expert/ExpertAchievement.html', username=username)
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg = "服务器错误！"
            return render_template('expert/ExpertAchievement.html', username=username, msg=msg)
        # 关闭数据库连接
        db.close()
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertContact专家用户联系我们页面
@app.route('/ExpertContact')
def ExpertContact():
    if 'username' in session:
        return render_template('expert/ExpertContact.html', username=session['username'])
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertSetting专家用户设置页面
@app.route('/ExpertSetting')
def ExpertSetting():
    if 'username' in session:
        return render_template('expert/ExpertSetting.html', username=session['username'])
    else:
        return render_template('expert/ExpertIlleagl.html')

# ExpertIlleagl非法专家用户页面
@app.route('/ExpertIlleagl')
def ExpertIlleagl():
    return render_template('expert/ExpertIlleagl.html')

# ExpertLogout专家用户登出页面
@app.route('/ExpertLogout')
def ExpertLogout():
    session.pop('username', None)
    session.clear()
    return render_template('expert/ExpertLogout.html')


"""
MRI影像操作
"""
# 写入MRI影像文件
def storageimage(filename, content):
    with open(filename, "wb+") as f:
        f.write(content)

"""""
普通用户上传原始MRI
"""""
# 普通用户上传MRI影像到user/upload文件夹下面
@app.route('/UserUpload', methods=["POST"])
def UserUpload():
    img = request.files.to_dict().get('file_data')
    filename = img.filename
    print(filename)
    content = img.read()
    print(content)
    if request.method == 'POST':
        try:
            username = session['username']
            dir = 'static/requiredimages/user/' + username
            if os.path.exists(dir + '/upload/'):
                storageimage(dir + '/upload/' + filename, content)
                data = {'filename':filename}
                data = json.dumps(data)
                return data
            else:
                os.mkdir(dir)
                os.mkdir(dir + '/upload')
                storageimage(dir + '/upload/' + filename, content)
                data = {'filename': filename}
                data = json.dumps(data)
                return data
        except Exception as e:
            raise e
    return "false"

#普通用户上传MRI信息到数据库中保存
@app.route('/UserUploadMRI', methods=["POST"])
def UserUploadMRI():
    if request.method == 'POST':
        m_uid = session['username']
        m_name = request.form['MRI_Name']
        m_utime = request.form['upload_time']
        m_getime = request.form['Shoot_time']
        if m_name == "" or m_utime == "" or m_getime == "":
            msg = "数据未填写完整或"
            return redirect(url_for('UserUploadMRIMessage', msg=msg))
        else:
            db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
            cursor = db.cursor()
            mri_mname = "select * from mri where m_name='" + m_name + "'"
            mri = "INSERT INTO mri(m_uid, m_name, m_utime, m_getime) VALUES " \
                  "('" + m_uid + "','" + m_name + "','" + m_utime + "','" + m_getime + "')"
            try:
                # 执行sql语句
                cursor.execute(mri_mname)
                results = cursor.fetchall()
                print(results)
                if results:
                    msg = '该MRI影像已存在，请勿重复上传！'
                    return redirect(url_for('UserUploadMRIMessage', msg=msg))
                else:
                    cursor.execute(mri)
                    # 提交到数据库执行
                    db.commit()
                    msg = '上传成功!'
                    return redirect(url_for('UserUploadMRIMessage', msg=msg))
                db.commit()
            except:
                # 如果发生错误则回滚
                traceback.print_exc()
                db.rollback()
                msg = '服务器错误！'
                return redirect(url_for('UserUploadMRIMessage', msg=msg))
            # 关闭数据库连接
            db.close()
    else:
        return redirect('/UserIlleagl')

# UserUploadMRIMessage普通用户上传MRI影像信息到数据库成功与否返回提示信息
@app.route('/UserUploadMRIMessage/?<string:msg>')
def UserUploadMRIMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        mri = "select * from mri where m_uid='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(mri)
            results = cursor.fetchall()
            if results:
                print(results)
                return render_template('user/UserGetMRI.html', username=session['username'], mri=results, msg=msg)
            else:
                return render_template('user/UserGetMRI.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg1 = "服务器错误！"
            return render_template('user/UserGetMRI.html', username=session['username'], msg=msg1)
        # 关闭数据库连接
        db.close()
    else:
        return redirect('/UserIlleagl')

"""""
专家用户上传MRI诊断结果
"""""
# 专家用户上传MRI影像诊断结果到expert/upload文件夹下面
@app.route('/ExpertUpload', methods=["POST"])
def ExpertUpload():
    img = request.files.to_dict().get('file_data')
    filename = img.filename
    print(filename)
    content = img.read()
    print(content)
    if request.method == 'POST':
        try:
            username = session['username']
            dir = 'static/requiredimages/expert/' + username
            if os.path.exists(dir + '/upload/'):
                storageimage(dir + '/upload/' + filename, content)
                data = {'filename':filename}
                data = json.dumps(data)
                return data
            else:
                os.mkdir(dir)
                os.mkdir(dir + '/upload')
                storageimage(dir + '/upload/' + filename, content)
                data = {'filename': filename}
                data = json.dumps(data)
                return data
        except Exception as e:
            raise e
    return "false"

#专家上传MRI影像诊断结果信息到数据库中保存
@app.route('/ExpertUploadMRI', methods=["POST"])
def ExpertUploadMRI():
    if request.method == 'POST':
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        r_eid = session['username']
        r_mname = request.form['MRI_Name']
        r_rtime = request.form['feedback_time']
        r_diag = request.form['Diagnosis']
        if r_mname == "" or r_diag == "":
            msg = "数据未填写完整"
            return redirect(url_for('ExpertUploadMRIMessage', msg=msg))
        else:
            mri = "select * from mri where m_name='" + r_mname + "'"#从MRI影像表中查询该MRI影像的信息，并获取其中的用户ID和上传时间信息
            rmname = "select * from resu where r_mname='" + r_mname + "'"#从诊断结果表中查询该MRI影像是否已经存在
            cursor.execute(rmname)
            rmname_r = cursor.fetchall()
            if rmname_r:
                db.commit()
                msg = "该MRI影像诊断结果已经上传，请勿重新上传！"
                return redirect(url_for('ExpertUploadMRIMessage', msg=msg))
            else:
                try:
                    # 执行sql语句
                    cursor.execute(mri)
                    mri_r = cursor.fetchall()
                    if mri_r:
                        print(mri_r)
                        r_uid = mri_r[0][1]
                        r_utime = mri_r[0][3]
                        r_utime = r_utime.strftime('%Y-%m-%d %H:%M:%S')#将时间格式转换为str格式
                        print(r_rtime)
                        print(str(r_utime))

                        r_hipvolu = get_hipvlousum(username=r_eid,MRI_Name=r_mname)#这里是通过MRI影像名称来获得该MRI影像，并计算出其海马体大小。5000为一个临时值
                        r_hipvolu = str(r_hipvolu)
                        status = "诊断完毕"
                        resu_allow = "UPDATE dapplication set da_status='" + status + "'where da_mname='" + r_mname + "'"
                        try:
                            # 执行sql语句
                            cursor.execute(resu_allow)
                            # 提交到数据库执行
                            db.commit()
                            print("诊断完成，修改诊断状态为：诊断完毕")
                        except:
                            # 抛出错误信息
                            traceback.print_exc()
                            # 如果发生错误则回滚
                            db.rollback()
                            print("服务器错误，修改诊断状态失败！请重新失败")
                        # 关闭数据库连接
                        # db.close()

                        """
                        这里是上传MRI影像诊断结果的数据库操作，同时还需要改变诊断申请表中的诊断状态为诊断完毕
                        """
                        resu = "INSERT INTO resu(r_uid, r_eid, r_mname, r_rtime, r_utime, r_hipvolu, r_diag) VALUES " \
                              "('" + r_uid + "','" + r_eid + "','" + r_mname + "','" + r_rtime + "','"+ r_utime +"','" \
                               + r_hipvolu + "','" + r_diag + "')"
                        cursor.execute(resu)
                        da_status = "诊断完毕"
                        dapply = ""
                        # 提交到数据库执行
                        db.commit()
                        msg = "上传成功！"
                        return redirect(url_for('ExpertUploadMRIMessage', msg=msg))
                    else:
                        msg = "数据库中未找到该用户信息或该用户未发起该MRI影像诊断申请，请选择正确的诊断结果进行上传！"
                        return redirect(url_for('ExpertUploadMRIMessage', msg=msg))
                    db.commit()
                except:
                    # 如果发生错误则回滚
                    traceback.print_exc()
                    db.rollback()
                    msg = '服务器错误！'
                    return redirect(url_for('ExpertUploadMRIMessage', msg=msg))
                # 关闭数据库连接
        db.close()

# ExpertUploadMRIMessage专家用户上传MRI影像诊断结果信息到数据库成功与否返回提示信息
@app.route('/ExpertUploadMRIMessage/?<string:msg>')
def ExpertUploadMRIMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        resu = "select * from resu where r_eid='" + username + "'"
        results_r = ()
        try:
            # 执行sql语句
            cursor.execute(resu)
            results = cursor.fetchall()
            if results:
                r_diag = results[0][7][:15] + '***'  # 截取指定部分的个人履历进行显示
                for i in results:
                    i = i + (r_diag,)
                    results_r += ((i),)
                print(results)
                return render_template('expert/ExpertGetMRI.html', username=session['username'], resu=results_r, msg=msg)
            else:
                return render_template('expert/ExpertGetMRI.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg1 = "服务器错误！"
            return render_template('expert/ExpertGetMRI.html', username=session['username'], msg=msg1)
        # 关闭数据库连接
        db.close()
    else:
        return redirect(url_for('ExpertIlleagl'))

"""""
普通用户诊断申请
"""""
# DApply普通用户诊断申请提交
@app.route('/DApply', methods=['POST', 'GET'])
def DApply():
    if request.method == 'GET':
        return render_template('user/UserDApply.html')
    if request.method == 'POST':
        da_uid = session['username']
        da_mname = request.form['MRI_Name']
        da_atime = request.form['upload_time']
        da_status = "申请中"
        if da_mname == 'placeholder="MRI影像名称"':
            msg = '未上传MRI影像，请先上传后再申请！'
            print(msg)
            return redirect(url_for('DApplyMessage', msg=msg))
        else:
            db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
            cursor = db.cursor()
            da_verify = "select * from dapplication where da_uid='" + da_uid + "'"
            da_insert = "INSERT INTO dapplication(da_uid, da_mname, da_atime, da_status) VALUES " \
                  "('" + da_uid + "','" + da_mname + "','" + da_atime + "','" + da_status + "')"
            try:
                # 执行sql语句
                cursor.execute(da_verify)
                da_check = cursor.fetchall()
                # 若在诊断申请表中找到该用户的记录，判断是否有未完成的诊断申请，或该MRI影像是否已经诊断，都没有则可以进行申请
                if da_check:
                    for i in da_check:
                        if i[2] == da_mname:
                            print("该MRI影像诊断申请已经提交或诊断已经完成，请勿重复诊断！")
                            msg = '该MRI影像诊断申请已经提交或诊断已经完成，请勿重复诊断！'
                            return redirect(url_for('DApplyMessage', msg=msg))
                    for i in da_check:
                        if i[4] != "诊断完毕":
                            print("你有未完成的诊断申请，请勿重复提交！")
                            msg = '你有未完成的诊断申请，请勿重复提交！'
                            return redirect(url_for('DApplyMessage', msg=msg))
                    cursor.execute(da_insert)
                    # 提交到数据库执行
                    db.commit()
                    print("诊断申请成功！")
                    msg = '诊断申请提交成功！'
                    return redirect(url_for('DApplyMessage', msg=msg))
                else:
                    cursor.execute(da_insert)
                    # 提交到数据库执行
                    db.commit()
                    print("同样可以申请")
                    msg = '诊断申请提交成功！'
                    return redirect(url_for('DApplyMessage', msg=msg))
                db.commit()
            except:
                # 如果发生错误则回滚
                traceback.print_exc()
                db.rollback()
                msg = '服务器错误！'
                return redirect(url_for('DApplyMessage', msg=msg))
                # 关闭数据库连接
            db.close()
    else:
        return redirect('/UserIlleagl')

# DApplyMessage普通用户诊断申请提交反馈信息
@app.route('/DApplyMessage/?<string:msg>')
def DApplyMessage(msg):
    if 'username' in session:
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        mri = "select * from mri where m_uid='" + username + "'order by m_id desc "
        dapply = "select * from dapplication where da_uid='" + username + "'"
        try:
            # 执行sql语句
            cursor.execute(mri)
            mri_re = cursor.fetchall()
            if mri_re:
                if mri_re[0]:
                    if mri_re[0][0]:
                        cursor.execute(dapply)
                        da_re = cursor.fetchall()
                        db.commit()
                        return render_template('user/UserDApply.html', username=session['username'],
                                               MRI_Name=mri_re[0][2], dapply=da_re, msg=msg)
                    else:
                        cursor.execute(dapply)
                        da_re = cursor.fetchall()
                        db.commit()
                        return render_template('user/UserDApply.html', username=session['username'],
                                               MRI_Name="未获得MRI影像名称", dapply=da_re, msg=msg)
            else:
                return render_template('user/UserDApply.html', username=session['username'], msg=msg)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            msg1 = "服务器错误！"
            return render_template('user/UserDApply.html', username=session['username'], msg=msg1)
        # 关闭数据库连接
        db.close()

"""""
管理员和专家对MRI影像进行诊断操作
number参数的值为1,2,3,4
# number=1：表示管理员批准诊断申请；
# number=2：表示专家开始诊断；
# number=3：表示管理员批准入职申请，此时MRI_Name表示专家ID
# number=4：表示管理员查看专家履历，此时MRI_Name表示专家ID

# 后续的诊断加载以及预测模型都是在这个函数中完成
"""""
@app.route('/<string:MRI_Name>/<int:number>', methods=['GET', 'POST'])
def DApplyAllow(MRI_Name, number):
    if request.method == 'GET':
        return render_template('admin/AdminDApply.html')
    if request.method == 'POST':
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = session['username']
        if number == 1:
            # 这里加载预测模型并预测得到预测图片保存在results文件夹中
            status = "申请完毕，请预测"
            daig_allow = "UPDATE dapplication set da_status='" + status + "'where da_mname='" + MRI_Name + "'"
            try:
                # 执行sql语句
                cursor.execute(daig_allow)
                # 提交到数据库执行
                db.commit()
                msg = '成功批准！'
                return redirect('AdminDApply')
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = '批准失败！'
                return redirect('AdminDApply')
            # 关闭数据库连接
            db.close()
        elif number == 2:
            # 这里的操作时专家将从results文件夹中获取对应的MRI影像的标签来进行诊断
            status = "已诊断，请反馈结果"
            daig_allow = "UPDATE dapplication set da_status='" + status + "'where da_mname='" + MRI_Name + "'"
            try:
                # 执行sql语句
                cursor.execute(daig_allow)
                db.commit()
                # 这里将会自动从results文件夹下面获得对应用户的MRI标签图像
                msg = "确诊成功！"
                return redirect('ExpertDApply')
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = "服务器错误，确诊失败，请重新确诊！"
                return redirect('ExpertDApply')
            # 关闭数据库连接
            db.close()
        elif number == 3:
            # 这里将对专家用户的 个人成就表进行修改，将初始值写入
            status = "申请完毕"
            j_apply = "UPDATE japply set j_astatus='" + status + "'where j_eid='" + MRI_Name + "'"#MRI_Name表示专家ID
            try:
                # 执行sql语句
                cursor.execute(j_apply)
                db.commit()
                # 这里将会自动从results文件夹下面获得对应用户的MRI标签图像
                msg = "入职申请批准成功！"
                return redirect('AdminJApply')
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = "服务器错误，批准失败，请重新批准！"
                return redirect('AdminJApply')
            # 关闭数据库连接
            db.close()
        elif number == 4:
            expertid = MRI_Name
            japply = "select * from japply where j_eid='" + expertid + "'"  # 获得入职申请列表
            try:
                # 执行sql语句
                cursor.execute(japply)
                japply_r = cursor.fetchall()
                if japply_r:
                    db.commit()
                    print("查看成功！")
                    return render_template('admin/AdminExpertResume.html', username=username, expertid=expertid, japply=japply_r)
                else:
                    db.commit()
                    print("暂无该专家用户的个人履历")
                    return render_template('admin/AdminExpertResume.html', username=username, expertid=expertid, japply_r=japply_r)
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = "服务器错误，查看失败！"
                return render_template('admin/AdminExpertResume.html', experid=msg)
            # 关闭数据库连接
            db.close()
        # elif number == 11:


# 管理员对申请的MRI影像进行预测
@app.route('/<string:userid>/<string:MRIName>', methods=['GET', 'POST'])
def AdminPred(userid, MRIName):
    if request.method == 'GET':
        return render_template('admin/AdminDApply.html')
    if request.method == 'POST':
        db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
        cursor = db.cursor()
        username = userid
        MRI_Name = MRIName
        duration = Prediction(username, MRI_Name)
        print('总耗时{}s'.format(duration))
        if duration:
            mri = "select * from mri where m_name='" + MRI_Name + "'"  # 从MRI影像表中查询该MRI影像的信息，并获取其中的用户ID和上传时间信息
            status = "预测完毕"
            daig_allow = "UPDATE dapplication set da_status='" + status + "'where da_mname='" + MRI_Name + "'"
            p_utime = ""
            cursor.execute(mri)
            mri_r = cursor.fetchall()
            if mri_r:
                db.commit()
                p_utime = mri_r[0][3]
                p_utime = p_utime.strftime('%Y-%m-%d %H:%M:%S')  # 将时间格式转换为str格式
            p_ptime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            r_hipvolu = get_PredHipvlouSum(MRI_Name=MRI_Name)  # 这里是通过MRI影像名称来获得该MRI影像，并计算出其海马体大小。5000为一个临时值
            r_hipvolu = str(r_hipvolu)
            pred_insert = "INSERT INTO pred(p_uid, p_mname, p_ptime, p_utime, p_hipvolu) VALUES " \
                          "('" + username + "','" + MRI_Name + "','" + p_ptime + "','" + p_utime \
                          + "','" + r_hipvolu + "')"
            try:
                # 执行sql语句
                cursor.execute(pred_insert)
                db.commit()
                cursor.execute(daig_allow)
                # 提交到数据库执行
                db.commit()
                msg = '预测完毕！'
                return redirect('AdminDApply')
            except:
                # 抛出错误信息
                traceback.print_exc()
                # 如果发生错误则回滚
                db.rollback()
                msg = '预测失败！'
                return redirect('AdminDApply')
            # 关闭数据库连接
            db.close()

"""
程序的启动入口
"""
if __name__ == '__main__':
    app.run(debug=True)
