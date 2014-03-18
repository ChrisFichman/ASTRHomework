#File: body.py
#Name: Chris Fichman
#Email: chris.fichman@gmail.com

from numpy import *
from matplotlib.pyplot import *

wavelength = arange(0., 3000., 10.)
h = 6.6260693e-34
c = 2.99792458e8
k = 1.380658e-25
const_1 = pi*2*h*c**2
wavelength = wavelength*10**-6

class Body:
	name = ""
	temp = float(0)
	radius = float(0)
	distance = float(0)
	def __init__(self, name, temp, radius, distance):
		self.name = name
		self.temp = temp
		self.radius = radius
		self.distance = distance

def calc_and_graph(body):
	T = body.temp
	L = empty([120, 1])
	const_2 = h*c/(T*k*wavelength)
	L = const_1/((wavelength**5)*exp(const_2)-1)          #Blackbody
	plot(wavelength, L, 'b')
	show()

def new_body(name, temp, radius, distance):
	body = Body(name, temp, radius, distance)
	return body

def print_all(body):
	print "Name: " + str(body.name)
	print "Temp: " + str(body.temp) + " K"
	print "Radius: " + str(body.radius) + " m"
	print "Distance: " + str(body.distance) + " pc"
