import pandas as pd

data = pd.read_csv('Real_decetion/G100/real_G100_0099.csv')

with open('Real_decetion/G100/txt/real_G100_0099.txt','a+') as f:
    for line in data.values:
        f.write((str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\t'+str(line[3])+'\t'+str(line[4])+'\n'))