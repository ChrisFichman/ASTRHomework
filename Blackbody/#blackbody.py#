#File: blackbody.py
#Author: Chris Fichman
#Email: chris.fichman@gmail.com

from numpy import *
from matplotlib.pyplot import *
from body import *

b1 = new_body("Alpha Centauri A", 5790, 6.955e8*1.227, 1.339, 'y--')
b2 = new_body("Sun", 5778, 6.955e8, 0, 'y')
b3 = new_body("Mira", 3000, 6.955e8*380, 90, 'r')
b4 = new_body("Polaris", 6000, 6.955e8*46, 100, 'w')
b5 = new_body("Arcturus", 4290, 6.955e8*25, 11, '#FF7D40')

ax = subplot(1,1,1, axisbg = 'black')

calc_and_plot(b1,ax)
calc_and_plot(b2,ax)
calc_and_plot(b3,ax)
calc_and_plot(b4,ax)
calc_and_plot(b5,ax)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set_title("Blackbody Diagrams")
ax.set_xlabel("Wavelength(nm)")
ax.set_ylabel("Intensity(W/m^2)")

show()
