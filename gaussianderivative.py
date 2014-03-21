from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('rajat.JPG'))

sigma = 5 #standard deviation
imx = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)
imy = zeros(im.shape)
filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
imshow(imx)
show()
imshow(imy)
show()