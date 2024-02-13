import numpy as np
import matplotlib.pyplot as plt

k = 8.9875517873681764

q1 = 1
q2 = 1
q3 = 1
r1 = np.array([-1, 0]) 
r2 = np.array([0, 0]) 
r3 = np.array([1, 0])

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

Ex = k * (q1 * (X - r1[0]) / ((X - r1[0])**2 + (Y - r1[1])**2)**(3/2) + q2 * (X - r2[0]) / ((X - r2[0])**2 + (Y - r2[1])**2)**(3/2)) + q3 * (x - r3[0]) / ((X - r3[0])**2 + (Y - r3[1])**2)**(3/2)


Ey = k * (q1 * (Y - r1[1]) / ((X - r1[0])**2 + (Y - r1[1])**2)**(3/2) + q2 * (Y - r2[1]) / ((X - r2[0])**2 + (Y - r2[1])**2)**(3/2)) + q3 * (Y - r3[1]) / ((X - r3[0])**2 + (Y - r3[1])**2)**(3/2)

plt.streamplot(X, Y, Ex, Ey, color='b', linewidth=0.5, density=6)
plt.scatter([r1[0], r2[0], r3[0]], [r1[1], r2[1], r3[1]], c=['red', 'red', 'red'], s=100, label=['q1', 'q2', 'q3'])
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
