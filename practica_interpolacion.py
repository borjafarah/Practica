from practica_import import *
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

points08 = np.array((lon08, lat08)).T
values08 = np.array(val08).T
grid_x08, grid_y08 = np.mgrid[-70.1477776:-70.1444949:1000j, -24.4919934:-24.4832288:1000j]

grid08_linear = interpolate.griddata(points08, values08, (grid_x08, grid_y08), method='linear')
grid08_cubic = interpolate.griddata(points08, values08, (grid_x08, grid_y08), method='cubic')
grid08_nearest = interpolate.griddata(points08, values08, (grid_x08, grid_y08), method='nearest')


plt.imshow(grid08_linear)


points09 = np.array((lon09, lat09)).T
values09 = np.array(val09).T
grid_x09, grid_y09 = np.mgrid[-70.1527946:-70.148457:1000j, -24.4922693:-24.483098:1000j]

grid09_linear = interpolate.griddata(points09, values09, (grid_x09, grid_y09), method='linear',rescale=True)
grid09_cubic = interpolate.griddata(points09, values09, (grid_x09, grid_y09), method='cubic', rescale=True)
grid09_nearest = interpolate.griddata(points09, values09, (grid_x09, grid_y09), method='nearest', rescale=True)

#plt.imshow(grid09_linear.T)
