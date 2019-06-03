#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 11:47
# @Author  : HuaCode
# @File    : create_db.py
# @Software: PyCharm

from app import db
from app.models import User, Admin, Expert, MRI, DApplication, EAchievement, Resu, Pred, JApply
from flask import render_template, session
import pymysql
import traceback

# 创建数据库：create database adms default charset utf8;
# 创建数据库及表
def create_db():
    """
    创建数据库表
    """
    db.create_all()
    return '创建成功'

# 删除数据库及表
def drop_db():
    """
    删除数据库
    """
    db.drop_all()
    return '删除成功'

def add_Admin():
    """
    添加管理员数据
    :return:
    """
    # 声明对象
    admin = Admin(a_id='1111111', a_pwd='123456a', a_name='许明华', a_sex='男', a_birth='1994-12-15', a_phone='18402869099')
    # 调用添加方法
    db.session.add(admin)
    # 提交入库
    db.session.commit()

def add_User():
    """
    添加普通用户数据
    :return:
    """
    user1 = User(u_id='1111111', u_pwd='123456a', u_name='孟萍', u_sex='女', u_birth='1995-09-05', u_phone='13618025199')
    user2 = User(u_id='2222222', u_pwd='123456a', u_name='黄程', u_sex='男', u_birth='1995-09-05', u_phone='18782413894')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

def add_Expert():
    """
    添加专家用户数据
    :return:
    """
    expert = Expert(e_id='1234abc', e_pwd='111111a', e_name='廖浩杰', e_sex='男', e_birth='1996-04-12', e_phone='15680814096')
    db.session.add(expert)
    db.session.commit()

def add_achievement():
    """
    添加普通用户数据
    :return:
    """
    user1 = EAchievement(ea_eid='2010abc', ea_identity='三级专家', ea_level='诊断一级', ea_score=10, ea_diagnum=1, ea_rank='1')
    user2 = EAchievement(ea_eid='2011abc', ea_identity='二级专家', ea_level='诊断二级', ea_score=100, ea_diagnum=10, ea_rank='2')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

def del_user():
    """
    删除某条数据
    :return:
    """
    # 根据某个字段做删除，filter_by可以理解为where条件限定
    # 翻译为   delete from user where id = 1
    User.query.filter_by(id=1).delete()
    return '这里是删除操作'

def edit_user():
    """
    修改某条数据
    :return:
    """
    # 根据某个字段做修改操作
    # 翻译为update user set u_name='张三' where id=1
    User.query.filter_by(id=1).update({'u_name':'张三'})

def select_user():
    """
    查询数据库操作
    :return:
    """
    #简单的全量查询
    # 翻译为  select * from user
    # ulist = User.query.all()
    # print(ulist)
    # for i in ulist:
    #     print(i.name,i.password)

    #只取一条
    # ulist = User.query.first()
    # print(ulist)
    #使用原生的sql语句
    #翻译为  select * from user order by id desc limit 1,2
    sql = 'select * from mri order by m_id desc'
    item = db.session.execute(sql)

    # item = db.session.execute('select * from user order by id desc')
    #将结果集强转为list
    item = list(item)
    # item = item[0][3]
    print(item)
    # item = db.session.execute('update user set u_pwd = "321321" where id=1')
    # 将动态数据传递给模板
    # return render_template('index.html', item=item)

def select_mri():
    # m_name = "ADNI_002_S_0413_MR_HarP_135_final_release_2015_Br_20150226110131972_S13893_I474824.nii"
    # mri = "select * from mri where m_name='" + m_name + "'"
    # item = db.session.execute(mri)
    # item = list(item)
    username = "2222222"
    mri = MRI.query.filter(MRI.m_uid == username).order_by(MRI.m_id.desc()).first()
    if mri:
        mri.save()
        print(mri.m_name)
    else:
        print("nothing")

def selectuser():
    user = User.query.get("1111111");
    print(user.u_birth)

def selectMRI():
    mri = MRI.query.order_by('-m_id').first()
    print(mri.m_id)

def selectDApply():
    db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
    cursor = db.cursor()
    dapply = "select * from dapplication"  # 获得诊断申请列表查询语句 where da_uid='" + username + "'"
    try:
        # 执行sql语句
        cursor.execute(dapply)
        da_re = cursor.fetchall()
        da = ()
        for i in da_re:
            if i[4] == "申请中":
                i = i + ('/Allow', 'btn btn-success', 'submit', '批准')
            da += ((i),)
        print(da)
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        msg = "服务器错误！"

    # 关闭数据库连接
    db.close()

def select_japply():
    db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
    cursor = db.cursor()
    username = "1234abc"
    r_mname = "ADNI_002_S_0295_MR_HarP_135_final_release_2015_Br_20150226095012465_S13408_I474728.nii"
    mri = "select * from mri where m_name='" + r_mname + "'"
    cursor.execute(mri)
    mri_r = cursor.fetchall()
    r_uid = mri_r[0][1]
    r_utime = mri_r[0][3]
    print(mri_r)
    print(r_uid)
    print(r_utime)
    db.commit()
    db.close()
    # japply = "select * from japply where j_eid='" + username + "'"  # 获得入职申请列表
    # japply_r1 = ()
    # try:
    #     # 执行sql语句
    #     cursor.execute(japply)
    #     japply_r = cursor.fetchall()
    #     if japply_r:
    #         db.commit()
    #         print(japply_r[0][5])
    #         resume = japply_r[0][5][:20] + '***'  # 截取指定部分的个人履历进行显示
    #         for i in japply_r:
    #             i = i + (resume,)
    #             japply_r1 += ((i),)
    #         print(japply_r1)
    #     else:  # 如果查询到的结果为空，就直接返回
    #         db.commit()
    #         msg = "(暂无入职申请)"
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # 如果发生错误则回滚
    #     traceback.print_exc()
    #     db.rollback()
    #     msg = "服务器错误！"
    # # 关闭数据库连接
    # db.close()

def select_achievement():
    db = pymysql.connect("127.0.0.1", "root", "638436", "adms")
    cursor = db.cursor()
    # username = "1234abc"
    # r_mname = "ADNI_002_S_0295_MR_HarP_135_final_release_2015_Br_20150226095012465_S13408_I474728.nii"
    # mri = "select * from mri where m_name='" + r_mname + "'"
    # 方法一：
    # select Score, (select count(distinct Score) from Scores where Score>=s.Score) as Rank from Scores as s order by Score desc;
    # rank = "select ea_eid, ea_score, (select count(distinct ea_score) from eachievement where ea_score >= s.ea_score) " \
    #        "as Rank from eachievement as s order by ea_score desc"
    username = "1111111"
    resu = "select * from resu where r_uid='" + username + "'"
    cursor.execute(resu)
    rhipvlou_r = cursor.fetchall()
    print(rhipvlou_r)
    data = []
    for i in rhipvlou_r:
        x_data = "海马体数量" + "-" + i[4].strftime('%Y.%m.%d')
        y_data = int(i[6])
        print(x_data)
        print(y_data)
        data_dict = {"name":x_data,"num":y_data}
        data.append(data_dict)
    print(data)
    # r_uid = mri_r[0][1]
    # r_utime = mri_r[0][3]
    # print(mri_r)
    # print(r_uid)
    # print(r_utime)
    db.commit()
    db.close()


if __name__ == '__main__':
    # drop_db()
    # create_db()
    # add_Admin();
    # add_User();
    # add_Expert();
    # selectuser();
    # selectMRI();
    # select_user();
    # select_mri();
    # selectDApply();
    select_japply();
    # add_achievement();
    # select_achievement();
