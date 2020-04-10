# coding:utf-8
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import cv2
#项目中有3个类别，类别名称在这里修改
classes = ['holothurian', 'echinus', 'scallop', 'starfish']
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    #这里改为xml文件夹的路径
    in_file = open('/DATA/zhanghui/wanglei/train/box/%s.xml'%(image_id))
    #这里是生成每张图片对应的txt文件的路径
    out_file = open('/DATA/zhanghui/wanglei/train/txtbox/%s.txt'%(image_id),'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')  
    w = int(size.find('width').text)
    h = int(size.find('height').text)#

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')   
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

def file_name(file_dir):     
    L = []
    for root, dirs, files in os.walk(file_dir):    
        for file in files:      
            L.append(os.path.splitext(file)[0])    
    return L  

train_datas = open("//DATA/zhanghui/wanglei/train/train.txt","w+")
dir=file_name('/DATA/zhanghui/wanglei/train/image/')
for i in range(len(dir)):
	train_datas.write(str(dir[i])+"\n")
train_datas.close()
image_ids_train = open('/DATA/zhanghui/wanglei/train/train.txt').read().strip().split()

list_file_train = open('/DATA/zhanghui/wanglei/train/bag_train.txt', 'w')
for image_id in image_ids_train:
    #这里改为样本图片所在文件夹的路径
    list_file_train.write('/DATA/zhanghui/wanglei/train/image/%s.jpg\n'%(image_id))
    # img = cv2.imread()
    convert_annotation(image_id)   
list_file_train.close()
