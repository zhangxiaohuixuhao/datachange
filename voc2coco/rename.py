# coding utf-8
import os, shutil
import random
import numpy as np


def renameData(xmlDir, imgDir):
    xmlFiles = os.listdir(xmlDir)
    total = len(xmlFiles)
    cur = 0
    for xml in xmlFiles:
        cur += 1
        if cur % 500 == 1:
            print("Total/cur:", total, "/", cur)
        imgPath = imgDir + xml[:-4] + ".jpg"

        outName = ("%08d" % (cur))

        outXMLPath = ("%s%s.xml" % (xmlDir, outName))
        outImgPath = ("%s%s.jpg" % (imgDir, outName))

        os.rename(xmlDir + xml, outXMLPath)
        os.rename(imgPath, outImgPath)

    print("picker number:", cur)


if __name__ == '__main__':
    # 下面的图片路径和标注路径注意更改为自己的实际路径
    xmlDir = "/DATA/zh_1210/yzrgb/yolo/Annotations/"
    imgDir = "/DATA/zh_1210/yzrgb/yolo/JPEGImages/"

    print(xmlDir)
    print(imgDir)

    renameData(xmlDir, imgDir)


