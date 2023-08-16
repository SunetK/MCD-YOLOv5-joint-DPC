import pandas as pd

path = 'table/new/synthetic_outcat_0099.csv'
data = pd.read_csv(path, sep='\t')


with open('table/new/0099_realcen.txt', 'a+') as f:
    for line in data.values:
        f.write((str(line[4])+'\t'+str(line[5])+'\t'+(str(line[6])+'\n')))