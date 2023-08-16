import cv2
import xml.etree.ElementTree as ET
import os

def main():
    img_path = 'Core_data/Images/G100/G100_0099/'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    anno_path = 'Mark_core/G100/G100_0099/'
    cut_path = 'Core_data/Crops/G100/G100_0099/'
    if not os.path.exists(cut_path):
        os.makedirs(cut_path)
    imagelist = os.listdir(img_path)
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        img_file = img_path + image
        img = cv2.imread(img_file)
        xml_file = anno_path + image_pre + '.xml'
        tree = ET.parse(xml_file)
        root = tree.getroot()
        obj_i = 0
        for obj in root.iter('object'):
            obj_i += 1
            print(obj_i)
            cls = obj.find('name').text
            xmlbox = obj.find('bndbox')
            b = [int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)),
                 int(float(xmlbox.find('xmax').text)),
                 int(float(xmlbox.find('ymax').text))]
            img_cut = img[b[1]:b[3], b[0]:b[2], :]
            path = os.path.join(cut_path, cls)
            mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
            mkdirlambda(path)
            try:
                cv2.imwrite(os.path.join(cut_path, cls, '{}_{:0>2d}.jpg'.format(image_pre, obj_i)), img_cut)
            except:
                continue

            print("Finish!")

if __name__ == '__main__':
    main()
