import os
from xml.etree.ElementTree import SubElement

def prettyXml(element, indent, newline, level = 0):
    if element:
        if element.text == None or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)

    temp = list(element) 
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level = level + 1)

def nff(_list):
    for i in range(len(_list)):
        if int(_list[i]) < 0:
            _list[i] = 0

def gen_maxin_data(name):
    import pandas as pd
    import re
    path = name
    data = pd.read_csv(path)
    Name = list(data['name'])
    Xmin = list(data['Xmin'])
    Ymin = list(data['Ymin'])
    Xmax = list(data['Xmax'])
    Ymax = list(data['Ymax'])
    return (Name, Xmin, Ymin, Xmax, Ymax)

def write_xml_(data):
    import xml.etree.ElementTree as ET
    from xml.etree.ElementTree import Element
    for j in range(len(data[0])): # 行
        path = 'Mark_core/G100/G100_0099/'
        if not os.path.exists(path):
            os.makedirs(path)

        write_name = f"Mark_core/G100/G100_0099/{data[0][j].split('.txt')[0]}.xml"
        if os.path.isfile(write_name):
            tree =ET.parse(write_name)
            root = tree.getroot()
        else:
            root = Element('annotation')
            tree = ET.ElementTree(root)
        print(write_name)

        object1 = SubElement(root, 'object')
        name = SubElement(object1, 'name')
        name.text = 'core'
        pose = SubElement(object1, 'pose')
        pose.text = 'Unspecified'
        truncated = SubElement(object1, 'truncated')
        truncated.text = '0'
        difficult = SubElement(object1, 'difficult')
        difficult.text = '0'
        bndbox = SubElement(object1, 'bndbox')
        xmin = SubElement(bndbox, 'xmin')
        xmin.text = str(data[1][j])
        ymin = SubElement(bndbox, 'ymin')
        ymin.text = str(data[2][j])
        xmax = SubElement(bndbox, 'xmax')
        xmax.text = str(data[3][j])
        ymax = SubElement(bndbox, 'ymax')
        ymax.text = str(data[4][j])
        prettyXml(root, '\t', '\n')

        tree.write(write_name, encoding='utf-8')

if __name__ == "__main__": 
    csv_name = r'detection-results/G100/G100_0099/G100_0099.csv'
    data = gen_maxin_data(csv_name)
    print(data)
    write_xml_(data)
