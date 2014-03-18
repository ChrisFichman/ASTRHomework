import math 
import numpy as np
from scipy import *
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from pylab import *
def planck_fun(T,h,c,k,wav,c_1): # lamda is mu*m , T is temperature (K)
# INPUT
		# wavelength= the observing wave (in um) 
		# kB= the Boltzmann constant (in J/K) 
		# T = the temperature (in K) 
		# c =the speed of light (in m/s) and 
		# h = the Planck constant (in JS) 
# OUTput
		# the intensity of radiation emitted by a black body 	
# calculations 
	c_2 = h*c/(T*k*wav)        	# c2 is a constant in m*k 
	# planck function in W(m**-2)*mum**-1 
	intensity = c_1/((wav**5)*(np.exp(c_2)-1))    # planck equation
	return intensity   # return value








	 
