#Name: Chris Fichman
#Email: chris.fichman@gmail.com
#Assignment: Homework 7

from numpy import *
from matplotlib import *
from pylab import *
from math import *
from scipy.ndimage import *
from astropy.io.fits import *

image = fromfile('m33.dat', dtype = int16)
image_fortran = image.reshape((1000,1000), order="FORTRAN")
image_fortran_smoothed = filters.gaussian_filter(image_fortran, 5, mode='nearest')
x_values = linspace(0.0, 12000.0, 500)

fitsfile = PrimaryHDU(data=image_fortran)
fitsfile.writeto('m33.fits',clobber=True)
data = getdata('m33.fits')

figure(1)
imshow(data)

figure(2)
imshow(image_fortran, cmap='spectral')
colorbar()

figure(3)
imshow(image_fortran, cmap='gist_heat')
colorbar()
contour(image_fortran_smoothed, levels=[3000, 6000, 9000, 12000],colors=('red','yellow','blue','white'))

y_slice = image_fortran[:,500]
x_slice = image_fortran[500,:]

figure(4)
plot(y_slice, 'b')
plot(x_slice, 'r')

print 'Max brightness = 13500'
print 'Location = 817, 412'

print 'Average Brigness at center = ~11000'

show()
