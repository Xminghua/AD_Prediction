#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 13:38
# @Author  : HuaCode
# @File    : img_crop.py
# @Software: PyCharm
import os
import numpy as np
import nibabel as nib

def image_crop(username, MRI_Name):
    img_name = "./static/requiredimages/user/" + username + "/upload/" + MRI_Name
    label_name = "./static/requiredimages/label/" + MRI_Name
    # 测试用
    # img_name = "../static/requiredimages/user/1111111/upload/" + MRI_Name
    # label_name = "../static/requiredimages/label/" + MRI_Name
    img = os.path.basename(img_name)
    print(img)
    timg = nib.load(img_name)
    image = timg.get_data()
    image = image.transpose(2,1,0)
    image = image[::-1, ::-1, :]  # 进行了一个左右翻转

    tlabel = nib.load(label_name)
    label = tlabel.get_data()
    label = label.transpose(2,1,0)
    label = label[::-1, ::-1, :]
    bool_label = label.astype(np.bool)

    axis_list = np.where(bool_label)

    center_x = (axis_list[0].max() + axis_list[0].min()) / 2  # 获得x轴的中间值
    # print center_x
    center_y = (axis_list[1].max() + axis_list[1].min()) / 2  # 获得y轴的中间值
    # print center_y
    center_z = (axis_list[2].max() + axis_list[2].min()) / 2  # 获得z轴的中间值
    # print center_z
    centerpoint = [np.array(center_x, np.int32), np.array(center_y, np.int32), np.array(center_z, np.int32)]

    image_block = image[centerpoint[0] - 32:centerpoint[0] + 32, centerpoint[1] - 32:centerpoint[1] + 32,
                  centerpoint[2] - 48:centerpoint[2] + 48]
    nib.save(nib.Nifti1Image(image_block, timg.affine), './static/requiredimages/admin/Croped/' + img)
    print('croped！')


#对MRI格式图像进行裁剪，裁剪大小为(64,64,96)(96,96,80)
# def image_crop(username, MRI_Name):
#     # img_name = "../static/requiredimages/user/" + username + "/upload/" + MRI_Name
#     img_name = "../static/requiredimages/user/1111111/upload/" + MRI_Name
#     img = os.path.basename(img_name)
#     print(img)
#     timg = nib.load(img_name)
#
#     image = timg.get_data()
#     image = image.transpose(2,1,0)
#
#     image = image[::-1, ::-1, :]  # 进行了一个左右翻转
#     center_x = (image.shape[0]) / 2
#     center_y = (image.shape[1]) / 2
#     center_z = (image.shape[2]) / 2
#     centerpoint = [np.array(center_x, np.int32), np.array(center_y, np.int32), np.array(center_z, np.int32)]
#     img_block = image[centerpoint[0] - 48:centerpoint[0] + 48, centerpoint[1] - 48:centerpoint[1] + 48,
#                  centerpoint[2] - 40:centerpoint[2] + 40]
#     # img_block = image[centerpoint[0] - 32:centerpoint[0] + 32, centerpoint[1] - 32:centerpoint[1] + 32,
#                 # centerpoint[2] - 48:centerpoint[2] + 48]
#     nib.save(nib.Nifti1Image(img_block, timg.affine), '../static/requiredimages/admin/Croped/' + img)
#     print('croped！')