#!/usr/bin/env python
#-*- coding:utf-8 -*-
# from load_data2 import loadDataGeneral2
import numpy as np
import pandas as pd
import nibabel as nib
from keras.models import load_model
import time
import os
from Pred.ImgCrop import image_crop
from scipy.misc import imresize
from skimage.color import hsv2rgb, rgb2hsv, gray2rgb
from skimage import io, exposure


"""
在此基础上进行单张图片的测试，并求出Dice值和IoU值，
target_folder文件夹下面必须有三个建好的文件夹，pred，image，label
"""

def squeeze_dim(img):
    if img.ndim == 4:
        if img.shape[0] == 1:
            img = np.squeeze(img,axis=0)
        if img.shape[1] == 1:
            img = np.squeeze(img,axis=1)
        if img.shape[2] == 1:
            img = np.squeeze(img,axis=2)
        if img.shape[3] == 1:
            img = np.squeeze(img,axis=3)
    else:
        pass
    return img

def crop(img, a , b, c):
    '''
    有一个缺点就是 a,b,c的值只能是偶数,即便是设置为奇数,返回的shape也是(a-1,b-1,c-1)之类的偶数形状
    '''
    img_shape = img.shape
    img_a = img_shape[0]
    img_b = img_shape[1]
    img_c = img_shape[2]
    img_res = img[img_a//2-a//2:img_a//2+a//2, img_b//2-b//2:img_b//2+b//2, img_c//2-c//2:img_c//2+c//2]
    return img_res

def decrop(in_img,shell):
    """
    shell 是一个全零的壳子矩阵,用来装预测的图形
    in_img 是预测得到的被剪切图像
    """
    in_img_shape = in_img.shape
    shell_shape = shell.shape
    a = in_img_shape[0]
    b = in_img_shape[1]
    c = in_img_shape[2]
    img_a = shell_shape[0]
    img_b = shell_shape[1]
    img_c = shell_shape[2]
    shell[img_a//2-a//2:img_a//2+a//2, img_b//2-b//2:img_b//2+b//2, img_c//2-c//2:img_c//2+c//2] = in_img
    return shell

#单张图片的数据加载
def loadSingleData(img_name):
    X, shape_list = [], []
    nii_img = nib.load(img_name)
    img = nii_img.get_data()
    img = squeeze_dim(img)
    shape = img.shape
    # img = crop(img, 96, 96, 80)
    img = crop(img, 64, 64, 96)

    img = np.array(img, dtype=np.float64)
    brain = img > 0
    #img -= img[brain].mean()
    #img /= img[brain].std()
    img -= img.mean()
    img /= img.std()
    X.append(img)
    shape_list.append(shape)
    X = np.array(X)
    print(X.mean())
    print('std:{}'.format(X.std()))
    X = np.expand_dims(X, -1)

    print('### Dataset loaded')
    # print('\t{}\t'.format(path))
    print('\t{}\t'.format(X.shape))
    print('\tX:{:.1f}-{:.1f}\t'.format(X.min(), X.max()))
    return X, shape_list

def IoU(y_true, y_pred):
    '''
    交叉联合预测函数，返回的是交叉联合得到的分数
    :param y_true:
    :param y_pred:
    :return:
    '''
    assert y_true.dtype == bool and y_pred.dtype == bool
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.logical_and(y_true_f, y_pred_f).sum()
    union = np.logical_or(y_true_f, y_pred_f).sum()
    return (intersection + 1) * 1. / (union + 1)

def Dice(y_true, y_pred):
    '''
    #dice metric指标:Dice(A, B) =2|A ∩ B|/(|A| + |B|)，
    其中A为分割图,B为ground-truth 真实分割,|A|和|B|分别为A和B分割图的体素(三维像素)数量,
    |A ∩ B|为两图重合部分的体素数量。
    :param y_true:
    :param y_pred:
    :return:
    '''
    assert y_true.dtype == bool and y_pred.dtype == bool
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.logical_and(y_true_f, y_pred_f).sum()
    return (2. * intersection + 1.) / (y_true.sum() + y_pred.sum() + 1.)

def Prediction(username, MRI_Name):
    '''

    :param img_name:
    :return:
    '''
    start_time = time.time()
    image_crop(username, MRI_Name)
    img_name = "./static/requiredimages/admin/Croped/" + MRI_Name
    # 测试用
    # img_name = "../static/requiredimages/admin/Croped/" + MRI_Name
    df = os.path.basename(img_name)
    X, shape_list = loadSingleData(img_name)
    n_test = X.shape[0]
    print(n_test)
    model_name1 = './Model/Unet_model.100.hdf5'  # 加载预测的模型,可变数据
    model_name2 = './Model/Dense_unet_model.100.hdf5'

    model1 = load_model(model_name1)
    model2 = load_model(model_name2)
    pred1 = model1.predict(X, batch_size=1)[..., 1]
    pred2 = model2.predict(X, batch_size=1)[..., 1]
    pred = pred1 * 0.3077 + pred2 * 0.6923

    save_pred_folder = "./static/requiredimages/admin/Pred/"
    # 测试用
    # save_pred_folder = "../static/requiredimages/admin/Pred/"
    if not os.path.exists(save_pred_folder):
        os.makedirs(save_pred_folder)
    IoU_list = []
    Dice_list = []
    IoUs = np.zeros(n_test)
    Dices = np.zeros(n_test)
    for i in range(n_test):
        # gt = y[i, :, :, :, 1] > 0.5
        pr = pred[i] > 0.5
        shell = np.zeros(shape_list[i])
        pr = decrop(pr, shell)
        ifsave = True
        if ifsave:
            tImg = nib.load(img_name)
            nib.save(nib.Nifti1Image(2 * pr.astype('float'), affine=tImg.get_affine()),
                     save_pred_folder + df[:-4] + '.nii')  # 存储具体的预测结果图，可变数据


            # tImg = nib.load(img_name)
            # nib.save(nib.Nifti1Image(2 * pr.astype('float'), affine=tImg.get_affine()),
            #          save_pred_folder + df[:-4] + '.nii')
    duration = time.time() - start_time
    print("all is done!")
    return duration

# if __name__ == '__main__':
#     MRI_Name = "ADNI_002_S_0413_MR_HarP_135_final_release_2015_Br_20150226110131972_S13893_I474824.nii"
#     Prediction(username=None, MRI_Name=MRI_Name)
