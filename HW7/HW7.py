#Name: Chris Fichman
#Email: chris.fichman@gmail.com
#Assignment: Homework 7

from numpy import *
from matplotlib import *
from pylab import *
from math import *

#open file and read out data into two arrays.
x_data, y_data = loadtxt('correl.txt', delimiter = ',', unpack=True )

#Find x_avg
x_avg = fsum(x_data)/len(x_data)
y_avg = fsum(y_data)/len(y_data)

#Find the difference between data and average
x_diff = x_data-x_avg
y_diff = y_data-y_avg

denom = len(x_data)*fsum(x_data*x_data)-fsum(x_data)**2
A = (fsum(x_data*x_data)*fsum(y_data) - fsum(x_data)*fsum(x_data*y_data))/denom
B = (len(y_data)*fsum(x_data*y_data)-fsum(x_data)*fsum(y_data))/denom
r = fsum(x_diff*y_diff)/sqrt(fsum(x_diff**2)*fsum(y_diff**2))

best_fit = B*x_data + A

#Graph a Scatter Plot and Label
scatter(x_data, y_data)
p1, = plot(x_data,best_fit, "r")
title("Chris Fichman - Correllation of x vs. y")
xlabel("x")
ylabel("y")
legend([p1],['Correlation Coefficient:' + str(r)])
print('Confidence in correlation is 100% because the coefficient is > 0.35, and there are 100 datapoints.')
show()

