import csv
import os
import pandas as pd

csvfile_path = 'Real_decetion/G100/3D_0099.csv'
txtfile_path = 'Real_decetion/G100/3D_0099.txt'
example = []

for line in open(txtfile_path):
    del example[:]
    a = line.split('\t')
    b0 = float(a[0])
    b1 = float(a[1])
    b2 = a[2].split('\n')[0]
    example.append(b0)
    example.append(b1)
    example.append(b2)

    with open(csvfile_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(example)

df = pd.read_csv('Real_decetion/G100/3D_0099.csv', header=None, names=['XX', 'YY', 'VV'])
df.to_csv('Real_decetion/G100/3D_0099.csv', index=False)
