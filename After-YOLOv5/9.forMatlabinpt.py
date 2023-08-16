import pandas as pd

data = pd.read_csv('Real_decetion/G100/centroid_data_0099.csv')
with open('Real_decetion/G100/3D_0099.txt','a+') as f:
    for line in data.values:
        f.write((str(line[1])+'\t'+str(line[2])+'\t'+(str(line[0].split('_')[-1])+'\n')))
