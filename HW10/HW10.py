#File: HW10.py
#Name: Chris Fichman
#Email: chris.fichman@gmail.com

from numpy import *
from matplotlib import *
from pylab import *
from math import *
from body import *

angstroms, counts = loadtxt('correl.txt', delimiter = ',', unpack=True)


ax = subplot(1,1,1, axisbg = 'black')

ax.data = plot(angstroms*100, counts*1e11, 'g', label = "Data from File")
b1 = new_body("T=5440(Blackbody)", 5440, 1, 1, 'b')

calc_and_plot(b1,ax)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_title("Blackbody Diagram")
ax.set_xlabel("Wavelength(nm)")
ax.set_ylabel("Intensity(W/m^2)")

show()
