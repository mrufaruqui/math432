# See the exercise "Pendulum.pdf" from Pendulum.html 
# in  http://www.physics.cornell.edu/sethna/StatMech/ComputerExercises/
#
"""Simple example animating the motion of a pendulum."""

# The "visual" module can create 3D objects (such as spheres, curves, etc.)
# and animate their motions in space.
# See www.vpython.org
from vpython import *

#from vectors import Vector as vector;
# kludge required to get visual window up and running before import scipy/numpy
scene2 = canvas()
c = cone(radius=1.0e-10)
c.visible = 0

# numpy allows us to use "array", "sin", "cos" etc.
# numpy is also imported in "visual"
from numpy import *	

# Physical properties and initial conditions for pendulum

g = 9.8
L = 1.0				# physical length of bar
d = 0.02 			# thickness of bar: needed for graphics
theta = 2.*pi/3. 		# initial upper angle (from vertical)
thetaDot = 0. 			# start pendulum at rest

# Set up graphics display

scene.title = 'Pendulum'
scene.height = scene.width = 800
pivot = vector(0,0,0) 		# pivot position of pendulum
scene.center =pivot	# graphics center

# Build a cylinder representing current position of pendulum
# Cylinder extends from bar.pos to bar.pos + bar.axis.
#
# "visual" will automagically move the image of the pendulum whenever
# one of its properties changes: we'll be moving bar.axis

bar = cylinder(pos=pivot, axis = vector(L*sin(theta),
                      -L*cos(theta),0), 
                      radius = d, color=color.red)

# The scale of the graph is set automatically by the system by default. 
# We allow it to do so for the first frame (created above when we
# constructed "bar"), but don't want it to keep rescaling as the pendulum moves

scene.autoscale = False

# visual.rate(rateWait) will pause to ensure not too many frames are drawn
# so that the graphics can keep up

framesPerSecond = 50

# Time steps for our pendulum

# Simple time stepping algorithm

dt = 0.01
t = 0.

while 1:
    # Calculate accelleration due to gravity
    thetaDotDot = -(g/L) * sin(theta)
    # Change velocity according to accelleration
    thetaDot += thetaDotDot * dt
    # Change position according to (updated) velocity
    theta += thetaDot * dt
    # Change position according to (updated) velocity
    bar.axis = vec(L*sin(theta), -L*cos(theta), 0)
    t = t+dt

    # Slow down graphics
    rate(framesPerSecond)
