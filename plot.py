import os
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

enable_3D = True



array2D = [ ]
with open('/home/areeb/vslam/src/ORB_SLAM3/CameraTrajectory(1-60).txt' , 'r') as f:
    for line in f.readlines():
        array2D.append(line.split(' '))
x_coordinates = [0]
y_coordinates = [0]
z_coordinates = [0]
for i in range (len(array2D)):

    x_coordinates.append(array2D[i][1])
    y_coordinates.append(array2D[i][2])
    z_coordinates.append(array2D[i][3])


x_coordinates = [float(x) for x in x_coordinates]
y_coordinates = [float(x) for x in y_coordinates]
z_coordinates = [float(x) for x in z_coordinates]


if enable_3D:
    plt.style.use('seaborn-poster')
    fig = plt.figure(figsize = (8,8))
    ax = plt.axes(projection='3d')
    ax.grid()
    # plt.style.use('2D- Trajectory')


    ax.plot3D(x_coordinates, y_coordinates, z_coordinates)
    ax.set_title('3D- Trajectory')

    # Set axes label
    ax.set_xlabel('x (meters)', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)
    # plt.axis('scaled')

    plt.show()

else:
    plt.plot(x_coordinates,y_coordinates)
    # fig = plt.figure(figsize = (8,8))
    ax = plt.axes()
    ax.grid()
    plt.axis('scaled')

    # # Set axes label
    ax.set_xlabel('x (meters)', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    plt.show()

