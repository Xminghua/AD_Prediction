#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 11:47
# @Author  : HuaCode
# @File    : models.py
# @Software: PyCharm

from app import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例
from datetime import datetime



# 管理员表
class Admin(db.Model):
    __tablename__ = 'admin'
    a_id = db.Column(db.String(30), primary_key=True, nullable=False)
    a_pwd = db.Column(db.String(30), nullable=False)
    a_name = db.Column(db.String(30), nullable=False)
    a_sex = db.Column(db.String(4), nullable=False)
    a_birth = db.Column(db.String(20), nullable=False)
    a_phone = db.Column(db.String(11), unique=True, nullable=False)

    def __init__(self,a_id, a_pwd, a_name, a_sex, a_birth, a_phone):
        self.a_id = a_id
        self.a_pwd = a_pwd
        self.a_name = a_name
        self.a_sex = a_sex
        self.a_birth = a_birth
        self.a_phone = a_phone

    def save(self):
        db.session.add(self)
        db.session.commit()


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    u_id = db.Column(db.String(30), primary_key=True, nullable=False)
    u_pwd = db.Column(db.String(30), nullable=False)
    u_name = db.Column(db.String(30), nullable=False)
    u_sex = db.Column(db.String(4), nullable=False)
    u_birth = db.Column(db.String(20), nullable=False)
    u_phone = db.Column(db.String(11), unique=True, nullable=False)

    def __init__(self, u_id, u_pwd, u_name, u_sex, u_birth, u_phone):
        self.u_id = u_id
        self.u_pwd = u_pwd
        self.u_name = u_name
        self.u_sex = u_sex
        self.u_birth = u_birth
        self.u_phone = u_phone

    def save(self):
        db.session.add(self)
        db.session.commit()

# 专家表
class Expert(db.Model):
    __tablename__ = 'expert'
    e_id = db.Column(db.String(30), primary_key=True, nullable=False)
    e_pwd = db.Column(db.String(30), nullable=False)
    e_name = db.Column(db.String(30), nullable=False)
    e_sex = db.Column(db.String(4), nullable=False)
    e_birth = db.Column(db.String(20), nullable=False)
    e_phone = db.Column(db.String(11), unique=True, nullable=False)

    def __init__(self,e_id, e_pwd, e_name, e_sex, e_birth, e_phone):
        self.e_id = e_id
        self.e_pwd = e_pwd
        self.e_name = e_name
        self.e_sex = e_sex
        self.e_birth = e_birth
        self.e_phone = e_phone

    def save(self):
        db.session.add(self)
        db.session.commit()

# 专家成就表
class EAchievement(db.Model):
    __tablename__ = 'eachievement'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    ea_eid = db.Column(db.String(30), db.ForeignKey('expert.e_id'))
    ea_identity = db.Column(db.String(30), nullable=True)
    ea_level = db.Column(db.String(30), nullable=True)
    ea_score = db.Column(db.Integer, nullable=True)
    ea_diagnum = db.Column(db.Integer, nullable=True)
    # ea_rank = db.Column(db.String(11), unique=True, nullable=True)

    def __init__(self,ea_eid, ea_identity, ea_level, ea_score, ea_diagnum):
        self.ea_eid = ea_eid
        self.ea_identity = ea_identity
        self.ea_level = ea_level
        self.ea_score = ea_score
        self.ea_diagnum = ea_diagnum
        # self.ea_rank = ea_rank

    def save(self):
        db.session.add(self)
        db.session.commit()

# MRI影像表
class MRI(db.Model):
    __tablename__ = 'mri'
    m_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    m_uid = db.Column(db.String(30), db.ForeignKey('user.u_id'))
    m_name = db.Column(db.String(200), unique=True, nullable=False)
    m_utime = db.Column(db.DateTime, default=datetime.now, unique=True, nullable=False)
    m_getime = db.Column(db.String(20), nullable=False)

    def __init__(self, m_uid, m_name, m_utime, m_getime):
        self.m_uid = m_uid
        self.m_name = m_name
        self.m_utime = m_utime
        self.m_getime = m_getime

    def save(self):
        db.session.add(self)
        db.session.commit()

# 诊断申请表
class DApplication(db.Model):
    __tablename__ = 'dapplication'
    da_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    da_uid = db.Column(db.String(30), db.ForeignKey('user.u_id'))
    da_mname = db.Column(db.String(200), db.ForeignKey('mri.m_name'))
    da_atime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    da_status = db.Column(db.String(10), nullable=False)

    def __init__(self, da_uid, da_mname, da_atime, da_status):
        self.da_uid = da_uid
        self.da_mname = da_mname
        self.da_atime = da_atime
        self.da_status = da_status

    def save(self):
        db.session.add(self)
        db.session.commit()

# 预测结果表
class Pred(db.Model):
    __tablename__ = 'pred'
    p_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    p_uid = db.Column(db.String(30), db.ForeignKey('user.u_id'))
    p_mname = db.Column(db.String(200), db.ForeignKey('mri.m_name'))
    p_ptime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    p_utime = db.Column(db.DateTime, db.ForeignKey('mri.m_utime'), unique=True)
    p_hipvolu = db.Column(db.Integer, nullable=False)

    def __init__(self, p_uid, p_mname, p_ptime, p_utime, p_hipvolu):
        self.p_uid = p_uid
        self.p_mname = p_mname
        self.p_ptime = p_ptime
        self.p_utime = p_utime
        self.p_hipvolu = p_hipvolu

    def save(self):
        db.session.add(self)
        db.session.commit()

# 结果反馈表
class Resu(db.Model):
    __tablename__ = 'resu'
    r_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    r_uid = db.Column(db.String(30), db.ForeignKey('user.u_id'))
    r_eid = db.Column(db.String(30), db.ForeignKey('expert.e_id'))
    r_mname = db.Column(db.String(200), db.ForeignKey('mri.m_name'))
    r_rtime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    r_utime = db.Column(db.DateTime, db.ForeignKey('mri.m_utime'), unique=True)
    r_hipvolu = db.Column(db.Integer, nullable=False)
    r_diag = db.Column(db.String(200), nullable=False)

    def __init__(self, r_uid, r_eid, r_mname,  r_rtime, r_utime, r_hipvolu, r_diag):
        self.r_uid = r_uid
        self.r_eid = r_eid
        self.r_mname = r_mname
        self.r_rtime = r_rtime
        self.r_utime = r_utime
        self.r_hipvolu = r_hipvolu
        self.r_diag = r_diag

    def save(self):
        db.session.add(self)
        db.session.commit()

# 入职申请表
class JApply(db.Model):
    __tablename__ = 'japply'
    j_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    j_eid = db.Column(db.String(30), db.ForeignKey('expert.e_id'))
    j_atime = db.Column(db.DateTime, default=datetime.now, nullable=False)
    j_aidentity = db.Column(db.String(30), nullable=False)
    j_asalary = db.Column(db.String(10), nullable=False)
    j_resume = db.Column(db.String(800), unique=True, nullable=False)
    j_astatus = db.Column(db.String(10), nullable=False)

    def __init__(self, j_eid, j_atime, j_aidentity, j_asalary, j_resume, j_astatus):
        self.j_eid = j_eid
        self.j_atime = j_atime
        self.j_aidentity = j_aidentity
        self.j_asalary = j_asalary
        self.j_resume = j_resume
        self.j_astatus = j_astatus

    def save(self):
        db.session.add(self)
        db.session.commit()
