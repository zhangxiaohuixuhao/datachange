'''
根据xml文件判断每一类标签有多少个目标
'''
from lxml import etree as ET
import glob
count1 = 0;
count2 = 0;
count3 = 0;
for xml in glob.glob('xml/*.xml'):
	tree = ET.parse(xml);
	root = tree.getroot();
	for obj in root.iter('object'):
		if obj[0].text == 'backpack':
			count1 = count1 + 1;
		elif obj[0].text == 'handbag':
			count2 = count2 + 1;
		elif obj[0].text == 'suitcase':
			count3 = count3 + 1;
			
print('Backpack: {}\nHandbag: {}\nSuitcase: {}'.format(count1, count2, count3))
