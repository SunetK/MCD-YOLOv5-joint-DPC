import numpy as np
import astropy.io.fits as fits
import pandas as pd

path = 'Real_decetion/G100/3D_0099.csv'
data = pd.read_csv(path)
intensity = r'FITS/synthetic_model_0099.fits'
intensity_data = fits.getdata(intensity)
cen = []

Cen_X = list(data['XX'])
Cen_Y = list(data['YY'])
Cen_Z = list(data['VV'])

for i in range(0, len(Cen_X)):
    CEN_P = intensity_data[int(Cen_Z[i]) : int(Cen_Z[i]) + 1, int(Cen_Y[i]) : int(Cen_Y[i] + 1) ,
            int(Cen_X[i]) : int(Cen_X[i] + 1)]

    cen.append(Cen_X[i])
    cen.append(Cen_Y[i])
    cen.append(Cen_Z[i])
    cen.append(CEN_P[0][0][0])

arr = np.array(cen).reshape(-1, 4)
np.savetxt("Real_decetion/G100/txt/G100_3D_0099_CenStrong.txt", arr, fmt = '%s')
