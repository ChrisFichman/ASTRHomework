#Author:Chris Fichman
#Email:chris.fichman@gmail.com
#Program Description: This program provides the method for graphing a 
#Lorenz Attractor.

#References for math: 
#	http://www.physics.emory.edu/faculty/weeks//research/tseries1.html
# 	http://mathworld.wolfram.com/LorenzAttractor.html

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

s = input("Enter value for s: ") #Prandtl Number
r = input("Enter value for r: ") #Rayleigh Number
b = input("Enter value for b: ") #Geometric Factor

s_diff = input("Enter value for s_diff: ")
r_diff = input("Enter value for r_diff: ")
b_diff = input("Enter value for b_diff: ")

s1 = s + s_diff
r1 = r + r_diff
b1 = b + b_diff

if s >= 10 or r >=28 or b >= 2.667:
	msg1 = "Unstable: s= "
else:
	msg1 = "Stable: s= "
	
if s1 >= 10 or r1 >=28 or b1 >= 2.667:
	msg2 = "Unstable: s1= "
else:
	msg2 = "Stable: s1= "
	
# Need one more for the initial values
X = empty((N + 1,))
Y = empty((N + 1,))
Z = empty((N + 1,))
X1 = empty((N + 1,))
Y1 = empty((N + 1,))
Z1 = empty((N + 1,))

# Setting initial values
X[0], Y[0], Z[0] = (0., 1., 1.05)
X1[0], Y1[0], Z1[0] = (0., 1., 1.05)

# Stepping through "time".

for i in range(N) :
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lorenz(X[i], Y[i], Z[i], s, r, b)
    X[i + 1] = X[i] + (x_dot * dt)
    Y[i + 1] = Y[i] + (y_dot * dt)
    Z[i + 1] = Z[i] + (z_dot * dt)

fig1 = figure(1)
ax = fig1.gca(projection='3d')

for i in xrange(N):
    ax.plot(X[i:i+2], Y[i:i+2], Z[i:i+2], color=cm.autumn(255*i/N))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(msg1 + str(s) + ", r=" + str(r) + ", b="+ str(b))
fig1.suptitle("Lorenz Attractor 0")


##LORENZ ATTRACTOR 2##
for i in range(N) :
    # Derivatives of the X1, Y1, Z1 state
    x_dot, y_dot, z_dot = lorenz(X1[i], Y1[i], Z1[i], s1, r1, b1)
    X1[i + 1] = X1[i] + (x_dot * dt)
    Y1[i + 1] = Y1[i] + (y_dot * dt)
    Z1[i + 1] = Z1[i] + (z_dot * dt)

fig2 = figure(2)    
bx = fig2.gca(projection='3d')

for i in xrange(N):
    bx.plot(X1[i:i+2], Y1[i:i+2], Z1[i:i+2], color=cm.autumn(255*i/N))

bx.set_xlabel("X1")
bx.set_ylabel("Y1")
bx.set_zlabel("Z1")
bx.set_title(msg2 + str(s1) + ", r1=" + str(r1) + ", b1="+ str(b1))
fig2.suptitle("Lorenz Attractor 1")


fig3 = figure(3)

x_diff, = plot(linspace(0.0, 5000.1, 5001), (X1-X)[:5001], 'r')
y_diff, = plot(linspace(0.0, 5000.1, 5001), (Y1-Y)[:5001], 'b')
z_diff, = plot(linspace(0.0, 5000.1, 5001), (Z1-Z)[:5001], 'y')
legend([x_diff,y_diff,z_diff],["X_diff", "Y_diff", "Z_diff"])
xlabel("Magnitude of difference")
ylabel("Time(milliseconds)")
fig3.suptitle("Difference in Magnitude in X, Y, and Z directions at each time step")
xlim(0,5000)

show()
