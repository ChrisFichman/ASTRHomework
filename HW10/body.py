#File: body.py
#Name: Chris Fichman
#Email: chris.fichman@gmail.com

from numpy import *
from matplotlib.pyplot import *

wavelength = linspace(0.0, 2000.0, 1001)
h = 6.6260693e-34
c = 2.99792458e8
k = 1.380658e-23
const_1 = 2*h*c**2
wav = wavelength*10**-9

class Body:
	name = ""
	temp = float(0)
	radius = float(0)
	distance = float(0)
	def __init__(self, name, temp, radius, distance, color, plot=None):
		self.name = name
		self.temp = temp
		self.radius = radius
		self.distance = distance
		self.color = color
		self.plot = plot

def calc_and_plot(body, ax):
	T = body.temp
	intensity = empty([120, 1])
	const_2 = h*c/(T*k*wav)
	intensity = const_1/((wav**5)*(exp(const_2)-1))          #Blackbody
	plot, = ax.plot(wavelength, intensity, body.color, label = str(body.name))
	body.plot = plot,
	
def new_body(name, temp, radius, distance, color):
	body = Body(name, temp, radius, distance, color)
	return body

def print_all(body):
	print "Name: " + str(body.name)
	print "Temp: " + str(body.temp) + " K"
	print "Radius: " + str(body.radius) + " m"
	print "Distance: " + str(body.distance) + " pc"
	print "Color: " + str(body.color)
