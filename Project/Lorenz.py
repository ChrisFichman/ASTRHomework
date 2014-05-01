#Author:Chris Fichman
#Email:chris.fichman@gmail.com
#Program Description: This program provides the method for graphing a 
#Lorenz Attractor.

from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s, r, b) :
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot
    
dt = 0.01
N = 10000

s = input("Enter value for s: ")
r = input("Enter value for r: ")
b = input("Enter value for b: ")

if s >= 10 or r >=28 or b >= 2.667:
	msg = "Unstable Atmospheric Convection for s= "
else:
	msg = "Stable Atmospheric Convection for s= "
	
# Need one more for the initial values
X = empty((N + 1,))
Y = empty((N + 1,))
Z = empty((N + 1,))

# Setting initial values
X[0], Y[0], Z[0] = (0., 1., 1.05)

# Stepping through "time".

for i in range(N) :
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lorenz(X[i], Y[i], Z[i], s, r, b)
    X[i + 1] = X[i] + (x_dot * dt)
    Y[i + 1] = Y[i] + (y_dot * dt)
    Z[i + 1] = Z[i] + (z_dot * dt)

fig = figure()
ax = fig.gca(projection='3d')

for i in xrange(N):
    ax.plot(X[i:i+2], Y[i:i+2], Z[i:i+2], color=cm.RdYlBu(255*i/N))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(msg + str(s) + ", r=" + str(r) + ", b="+ str(b))

show()
