# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os, cv2

path_img1 = '/DATA/zhanghui/new_img/'
path_img2 = '/DATA/zhanghui/new_img/'
end_xml = '/DATA/zhanghui/Annotations_labelImg1/'

xml_file = 'C:/Users/nansbas/Desktop/01_000002_01244-01086_0939-0989.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
imgfile = 'C:/Users/nansbas/Desktop/01_000002_01244-01086_0939-0989.jpg'
im = cv2.imread(imgfile)
for object in root.findall('object'):
    object_name = object.find('name').text
    Xmin = int(object.find('bndbox').find('xmin').text)
    Ymin = int(object.find('bndbox').find('ymin').text)
    Xmax = int(object.find('bndbox').find('xmax').text)
    Ymax = int(object.find('bndbox').find('ymax').text)
    color = (4, 250, 7)
    cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(im, object_name, (Xmin, Ymin - 7), font, 0.5, (6, 230, 230), 2)
    cv2.imshow('01', im)
cv2.imwrite('C:/Users/nansbas/Desktop/02.jpg', im)