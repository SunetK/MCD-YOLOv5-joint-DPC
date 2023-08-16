import csv
import pandas as pd

csvfile_path = 'G100/0099_G100.csv'
txtfile1_path = 'G100/real_G100_0099.txt'
txtfile2_path = 'G100/0099_G100.txt'

example = []

with open(txtfile1_path) as fp1:
    with open(txtfile2_path) as fp2:
        for line1, line2 in zip(fp1, fp2):
            del example[:]
            a = line1.split('\t')
            b = line2.split('\n')[0]

            c0 = a[0].split('_')[-1].split('.txt')[0]
            c1 = a[1]
            c2 = a[2]
            c3 = a[3]
            c4 = a[4].split('\n')[0]

            example.append(c0)
            example.append(c1)
            example.append(c2)
            example.append(c3)
            example.append(c4)
            example.append(b)

            with open(csvfile_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(example)


df = pd.read_csv('G100/0099_G100.csv', header=None, names=['Velo', 'Xmin', 'Ymin', 'Xmax', 'Ymax', 'belongsto'])
df.to_csv('G100/0099_G100.csv', index=False)
