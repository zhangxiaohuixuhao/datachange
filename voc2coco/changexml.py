# coding=utf-8
import xml.etree.ElementTree as et
import os
import cv2


def findclass():
    #查看所有XML文件中所有的类别有哪一些
    xml_lst = os.listdir('/DATA/zhanghui/car_park/new/Annotations/')
    class_name = []
    with open('class_name.txt', 'w') as f:
        for axml in xml_lst:
            path_xml = os.path.join('/DATA/zhanghui/car_park/new/Annotations/', axml)
            tree = et.parse(path_xml)
            root = tree.getroot()
            for child in root.findall('object'):
                name = child.find('name').text
                if name not in class_name:
                    class_name.append(name)
                    f.write(name + '\n')
    return class_name

def change_xml():
    #修改xml文件中的类别并保存修改之后的xml文件
    xml_lst = os.listdir(path_car)
    for axml in xml_lst:
        path_xml = os.path.join(path_car, axml)
        tree = et.parse(path_xml)
        root = tree.getroot()
        for child in root.findall('object'):
            name = child.find('name').text
            # if name == 'Perpendicular_Parking':
            #     child.find('name').text = 'Parallel_Parking'
            if not name in class_name:
                child.find('name').text = 'Others'
        num_child = root.findall('object')
        if len(num_child) == 0:
            continue
        else:
            tree.write(os.path.join(path_rename, axml))

def delete_lab():
    #删除xml中不需要的类别并保存剩余的类别文件
    xml_lst = os.listdir(path0)
    for axml in xml_lst:
        path_xml = os.path.join(path0, axml)
        tree = et.parse(path_xml)
        root = tree.getroot()
        for child in root.findall('object'):
            name = child.find('name').text
            if name == 'Others':
                root.remove(child)
        num_child = root.findall('object')
        if len(num_child) == 0:
            continue
        else:
            tree.write(os.path.join(path_car, axml))

def delete_img():
    #根据修改的xml文件若删除了空的文件之后将图片也删掉
    xml_lst = os.listdir(end_xml)
    for axml in xml_lst:
        img_name = axml[:-4] + '.jpg'
        path_img = os.path.join(path_img1, img_name)
        img = cv2.imread(path_img)
        cv2.imwrite(os.path.join(path_img2, img_name), img)


path0 = '/DATA/zhanghui/car_park/Annotations_labelImg/'
path_car = '/DATA/zhanghui/car_park/car/'
path_rename = '/DATA/zhanghui/car_park/rename/'
path_img1 = '/DATA/zhanghui/yzrgb/video2/'
path_img2 = '/DATA/zhanghui/yzrgb/test/'
end_xml = '/DATA/zhanghui/yzrgb/video2_lab/'

class_name = ['Along_Double_Yellow_Lines', 'Parallel_Parking', 'Others', 'Car', 'Motorcycle', 'Truck']

# findclass()
change_car()
# change_xml()
# delete_img()

