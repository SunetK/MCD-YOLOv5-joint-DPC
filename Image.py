import astropy.io.fits as fits
import matplotlib
import os
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fits_path = 'fits/synthetic_model_0000.fits'
data = fits.getdata(fits_path)
image_path = 'fits/0000'
if not os.path.exists(image_path):
    os.makedirs(image_path)

for i in range(0, 424):
    data_cut = data[i:i + 1, :, :].sum(0)
    matplotlib.image.imsave('fits/0000/'+'synthetic_model_0000_' + str(i) + '.png', data_cut)