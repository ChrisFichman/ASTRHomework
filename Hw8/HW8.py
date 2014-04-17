#Name: Chris Fichman
#Email: chris.fichman@gmail.com
#Assignment: Homework 7

from numpy import *
from matplotlib import *
from pylab import *
from math import *

image = zeros((1000,1000))
print "Image Shape: "+ str(image.shape)

with open('m33.dat', 'r') as data:  
    image =[[0 for x in range(1000)] for x in range(1000)]
    for i in range(1000):
        for j in range(1000):
            image[i][j] = data.readline()

print str(image)
