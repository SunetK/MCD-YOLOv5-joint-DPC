import csv
import pandas as pd

csvfile_path = 'Real_decetion/G100/centroid_data_0099.csv'
txtfile1_path = 'detection-results/G100/G100_0099/G100_0099.txt'
txtfile2_path = 'Core_data/Crops/G100/G100_0099.txt'
example = []

with open(txtfile1_path) as fp1:
    with open(txtfile2_path) as fp2:
        for line1, line2 in zip(fp1, fp2):
            del example[:]
            a = line1.split('\t')
            b = line2.split('\n')[0].split(' ')
            c1 = int(a[1]) + int(b[1])
            c2 = int(a[2]) + int(b[2])
            c3 = a[0].split('.txt')[0]
            example.append(c3)
            example.append(c1)
            example.append(c2)

            with open(csvfile_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(example)

df = pd.read_csv('Real_decetion/G100/centroid_data_0099.csv', header=None, names=['name', 'X', 'Y'])
df.to_csv('Real_decetion/G100/centroid_data_0099.csv', index=False)
