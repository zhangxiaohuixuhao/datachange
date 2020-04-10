# -*- coding:utf-8 -*-
import cv2
import os
import glob

files = glob.glob('/DATA/zh_1210/WIN_20191210_09_31_07_Pro/*jpg')
for f in files:
    os.remove(f)
def save_img():
    video_path = '/DATA/datasets_gz/yzpark/20191210/'
    img = '/DATA/zh_1210/WIN_20191210_09_31_07_Pro/'
    # videos = os.listdir(video_path)
    # for video_name in videos:
    #     file_name = video_name.split('.mp4')
    #     # folder_name = img + str(file_name[0])
    #     # os.makedirs(folder_name)
    vc = cv2.VideoCapture(video_path+'WIN_20191210_09_31_07_Pro.mp4') #读入视频文件
    c = 0
    rval = vc.isOpened()

    while rval:   #循环读取视频帧
        rval, frame = vc.read()
        # pic_path = folder_name+'/'
        if rval:
            c = c + 1
            if c % 10 == 0:
                # num = ("%06d" % (c))
                # row, col, channel = frame.shape
                cv2.imwrite(img + 'WIN_20191210_09_31_07_Pro' + str(c) + '.jpg', frame) #存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg

                # cv2.waitKey(1)
        else:
            break
    vc.release()
    print('save_success')
save_img()