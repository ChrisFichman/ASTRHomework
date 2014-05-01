import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage


## read in image from unformatted file
data = np.fromfile('m33.dat', dtype=np.int16)
data_fortran = data.reshape((1000,1000),order="FORTRAN")

#let's look at it!
plt.figure(1)
plt.imshow(data_fortran)
plt.colorbar()


# 5 is basically the number of pixels you will smooth by.  Can do 2, or 20, or whatever.
data_fortran_smoothed = scipy.ndimage.filters.gaussian_filter(data_fortran, 5, mode='nearest')
plt.figure(2)
plt.imshow(data_fortran_smoothed)
plt.colorbar()  ## this is to help you figure out what level to make your contours!!

## color image with black contours
plt.figure(3)
plt.imshow(data_fortran)
plt.colorbar()
plt.contour(data_fortran_smoothed,levels=[3000,5000,7000,9000,11000],colors='black')

## greyscale image with rainbow contours
plt.figure(4)
plt.imshow(data_fortran,cmap='gist_gray')
plt.colorbar()
plt.contour(data_fortran_smoothed,levels=[3000,5000,7000,9000,11000])

## The possibilities are endless!


## let's write this image (data_fortran) to a fits file!  We don't have a header
## but that's okay
fitsfile = pyfits.PrimaryHDU(data=data_fortran)
fitsfile.writeto('m33.fits',clobber=True)

## neat! can look at this in ds9 if you have it.
## get it here: http://ds9.si.edu/site/Download.html

## now let's read it back in!!
HDU = pyfits.open('m33.fits')
data = HDU[0].data
header = HDU[0].header  ## but we don't actually have a header
# alternatively
data = pyfits.getdata('m33.fits')
header = pyfits.getheader('m33.fits')  ## but we don't actually have a header

plt.figure(5)
plt.imshow(data)  # yep, it works


### SOMETHING REALLY COOL.  WANNA PUT COORDINATES (RA, DEC) ON THIS IMAGE???
## go to http://nova.astrometry.net/upload and upload "m33.fits" and wait for
## the result (give it a minute, then click "go to results" and download
## "new-image.fits")




### THE EAGLE NEBULA -- PILLARS OF CREATION ###
### Download the 3 fits files from this website
### http://www.spacetelescope.org/projects/fits_liberator/eagledata/

SII_R = pyfits.getdata('673nmos.fits')
Ha_V = pyfits.getdata('656nmos.fits')
OIII_B = pyfits.getdata('502nmos.fits')

### can also take a look at the headers if you want, they store lots
### of info, include RA/DEC coordinates for the image
### See the CTYPE,CRVAL,CRPIX,CD keywords
SII_R_header = pyfits.getheader('673nmos.fits')

## set parts of the image = 0 to NaN's so they get plotted as white
zeros = np.where(SII_R == 0)
SII_R[zeros] = np.nan
zeros = np.where(Ha_V == 0)
Ha_V[zeros] = np.nan
zeros = np.where(OIII_B == 0)
OIII_B[zeros]=np.nan

## Creating a RGB color image -- doesn't turn out too great
## You could fiddle with the parameters to get it to look nicer
## Each colormap can be inverted by tacking on a "_r" to the end
## of its name.  Colormaps found at 
## http://matplotlib.org/examples/color/colormaps_reference.html
## vmin & vmax scale your colorbar
## alpha=0 means transparent, alpha=1 means opaque (default), in between
## allows me to overplot these images
plt.figure(6)
imG = plt.imshow(Ha_V,cmap='Greens_r',vmin=50,vmax=300,alpha=0.3)
imB = plt.imshow(OIII_B,cmap='Blues_r',vmin=4,vmax=18,alpha=0.4)
imR = plt.imshow(SII_R,cmap='Reds_r',vmin=7,vmax=100,alpha=0.3)

plt.colorbar()  ## I don't know how to make it show all 3 colorbars
plt.show()

## Alternative method (THE BEST METHOD) -- need the module "aplpy"
##   -- tutorial: http://aplpy.readthedocs.org/en/latest/quickstart.html
import aplpy
imG = aplpy.FITSFigure('656nmos.fits')
imG.show_grayscale()  ## note how it does the scaling for you! very awesome

## could also do a colorscale
imG.show_colorscale()  ## the colorscale can be changed from default
                       ## default is ugly

## can also show contours
imG = aplpy.FITSFigure('656nmos.fits')
imG.show_grayscale() 
imG.show_contour('656nmos.fits',colors='red',levels=3) ## levels=3 --> 3 contour levels  
                                  ## so this call means that you are applying
                                  ## contours from '656nmos.fits' to imG, meaning
                                  ## you can pull contours from another image!
## example of this:
imG = aplpy.FITSFigure('656nmos.fits')
imG.show_grayscale()
imG.show_contour('m33.fits')  ## m33.fits doesn't have any RA/DEC info,
                              ## so it just overlays the contours in pixel space
                              ## but it overlay contours in RA/DEC space!
