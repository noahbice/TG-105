import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections

def get_new_point(point, mu=1.0):
	distance = - np.log(1 - np.random.random()) /  mu
	direction = np.random.random()*2*np.pi
	delta_x = distance*np.cos(direction)
	delta_y = distance*np.sin(direction)
	new_position = (point[0] + delta_x, point[1] + delta_y)
	return new_position

#----------------------------
num_students = 30
radius = 10.
point = (0,0)
pause = 0.3
mu = 1.0
#----------------------------

interval = 2*np.pi / num_students
angles = [0.]
val = 0.
for _ in range(num_students - 1):
	val += interval
	angles.append(val)
angles = np.array(angles)
chars = angles + (interval/2)
marker_x = radius*np.cos(angles)
marker_y = radius*np.sin(angles)
char_x = radius*1.2*np.cos(chars)
char_y = radius*1.2*np.sin(chars)
texts = np.linspace(1, num_students, num_students).astype('int')

theta = np.linspace(0,2*np.pi, 100)
displacement = 0.
lines = []
fig, ax = plt.subplots()
ax.plot(radius*np.cos(theta),radius*np.sin(theta), c="black")
ax.scatter(marker_x,marker_y, c="black", marker="*")
for i in range(num_students):
	plt.text(char_x[i], char_y[i], str(texts[i]))
ax.set_title("Student picker")
plt.axis('off')
while displacement < radius:
	new_point = get_new_point(point, mu=mu)
	displacement = np.sqrt(new_point[0]**2 + new_point[1]**2)
	lines.append([point, new_point])
	point = new_point
	col = collections.LineCollection(lines)
	ax.add_collection(col)
	plt.draw()
	plt.pause(pause)
plt.show()
