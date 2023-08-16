import csv
import os
import pandas as pd

csvfile_path = 'detection-results/G100/G100_0099/G100_0099.csv'
txtfile_path = 'detection-results/G100/G100_0099/labels/'
example = []

txt_names = os.listdir(txtfile_path)
txt_names.sort(key=lambda x:int(x.split('.')[0].split('_')[-1]))
for txt_name in txt_names:
    txt_path = os.path.join(txtfile_path, txt_name)

    for line in open(txt_path):
        del example[:]
        a = line.split(' ')
        b1 = int(a[2]) 
        b2 = int(a[3])
        b3 = int(a[4])
        b4 = int(a[5])
        example.append(txt_name.split('.txt')[0])
        example.append(b1)
        example.append(b2)
        example.append(b3)
        example.append(b4)

        with open(csvfile_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(example)

df = pd.read_csv('detection-results/G100/G100_0099/G100_0099.csv', header=None, names=['name', 'Xmin', 'Ymin', 'Xmax', 'Ymax'])
df.to_csv('detection-results/G100/G100_0099/G100_0099.csv', index=False)

