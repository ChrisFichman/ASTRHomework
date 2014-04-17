from numpy import *
from matplotlib import *
from pylab import *
from math import *

x_data = []
y_data = []
z_data = []
qx_data = []
qy_data = []
qz_data = []

#open file and read out data.
with open('rays.txt') as data:
	for line in data:
		x,y,z,qx,qy,qz = line.rstrip().split(' ')
		x_data.append(float(x))
		y_data.append(float(y))
		z_data.append(float(z))
		qx_data.append(float(qx))
		qy_data.append(float(qy))
		qz_data.append(float(qz))

#Find x_avg
x_avg = float(fsum(x_data)/float(len(x_data)))
y_avg = float(fsum(y_data)/float(len(y_data)))

#Find the difference of x values and x_avg
x_diff = [x_val - x_avg for x_val in x_data]
y_diff = [y_val - y_avg for y_val in y_data]

#Truncate lists using slice
x_av_trunc = x_diff[0:25]
y_av_trunc = y_diff[0:25]

#Write truncated lists to a text file
file = open("rays_av.csv", "w")
for (x_val, y_val) in zip(x_av_trunc, y_av_trunc):
	string = (str(x_val) + "," + str(y_val) + "\n")
	file.write(string)
file.close()

#Graph a Scatter Plot and Label
scatter(x_diff, y_diff)
title("Chris Fichman - Graph of x_diff vs. y_diff")
xlabel("x-x_avg")
ylabel("y-y_avg")
show()

