import os
import random
import glob
import shutil

test_percent = 0
val_percent = 0.1
# train_percent = 0.7
files = glob.glob('/DATA/zh_1210/yzrgb/coco/JPEGImages/*.jpg')

total_num = len(files)
test_num = int(total_num * test_percent)
val_num = int(total_num * val_percent)
# train_num = int(total_num * train_percent)

total_list = range(total_num)
test_val_list = random.sample(total_list, test_num + val_num)
test_list = random.sample(test_val_list, test_num)

for i in total_list:
    path = files[i]
    path1 = path.split('/')[-2]
    path2 = path.split('/')[-1]
    pathxml = 'Annotations'
    if i in test_val_list:
        if i in test_list:
            shutil.copy(path, os.path.join('/DATA/zh_1210/yzrgb/coco/test/', path1 + '/'))
            shutil.copy(os.path.join('/DATA/zh_1210/yzrgb/coco/', pathxml, path2[:-4] + '.xml'), os.path.join('/DATA/zh_1210/yzrgb/coco/test/', pathxml, path2[:-4] + '.xml'))
        else:
            shutil.copy(path, os.path.join('/DATA/zh_1210/yzrgb/coco/minival/', path1 + '/'))
            shutil.copy(os.path.join('/DATA/zh_1210/yzrgb/coco/', pathxml, path2[:-4] + '.xml'), os.path.join('/DATA/zh_1210/yzrgb/coco/minival/', pathxml, path2[:-4] + '.xml'))
    else:
        shutil.copy(path, os.path.join('/DATA/zh_1210/yzrgb/coco/trainval/', path1 + '/'))
        shutil.copy(os.path.join('/DATA/zh_1210/yzrgb/coco/', pathxml, path2[:-4] + '.xml'), os.path.join('/DATA/zh_1210/yzrgb/coco/trainval/', pathxml, path2[:-4] + '.xml'))