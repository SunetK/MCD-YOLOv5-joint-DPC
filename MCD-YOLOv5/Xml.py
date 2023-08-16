import os
import pandas as pd
import csv

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET


def prettyXml(element, indent, newline, level=0):
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
        prettyXml(subelement, indent, newline, level=level + 1)

def nff(_list):
    for i in range(len(_list)):
        if int(_list[i]) < 0:
            _list[i] = 0

def gen_maxin_data(name):
    path = name
    data = pd.read_csv(path, sep='\t')
    Cen1 = list(data['Cen1'])
    Cen2 = list(data['Cen2'])
    Cen3 = list(data['Cen3'])
    Size1 = list(data['Size1'])
    Size2 = list(data['Size2'])
    Size3 = list(data['Size3'])
    Xmin = [round(Cen1[i] - Size1[i]) for i in range(len(Cen1))]
    Xmax = [round(Cen1[i] + Size1[i]) for i in range(len(Cen1))]
    Ymin = [round(Cen2[i] - Size2[i]) for i in range(len(Cen2))]
    Ymax = [round(Cen2[i] + Size2[i]) for i in range(len(Cen2))]
    _min = [int(Cen3[i] - Size3[i]+1) for i in range(len(Cen3))]
    nff(_min)
    _max = [int(Cen3[i] + Size3[i]) for i in range(len(Cen3))]
    nff(_max)
    return (Xmin, Xmax, Ymin, Ymax, _min, _max)

def write_xml(data):
    for i in range(len(data[0])):
        for j in range(data[4][i], data[5][i] + 1):
            xml_path = 'fits/0000'
            if not os.path.exists(xml_path):
                os.makedirs(xml_path)
            write_name = f"fits/0000/synthetic_model_0000_{j}.xml"
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
            xmin.text = str(data[0][i])
            ymin = SubElement(bndbox, 'ymin')
            ymin.text = str(data[2][i])
            xmax = SubElement(bndbox, 'xmax')
            xmax.text = str(data[1][i])
            ymax = SubElement(bndbox, 'ymax')
            ymax.text = str(data[3][i])
            prettyXml(root, '\t', '\n')

            tree.write(write_name, encoding='utf-8')

if __name__ == "__main__":
    csv_name = r"fits/synthetic_outcat_0000.csv"
    data = gen_maxin_data(csv_name)
    write_xml(data)
