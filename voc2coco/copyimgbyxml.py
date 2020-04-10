import os
import random
import glob
import shutil

path1 = '/DATA/zh_1210/yzrgb/Annotations/'
path2 = '/DATA/zh_1210/yzrgb/images/'
pathsave = '/DATA/zh_1210/yzrgb/JPEGImages/'
file = glob.glob(path1 + '*.xml')
for xmlpath in file:
    imgname = os.path.basename(xmlpath)[:-4] + '.jpg'
    imgpath = os.path.join(path2 + imgname)
    shutil.copy(imgpath, os.path.join(pathsave + imgname))