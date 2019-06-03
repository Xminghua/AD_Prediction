#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 14:04
# @Author  : HuaCode
# @File    : HipvoluSum.py
# @Software: PyCharm

import numpy as np
import os
import nibabel as nib
import shutil

def get_hipvlousum(username, MRI_Name):
    pred_path = "./static/requiredimages/expert/" + username + "/upload/"
    # 单独测试用
    # pred_path = "../static/requiredimages/admin/Pred/"
    if not os.path.exists(pred_path):
        os.makedirs(pred_path)
    tlabel = nib.load(pred_path +  MRI_Name)
    label = tlabel.get_data()
    label = label.transpose(2,1,0)
    label = label[::-1,::-1,:]
    bool_label = label.astype(np.bool)
    hipvolu_sum = np.sum(bool_label)
    if hipvolu_sum:
        print(hipvolu_sum)
        return hipvolu_sum
    else:
        print("数量为空！")
        return 0

def get_PredHipvlouSum(MRI_Name):
    pred_path = "./static/requiredimages/admin/Pred/"
    # 单独测试用
    # pred_path = "../static/requiredimages/admin/Pred/"
    if not os.path.exists(pred_path):
        os.makedirs(pred_path)
    tlabel = nib.load(pred_path +  MRI_Name)
    label = tlabel.get_data()
    label = label.transpose(2,1,0)
    label = label[::-1,::-1,:]
    bool_label = label.astype(np.bool)
    hipvolu_sum = np.sum(bool_label)
    if hipvolu_sum:
        print(hipvolu_sum)
        return hipvolu_sum
    else:
        print("数量为空！")
        return 0



# if __name__ == '__main__':
#     name = "ADNI_002_S_0295_13722.nii"
#     name1 = "ADNI_002_S_0295_MR_HarP_135_final_release_2015_Br_20150226095012465_S13408_I474728.nii"
#     name2 = "ADNI_002_S_0295_13722-dense-uU-pred.nii"
#     name3 = "ADNI_002_S_0413_14437-dense-uU-pred.nii"
#     name4 = "ADNI_002_S_0413_MR_HarP_135_final_release_2015_Br_20150226110131972_S13893_I474824.nii"
    # get_hipvlousum(username=None, MRI_Name=name)
    # get_hipvlousum(username=None, MRI_Name=name1)
    # get_hipvlousum(username=None, MRI_Name=name2)
    # get_hipvlousum(username=None, MRI_Name=name3)
    # get_hipvlousum(username=None, MRI_Name=name4)


