from numpy import *
from matplotlib import *
from pylab import *
from math import *

x_data = []
y_data = []

#open file and read out data.
with open('rays.txt') as data:
	for line in data:
		x,y = line.rstrip().split(' ')
		x_data.append(float(x))
		y_data.append(float(y))

#Find x_avg
x_avg = float(fsum(x_data)/float(len(x_data)))
y_avg = float(fsum(y_data)/float(len(y_data)))

#Find the difference of x values and x_avg
x_diff = [x_val - x_avg for x_val in x_data]
y_diff = [y_val - y_avg for y_val in y_data]

#Graph a Scatter Plot and Label
scatter(x_data, y_data)
plot(A,x, "b")
plot(B,x, "r")
plot(r,x, "g")
title("Chris Fichman - Correllation of x vs. y")
xlabel("x")
ylabel("y")
label(str(conf))
show()

