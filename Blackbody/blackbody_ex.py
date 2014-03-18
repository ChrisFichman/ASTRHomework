"""
    semere Ghebrechristos 
    blackbody.py 
    2/13/14
    the purpose of this code is to plot a star blackbody in different 
    temperature
This is the wavelength version of blackbody enery density
"""
from pylab import *
import numpy as np
from scipy import *
import matplotlib.pyplot as plt 
import planck_fun

# constants 

h=6.626e-34         # Planck constant in Js
c=2.998e8           # speed of light in m/s
k=1.38e-23          # Boltzmann constant in J/K%
c_1 = np.pi*2.0*h*c**2        # c1 is a constant in Wm**-2

# calculation and plots 
for T in (1000,1500,2000,2500,3000) : #temperatures
    loglam=linspace(0.1,10.,250) #250 equally spaced points
    wav=loglam*10**-6         # wave length in um 
    # call planck function 
    lb = planck_fun.planck_fun(T,h,c,k,wav,c_1)
    lab=str(T)+'K' 
    hold(True)
    plt.plot(wav,lb,label=lab,markersize=2)
    plt.xlabel('wavelength (nm)')
    hold(False)
    plt.ylabel('flux emitted in W/m*m')
    plt.legend(loc='upper right')
    plt.title("Blackbody radiation")

"""
here the code is calculating the flux for different stars 
"""
class star_1:
    def __init__(self,name,T,R,d): 
        self.name = name    # name of the star 
        self.T = T          # surface temp. of the star 
        self.R = R          # radius of the star 
        self.d = d          # distance from earth
s = star_1('sun',5778,6.955e8,1.5e11)
m = star_1('mars',294.26,3390000**2,225e9)
wav = 0.0
x=list()
y=list()
y_m = list()
while wav < 500:
    wav +=5.0
    intensity = planck_fun.planck_fun(s.T,h,c,k,wav*10e-9,c_1)
    c_s = (intensity*4*np.pi*(s.R)**2)   # multi... by 4piR^2 and divi it by distance
    L = (c_s)/(4*np.pi*s.d**2)
    x.append(wav*10e-9)
    y.append(L)
    figure(2)
    plt.plot(x,y,label=s.name,markersize=10)
    plt.draw()
    plt.xlabel('wavelength (nm)')
    plt.ylabel('flux emitted in W/m*m')
    plt.title("sun flux from earth ")   
"""
# mars 
    figure(3)
    intensity_m = planck_fun.planck_fun(m.T,h,c,k,wav*10e-9,c_1)
    c_m = (intensity_m*4*np.pi*(s.R)**2)   # multi... by 4piR^2 and divi it by distance
    L_m = (c_m)/(4*np.pi*s.d**2)
    y_m.append(L_m)
    plt.title("Blackbody radiation of mars from earth distance")
    plt.plot(x,y_m,label=m.name,markersize=10)
    plt.draw()
    plt.xlabel('wavelength (nm)')
    plt.ylabel('flux emitted in W/m*m')
    plt.legend(loc='upper right')
    plt.title("mars flux from earth") 

print "The solar luminosity : ",sum(c_s),"  w"
print "The solar flux : ",sum(L),"  w/m*m"
print "The mars luminosity : ",sum(intensity_m),"  w"
print "mars flux : ",sum(L_m),"  w/m*m"
"""
show()




