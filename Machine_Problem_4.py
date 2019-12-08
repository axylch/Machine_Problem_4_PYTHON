#Machine Problem 4 (Projectile Motion)
import numpy as np
from math import radians, cos, sin, sqrt
import matplotlib.pyplot as plt
#Input of all the components needed for calculation
height = float(input('Initial Height above Ground (meters): '))
velocity = float(input('Magnitude of the Velocity (m/s): '))
angle = float(input('Angle in Degrees with respect to the X-Axis at which the Projectile is fired: '))
xacceleration = float(input('X-Component of the Acceleration, considering the sign (m/s^2): '))
yacceleration = float(input('Y-Component of the Acceleration, considering the sign (m/s^2): '))
#Error to show no free fall and no negative height
if yacceleration == 0:
    raise NameError('NO FREE FALL')
elif height <0:
    raise NameError('The Height should be ABOVE GROUND')
#Needed calculation for the x and y trajectory
xvelocity = velocity*cos(radians(angle))
yvelocity = velocity*sin(radians(angle))
distance = sqrt(((yvelocity**2) - ((2*yacceleration)*height)))
traj1 = (-yvelocity + distance )/ yacceleration
traj2 = (-yvelocity - distance )/ yacceleration
#Kinematic Equations
if traj1 <= 0:
    traj1 = traj2
    xtrajectory = xvelocity*(np.linspace(0,traj1)) + 1/2*xacceleration*np.linspace(0,traj1)**2
    ytrajectory = height + yvelocity*np.linspace(0,traj1) + 1/2*yacceleration*np.linspace(0,traj1)**2
else:
    xtrajectory = xvelocity*(np.linspace(0,traj1)) + 1/2*xacceleration*np.linspace(0,traj1)**2
    ytrajectory = height + yvelocity*np.linspace(0,traj1) + 1/2*yacceleration*np.linspace(0,traj1)**2
#Plotting the Trajectory of the Projectile
plt.plot(xtrajectory,ytrajectory);plt.grid()
plt.title('The Traveled Path of the Projectile')
plt.xlabel('Horizontal Trajectory (X)');plt.ylabel('Vertical Trajectory (Y)')